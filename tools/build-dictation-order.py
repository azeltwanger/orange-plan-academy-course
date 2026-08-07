#!/usr/bin/env python3
"""Regenerate the running order in DICTATION-ORDER.md from the current course.

Everything ABOVE the '## The order' heading is hand-written and preserved
verbatim — the settle-these-five list, the say-once items, Austin's notes.
Everything from '## The order' down is rebuilt from MASTER-COURSE.md (module
names and lesson order) and scripts/ (measured runtimes), so a trim pass can
never leave the filming order describing a course that no longer exists.

Walkthroughs and demos are listed for context but carry no dictation minutes:
they're narrated off the DO/SEE/⚠ sheets, not read.

Run after editing the master or a script:  python3 tools/build-dictation-order.py
"""
import re, os, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
master = open(os.path.join(root, 'MASTER-COURSE.md'), encoding='utf-8').read()
sd = os.path.join(root, 'scripts')

# --- measured runtimes, keyed by lesson number ------------------------------
runtime, slug = {}, {}
for f in sorted(os.listdir(sd)):
    if not f.endswith('.md') or f in ('README.md', 'VOICE-GUIDE.md'):
        continue
    # '09-3-A_slug.md' -> '9.3'; '10-1_slug.md' -> '10.1'
    stem = f.split('_')[0]
    if stem.endswith('-A'):
        stem = stem[:-2]
    mod, _, sub = stem.partition('-')
    if not mod.isdigit():
        continue                       # advanced-library numbering (A4-1)
    num = f'{int(mod)}.{sub}'
    body = open(os.path.join(sd, f), encoding='utf-8').read().split('=' * 60, 1)[-1]
    words = len(body.split())
    runtime[num] = words / 155
    slug[num] = f

# --- module + lesson order from the master ----------------------------------
units = []           # [(unit_title, [(num, title, is_screen)])]
for m in re.finditer(r'^# Unit \d+ · (.+)$', master, re.M):
    units.append((m.group(1), m.start(), []))
for i, (title, start, lessons) in enumerate(units):
    end = units[i + 1][1] if i + 1 < len(units) else len(master)
    for lm in re.finditer(r'^## (\d+\.\d+) (.+)$', master[start:end], re.M):
        num, t = lm.group(1), lm.group(2)
        screen = (t.lower().startswith('walkthrough')
                  or t.lower().startswith('external demo'))
        lessons.append((num, t, screen))

out = ['## The order', '']
teach_n = teach_min = 0
for title, _, lessons in units:
    mins = sum(runtime.get(n, 0) for n, t, s in lessons if not s)
    n_teach = sum(1 for n, t, s in lessons if not s)
    teach_n += n_teach
    teach_min += mins
    out += [f'### {title} · {mins:.0f} min', '',
            '| # | Lesson | min |', '|---|---|---|']
    for num, t, screen in lessons:
        if screen:
            kind = 'DEMO' if t.lower().startswith('external') else 'WALKTHROUGH'
            out.append(f'| {num} | *{t}* | — {kind}, narrated off the sheet |')
        else:
            r = runtime.get(num)
            out.append(f'| {num} | {t} | {r:.1f} |' if r else
                       f'| {num} | {t} | ⚠ no script |')
    out += ['']

hours = teach_min / 60
out += ['---', '',
        f'**{teach_n} teach lessons · {teach_min:.0f} min '
        f'({hours:.1f} h) of finished audio at 155 wpm.**', '',
        'Walkthroughs are not dictated. They are screen captures you narrate in',
        'your own words off the DO / SEE / ⚠ sheets, and they happen after the',
        'teach lessons for that module.', '']

p = os.path.join(root, 'DICTATION-ORDER.md')
old = open(p, encoding='utf-8').read()
head = old.split('## The order')[0].rstrip()
# keep the headline stat in the preamble honest too
head = re.sub(r'\*\*\d+ teach lessons · [\d,]+ words · [\d.]+ hours[^*]*\*\*',
              f'**{teach_n} teach lessons · {teach_min:.0f} min '
              f'({hours:.1f} h) of finished audio at 155 wpm.**', head)
open(p, 'w', encoding='utf-8').write(head + '\n\n' + '\n'.join(out))
print(f'DICTATION-ORDER.md regenerated — {teach_n} teach lessons, {teach_min:.0f} min')
