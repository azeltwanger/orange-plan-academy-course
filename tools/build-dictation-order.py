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

# The say-once block used to be hand-written, and it went stale exactly the
# way the running order did: it still named retired lessons 4.5, 6.4, 8.5,
# 11.1 and 11.3, and described hybrid screen work in Modules 4 and 8 that no
# longer exists. Derive it instead.
handoff, no_capture = [], []
for title, _, lessons in units:
    teach = [n for n, t_, s in lessons if not s]
    caps = [n for n, t_, s in lessons if s]
    if not teach:
        continue
    if caps:
        handoff.append(teach[-1])
    else:
        no_capture.append((title.split('—')[0].strip(), teach[-1]))

say_once = ['## Say-once items (already built that way, don\'t re-explain later)', '',
  '*Generated. Regenerating this file rewrites this section from the current '
  'course, so it cannot go stale again.*', '',
  '- **The AI** is taught in full in **1.2** and nowhere else. Later '
  'walkthroughs only name the button and say when it is worth running.',
  '- **The US-specific disclaimer** is said at the top of **6.1** and the top '
  'of **9.1**. Twice, total, plus the breakdown in 1.1 of which modules are '
  'US-shaped. It used to run 12 times.',
  '- **The walkthrough hand-off** ("watch the walkthrough below this video") '
  'belongs ONLY on the last teach lesson of a module that has a capture: '
  + ' · '.join(f'**{n}**' for n in handoff) + '.']
if no_capture:
    say_once.append('- **No capture, so no hand-off:** '
        + ' · '.join(f'{m} (last teach {n})' for m, n in no_capture)
        + '. Do not record a hand-off line there until a sheet exists.')
say_once += ['', '---', '']

out = say_once + ['## The order', '']
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
head = head.split('## Say-once items')[0].rstrip()
# keep the headline stat in the preamble honest too
# Match BOTH the retired "N words · N hours" headline and the current
# "N min (N h)" one. The first version only matched the old form, so once the
# headline was converted to minutes it silently stopped updating and the file
# opened with 23 min while ending with 222.
head, n = re.subn(
    r'\*\*\d+ teach lessons · (?:[\d,]+ words · [\d.]+ hours|[\d,]+ min \([\d.]+ h\))[^*]*\*\*',
    f'**{teach_n} teach lessons · {teach_min:.0f} min '
    f'({hours:.1f} h) of finished audio at 155 wpm.**', head)
if n == 0:
    print('  !! headline not found in the preserved preamble — check it by hand')
open(p, 'w', encoding='utf-8').write(head + '\n\n' + '\n'.join(out))
print(f'DICTATION-ORDER.md regenerated — {teach_n} teach lessons, {teach_min:.0f} min')
