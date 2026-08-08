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
# An OPTIONAL lesson must never carry the walkthrough hand-off: a student who
# correctly skips it would never hear where the capture is. Module 2's college
# lesson is the first of these. Hand-off goes to the last REQUIRED teach lesson.
def optional(title):
    return title.lower().startswith('optional')


handoff, no_capture, optionals = [], [], []
for title, _, lessons in units:
    teach = [n for n, t_, s in lessons if not s]
    required = [n for n, t_, s in lessons if not s and not optional(t_)]
    caps = [n for n, t_, s in lessons if s]
    optionals += [(n, t_) for n, t_, s in lessons if not s and optional(t_)]
    if not teach:
        continue
    if caps:
        handoff.append((required or teach)[-1])
    else:
        no_capture.append((title.split('—')[0].strip(), teach[-1]))

# These two used to be hardcoded strings inside a block that advertised itself as
# generated, so they rotted invisibly: the AI bullet still said 1.2 after the AI
# lesson became 0.2, and the disclaimer bullet still said 6.1/9.1 after the tax
# and estate modules were renumbered to 5.1/8.1. Derive both from the master.
ai = re.search(r'^## (\d+\.\d+) (How the AI works.+)$', master, re.M)
ai_num = ai.group(1) if ai else '??'
# Each US-specific module header states where its disclaimer is spoken, once.
disc = re.findall(r'Said ONCE, at the top of (\d+\.\d+)', master)
# ...and one lesson carries the breakdown of which modules are US-shaped. That
# paragraph currently lives only in the DICTATION script for 0.1, not in the
# master, so the master alone cannot answer this. Search both layers rather than
# print "??" — and shout, because a script-only paragraph is a parity gap.
BRK = r'built on US rules'
brk = re.search(r'^## (\d+\.\d+) [^\n]*\n(?:(?!^## ).)*?' + BRK, master, re.M | re.S)
if brk:
    brk_num = brk.group(1)
else:
    brk_num = '??'
    for f in sorted(slug.values()):
        if re.search(BRK, open(os.path.join(sd, f), encoding='utf-8').read()):
            stem = f.split('_')[0]
            brk_num = f'{int(stem.split("-")[0])}.{stem.split("-")[1]}'
            print(f'  !! PARITY: the "which modules are US-shaped" breakdown is in '
                  f'scripts/{f} ({brk_num}) but NOT in MASTER-COURSE.md')
            break

say_once = ['## Say-once items (already built that way, don\'t re-explain later)', '',
  '*Generated. Regenerating this file rewrites this section from the current '
  'course, so it cannot go stale again.*', '',
  f'- **The AI** is taught in full in **{ai_num}** and nowhere else. Later '
  'walkthroughs only name the button and say when it is worth running.',
  '- **The US-specific disclaimer** is said at the top of '
  + ' and the top of '.join(f'**{n}**' for n in disc)
  + f'. {"Twice" if len(disc) == 2 else str(len(disc)) + " times"}, total, plus '
  f'the breakdown in {brk_num} of which modules are US-shaped. It used to run 12 times.',
  '- **The walkthrough hand-off** ("watch the walkthrough below this video") '
  'belongs ONLY on the last REQUIRED teach lesson of a module that has a '
  'capture: ' + ' · '.join(f'**{n}**' for n in handoff) + '.']
if optionals:
    say_once.append('- **Optional lessons never carry the hand-off**, because a '
        'student who correctly skips one would never hear it: '
        + ' · '.join(f'**{n}** {t}' for n, t in optionals) + '.')
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
