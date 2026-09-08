#!/usr/bin/env python3
"""Generate CIRCLE-STRUCTURE.md — the paste-ready course build for Circle.

The student-facing answer to the four stalls the 24 client calls found. Each
module block, in order, gives a student:

  what they will BUILD          -> "am I finished?" has an object, not a feeling
  which lessons are REQUIRED    -> "does this apply to me?" is answered up front
  which are OPTIONAL, and when  -> college is skippable without guessing
  the CHECKPOINT                -> the finish line, checkable by them
  the ADVANCED lessons + gates  -> optional next levels, each with its condition

Everything here already exists somewhere in the repo. This assembles it so
nothing is retyped into Circle by hand, because a hand-typed copy is what went
stale in the README, the shoot list, the dictation order and the film order.

Sources, all of them generated-from or authored-in exactly one place:
  MASTER-COURSE.md      module order, lesson numbers, titles, optional markers
  MASTER-ADVANCED.md    the Gate line on every advanced lesson
  MODULE-CHECKPOINTS.md "You will build" and the completion checklist
  scripts/              measured runtimes, and which sheet covers which capture

Run:  python3 tools/build-circle-structure.py
"""
import os, re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
core = open(os.path.join(root, 'MASTER-COURSE.md'), encoding='utf-8').read()
adv = open(os.path.join(root, 'MASTER-ADVANCED.md'), encoding='utf-8').read()
cps = open(os.path.join(root, 'MODULE-CHECKPOINTS.md'), encoding='utf-8').read()
sd = os.path.join(root, 'scripts')

# --- runtimes, and which sheet covers which capture -------------------------
runtime, sheet_of = {}, {}
for f in sorted(os.listdir(sd)):
    if not f.endswith('.md') or f in ('README.md', 'VOICE-GUIDE.md'):
        continue
    stem = f.split('_')[0].removesuffix('-A')
    num = f'{int(stem.split("-")[0])}.{stem.split("-")[1]}'
    body = open(os.path.join(sd, f), encoding='utf-8').read()
    runtime[num] = len(body.split('=' * 60, 1)[-1].split()) / 155
    if 'WALKTHROUGH' in f or 'DEMO' in f:
        nums = re.findall(r'\d+\.\d+', body.split('\n', 1)[0].split('·')[0])
        for n in nums:
            sheet_of[n] = nums

# --- checkpoints ------------------------------------------------------------
build, checklist = {}, {}
blocks = list(re.finditer(r'^## Module (\d+) — (.+)$', cps, re.M))
for i, m in enumerate(blocks):
    e = blocks[i + 1].start() if i + 1 < len(blocks) else len(cps)
    seg = cps[m.start():e]
    mod = int(m.group(1))
    b = re.search(r'\*\*You will build:\*\* (.+)', seg)
    build[mod] = b.group(1).strip() if b else ''
    checklist[mod] = [l.rstrip() for l in seg.split('\n') if l.strip().startswith('- [ ]')]

# --- advanced lessons, grouped by the core module they extend ---------------
adv_by_mod = {}
units = list(re.finditer(r'^# Advanced Module (\d+) — (.+)$', adv, re.M))
for i, m in enumerate(units):
    e = units[i + 1].start() if i + 1 < len(units) else len(adv)
    seg = adv[m.start():e]
    rows = []
    for lm in re.finditer(r'^## (\S+) (.+)$', seg, re.M):
        after = seg[lm.end():lm.end() + 1500]
        g = re.search(r'> \*\*Gate\.\*\*\s*(.+?)(?:\n\n|\n\*\*By the end)', after, re.S)
        cond = re.sub(r'\s+', ' ', g.group(1).replace('>', '')).strip() if g else ''
        blocked = bool(re.search(r'DO NOT FILM|TEXT-ONLY FOR v1', after))
        rows.append((lm.group(1), lm.group(2), cond, blocked))
    adv_by_mod[int(m.group(1))] = rows

