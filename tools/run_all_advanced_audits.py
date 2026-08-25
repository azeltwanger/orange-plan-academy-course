#!/usr/bin/env python3
"""Run every current Advanced Library pre-dictation audit."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts" / "advanced-full-audit"

COMMANDS = (
    ("Advanced structure and parity", [sys.executable, str(ROOT / "tools" / "advanced_course_audit.py")]),
    ("Advanced example fixture", [sys.executable, str(ROOT / "tools" / "advanced_demo_fixture_audit.py")]),
    ("Advanced quality gates", [sys.executable, str(ROOT / "tools" / "advanced_quality_gate_audit.py")]),
    ("Advanced voice and AI-slop", [sys.executable, str(ROOT / "tools" / "advanced_voice_lint.py")]),
)


def slug(value: str) -> str:
    return value.lower().replace(" ", "-").replace("/", "-")


def main() -> int:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    summary = ["# Advanced Library full audit", ""]

    for index, (name, command) in enumerate(COMMANDS, start=1):
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        output = completed.stdout
        if completed.stderr:
            output += "\n## STDERR\n\n" + completed.stderr
        print(f"\n{'=' * 80}\n{name}\n{'=' * 80}\n{output}")
        (ARTIFACTS / f"{index:02d}-{slug(name)}.md").write_text(output, encoding="utf-8")
        status = "PASS" if completed.returncode == 0 else f"FAIL ({completed.returncode})"
        summary.append(f"- **{status}** — {name}")
        if completed.returncode != 0:
            failures.append(name)

    summary.extend(
        [
            "",
            f"**Overall internal audit:** {'PASS' if not failures else 'FAIL'}",
            "",
            "External professional responses, deployed UI receipts, current agreements/quotes/device procedures, real-world proof, pilot results, and Austin approval are intentionally outside this automated result.",
            "",
        ]
    )
    (ARTIFACTS / "SUMMARY.md").write_text("\n".join(summary), encoding="utf-8")
    print("\n" + "\n".join(summary))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
