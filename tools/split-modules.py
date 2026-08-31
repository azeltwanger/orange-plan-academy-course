#!/usr/bin/env python3
"""Regenerate modules/*.md from the course masters.

The Academy is two courses. Default splits the required core; --advanced
splits the optional library into modules/advanced/.

    python3 tools/split-modules.py
    python3 tools/split-modules.py --advanced

Module files are derived. Never edit them directly; edit the master and rerun.
The canonical filenames stay stable so course links do not change when a unit
heading is reworded.
"""
import os, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADVANCED = '--advanced' in sys.argv
SRC = 'MASTER-ADVANCED.md' if ADVANCED else 'MASTER-COURSE.md'
OUT = os.path.join(root, 'modules', 'advanced') if ADVANCED else os.path.join(root, 'modules')
HEADER = '# Advanced Module ' if ADVANCED else '# Unit '
os.makedirs(OUT, exist_ok=True)

CORE_FILENAMES = [
    '00-start-here.md',
    '01-foundation.md',
    '02-cash-flow-reserve.md',
    '03-allocation-next-dollar.md',
    '04-debt-strategy.md',
    '05-tax-strategy.md',
    '06-retirement-income.md',
    '07-custody.md',
    '08-estate-inheritance.md',
    '09-finish-test-maintain.md',
]

ADVANCED_FILENAMES = [
    'A01-foundation.md',
    'A03-allocation-next-dollar.md',
    'A04-debt-strategy.md',
    'A05-tax-strategy.md',
    'A06-retirement-income.md',
    'A07-custody.md',
    'A08-estate-inheritance.md',
]

t = open(os.path.join(root, SRC), encoding='utf-8').read()
L = t.split('\n')
idx = [i for i, l in enumerate(L) if l.startswith(HEADER)]
assert idx, f"no '{HEADER}' headings found in {SRC}"

filenames = ADVANCED_FILENAMES if ADVANCED else CORE_FILENAMES
assert len(idx) == len(filenames), (
    f"{SRC} has {len(idx)} module headings but {len(filenames)} canonical filenames"
)

written = set()
for k, a in enumerate(idx):
    b = idx[k + 1] if k + 1 < len(idx) else len(L)
    name = filenames[k]
    p = os.path.join(OUT, name)
    open(p, 'w', encoding='utf-8').write('\n'.join(L[a:b]).strip() + '\n')
    written.add(name)
    print(f"wrote {os.path.relpath(p, root)}")

# A generated directory mirrors its source. Remove stale renamed copies.
for f in sorted(os.listdir(OUT)):
    if f.endswith('.md') and f not in written:
        os.remove(os.path.join(OUT, f))
        print(f"  removed stale {os.path.relpath(os.path.join(OUT, f), root)}")
