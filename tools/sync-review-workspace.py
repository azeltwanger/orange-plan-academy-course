#!/usr/bin/env python3
"""Synchronize the clean Austin review workspace from current Core sources.

The current course, scripts, and lesson text remain the source. The review/
workspace is a generated convenience layer and must never drift behind them.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "review"
SCRIPT_DIR = ROOT / "scripts"
LESSON_DIR = ROOT / "lesson-text"

MODULE_HEADING = re.compile(r"^### Module (\d+) — (.+)$", re.M)
LESSON_LINE = re.compile(r"^- (\d+\.\d+) · (.+)$", re.M)
SCRIPT_NAME = re.compile(r"^(\d{2})-(\d+)_.*\.md$")

MODULE_FILE_NAMES = {
    0: "00-start-here.md",
    1: "01-baseline-and-confidence.md",
    2: "02-cash-flow-and-reserve.md",
    3: "03-debt-strategy.md",
    4: "04-allocation-and-the-next-dollar.md",
    5: "05-tax-strategy.md",
    6: "06-retirement-income.md",
    7: "07-custody-and-recovery.md",
    8: "08-estate-and-family-handoff.md",
    9: "09-maintain-test-and-read.md",
}

SUPPORT_COPIES = {
    "CURRENT-COURSE.md": "CURRENT-COURSE.md",
    "DICTATION-ORDER.md": "DICTATION-ORDER.md",
    "AUSTIN-REVIEW-HOLD-REGISTER.md": "AUSTIN-REVIEW-HOLD-REGISTER.md",
    "AUSTIN-REVIEW-INDEX.md": "AUSTIN-REVIEW-INDEX.md",
    "AUSTIN-AUTHORITY.md": "AUSTIN-AUTHORITY.md",
    "SLOP-ACCEPTED.md": "SLOP-ACCEPTED.md",
    "VOICE-GUIDE.md": "VOICE-GUIDE.md",
    "AI-PLANNING-QUESTION-GUIDE.md": "AI-PLANNING-QUESTION-GUIDE.md",
    "research/CLIENT-CALL-VOICE-EVIDENCE.md": "CLIENT-CALL-VOICE-EVIDENCE.md",
}


def normalize_current_course() -> None:
    """Keep the AI outline aligned with the current useful-decision lesson."""
    path = ROOT / "CURRENT-COURSE.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "**Outcome:** understand what is being built, how the app and Academy divide the work, how Core and Advanced differ, and the no-secrets rule.",
        "**Outcome:** understand what is being built, how the app and Academy divide the work, and how to use Orange Plan AI to explain, prioritize, compare, challenge, and act on the plan.",
    )
    text = text.replace(
        "- 0.2 · How the AI works: what it reads and what it never needs",
        "- 0.2 · Use Orange Plan AI to understand the numbers and make better decisions",
    )
    path.write_text(text, encoding="utf-8")


def parse_modules() -> list[tuple[int, str, list[tuple[str, str]]]]:
    text = (ROOT / "CURRENT-COURSE.md").read_text(encoding="utf-8")
    matches = list(MODULE_HEADING.finditer(text))
    modules: list[tuple[int, str, list[tuple[str, str]]]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        lessons = LESSON_LINE.findall(text[start:end])
        if lessons:
            modules.append((int(match.group(1)), match.group(2).strip(), lessons))
    return modules


def current_scripts() -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in sorted(SCRIPT_DIR.glob("*.md")):
        match = SCRIPT_NAME.match(path.name)
        if not match or "WALKTHROUGH" in path.name.upper() or "DEMO" in path.name.upper():
            continue
        lesson_id = f"{int(match.group(1))}.{int(match.group(2))}"
        result[lesson_id] = path
    return result


def copy_current_files(modules, scripts) -> None:
    review_scripts = REVIEW / "scripts"
    review_lessons = REVIEW / "lesson-text"
    review_scripts.mkdir(parents=True, exist_ok=True)
    review_lessons.mkdir(parents=True, exist_ok=True)

    expected_names: set[str] = set()
    for _, _, lessons in modules:
        for lesson_id, _ in lessons:
            source_script = scripts[lesson_id]
            source_lesson = LESSON_DIR / source_script.name
            if not source_lesson.exists():
                raise SystemExit(f"Missing lesson text for {source_script.name}")
            expected_names.add(source_script.name)
            shutil.copyfile(source_script, review_scripts / source_script.name)
            shutil.copyfile(source_lesson, review_lessons / source_script.name)

    for directory in (review_scripts, review_lessons):
        for path in directory.glob("*.md"):
            if path.name not in expected_names:
                path.unlink()


def build_module_files(modules, scripts) -> None:
    module_dir = REVIEW / "modules"
    module_dir.mkdir(parents=True, exist_ok=True)
    expected: set[str] = set()

    for number, title, lessons in modules:
        filename = MODULE_FILE_NAMES[number]
        expected.add(filename)
        parts = [f"# Module {number} — {title}", ""]
        for lesson_id, _ in lessons:
            script_path = scripts[lesson_id]
            lesson_path = LESSON_DIR / script_path.name
            parts.extend([
                "---",
                "",
                f"# {script_path.name}",
                "",
                "## SPOKEN SCRIPT",
                "",
                script_path.read_text(encoding="utf-8").rstrip(),
                "",
                "## MATCHING LESSON TEXT",
                "",
                lesson_path.read_text(encoding="utf-8").rstrip(),
                "",
            ])
        (module_dir / filename).write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")

    for path in module_dir.glob("*.md"):
        if path.name not in expected:
            path.unlink()


def copy_support_files() -> None:
    for source_name, destination_name in SUPPORT_COPIES.items():
        source = ROOT / source_name
        if source.exists():
            shutil.copyfile(source, REVIEW / destination_name)


def build_manifest(modules, scripts) -> None:
    lines = [
        "# Austin review workspace manifest",
        "",
        "Generated from the current Core source. Historical and production layers are excluded.",
        "",
        "## Current lessons",
        "",
    ]
    count = 0
    for number, title, lessons in modules:
        lines.append(f"### Module {number} — {title}")
        lines.append("")
        for lesson_id, outline_title in lessons:
            script = scripts[lesson_id]
            lines.append(f"- {lesson_id} · [{outline_title}](scripts/{script.name})")
            count += 1
        lines.append("")
    lines.extend([
        f"**Total:** {count} spoken scripts and {count} matching lesson-text files.",
        "",
        "## AI support",
        "",
        "- `AI-PLANNING-QUESTION-GUIDE.md` — practical questions by planning area",
        "- `../scripts/00-3_DEMO_use-orange-plan-ai.md` — versioned screen-share demo run sheet",
        "",
    ])
    (REVIEW / "MANIFEST.md").write_text("\n".join(lines), encoding="utf-8")


def build_zip() -> None:
    artifact_dir = ROOT / "artifact"
    artifact_dir.mkdir(exist_ok=True)
    output = artifact_dir / "orange-plan-austin-review.zip"
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        start = ROOT / "00-START-HERE-AUSTIN-REVIEW.md"
        if start.exists():
            archive.write(start, start.name)
        for path in sorted(REVIEW.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(ROOT).as_posix())


def main() -> int:
    normalize_current_course()
    subprocess.run([sys.executable, str(ROOT / "tools" / "build-dictation-order.py")], check=True)
    modules = parse_modules()
    scripts = current_scripts()
    outlined = [lesson_id for _, _, lessons in modules for lesson_id, _ in lessons]
    if len(outlined) != 28 or set(outlined) != set(scripts):
        raise SystemExit(
            f"Current review mismatch: outlined={len(outlined)} scripts={len(scripts)} "
            f"missing={sorted(set(outlined) - set(scripts))} extras={sorted(set(scripts) - set(outlined))}"
        )
    REVIEW.mkdir(exist_ok=True)
    copy_current_files(modules, scripts)
    build_module_files(modules, scripts)
    copy_support_files()
    build_manifest(modules, scripts)
    build_zip()
    print("Review workspace synchronized from current Core sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
