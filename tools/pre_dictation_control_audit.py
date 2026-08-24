#!/usr/bin/env python3
"""Audit the Orange Plan Academy pre-dictation control layer.

The script audit checks individual lessons. This audit checks that the
repository has one current production path and that new engine, professional,
and visual controls cannot disappear while stale paths return.
"""

from __future__ import annotations

import re
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
    "DICTATION-ORDER.md",
    "AUSTIN-REVIEW-HOLD-REGISTER.md",
    "DEMO-CHECKPOINT-RUN-SHEET.md",
    "PRE-DICTATION-QA.md",
    "FILMING-READINESS.md",
    "MY-ORANGE-PLAN-CAPSTONE.md",
    "ADVANCED-GATES.md",
    "VISUAL-PRODUCTION-BRIEFS.md",
    "demo/demo-v1-inputs.json",
    "demo/ENGINE-CHECKPOINT-CANDIDATE-3105664.md",
    "demo/VISUAL-DATA-RECEIPT-3105664.md",
    "demo/UI-ACCEPTANCE-CHECKLIST-3105664.md",
    "professional-review/README.md",
    "professional-review/SEND-CHECKLIST.md",
    "professional-review/CANDIDATE-REVIEWERS.md",
    "professional-review/CPA-SEND.md",
    "professional-review/CUSTODY-SEND.md",
    "professional-review/ESTATE-ATTORNEY-SEND.md",
    "professional-review/INSURANCE-SEND.md",
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
    "DICTATION-ORDER.md",
    "AUSTIN-REVIEW-HOLD-REGISTER.md",
    "DEMO-CHECKPOINT-RUN-SHEET.md",
    "PRE-DICTATION-QA.md",
    "FILMING-READINESS.md",
    "MY-ORANGE-PLAN-CAPSTONE.md",
    "ADVANCED-GATES.md",
    "VISUAL-PRODUCTION-BRIEFS.md",
    "professional-review/README.md",
    "professional-review/SEND-CHECKLIST.md",
)

STALE_REFERENCE_PATTERNS = {
    "retired review/ packet path": re.compile(
        r"(?<!professional-)\breview/(?:CPA|CUSTODY|ESTATE|INSURANCE)-REVIEW",
        re.I,
    ),
    "retired review-packets/ path": re.compile(r"\breview-packets/", re.I),
    "encrypted export described as currently restorable": re.compile(
        r"(?:encrypted (?:backup|export)|exported file).{0,90}"
        r"(?:restore the plan|restorable plan data|use it to restore)",
        re.I | re.S,
    ),
    "superseded engine candidate": re.compile(r"ENGINE-CHECKPOINT-CANDIDATE-4456b3c", re.I),
}

REQUIRED_PHRASES = {
    "CURRENT-COURSE.md": (
        "Austin's voice-and-judgment review is ready to begin",
        "ENGINE-CHECKPOINT-CANDIDATE-3105664.md",
        "DEMO-HOUSEHOLD.md",
        "PRE-DICTATION-QA.md",
    ),
    "DICTATION-ORDER.md": (
        "Austin may begin the voice-and-judgment review",
        "25,407 spoken words",
        "0.079251 BTC",
    ),
    "AUSTIN-REVIEW-HOLD-REGISTER.md": (
        "A held line blocks",
        "## UI holds",
        "## Professional and real-world holds",
    ),
    "BUILD-YOUR-PLAN-CROSSWALK.md": (
        "deployed Build Your Plan flow",
        "app_completion_rule",
        "human_completion_rule",
    ),
    "PRE-DICTATION-QA.md": (
        "Reproducible app-engine outputs",
        "External professional responses",
        "Build Your Plan preview",
    ),
    "README.md": (
        "In-app plan restore is currently unavailable",
        "professional-review/",
    ),
    "professional-review/README.md": (
        "Actual outside sign-off is not complete",
        "SEND-CHECKLIST.md",
        "CANDIDATE-REVIEWERS.md",
    ),
    "VISUAL-PRODUCTION-BRIEFS.md": (
        "VISUAL-DATA-RECEIPT-3105664.md",
        "64.8%",
        "$101,948",
    ),
}


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            failures.append(f"missing required control file: {relative_path}")

    for relative_path in FORBIDDEN_CURRENT_DIRECTORIES:
        if (ROOT / relative_path).exists():
            failures.append(
                f"retired duplicate control directory still exists: {relative_path}/; "
                "use professional-review/ only"
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
                failures.append(
                    f"{relative_path}: missing required control phrase: {phrase!r}"
                )

    review_index_path = ROOT / "AUSTIN-REVIEW-INDEX.md"
    if review_index_path.is_file():
        review_index = review_index_path.read_text(encoding="utf-8")
        linked_scripts = set(
            re.findall(r"\(scripts/(\d{2}-\d+_[^)]+\.md)\)", review_index)
        )
        if len(linked_scripts) != 28:
            failures.append(
                f"AUSTIN-REVIEW-INDEX.md links {len(linked_scripts)} unique core scripts; "
                "expected 28"
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
        if "APPROVED" not in decisions.upper():
            failures.append(
                "AUSTIN-DEMO-DECISIONS.md should retain an obvious APPROVED state"
            )

    professional_readme = ROOT / "professional-review/README.md"
    if professional_readme.is_file():
        text = professional_readme.read_text(encoding="utf-8")
        not_sent_count = text.count("NOT SENT")
        if not_sent_count < 4:
            warnings.append(
                "professional-review/README.md should visibly show all four external reviews as NOT SENT until returned"
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

    print(
        "\nThe repository has one current pre-dictation control path, the reconciled "
        "engine/visual/professional controls are present, and no stale packet or "
        "restore-language regression was detected."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
