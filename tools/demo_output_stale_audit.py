#!/usr/bin/env python3
"""Detect retired demo claims after the reconciled Academy engine pass."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = (ROOT / "scripts", ROOT / "lesson-text")
CURRENT_DOCS = (
    ROOT / "CURRENT-COURSE.md",
    ROOT / "DEMO-HOUSEHOLD.md",
    ROOT / "AUSTIN-DEMO-DECISIONS.md",
    ROOT / "VISUAL-PRODUCTION-BRIEFS.md",
    ROOT / "NUMBER-PROVENANCE-REGISTRY.md",
    ROOT / "BUILD-YOUR-PLAN-CROSSWALK.md",
    ROOT / "DICTATION-ORDER.md",
    ROOT / "AUSTIN-REVIEW-INDEX.md",
    ROOT / "PRE-DICTATION-QA.md",
)

RETIRED_PATTERNS = {
    "younger spouse keeps wages until reaching 55": re.compile(
        r"Jordan(?:'s)?\s+(?:earned income|wages|W-2 income).{0,80}(?:until|through).{0,30}Jordan(?:\s+also)?\s+reaches?\s+55",
        re.I | re.S,
    ),
    "old 295k app allocation denominator": re.compile(
        r"(?:app|Orange Plan)(?:'s)?\s+(?:allocatable|target[- ]allocation|investable)\s+(?:portfolio|denominator).{0,40}\$295,000",
        re.I | re.S,
    ),
    "old 59.3 percent app allocation": re.compile(
        r"(?:app|Orange Plan)(?:'s)?.{0,50}(?:Bitcoin allocation|Bitcoin percentage).{0,30}59\.3%",
        re.I | re.S,
    ),
    "old near-upper-edge allocation state": re.compile(
        r"(?:59\.3%|current allocation).{0,80}near the upper edge",
        re.I | re.S,
    ),
    "old fixed-price one-Bitcoin sale": re.compile(
        r"(?:Bitcoin sold|sell(?:s|ing)?).{0,30}(?<![\d.])1(?:\.0+)?\s*BTC",
        re.I | re.S,
    ),
    "old 98k first-year draw": re.compile(
        r"(?:first retirement year|total draw).{0,80}\$98,?000",
        re.I | re.S,
    ),
    "old 60k/38k funding split": re.compile(
        r"\$60,?000.{0,100}\$38,?000",
        re.I | re.S,
    ),
    "superseded engine candidate": re.compile(r"ENGINE-CHECKPOINT-CANDIDATE-4456b3c", re.I),
}

REQUIRED_CURRENT_ANCHORS = {
    "CURRENT-COURSE.md": ("94.6%", "$270,000", "$101,948", "0.079251 BTC"),
    "DEMO-HOUSEHOLD.md": ("64.8%", "$3,761", "$100,000/year at 94.6%"),
    "BUILD-YOUR-PLAN-CROSSWALK.md": ("seven missions", "app_completion_rule", "human_completion_rule"),
    "DICTATION-ORDER.md": ("26,932", "94.6%", "$270,000", "$101,948", "0.079251 BTC"),
}


def current_core_files() -> list[Path]:
    files: list[Path] = []
    for directory in SCAN_DIRS:
        for path in sorted(directory.glob("[0-9][0-9]-[0-9]_*.md")):
            upper = path.name.upper()
            if "WALKTHROUGH" in upper or "DEMO" in upper:
                continue
            files.append(path)
    files.extend(path for path in CURRENT_DOCS if path.is_file())
    return files


def main() -> int:
    failures: list[str] = []
    scanned = current_core_files()

    for path in scanned:
        content = path.read_text(encoding="utf-8")
        for label, pattern in RETIRED_PATTERNS.items():
            if pattern.search(content):
                failures.append(f"{path.relative_to(ROOT)} — {label}")

    for relative, anchors in REQUIRED_CURRENT_ANCHORS.items():
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"missing current control file: {relative}")
            continue
        content = path.read_text(encoding="utf-8")
        for anchor in anchors:
            if anchor not in content:
                failures.append(f"{relative} — missing current anchor {anchor!r}")

    print("# Demo-output stale-claim audit\n")
    print(f"- Current files scanned: **{len(scanned)}**")
    print(f"- Retired patterns checked: **{len(RETIRED_PATTERNS)}**")
    print(f"- Findings: **{len(failures)}**")

    if failures:
        print("\n## Failures")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nNo retired spouse-timing, Allocation, first-year-funding, or engine-candidate claim was found in the current Core path.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
