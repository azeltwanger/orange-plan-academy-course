#!/usr/bin/env python3
"""Inventory direct-language risks across every canonical Academy lesson.

This audit is intentionally broad. It scans every core and Advanced script and
records every sentence containing a negative construction, plus a smaller set of
repetitive copywriting frames. It is a review inventory, not an automatic verdict.
The summary lists every lesson, including lessons with zero hits, so a completed
report proves full 52-lesson coverage.
"""
from __future__ import annotations

import glob
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "FULL-LANGUAGE-SWEEP.md"

NEGATIVE = re.compile(
    r"\b(?:not|no|never|nothing|none|neither|nor|isn['’]?t|aren['’]?t|"
    r"wasn['’]?t|weren['’]?t|doesn['’]?t|don['’]?t|didn['’]?t|won['’]?t|"
    r"wouldn['’]?t|can['’]?t|cannot|couldn['’]?t|shouldn['’]?t|without|"
    r"instead of|rather than|as opposed to)\b",
    re.I,
)

COPY_FRAME = re.compile(
    r"\b(?:the goal is|the point is|the question is|the main takeaway is|"
    r"what this really means|the truth is|here['’]?s the thing|this is where|"
    r"the reason (?:is|why)|it is important to|it['’]?s important to|"
    r"the real question|the honest answer|the honest version|the key is)\b",
    re.I,
)

REVERSAL = re.compile(
    r"\b(?:not\b[^.!?]{0,140}\bbut\b|not\b[^.!?]{0,140}\binstead\b|"
    r"isn['’]?t\b[^.!?]{0,140}\bit['’]?s\b|doesn['’]?t\b[^.!?]{0,140}\bdoes\b|"
    r"rather than\b[^.!?]{0,140}\b(?:use|choose|focus|start|show|say)\b)",
    re.I,
)

SAFETY = re.compile(
    r"\b(?:seed|private key|passphrase|PIN|password|secret|wallet backup|"
    r"guarantee|prediction|forecast|tax|IRS|CPA|attorney|insurance|legal|"
    r"execute|execution|trade|conversion|harvest|loan|withdrawal|transfer|"
    r"basis|beneficiary|trust|RMD|Social Security|Medicare|liquidation|"
    r"margin|LTV|custody|multisig|recovery|simulation|current versus preview|"
    r"save to plan|provider|security|phishing|scam)\b",
    re.I,
)

SKIP_PREFIXES = (
    "TELEPROMPTER", "ADVANCED TELEPROMPTER", "SOURCE:", "PUBLICATION GATE:",
    "=", "#", "🎬 VISUAL", "**Screen capture", "**External screen",
)


@dataclass(frozen=True)
class Hit:
    line: int
    kind: str
    text: str
    safety: bool


def target_files() -> list[Path]:
    files = [Path(p) for p in glob.glob(str(ROOT / "scripts" / "*.md"))]
    files += [Path(p) for p in glob.glob(str(ROOT / "scripts" / "advanced" / "*.md"))]
    return [
        path for path in sorted(files)
        if path.name not in {"README.md", "VOICE-GUIDE.md"}
    ]


def sentences(line: str) -> list[str]:
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", line) if part.strip()]


def lesson_id(path: Path, text: str) -> str:
    match = re.search(r"\b(A?\d+\.\d+)\b", text.splitlines()[0])
    if match:
        return match.group(1)
    match = re.search(r"\b(A?\d+\.\d+)\b", text[:300])
    return match.group(1) if match else path.stem


def main() -> None:
    rows: list[tuple[str, str, list[Hit]]] = []
    for path in target_files():
        source = path.read_text(encoding="utf-8")
        hits: list[Hit] = []
        for line_no, raw in enumerate(source.splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith(SKIP_PREFIXES):
                continue
            for sentence in sentences(line):
                kinds: list[str] = []
                if REVERSAL.search(sentence):
                    kinds.append("reversal")
                if NEGATIVE.search(sentence):
                    kinds.append("negative")
                if COPY_FRAME.search(sentence):
                    kinds.append("copy frame")
                if kinds:
                    hits.append(
                        Hit(
                            line=line_no,
                            kind=" + ".join(kinds),
                            text=sentence,
                            safety=bool(SAFETY.search(sentence)),
                        )
                    )
        rows.append((lesson_id(path, source), path.relative_to(ROOT).as_posix(), hits))

    total_hits = sum(len(hits) for _, _, hits in rows)
    reversal_hits = sum("reversal" in hit.kind for _, _, hits in rows for hit in hits)
    negative_hits = sum("negative" in hit.kind for _, _, hits in rows for hit in hits)
    frame_hits = sum("copy frame" in hit.kind for _, _, hits in rows for hit in hits)

    out = [
        "# Full 52-lesson language sweep",
        "",
        "This is an exhaustive review inventory across every canonical core and Advanced script.",
        "A hit is a sentence to read, not an automatic instruction to delete it. Safety, tax, legal,",
        "custody, and model boundaries often need direct negatives. Ordinary copywriting reversals do not.",
        "",
        f"- Lessons scanned: **{len(rows)}**",
        f"- Total candidate sentences: **{total_hits}**",
        f"- Reversal-pattern candidates: **{reversal_hits}**",
        f"- Negative-construction candidates: **{negative_hits}**",
        f"- Repetitive copy-frame candidates: **{frame_hits}**",
        "",
        "## Coverage",
        "",
        "| Lesson | File | Candidates |",
        "|---|---|---:|",
    ]
    for lesson, path, hits in rows:
        out.append(f"| {lesson} | `{path}` | {len(hits)} |")

    out += ["", "## Candidate sentences", ""]
    for lesson, path, hits in rows:
        out += [f"### {lesson} · `{path}`", ""]
        if not hits:
            out += ["- No candidate sentences.", ""]
            continue
        for hit in hits:
            bucket = "safety / accuracy context" if hit.safety else "ordinary prose"
            out += [f"- **L{hit.line} · {hit.kind} · {bucket}**", f"  - {hit.text}"]
        out.append("")

    OUT.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(
        f"scanned {len(rows)} lessons; wrote {OUT.name} with {total_hits} candidates "
        f"({reversal_hits} reversal patterns)"
    )


if __name__ == "__main__":
    main()
