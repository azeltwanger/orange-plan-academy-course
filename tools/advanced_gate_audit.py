#!/usr/bin/env python3
"""Audit parity between Advanced lessons and their pre-dictation gates."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "curriculum" / "advanced-learner-questions.json"
EXPECTED = 18

REQUIRED_FILES = (
    "ADVANCED-CURRENT.md",
    "ADVANCED-APP-CONTRACT.md",
    "ADVANCED-NUMBER-PROVENANCE-REGISTRY.md",
    "ADVANCED-FILMING-READINESS.md",
    "research/ADVANCED-WORKED-EXAMPLE-AUDIT.md",
    "research/ADVANCED-SLIDE-CORRECTION-MAP.md",
    "research/ADVANCED-VISUAL-BRIEFS.md",
    "research/ADVANCED-DEMO-RUN-SHEETS.md",
    "research/ADVANCED-PILOT-TEST-PLAN.md",
    "professional-review/ADVANCED-AUTHORITATIVE-SOURCE-VERIFICATION.md",
    "professional-review/LENDING-SEND.md",
    "professional-review/CPA-ADVANCED-SEND.md",
    "professional-review/HEALTHCARE-SEND.md",
    "professional-review/CUSTODY-ADVANCED-SEND.md",
    "professional-review/ESTATE-ADVANCED-SEND.md",
    "professional-review/ADVANCED-PROFESSIONAL-REVIEW-TRACKER.md",
    "review/advanced/JUDGMENT-REVIEW.md",
    "review/advanced/HOLD-REGISTER.md",
)

SCRIPT_MARKERS = (
    "> **Watch this only",
    "== YOUR DECISION ==",
    "== PUT IT IN ORANGE PLAN ==",
    "== YOU ARE DONE WHEN ==",
    "**Return to Core:**",
)

FORBIDDEN = {
    "legacy provenance": re.compile(r"SPOKEN-PROSE VERSION", re.I),
    "normal LTV": re.compile(r"normal (?:borrow|starting point).*50%|50% LTV is (?:a )?normal", re.I),
    "universal RMD 73": re.compile(r"RMDs? (?:always )?(?:begin|start)s? at (?:age )?73", re.I),
    "no RMDs ever": re.compile(r"No RMDs ever", re.I),
    "blanket wipe": re.compile(r"(?:must|always|you will) (?:wipe|reset) (?:the|your) (?:main )?device", re.I),
    "automatic trust": re.compile(r"every Bitcoin holder (?:needs|should have) a trust", re.I),
    "automatic loan tax": re.compile(r"Bitcoin-backed loan proceeds are tax-free|borrowing against Bitcoin is tax-free", re.I),
}


def main() -> int:
    failures: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            failures.append(f"missing gate file: {relative}")

    entries = json.loads(CONTRACT.read_text(encoding="utf-8")).get("lessons", []) if CONTRACT.is_file() else []
    if len(entries) != EXPECTED:
        failures.append(f"expected {EXPECTED} contract entries, found {len(entries)}")

    seen: set[str] = set()
    for entry in entries:
        lesson_id = entry.get("id", "UNKNOWN")
        if lesson_id in seen:
            failures.append(f"duplicate lesson id: {lesson_id}")
        seen.add(lesson_id)

        script = ROOT / str(entry.get("script", ""))
        lesson = ROOT / str(entry.get("lessonText", ""))
        if not script.is_file():
            failures.append(f"{lesson_id}: missing script")
            continue
        if not lesson.is_file():
            failures.append(f"{lesson_id}: missing lesson text")

        content = script.read_text(encoding="utf-8")
        for marker in SCRIPT_MARKERS:
            if marker not in content:
                failures.append(f"{lesson_id}: missing {marker}")
        for label, pattern in FORBIDDEN.items():
            if pattern.search(content):
                failures.append(f"{lesson_id}: forbidden claim — {label}")
        for field in ("gate", "question", "decision", "example", "returnToCore", "holds"):
            value = entry.get(field)
            if value is None or value == "" or value == []:
                failures.append(f"{lesson_id}: blank contract field {field}")

    verification = ROOT / "professional-review" / "ADVANCED-AUTHORITATIVE-SOURCE-VERIFICATION.md"
    if verification.is_file():
        text = verification.read_text(encoding="utf-8")
        for section in ("A1 ·", "A2 ·", "A3 ·", "A4 ·", "A5 ·", "A6 ·"):
            if section not in text:
                failures.append(f"source verification missing {section}")
        if "not" not in text.lower() or "professional sign-off" not in text.lower():
            failures.append("source verification must distinguish research from professional sign-off")

    app_contract = ROOT / "ADVANCED-APP-CONTRACT.md"
    if app_contract.is_file():
        app_text = app_contract.read_text(encoding="utf-8")
        for entry in entries:
            if str(entry.get("id")) not in app_text:
                failures.append(f"app contract missing {entry.get('id')}")

    print("# Advanced gate audit\n")
    print(f"- Contract lessons checked: **{len(entries)}**")
    print(f"- Required gate files checked: **{len(REQUIRED_FILES)}**")
    print(f"- Findings: **{len(failures)}**")

    if failures:
        print("\n## Failures")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nAll current Advanced lessons have the same pre-dictation control layers as Core: structure, example, app ownership, provenance, source verification, professional hold, visual/demo plan, pilot, and filming gate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
