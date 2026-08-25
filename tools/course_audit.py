#!/usr/bin/env python3
"""Audit the current Orange Plan Academy core scripts and lesson texts.

The tool is dependency-free so it can run locally and in GitHub Actions after
course changes. It checks structure, provenance, runtime, matching lesson text,
and known retired or unsafe teaching language.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

WORDS_PER_MINUTE = 155
# Script headers include natural pauses, visual holds, and worked-example pacing.
# The raw word-count estimate intentionally excludes those production moments.
RUNTIME_WARNING_TOLERANCE_MINUTES = 3.5
CORE_FILENAME = re.compile(r"^(?P<module>\d{2})-(?P<lesson>\d+)_[^/]+\.md$")
WORD = re.compile(r"[A-Za-z0-9]+(?:[’'][A-Za-z0-9]+)?(?:-[A-Za-z0-9]+)*")
DECLARED_RUNTIME = re.compile(r"~\s*(\d+(?:\.\d+)?)\s*min", re.IGNORECASE)

PROVENANCE_MARKERS = (
    "AUSTIN DICTATION + VOICE-MATCHED COMPLETION",
    "AUSTIN DICTATION",
    "VOICE-MATCHED DRAFT",
    "AUSTIN APPROVED",
)

REQUIRED_SCRIPT_SECTIONS = (
    "== YOUR DECISION ==",
    "== PUT IT IN ORANGE PLAN ==",
    "== YOU ARE DONE WHEN ==",
)

CRITICAL_LEGACY_PATTERNS = {
    "legacy provenance label": re.compile(r"SPOKEN-PROSE VERSION \(calibrated\)", re.I),
    "retired freedom-date terminology": re.compile(r"\bFreedom Date\b", re.I),
    "retired Keep/Cut/Reduce framework": re.compile(r"Keep\s*/\s*Cut\s*/\s*Reduce", re.I),
    "retired separate deterministic date framing": re.compile(
        r"deterministic retirement date|retirement date is deterministic", re.I
    ),
    "retired guardrails path": re.compile(r"Plan\s*→\s*Retirement\s*→\s*guardrails", re.I),
    "unsafe beneficiary absolute": re.compile(
        r"beneficiar(?:y|ies)(?:\s+forms?)?\s+(?:always\s+)?override(?:s)?\s+(?:the\s+)?will",
        re.I,
    ),
    "hardcoded universal RMD age": re.compile(
        r"RMDs?\s+(?:always\s+)?(?:start|begin)s?\s+at\s+(?:age\s+)?73",
        re.I,
    ),
    "retired encrypted-backup wording": re.compile(r"\bencrypted (?:data )?backup\b", re.I),
    "restore described as currently usable": re.compile(
        r"\b(?:restorable plan data|data-recovery file used to restore|"
        r"restore(?:d|s)? the plan from (?:this|the) (?:file|export))\b",
        re.I,
    ),
}

WARNING_PATTERNS = {
    "hardcoded 90-day switch": re.compile(r"(?:default\s+)?check-in\s+is\s+90\s+days", re.I),
    "universal main-device wipe instruction": re.compile(
        r"(?:must|always|you\s+will)\s+(?:wipe|factory reset)\s+(?:the|your)\s+(?:main\s+)?device",
        re.I,
    ),
    "unqualified all Roth no-RMD claim": re.compile(r"\bNo RMDs ever\b", re.I),
    "unqualified app-wide apply rule": re.compile(
        r"If you (?:did not|didn't) click Apply, it (?:did not|didn't) happen",
        re.I,
    ),
}


@dataclass
class ScriptResult:
    path: str
    lesson_text_path: str
    module: str
    lesson: str
    title: str
    provenance: str
    spoken_words: int
    estimated_minutes: float
    declared_minutes: float | None
    matching_lesson_text: bool
    missing_script_sections: list[str]
    script_critical_findings: list[str]
    script_warnings: list[str]
    lesson_text_critical_findings: list[str]
    lesson_text_warnings: list[str]

    @property
    def critical_count(self) -> int:
        return (
            len(self.missing_script_sections)
            + len(self.script_critical_findings)
            + len(self.lesson_text_critical_findings)
            + (0 if self.matching_lesson_text else 1)
        )

    @property
    def warning_count(self) -> int:
        return len(self.script_warnings) + len(self.lesson_text_warnings)


def current_core_scripts(root: Path) -> list[Path]:
    scripts_dir = root / "scripts"
    results: list[Path] = []
    for path in sorted(scripts_dir.glob("*.md")):
        name = path.name
        if not CORE_FILENAME.match(name):
            continue
        if any(token in name.upper() for token in ("WALKTHROUGH", "DEMO")):
            continue
        results.append(path)
    return results


def spoken_body(content: str) -> str:
    lines = content.splitlines()
    separator_index = next(
        (index for index, line in enumerate(lines) if line.startswith("====")),
        3,
    )
    body = lines[separator_index + 1 :]
    kept: list[str] = []
    in_editor_note = False

    for line in body:
        stripped = line.strip()
        if stripped.startswith("[🔶"):
            in_editor_note = True
        if in_editor_note:
            if stripped.endswith("]"):
                in_editor_note = False
            continue
        if not stripped:
            continue
        if stripped.startswith(("==", "🎬", "<!--", "```")):
            continue
        kept.append(stripped)

    return "\n".join(kept)


def parse_title(lines: list[str], fallback: str) -> str:
    if len(lines) >= 2 and lines[1].strip():
        return lines[1].strip()
    return fallback


def parse_declared_runtime(content: str) -> float | None:
    match = DECLARED_RUNTIME.search("\n".join(content.splitlines()[:5]))
    return float(match.group(1)) if match else None


def parse_provenance(content: str) -> str:
    head = "\n".join(content.splitlines()[:5])
    for marker in PROVENANCE_MARKERS:
        if marker in head:
            return marker
    return "MISSING / LEGACY"


def find_patterns(content: str, patterns: dict[str, re.Pattern[str]]) -> list[str]:
    return [label for label, pattern in patterns.items() if pattern.search(content)]


def audit_script(root: Path, path: Path) -> ScriptResult:
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    filename_match = CORE_FILENAME.match(path.name)
    assert filename_match is not None

    body = spoken_body(content)
    words = len(WORD.findall(body))
    estimated = words / WORDS_PER_MINUTE
    declared = parse_declared_runtime(content)
    lesson_text_path = root / "lesson-text" / path.name
    lesson_exists = lesson_text_path.exists()

    missing_sections = [
        section for section in REQUIRED_SCRIPT_SECTIONS if section not in content
    ]
    script_critical = find_patterns(content, CRITICAL_LEGACY_PATTERNS)
    script_warnings = find_patterns(content, WARNING_PATTERNS)
    lesson_critical: list[str] = []
    lesson_warnings: list[str] = []

    if parse_provenance(content) == "MISSING / LEGACY":
        script_critical.append("missing current provenance label")
    if declared is None:
        script_warnings.append("missing declared runtime")
    elif abs(declared - estimated) > RUNTIME_WARNING_TOLERANCE_MINUTES:
        script_warnings.append(
            "declared runtime differs from raw word estimate by "
            f"{abs(declared - estimated):.1f} minutes"
        )
    if estimated > 11.5:
        script_warnings.append("estimated runtime exceeds 11.5 minutes")
    if words < 350:
        script_warnings.append(
            "spoken script is under 350 words; confirm it still teaches the decision"
        )

    if lesson_exists:
        lesson_content = lesson_text_path.read_text(encoding="utf-8")
        lesson_critical.extend(find_patterns(lesson_content, CRITICAL_LEGACY_PATTERNS))
        lesson_warnings.extend(find_patterns(lesson_content, WARNING_PATTERNS))
        if not lesson_content.lstrip().startswith("# "):
            lesson_critical.append("missing H1 title")
        if not re.search(r"^##\s+Done when\s*$", lesson_content, re.I | re.M):
            lesson_critical.append("missing Done when heading")

    return ScriptResult(
        path=str(path.relative_to(root)),
        lesson_text_path=str(lesson_text_path.relative_to(root)),
        module=filename_match.group("module"),
        lesson=filename_match.group("lesson"),
        title=parse_title(lines, path.stem),
        provenance=parse_provenance(content),
        spoken_words=words,
        estimated_minutes=round(estimated, 1),
        declared_minutes=declared,
        matching_lesson_text=lesson_exists,
        missing_script_sections=missing_sections,
        script_critical_findings=script_critical,
        script_warnings=script_warnings,
        lesson_text_critical_findings=lesson_critical,
        lesson_text_warnings=lesson_warnings,
    )


def combined_findings(result: ScriptResult) -> list[str]:
    findings = [f"script: {item}" for item in result.script_critical_findings]
    findings.extend(f"script: missing {item}" for item in result.missing_script_sections)
    findings.extend(f"lesson text: {item}" for item in result.lesson_text_critical_findings)
    findings.extend(f"script warning: {item}" for item in result.script_warnings)
    findings.extend(f"lesson warning: {item}" for item in result.lesson_text_warnings)
    if not result.matching_lesson_text:
        findings.append("matching lesson text is missing")
    return findings


def markdown_report(results: list[ScriptResult]) -> str:
    module_totals: dict[str, dict[str, float]] = defaultdict(
        lambda: {"scripts": 0, "words": 0, "minutes": 0.0}
    )
    for result in results:
        total = module_totals[result.module]
        total["scripts"] += 1
        total["words"] += result.spoken_words
        total["minutes"] += result.estimated_minutes

    total_words = sum(item.spoken_words for item in results)
    total_minutes = sum(item.estimated_minutes for item in results)
    critical_count = sum(item.critical_count for item in results)
    warning_count = sum(item.warning_count for item in results)
    missing_text_count = sum(not item.matching_lesson_text for item in results)

    lines = [
        "# Core runtime and structural audit",
        "",
        f"- Core teach scripts: **{len(results)}**",
        f"- Spoken words: **{total_words:,}**",
        f"- Estimated concept-video runtime at {WORDS_PER_MINUTE} wpm: "
        f"**{total_minutes:.1f} minutes ({total_minutes / 60:.1f} hours)**",
        f"- Critical findings across scripts and lesson text: **{critical_count}**",
        f"- Warnings: **{warning_count}**",
        f"- Missing matching lesson texts: **{missing_text_count}**",
        "",
        "## Module totals",
        "",
        "| Module | Scripts | Words | Est. minutes |",
        "|---:|---:|---:|---:|",
    ]

    for module in sorted(module_totals):
        total = module_totals[module]
        lines.append(
            f"| {int(module)} | {int(total['scripts'])} | "
            f"{int(total['words']):,} | {total['minutes']:.1f} |"
        )

    lines.extend(
        [
            "",
            "## Lesson detail",
            "",
            "| Lesson | Spoken words | Est. min | Declared | Provenance | Lesson text | Findings |",
            "|---|---:|---:|---:|---|---|---|",
        ]
    )

    for result in results:
        findings = combined_findings(result)
        findings_text = "; ".join(findings) if findings else "—"
        declared_text = (
            f"{result.declared_minutes:g}"
            if result.declared_minutes is not None
            else "—"
        )
        lines.append(
            f"| {result.title} | {result.spoken_words:,} | "
            f"{result.estimated_minutes:.1f} | {declared_text} | "
            f"{result.provenance} | "
            f"{'Yes' if result.matching_lesson_text else 'NO'} | {findings_text} |"
        )

    if critical_count:
        lines.extend(["", "## Critical findings", ""])
        for result in results:
            for finding in result.script_critical_findings:
                lines.append(f"- `{result.path}` — {finding}")
            for missing in result.missing_script_sections:
                lines.append(f"- `{result.path}` — missing `{missing}`")
            if not result.matching_lesson_text:
                lines.append(f"- `{result.lesson_text_path}` — file is missing")
            for finding in result.lesson_text_critical_findings:
                lines.append(f"- `{result.lesson_text_path}` — {finding}")

    lines.extend(
        [
            "",
            "## Counting method",
            "",
            "The raw estimate counts spoken words after the script header and excludes section labels, production cues, and editor notes. Header runtimes can be longer because they include visual holds, screen pauses, and natural teaching pace.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("artifacts/course-audit"),
    )
    parser.add_argument("--expected-core-count", type=int, default=28)
    parser.add_argument("--strict-warnings", action="store_true")
    return parser.parse_args(list(argv))


def main(argv: Iterable[str] = sys.argv[1:]) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    out_dir = (
        (root / args.out_dir).resolve()
        if not args.out_dir.is_absolute()
        else args.out_dir
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    paths = current_core_scripts(root)
    results = [audit_script(root, path) for path in paths]

    markdown = markdown_report(results)
    (out_dir / "CORE-RUNTIME-REPORT.md").write_text(markdown, encoding="utf-8")
    (out_dir / "course-audit.json").write_text(
        json.dumps([asdict(item) for item in results], indent=2),
        encoding="utf-8",
    )
    print(markdown)

    failures: list[str] = []
    if len(results) != args.expected_core_count:
        failures.append(
            f"expected {args.expected_core_count} core scripts but found {len(results)}"
        )
    for result in results:
        if result.critical_count:
            failures.append(result.path)

    if failures:
        print("\nAudit failed:", file=sys.stderr)
        for item in failures:
            print(f"- {item}", file=sys.stderr)
        return 1
    if args.strict_warnings and any(result.warning_count for result in results):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
