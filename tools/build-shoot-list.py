#!/usr/bin/env python3
"""Regenerate SCREEN-SHOOT-LIST.md from the capture sheets in scripts/.

The shoot list is an index over the canonical walkthrough and demo sheets. The
sheet is the only place a capture beat is written down.

Run:  python3 tools/build-shoot-list.py
"""
import re, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sd = os.path.join(root, 'scripts')
master = open(os.path.join(root, 'MASTER-COURSE.md'), encoding='utf-8').read()

sheets = sorted(
    f for f in os.listdir(sd)
    if f.endswith('.md') and ('WALKTHROUGH' in f or 'DEMO' in f)
)

out = [
    '# Screen-Share Shoot List — capture run sheet', '',
    '> **GENERATED** from the capture sheets in `scripts/`. Do not edit this',
    '> file: edit the sheet, then run `python3 tools/build-shoot-list.py`.',
    '> The sheet beside your keyboard is the sheet in `scripts/`; this is the',
    '> order to shoot them in and what each one needs staged first.', '',
]

body, total, gaps = [], 0.0, []
for f in sheets:
    text = open(os.path.join(sd, f), encoding='utf-8').read()
    title = text.split('\n', 1)[0].lstrip('# ').strip()
    meta = next(
        (
            line.strip()
            for line in text.split('\n')[:8]
            if line.startswith('**')
            and re.search(r'about\s+\d+(?:\.\d+)?\s+minutes?', line, re.I)
        ),
        '',
    )
    minutes = re.search(r'about\s+(\d+(?:\.\d+)?)\s+minutes?', meta, re.I)
    if minutes:
        total += float(minutes.group(1))

    pre = []
    if '## Before you record' in text:
        block = text.split('## Before you record', 1)[1].split('\n## ', 1)[0]
        pre = [line.strip() for line in block.split('\n') if line.strip().startswith('- [ ]')]

    steps = re.findall(r'^## □ (.+)$', text, re.M)
    cuts = re.findall(r'^#+ (✂ CUT POINT.*)$', text, re.M)

    body += [f'## ☐ {title}', '', f'*{meta.strip("*")}*  ·  sheet: `scripts/{f}`', '']
    if cuts:
        body += ['**Cut points in this capture:** ' + ' · '.join(f'**{cut}**' for cut in cuts), '']
    if pre:
        body += ['**Stage this first:**'] + pre + ['']
    if steps:
        body += ['**Beats:**']
        body += [f'{i}. ☐ {step}' for i, step in enumerate(steps, 1)]
        body += ['']
    body += ['---', '']

have = set()
for f in sheets:
    h1 = open(os.path.join(sd, f), encoding='utf-8').read().split('\n', 1)[0]
    have |= set(re.findall(r'A?\d+\.\d+', h1.split('·')[0]))

for match in re.finditer(r'^## (\d+\.\d+) ((?:WALKTHROUGH|DEMO).+)$', master, re.M | re.I):
    if match.group(1) not in have:
        gaps.append(f'{match.group(1)} {match.group(2)}')

units = [(match.group(1), match.start()) for match in re.finditer(r'^# Unit \d+ · (.+)$', master, re.M)]
for i, (name, start) in enumerate(units):
    end = units[i + 1][1] if i + 1 < len(units) else len(master)
    if 'Start Here' in name:
        continue
    nums = re.findall(r'^## (\d+)\.\d+ ', master[start:end], re.M)
    if nums and not any(num in {item.split('.')[0] for item in have} for num in nums):
        gaps.append(f'{name} — NO capture of any kind')

for sub in ('', 'advanced'):
    directory = os.path.join(sd, sub)
    if not os.path.isdir(directory):
        continue
    for f in sorted(name for name in os.listdir(directory) if name.endswith('.md')):
        if 'WALKTHROUGH' in f or 'DEMO' in f:
            continue
        text = open(os.path.join(directory, f), encoding='utf-8').read()
        for segment in re.findall(r'🎥 SCREEN SHARE \(segment ([^)]+)\)', text):
            gaps.append(
                f'{segment} — embedded screen-share block in '
                f'scripts/{sub + "/" if sub else ""}{f}, no capture sheet'
            )

raw_minutes = int(total) if total.is_integer() else round(total, 1)
out += [
    f'**{len(sheets)} capture sessions, covering {len(have)} capture lessons '
    f'· ~{raw_minutes} min of raw capture.**', '',
    'A session is one continuous recording. Where a sheet names more than one',
    'lesson, it is filmed once and the edit splits it at the cut point.', '',
    'Seed the demo account with the couple\'s canonical numbers before the',
    'first segment (ONE-TIME SETUP in PRODUCTION-CHECKLIST.md). Clean browser',
    'profile, notifications off, 5 seconds of stillness before the first click',
    'and after the last.', '',
    '**Evergreen rule:** never zoom on or read out a law-set number (brackets,',
    'limits, exemptions). Call it "the current number the app shows" and move on.', '',
    '**Film each module\'s capture in ONE continuous session.** App state builds',
    'forward and restarting is where the retakes come from. Where a sheet has',
    '`✂ CUT POINT` markers, the edit can split it into several videos later.', '',
]
if gaps:
    out += [
        '> ⚠ **No capture sheet yet:** ' + ' · '.join(gaps)
        + '. These cannot be filmed until a sheet exists.', ''
    ]
out += ['---', ''] + body

open(os.path.join(root, 'SCREEN-SHOOT-LIST.md'), 'w', encoding='utf-8').write('\n'.join(out))
print(
    f'SCREEN-SHOOT-LIST.md regenerated — {len(sheets)} captures, ~{raw_minutes} min'
    + (f'; {len(gaps)} missing sheet(s): {gaps}' if gaps else '')
)
