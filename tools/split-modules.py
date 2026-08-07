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


for k, a in enumerate(idx):
    b = idx[k + 1] if k + 1 < len(idx) else len(L)
    name = f'{k:02d}-{slugify(L[a])}'
    p = os.path.join(OUT, f'{name}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L[a:b]).strip() + '\n')
    print(f"wrote {os.path.relpath(p, root)}")
