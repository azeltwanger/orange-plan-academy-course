#!/usr/bin/env python3
"""Validate every lesson-number and module-number reference in the repo.

Renumbering is where a course quietly breaks. A reference to a lesson that
moved still reads fine — it just sends the student somewhere wrong, and
nobody notices until it is on camera.

Checks:
  DEAD LESSON   "lesson 4.1" / "segment 5.2" pointing at a number that no
                longer exists in either master
  WRONG MODULE  "Module N" where N is outside the current 0-9 range, or
                names a module that no longer exists
  SELF-REF      a walkthrough sheet naming a lesson number that isn't in its
                own module — usually a stale copy from before a swap

Exit code 1 if anything is found, so it can gate a content freeze.

  python3 tools/check-crossrefs.py
"""
import os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
core = open(os.path.join(root, 'MASTER-COURSE.md'), encoding='utf-8').read()
adv = open(os.path.join(root, 'MASTER-ADVANCED.md'), encoding='utf-8').read()

valid = {m.group(1) for m in re.finditer(r'^## (\d+\.\d+) ', core, re.M)}
valid |= {m.group(1) for m in re.finditer(r'^## (A?\d+\.\d+) ', adv, re.M)}
modules = {int(m.group(1)) for m in re.finditer(r'^# Unit \d+ · Module (\d+)', core, re.M)}
module_of = {}
units = [(int(m.group(1)), m.start()) for m in re.finditer(r'^# Unit \d+ · Module (\d+)', core, re.M)]
for i, (mod, s) in enumerate(units):
    e = units[i + 1][1] if i + 1 < len(units) else len(core)
    for lm in re.finditer(r'^## (\d+\.\d+) ', core[s:e], re.M):
        module_of[lm.group(1)] = mod

FILES = []
for d in ('.', 'scripts', 'scripts/advanced', 'lesson-text', 'lesson-text/advanced'):
    p = os.path.join(root, d)
    if not os.path.isdir(p):
        continue
    for f in sorted(os.listdir(p)):
        # Generated files are rebuilt from the masters, so they cannot drift.
        # Two HISTORICAL files are excluded for the same reason as each other:
        # their references to retired lesson and module numbers are correct in
        # their own context and must not be "fixed" into a false record.
        #   COURSE-IMPROVEMENT-ANALYSIS.md — the decision log.
        #   FILMING-CHECKLIST.md — archived 2026-08-08. Its banner deliberately
        #     names the Module 10 it used to reference, as evidence of why it was
        #     retired. Rewording that to satisfy this checker would delete the
        #     finding. Anything still filming from that file is the real problem,
        #     and the banner is what prevents it.
        #   CLAIM-REGISTRY.md — the rule that FORBIDS "Module 10" has to quote it
        #     to match it. Scanning the registry means this checker fights the
        #     gate that enforces the same thing one layer down.
        if f.endswith('.md') and f not in ('ALL-SCRIPTS.md', 'FILM-ORDER.md',
                                           'DICTATION-ORDER.md', 'SCREEN-SHOOT-LIST.md',
                                           'PRODUCTION-CHECKLIST.md',
                                           'COURSE-IMPROVEMENT-ANALYSIS.md',
                                           'FILMING-CHECKLIST.md',
                                           'CLAIM-REGISTRY.md'):
            FILES.append(os.path.join(d, f))

REF = re.compile(r'\b(?:lesson|segment|walkthrough|see|in)\s+(A?\d+\.\d+)\b', re.I)
MOD = re.compile(r'\bModule\s+(\d+)\b')
dead, badmod, selfref = [], [], []

for rel in FILES:
    p = os.path.join(root, rel)
    text = open(p, encoding='utf-8').read()
    own = None
    base = os.path.basename(rel)
    if base[:2].isdigit():
        a, _, b = base.split('_')[0].partition('-')
        own = f'{int(a)}.{b.rstrip("-A")}'
    for ln, line in enumerate(text.split('\n'), 1):
        if line.lstrip().startswith(('>', '*`')) and 'Gate' not in line:
            pass                                    # flags still get checked
        for m in REF.finditer(line):
            n = m.group(1)
            if n not in valid:
                dead.append((rel, ln, n, line.strip()[:78]))
            elif own and own in module_of and n in module_of and \
                    'WALKTHROUGH' in base and module_of[n] != module_of[own]:
                selfref.append((rel, ln, n, line.strip()[:78]))
        for m in MOD.finditer(line):
            if int(m.group(1)) not in modules:
                badmod.append((rel, ln, m.group(1), line.strip()[:78]))

def show(name, rows):
    print(f'\n{name}  —  {len(rows)}')
    for r in rows:
        print(f'  {r[0]}:{r[1]}  [{r[2]}]  {r[3]}')

show('DEAD LESSON REFERENCE', dead)
show('MODULE NUMBER OUT OF RANGE', badmod)
show('WALKTHROUGH NAMING ANOTHER MODULE\'S LESSON', selfref)
total = len(dead) + len(badmod) + len(selfref)
print(f'\n{total} problems. Valid lessons: {len(valid)}. Modules: {sorted(modules)}')
sys.exit(1 if total else 0)
