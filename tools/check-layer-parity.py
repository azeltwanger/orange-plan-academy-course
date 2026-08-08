#!/usr/bin/env python3
"""Catch a layer teaching something another layer has already replaced.

This is the failure mode this repo actually has. Three review rounds in a row
found the same shape and each time a human found it by reading:

  - 2.3 existed in three materially different versions at once. The master
    taught the retired timeframe table AND the rule that replaced it.
  - A7.4's master refused to give the number its own script gives, which is the
    exact substitution AUSTIN-AUTHORITY records as reverted.
  - The "which modules are US-shaped" breakdown lives only in the 0.1 script.

None of the existing four gates can see any of that. check-crossrefs validates
lesson *numbers*, course-metrics validates *counts*, check-visuals validates
*filenames*, build-scripts validates *protection*. Nothing validated what the
layers actually SAY. This does.

Three checks:

  COVERAGE   a master lesson with no script or no lesson-text
  CLAIMS     per CLAIM-REGISTRY.md. A MUST rule names a lesson and the layers
             that must EACH carry the claim independently — master, script,
             lesson-text, module — and every one is resolved and checked on its
             own. The first version of this check passed if the claim appeared
             anywhere in a filename-substring scope, which meant a claim could
             disappear from the master and still pass; worse, those scopes never
             matched the master filename at all. A MUST NOT rule fails wherever
             the retired phrasing resurfaces.
  BEATS      a lesson closing beat present in some layers but not others

Matching runs on NORMALISED text: markdown emphasis stripped, whitespace
collapsed. Otherwise `between **10 and 20% LTV**` in the master and the plain
form in the script read as a mismatch when the layers actually agree.

Exit 1 on any failure. Coverage notes and deliberate beat exemptions are
reported but do not fail.

  python3 tools/check-layer-parity.py
  python3 tools/check-layer-parity.py -v    # also list what passed
"""
import os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERBOSE = '-v' in sys.argv

# Files that quote retired positions on purpose. Scanning them would report the
# record itself as a regression, which is how you end up deleting the evidence.
HISTORICAL = {'AUTHORITY-FLAGS.md', 'COURSE-IMPROVEMENT-ANALYSIS.md',
              'FILMING-CHECKLIST.md', 'HANDOFF.md', 'CLAIM-REGISTRY.md',
              'ALL-SCRIPTS.md', 'AI-FACTS.md', 'LEGAL-REVIEW-PACKET.md',
              'COLLEGE-FUNDING-AUTHORITY.md', 'SOURCE-MATERIAL-POLICY.md',
              'AUSTIN-AUTHORITY.md', 'COURSE-LEGAL-COPY.md', 'README.md',
              'PRODUCTION-CHECKLIST.md', 'FILM-ORDER.md', 'DICTATION-ORDER.md',
              'SCREEN-SHOOT-LIST.md', 'USABILITY-TEST-M1-M3.md',
              'FAQ-AND-AI-BACKLOG.md', 'VOICE-GUIDE.md'}

core = open(os.path.join(root, 'MASTER-COURSE.md'), encoding='utf-8').read()
adv = open(os.path.join(root, 'MASTER-ADVANCED.md'), encoding='utf-8').read()

fails, notes, passed = [], [], []
DUPES = []      # a lesson appearing in more than one generated module file


# --- the layer map ----------------------------------------------------------
def stem(num):
    mod, sub = num.split('.', 1)
    return f'{mod}-{sub}' if mod.startswith('A') else f'{int(mod):02d}-{sub}'


def find(d, num):
    """The file serving this lesson, including a sheet shared with another."""
    p = os.path.join(root, d)
    if not os.path.isdir(p):
        return None
    s = stem(num)
    for f in sorted(os.listdir(p)):
        if f.split('_')[0].removesuffix('-A') == s:
            return os.path.join(d, f)
    # A capture sheet can cover two lessons and is named for the first: Module 1
    # is filmed once and cut in two, so 1.5 is served by the 1.4 sheet.
    for f in sorted(os.listdir(p)):
        if 'WALKTHROUGH' not in f and 'DEMO' not in f:
            continue
        h1 = open(os.path.join(p, f), encoding='utf-8').read().split('\n', 1)[0]
        if num in re.findall(r'A?\d+\.\d+', h1.split('·')[0]):
            return os.path.join(d, f)
    return None


def sections(text):
    ms = list(re.finditer(r'^## (A?\d+\.\d+) (.+)$', text, re.M))
    for i, m in enumerate(ms):
        e = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        yield m.group(1), m.group(2), text[m.start():e]


def norm(s):
    """Markdown emphasis and line wrapping are formatting, not meaning."""
    s = s.replace('**', '').replace('`', '')
    s = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'\1', s)
    return re.sub(r'\s+', ' ', s)


def master_section(num):
    src = adv if num.startswith('A') else core
    m = re.search(rf'^## {re.escape(num)} ', src, re.M)
    if not m:
        return None
    nxt = re.search(r'\n#{1,2} (?:A?\d+\.\d+|Unit |Advanced Module )', src[m.end():])
    return src[m.start():m.end() + nxt.start()] if nxt else src[m.start():]


