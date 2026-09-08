#!/usr/bin/env python3
"""Find what a non-planner hits before a real tester does.

Usability testing is expensive and the attention of three intelligent
non-planners is the scarcest input in this project. Spending it on defects a
script can find is waste, so this runs first.

Three checks, in course order, because order is the whole point — a term
defined in Module 6 is undefined in Module 2:

  JARGON     a domain term used before it is defined anywhere in the course
  ORPHAN     an instruction to do something in the app with no click path,
             in a lesson whose module has a walkthrough that never mentions it
  NUMBER     a figure spoken with no stated source and no on-screen anchor

Everything it prints is a CANDIDATE. The tool cannot tell "the app calls this
the deficit" (a definition) from "your deficit is $X" (a use). Read each hit.

  python3 tools/cold-read-audit.py            # whole core, in order
  python3 tools/cold-read-audit.py 1 2 3      # only these module numbers
"""
import os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
master = open(os.path.join(root, 'MASTER-COURSE.md'), encoding='utf-8').read()
sd = os.path.join(root, 'scripts')
want = {int(a) for a in sys.argv[1:] if a.isdigit()}

# --- lessons in course order, with their module number ----------------------
order = []
units = [(int(m.group(1)), m.start()) for m in re.finditer(r'^# Unit \d+ · Module (\d+)', master, re.M)]
for i, (mod, start) in enumerate(units):
    end = units[i + 1][1] if i + 1 < len(units) else len(master)
    for lm in re.finditer(r'^## (\d+\.\d+) (.+)$', master[start:end], re.M):
        order.append((mod, lm.group(1), lm.group(2)))

def script_for(num):
    a, b = num.split('.')
    stem = f'{int(a):02d}-{b}'
    for f in sorted(os.listdir(sd)):
        if f.startswith(stem + '_'):
            return os.path.join(sd, f)
    return None

# Terms a smart non-planner would not arrive knowing. Deliberately not
# exhaustive: these are the ones the client calls actually tripped on.
TERMS = [
 'drawdown', 'cost basis', 'tax lot', 'basis', 'UTXO', 'dust', 'seed phrase',
 'passphrase', 'multisig', 'cold storage', 'self-custody', 'DCA',
 'surplus', 'reserve', 'bridge years', 'income floor', 'the gap', 'guardrail',
 'sequence risk', 'sequence-of-returns', 'Monte Carlo', 'confidence number',
 'fat tail', 'RMD', 'Roth conversion', 'harvest', 'wash sale', 'step-up in basis',
 'tax-deferred', 'taxable account', 'asset location', 'allocation', 'drift band',
 'DTI', 'DTA', 'LTV', 'margin call', 'liquidation', 'probate', 'executor',
 'beneficiary designation', 'dead man', 'heir letter', 'trust', 'life event',
 'scenario', 'baseline', 'deficit', 'withdrawal order', 'refill rule',
 'Reserve bucket', 'Bridge bucket', 'Legacy bucket',
]
DEFINED = re.compile(
  r'(which is|which means|means|meaning|is just|is the|are the|is your|are your'
  r'|is what|refers to|stands for|I mean by|the term|in other words)', re.I)

jargon, orphan, number = [], [], []
seen = set()
for mod, num, title in order:
    if want and mod not in want:
        continue
    p = script_for(num)
    if not p:
        continue
    body = open(p, encoding='utf-8').read().split('=' * 60, 1)[-1]
    is_cap = 'WALKTHROUGH' in p or 'DEMO' in p
    sents = [s.strip() for s in re.split(r'(?<=[.?!])\s+', body.replace('\n', ' ')) if s.strip()]

    for t in TERMS:
        if t in seen:
            continue
        for s in sents:
            if re.search(rf'\b{re.escape(t)}', s, re.I):
                window = s
                if not DEFINED.search(window):
                    jargon.append((mod, num, t, s[:110]))
                seen.add(t)
                break

    if not is_cap:
        for s in sents:
            if re.search(r'\b(enter|set|open|click|go to|add|save|check) (your|the|it|that)\b', s, re.I) \
               and '→' not in s and not re.search(r'walkthrough|lesson text|below this video', s, re.I):
                orphan.append((mod, num, s[:110]))
        for s in sents:
            m = re.search(r'\$[\d,]{4,}', s)
            if m and not re.search(r'couple|example|say|illustrat|screen|suppose|imagine|their|they', s, re.I):
                number.append((mod, num, s[:110]))

def show(name, rows, note):
    print(f'\n{"="*74}\n{name}  —  {len(rows)} candidates\n{note}\n{"="*74}')
    for r in rows[:40]:
        print(f'  M{r[0]} {r[1]:>5}  ' + '  '.join(str(x) for x in r[2:]))

show('JARGON — term used before it is defined', jargon,
     'First use in course order. A hit means no definition cue in that sentence.')
show('ORPHAN ACTION — told to do it, no click path', orphan,
     'Fine if the module walkthrough covers it. Check that it does.')
show('UNSOURCED NUMBER', number,
     'A figure with no example framing. Say where it comes from, or drop it.')
print(f'\n{len(jargon)+len(orphan)+len(number)} total. Every one is a candidate, not a verdict.')
