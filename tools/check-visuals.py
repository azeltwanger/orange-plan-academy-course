#!/usr/bin/env python3
"""Check the visuals library against the course.

The visuals directory was excluded from the 2026-08-08 renumber and quietly
went stale by TWO structural changes: its 04-x files were allocation graphics
and 05-x were debt, which is the numbering from before Debt moved ahead of
Allocation, and it still carried 11-x files for a module that no longer exists.
Nothing broke, because no script cites a visual filename — which is exactly why
nobody noticed. This check is the tripwire.

Reports:
  ORPHAN    a visual whose lesson number is not in either master
  GAP       a teach lesson with no visual prompt
  H1 DRIFT  a visual whose in-file heading disagrees with its filename

Exit 1 on orphans or H1 drift. Gaps are reported but do not fail, because not
every lesson needs a graphic.

  python3 tools/check-visuals.py
"""
import os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
vd = os.path.join(root, 'visuals')
core = open(os.path.join(root, 'MASTER-COURSE.md'), encoding='utf-8').read()
adv = open(os.path.join(root, 'MASTER-ADVANCED.md'), encoding='utf-8').read()

# teach lessons only: walkthroughs and demos do not get a graphic
teach = set()
for src in (core, adv):
    for m in re.finditer(r'^## (A?\d+\.\d+) (.+)$', src, re.M):
        if not re.match(r'(Walkthrough|External demo)', m.group(2)):
            teach.add(m.group(1))

orphans, drift, have = [], [], {}
for fn in sorted(os.listdir(vd)):
    if not fn.endswith('.md') or fn in ('00-STYLE.md', 'README.md'):
        continue
    m = re.match(r'^(A?\d+)-(\d+)[ab]?_', fn)
    if not m:
        orphans.append((fn, 'filename does not encode a lesson number'))
        continue
    num = f'{m.group(1)}.{m.group(2)}'
    have.setdefault(num, []).append(fn)
    if num not in teach:
        orphans.append((fn, f'{num} is not a teach lesson in either master'))
    h1 = open(os.path.join(vd, fn), encoding='utf-8').readline().strip()
    hm = re.match(r'^# (A?\d+\.\d+) ', h1)
    if not hm:
        drift.append((fn, f'no lesson number in H1: {h1[:50]}'))
    elif hm.group(1) != num:
        drift.append((fn, f'H1 says {hm.group(1)}, filename says {num}'))

gaps = sorted(teach - set(have), key=lambda s: (s.startswith('A'), s))

print(f'visuals: {sum(len(v) for v in have.values())} prompts covering '
      f'{len(have)} of {len(teach)} teach lessons')
for label, items in (('ORPHAN', orphans), ('H1 DRIFT', drift)):
    print(f'\n{label}  —  {len(items)}')
    for f, why in items:
        print(f'  {f}: {why}')
print(f'\nGAP (lesson with no visual)  —  {len(gaps)}')
for g in gaps:
    title = re.search(rf'^## {re.escape(g)} (.+)$', core + '\n' + adv, re.M)
    print(f'  {g}  {title.group(1)[:56] if title else ""}')

sys.exit(1 if orphans or drift else 0)
