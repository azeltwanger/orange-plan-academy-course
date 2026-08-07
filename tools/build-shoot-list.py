#!/usr/bin/env python3
"""Regenerate SCREEN-SHOOT-LIST.md from the capture sheets in scripts/.

The shoot list used to be a hand-maintained copy of the walkthrough sheets,
which is why it drifted — it still named segments 8.7, 9.5-B, 11.2 and 11.4
after those were merged or moved. Now it is an INDEX over the sheets, so the
sheet is the only place a beat is written down.

What it reads: every scripts/*WALKTHROUGH*.md and *DEMO*.md sheet —
  '# 10.3 · WALKTHROUGH — title'      the segment
  '**Screen capture · ...**'          the capture estimate line
  '- [ ] ...' under '## Before you record'   pre-flight
  '## □ A1 · step title'              the beats
  '### ✂ CUT POINT n'                 where the edit may split

It also checks the sheets against MASTER-COURSE.md and flags any walkthrough
lesson in the master that has no sheet yet.

Run:  python3 tools/build-shoot-list.py
"""
import re, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sd = os.path.join(root, 'scripts')
master = open(os.path.join(root, 'MASTER-COURSE.md'), encoding='utf-8').read()

sheets = sorted(f for f in os.listdir(sd)
                if f.endswith('.md') and ('WALKTHROUGH' in f or 'DEMO' in f))

out = ['# Screen-Share Shoot List — capture run sheet', '',
       '> **GENERATED** from the capture sheets in `scripts/`. Do not edit this',
       '> file: edit the sheet, then run `python3 tools/build-shoot-list.py`.',
       '> The sheet beside your keyboard is the sheet in `scripts/`; this is the',
       '> order to shoot them in and what each one needs staged first.', '']

body, total, gaps = [], 0, []
for f in sheets:
    t = open(os.path.join(sd, f), encoding='utf-8').read()
    title = t.split('\n', 1)[0].lstrip('# ').strip()
    meta = next((l.strip() for l in t.split('\n')[:6]
                 if l.startswith('**Screen capture') or l.startswith('**Screen')), '')
    mins = re.findall(r'~(\d+)\s*min', meta)
    if mins:
        total += int(mins[-1])
    pre = []
    if '## Before you record' in t:
        block = t.split('## Before you record', 1)[1].split('\n## ', 1)[0]
        pre = [l.strip() for l in block.split('\n') if l.strip().startswith('- [ ]')]
    steps = re.findall(r'^## □ (.+)$', t, re.M)
    cuts = re.findall(r'^#+ (✂ CUT POINT.*)$', t, re.M)

    body += [f'## ☐ {title}', '', f'*{meta.strip("*")}*  ·  sheet: `scripts/{f}`', '']
    if cuts:
        body += ['**Cut points in this capture:** ' + ' · '.join(f'**{c}**' for c in cuts), '']
    if pre:
        body += ['**Stage this first:**'] + pre + ['']
    if steps:
        body += ['**Beats:**']
        body += [f'{i}. ☐ {s}' for i, s in enumerate(steps, 1)]
        body += ['']
    body += ['---', '']

# any walkthrough/demo lesson in the master with no sheet?
have = {re.match(r'(\S+)', open(os.path.join(sd, f), encoding='utf-8')
                 .read().lstrip('# ')).group(1) for f in sheets}
for m in re.finditer(r'^## (\d+\.\d+) ((?:Walkthrough|External demo).+)$', master, re.M):
    if m.group(1) not in have:
        gaps.append(f'{m.group(1)} {m.group(2)}')

# A module with teach lessons but no capture at all is the more dangerous gap:
# nothing in the master points at the missing sheet, so it can't be caught above.
units = [(m.group(1), m.start()) for m in re.finditer(r'^# Unit \d+ · (.+)$', master, re.M)]
for i, (name, start) in enumerate(units):
    end = units[i + 1][1] if i + 1 < len(units) else len(master)
    if 'Start Here' in name:
        continue                       # intentionally talking-head only
    nums = re.findall(r'^## (\d+)\.\d+ ', master[start:end], re.M)
    if nums and not any(n in {h.split('.')[0] for h in have} for n in nums):
        gaps.append(f'{name} — NO capture of any kind')

out += [f'**{len(sheets)} captures · ~{total} min of raw capture.**', '',
        'Seed the demo account with the couple\'s canonical numbers before the',
        'first segment (Phase 0 of FILMING-CHECKLIST.md). Clean browser profile,',
        'notifications off, 5 seconds of stillness before the first click and',
        'after the last.', '',
        '**Evergreen rule:** never zoom on or read out a law-set number (brackets,',
        'limits, exemptions). Call it "the current number the app shows" and move on.', '',
        '**Film each module\'s capture in ONE continuous session.** App state builds',
        'forward and restarting is where the retakes come from. Where a sheet has',
        '`✂ CUT POINT` markers, the edit can split it into several videos later.', '']
if gaps:
    out += ['> ⚠ **No capture sheet yet:** ' + ' · '.join(gaps) +
            '. These cannot be filmed until a sheet exists.', '']
out += ['---', ''] + body

open(os.path.join(root, 'SCREEN-SHOOT-LIST.md'), 'w', encoding='utf-8').write('\n'.join(out))
print(f'SCREEN-SHOOT-LIST.md regenerated — {len(sheets)} captures, ~{total} min'
      + (f'; {len(gaps)} missing sheet(s): {gaps}' if gaps else ''))
