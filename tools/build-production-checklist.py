#!/usr/bin/env python3
"""Regenerate the filming checklist from the current masters and scripts.

PRODUCTION-CHECKLIST used to hold a hand-typed list of every lesson to film.
It drifted exactly like the shoot list and the dictation order did — still
naming 11.1, 8.6 and an Allocation module numbered 3 long after none of that
was true. Filming from a stale checklist is the most expensive mistake
available at this stage, so it is generated.

THREE things are generated now, not one:

  1. The STATUS block, between `<!-- STATUS:START/END -->`. It used to be
     hand-written, which is how the file came to say "FINAL — cleared for
     filming" while a lesson carried a red "do not film" flag and another had
     an unresolved legal review. **The word FINAL is now earned, not typed.**
  2. The generated-warning notice. It used to be re-appended on every run
     while the previous copy was preserved as part of the "head", so the file
     accumulated seven identical warning blocks. Running this twice now
     produces a zero-byte diff.
  3. The per-module and advanced-library lists.

Everything else above '## ☐ ONE-TIME SETUP' is preserved verbatim.

Run:  python3 tools/build-production-checklist.py
"""
import os, re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
core = open(os.path.join(root, 'MASTER-COURSE.md'), encoding='utf-8').read()
adv = open(os.path.join(root, 'MASTER-ADVANCED.md'), encoding='utf-8').read()
sd = os.path.join(root, 'scripts')

runtime = {}
for d in (sd, os.path.join(sd, 'advanced')):
    for f in sorted(os.listdir(d)):
        if not f.endswith('.md') or f in ('README.md', 'VOICE-GUIDE.md'):
            continue
        stem = f.split('_')[0]
        num = (stem.replace('-', '.', 1) if stem[0] == 'A'
               else f'{int(stem.split("-")[0])}.{stem.split("-")[1]}')
        body = open(os.path.join(d, f), encoding='utf-8').read().split('=' * 60, 1)[-1]
        runtime[num] = len(body.split()) / 155

# --- blockers -------------------------------------------------------------
# Three statuses, not one. Conflating them is how the checklist came to list only
# 4.3 and A8.1 and then say "everything not listed is clear to shoot" — while the
# handoff separately named F20 and F23 as filming blockers it could not see, and
# while A8.1's text-only status was being counted as a filming blocker when the
# thing actually blocking A8.1 is publication.
#
#   FILMING BLOCKER      cannot be shot until a human resolves it
#   PUBLICATION BLOCKER  can be shot; cannot ship
#   NO FILMING PLANNED   not a blocker at all; nothing scheduled
#
# Markers are written into the layer that carries them so this reads structure
# rather than trusting a person to remember. Module-level markers sit under the
# `# Unit N · Module M` heading; lesson-level markers sit in the lesson section.
MARKERS = [
    (r'🔴 \*\*FILMING BLOCKER \((F\d+)\)',        'filming',     None),
    (r'HOLD FOR REDICTATION',                       'filming',     'F22'),
    (r'FLAGGED FOR REBUILD',                        'filming',     None),
    (r'⚖ \*\*PUBLICATION BLOCKER',                  'publication', None),
    (r'(?i)pending estate-attorney review',         'publication', None),
    (r'(?i)CPA-blocking',                           'publication', None),
    (r'⬜ \*\*NO FILMING PLANNED',                   'noplan',      None),
]


def scan(text, label, unit_level=False):
    """Attribute each marker to the lesson, or to the module for unit-level ones."""
    out = []
    if unit_level:
        # A module-level marker lives between the unit heading and its first
        # lesson. Anything past that belongs to a lesson, not the module.
        for m in re.finditer(r'^# Unit \d+ · (Module \d+)[^\n]*$', text, re.M):
            nxt = re.search(r'^## ', text[m.end():], re.M)
            seg = text[m.end():m.end() + nxt.start()] if nxt else text[m.end():]
            for pat, kind, fid in MARKERS:
                hit = re.search(pat, seg)
                if hit:
                    tag = fid or (hit.group(1) if hit.groups() else '')
                    out.append((m.group(1), kind, tag, label))
        return out
    sections = list(re.finditer(r'^## (A?\d+\.\d+) (.+)$', text, re.M))
    for i, m in enumerate(sections):
        end = sections[i + 1].start() if i + 1 < len(sections) else len(text)
        seg = text[m.start():end]
        # A module's LAST lesson would otherwise swallow the following
        # "# Unit N · Module M" heading and any module-level marker under it,
        # which attributed Module 2's F23 to lesson 1.5. Same bug class as the
        # one build-scripts.py guards against.
        seg = re.split(r'\n#{1,2} (?:Unit |Advanced Module )', seg)[0]
        for pat, kind, fid in MARKERS:
            hit = re.search(pat, seg)
            if hit:
                tag = fid or (hit.group(1) if hit.groups() else '')
                out.append((m.group(1), kind, tag, label))
    return out