def module_section(num):
    """modules/ is GENERATED, and checking it independently is the point: the
    build-module-gates-before-split-modules ordering bug leaves it stale while
    every hand-edited layer is correct."""
    d = 'modules/advanced' if num.startswith('A') else 'modules'
    p = os.path.join(root, d)
    if not os.path.isdir(p):
        return None
    found = []
    for f in sorted(x for x in os.listdir(p) if x.endswith('.md')):
        t = open(os.path.join(p, f), encoding='utf-8').read()
        m = re.search(rf'^## {re.escape(num)} ', t, re.M)
        if m:
            nxt = re.search(r'\n#{1,2} (?:A?\d+\.\d+|Unit |Advanced Module )', t[m.end():])
            found.append((f, t[m.start():m.end() + nxt.start()] if nxt else t[m.start():]))
    if len(found) > 1:
        # Two generated files claiming the same lesson means a stale copy from a
        # rename is still in the tree. Reading "the first one" would silently pick
        # whichever sorts earlier, which is how the pre-revert A3.1 survived.
        DUPES.append((num, [f for f, _ in found]))
    return found[0][1] if found else None


def layer_text(num, layer):
    """The text of ONE layer for ONE lesson, or None if that layer has no file."""
    a = num.startswith('A')
    if layer == 'master':
        return master_section(num)
    if layer == 'module':
        return module_section(num)
    d = {'script': 'scripts/advanced' if a else 'scripts',
         'lesson-text': 'lesson-text/advanced' if a else 'lesson-text'}[layer]
    f = find(d, num)
    return open(os.path.join(root, f), encoding='utf-8').read() if f else None


LESSONS = []          # (num, title, master_section, is_advanced)
for src, is_adv in ((core, False), (adv, True)):
    for num, title, seg in sections(src):
        LESSONS.append((num, title, seg, is_adv))


# --- CHECK 1: coverage ------------------------------------------------------
for num, title, seg, is_adv in LESSONS:
    sd = 'scripts/advanced' if is_adv else 'scripts'
    ld = 'lesson-text/advanced' if is_adv else 'lesson-text'
    for layer, d in (('script', sd), ('lesson-text', ld)):
        if not find(d, num):
            fails.append(('COVERAGE', f'{num} {title[:44]}', f'no {layer} in {d}/'))
if VERBOSE:
    passed.append(f'coverage: {len(LESSONS)} lessons, every one has a script and lesson text')


# --- CHECK 2: the claim registry --------------------------------------------
def parse_registry():
    """Rows out of the two markdown tables in CLAIM-REGISTRY.md."""
    t = open(os.path.join(root, 'CLAIM-REGISTRY.md'), encoding='utf-8').read()
    out = []
    for kind, header in (('MUST', '## MUST — '), ('MUST NOT', '## MUST NOT — ')):
        if header not in t:
            continue
        block = t.split(header, 1)[1].split('\n## ', 1)[0]
        for line in block.split('\n'):
            if not line.startswith('|') or line.startswith('|---') or '| id |' in line:
                continue
            # Patterns are regexes and contain alternation, which in a markdown
            # table has to be written `\|` or it splits the row. Split on
            # unescaped pipes only, then unescape.
            cells = [c.strip().replace('\\|', '|')
                     for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]
            if len(cells) < 3:
                continue
            if kind == 'MUST':
                # id | lesson | pattern | layers | why
                if len(cells) < 4:
                    continue
                out.append((kind, cells[0], cells[1].strip('`'), cells[2].strip('`'),
                            [x.strip() for x in cells[3].split(',') if x.strip()]))
            else:
                # id | pattern | scope | unless | why
                cid, pat, scope = cells[0], cells[1].strip('`'), cells[2].strip('`')
                unless = cells[3].strip('`') if len(cells) > 4 else ''
                out.append((kind, cid, pat, scope, unless))
    return out


REGISTRY = parse_registry()
if not REGISTRY:
    fails.append(('CLAIMS', 'CLAIM-REGISTRY.md', 'no rows parsed — the gate is not enforcing anything'))

SCAN = []
for d in ('.', 'scripts', 'scripts/advanced', 'lesson-text', 'lesson-text/advanced',
          'modules', 'modules/advanced'):
    p = os.path.join(root, d)
    if not os.path.isdir(p):
        continue
    for f in sorted(os.listdir(p)):
        if f.endswith('.md') and f not in HISTORICAL:
            SCAN.append(os.path.join(d, f))

