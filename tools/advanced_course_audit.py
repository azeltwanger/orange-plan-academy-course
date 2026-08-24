#!/usr/bin/env python3
"""Audit the current Orange Plan Academy Advanced Library."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts" / "advanced" / "current"
LESSONS = ROOT / "lesson-text" / "advanced" / "current"
CONTRACT = ROOT / "curriculum" / "advanced-learner-questions.json"
OUTPUT = ROOT / "artifacts" / "advanced-course-audit"
EXPECTED = 18
WPM = 155
WORD = re.compile(r"[A-Za-z0-9]+(?:[’'][A-Za-z0-9]+)?(?:-[A-Za-z0-9]+)*")
RUNTIME = re.compile(r"~\s*(\d+(?:\.\d+)?)\s*min", re.I)

REQUIRED = (
    "> **Watch this only",
    "== YOUR DECISION ==",
    "== PUT IT IN ORANGE PLAN ==",
    "== YOU ARE DONE WHEN ==",
    "**Return to Core:**",
)

FORBIDDEN = {
    "legacy provenance": re.compile(r"SPOKEN-PROSE VERSION", re.I),
    "interest-only universal": re.compile(r"interest-only beats amortizing", re.I),
    "normal 50% LTV": re.compile(r"50% LTV is (?:a )?normal|normal borrow at 50%", re.I),
    "universal RMD age": re.compile(r"RMDs? (?:always )?(?:start|begin)s? at (?:age )?73", re.I),
    "no RMDs ever": re.compile(r"No RMDs ever", re.I),
    "blanket wipe instruction": re.compile(r"(?:must|always|you will) (?:wipe|reset) (?:the|your) (?:main )?device", re.I),
    "mandatory passphrase level": re.compile(r"Level 3 (?:is|requires) (?:a )?passphrase", re.I),
    "four-key 2-of-3": re.compile(r"you hold 2 keys.*executor.*1 key.*provider.*1 key", re.I | re.S),
}


@dataclass
class Result:
    path: str
    id: str
    words: int
    raw_minutes: float
    declared_minutes: float | None
    lesson_text: bool
    missing: list[str]
    forbidden: list[str]


def spoken_body(content: str) -> str:
    lines = content.splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith("====")), 3) + 1
    kept = []
    for line in lines[start:]:
        stripped = line.strip()
        if not stripped or stripped.startswith(("==", "<!--", "```")):
            continue
        kept.append(stripped)
    return "\n".join(kept)


def main() -> int:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    paths = sorted(SCRIPTS.glob("*.md"))
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    entries = contract.get("lessons", [])
    contract_by_path = {entry["script"]: entry for entry in entries}
    results: list[Result] = []

    if len(paths) != EXPECTED:
        failures.append(f"expected {EXPECTED} current scripts, found {len(paths)}")
    if len(entries) != EXPECTED:
        failures.append(f"expected {EXPECTED} contract entries, found {len(entries)}")

    seen_ids: set[str] = set()
    total_words = 0
    total_raw = 0.0
    total_declared = 0.0

    for path in paths:
        relative = str(path.relative_to(ROOT))
        content = path.read_text(encoding="utf-8")
        entry = contract_by_path.get(relative)
        lesson_path = LESSONS / path.name
        missing = [marker for marker in REQUIRED if marker not in content]
        forbidden = [label for label, pattern in FORBIDDEN.items() if pattern.search(content)]
        body = spoken_body(content)
        words = len(WORD.findall(body))
        raw_minutes = words / WPM
        runtime_match = RUNTIME.search("\n".join(content.splitlines()[:5]))
        declared = float(runtime_match.group(1)) if runtime_match else None
        lesson_id = entry.get("id") if entry else "MISSING"

        if entry is None:
            failures.append(f"{relative}: missing contract entry")
        else:
            if lesson_id in seen_ids:
                failures.append(f"duplicate lesson id: {lesson_id}")
            seen_ids.add(lesson_id)
            if entry.get("lessonText") != str(lesson_path.relative_to(ROOT)):
                failures.append(f"{relative}: lessonText contract mismatch")
            for field in ("gate", "question", "decision", "example", "returnToCore"):
                if not str(entry.get(field, "")).strip():
                    failures.append(f"{relative}: blank contract field {field}")

        if not lesson_path.is_file():
            failures.append(f"{relative}: matching lesson text missing")
        if missing:
            failures.append(f"{relative}: missing {', '.join(missing)}")
        if forbidden:
            failures.append(f"{relative}: forbidden {', '.join(forbidden)}")
        if "VOICE-MATCHED DRAFT" not in "\n".join(content.splitlines()[:5]) and "AUSTIN APPROVED" not in "\n".join(content.splitlines()[:5]):
            failures.append(f"{relative}: missing current provenance label")
        if declared is None:
            failures.append(f"{relative}: missing runtime header")

        total_words += words
        total_raw += raw_minutes
        total_declared += declared or 0
        results.append(Result(relative, lesson_id, words, round(raw_minutes, 1), declared, lesson_path.is_file(), missing, forbidden))

    for entry in entries:
        if not (ROOT / entry["script"]).is_file():
            failures.append(f"contract script missing: {entry['script']}")
        if not (ROOT / entry["lessonText"]).is_file():
            failures.append(f"contract lesson text missing: {entry['lessonText']}")

    report = [
        "# Advanced course audit",
        "",
        f"- Current scripts: **{len(paths)}**",
        f"- Matching contract entries: **{len(entries)}**",
        f"- Spoken words: **{total_words:,}**",
        f"- Raw runtime at {WPM} wpm: **{total_raw:.1f} min ({total_raw / 60:.1f} h)**",
        f"- Production runtime from headers: **{total_declared:.1f} min ({total_declared / 60:.1f} h)**",
        f"- Findings: **{len(failures)}**",
        "",
        "| Lesson | Words | Raw min | Header min | Lesson text | Findings |",
        "|---|---:|---:|---:|---|---|",
    ]
    for result in results:
        findings = result.missing + result.forbidden
        report.append(
            f"| {result.id} | {result.words:,} | {result.raw_minutes:.1f} | "
            f"{result.declared_minutes if result.declared_minutes is not None else '—'} | "
            f"{'Yes' if result.lesson_text else 'NO'} | {'; '.join(findings) if findings else '—'} |"
        )
    if failures:
        report.extend(["", "## Failures", ""] + [f"- {item}" for item in failures])

    markdown = "\n".join(report) + "\n"
    (OUTPUT / "ADVANCED-COURSE-AUDIT.md").write_text(markdown, encoding="utf-8")
    (OUTPUT / "advanced-course-audit.json").write_text(json.dumps([asdict(item) for item in results], indent=2), encoding="utf-8")
    print(markdown)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
