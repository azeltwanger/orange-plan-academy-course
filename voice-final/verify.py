#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def run(label: str, command: list[str], results: list[tuple[str, str]]) -> None:
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    output = (proc.stdout + proc.stderr).strip()
    if proc.returncode != 0:
        raise RuntimeError(f"{label} failed\n{output}")
    results.append((label, output[-5000:] or "(no output)"))


# The new authority must survive in every live 2.3 layer.
for path in [
    "MASTER-COURSE.md",
    "scripts/02-3_fund-a-known-future-cost-the-six-questio.md",
    "lesson-text/02-3_fund-a-known-future-cost-the-six-questio.md",
    "modules/02-module-2-cash-flow-reserve.md",
    "visuals/2-3_cost-lanes.md",
]:
    if "Bitcoin can remain part of the funding plan" not in read(path):
        raise RuntimeError(f"F20 authority missing from {path}")

# F20 is resolved; F22 remains the only Austin content blocker.
production = read("PRODUCTION-CHECKLIST.md")
if "(F20)" in production or "FILMING BLOCKER (F20)" in read("MASTER-COURSE.md"):
    raise RuntimeError("F20 still appears as an active filming blocker")
if "1 filming blocker" not in production or "**4.3** (F22)" not in production:
    raise RuntimeError("production checklist does not show F22 as the one remaining blocker")

final_status = read("FINALIZATION-STATUS.md")
if "**F20:**" in final_status or "**F22:**" not in final_status:
    raise RuntimeError("final status blocker list is stale")

# Retired editor-shaped lines should not return in the spoken or master layers.
combined = "\n".join([
    read("MASTER-COURSE.md"),
    read("MASTER-ADVANCED.md"),
    *[p.read_text(encoding="utf-8") for p in sorted((ROOT / "scripts").glob("*.md"))],
    *[p.read_text(encoding="utf-8") for p in sorted((ROOT / "scripts/advanced").glob("*.md"))],
])
blocked = [
    "The useful question is not everything the AI cannot do",
    "The goal is to replace doomscrolling",
    "The goal isn't to have the AI make every decision",
    "The goal is not to stop buying Bitcoin for seven years",
    "Same sale proceeds. Different identified units. Different gain.",
    "That's the whole product.",
    "Three documents, three jobs.",
    "The goal is not maximum complexity",
    "The goal is not to collect devices",
    "The goal is not fear. The goal is",
]
for phrase in blocked:
    if phrase in combined:
        raise RuntimeError(f"retired editor-shaped line remains: {phrase}")

for required in [
    "source-material/2026-08-25-module-0-1-dictation.md",
    "source-material/2026-08-26-f20-and-voice-pass.md",
    "AUSTIN-VOICE-PASS-REPORT.md",
]:
    if not (ROOT / required).exists():
        raise RuntimeError(f"required voice authority/report missing: {required}")

if "Additional calibration from the 2026-08-25 dictation" not in read("scripts/VOICE-GUIDE.md"):
    raise RuntimeError("new dictation calibration missing from VOICE-GUIDE")

results: list[tuple[str, str]] = []
for label, command in [
    ("Cross-references", ["python3", "tools/check-crossrefs.py"]),
    ("Layer parity", ["python3", "tools/check-layer-parity.py"]),
    ("Voice/slop scan", ["python3", "tools/slop-scan.py", "--all"]),
    ("Visual coverage", ["python3", "tools/check-visuals.py"]),
    ("Metrics freshness", ["python3", "tools/course-metrics.py", "--check"]),
    ("Layer-parity mutation harness", ["python3", "tools/test-layer-parity-mutations.py"]),
]:
    run(label, command, results)

report = read("AUSTIN-VOICE-PASS-REPORT.md").rstrip()
report += "\n\n## Final repository gates\n\n"
for label, output in results:
    report += f"### PASS · {label}\n\n```text\n{output}\n```\n\n"
(ROOT / "AUSTIN-VOICE-PASS-REPORT.md").write_text(report.rstrip() + "\n", encoding="utf-8")