raw = (scan(core, 'MASTER-COURSE.md') + scan(adv, 'MASTER-ADVANCED.md')
       + scan(core, 'MASTER-COURSE.md', unit_level=True))
for d, sub in ((sd, ''), (os.path.join(sd, 'advanced'), 'advanced/')):
    for f in sorted(os.listdir(d)):
        if f in ('README.md', 'VOICE-GUIDE.md') or not f.endswith('.md'):
            continue
        head = open(os.path.join(d, f), encoding='utf-8').read().split('=' * 60, 1)[0]
        stem = f.split('_')[0].removesuffix('-A')
        num = (stem.replace('-', '.', 1) if stem[0] == 'A'
               else f'{int(stem.split("-")[0])}.{stem.split("-")[1]}')
        for pat, kind, fid in MARKERS:
            hit = re.search(pat, head)
            if hit:
                tag = fid or (hit.group(1) if hit.groups() else '')
                raw.append((num, kind, tag, f'scripts/{sub}{f}'))

buckets = {'filming': {}, 'publication': {}, 'noplan': {}}
for where, kind, tag, src in raw:
    buckets[kind].setdefault((where, tag), []).append(src)

filming = sorted(buckets['filming'], key=lambda k: (k[0][0] == 'A', k[0]))
publication = sorted(buckets['publication'], key=lambda k: (k[0][0] == 'A', k[0]))
noplan = sorted(buckets['noplan'], key=lambda k: (k[0][0] == 'A', k[0]))
blocked_lessons = {w for w, _ in filming}

status = ['<!-- STATUS:START -->', '']
if filming:
    status += [f'> **Status: NOT CLEARED FOR FILMING — {len(filming)} filming '
               f'blocker' + ('s' if len(filming) != 1 else '') + '.**', '>',
               '> The word FINAL is generated, not typed. It appears only when the',
               '> filming list below is empty. Each line is a marker found in the layer',
               '> that carries it, so clearing one means removing its marker at source.', '>',
               '> ### 🔴 CORE FILMING BLOCKERS', '>']
    for where, tag in filming:
        srcs = ' · '.join(f'`{s}`' for s in sorted(set(buckets['filming'][(where, tag)])))
        status.append(f'> - **{where}**' + (f' ({tag})' if tag else '') + f' — {srcs}')
    status.append('>')
else:
    status += ['> **Status: cleared for filming.** No filming blocker marker is',
               '> present in any layer.', '>']

if noplan:
    status += ['> ### ⬜ NOT SCHEDULED FOR v1 — not blockers', '>']
    for where, tag in noplan:
        status.append(f'> - **{where}** — no filming planned for v1')
    status.append('>')

if publication:
    status += ['> ### ⚖ PUBLICATION BLOCKERS — can be shot, cannot ship', '>']
    for where, tag in publication:
        srcs = ' · '.join(f'`{s}`' for s in sorted(set(buckets['publication'][(where, tag)])))
        status.append(f'> - **{where}** — {srcs}')
    status += ['>', '> Tracked in `LEGAL-REVIEW-PACKET.md`. A publication blocker does',
               '> not stop a camera; it stops a student seeing the result.', '>']

status += ['> **Anything not listed above is clear to shoot.**', '', '<!-- STATUS:END -->']

# --- per-module list ------------------------------------------------------
# One sheet can cover two lessons (Module 1 is filmed once, cut in two), so read
# the sheets and say which captures share a session instead of implying two.
sheet_of = {}
for f in sorted(x for x in os.listdir(sd) if x.endswith('.md')):
    if 'WALKTHROUGH' not in f and 'DEMO' not in f:
        continue
    h1 = open(os.path.join(sd, f), encoding='utf-8').read().split('\n', 1)[0]
    nums = re.findall(r'\d+\.\d+', h1.split('·')[0])
    for n in nums:
        sheet_of[n] = (f, nums)

