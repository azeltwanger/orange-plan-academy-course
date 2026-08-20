#!/usr/bin/env python3
"""Audit the Orange Plan Academy pre-dictation control layer.

This complements course_audit.py. The core audit checks individual scripts;
this audit checks that the repository has one current production path and does
not quietly reintroduce stale control files or app claims.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "CURRENT-COURSE.md",
    "COURSE-APP-CONTRACT.md",
    "BUILD-YOUR-PLAN-CROSSWALK.md",
    "DEMO-HOUSEHOLD.md",
    "AUSTIN-DEMO-DECISIONS.md",
    "AUSTIN-REVIEW-INDEX.md",
    "DEMO-CHECKPOINT-RUN-SHEET.md",
    "PRE-DICTATION-QA.md",
    "FILMING-READINESS.md",
    "MY-ORANGE-PLAN-CAPSTONE.md",
    "ADVANCED-GATES.md",
    "professional-review/README.md",
    "professional-review/CPA.md",
    "professional-review/CUSTODY.md",
    "professional-review/ESTATE-ATTORNEY.md",
    "professional-review/INSURANCE.md",
    "research/CLIENT-CALL-VOICE-EVIDENCE.md",
    "research/CLIENT-CONFUSION-REGISTRY.md",
    "research/CORE-OWNERSHIP-AND-RUNTIME.md",
    "research/DEMO-NUMBER-RECONCILIATION.md",
    "research/EDUCATIONAL-PROGRESSION-AUDIT.md",
    "research/SLIDE-CORRECTION-MAP.md",
)

FORBIDDEN_CURRENT_DIRECTORIES = (
    "review",
    "review-packets",
)

CURRENT_TEXT_PATHS = (
    "README.md",
    "CURRENT-COURSE.md",
    "COURSE-APP-CONTRACT.md",
    "BUILD-YOUR-PLAN-CROSSWALK.md",
    "DEMO-HOUSEHOLD.md",
    "AUSTIN-DEMO-DECISIONS.md",
    "AUSTIN-REVIEW-INDEX.md",
    "DEMO-CHECKPOINT-RUN-SHEET.md",
    "PRE-DICTATION-QA.md",
    "FILMING-READINESS.md",
    "MY-ORANGE-PLAN-CAPSTONE.md",
    "ADVANCED-GATES.md",
)

STALE_REFERENCE_PATTERNS = {
    "retired review/ packet path": re.compile(r"(?<!professional-)\breview/(?:CPA|CUSTODY|ESTATE|INSURANCE)-REVIEW", re.I),
    "retired review-packets/ path": re.compile(r"\breview-packets/", re.I),
    "encrypted export described as currently restorable": re.compile(
        r"(?:encrypted (?:backup|export)|exported file).{0,90}(?:restore the plan|restorable plan data|use it to restore)",
        re.I | re.S,
    ),
}

REQUIRED_PHRASES = {
    "CURRENT-COURSE.md": (
        "Austin's final read and dictation pass has not started",
        "DEMO-HOUSEHOLD.md",
        "PRE-DICTATION-QA.md",
    ),
    "BUILD-YOUR-PLAN-CROSSWALK.md": (
        "working preview",
        "app_completion_rule",
        "human_completion_rule",
    ),
    "PRE-DICTATION-QA.md": (
        "App-calculated demo outputs",
        "External professional responses",
        "Build Your Plan preview",
    ),
    "README.md": (
        "In-app plan restore is currently unavailable",
        "professional-review/",
    ),
}


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            failures.append(f"missing required control file: {relative_path}")

    for relative_path in FORBIDDEN_CURRENT_DIRECTORIES:
        if (ROOT / relative_path).exists():
            failures.append(
                f"retired duplicate control directory still exists: {relative_path}/; use professional-review/ only"
            )

    for relative_path in CURRENT_TEXT_PATHS:
        path = ROOT / relative_path
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        for label, pattern in STALE_REFERENCE_PATTERNS.items():
            if pattern.search(content):
                failures.append(f"{relative_path}: {label}")

    for relative_path, phrases in REQUIRED_PHRASES.items():
        path = ROOT / relative_path
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in content:
                failures.append(f"{relative_path}: missing required control phrase: {phrase!r}")

    review_index_path = ROOT / "AUSTIN-REVIEW-INDEX.md"
    if review_index_path.is_file():
        review_index = review_index_path.read_text(encoding="utf-8")
        linked_scripts = set(re.findall(r"\(scripts/(\d{2}-\d+_[^)]+\.md)\)", review_index))
        if len(linked_scripts) != 28:
            failures.append(
                f"AUSTIN-REVIEW-INDEX.md links {len(linked_scripts)} unique core scripts; expected 28"
            )

    contract_path = ROOT / "COURSE-APP-CONTRACT.md"
    if contract_path.is_file():
        contract = contract_path.read_text(encoding="utf-8")
        commit_match = re.search(
            r"App source (?:reviewed|verified):.*?`([0-9a-f]{7,40})`",
            contract,
            flags=re.I,
        )
        if not commit_match:
            failures.append("COURSE-APP-CONTRACT.md: missing last-reviewed app commit")
        elif len(commit_match.group(1)) < 7:
            failures.append("COURSE-APP-CONTRACT.md: malformed app commit")

    decision_path = ROOT / "AUSTIN-DEMO-DECISIONS.md"
    if decision_path.is_file():
        decisions = decision_path.read_text(encoding="utf-8")
        if "APPROVE" not in decisions.upper() or "CHANGE" not in decisions.upper():
            warnings.append(
                "AUSTIN-DEMO-DECISIONS.md should keep an obvious APPROVE / CHANGE response format"
            )

    print("# Pre-dictation control audit")
    print()
    print(f"- Required files checked: **{len(REQUIRED_FILES)}**")
    print(f"- Critical findings: **{len(failures)}**")
    print(f"- Warnings: **{len(warnings)}**")

    if warnings:
        print("\n## Warnings")
        for warning in warnings:
            print(f"- {warning}")

    if failures:
        print("\n## Failures")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nThe repository has one current pre-dictation control path and no detected stale packet or restore-language regression.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
