#!/usr/bin/env python3
"""Audit spoken course scripts for indirect, copywriting-style phrasing.

The audit catches two patterns Austin has flagged during the voice review:

1. A rhetorical setup that says “not A” merely so the useful idea B can land
   afterward, including the same move split across nearby paragraphs.
2. Filler transitions such as sentence-leading “Also” that delay the useful fact.

Ordinary narrative negatives are ignored. Safety, legal, tax, custody, model,
and explicit UI warnings stay in their own review bucket.

Usage:
    python3 tools/direct-voice-audit.py
    python3 tools/direct-voice-audit.py --fail-ordinary
"""
from __future__ import annotations

import glob
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "DIRECT-VOICE-AUDIT.md"


@dataclass(frozen=True)
class Hit:
    path: str
    line: int
    family: str
    text: str


CONCEPT_SUBJECT = (
    r"(?:The (?:goal|point|purpose|question|answer|decision|relevant number|"
    r"safest architecture|first decision|reason)|This|That|It|A setup|"
    r"Most people|I|We|You|Redundancy|Price context|Historical data)"
)

NEGATION_CORE = (
    r"(?:isn'?t|is not|aren'?t|are not|doesn'?t mean|does not mean|"
    r"don'?t need|do not need|not automatically|not only|not just)"
)

SAME_SENTENCE = [
    re.compile(
        rf"\b{CONCEPT_SUBJECT}\b[^.!?]{{0,80}}\b{NEGATION_CORE}\b"
        r"[^.!?]{2,140}\bbut\b",
        re.I,
    ),
    re.compile(r"\bnot\s+(?:just\s+)?(?:a|an|the)?\s*[^.!?]{2,100},\s*(?:but|it'?s|they'?re|that'?s|instead)\b", re.I),
    re.compile(r"\bnot because\b[^.!?]{2,120}\bbut because\b", re.I),
    re.compile(r"\bless about\b[^.!?]{2,100}\bmore about\b", re.I),
    re.compile(r"\bit'?s not that\b[^.!?]{2,120}\bit'?s that\b", re.I),
]

NEGATION_LED = re.compile(
    rf"^{CONCEPT_SUBJECT}\b[^.!?]{{0,140}}\b{NEGATION_CORE}\b",
    re.I,
)

HIGH_FRICTION = re.compile(
    r"\b(?:doesn'?t mean|does not mean|not automatically|"
    r"I do not mean|I don'?t mean|I do not think|I don'?t think|"
    r"The goal is not|The point is not|The purpose is not|"
    r"The question is not|The decision is not|This is not|That is not)\b",
    re.I,
)

AFFIRMATIVE_START = re.compile(
    r"^(?:It|They|This|That|The|Instead|Use|Choose|Start|Focus|Review|Ask|"
    r"Your|Orange Plan|A|An|For|Another|Each|Every)\b",
    re.I,
)

FILLER_OPENING = re.compile(
    r"^(?:Also|And also|It is also important to note|It is also worth noting|"
    r"Something else to keep in mind|Another thing to keep in mind)\b",
    re.I,
)

SAFETY = re.compile(
    r"\b(?:seed phrase|private key|passphrase|PIN|password|wallet backup|secret|"
    r"guarantee|financial advice|tax advice|legal advice|insurance|CrowdHealth|"
    r"execute|execution|trade|conversion|harvest|loan|withdrawal|taxable|tax|IRS|"
    r"probability|chance of going broke|chance you go broke|forecast|prediction|"
    r"transfer|basis|beneficiary|trustee|trust|will|RMD|Social Security|Medicare|"
    r"liquidation|margin call|LTV|provider|custody|multisig|recovery|MFA|2FA|"
    r"simulation|standard|current versus preview|save to plan)\b",
    re.I,
)

WARNING_LINE = re.compile(r"^(?:\*\*⚠|⚠|DO NOT\b|NEVER\b)", re.I)
SKIP_PREFIXES = (
    "#", "|", "```", "TELEPROMPTER", "ADVANCED TELEPROMPTER", "==",
    "**DO**", "**SEE**", "**ENTER**", "**SAVE**", "**POINT", "**WATCH",
)


