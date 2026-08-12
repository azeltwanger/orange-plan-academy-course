"""The spoken body of a teleprompter script — nothing else.

Every runtime figure in this repo is words divided by 155. That makes the
word count a production fact, not a nicety: it sets the dictation schedule,
the per-module minutes, the course total, and the shoot estimates.

The rule used to be `text.split('=' * 60, 1)[-1]`, which takes EVERYTHING
after the first separator. Two kinds of non-spoken text live down there:

  - a `>>> ... <<<` note block telling Austin what changed in his dictation,
    which every re-dictated script carries; and
  - a trailing `NOT YET DICTATED` appendix, a draft waiting for him to say it.

Both were being counted as finished audio. Found 2026-08-11, when editing a
note block in 0.1 moved its runtime in DICTATION-ORDER.md — the note was in
the number. Five tools shared the bug, so the figure was wrong the same way
everywhere and nothing disagreed with anything.

`sync-master-from-script.py` uses this for a second reason: under the old
rule, a block explicitly marked NOT YET DICTATED was pushed into the master
as though Austin had already said it.
"""

SEP = '=' * 60


def script_body(raw):
    """Spoken text only: no metadata header, no note blocks, no draft appendix."""
    out = []
    for part in raw.split(SEP)[1:]:          # drop the metadata header
        stripped = part.strip()
        if stripped[:40].upper().startswith('NOT YET DICTATED'):
            break                            # draft appendix, and everything after it
        if stripped.startswith('>>>'):
            continue                         # production note to Austin
        out.append(part)
    return '\n'.join(out).strip()


def spoken_words(raw):
    return len(script_body(raw).split())


def runtime_min(raw, wpm=155):
    return spoken_words(raw) / wpm


if __name__ == '__main__':
    # Self-test. The bug this module exists to prevent is silent — a wrong
    # runtime looks exactly like a right one — so the contract is asserted
    # here rather than trusted.
    import sys
    SAMPLE = (
        'TELEPROMPTER SCRIPT — segment 9.9\n9.9 Example\n~1 min · AUSTIN DICTATION\n'
        + SEP + '\n\n>>> A NOTE TO AUSTIN <<<\nnotenote notenote\n'
        + SEP + '\n\nspoken one two three\n\n'
        + SEP + '\nNOT YET DICTATED — draft below.\n'
        + SEP + '\n\ndraft draft draft draft\n')
    body = script_body(SAMPLE)
    fails = []
    if 'spoken one two three' not in body:
        fails.append('spoken text was dropped')
    if 'notenote' in body:
        fails.append('production note block counted as spoken')
    if 'draft' in body:
        fails.append('NOT YET DICTATED appendix counted as spoken')
    if 'TELEPROMPTER SCRIPT' in body:
        fails.append('metadata header counted as spoken')
    if spoken_words(SAMPLE) != 4:
        fails.append(f'word count {spoken_words(SAMPLE)}, expected 4')
    for f in fails:
        print('  FAIL:', f)
    print('scriptbody self-test:', 'FAILED' if fails else 'all 5 checks pass')
    sys.exit(1 if fails else 0)
