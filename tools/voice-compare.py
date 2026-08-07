#!/usr/bin/env python3
"""Measure any script against Austin's own dictation.

`scripts/03-2_size-your-cash-reserve-in-months-of-spen.md` is the calibration
master: a full lesson Austin dictated himself. Every rewritten script gets
compared against it here before it goes on the dictation list.

The metrics are the ones that actually separate his voice from AI prose,
established empirically across earlier passes:

  chaining       sentences opening with so/and/but/now/then. Register control:
                 his DICTATED lesson runs ~15%, his conversation ~39%. The
                 lesson number is the target, not the conversation number.
  article        sentences opening with the/a/an/this/that/these/those. A high
                 rate usually means abstract nouns doing the work.
  median_len     median sentence length in words. His dictation sits ~13.
  going_to       "going to" per 1k words. He scaffolds in future tense; AI
                 writes present tense.
  i_think        "I think" per 1k words. He marks opinions as opinions.
  because        "because" per 1k words. Nearly every claim carries its why.
  heres          "Here's" per 1k words. He uses it about once per 4,300 words;
                 unchecked AI drafts ran 6.8x that.
  spelled        spelled-out percentages, which he never uses.

Nothing here is a pass/fail gate. It tells you which direction a script drifts
so you can fix it before recording, and it will not catch a sentence that is
grammatically his and still says nothing.

  python3 tools/voice-compare.py                 # every teach script
  python3 tools/voice-compare.py scripts/09-2*   # specific files
"""
import re, sys, glob, os, statistics

MASTER = 'scripts/03-2_size-your-cash-reserve-in-months-of-spen.md'
CHAIN = re.compile(r'^(so|and|but|now|then)\b', re.I)
ART = re.compile(r'^(the|a|an|this|that|these|those)\b', re.I)

def body(path):
    """Strip the header block and production markers; keep spoken prose."""
    t = open(path, encoding='utf-8').read()
    t = re.split(r'={10,}\n', t, maxsplit=1)[-1]
    keep = []
    for line in t.split('\n'):
        s = line.strip()
        if not s or s.startswith(('==', '🎬', '>>>', '#', '>', '|', '**DO**',
                                  '**SEE**', '**⚠**', 'TELEPROMPTER')):
            continue
        keep.append(s)
    return ' '.join(keep)

def sentences(text):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]

def profile(path):
    t = body(path)
    words = t.split()
    n = len(words) or 1
    sents = sentences(t)
    k = len(sents) or 1
    per1k = lambda pat: round(len(re.findall(pat, t, re.I)) * 1000 / n, 1)
    return {
        'file': os.path.basename(path),
        'words': n,
        'chaining': round(100 * sum(bool(CHAIN.match(s)) for s in sents) / k),
        'article': round(100 * sum(bool(ART.match(s)) for s in sents) / k),
        'median_len': int(statistics.median(len(s.split()) for s in sents)) if sents else 0,
        'going_to': per1k(r'\bgoing to\b'),
        'i_think': per1k(r'\bI think\b'),
        'because': per1k(r'\bbecause\b'),
        'heres': per1k(r"(?<![a-zA-Z])here's\b"),
        'spelled': len(re.findall(r'\b(one|two|three|five|ten|twenty|thirty|fifty|seventy|eighty|ninety)\s+percent\b', t, re.I)),
    }

# how far a script may drift from the master before it is worth a look
TOL = {'chaining': 12, 'article': 15, 'median_len': 6,
       'going_to': 6, 'i_think': 3, 'because': 6, 'heres': 1.0}

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    if args:
        targets = [f for a in args for f in glob.glob(a)]
    else:
        targets = [f for f in sorted(glob.glob('scripts/[0-9]*.md'))
                   if 'WALKTHROUGH' not in f and 'DEMO' not in f]
    m = profile(MASTER)
    print(f"CALIBRATION MASTER — {m['file']}  ({m['words']} words)")
    print(f"  chaining {m['chaining']}%  article {m['article']}%  median {m['median_len']}w"
          f"  going-to {m['going_to']}  I-think {m['i_think']}  because {m['because']}"
          f"  Here's {m['heres']}\n")
    hdr = f"{'file':<46}{'chain':>6}{'art':>5}{'med':>5}{'goto':>6}{'think':>6}{'bcse':>6}{'here':>6}  drift"
    print(hdr); print('-' * len(hdr))
    for f in targets:
        if os.path.abspath(f) == os.path.abspath(MASTER):
            continue
        p = profile(f)
        off = [k for k, tol in TOL.items() if abs(p[k] - m[k]) > tol]
        if p['spelled']:
            off.append('spelled-numbers')
        print(f"{p['file'][:44]:<46}{p['chaining']:>5}%{p['article']:>4}%{p['median_len']:>5}"
              f"{p['going_to']:>6}{p['i_think']:>6}{p['because']:>6}{p['heres']:>6}"
              f"  {', '.join(off) if off else 'ok'}")

if __name__ == '__main__':
    main()
