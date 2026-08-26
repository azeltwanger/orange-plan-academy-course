#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from config import ADVANCED_FILENAMES, ADVANCED_ORDER, CORE_FILENAMES, DICTATED, MODULES, VISUALS

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
ADV = SCRIPTS / "advanced"

expected_teach = [n for m in MODULES for n in m["lessons"]]
expected_captures = [n for m in MODULES for n in m["captures"]]

errors = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


core_files = {p.name for p in SCRIPTS.glob("*.md") if p.name not in {"README.md", "VOICE-GUIDE.md"}}
expected_files = {CORE_FILENAMES[n] for n in expected_teach + expected_captures}
check(core_files == expected_files, f"Core file mismatch: missing={expected_files-core_files}, extra={core_files-expected_files}")

adv_files = {p.name for p in ADV.glob("*.md")}
expected_adv_files = {ADVANCED_FILENAMES[n] for n in ADVANCED_ORDER}
check(adv_files == expected_adv_files, f"Advanced file mismatch: missing={expected_adv_files-adv_files}, extra={adv_files-expected_adv_files}")

check(len(expected_teach) == 28, f"Expected 28 teach lessons, got {len(expected_teach)}")
check(len(expected_captures) == 10, f"Expected 10 walkthroughs/demos, got {len(expected_captures)}")
check(len(ADVANCED_ORDER) == 14, f"Expected 14 advanced lessons, got {len(ADVANCED_ORDER)}")

for number in expected_teach:
    text = (SCRIPTS / CORE_FILENAMES[number]).read_text(encoding="utf-8")
    check(f"segment {number}" in text.splitlines()[0], f"Wrong segment header for {number}")
    if number in DICTATED:
        check("AUSTIN DICTATION" in text[:700], f"Dictated status missing for {number}")
    else:
        check("PRE-DICTATION FILMING DRAFT" in text[:900], f"Draft status missing for {number}")
        for phrase in ("== YOUR DECISION ==", "== PUT IT IN ORANGE PLAN ==", "== YOU ARE DONE WHEN =="):
            check(phrase not in text, f"Generated close remains in {number}: {phrase}")

for number in expected_captures:
    text = (SCRIPTS / CORE_FILENAMES[number]).read_text(encoding="utf-8")
    check(text.startswith(f"# {number} ·"), f"Capture heading wrong for {number}")

for number in ADVANCED_ORDER:
    text = (ADV / ADVANCED_FILENAMES[number]).read_text(encoding="utf-8")
    check("PRE-DICTATION FILMING DRAFT" in text[:900], f"Advanced draft status missing for {number}")
    check("PUBLICATION GATE:" in text[:1200], f"Advanced gate missing for {number}")

master = (ROOT / "MASTER-COURSE.md").read_text(encoding="utf-8")
order = [
    "Module 2 — Cash Flow + Reserve",
    "Module 3 — Allocation + Next-Dollar",
    "Module 4 — Debt Strategy",
]
positions = [master.find(item) for item in order]
check(all(p >= 0 for p in positions) and positions == sorted(positions), f"Module 2/3/4 order wrong: {positions}")
check("first full 1,000-path confidence result is saved in Module 9" in master, "Master does not defer full confidence to Module 9")

reserve = (SCRIPTS / CORE_FILENAMES["2.2"]).read_text(encoding="utf-8")
check("Orange Plan calculates the target" in reserve, "Reserve target ownership not corrected")
check("you do that multiplication, not the app" not in reserve.lower(), "Manual Reserve multiplication claim remains")

foundation = (SCRIPTS / CORE_FILENAMES["1.4"]).read_text(encoding="utf-8")
check("Module 5 owns that work" in foundation, "Foundation does not defer historical tax reconstruction")
check("income, living expenses" in foundation.lower(), "Foundation handoff to later modules missing")

allocation = (SCRIPTS / CORE_FILENAMES["3.5"]).read_text(encoding="utf-8")
check("Extra debt is provisional" in allocation or "extra-debt claim" in allocation, "Allocation does not mark Debt as provisional")
check("Build Your Plan" in allocation and "Allocation" in allocation, "Allocation Build Your Plan handoff missing")

debt = (SCRIPTS / CORE_FILENAMES["4.2"]).read_text(encoding="utf-8")
check("Return to the contribution waterfall" in debt, "Debt does not return to the waterfall")

income = (SCRIPTS / CORE_FILENAMES["6.4"]).read_text(encoding="utf-8")
check("first saved full 1,000-path confidence run waits until Module 9" in income, "Income walkthrough runs confidence too early")

finish = (SCRIPTS / CORE_FILENAMES["9.3"]).read_text(encoding="utf-8")
check("Run the first full confidence check" in finish, "Module 9 full confidence step missing")

all_core_text = "\n".join((SCRIPTS / CORE_FILENAMES[n]).read_text(encoding="utf-8") for n in expected_teach)
check(all_core_text.count("🎬 VISUAL") >= 20, "Too few visual cues survived the rebuild")
for number in VISUALS:
    check(number in expected_teach, f"Visual map points to unknown lesson {number}")

for path in [
    ROOT / "MASTER-COURSE.md",
    ROOT / "MASTER-ADVANCED.md",
    ROOT / "ALL-SCRIPTS.md",
    ROOT / "FINALIZATION-STATUS.md",
    ROOT / "DICTATION-ORDER.md",
    ROOT / "FILM-ORDER.md",
    ROOT / "SCREEN-SHOOT-LIST.md",
    ROOT / "MODULE-CHECKPOINTS.md",
    ROOT / "CIRCLE-STRUCTURE.md",
    ROOT / "COURSE-REBUILD-REPORT.md",
]:
    check(path.exists() and path.stat().st_size > 100, f"Missing or empty generated file: {path.name}")

lesson_files = list((ROOT / "lesson-text").glob("*.md"))
advanced_lesson_files = list((ROOT / "lesson-text" / "advanced").glob("*.md"))
check(len(lesson_files) == len(expected_teach) + len(expected_captures), f"Lesson-text count wrong: {len(lesson_files)}")
check(len(advanced_lesson_files) == 14, f"Advanced lesson-text count wrong: {len(advanced_lesson_files)}")

check(not (ROOT / "SLOP-ACCEPTED.md").exists(), "SLOP-ACCEPTED.md should be retired")

if errors:
    print("COURSE REBUILD VERIFICATION FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("COURSE REBUILD VERIFIED")
print(f"Core teach: {len(expected_teach)}")
print(f"Core captures: {len(expected_captures)}")
print(f"Advanced teach: {len(ADVANCED_ORDER)}")
print(f"Visual cues: {all_core_text.count('🎬 VISUAL')}")
