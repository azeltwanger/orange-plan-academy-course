#!/usr/bin/env python3
"""Apply edits made in a combined ALL-SCRIPTS.md back into scripts/.

    python3 tools/apply-onefile.py <edited-all-scripts.md>

Splits on the per-lesson `filename.md` marker, restores each script's own
teleprompter header (or walkthrough H1), and writes the edited body back.
Reports every file changed. Never creates or deletes files.
"""
import re, os, sys, difflib

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src  = open(sys.argv[1], encoding='utf-8').read()
sdir = os.path.join(root, 'scripts')

# sections look like:  `NN-N_slug.md` · TEACH · ~6 min · 859 words\n\n<body>
pat = re.compile(r'^`([0-9][^`]+\.md)`[^\n]*\n(.*?)(?=\n<a id=|\n---\n\n# |\Z)', re.M | re.S)
found = pat.findall(src)
print(f'sections found: {len(found)}')

changed, missing, same = [], [], 0
for fname, body in found:
    path = os.path.join(sdir, fname)
    if not os.path.exists(path):
        missing.append(fname); continue
    cur = open(path, encoding='utf-8').read()
    lines = cur.split('\n')

    # rebuild: original header + edited body
    if lines[0].startswith('TELEPROMPTER'):
        for i, ln in enumerate(lines):
            if set(ln.strip()) == {'='}:
                header = '\n'.join(lines[:i+1]) + '\n\n'
                break
    elif lines[0].startswith('# '):
        header = lines[0] + '\n\n'
    else:
        header = ''

    new = header + body.strip() + '\n'
    if new == cur:
        same += 1
    else:
        open(path, 'w', encoding='utf-8').write(new)
        d = list(difflib.unified_diff(cur.split('\n'), new.split('\n'), lineterm='', n=0))
        changed.append((fname, sum(1 for l in d if l.startswith(('+', '-')) and not l.startswith(('+++', '---')))))

print(f'unchanged: {same}   changed: {len(changed)}')
for f, n in changed: print(f'  {n:4} line-changes  {f}')
if missing: print('NOT FOUND in scripts/:'); [print('  ', m) for m in missing]
