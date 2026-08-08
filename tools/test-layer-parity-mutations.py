#!/usr/bin/env python3
"""Prove that check-layer-parity.py actually fails when a layer drifts.

A gate that has never failed is not a gate, and until this file existed the
mutation tests were a paragraph of prose describing edits somebody once made by
hand. That is not a test — nobody re-runs it, and an early hand-run of mutation 2
passed falsely because it changed one instance of a claim that appears twice.

Each mutation:

  1. copies the target file(s) to a temp directory
  2. applies exactly one mutation
  3. runs the checker
  4. requires a NON-ZERO exit
  5. restores the file(s) in a finally block, so a crash cannot leave the repo
     mutated
  6. repeats for every class

Exit 1 if any mutation SURVIVES — that is, if the checker still passes while the
repo is deliberately broken.

Run this when the checker or the registry changes. The five normal gates run on
every content change; this one runs when the thing doing the checking changes.

  python3 tools/test-layer-parity-mutations.py
  python3 tools/test-layer-parity-mutations.py -v    # show the checker's output
"""
import os, re, shutil, subprocess, sys, tempfile

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKER = os.path.join(root, 'tools', 'check-layer-parity.py')
VERBOSE = '-v' in sys.argv


def checker_passes():
    r = subprocess.run([sys.executable, CHECKER], capture_output=True, text=True)
    if VERBOSE:
        print('    ' + '\n    '.join(r.stdout.strip().split('\n')[-6:]))
    return r.returncode == 0


def sub_all(path, pairs):
    """Replace EVERY occurrence. Mutating one instance of a claim that appears
    twice in a layer proves nothing — that is the false pass this guards."""
    p = os.path.join(root, path)
    t = open(p, encoding='utf-8').read()
    for a, b in pairs:
        t = t.replace(a, b)
    open(p, 'w', encoding='utf-8').write(t)


def insert_after(path, anchor, text):
    p = os.path.join(root, path)
    t = open(p, encoding='utf-8').read()
    assert anchor in t, f'anchor not found in {path}: {anchor[:50]}'
    open(p, 'w', encoding='utf-8').write(t.replace(anchor, anchor + text, 1))


THRESH = [('0.01 to 0.02 Bitcoin', 'a sensible amount of Bitcoin'),
          ('0.01–0.02 BTC', 'a sensible BTC')]

# (name, [files it touches], mutate fn, what a pass would mean)
MUTATIONS = [
    ('retired phrasing returns in the master',
     ['MASTER-ADVANCED.md'],
     lambda: sub_all('MASTER-ADVANCED.md', [
         ('My rule of thumb is about 0.01 to 0.02 Bitcoin as a minimum per transfer.',
          "Now, I'm deliberately not going to give you a fixed number of Bitcoin here.")]),
     'a reverted position could come back'),

    ('silent omission from the MASTER only',
     ['MASTER-ADVANCED.md'],
     lambda: sub_all('MASTER-ADVANCED.md', THRESH),
     'a claim could vanish from one layer with no forbidden phrase to catch it'),

    ('paraphrase in LESSON-TEXT only',
     ['lesson-text/advanced/A7-4_wallet-operations.md'],
     lambda: sub_all('lesson-text/advanced/A7-4_wallet-operations.md',
                     [('0.01 to 0.02 Bitcoin', 'roughly one to two hundredths of a Bitcoin')]),
     'one layer could be reworded away from the approved position'),

    ('stale GENERATED module only',
     ['modules/advanced/06-advanced-module-7-advanced-custody.md'],
     lambda: sub_all('modules/advanced/06-advanced-module-7-advanced-custody.md', THRESH),
     'a generated layer could go stale while every hand-edited layer is correct'),

    ('duplicate module file left by a rename',
     ['modules/advanced/06-advanced-module-7-advanced-custody.md'],
     lambda: shutil.copy(
         os.path.join(root, 'modules/advanced/06-advanced-module-7-advanced-custody.md'),
         os.path.join(root, 'modules/advanced/99-stale-rename-copy.md')),
     'a stale copy from a rename could hide behind "the first match"'),

    # The two classes the scoped MUST NOT rule used to miss entirely.
    ('retired cost-lane table reinserted into the MASTER only',
     ['MASTER-COURSE.md'],
     lambda: insert_after(
         'MASTER-COURSE.md',
         '## 2.3 Fund a known future cost: the six questions',
         '\n\n| 3 to 10 years | Balanced stocks/bonds, I-Bonds | Bitcoin |\n'),
     'the retired table could return to the master, which the filename-scoped '
     'rule never examined'),

    ('flat beneficiary claim inserted into the VISUAL only',
     ['visuals/8-1_form-generally-controls.md'],
     lambda: insert_after(
         'visuals/8-1_form-generally-controls.md',
         '## Labels and data\n',
         'Caption across the arrow: the form overrides the will.\n'),
     'a graphic could contradict all four text layers with every gate green'),
]


def main():
    if not checker_passes():
        print('ABORT: the checker already fails on a clean tree. Fix that first —\n'
              '       a mutation test means nothing if the baseline is red.')
        return 1

    print(f'baseline clean · running {len(MUTATIONS)} mutation classes\n')
    survived = []
    for i, (name, files, mutate, consequence) in enumerate(MUTATIONS, 1):
        tmp = tempfile.mkdtemp(prefix='parity-mut-')
        backups = {f: os.path.join(tmp, f'{i}-{os.path.basename(f)}') for f in files}
        added = os.path.join(root, 'modules/advanced/99-stale-rename-copy.md')
        try:
            for f, b in backups.items():
                shutil.copy(os.path.join(root, f), b)
            mutate()
            caught = not checker_passes()
            print(f'{i}. {name:58} {"CAUGHT" if caught else "*** SURVIVED ***"}')
            if not caught:
                survived.append((name, consequence))
        finally:
            # Restore no matter what, including on an exception inside mutate().
            for f, b in backups.items():
                shutil.copy(b, os.path.join(root, f))
            if os.path.exists(added):
                os.remove(added)
            shutil.rmtree(tmp, ignore_errors=True)

    if not checker_passes():
        print('\nERROR: the tree did not come back clean after restore. '
              'Check `git status` before doing anything else.')
        return 1

    print()
    if survived:
        print(f'{len(survived)} mutation(s) SURVIVED — the gate does not catch:')
        for name, why in survived:
            print(f'  - {name}\n      consequence: {why}')
        return 1
    print(f'all {len(MUTATIONS)} mutations caught · tree restored clean')
    return 0


if __name__ == '__main__':
    sys.exit(main())
