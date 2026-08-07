#!/usr/bin/env python3
"""Structural slop scanner for the course.

The point: earlier sweeps grepped for LITERAL phrases ("here's the thing") and
kept missing the same move written a new way. Austin caught one on 2026-08-08
that three clean sweeps had walked past:

  "One reframe that makes this whole system click: the futures that fail at 80%
   confidence aren't random bad luck sprinkled evenly across time. They're
   almost always the same shape, which is a deep drawdown..."

Three stacked moves, zero literal matches: an announce frame, a
negation-reversal, and an abstract noun doing the work. So this scans for the
SHAPES, not the strings.

Every hit is a CANDIDATE, not a verdict. Plenty are legitimate (a real
comparative, a real "not X" that carries information). Read each one.

  python3 tools/slop-scan.py            # teach scripts + lesson text
  python3 tools/slop-scan.py --all      # + walkthroughs + master
  python3 tools/slop-scan.py --family A # one family
"""
import re, sys, glob, os

FAMILIES = {
'A · announce / reframe frame': [
  r"\b(one|the|another|a)\s+(reframe|insight|unlock|trick|secret|mental model)\b",
  r"makes?\s+(this|the|it)\s+(whole\s+)?\w*\s*click",
  r"\bclicks? into place\b",
  r"here'?s (the|what|why|how|where)\b(?!.{0,30}\b(app|button|page|screen|form|field|number you|it lives|to find|I'?d)\b)",
  r"\bthe (key|trick|whole point|real point|important part|important thing) (here )?is\b",
  r"\bthe way to think about (this|it)\b",
  r"\bthink of (it|this) (like|as)\b",
  r"\bif you (take|remember) (only )?one thing\b",
  r"\bthis is the part (that|where|I)\b",
  r"\bonce you (see|understand|internalize) (this|it|that)\b",
  r"\bworth (understanding|internalizing|sitting with|noting|pausing)\b",
  r"\b(zoom out|step back|at a high level|big picture)\b",
  r"\bpay attention to\b",
  r"\bwhat (really )?matters (here )?is\b",
  r"\bthe real (question|issue|point|problem) (here )?is\b",
  r"\bnotice (that|how)\b",
  r"\bbear in mind\b",
  r"\bkeep in mind\b",
  r"\bthe punchline\b",
  r"\bhere is why this matters\b|\bwhy this matters\b",
],
'B · negation-reversal ("not A, it\'s B")': [
  r"\b(isn'?t|aren'?t|is not|are not|wasn'?t|weren'?t)\b[^.!?]{3,80}[.,]\s*(it'?s|they'?re|that'?s|it is|they are)\b",
  r"\bnot\s+(just\s+)?(a|an|the)\s+[^.!?]{2,45},\s*(but|it'?s|they'?re|that'?s)\b",
  r"\bless about\b[^.!?]{2,50}\bmore about\b",
  r"\bit'?s not that\b[^.!?]{3,60}\.\s*It'?s that\b",
  r"\bdoesn'?t\s+\w+[^.!?]{2,50},\s*it\s+(just\s+)?\w+s\b",
  r"\bnot\s+because\b[^.!?]{2,50},\s*but because\b",
],
'C · decorative metaphor / abstract noun': [
  r"\bsprinkled\b|\bscattered (evenly|across)\b|\bbaked in(to)?\b",
  r"\bunder the hood\b|\bmoving parts\b|\bripples? (through|out|across)\b",
  r"\b(the |that )?same shape\b|\bthe shape of the\b",
  r"\bis where the (magic|money|work|action)\b",
  r"\bcompounds? into\b|\bsnowball(s|ing)?\b",
  r"\bquietly (eats|erodes|drains|kills|breaks)\b",
  r"\ba dent\b|\bmoves the needle\b|\bheavy lifting\b|\bdo(es|ing)? the heavy\b",
  r"\bthe engine (of|that)\b|\bthe backbone\b|\bthe bedrock\b|\bthe north star\b",
],
'D · aphorism / payoff line': [
  r"\bthat'?s the whole (point|thing|reason|job|design|product|conversation|argument|game|ballgame)\b",
  r"\bin one (line|sentence|number|dial|word|move)\b",
  r"\bthat'?s (it|the ballgame|the whole ballgame)\b\.",
  r"\band that'?s (the|what|why) [^.!?]{2,40}\.$",
  r"\b\w+ beats \w+[^.!?]{0,40}\.$",
  r"\bwins over\b|\btrumps\b",
],
'E · em-dash parallelism / triad': [
  r"—[^—\n]{2,60}—",
  r"\b\w+, the \w+, and the \w+\b",
],
'F · fragment for drama': [
  r"(?<=[.!?])\s+[A-Z][a-z]+(?: [a-z]+){0,2}\.\s+(?=[A-Z])",
],
'G · textbook example opener': [
  r"\b(take someone|take a couple|take a household|consider a|imagine (a|if|you)|picture (a|your|two|the))\b",
],
'H · spelled-out number': [
  r"\b(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred)[- ](percent|thousand)\b",
  r"\b(one|two|three|four|five|six|seven|eight|nine|ten) percent\b",
],
}

def targets(all_files):
    fs = sorted(glob.glob('scripts/[0-9]*.md')) + sorted(glob.glob('lesson-text/*.md'))
    if not all_files:
        fs = [f for f in fs if 'WALKTHROUGH' not in f and 'DEMO' not in f
              and 'walkthrough' not in os.path.basename(f)]
    else:
        fs += ['MASTER-COURSE.md']
    return [f for f in fs if os.path.basename(f) not in ('README.md',)]

def sentences(text):
    """Yield (line_no, sentence). Skips fenced/reference/marker lines."""
    for i, line in enumerate(text.split('\n'), 1):
        s = line.strip()
        if not s or s.startswith(('#', '>', '|', '```', '===', '==', '**DO**',
                                  '**SEE**', '**⚠**', '- [ ]', '☐', 'TELEPROMPTER',
                                  '>>>')):
            continue
        for sent in re.split(r'(?<=[.!?])\s+', s):
            if sent.strip():
                yield i, sent.strip()

def main():
    all_files = '--all' in sys.argv
    only = None
    if '--family' in sys.argv:
        only = sys.argv[sys.argv.index('--family') + 1].upper()

    total = 0
    for fam, pats in FAMILIES.items():
        if only and not fam.startswith(only):
            continue
        hits = []
        for f in targets(all_files):
            text = open(f, encoding='utf-8').read()
            for ln, sent in sentences(text):
                for p in pats:
                    if re.search(p, sent, re.I):
                        hits.append((f, ln, sent))
                        break
        if hits:
            print(f"\n{'='*78}\n{fam}  —  {len(hits)} candidates\n{'='*78}")
            for f, ln, sent in hits:
                print(f"{f}:{ln}\n    {sent[:300]}")
            total += len(hits)
    print(f"\n{total} candidates. Each one is a candidate, not a verdict.")

if __name__ == '__main__':
    main()
