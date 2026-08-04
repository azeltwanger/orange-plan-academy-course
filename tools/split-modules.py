#!/usr/bin/env python3
"""Regenerate modules/*.md from MASTER-COURSE.md (the canonical file).

Run after editing the master, before refreshing Google Drive:
    python3 tools/split-modules.py
"""
import re, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
t = open(os.path.join(root, 'MASTER-COURSE.md'), encoding='utf-8').read()
L = t.split('\n')
idx = [i for i, l in enumerate(L) if l.startswith('# Unit ')]
assert len(idx) == 11, f"expected 11 units, found {len(idx)}"
names = ['01-module-0-start-here','02-module-1-foundation','03-module-2-cashflow-reserve',
'04-module-3-allocation','05-module-4-debt','06-module-5-tax','07-module-6-retirement-income',
'08-module-7-custody','09-module-8-estate','10-module-9-maintenance','11-module-10-plan-review']
for k, (a, name) in enumerate(zip(idx, names)):
    b = idx[k+1] if k+1 < len(idx) else len(L)
    p = os.path.join(root, 'modules', f'{name}.md')
    open(p, 'w', encoding='utf-8').write('\n'.join(L[a:b]).strip() + '\n')
    print(f"wrote {p}")
