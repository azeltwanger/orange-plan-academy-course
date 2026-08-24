#!/usr/bin/env python3
"""Validate the Core learner-question contract before script approval."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "curriculum" / "core-learner-questions.json"
EXPECTED_IDS = {"0.1","0.2","1.1","1.2","1.3","2.1","2.2","2.3","2.4","3.1","4.1","4.2","4.3","4.4","5.1","5.2","6.1","6.2","6.3","7.1","7.2","7.3","8.1","8.2","8.3","8.4","9.1","9.2"}
QUESTION_START = re.compile(r"^(what|how|when|where|which|who|why|can|should|will|is|are|do|does)\b", re.I)


def words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def main() -> int:
    failures: list[str] = []
    if not CONTRACT.is_file():
        print(f"Missing contract: {CONTRACT.relative_to(ROOT)}")
        return 1

    payload = json.loads(CONTRACT.read_text(encoding="utf-8"))
    lessons = payload.get("lessons")
    if not isinstance(lessons, list):
        print("Contract must contain a lessons array")
        return 1

    by_id: dict[str, dict] = {}
    questions: dict[str, str] = {}
    for lesson in lessons:
        if not isinstance(lesson, dict):
            failures.append("Every lesson entry must be an object")
            continue
        lesson_id = str(lesson.get("id", "")).strip()
        if not lesson_id:
            failures.append("Lesson entry missing id")
            continue
        if lesson_id in by_id:
            failures.append(f"Duplicate lesson id: {lesson_id}")
        by_id[lesson_id] = lesson
        question = str(lesson.get("learnerQuestion", "")).strip()
        decision = str(lesson.get("decision", "")).strip()
        example = str(lesson.get("example", "")).strip()
        script = str(lesson.get("script", "")).strip()
        if not question.endswith("?"):
            failures.append(f"{lesson_id}: learner question must end with ?")
        if question and not QUESTION_START.search(question):
            failures.append(f"{lesson_id}: learner question should begin as a real question")
        if words(question) > 28:
            failures.append(f"{lesson_id}: learner question is longer than 28 words")
        normalized = question.casefold()
        if normalized in questions:
            failures.append(f"{lesson_id}: duplicates learner question from {questions[normalized]}")
        questions[normalized] = lesson_id
        if not decision:
            failures.append(f"{lesson_id}: missing decision")
        if not example:
            failures.append(f"{lesson_id}: missing example or orientation story")
        if not script:
            failures.append(f"{lesson_id}: missing script path")
        elif not (ROOT / script).is_file():
            failures.append(f"{lesson_id}: script does not exist: {script}")

    actual_ids = set(by_id)
    for missing in sorted(EXPECTED_IDS - actual_ids):
        failures.append(f"Missing Core lesson: {missing}")
    for extra in sorted(actual_ids - EXPECTED_IDS):
        failures.append(f"Unexpected Core lesson: {extra}")

    print("# Core learner-question audit\n")
    print(f"- Expected lessons: **{len(EXPECTED_IDS)}**")
    print(f"- Mapped lessons: **{len(actual_ids)}**")
    print(f"- Unique learner questions: **{len(questions)}**")
    print(f"- Findings: **{len(failures)}**")
    if failures:
        print("\n## Failures")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("\nEvery Core lesson has one real learner question, one decision, one example or orientation story, and a current script path.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
