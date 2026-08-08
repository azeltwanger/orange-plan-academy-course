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
import re, sys, glob, os, hashlib

FAMILIES = {
'A · announce / reframe frame': [
  # NOTE: "secret" deliberately excluded. In this repo it is almost always the
  # literal custody noun — "this map never contains a secret", "your executor
  # holds the process rather than the secret" — and the pattern fired on the
  # no-secrets rule itself, which is load-bearing safety text.
  r"\b(one|the|another|a)\s+(reframe|insight|unlock|trick|mental model)\b",
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
# Added 2026-08-08 after a probe found slop the eight original families could
# not see. Only the families that produced REAL hits are encoded; the probe's
# corporate-vocabulary net caught "leverage" 13 times, which in this repo is the
# financial noun, so that pattern is deliberately narrow.
'I · filler opener Austin verifiably never uses': [
  # The guide checked these against three call transcripts and found ZERO.
  r"\bhere'?s the thing\b", r"\bi want to be clear\b", r"\band honestly\b",
  r"\bto be honest\b", r"\bthe truth is\b", r"\bat the end of the day\b",
  r"\bmake no mistake\b", r"\blet'?s be clear\b", r"\bthe reality is\b",
  r"\bsimply put\b", r"\bthat said,",
],
'J · abstract noun doing the work': [
  # The guide's own worked example — "the drag costs the plan" — was still sitting
  # in MASTER-COURSE when this pattern was written. Austin says who does what.
  r"\bthe drag costs\b",
  # "the app" excluded: it is a concrete actor that literally displays a drift
  # alert, so "the app tells you when Bitcoin runs past 65%" is plain fact.
  r"\b(the plan|the number|the math|the strategy) (tells|teaches|wants|demands|insists|rewards|punishes) you\b",
  r"\b\w+ erodes your\b",
],
'K · corporate vocabulary where a concrete word exists': [
  # NARROW on purpose. "leverage" is excluded: it is the financial noun here.
  r"\blandscape\b", r"\bdelve\b", r"\bseamless", r"\bholistic\b",
  r"\bsynerg", r"\bgame.?changer\b", r"\bempower",
  r"\bunlock(s|ing)? the (report|section|feature)\b",
  r"\bin today'?s \w+ (world|environment|market)\b",
],
'L · reassurance couplet': [
  r"\b(isn'?t|is not) a (character flaw|failure|weakness|moral failing)\b",
  r"\bthat'?s not (weakness|a weakness|a moral)\b",
  r"\bnothing to be (ashamed|embarrassed)\b",
],
'H · spelled-out number': [
  r"\b(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred)[- ](percent|thousand)\b",
  r"\b(one|two|three|four|five|six|seven|eight|nine|ten) percent\b",
],
}

ACCEPTED_FILE = 'SLOP-ACCEPTED.md'


def key(fam, sent):
    """Identify a candidate by family + the sentence itself, not by line number.

    Line numbers move every time anything above them is edited, so a
    line-keyed allowlist would silently expire. Keying on the sentence means an
    adjudication survives edits elsewhere in the file and — correctly — LAPSES
    the moment the sentence itself is reworded, which is exactly when it needs
    looking at again.
    """
    norm = re.sub(r'\s+', ' ', sent).strip()
    return f'{fam[0]}:{hashlib.sha1(norm.encode()).hexdigest()[:12]}'


def accepted():
    """Adjudicated candidates: {key: reason}."""
    if not os.path.exists(ACCEPTED_FILE):
        return {}
    out = {}
    for line in open(ACCEPTED_FILE, encoding='utf-8'):
        m = re.match(r'\|\s*`([A-Z]:[0-9a-f]{12})`\s*\|([^|]*)\|([^|]*)\|', line)
        if m:
            out[m.group(1)] = m.group(3).strip()
    return out


def targets(all_files):
    """Every prose layer, core AND advanced.

    The glob used to be `scripts/[0-9]*.md` + `lesson-text/*.md`, which silently
    excluded the entire Advanced Library: 14 scripts and 14 lesson-text files
    live under scripts/advanced/ and lesson-text/advanced/ with 'A'-led names,
    so no advanced lesson had ever been slop-scanned. MASTER-ADVANCED.md was
    outside --all for the same reason. A scanner that skips a third of the
    corpus reads as coverage and is not.
    """
    fs = (sorted(glob.glob('scripts/[0-9]*.md'))
          + sorted(glob.glob('scripts/advanced/A*.md'))
          + sorted(glob.glob('lesson-text/*.md'))
          + sorted(glob.glob('lesson-text/advanced/*.md')))
    if not all_files:
        fs = [f for f in fs if 'WALKTHROUGH' not in f and 'DEMO' not in f
              and 'walkthrough' not in os.path.basename(f)]
    else:
        fs += ['MASTER-COURSE.md', 'MASTER-ADVANCED.md']
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
    OK = accepted()
    show_ok = '--show-accepted' in sys.argv

    total = live = 0
    for fam, pats in FAMILIES.items():
        if only and not fam.startswith(only):
            continue
        hits, known = [], []
        for f in targets(all_files):
            text = open(f, encoding='utf-8').read()
            for ln, sent in sentences(text):
                for p in pats:
                    if re.search(p, sent, re.I):
                        (known if key(fam, sent) in OK else hits).append((f, ln, sent, key(fam, sent)))
                        break
        total += len(hits) + len(known)
        live += len(hits)
        if hits:
            print(f"\n{'='*78}\n{fam}  —  {len(hits)} UNADJUDICATED\n{'='*78}")
            for f, ln, sent, k in hits:
                print(f"{f}:{ln}   key `{k}`\n    {sent[:300]}")
        if known and show_ok:
            print(f"\n{fam}  —  {len(known)} adjudicated (accepted)")
            for f, ln, sent, k in known:
                print(f"  ok {f}:{ln}  {OK[k][:60]}")

    print(f"\n{total} candidates · {len(OK)} adjudicated in {ACCEPTED_FILE} · "
          f"{live} UNADJUDICATED")
    if live:
        print("\nEach unadjudicated hit is a CANDIDATE, not a verdict. Either fix the\n"
              "sentence, or add its key to SLOP-ACCEPTED.md with a written reason.\n"
              "An adjudication lapses automatically if the sentence is reworded.")
    sys.exit(1 if live else 0)


if __name__ == '__main__':
    main()
