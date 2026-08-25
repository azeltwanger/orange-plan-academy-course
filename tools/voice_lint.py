#!/usr/bin/env python3
"""Flag phrases and patterns that make the current Academy sound generated.

This is a guardrail, not a voice generator. Austin's dictation and final read remain
higher authority than any style score.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

CORE_FILENAME = re.compile(r"^\d{2}-\d+_[^/]+\.md$")
WORD = re.compile(r"[A-Za-z0-9]+(?:[’'][A-Za-z0-9]+)?(?:-[A-Za-z0-9]+)*")
SENTENCE = re.compile(r"(?<=[.!?])\s+")
LIST_PREFIX = re.compile(r"^(?:[-*]|\d+[.)])\s+")
TABLE_SEPARATOR = re.compile(r"^\|?\s*:?-{3,}")

FORBIDDEN_PHRASES = {
    "generic lesson opener": re.compile(r"\b(?:so\s+)?in (?:today'?s|this) lesson,? (?:we(?:'re| are)|i(?:'m| am)) going to\b", re.I),
    "let's dive in": re.compile(r"\blet'?s dive in\b", re.I),
    "important to understand filler": re.compile(r"\bit'?s important to understand\b", re.I),
    "by the end of this lesson": re.compile(r"\bby the end of this lesson\b", re.I),
    "financial journey filler": re.compile(r"\b(?:navigate|navigating|journey)\b.{0,35}\bfinancial\b|\bfinancial\b.{0,35}\bjourney\b", re.I),
    "comprehensive holistic filler": re.compile(r"\bcomprehensive and holistic\b", re.I),
    "key takeaway filler": re.compile(r"\bthe key takeaway (?:here )?is\b", re.I),
    "ultimately filler": re.compile(r"\bultimately,? the right choice depends on\b", re.I),
    "at the end of the day": re.compile(r"\bat the end of the day\b", re.I),
    "with that being said": re.compile(r"\bwith that being said\b", re.I),
    "empower language": re.compile(r"\bempower(?:ed|ing|ment)?\b", re.I),
    "unlock language": re.compile(r"\bunlock(?:ing|ed)? your (?:financial|retirement|wealth)\b", re.I),
}

SOFT_PHRASES = {
    "generic goal transition": re.compile(r"\bthe goal (?:here )?is\b", re.I),
    "generic importance transition": re.compile(r"\bwhat'?s important is\b", re.I),
    "generic remember transition": re.compile(r"\bit'?s important to remember\b", re.I),
    "generic recap": re.compile(r"\bto recap\b|\bin summary\b", re.I),
    "vague right answer": re.compile(r"\bthere is no (?:single )?right answer\b", re.I),
}

DIRECTNESS_MARKERS = (
    "i think",
    "i would",
    "the app",
    "orange plan",
    "our demo",
    "the demo",
    "your decision",
)


@dataclass
class Result:
    path: str
    words: int
    sentences: int
    average_sentence_words: float
    forbidden: list[str]
    warnings: list[str]


def current_scripts(root: Path) -> list[Path]:
    results: list[Path] = []
    for path in sorted((root / "scripts").glob("*.md")):
        if not CORE_FILENAME.match(path.name):
            continue
        upper = path.name.upper()
        if "WALKTHROUGH" in upper or "DEMO" in upper:
            continue
        results.append(path)
    return results


def spoken_text(content: str) -> str:
    lines = content.splitlines()
    separator_index = next((i for i, line in enumerate(lines) if line.startswith("====")), 3)
    body: list[str] = []
    in_editor_note = False

    for line in lines[separator_index + 1 :]:
        stripped = line.strip()
        if stripped.startswith("[🔶"):
            in_editor_note = True
        if in_editor_note:
            if stripped.endswith("]"):
                in_editor_note = False
            continue
        if not stripped or stripped.startswith(("==", "<!--", "```", "🎬", "#")):
            continue
        # Markdown tables are visual support, not spoken prose. Counting their rows
        # as one sentence created false 45-word warnings.
        if stripped.startswith("|") or TABLE_SEPARATOR.match(stripped):
            continue

        list_match = LIST_PREFIX.match(stripped)
        if list_match:
            stripped = stripped[list_match.end() :].strip()
            if stripped and stripped[-1] not in ".!?":
                stripped += "."
        body.append(stripped)

    return "\n".join(body)


def clean_sentences(text: str) -> list[str]:
    normalized = re.sub(r"\s+", " ", text).strip()
    return [sentence.strip() for sentence in SENTENCE.split(normalized) if sentence.strip()]


def repeated_opening_warning(sentences: list[str]) -> list[str]:
    openings: list[str] = []
    for sentence in sentences:
        words = WORD.findall(sentence.lower())
        if words:
            openings.append(" ".join(words[:2]))
    counts = Counter(openings)
    return [
        f"sentence opening {opening!r} repeats {count} times"
        for opening, count in counts.items()
        if count >= 8 and opening not in {"the app", "the household", "the demo"}
    ]


def audit(path: Path, root: Path) -> Result:
    content = path.read_text(encoding="utf-8")
    text = spoken_text(content)
    words = WORD.findall(text)
    sentences = clean_sentences(text)
    average = len(words) / max(len(sentences), 1)

    forbidden: list[str] = []
    for label, pattern in FORBIDDEN_PHRASES.items():
        matches = pattern.findall(text)
        if matches:
            forbidden.append(f"{label} ({len(matches)})")

    warnings: list[str] = []
    for label, pattern in SOFT_PHRASES.items():
        count = len(pattern.findall(text))
        if count >= 2:
            warnings.append(f"{label} repeats {count} times")

    if average > 27:
        warnings.append(f"average sentence length is {average:.1f} words")

    long_sentences = [sentence for sentence in sentences if len(WORD.findall(sentence)) > 45]
    if long_sentences:
        warnings.append(f"{len(long_sentences)} sentence(s) exceed 45 words")

    lowered = text.lower()
    marker_count = sum(1 for marker in DIRECTNESS_MARKERS if marker in lowered)
    if marker_count < 3:
        warnings.append("few direct Austin/app/demo decision markers; verify the lesson is not abstract")

    warnings.extend(repeated_opening_warning(sentences))

    return Result(
        path=str(path.relative_to(root)),
        words=len(words),
        sentences=len(sentences),
        average_sentence_words=round(average, 1),
        forbidden=forbidden,
        warnings=warnings,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--strict-warnings", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    results = [audit(path, root) for path in current_scripts(root)]
    forbidden_count = sum(len(result.forbidden) for result in results)
    warning_count = sum(len(result.warnings) for result in results)

    print("# Voice and AI-slop lint")
    print()
    print(f"- Core scripts checked: **{len(results)}**")
    print(f"- Forbidden phrase findings: **{forbidden_count}**")
    print(f"- Readability warnings: **{warning_count}**")
    print()
    print("| Script | Words | Avg sentence | Forbidden | Warnings |")
    print("|---|---:|---:|---|---|")
    for result in results:
        forbidden = "; ".join(result.forbidden) if result.forbidden else "—"
        warnings = "; ".join(result.warnings) if result.warnings else "—"
        print(
            f"| `{result.path}` | {result.words:,} | {result.average_sentence_words:.1f} | "
            f"{forbidden} | {warnings} |"
        )

    print()
    print("This lint catches obvious generated phrasing and readability risks. It does not certify Austin's voice. Austin's dictated source, client-call evidence, and final spoken read remain the authority.")

    if len(results) != 28:
        print(f"Expected 28 current scripts but found {len(results)}.", file=sys.stderr)
        return 1
    if forbidden_count:
        return 1
    if args.strict_warnings and warning_count:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