out = ['# Circle structure — paste-ready course build', '',
       '> **GENERATED** by `tools/build-circle-structure.py`. Do not hand-edit:',
       '> edit the master, `MODULE-CHECKPOINTS.md`, or the advanced Gate line, then',
       '> regenerate. A hand-typed copy of any of this is what went stale in the',
       '> README, the shoot list, the dictation order and the film order.', '',
       'Build the space group in this order. Each module below is one Circle',
       'section; each numbered row is one lesson inside it.', '',
       '**Four things every module page needs, in this order:** what you will build',
       '· the lessons · the checkpoint · the optional next levels. That order is the',
       'answer to the four stalls the client calls found — *does this apply to me*,',
       '*is this required*, *am I finished*, *what do I do next*.', '',
       '---', '']

cunits = list(re.finditer(r'^# Unit \d+ · Module (\d+) — (.+)$', core, re.M))
for i, m in enumerate(cunits):
    e = cunits[i + 1].start() if i + 1 < len(cunits) else len(core)
    seg, mod, name = core[m.start():e], int(m.group(1)), m.group(2)
    out += [f'## Module {mod} — {name}', '']
    if build.get(mod):
        out += [f'### 📦 What you will build', '', f'**{build[mod]}**', '',
                'The module is complete when this exists. Not when the videos are',
                'watched — watching is not the deliverable, a plan is.', '']

    out += ['### Lessons', '']
    optional_rows = []
    for lm in re.finditer(r'^## (\d+\.\d+) (.+)$', seg, re.M):
        n, t = lm.group(1), lm.group(2)
        cap = t.lower().startswith(('walkthrough', 'external demo'))
        opt = t.lower().startswith('optional')
        mins = runtime.get(n)
        if cap:
            share = ''
            if n in sheet_of and len(sheet_of[n]) > 1:
                other = ' + '.join(x for x in sheet_of[n] if x != n)
                share = f' · filmed in one session with {other}, published separately'
            out.append(f'- **{n} {t}** — 🖥 walkthrough{share}')
        elif opt:
            optional_rows.append((n, t))
            out.append(f'- **{n} {t}** — 🎙 ~{mins:.0f} min · **OPTIONAL**')
        else:
            out.append(f'- **{n} {t}** — 🎙 ~{mins:.0f} min')
    out.append('')

    for n, t in optional_rows:
        label = t.split(':', 1)[-1].strip() if ':' in t else t
        out += [f'> ### ⭕ Optional in this module: {label}', '>',
                f'> **Complete {n} only if it applies to you.** If it does not, your',
                f'> Module {mod} plan is complete without it, and nothing later in the',
                '> course depends on it.', '',
                '*Paste that callout directly above the lesson in Circle, so a student',
                'decides before watching rather than seven minutes in.*', '']

    if checklist.get(mod):
        out += ['### ✅ Checkpoint — paste at the bottom of the module page', '',
                '**You are done when:**', ''] + checklist[mod] + ['',
                '> **"Not applicable" is a completed line, not a skipped one.** A',
                '> household the line was never about completes it by saying so.', '']

    rows = adv_by_mod.get(mod, [])
    if rows:
        out += ['### 🔓 Optional next levels', '',
                '**Your core plan is complete without any of these.** Each one is worth',
                'watching only when its condition is true for you:', '']
        for num, title, cond, blocked in rows:
            out.append(f'- **{num} {title}**' + ('  🔴 *not yet published*' if blocked else ''))
            out.append(f'  → *{cond}*' if cond else
                       '  → *(no gate condition set — add one to MASTER-ADVANCED.md)*')
        out.append('')
    else:
        out += ['### 🔓 Optional next levels', '',
                '*None for this module. The core lessons are the whole of it.*', '']
    out += ['---', '']

n_opt = sum(1 for u in cunits
            for _ in re.finditer(r'^## \d+\.\d+ Optional', core[u.start():], re.M))
p = os.path.join(root, 'CIRCLE-STRUCTURE.md')
open(p, 'w', encoding='utf-8').write('\n'.join(out))
print(f'CIRCLE-STRUCTURE.md regenerated — {len(cunits)} modules, '
      f'{sum(len(v) for v in adv_by_mod.values())} advanced lessons routed')
