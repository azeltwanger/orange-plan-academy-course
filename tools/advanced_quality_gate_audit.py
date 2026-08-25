#!/usr/bin/env python3
"""Audit the Advanced Library quality-control layer.

This audit does not pretend external professional responses or real-world proof
exist. It checks that the course has the same internal controls as Core and that
remaining holds are stated honestly.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = 18

REQUIRED_FILES = (
    "ADVANCED-CURRENT.md",
    "ADVANCED-APP-CONTRACT.md",
    "ADVANCED-NUMBER-PROVENANCE-REGISTRY.md",
    "ADVANCED-QUALITY-GATE-MATRIX.md",
    "ADVANCED-FILMING-READINESS.md",
    "curriculum/advanced-learner-questions.json",
    "demo/advanced-demo-fixtures.json",
    "demo/ADVANCED-DEMO-FIXTURE.md",
    "professional-review/ADVANCED-AUTHORITATIVE-SOURCE-VERIFICATION.md",
    "professional-review/ADVANCED-SEND-PACKAGE-INDEX.md",
    "professional-review/ADVANCED-PROFESSIONAL-REVIEW-TRACKER.md",
    "professional-review/LENDING-SEND.md",
    "professional-review/HEALTHCARE-SEND.md",
    "professional-review/CPA-ADVANCED-SEND.md",
    "professional-review/CUSTODY-ADVANCED-SEND.md",
    "professional-review/ESTATE-ADVANCED-SEND.md",
    "research/ADVANCED-WORKED-EXAMPLE-AUDIT.md",
    "research/ADVANCED-VISUAL-BRIEFS.md",
    "research/ADVANCED-DEMO-AND-WALKTHROUGH-PLAN.md",
    "research/ADVANCED-LEARNER-PILOT-PLAN.md",
    "review/advanced/README.md",
    "review/advanced/LEARNER-QUESTION-MAP.md",
    "review/advanced/DICTATION-ORDER.md",
    "review/advanced/HOLD-REGISTER.md",
    "review/advanced/JUDGMENT-REVIEW.md",
    "tools/advanced_course_audit.py",
    "tools/advanced_demo_fixture_audit.py",
    "tools/advanced_voice_lint.py",
)

REQUIRED_PHRASES = {
    "ADVANCED-APP-CONTRACT.md": (
        "Saved Plan input",
        "Preview",
        "Scenario",
        "External evidence",
        "A6.2",
    ),
    "ADVANCED-NUMBER-PROVENANCE-REGISTRY.md": (
        "Proof / qualification",
        "Starting LTV",
        "First-pass conversion room",
        "Healthcare full cost",
        "Provider-independent recovery",
        "Ownership-authority matrix complete",
    ),
    "ADVANCED-QUALITY-GATE-MATRIX.md": (
        "18/18",
        "HOLD · NOT SENT",
        "Ready for Austin review",
        "Ready to film",
    ),
    "ADVANCED-FILMING-READINESS.md": (
        "all 18 lessons",
        "none is final-film-ready",
        "Learner pilot plan",
        "A6.2",
    ),
    "professional-review/ADVANCED-AUTHORITATIVE-SOURCE-VERIFICATION.md": (
        "not",
        "professional",
        "A2",
        "A3",
        "A4",
        "A5",
        "A6",
    ),
    "professional-review/ADVANCED-SEND-PACKAGE-INDEX.md": (
        "Bitcoin lending/legal",
        "CPA / tax attorney",
        "Pre-Medicare healthcare",
        "Advanced custody",
        "Colorado estate / trust",
        "NOT SENT",
    ),
    "research/ADVANCED-LEARNER-PILOT-PLAN.md": (
        "pilot has **not been run**",
        "Blocking misunderstanding",
        "return to Core",
    ),
    "demo/ADVANCED-DEMO-FIXTURE.md": (
        "advanced-demo-v1",
        "0.45 BTC",
        "$6,923",
        "$101,948",
        "2-of-3",
    ),
}

FORBIDDEN_PATTERNS = {
    "professional review falsely complete": re.compile(
        r"(?:professional sign[- ]?off complete|all professional reviews complete|outside professional clearance complete)",
        re.I,
    ),
    "illustrative LTV called safe": re.compile(
        r"(?:65%|80%|50%).{0,40}(?:safe|normal) LTV|(?:safe|normal).{0,40}(?:65%|80%|50%) LTV",
        re.I,
    ),
    "advanced described as mandatory": re.compile(
        r"every learner (?:must|should) (?:watch|complete) (?:all )?Advanced",
        re.I,
    ),
}

CURRENT_CONTROL_FILES = (
    "ADVANCED-CURRENT.md",
    "ADVANCED-APP-CONTRACT.md",
    "ADVANCED-NUMBER-PROVENANCE-REGISTRY.md",
    "ADVANCED-QUALITY-GATE-MATRIX.md",
    "ADVANCED-FILMING-READINESS.md",
    "professional-review/ADVANCED-AUTHORITATIVE-SOURCE-VERIFICATION.md",
    "professional-review/ADVANCED-SEND-PACKAGE-INDEX.md",
    "research/ADVANCED-LEARNER-PILOT-PLAN.md",
    "review/advanced/HOLD-REGISTER.md",
)


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            failures.append(f"missing required Advanced quality file: {relative}")

    for relative, phrases in REQUIRED_PHRASES.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        lowered = content.lower()
        for phrase in phrases:
            if phrase.lower() not in lowered:
                failures.append(f"{relative}: missing quality phrase {phrase!r}")

    for relative in CURRENT_CONTROL_FILES:
        path = ROOT / relative
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(content):
                failures.append(f"{relative}: {label}")

    contract_path = ROOT / "curriculum" / "advanced-learner-questions.json"
    if contract_path.is_file():
        lessons = json.loads(contract_path.read_text(encoding="utf-8")).get("lessons", [])
        if len(lessons) != EXPECTED:
            failures.append(f"Advanced contract has {len(lessons)} lessons; expected {EXPECTED}")
        ids = [entry.get("id") for entry in lessons]
        if len(set(ids)) != len(ids):
            failures.append("Advanced contract contains duplicate lesson IDs")
        for entry in lessons:
            for field in ("gate", "question", "decision", "example", "returnToCore", "holds"):
                value = entry.get(field)
                if not value:
                    failures.append(f"{entry.get('id', 'UNKNOWN')}: missing {field}")

    scripts = sorted((ROOT / "scripts" / "advanced" / "current").glob("*.md"))
    texts = sorted((ROOT / "lesson-text" / "advanced" / "current").glob("*.md"))
    if len(scripts) != EXPECTED:
        failures.append(f"found {len(scripts)} current Advanced scripts; expected {EXPECTED}")
    if len(texts) != EXPECTED:
        failures.append(f"found {len(texts)} current Advanced lesson texts; expected {EXPECTED}")

    tracker = ROOT / "professional-review" / "ADVANCED-PROFESSIONAL-REVIEW-TRACKER.md"
    if tracker.is_file():
        content = tracker.read_text(encoding="utf-8").upper()
        if content.count("NOT SENT") < 5:
            failures.append("Advanced professional tracker must show all five packages as NOT SENT")

    hold_register = ROOT / "review" / "advanced" / "HOLD-REGISTER.md"
    if hold_register.is_file():
        content = hold_register.read_text(encoding="utf-8")
        for section in ("A1.1", "A2.1", "A3.1", "A4.1", "A5.1", "A6.1"):
            if section not in content:
                failures.append(f"Advanced hold register is missing {section}")

    fixture = ROOT / "demo" / "advanced-demo-fixtures.json"
    if fixture.is_file():
        data = json.loads(fixture.read_text(encoding="utf-8"))
        if data.get("privacy", {}).get("synthetic") is not True:
            failures.append("Advanced fixture is not marked synthetic")
        if data.get("status") == "professionally_reviewed":
            failures.append("Advanced fixture may not claim professional review")

    if not failures:
        warnings.append("External reviews, UI receipts, practice proofs, and learner pilot still remain human evidence gates.")

    print("# Advanced quality-gate audit\n")
    print(f"- Required quality files checked: **{len(REQUIRED_FILES)}**")
    print(f"- Current scripts expected: **{EXPECTED}**")
    print(f"- Critical findings: **{len(failures)}**")
    print(f"- Honest remaining-gate notes: **{len(warnings)}**")

    if warnings:
        print("\n## Remaining gates")
        for warning in warnings:
            print(f"- {warning}")

    if failures:
        print("\n## Failures")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nAdvanced has the internal quality controls required for Austin review without overstating external clearance.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
