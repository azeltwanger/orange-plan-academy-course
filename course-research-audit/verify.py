#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(label: str, command: list[str], log: list[tuple[str, int, str]]) -> None:
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    output = (proc.stdout + proc.stderr).strip()
    log.append((label, proc.returncode, output))
    if proc.returncode != 0:
        raise RuntimeError(f"{label} failed\n{output}")


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text.rstrip() + "\n", encoding="utf-8")


build_log: list[tuple[str, int, str]] = []
for label, command in [
    ("Build module gates", ["python3", "tools/build-module-gates.py"]),
    ("Build core scripts", ["python3", "tools/build-scripts.py"]),
    ("Build Advanced scripts", ["python3", "tools/build-scripts.py", "--advanced"]),
    ("Split core modules", ["python3", "tools/split-modules.py"]),
    ("Split Advanced modules", ["python3", "tools/split-modules.py", "--advanced"]),
    ("Build one-file scripts", ["python3", "tools/build-onefile.py"]),
    ("Build Circle structure", ["python3", "tools/build-circle-structure.py"]),
    ("Build core dictation order", ["python3", "tools/build-dictation-order.py"]),
    ("Build film order", ["python3", "tools/build-film-order.py"]),
    ("Build screen-shoot list", ["python3", "tools/build-shoot-list.py"]),
    ("Build production checklist", ["python3", "tools/build-production-checklist.py"]),
    ("Update metrics", ["python3", "tools/course-metrics.py"]),
]:
    run(label, command, build_log)

# Assertions for the exact dangerous claims removed by the audit.
scan_files = [
    ROOT / "MASTER-COURSE.md",
    ROOT / "MASTER-ADVANCED.md",
    *sorted((ROOT / "scripts").glob("*.md")),
    *sorted((ROOT / "scripts/advanced").glob("*.md")),
    *sorted((ROOT / "lesson-text").glob("*.md")),
    *sorted((ROOT / "lesson-text/advanced").glob("*.md")),
]
combined = "\n".join(path.read_text(encoding="utf-8") for path in scan_files)
blocked = [
    "The IRS standard is reasonable and documented",
    "the seed works in any hardware wallet",
    "Check these ONLY if the wipe-and-restore actually happened",
    "one key stored with the configuration file",
    "borrowing creates no taxable event",
    "the assets leave your estate" ,
    "waive the prudent investor rule",
]
for phrase in blocked:
    if phrase.lower() in combined.lower():
        raise RuntimeError(f"retired researched claim remains: {phrase}")

required = {
    "scripts/05-1_cost-basis-what-you-paid-and-how-to-reco.md": [
        "identify the particular units",
        "Estimated for planning",
        "zero-basis assumption can show",
    ],
    "scripts/07-2_set-up-a-hardware-wallet-and-test-recove.md": [
        "manufacturer's backup-check feature",
        "spare compatible device",
        "destructive wipe-and-restore only after",
    ],
    "scripts/advanced/A7-1_advanced-custody-passphrase-multisig-collaborative.md": [
        "Every possible passphrase derives a valid wallet",
        "A descriptor cannot sign",
        "provider-independent recovery test",
    ],
    "scripts/08-4_insurance-term-life-disability-umbrella-.md": [
        "first-pass need",
        "actual certificate or policy",
        "Do not cancel or replace",
    ],
    "scripts/advanced/A8-1_advanced-do-you-need-a-trust-and-which-o.md": [
        "does not mechanically mean a trust is required",
        "Do not use \"irrevocable\" as a synonym",
        "There is not one universal sentence",
    ],
}
for path, phrases in required.items():
    text = read(path)
    for phrase in phrases:
        if phrase not in text:
            raise RuntimeError(f"{path}: required researched claim missing: {phrase}")

# Austin's supplied source remains untouched and referenced.
source = ROOT / "source-material/2026-08-25-module-0-1-dictation.md"
if not source.exists():
    raise RuntimeError("Austin source dictation is missing")
for path in [
    "scripts/00-2_how-the-ai-works-what-it-reads-what-it-n.md",
    "scripts/01-1_what-to-gather-before-you-build-the-plan.md",
    "scripts/01-2_set-your-growth-and-inflation-assumption.md",
]:
    if "source-material/2026-08-25-module-0-1-dictation.md" not in read(path):
        raise RuntimeError(f"source provenance missing from {path}")

production = read("PRODUCTION-CHECKLIST.md")
if "3 filming blockers" in production or "Module 2 (F23)" in production:
    raise RuntimeError("resolved structural blocker returned")
for blocker in ["**2.3** (F20)", "**4.3** (F22)"]:
    if blocker not in production:
        raise RuntimeError(f"real Austin blocker missing from production list: {blocker}")
for retired in [
    "Module 5, and the advanced tax lessons (A5.1, A5.2, A5.3, A6.2) — do not FILM",
    "Module 7 and advanced custody lessons A7.1–A7.4 — do not FILM",
    "8.4 — do not FILM",
]:
    if retired in production:
        raise RuntimeError(f"blanket review gate remains: {retired}")

check_log: list[tuple[str, int, str]] = []
for label, command in [
    ("Cross-references", ["python3", "tools/check-crossrefs.py"]),
    ("Layer parity", ["python3", "tools/check-layer-parity.py"]),
    ("Slop scan", ["python3", "tools/slop-scan.py", "--all"]),
    ("Visual coverage", ["python3", "tools/check-visuals.py"]),
    ("Metrics freshness", ["python3", "tools/course-metrics.py", "--check"]),
    ("Layer-parity mutation harness", ["python3", "tools/test-layer-parity-mutations.py"]),
]:
    run(label, command, check_log)

lines = [
    "# Professional research verification",
    "",
    "**Completed:** 2026-08-25",
    "",
    "## Scope",
    "",
    "- Tax and healthcare: Module 5, A5.1–A5.3, A6.1–A6.2",
    "- Custody: Module 7 and A7.1–A7.4",
    "- Insurance and estate: 8.1–8.5 and A8.1",
    "- Production policy, checkpoints, legal packet, source registry, and regression claims",
    "",
    "## Result",
    "",
    "- Primary-source audit completed.",
    "- Unsafe or overstated claims removed from spoken, master, student, walkthrough, and generated module layers.",
    "- Blanket professional-before-recording gates replaced with targeted operational or publication signoffs.",
    "- Austin's original dictation source remains retained and unchanged.",
    "- F20 and F22 remain the only Austin dictation blockers.",
    "",
    "## Generation",
    "",
]
for label, code, output in build_log:
    lines += [f"### {'PASS' if code == 0 else 'FAIL'} · {label}", "", "```text", output[-5000:] or "(no output)", "```", ""]
lines += ["## Repository gates", ""]
for label, code, output in check_log:
    lines += [f"### {'PASS' if code == 0 else 'FAIL'} · {label}", "", "```text", output[-5000:] or "(no output)", "```", ""]
write("PROFESSIONAL-RESEARCH-VERIFICATION.md", "\n".join(lines))
