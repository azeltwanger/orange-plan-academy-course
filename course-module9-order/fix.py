#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "scripts/09-3_WALKTHROUGH_annual-review-scenarios-report.md"
REPORT = ROOT / "COURSE-LIFECYCLE-REVISION-REPORT.md"

BLOCK = """### PART 0 — finish Build Your Plan and run the plan

<!-- PLAN-LIFECYCLE:M9-RUN -->
**DO** Open Build Your Plan. Read every area before Run your plan. Fix an accidental gap; use not-applicable answers only when true.

**DO** Plan → run the full confidence check. Wait for **1,000 test runs**.

**DO** Set the confidence target in the earliest-date hero. Default is 80%.

**SEE** The earliest retirement date becomes the first age that clears that target.

**SAY** This is the first finished-plan read. The onboarding age was a rough deterministic estimate, not this result.

**⚠** Never pair a new plan with an old confidence receipt. Re-run after material plan inputs change.
"""


def run(label: str, command: list[str], report: list[str]) -> None:
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    output = (proc.stdout + proc.stderr).strip()
    report += [f"### {'PASS' if proc.returncode == 0 else 'FAIL'} · {label}", "", "```text", output[-5000:] or "(no output)", "```", ""]
    if proc.returncode != 0:
        raise RuntimeError(f"{label} failed\n{output}")


def main() -> None:
    text = PATH.read_text(encoding="utf-8")

    # Remove the migration block from wherever it landed, then place it before
    # the first maintenance section. This is deliberately exact so no other
    # content can be swallowed if the walkthrough changes later.
    text = text.replace("\n" + BLOCK.strip() + "\n", "\n")
    text = text.replace(BLOCK.strip() + "\n", "")

    marker = "# PART A — the two rhythms"
    if marker not in text:
        raise RuntimeError("Module 9 Part A marker not found")
    text = text.replace(marker, BLOCK.strip() + "\n\n---\n\n" + marker, 1)

    old_preflight = '- [ ] A fresh confidence check run — the report\'s spending band needs explicit bands, or you get the *"Run a fresh confidence check…"* line instead'
    new_preflight = '- [ ] No fresh 1,000-run receipt yet if you want the result to land live — Part 0 runs it, and the report\'s spending band uses that fresh result'
    if old_preflight not in text and new_preflight not in text:
        raise RuntimeError("Module 9 confidence pre-flight line not found")
    text = text.replace(old_preflight, new_preflight, 1)
    PATH.write_text(text.rstrip() + "\n", encoding="utf-8")

    report = ["## Final Module 9 walkthrough-order pass", ""]
    for label, command in [
        ("build one-file", ["python3", "tools/build-onefile.py"]),
        ("build shoot list", ["python3", "tools/build-shoot-list.py"]),
        ("build production checklist", ["python3", "tools/build-production-checklist.py"]),
        ("check crossrefs", ["python3", "tools/check-crossrefs.py"]),
        ("check layer parity", ["python3", "tools/check-layer-parity.py"]),
        ("slop scan", ["python3", "tools/slop-scan.py", "--all"]),
    ]:
        run(label, command, report)

    existing = REPORT.read_text(encoding="utf-8").rstrip()
    REPORT.write_text(existing + "\n\n" + "\n".join(report).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
