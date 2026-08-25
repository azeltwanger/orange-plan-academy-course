#!/usr/bin/env python3
"""Generate teleprompter scripts (scripts/) from MASTER-COURSE.md.

One file per A-roll segment: every talking-head lesson in full, and the
teach half of each hybrid lesson (everything above the 🎥 marker).
Screen-share narration stays in MASTER-COURSE.md + SCREEN-SHOOT-LIST.md.

What gets stripped: outcomes blocks, `>` flag lines, metadata lines,
🎥 markers, markdown bold/italic markers. Tables are kept but fenced with
"on screen — don't read verbatim". Headings become == SECTION == cues.

Run after editing the master:  python3 tools/build-scripts.py
"""
import re, os, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# The Academy is two courses. Default is the required core; --advanced builds
# the optional library from its own master into scripts/advanced/.
ADVANCED = '--advanced' in sys.argv
SRC = 'MASTER-ADVANCED.md' if ADVANCED else 'MASTER-COURSE.md'
t = open(os.path.join(root, SRC), encoding='utf-8').read()
outdir = os.path.join(root, 'scripts', 'advanced') if ADVANCED else os.path.join(root, 'scripts')
os.makedirs(outdir, exist_ok=True)

# PROVENANCE and REGENERATION PROTECTION are separate questions.
#
# Current production states:
#   - AUSTIN DICTATION -> Austin recorded these words. Highest authority.
#   - VOICE-MATCHED DRAFT -> rewritten from Austin's dictation, client calls,
#     slides, and current app. Austin review is still pending.
#   - AUSTIN APPROVED -> Austin reviewed the wording and cleared it for filming.
#   - GENERATED -> derived from the master and safe to regenerate.
#
# Legacy authored states remain protected during module-by-module migration so
# running this tool cannot destroy work before it is reviewed and relabeled:
#   - VOICE-REVIEWED SCRIPT
#   - AUTHORED SCRIPT
#   - SPOKEN-PROSE VERSION
#
# Walkthroughs, demos, and docs are production sheets rather than files this
# generator owns. This script only WRITES generated files; it does not delete.
PROTECTED_MARKERS = (
    'AUSTIN DICTATION',
    'VOICE-MATCHED DRAFT',
    'AUSTIN APPROVED',
    # Legacy migration states:
    'VOICE-REVIEWED SCRIPT',
    'AUTHORED SCRIPT',
    'SPOKEN-PROSE VERSION',
)
VOICE_REVIEW_PENDING_MARKERS = (
    'VOICE-MATCHED DRAFT',
    'AUTHORED SCRIPT',
    'SPOKEN-PROSE VERSION',
)

PROTECTED_FILES = set()
VOICE_REVIEW_PENDING = set()
for f in sorted(os.listdir(outdir)):
    if not f.endswith('.md'):
        continue
    if any(k in f for k in ('WALKTHROUGH', 'DEMO', 'README', 'VOICE-GUIDE')):
        PROTECTED_FILES.add(f)
        continue
    head = open(os.path.join(outdir, f), encoding='utf-8').read(1400)
    if any(state in head for state in PROTECTED_MARKERS):
        PROTECTED_FILES.add(f)
    if any(state in head for state in VOICE_REVIEW_PENDING_MARKERS):
        VOICE_REVIEW_PENDING.add(f)

# Protect by LESSON NUMBER, not filename. A manually edited script whose title
# drifted from the master's would otherwise be shadowed by a fresh generated
# copy under a new slug, leaving two files for one lesson.
#
# Normalise the hybrid '-A' suffix. A protected hybrid script is named
# '09-3-A_slug.md', but if the master's 🎥 marker is later removed the
# generator emits '09-3_slug.md' — a different filename AND a different key.
#
# Advanced-library files are 'A3-1_slug.md', not digit-led, so include both
# numeric and A-prefixed lesson keys.
PROTECTED_NUMS = {
    f.split('_')[0].removesuffix('-A')
    for f in PROTECTED_FILES
    if f[:2].isdigit() or f[:1] == 'A'
}
print(f'protected: {len(PROTECTED_FILES)} files / {len(PROTECTED_NUMS)} lesson numbers')
if VOICE_REVIEW_PENDING:
    print(f'voice review pending: {len(VOICE_REVIEW_PENDING)} authored scripts')

# Core lessons are '## 4.1'; Advanced Library lessons are '## A7.2'.
parts = re.split(r'\n(?=## A?\d+\.\d+ )', t)
made = 0
for p in parts[1:]:
    head = p.split('\n', 1)[0][3:]
    num = head.split()[0]
    title = head[len(num)+1:]
    body = p.split('\n', 1)[1]
    # A lesson section runs until the next lesson OR the next unit header.
    body = re.split(r'\n#{1,2} Unit \d+ ', body)[0]
    is_screen = (
        title.lower().startswith('walkthrough')
        or 'check your work' in title.lower()
        or title.startswith('External demo')
    )
    if is_screen:
        continue
    hybrid = 'SCREEN SHARE STARTS HERE' in body
    if hybrid:
        body = body.split('> 🎥 **SCREEN SHARE STARTS HERE')[0]
    lines = body.split('\n')
    out, skip_outcomes = [], False
    for line in lines:
        s = line.rstrip()
        if s.startswith('*`'):
            continue
        if s.startswith('**By the end of this lesson'):
            skip_outcomes = True
            continue
        if skip_outcomes:
            if s.strip() == '---':
                skip_outcomes = False
            continue
        if s.startswith('>'):
            continue
        if s.strip() == '---':
            continue
        match = re.match(r'^(#{3,5}) (.*)', s)
        if match:
            out += ['', f'== {match.group(2).upper()} ==', '']
            continue
        out.append(s)

    # Fence tables so nobody mistakes them for prompter-readable prose.
    fenced, i = [], 0
    while i < len(out):
        if out[i].lstrip().startswith('|'):
            table = []
            while i < len(out) and out[i].lstrip().startswith('|'):
                table.append(out[i])
                i += 1
            fenced.append(
                '┄┄ TABLE (REFERENCE — not prompter-readable; the spoken read '
                'must be written above this during voice conversion) ┄┄'
            )
            fenced += table
            fenced.append('┄┄ end table ┄┄')
        else:
            fenced.append(out[i])
            i += 1

    text = '\n'.join(fenced)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'\1', text)
    text = text.replace('`', '')
    text = re.sub(r'\n{3,}', '\n\n', text).strip() + '\n'
    words = len([word for word in text.split() if not word.startswith('┄')])
    mins = words / 155
    seg = f'{num}-A' if hybrid else num
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:40]
    header = (
        f'TELEPROMPTER SCRIPT — segment {seg}\n'
        f'{num} {title}\n'
        f'{words} words · ~{mins:.1f} min at 155 wpm · GENERATED'
        + (
            ' · A-ROLL ONLY (screen half = shoot list segment '
            f'{num}-B)'
            if hybrid else ''
        )
        + '\n'
        + '=' * 60
        + '\n\n'
    )
    mod, sub = num.split('.', 1)
    if mod.startswith('A'):
        fn = f'{mod}-{sub}_{slug}.md'
    else:
        fn = f'{int(mod):02d}-{sub}{"-A" if hybrid else ""}_{slug}.md'
    lesson_key = fn.split('_')[0].removesuffix('-A')
    if fn in PROTECTED_FILES or lesson_key in PROTECTED_NUMS:
        continue
    open(os.path.join(outdir, fn), 'w', encoding='utf-8').write(header + text)
    made += 1
print(f'wrote {made} scripts to scripts/')
