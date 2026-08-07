#!/usr/bin/env python3
"""Push a trimmed teleprompter script back into the master, body only.

The standing hazard in this repo runs the other way — a master edit never
reaches a protected script — but a trim pass creates the mirror problem: the
script gets cut and the master keeps the removed teaching, so the two layers
disagree about what the course says. This closes that.

It replaces ONLY the body of the master lesson. The header block is preserved
verbatim: the `*TEACH*` metadata line, the `>` flags, and the outcomes list
are editorial and belong to the master. The word/minute figures in the
metadata line are refreshed from the script.

  python3 tools/sync-master-from-script.py 7.1 9.2 10.1
  python3 tools/sync-master-from-script.py --advanced 8.5

Verify the result: outcomes lists are NOT auto-updated, so if a trim removed
an outcome, fix that line by hand. The tool prints a warning when the body no
longer mentions a word from one of the outcomes.
"""
import re, os, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADV = '--advanced' in sys.argv
nums = [a for a in sys.argv[1:] if not a.startswith('--')]
if not nums:
    sys.exit(__doc__)

mpath = os.path.join(root, 'MASTER-ADVANCED.md' if ADV else 'MASTER-COURSE.md')
sdir = os.path.join(root, 'scripts', 'advanced') if ADV else os.path.join(root, 'scripts')
master = open(mpath, encoding='utf-8').read()


def script_for(num):
    mod, sub = num.split('.', 1)
    stem = f'{mod}-{sub}' if mod.startswith('A') else f'{int(mod):02d}-{sub}'
    for f in sorted(os.listdir(sdir)):
        if f.startswith(stem + '_') or f.startswith(stem + '-A_'):
            return os.path.join(sdir, f)
    return None


def to_master(body):
    """Teleprompter conventions -> master markdown."""
    out = []
    for line in body.split('\n'):
        m = re.match(r'^== (.+) ==$', line)
        if m:
            # Prompter headings are shouted. Sentence-case them, but acronyms
            # stay shouted or you get "The ai does not do your math".
            KEEP = {'AI', 'LTV', 'DTI', 'DTA', 'HSA', 'PDF', 'RMD', 'UTXO',
                    'UTXOS', 'US', 'SS', 'IRA', 'CPA', 'ETF', 'PIN', 'FDIC',
                    'W-2', 'HVAC', 'SSA', 'BTC'}
            words = m.group(1).split()
            cased = [w if w.strip('.,:').upper() in KEEP else w.lower()
                     for w in words]
            head = ' '.join(cased)
            out.append('### ' + head[0].upper() + head[1:])
            continue
        if line.startswith('🎬 '):
            out.append('> 🎬 **' + line[2:].strip() + '**')
            continue
        out.append(line)
    return '\n'.join(out)


for num in nums:
    sp = script_for(num)
    if not sp:
        print(f'  !! {num}: no script found'); continue
    body = open(sp, encoding='utf-8').read().split('=' * 60, 1)[-1].strip()
    words = len(body.split())

    start = master.find(f'\n## {num} ')
    if start < 0:
        print(f'  !! {num}: not in {os.path.basename(mpath)}'); continue
    start += 1
    nxt = re.search(r'\n## (?:A?\d+\.\d+|✂)|\n# Unit ', master[start + 5:])
    end = start + 5 + nxt.start() + 1 if nxt else len(master)
    section = master[start:end]

    # header = everything through the '---' that closes the outcomes block
    parts = section.split('\n---\n', 1)
    if len(parts) != 2:
        print(f'  !! {num}: no header/body divider, skipped'); continue
    header, old_body = parts

    # The master body is sometimes DELIBERATELY richer than the script: a
    # prompter can't read a table, so several lessons carry the comparison as
    # prose on camera and as a table in the master. Overwriting that with the
    # spoken version silently destroys the better reference. Refuse, unless
    # told otherwise.
    m_tables = old_body.count('\n|')
    s_tables = body.count('\n|')
    if m_tables > s_tables and '--force' not in sys.argv:
        print(f'  !! {num}: master body has {m_tables} table rows the script '
              f'does not. Refusing — sync by hand, or pass --force to discard '
              f'them.')
        continue

    header = re.sub(r'· [\d,~]+ words · ~[\d.]+ min',
                    f'· ~{words:,} words · ~{words/155:.0f} min', header)

    # warn if an outcome now names something the trimmed body dropped
    for oc in re.findall(r'^- (.+)$', header, re.M):
        key = [w for w in re.findall(r'\b[a-z]{6,}\b', oc.lower())]
        if key and not any(k in body.lower() for k in key):
            print(f'  ?? {num}: outcome may be stale -> "{oc}"')

    master = master[:start] + header + '\n---\n\n' + to_master(body) + '\n\n\n' + master[end:]
    print(f'  ok {num}: body synced, {words:,} words / {words/155:.1f} min')

open(mpath, 'w', encoding='utf-8').write(master)
print(f'wrote {os.path.basename(mpath)}')
