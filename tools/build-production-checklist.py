#!/usr/bin/env python3
"""Regenerate the per-lesson filming checklist from the current masters.

PRODUCTION-CHECKLIST used to hold a hand-typed list of every lesson to film.
It drifted exactly like the shoot list and the dictation order did — still
naming 11.1, 8.6 and an Allocation module numbered 3 long after none of that
was true. Filming from a stale checklist is the most expensive mistake
available at this stage, so it is generated.

Everything above the '## ☐ ONE-TIME SETUP' heading is preserved; the per-module
list below it is rebuilt.

Run:  python3 tools/build-production-checklist.py
"""
import os, re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
core = open(os.path.join(root, 'MASTER-COURSE.md'), encoding='utf-8').read()
adv = open(os.path.join(root, 'MASTER-ADVANCED.md'), encoding='utf-8').read()
sd = os.path.join(root, 'scripts')

runtime = {}
for d in (sd, os.path.join(sd, 'advanced')):
    for f in sorted(os.listdir(d)):
        if not f.endswith('.md') or f in ('README.md', 'VOICE-GUIDE.md'):
            continue
        stem = f.split('_')[0]
        num = (stem.replace('-', '.', 1) if stem[0] == 'A'
               else f'{int(stem.split("-")[0])}.{stem.split("-")[1]}')
        body = open(os.path.join(d, f), encoding='utf-8').read().split('=' * 60, 1)[-1]
        runtime[num] = len(body.split()) / 155

out = []
units = [(m.group(1), m.start()) for m in re.finditer(r'^# Unit \d+ · (Module .+)$', core, re.M)]
wave = {'Module 0': 1, 'Module 1': 1, 'Module 2': 1, 'Module 3': 1, 'Module 4': 1}
for i, (name, s) in enumerate(units):
    e = units[i + 1][1] if i + 1 < len(units) else len(core)
    key = name.split(' —')[0]
    out += ['', f'## ☐ {name.upper()}   ·   WAVE {wave.get(key, 2)}', '']
    for lm in re.finditer(r'^## (\d+\.\d+) (.+)$', core[s:e], re.M):
        n, t = lm.group(1), lm.group(2)
        cap = t.lower().startswith(('walkthrough', 'external demo'))
        mins = runtime.get(n)
        mark = '🖥 capture' if cap else '🎙 film'
        dur = '' if cap else f' (~{mins:.0f} min)' if mins else ''
        out.append(f'☐ {n} {t} — {mark}{dur}')
    out.append(f'☐ Paste the Module {key.split()[-1]} checkpoint into Circle '
               f'(top: "By the end…", bottom: "Complete when…")')

out += ['', '## ☐ ADVANCED LIBRARY — text first, video in demand order', '',
        '*Publish every advanced lesson as student-facing TEXT at launch. Film in this order afterwards.*', '']
DEMAND = ['6.3', 'A3.1', '7.4', '6.4', '8.5', '9.5', '7.2']
seen = set()
for j, n in enumerate(DEMAND, 1):
    m = re.search(rf'^## {re.escape(n)} (.+)$', adv, re.M)
    if m:
        out.append(f'☐ {j}. {n} {m.group(1)} — 🎙 film (~{runtime.get(n, 0):.0f} min)')
        seen.add(n)
for m in re.finditer(r'^## (A?\d+\.\d+) (.+)$', adv, re.M):
    if m.group(1) not in seen:
        out.append(f'☐ — {m.group(1)} {m.group(2)} — TEXT ONLY for now')

p = os.path.join(root, 'PRODUCTION-CHECKLIST.md')
old = open(p, encoding='utf-8').read()
head = old.split('## ☐ ONE-TIME SETUP')[0].rstrip()
setup = old.split('## ☐ ONE-TIME SETUP', 1)[1].split('\n## ', 1)[0]
open(p, 'w', encoding='utf-8').write(
    head + '\n\n> **The per-lesson list below is GENERATED** by\n'
    '> `tools/build-production-checklist.py`. Regenerate it before every shoot\n'
    '> day. Do not hand-edit it — that is how the last one ended up naming\n'
    '> lessons that no longer exist.\n\n'
    '## ☐ ONE-TIME SETUP' + setup + '\n' + '\n'.join(out) + '\n')
print('PRODUCTION-CHECKLIST.md regenerated')
