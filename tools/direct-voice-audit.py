#!/usr/bin/env python3
"""Audit spoken course scripts for contrastive-negation writing.

Austin's voice guide rejects the copywriting move that sets up “not A” merely so
the next clause or sentence can land “B.” This audit catches same-sentence and
cross-sentence versions. Every hit remains a candidate for a human read. Safety,
legal, tax, custody, model-interpretation, and explicit UI warnings may need the
negative because the exclusion itself carries information.

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


SAME_SENTENCE = [
    re.compile(r"\b(?:isn'?t|aren'?t|is not|are not|wasn'?t|weren'?t|doesn'?t|does not|don'?t|do not)\b[^.!?]{2,140}\bbut\b", re.I),
    re.compile(r"\bnot\s+(?:just\s+)?(?:a|an|the)?\s*[^.!?]{2,100},\s*(?:but|it'?s|they'?re|that'?s|instead)\b", re.I),
    re.compile(r"\bnot because\b[^.!?]{2,120}\bbut because\b", re.I),
    re.compile(r"\bless about\b[^.!?]{2,100}\bmore about\b", re.I),
    re.compile(r"\bit'?s not that\b[^.!?]{2,120}\bit'?s that\b", re.I),
]

NEGATION = re.compile(
    r"\b(?:isn'?t|aren'?t|is not|are not|wasn'?t|weren'?t|doesn'?t|does not|"
    r"don'?t|do not|didn'?t|did not|cannot|can'?t|not automatically|not only|"
    r"not just|I do not think|I don'?t think|I do not mean|I don'?t mean|"
    r"The goal is not|The point is not|The purpose is not)\b",
    re.I,
)

HIGH_FRICTION = re.compile(
    r"\b(?:doesn'?t mean|does not mean|not automatically|do not automatically|"
    r"I do not mean|I don'?t mean|I do not think|I don'?t think|"
    r"The goal is not|The point is not|The purpose is not|This is not|That is not)\b",
    re.I,
)

AFFIRMATIVE_START = re.compile(r"^(?:[A-Z0-9]|Orange Plan|Foundation|Integration|Optimization|Sovereign)")

# Safety/compliance lines remain visible in the report but are separated from the
# ordinary editorial candidates. Walkthrough warning lines are included here too.
SAFETY = re.compile(
    r"\b(?:seed phrase|private key|passphrase|PIN|password|wallet backup|secret|"
    r"guarantee|financial advice|tax advice|legal advice|insurance|CrowdHealth|"
    r"execute|execution|trade|conversion|harvest|loan|withdrawal|taxable|tax|IRS|"
    r"probability|chance of going broke|chance you go broke|forecast|prediction|"
    r"transfer|basis|beneficiary|trustee|trust|will|RMD|Social Security|Medicare|"
    r"liquidation|margin call|LTV|provider|custody|multisig|recovery|MFA|2FA)\b",
    re.I,
)

WARNING_LINE = re.compile(r"^(?:\*\*⚠|⚠|DO NOT\b|NEVER\b)", re.I)


def sentence_spans(line: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", line.strip()) if s.strip()]


def targets() -> list[Path]:
    files = [Path(p) for p in glob.glob(str(ROOT / "scripts" / "*.md"))]
    files += [Path(p) for p in glob.glob(str(ROOT / "scripts" / "advanced" / "*.md"))]
    return [p for p in sorted(files) if p.name not in {"README.md", "VOICE-GUIDE.md"}]


def main() -> None:
    hits: list[Hit] = []
    for path in targets():
        rel = path.relative_to(ROOT).as_posix()
        for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith(("#", "|", "```", "TELEPROMPTER", "ADVANCED TELEPROMPTER", "==", "**DO**", "**SEE**", "**ENTER**", "**SAVE**", "**POINT", "**WATCH")):
                continue

            is_safety = bool(SAFETY.search(line) or WARNING_LINE.search(line))
            family = "safety/compliance candidate" if is_safety else "direct-voice candidate"

            if any(rx.search(line) for rx in SAME_SENTENCE):
                hits.append(Hit(rel, line_no, family + " · same-sentence reversal", line))

            if HIGH_FRICTION.search(line):
                hits.append(Hit(rel, line_no, family + " · negation-led explanation", line))

            sents = sentence_spans(line)
            for left, right in zip(sents, sents[1:]):
                if NEGATION.search(left) and AFFIRMATIVE_START.search(right):
                    hits.append(Hit(rel, line_no, family + " · cross-sentence reversal", f"{left} {right}"))

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
        "> Generated by `tools/direct-voice-audit.py`. Every line below is a",
        "> candidate for a human read. Replace a copywriting-style reversal with",
        "> the useful affirmative fact. Preserve a negative when the exclusion",
        "> itself carries safety, legal, tax, custody, model, or UI-warning value.",
        "",
        f"- **{direct}** ordinary direct-voice candidates",
        f"- **{safety}** safety/compliance candidates",
        f"- **{len(unique)}** total candidates across **{len(by_file)}** files",
        "",
        "## Editing rule",
        "",
        "Say the useful fact first. Keep the negative only when removing it would",
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
    if "--fail-ordinary" in sys.argv and direct:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
