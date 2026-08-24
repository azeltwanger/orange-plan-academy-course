#!/usr/bin/env python3
"""Run every current Orange Plan Academy pre-dictation audit."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts" / "full-course-audit"

COMMANDS = (
    (
        "Core script and lesson-text audit",
        [sys.executable, str(ROOT / "tools" / "course_audit.py"), "--out-dir", str(ARTIFACTS / "core")],
    ),
    (
        "Advanced script and lesson-text audit",
        [sys.executable, str(ROOT / "tools" / "advanced_course_audit.py")],
    ),
    (
        "Pre-dictation control audit",
        [sys.executable, str(ROOT / "tools" / "pre_dictation_control_audit.py")],
    ),
    (
        "Canonical demo fixture audit",
        [sys.executable, str(ROOT / "tools" / "demo_fixture_audit.py")],
    ),
    (
        "Checkpoint receipt audit",
        [sys.executable, str(ROOT / "tools" / "checkpoint_receipt_audit.py")],
    ),
    (
        "Core voice and AI-slop lint",
        [sys.executable, str(ROOT / "tools" / "voice_lint.py")],
    ),
    (
        "Advanced voice and AI-slop lint",
        [sys.executable, str(ROOT / "tools" / "advanced_voice_lint.py")],
    ),
)


def main() -> int:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    summary: list[str] = ["# Full Orange Plan Academy audit", ""]

    for index, (name, command) in enumerate(COMMANDS, start=1):
        print(f"\n{'=' * 80}\n{name}\n{'=' * 80}\n")
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        output = completed.stdout
        if completed.stderr:
            output += "\n## STDERR\n\n" + completed.stderr
        print(output)

        report_path = ARTIFACTS / f"{index:02d}-{name.lower().replace(' ', '-').replace('/', '-')}.md"
        report_path.write_text(output, encoding="utf-8")

        status = "PASS" if completed.returncode == 0 else f"FAIL ({completed.returncode})"
        summary.append(f"- **{status}** — {name}")
        if completed.returncode != 0:
            failures.append(name)

    summary.extend(["", f"**Overall:** {'PASS' if not failures else 'FAIL'}", ""])
    (ARTIFACTS / "SUMMARY.md").write_text("\n".join(summary), encoding="utf-8")

    print("\n" + "\n".join(summary))
    if failures:
        print("Failed audits:", file=sys.stderr)
        for name in failures:
            print(f"- {name}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