for row in REGISTRY:
    kind = row[0]
    if kind == 'MUST':
        _, cid, lesson, pat, layers = row
        try:
            rx = re.compile(pat)
        except re.error as e:
            fails.append(('CLAIMS', cid, f'bad pattern: {e}'))
            continue
        if lesson.startswith('file:'):
            fn = lesson.split(':', 1)[1]
            fp = os.path.join(root, fn)
            if not os.path.exists(fp):
                fails.append(('CLAIMS', cid, f'{fn} does not exist'))
            elif not rx.search(norm(open(fp, encoding='utf-8').read())):
                fails.append(('CLAIMS', cid, f'MUST be present in {fn} — absent'))
            elif VERBOSE:
                passed.append(f'claim {cid}: present in {fn}')
            continue
        if not layers:
            fails.append(('CLAIMS', cid, 'no layers listed — the rule enforces nothing'))
            continue
        # Each layer is resolved and checked on its own. This is the whole point:
        # "present somewhere" is not parity.
        results = []
        for layer in layers:
            txt = layer_text(lesson, layer)
            if txt is None:
                results.append((layer, 'NO LAYER'))
            else:
                results.append((layer, 'PASS' if rx.search(norm(txt)) else 'FAIL'))
        bad = [l for l, r in results if r != 'PASS']
        if bad:
            detail = ' · '.join(f'{l}: {r}' for l, r in results)
            fails.append(('CLAIMS', f'{cid} ({lesson})',
                          f'MUST be present in every listed layer — {detail}'))
        elif VERBOSE:
            passed.append(f'claim {cid} ({lesson}): '
                          + ' · '.join(f'{l}: PASS' for l, _ in results))
    else:
        _, cid, pat, scope, unless = row
        try:
            rx = re.compile(pat)
        except re.error as e:
            fails.append(('CLAIMS', cid, f'bad pattern: {e}'))
            continue
        files = [f for f in SCAN if scope in f] if scope else SCAN
        if not files:
            fails.append(('CLAIMS', cid, f'scope "{scope}" matches no file — rule is dead'))
            continue
        hits = []
        for rel in files:
            raw = open(os.path.join(root, rel), encoding='utf-8').read()
            seen_line = False
            for ln, line in enumerate(raw.split('\n'), 1):
                n = norm(line)
                if rx.search(n) and not (unless and re.search(unless, n)):
                    hits.append((rel, str(ln), n.strip()[:72]))
                    seen_line = True
            # A forbidden phrase that WRAPS across two lines is invisible to the
            # per-line pass. Fall back to the whole file, normalised, so wrapping
            # cannot hide a regression.
            if not seen_line:
                whole = norm(raw)
                m = rx.search(whole)
                if m and not (unless and re.search(unless, whole[max(0, m.start() - 200):m.end() + 200])):
                    hits.append((rel, '?', whole[m.start():m.start() + 72]))
        for rel, ln, txt in hits:
            fails.append(('CLAIMS', cid, f'MUST NOT appear — {rel}:{ln}  {txt}'))
        if not hits and VERBOSE:
            passed.append(f'claim {cid}: correctly absent')


for num, files in DUPES:
    fails.append(('CLAIMS', f'{num} duplicated in modules/',
                  'appears in more than one generated file — a stale copy from a '
                  'rename is still in the tree: ' + ', '.join(files)))


# --- CHECK 3: three-beat closure --------------------------------------------
BEATS = [('YOUR DECISION', r'(?i)^[#=\s*]*your decision'),
         ('PUT IT IN ORANGE PLAN', r'(?i)^[#=\s*]*put it in orange plan'),
         ('YOU ARE DONE WHEN', r'(?i)^[#=\s*]*you are done when')]
EXEMPT = {'0.1', '0.2'}

for num, title, seg, is_adv in LESSONS:
    if is_adv or num in EXEMPT:
        continue                       # advanced closes with Homework, by design
    if re.match(r'(Walkthrough|External demo)', title):
        continue
    sd, ld = 'scripts', 'lesson-text'
    sp, lp = find(sd, num), find(ld, num)
    layers = {'master': seg}
    if sp:
        layers['script'] = open(os.path.join(root, sp), encoding='utf-8').read()
    if lp:
        layers['lesson-text'] = open(os.path.join(root, lp), encoding='utf-8').read()
    for beat, pat in BEATS:
        rx = re.compile(pat, re.M)
        have = {k for k, v in layers.items() if rx.search(v)}
        if not have:
            notes.append(('BEATS', f'{num} {title[:40]}',
                          f'no "{beat}" in any layer — lesson does not close with the '
                          f'three beats, so it contributes nothing to its checkpoint'))
        elif len(have) != len(layers):
            # This is the parity case: one layer changed and the others did not.
            fails.append(('BEATS', f'{num} {title[:40]}',
                          f'"{beat}" in {sorted(have)} but NOT in '
                          f'{sorted(set(layers) - have)}'))


# --- report -----------------------------------------------------------------
def show(rows, label):
    print(f'\n{label}  —  {len(rows)}')
    for kind, where, why in rows:
        print(f'  [{kind}] {where}')
        print(f'          {why}')


if VERBOSE and passed:
    print('PASSED')
    for p in passed:
        print(f'  ok  {p}')

show(notes, 'NOTES (reported, do not fail)')
show(fails, 'FAILURES')
print(f'\n{len(LESSONS)} lessons · {len(REGISTRY)} registry rules · '
      f'{len(SCAN)} files scanned · {len(fails)} failures, {len(notes)} notes')
sys.exit(1 if fails else 0)
