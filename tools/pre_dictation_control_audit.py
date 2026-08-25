#!/usr/bin/env python3
"""Audit the Orange Plan Academy pre-dictation control layer."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "CURRENT-COURSE.md",
    "ADVANCED-CURRENT.md",
    "ADVANCED-APP-CONTRACT.md",
    "ADVANCED-NUMBER-PROVENANCE-REGISTRY.md",
    "ADVANCED-FILMING-READINESS.md",
    "00-START-HERE-AUSTIN-REVIEW.md",
    "AUSTIN-FULL-REVIEW-INDEX.md",
    "COURSE-APP-CONTRACT.md",
    "BUILD-YOUR-PLAN-CROSSWALK.md",
    "DEMO-HOUSEHOLD.md",
    "AUSTIN-DEMO-DECISIONS.md",
    "AUSTIN-REVIEW-INDEX.md",
    "DICTATION-ORDER.md",
    "AUSTIN-REVIEW-HOLD-REGISTER.md",
    "AI-PLANNING-QUESTION-GUIDE.md",
    "DEMO-CHECKPOINT-RUN-SHEET.md",
    "PRE-DICTATION-QA.md",
    "FILMING-READINESS.md",
    "MY-ORANGE-PLAN-CAPSTONE.md",
    "ADVANCED-GATES.md",
    "VISUAL-PRODUCTION-BRIEFS.md",
    "scripts/00-3_DEMO_use-orange-plan-ai.md",
    "research/AI-LESSON-VISUAL-BRIEF.md",
    "review/README.md",
    "review/MANIFEST.md",
    "review/modules/00-start-here.md",
    "review/AI-PLANNING-QUESTION-GUIDE.md",
    "review/advanced/README.md",
    "review/advanced/LEARNER-QUESTION-MAP.md",
    "review/advanced/DICTATION-ORDER.md",
    "review/advanced/HOLD-REGISTER.md",
    "review/advanced/JUDGMENT-REVIEW.md",
    "curriculum/advanced-learner-questions.json",
    "research/ADVANCED-LEGACY-MIGRATION.md",
    "research/ADVANCED-WORKED-EXAMPLE-AUDIT.md",
    "research/ADVANCED-SLIDE-CORRECTION-MAP.md",
    "research/ADVANCED-VISUAL-BRIEFS.md",
    "research/ADVANCED-DEMO-AND-WALKTHROUGH-PLAN.md",
    "research/ADVANCED-DEMO-RUN-SHEETS.md",
    "research/ADVANCED-PILOT-TEST-PLAN.md",
    "demo/demo-v1-inputs.json",
    "demo/ENGINE-CHECKPOINT-CANDIDATE-3105664.md",
    "demo/VISUAL-DATA-RECEIPT-3105664.md",
    "demo/UI-ACCEPTANCE-CHECKLIST-3105664.md",
    "professional-review/README.md",
    "professional-review/AUTHORITATIVE-SOURCE-VERIFICATION.md",
    "professional-review/ADVANCED-AUTHORITATIVE-SOURCE-VERIFICATION.md",
    "professional-review/ADVANCED-REVIEW-ACCEPTANCE.md",
    "professional-review/SEND-CHECKLIST.md",
    "professional-review/CANDIDATE-REVIEWERS.md",
    "professional-review/CPA-SEND.md",
    "professional-review/CUSTODY-SEND.md",
    "professional-review/ESTATE-ATTORNEY-SEND.md",
    "professional-review/INSURANCE-SEND.md",
    "professional-review/LENDING-SEND.md",
    "professional-review/HEALTHCARE-SEND.md",
    "professional-review/CPA-ADVANCED-SEND.md",
    "professional-review/CUSTODY-ADVANCED-SEND.md",
    "professional-review/ESTATE-ADVANCED-SEND.md",
    "professional-review/ADVANCED-PROFESSIONAL-REVIEW-TRACKER.md",
    "research/CLIENT-CALL-VOICE-EVIDENCE.md",
    "research/CLIENT-CONFUSION-REGISTRY.md",
    "research/CORE-OWNERSHIP-AND-RUNTIME.md",
    "research/DEMO-NUMBER-RECONCILIATION.md",
    "research/EDUCATIONAL-PROGRESSION-AUDIT.md",
    "research/SLIDE-CORRECTION-MAP.md",
    "tools/advanced_course_audit.py",
    "tools/advanced_gate_audit.py",
    "tools/advanced_voice_lint.py",
)

FORBIDDEN_CURRENT_DIRECTORIES = ("review-packets",)

CURRENT_TEXT_PATHS = (
    "README.md",
    "CURRENT-COURSE.md",
    "ADVANCED-CURRENT.md",
    "ADVANCED-APP-CONTRACT.md",
    "ADVANCED-FILMING-READINESS.md",
    "COURSE-APP-CONTRACT.md",
    "BUILD-YOUR-PLAN-CROSSWALK.md",
    "DEMO-HOUSEHOLD.md",
    "AUSTIN-DEMO-DECISIONS.md",
    "AUSTIN-REVIEW-INDEX.md",
    "DICTATION-ORDER.md",
    "AUSTIN-REVIEW-HOLD-REGISTER.md",
    "AI-PLANNING-QUESTION-GUIDE.md",
    "DEMO-CHECKPOINT-RUN-SHEET.md",
    "PRE-DICTATION-QA.md",
    "FILMING-READINESS.md",
    "MY-ORANGE-PLAN-CAPSTONE.md",
    "ADVANCED-GATES.md",
    "VISUAL-PRODUCTION-BRIEFS.md",
    "professional-review/README.md",
    "professional-review/SEND-CHECKLIST.md",
    "professional-review/ADVANCED-REVIEW-ACCEPTANCE.md",
    "review/README.md",
    "review/MANIFEST.md",
    "review/advanced/README.md",
    "review/advanced/DICTATION-ORDER.md",
    "review/advanced/HOLD-REGISTER.md",
)

STALE_REFERENCE_PATTERNS = {
    "retired review/ professional-packet path": re.compile(r"(?<!professional-)\breview/(?:CPA|CUSTODY|ESTATE|INSURANCE)-REVIEW", re.I),
    "retired review-packets/ path": re.compile(r"\breview-packets/", re.I),
    "encrypted export described as currently restorable": re.compile(
        r"(?:encrypted (?:backup|export)|exported file).{0,90}(?:restore the plan|restorable plan data|use it to restore)",
        re.I | re.S,
    ),
    "superseded engine candidate": re.compile(r"ENGINE-CHECKPOINT-CANDIDATE-4456b3c", re.I),
}

REQUIRED_PHRASES = {
    "CURRENT-COURSE.md": (
        "Austin's voice-and-judgment review is ready to begin",
        "Use Orange Plan AI to understand the numbers and make better decisions",
        "ENGINE-CHECKPOINT-CANDIDATE-3105664.md",
        "ADVANCED-CURRENT.md",
        "18",
    ),
    "ADVANCED-CURRENT.md": (
        "18 current Advanced scripts",
        "18 matching student lesson texts",
        "ready for Austin voice-and-judgment review",
        "scripts/advanced/current/",
        "ADVANCED-APP-CONTRACT.md",
        "ADVANCED-NUMBER-PROVENANCE-REGISTRY.md",
        "ADVANCED-AUTHORITATIVE-SOURCE-VERIFICATION.md",
    ),
    "ADVANCED-APP-CONTRACT.md": (
        "Saved Plan input",
        "Preview",
        "Scenario",
        "External evidence",
        "A6.2",
    ),
    "ADVANCED-FILMING-READINESS.md": (
        "Primary-source verification",
        "Professional packets",
        "Learner pilot design",
        "Austin first review",
    ),
    "PRE-DICTATION-QA.md": (
        "Reproducible app-engine outputs",
        "External professional responses",
        "Build Your Plan preview",
        "46 scripts and 46 matching lesson texts",
    ),
    "README.md": (
        "In-app plan restore is currently unavailable",
        "professional-review/",
        "scripts/advanced/current/",
    ),
    "professional-review/README.md": (
        "Actual outside sign-off is not complete",
        "ADVANCED-AUTHORITATIVE-SOURCE-VERIFICATION.md",
        "ADVANCED-REVIEW-ACCEPTANCE.md",
        "LENDING-SEND.md",
        "HEALTHCARE-SEND.md",
    ),
    "professional-review/ADVANCED-REVIEW-ACCEPTANCE.md": (
        "Minimum response standard",
        "Cross-disciplinary claims",
        "Rejection criteria",
    ),
    "review/README.md": (
        "AI-PLANNING-QUESTION-GUIDE.md",
        "screen-share run sheet",
        "advanced/DICTATION-ORDER.md",
    ),
    "review/advanced/README.md": (
        "current Advanced review set is complete",
        "GATE",
        "ADVANCED ONLY",
    ),
    "review/advanced/DICTATION-ORDER.md": (
        "18 conditional lessons",
        "14,805 spoken words",
        "A6.2",
    ),
    "AUSTIN-FULL-REVIEW-INDEX.md": (
        "46 current scripts",
        "Core first",
        "Advanced waves",
    ),
    "BUILD-YOUR-PLAN-CROSSWALK.md": (
        "deployed Build Your Plan flow",
        "app_completion_rule",
        "human_completion_rule",
    ),
    "scripts/00-3_DEMO_use-orange-plan-ai.md": (
        "Review the current plan and rank what matters",
        "Explain a confusing number from its sources",
        "Turn the answer into action",
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
            failures.append(f"retired duplicate control directory still exists: {relative_path}/")

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

    core_index = ROOT / "AUSTIN-REVIEW-INDEX.md"
    if core_index.is_file():
        linked_scripts = set(re.findall(r"\(scripts/(\d{2}-\d+_[^)]+\.md)\)", core_index.read_text(encoding="utf-8")))
        if len(linked_scripts) != 28:
            failures.append(f"AUSTIN-REVIEW-INDEX.md links {len(linked_scripts)} unique core scripts; expected 28")

    advanced_contract = ROOT / "curriculum/advanced-learner-questions.json"
    if advanced_contract.is_file():
        entries = json.loads(advanced_contract.read_text(encoding="utf-8")).get("lessons", [])
        if len(entries) != 18:
            failures.append(f"advanced learner-question contract has {len(entries)} entries; expected 18")
        for entry in entries:
            for field in ("id", "script", "lessonText", "gate", "question", "decision", "example", "returnToCore", "holds"):
                value = entry.get(field)
                if value is None or value == "" or value == []:
                    failures.append(f"advanced contract {entry.get('id', 'UNKNOWN')}: blank {field}")

    contract = ROOT / "COURSE-APP-CONTRACT.md"
    if contract.is_file():
        match = re.search(r"App source (?:reviewed|verified):.*?`([0-9a-f]{7,40})`", contract.read_text(encoding="utf-8"), flags=re.I)
        if not match:
            failures.append("COURSE-APP-CONTRACT.md: missing last-reviewed app commit")

    advanced_app_contract = ROOT / "ADVANCED-APP-CONTRACT.md"
    if advanced_app_contract.is_file():
        app_text = advanced_app_contract.read_text(encoding="utf-8")
        for lesson_id in [f"A1.{i}" for i in range(1, 3)] + [f"A2.{i}" for i in range(1, 5)] + [f"A3.{i}" for i in range(1, 5)] + [f"A4.{i}" for i in range(1, 4)] + [f"A5.{i}" for i in range(1, 4)] + [f"A6.{i}" for i in range(1, 3)]:
            if lesson_id not in app_text:
                failures.append(f"ADVANCED-APP-CONTRACT.md missing {lesson_id}")

    decisions = ROOT / "AUSTIN-DEMO-DECISIONS.md"
    if decisions.is_file() and "APPROVED" not in decisions.read_text(encoding="utf-8").upper():
        failures.append("AUSTIN-DEMO-DECISIONS.md should retain an obvious APPROVED state")

    professional = ROOT / "professional-review/README.md"
    if professional.is_file() and professional.read_text(encoding="utf-8").count("NOT SENT") < 9:
        warnings.append("professional-review/README.md should visibly show all Core and Advanced review areas as NOT SENT")

    print("# Pre-dictation control audit\n")
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

    print("\nThe repository has one current Core and Advanced review path, reconciled demo and professional controls, and no stale packet or restore-language regression.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
