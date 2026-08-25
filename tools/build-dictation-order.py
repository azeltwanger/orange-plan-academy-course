#!/usr/bin/env python3
"""Build the current Austin review and dictation order from CURRENT-COURSE.md.

This generator deliberately ignores MASTER-COURSE.md and other migration layers.
The current Core outline lives in CURRENT-COURSE.md; spoken runtimes come from
exactly the 28 current scripts using the same spoken-text parser as voice_lint.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from voice_lint import WORD, spoken_text  # noqa: E402

WPM = 155
REVIEW_ORDER = (1, 2, 6, 3, 4, 5, 7, 8, 9, 0)
SCRIPT_NAME = re.compile(r"^(\d{2})-(\d+)_.*\.md$")
MODULE_HEADING = re.compile(r"^### Module (\d+) — (.+)$", re.M)
LESSON_LINE = re.compile(r"^- (\d+\.\d+) · (.+)$", re.M)


@dataclass(frozen=True)
class Script:
    lesson_id: str
    path: Path
    title: str
    status: str
    words: int

    @property
    def minutes(self) -> float:
        return self.words / WPM


@dataclass(frozen=True)
class Module:
    number: int
    title: str
    lessons: tuple[tuple[str, str], ...]


def parse_modules() -> list[Module]:
    text = (ROOT / "CURRENT-COURSE.md").read_text(encoding="utf-8")
    matches = list(MODULE_HEADING.finditer(text))
    modules: list[Module] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        lessons = tuple(LESSON_LINE.findall(text[start:end]))
        if lessons:
            modules.append(Module(int(match.group(1)), match.group(2).strip(), lessons))
    return modules


def parse_scripts() -> dict[str, Script]:
    scripts: dict[str, Script] = {}
    for path in sorted((ROOT / "scripts").glob("*.md")):
        match = SCRIPT_NAME.match(path.name)
        if not match or "WALKTHROUGH" in path.name.upper() or "DEMO" in path.name.upper():
            continue
        lesson_id = f"{int(match.group(1))}.{int(match.group(2))}"
        content = path.read_text(encoding="utf-8")
        lines = content.splitlines()
        title = lines[1].split(" ", 1)[1].strip() if len(lines) > 1 and " " in lines[1] else lesson_id
        status_line = lines[2] if len(lines) > 2 else ""
        status = status_line.split("·", 1)[1].strip() if "·" in status_line else "Austin review pending"
        words = len(WORD.findall(spoken_text(content)))
        scripts[lesson_id] = Script(lesson_id, path.relative_to(ROOT), title, status, words)
    return scripts


def module_minutes(module: Module, scripts: dict[str, Script]) -> float:
    return sum(scripts[lesson_id].minutes for lesson_id, _ in module.lessons)


def render_module(module: Module, scripts: dict[str, Script]) -> list[str]:
    lines = [
        f"### Module {module.number} — {module.title} · {module_minutes(module, scripts):.1f} min",
        "",
        "| Lesson | Current script | Words | Min | Review status |",
        "|---|---|---:|---:|---|",
    ]
    for lesson_id, outline_title in module.lessons:
        script = scripts[lesson_id]
        lines.append(
            f"| {lesson_id} | [{outline_title}]({script.path.as_posix()}) | "
            f"{script.words:,} | {script.minutes:.1f} | {script.status} |"
        )
    lines.append("")
    return lines


def main() -> int:
    modules = parse_modules()
    scripts = parse_scripts()
    outlined = [lesson_id for module in modules for lesson_id, _ in module.lessons]
    missing = [lesson_id for lesson_id in outlined if lesson_id not in scripts]
    extras = sorted(set(scripts) - set(outlined))
    if missing or extras or len(outlined) != 28:
        raise SystemExit(
            f"Current-course/script mismatch: outlined={len(outlined)}, missing={missing}, extras={extras}"
        )

    module_by_number = {module.number: module for module in modules}
    total_words = sum(script.words for script in scripts.values())
    total_minutes = total_words / WPM

    out: list[str] = [
        "# Austin review and dictation order",
        "",
        "**Current Core only.** Generated from `CURRENT-COURSE.md` and the 28 current `scripts/` files. "
        "Do not use `MASTER-COURSE.md`, old decks, aggregate scripts, or retired walkthroughs as the recording source.",
        "",
        f"**28 teach lessons · {total_words:,} spoken words · {total_minutes:.1f} min "
        f"({total_minutes / 60:.1f} h) at {WPM} wpm.**",
        "",
        "Austin may begin the voice-and-judgment review in the wave order below. "
        "A named UI or professional hold blocks `AUSTIN APPROVED` and filming; it does not require rebuilding or rereading unrelated concept prose.",
        "",
        "Walkthroughs are not dictated from these scripts. They are recorded later from the verified Build Your Plan run sheets after the deployed routes, labels, and completion rules are accepted.",
        "",
        "## What is locked before the read",
        "",
        "Do not recalculate or casually replace these during dictation:",
        "",
        "- One household retirement start: March 2036, Alex age 55.",
        "- Plan confidence target: 80%; current confidence: 94.6%; earliest target-qualified date: May 2032, Alex age 51.",
        "- Cash Flow: $3,761/month after the saved debt strategy; full route is $500 extra debt plus $3,500 account contributions; $261 operating cushion.",
        "- Allocation: $270,000 app denominator; 64.8% Bitcoin; 50% target; 40–60% review band; $131,250 Bitcoin loss in a 75% drawdown.",
        "- Retirement paycheck: keep $100,000/year; first-year total draw is $101,948; Bitcoin sale is $97,948 or 0.079251 BTC at the projected price.",
        "- Scenario: 4% inflation produces 91.6% confidence, 3.0 percentage points below the 3% Baseline.",
        "- Borrowing is excluded from the saved Core baseline and remains a gated comparison.",
        "- Reserve, Bridge, Healthcare Bridge, and Legacy are planning jobs; the current app wording governs any final on-screen label.",
        "",
        "## What Austin is reviewing",
        "",
        "- **Voice:** would I naturally say this?",
        "- **Judgment:** do I agree with the recommendation and trade-off?",
        "- **Example:** does Alex and Jordan's plan make the decision easier to understand?",
        "- **Finish line:** would the learner know what was decided and when the lesson is complete?",
        "",
        "Use `APPROVE`, `TIGHTEN`, `SAY IT THIS WAY`, `JUDGMENT`, `APP`, `PRO`, or `REMOVE`. "
        "Do not rewrite a correct section merely because another sentence is possible.",
        "",
        "## Review wave order",
        "",
        "The review starts with the biggest app and number changes, then strategy, then protection, then framing. "
        "This is not the learner's final publishing order.",
        "",
    ]

    for module_number in REVIEW_ORDER:
        out.extend(render_module(module_by_number[module_number], scripts))

    out.extend([
        "---",
        "",
        "## Final learner recording order",
        "",
        "After every named hold is cleared and the scripts are marked `AUSTIN APPROVED`, record the concept lessons in learner order:",
        "",
    ])
    for module in modules:
        ids = " · ".join(lesson_id for lesson_id, _ in module.lessons)
        out.append(f"- **Module {module.number} — {module.title}:** {ids}")

    out.extend([
        "",
        "## Approval boundary",
        "",
        "A voice-and-judgment review can be complete while an `APP` or `PRO` line remains held. "
        "The lesson becomes `AUSTIN APPROVED` only after that named hold is checked, the matching lesson text is reconciled, and Austin completes one clean final read of the corrected lesson.",
        "",
        "Regenerate after any current script or outline change:",
        "",
        "```bash",
        "python3 tools/build-dictation-order.py",
        "```",
        "",
    ])

    (ROOT / "DICTATION-ORDER.md").write_text("\n".join(out), encoding="utf-8")
    print(
        f"DICTATION-ORDER.md regenerated — 28 lessons, {total_words:,} spoken words, "
        f"{total_minutes:.1f} min"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