def sentence_spans(line: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", line.strip()) if s.strip()]


def targets() -> list[Path]:
    files = [Path(p) for p in glob.glob(str(ROOT / "scripts" / "*.md"))]
    files += [Path(p) for p in glob.glob(str(ROOT / "scripts" / "advanced" / "*.md"))]
    return [p for p in sorted(files) if p.name not in {"README.md", "VOICE-GUIDE.md"}]


def family_for(text: str) -> str:
    return "safety/compliance candidate" if SAFETY.search(text) or WARNING_LINE.search(text) else "direct-voice candidate"


def main() -> None:
    hits: list[Hit] = []
    for path in targets():
        rel = path.relative_to(ROOT).as_posix()
        adjacent: list[tuple[int, str]] = []

        for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith(SKIP_PREFIXES):
                continue

            family = family_for(line)
            if any(rx.search(line) for rx in SAME_SENTENCE):
                hits.append(Hit(rel, line_no, family + " · same-sentence reversal", line))

            if HIGH_FRICTION.search(line) and NEGATION_LED.search(line):
                hits.append(Hit(rel, line_no, family + " · negation-led explanation", line))

            for sentence in sentence_spans(line):
                if FILLER_OPENING.search(sentence):
                    sentence_family = family_for(sentence)
                    hits.append(Hit(rel, line_no, sentence_family + " · filler transition", sentence))

            # Bullets, quoted production directions, and metadata do not form a
            # prose pair with the next paragraph.
            if line.startswith(("- ", "* ", "> ", "**⚠", "⚠")):
                continue
            adjacent.extend((line_no, sentence) for sentence in sentence_spans(line))

        for (left_line, left), (right_line, right) in zip(adjacent, adjacent[1:]):
            # Adjacent prose paragraphs are normally one or two source lines apart.
            # Stop before a distant section can create a false pair.
            if right_line - left_line > 3:
                continue
            if NEGATION_LED.search(left) and AFFIRMATIVE_START.search(right):
                pair = f"{left} {right}"
                family = family_for(pair)
                hits.append(Hit(rel, left_line, family + " · cross-sentence reversal", pair))

    unique: list[Hit] = []
    seen: set[tuple[str, int, str]] = set()
    for hit in hits:
        key = (hit.path, hit.line, hit.text)
        if key not in seen:
            seen.add(key)
            unique.append(hit)

    by_file: dict[str, list[Hit]] = {}
    for hit in unique:
        by_file.setdefault(hit.path, []).append(hit)

    direct = sum("direct-voice candidate" in h.family for h in unique)
    safety = sum("safety/compliance candidate" in h.family for h in unique)
    out = [
        "# Direct-voice audit",
        "",
        "> Generated by `tools/direct-voice-audit.py`. Replace an ordinary",
        "> reversal or filler transition with the useful affirmative fact. Review",
        "> the safety/compliance bucket separately because the negative itself may",
        "> be the information the viewer needs.",
        "",
        f"- **{direct}** ordinary direct-voice candidates",
        f"- **{safety}** safety/compliance candidates",
        f"- **{len(unique)}** total candidates across **{len(by_file)}** files",
        "",
        "## Editing rule",
        "",
        "Say the useful fact first. Remove a transition when the next sentence can",
        "start with the fact itself. Keep a negative only when removing it would",
        "make the viewer more likely to take an unsafe action or misunderstand a",
        "material boundary.",
        "",
    ]
    for path, file_hits in sorted(by_file.items()):
        out += [f"## `{path}`", ""]
        for hit in file_hits:
            out += [f"- **L{hit.line} · {hit.family}**", f"  - {hit.text}"]
        out.append("")

    OUT.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(
        f"wrote {OUT.relative_to(ROOT)}: {direct} ordinary, "
        f"{safety} safety/compliance candidates"
    )

    ordinary = [h for h in unique if "direct-voice candidate" in h.family]
    if ordinary:
        print("ordinary direct-voice candidates:")
        for hit in ordinary:
            print(f"  {hit.path}:{hit.line} [{hit.family}] {hit.text}")

    if "--fail-ordinary" in sys.argv and direct:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
