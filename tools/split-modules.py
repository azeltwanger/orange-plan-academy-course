#!/usr/bin/env python3
"""Regenerate modules/*.md from the course masters.

The Academy is two courses. Default splits the required core; --advanced
splits the optional library into modules/advanced/.

    python3 tools/split-modules.py
    python3 tools/split-modules.py --advanced

Module files are derived. Never edit them directly; edit the master and rerun.
"""
import re, os, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADVANCED = '--advanced' in sys.argv
SRC = 'MASTER-ADVANCED.md' if ADVANCED else 'MASTER-COURSE.md'
OUT = os.path.join(root, 'modules', 'advanced') if ADVANCED else os.path.join(root, 'modules')
HEADER = '# Advanced Module ' if ADVANCED else '# Unit '
os.makedirs(OUT, exist_ok=True)

t = open(os.path.join(root, SRC), encoding='utf-8').read()
L = t.split('\n')
idx = [i for i, l in enumerate(L) if l.startswith(HEADER)]
assert idx, f"no '{HEADER}' headings found in {SRC}"


def slugify(line):
    """'# Unit 6 · Module 5 — Tax Strategy' -> 'module-5-tax-strategy'."""
    s = line.lstrip('# ').split('·')[-1]
    s = s.replace('—', ' ').replace('-', ' ')
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    return s[:44]


written = set()
for k, a in enumerate(idx):
    b = idx[k + 1] if k + 1 < len(idx) else len(L)
    name = f'{k:02d}-{slugify(L[a])}'
    p = os.path.join(OUT, f'{name}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L[a:b]).strip() + '\n')
    written.add(f'{name}.md')
    print(f"wrote {os.path.relpath(p, root)}")

# Prune anything this run did not write. Without it, RENAMING a module leaves the
# old slug behind forever, because this script only ever wrote and never deleted.
# That is not hypothetical: swapping Debt and Allocation left
# '02-advanced-module-3-allocation-and-asset-locat.md' and
# '03-advanced-module-4-debt-and-bitcoin-backed-lo.md' orphaned in the tree, and
# the stale copy of A3.1 inside one of them still carried the pre-revert LTV text
# that AUTHORITY-FLAGS records as reverted. A generated directory has to be a
# mirror of its source, not an accumulation of every name it has ever had.
for f in sorted(os.listdir(OUT)):
    if f.endswith('.md') and f not in written:
        os.remove(os.path.join(OUT, f))
        print(f"  removed stale {os.path.relpath(os.path.join(OUT, f), root)}")