out = []
units = [(m.group(1), m.start()) for m in re.finditer(r'^# Unit \d+ · (Module .+)$', core, re.M)]
wave = {'Module 0': 1, 'Module 1': 1, 'Module 2': 1, 'Module 3': 1, 'Module 4': 1}
for i, (name, s) in enumerate(units):
    e = units[i + 1][1] if i + 1 < len(units) else len(core)
    key = name.split(' —')[0]
    out += ['', f'## ☐ {name.upper()}   ·   WAVE {wave.get(key, 2)}', '']
    for lm in re.finditer(r'^## (\d+\.\d+) (.+)$', core[s:e], re.M):
        n, t = lm.group(1), lm.group(2)
        cap = t.lower().startswith(('walkthrough', 'external demo'))
        mins = runtime.get(n)
        mark = '🖥 capture' if cap else '🎙 film'
        dur = '' if cap else f' (~{mins:.0f} min)' if mins else ''
        note = ''
        if cap and n in sheet_of and len(sheet_of[n][1]) > 1:
            note = (' — ONE SESSION with '
                    + ' + '.join(x for x in sheet_of[n][1] if x != n)
                    + f', off `scripts/{sheet_of[n][0]}`')
        if n in blocked_lessons:
            note += '  🔴 BLOCKED — see status block above'
        out.append(f'☐ {n} {t} — {mark}{dur}{note}')
    out.append(f'☐ Paste the Module {key.split()[-1]} checkpoint into Circle '
               f'(top: "By the end…", bottom: "Complete when…")')

out += ['', '## ☐ ADVANCED LIBRARY — text first, video in demand order', '',
        '*Publish every advanced lesson as student-facing TEXT at launch. Film in this order afterwards.*', '']
# This list used to hold core-style numbers (6.3, 7.4, 8.5, 9.5, 7.2) that no
# advanced lesson has carried since the library was renumbered to A-prefixes.
# Every one silently failed to match, which is why the printed order began at
# "2." — only A3.1 resolved. Unmatched names are now an error, not a shrug.
DEMAND = ['A3.1', 'A6.1', 'A5.1', 'A7.1', 'A6.2', 'A5.2', 'A7.2']
seen, missing = set(), []
j = 0
for n in DEMAND:
    m = re.search(rf'^## {re.escape(n)} (.+)$', adv, re.M)
    if not m:
        missing.append(n)
        continue
    j += 1
    flag = '  🔴 BLOCKED' if n in blocked_lessons else ''
    out.append(f'☐ {j}. {n} {m.group(1)} — 🎙 film (~{runtime.get(n, 0):.0f} min){flag}')
    seen.add(n)
for m in re.finditer(r'^## (A?\d+\.\d+) (.+)$', adv, re.M):
    if m.group(1) not in seen:
        flag = '  🔴 BLOCKED' if m.group(1) in blocked_lessons else ''
        out.append(f'☐ — {m.group(1)} {m.group(2)} — TEXT ONLY for now{flag}')
if missing:
    out += ['', f'> ⚠ **Demand-order entries that match no advanced lesson: '
            f'{", ".join(missing)}.** Fix `DEMAND` in '
            '`tools/build-production-checklist.py` — a name that does not resolve '
            'is silently dropped from the numbering.']

WARNING = ('> **The per-lesson list below is GENERATED** by\n'
           '> `tools/build-production-checklist.py`. Regenerate it before every shoot\n'
           '> day. Do not hand-edit it — that is how the last one ended up naming\n'
           '> lessons that no longer exist.')

p = os.path.join(root, 'PRODUCTION-CHECKLIST.md')
old = open(p, encoding='utf-8').read()
head = old.split('## ☐ ONE-TIME SETUP')[0]
# Strip every previously-injected copy of the warning and of the status block.
# Not doing this is what stacked seven identical warnings into the file.
head = head.replace(WARNING, '')
head = re.sub(r'<!-- STATUS:START -->.*?<!-- STATUS:END -->', '', head, flags=re.S)
# ...and the hand-written status paragraph the generated block replaces.
head = re.sub(r'> \*\*Status: .*?(?=\n\n)', '', head, flags=re.S)
head = re.sub(r'\n{3,}', '\n\n', head).rstrip()
setup = old.split('## ☐ ONE-TIME SETUP', 1)[1].split('\n## ', 1)[0]

open(p, 'w', encoding='utf-8').write(
    head + '\n\n' + '\n'.join(status) + '\n\n' + WARNING + '\n\n'
    + '## ☐ ONE-TIME SETUP' + setup.rstrip() + '\n' + '\n'.join(out) + '\n')
print(f'PRODUCTION-CHECKLIST.md regenerated — '
      f'{len(filming)} filming blocker(s): '
      + (', '.join(f'{w} {t_}'.strip() for w, t_ in filming) or 'none')
      + f' · {len(publication)} publication blocker(s) · {len(noplan)} not scheduled')
