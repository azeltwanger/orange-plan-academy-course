#!/usr/bin/env python3
"""Validate the deterministic V1 transformation before it writes anything."""
from __future__ import annotations

import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRANSFORM = ROOT / "tools" / "apply-v1-alignment-direct-voice.py"


def main() -> None:
    namespace = runpy.run_path(str(TRANSFORM), run_name="v1_alignment_module")
    replacements = namespace["REPLACEMENTS"]
    full_scripts = namespace["FULL_SCRIPTS"]
    full_walkthroughs = namespace["FULL_WALKTHROUGHS"]

    failures: list[str] = []
    checked = 0
    for rel, pairs in replacements.items():
        if not pairs:
            continue
        path = ROOT / rel
        if not path.exists():
            failures.append(f"missing source file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for old, new in pairs:
            checked += 1
            if old not in text:
                failures.append(f"old text missing in {rel}: {old[:120]}")
                continue
            text = text.replace(old, new, 1)

    for rel in list(full_scripts) + list(full_walkthroughs):
        path = ROOT / rel
        if not path.exists():
            failures.append(f"full-rewrite target missing: {rel}")

    for rel, content in full_scripts.items():
        lines = content.splitlines()
        if not any(line and set(line.strip()) == {"="} for line in lines):
            failures.append(f"full script lacks teleprompter divider: {rel}")

    if failures:
        print("V1 ALIGNMENT PREFLIGHT FAILED")
        for failure in failures:
            print(" -", failure)
        raise SystemExit(1)

    print(
        f"V1 alignment preflight passed: {checked} exact replacements, "
        f"{len(full_scripts)} full teach rewrites, "
        f"{len(full_walkthroughs)} full walkthrough rewrites"
    )


if __name__ == "__main__":
    main()
