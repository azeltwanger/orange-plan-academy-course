#!/usr/bin/env python3
"""Apply Austin's teach-video versus walkthrough rule before dictation.

Teach lessons carry the decision and the number the learner should write down.
They do not narrate settings screens that the module walkthrough already owns.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_regex(path: str, pattern: str, replacement: str, label: str, *, flags: int = 0) -> None:
    text = read(path)
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match in {path}, found {count}")
    write(path, updated)


SOURCE = """# Austin source material — teach lesson to walkthrough handoff

**Received:** 2026-08-26  
**Source:** Austin's direct course-revision instruction

## Exact instruction

> Am I reading this or are we doing this in the walkthrough? need a clean segway if I'm reading it like \"I will show you exactly how to enter it during the walkthorugh lesson.\"

## Course rule

- The teach video explains the decision, example, trade-off, and number to write down.
- The teach video does not read a settings-screen click path that is demonstrated in the module walkthrough.
- A natural spoken handoff is enough: write down the decision now; the walkthrough will show exactly where to enter it and how the app uses it.
- Student reference text may still show the exact path so the learner can find it later.
"""
write("source-material/2026-08-26-teach-walkthrough-handoff.md", SOURCE)

SCRIPT_PATH = "scripts/02-2_size-your-cash-reserve-in-months-of-spen.md"
SCRIPT_CLOSE = """== PUT IT IN ORANGE PLAN ==

For now, write down your bare-bones spending and the number of months you want to hold. In the walkthrough for this module, I'll show you exactly where to enter both of those numbers in Orange Plan, how the app calculates your reserve target, and how to compare that target to the cash you already have.

== YOU ARE DONE WHEN ==

You're done with this lesson when those two numbers are written down and you can explain what the reserve is there to protect you from: a bad month forcing you to sell Bitcoin at the wrong time.
"""
replace_regex(
    SCRIPT_PATH,
    r"(?ms)^== PUT IT IN ORANGE PLAN ==\n.*?^== YOU ARE DONE WHEN ==\n.*?\Z",
    SCRIPT_CLOSE.rstrip() + "\n",
    "2.2 spoken walkthrough handoff",
)

# Keep the master as the richer reference, but make the spoken boundary clear.
master = read("MASTER-COURSE.md")
lesson_match = re.search(
    r"(?ms)^## 2\.2 Size your cash reserve in months of spending\n.*?(?=^## 2\.3 )",
    master,
)
if not lesson_match:
    raise RuntimeError("MASTER-COURSE 2.2 section not found")
section = lesson_match.group(0)
section_updated, count = re.subn(
    r"(?ms)^### Put it in Orange Plan\n.*?^### You are done when\n.*?(?=\n\n|\Z)",
    """### Before the walkthrough

Write down the bare-bones spending number and target months. During the module walkthrough, Austin shows exactly where to enter both numbers, how Orange Plan calculates the reserve target, and how to compare the target with current cash.

### You are done when

The two numbers are written down and the learner can explain the reserve's job: preventing a bad month from forcing a Bitcoin sale at the wrong time.""",
    section,
    count=1,
)
if count != 1:
    raise RuntimeError(f"MASTER-COURSE 2.2 handoff: expected one match, found {count}")
write("MASTER-COURSE.md", master[: lesson_match.start()] + section_updated + master[lesson_match.end() :])

# Student text can preserve the exact path as a reference, while making clear
# that it is demonstrated rather than read in the teach video.
replace_regex(
    "lesson-text/02-2_size-your-cash-reserve-in-months-of-spen.md",
    r"(?ms)^## Put it in Orange Plan\n.*?^## You are done when\n.*?\Z",
    """## In the module walkthrough

For now, write down your bare-bones spending and target months. The walkthrough demonstrates **Cash Flow → Reserve settings**, shows where to enter both numbers, and compares the calculated target with the cash you already hold.

Reference formula: **bare-bones spending × target months = reserve target.**

## You are done when

Those two numbers are written down and you can explain the reserve's job: preventing a bad month from forcing a Bitcoin sale at the wrong time.
""".rstrip() + "\n",
    "2.2 student walkthrough handoff",
)

# Preserve the rule in the voice guide so later scripts do not recreate the
# same duplicate-click problem.
voice_path = "scripts/VOICE-GUIDE.md"
voice = read(voice_path)
heading = "## Teach lesson versus walkthrough — Austin, 2026-08-26"
if heading not in voice:
    marker = "## Teach-lesson closings + walkthrough hand-off"
    addition = """## Teach lesson versus walkthrough — Austin, 2026-08-26

The teach video does **not** read a settings-screen click path that the module walkthrough demonstrates. The teach lesson should end the topic with the decision or number the learner needs to carry forward, then use a plain handoff such as:

> For now, write down those two numbers. In the walkthrough for this module, I'll show you exactly where to enter them in Orange Plan and how the app uses them.

The exact path stays in the walkthrough sheet and student reference text. A teach lesson may name the owning page when that helps orientation, but it should not narrate the clicks twice.

"""
    if marker not in voice:
        raise RuntimeError("VOICE-GUIDE handoff marker not found")
    voice = voice.replace(marker, addition + marker, 1)
    write(voice_path, voice)

print("teach-to-walkthrough handoff pass applied")
