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
t = open(os.path.join(root, 'MASTER-COURSE.md'), encoding='utf-8').read()
outdir = os.path.join(root, 'scripts')
os.makedirs(outdir, exist_ok=True)
# PROTECTED: never regenerate, never delete.
#   - AUSTIN DICTATION  -> his own recorded words. Highest authority in the repo.
#   - SPOKEN-PROSE VERSION -> hand-calibrated spoken conversion.
#   - walkthroughs / demos / docs -> not generated from the master at all.
# This script only ever WRITES files it generates. It does not delete.
SPOKEN = set()
for f in sorted(os.listdir(outdir)):
    if not f.endswith('.md'):
        continue
    if any(k in f for k in ('WALKTHROUGH', 'DEMO', 'README', 'VOICE-GUIDE')):
        SPOKEN.add(f); continue
    head = open(os.path.join(outdir, f), encoding='utf-8').read(1000)
    if 'AUSTIN DICTATION' in head or 'SPOKEN-PROSE VERSION' in head:
        SPOKEN.add(f)
# Protect by LESSON NUMBER, not filename. A hand-calibrated script whose title
# drifted from the master's would otherwise be shadowed by a fresh generated
# copy under a new slug, leaving two files for one lesson.
SPOKEN_NUMS = {f.split('_')[0] for f in SPOKEN if f[:2].isdigit()}
print(f'protected: {len(SPOKEN)} files / {len(SPOKEN_NUMS)} lesson numbers')

parts = re.split(r'\n(?=## \d+\.\d+ )', t)
made = 0
for p in parts[1:]:
    head = p.split('\n', 1)[0][3:]
    num = head.split()[0]
    title = head[len(num)+1:]
    body = p.split('\n', 1)[1]
    # A lesson section runs until the next lesson OR the next unit header.
    # Without this, the last lesson in a module swallows the following
    # "# Unit N · Module M" heading and its blurb (hit when Module 0 gained
    # a second lesson, 2026-08-07).
    body = re.split(r'\n#{1,2} Unit \d+ ', body)[0]
    is_screen = (title.lower().startswith('walkthrough')
                 or 'check your work' in title.lower()
                 or title.startswith('External demo'))
    if is_screen:
        continue  # screen narration lives in the master + shoot list
    hybrid = 'SCREEN SHARE STARTS HERE' in body
    if hybrid:
        body = body.split('> 🎥 **SCREEN SHARE STARTS HERE')[0]
    lines = body.split('\n')
    out, skip_outcomes = [], False
    for l in lines:
        s = l.rstrip()
        if s.startswith('*`'): continue                      # metadata line
        if s.startswith('**By the end of this lesson'):      # outcomes block
            skip_outcomes = True; continue
        if skip_outcomes:
            if s.strip() == '---': skip_outcomes = False
            continue
        if s.startswith('>'): continue                       # flag / 🎥 lines
        if s.strip() == '---': continue
        m = re.match(r'^(#{3,5}) (.*)', s)
        if m:
            out += ['', f'== {m.group(2).upper()} ==', '']
            continue
        out.append(s)
    # fence tables
    fenced, i = [], 0
    while i < len(out):
        if out[i].lstrip().startswith('|'):
            tbl = []
            while i < len(out) and out[i].lstrip().startswith('|'):
                tbl.append(out[i]); i += 1
            fenced.append('┄┄ TABLE (REFERENCE — not prompter-readable; the spoken read must be written above this during voice conversion) ┄┄')
            fenced += tbl
            fenced.append('┄┄ end table ┄┄')
        else:
            fenced.append(out[i]); i += 1
    text = '\n'.join(fenced)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)             # bold
    text = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'\1', text)  # italics
    text = text.replace('`', '')
    text = re.sub(r'\n{3,}', '\n\n', text).strip() + '\n'
    words = len([w for w in text.split() if not w.startswith('┄')])
    mins = words / 155
    seg = f'{num}-A' if hybrid else num
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:40]
    header = (f'TELEPROMPTER SCRIPT — segment {seg}\n'
              f'{num} {title}\n'
              f'{words} words · ~{mins:.1f} min at 155 wpm'
              + (' · A-ROLL ONLY (screen half = shoot list segment '
                 f'{num}-B)' if hybrid else '') + '\n'
              + '=' * 60 + '\n\n')
    mod, sub = num.split('.', 1)
    fn = f'{int(mod):02d}-{sub}{"-A" if hybrid else ""}_{slug}.md'
    if fn in SPOKEN or fn.split('_')[0] in SPOKEN_NUMS:
        continue  # keep the hand-written / dictated version for this lesson
    open(os.path.join(outdir, fn), 'w', encoding='utf-8').write(header + text)
    made += 1
print(f'wrote {made} scripts to scripts/')
