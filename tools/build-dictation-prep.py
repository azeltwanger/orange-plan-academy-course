#!/usr/bin/env python3
"""Build pre-dictation working drafts from the protected research scripts.

The canonical scripts contain the researched facts and caveats. Austin has not
spoken most of them. This tool creates a separate, chronological dictation layer
that is deliberately less polished: a natural opener, a teaching path, examples,
app handoff, and finish line. The original research prose remains available in a
collapsed reference section, but it is not presented as Austin's script.

It also replaces lesson 1.3 with a fully rewritten working draft verified against
the current production onboarding calculation.
"""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DRAFTS = ROOT / "dictation-drafts"
SEPARATOR = "=" * 60

DICTATED_NUMBERS = {"0.1", "1.1", "1.2", "2.2"}
SPECIAL_SECTIONS = {
    "YOUR DECISION",
    "PUT IT IN ORANGE PLAN",
    "YOU ARE DONE WHEN",
    "HOMEWORK",
}

SLOP_STARTS = (
    "that's the whole",
    "that is the whole",
    "three documents, three jobs",
    "the date tells you when",
    "treat it as the first draft",
    "the output of this lesson is not",
    "the goal is not",
    "this is not a",
    "that is the tradeoff",
    "that's the tradeoff",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def lesson_number(text: str, path: Path) -> str:
    match = re.search(r"(?m)^(?:TELEPROMPTER SCRIPT — segment )?(A?\d+\.\d+)\b", text)
    if match:
        return match.group(1)
    match = re.match(r"(A?\d+)[-_](\d+)", path.name)
    if match:
        return f"{match.group(1)}.{match.group(2)}"
    raise RuntimeError(f"Could not identify lesson number: {path}")


def title_from(text: str, number: str) -> str:
    for line in text.splitlines()[:12]:
        clean = line.strip().lstrip("# ")
        match = re.match(rf"{re.escape(number)}\s*[·:-]?\s*(.+)", clean)
        if match:
            return match.group(1).strip()
    return number


def body_from(text: str) -> str:
    if SEPARATOR in text:
        return text.split(SEPARATOR, 1)[1].strip()
    return text.strip()


def split_sections(body: str) -> tuple[str, list[tuple[str, str]]]:
    heading = re.compile(r"(?m)^==\s+(.+?)\s+==\s*$")
    matches = list(heading.finditer(body))
    if not matches:
        return body.strip(), []
    intro = body[: matches[0].start()].strip()
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        sections.append((match.group(1).strip(), body[match.end() : end].strip()))
    return intro, sections


def sentences(paragraph: str) -> list[str]:
    paragraph = re.sub(r"\s+", " ", paragraph).strip()
    if not paragraph:
        return []
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"“])", paragraph) if part.strip()]


def is_slop(sentence: str) -> bool:
    lower = sentence.lower().strip(" \"'“”")
    return any(lower.startswith(prefix) for prefix in SLOP_STARTS)


def compact_paragraph(paragraph: str) -> str | None:
    paragraph = paragraph.strip()
    if not paragraph:
        return None
    if paragraph.startswith("<!--"):
        return None
    if paragraph.startswith("🎬") or paragraph.startswith("⚠"):
        return paragraph
    if paragraph.startswith(("- ", "* ", "> ", "|", "1. ", "2. ", "3. ", "4. ", "5. ", "6. ")):
        return paragraph

    parts = sentences(paragraph)
    if not parts:
        return None

    selected: list[str] = []
    for index, sentence in enumerate(parts):
        if is_slop(sentence):
            continue
        lower = sentence.lower()
        fact_signal = bool(re.search(r"[$%\d]", sentence)) or any(
            word in lower
            for word in (
                "because",
                " if ",
                " when ",
                "only",
                "must",
                "cannot",
                "can't",
                "generally",
                "current law",
                "risk",
                "tax",
                "bitcoin",
                "account",
                "app",
                "provider",
                "means",
            )
        )
        if index < 2 or fact_signal:
            selected.append(sentence)
    if not selected:
        selected = [parts[0]]

    # Keep the working notes readable. The full paragraph remains in reference.
    selected = selected[:5]
    return " ".join(selected)


def notes_for(content: str) -> list[str]:
    notes: list[str] = []
    for paragraph in re.split(r"\n\s*\n", content):
        compact = compact_paragraph(paragraph)
        if compact and compact not in notes:
            notes.append(compact)
    return notes


def sentence_case_heading(value: str) -> str:
    value = value.strip()
    if value.isupper():
        value = value.lower()
        value = value[:1].upper() + value[1:]
    return value


def suggested_opening(intro: str, title: str) -> str:
    intro_notes = notes_for(intro)
    if intro_notes:
        opener = intro_notes[0]
        if len(opener.split()) <= 70:
            return opener
    cleaned = title.rstrip(".")
    return f"In today's lesson, we're going to cover {cleaned[:1].lower() + cleaned[1:]}."


def draft_for(path: Path) -> tuple[str, str, str]:
    text = read(path)
    number = lesson_number(text, path)
    title = title_from(text, number)
    body = body_from(text)
    intro, sections = split_sections(body)

    standard: list[tuple[str, str]] = []
    special: dict[str, str] = {}
    for heading, content in sections:
        key = heading.upper().strip()
        if key in SPECIAL_SECTIONS:
            special[key] = content
        elif key in {"WHAT HAPPENS NEXT", "NEXT"}:
            # Positional transitions are editor notes, not spoken structure.
            special["SEQUENCE NOTE"] = content
        else:
            standard.append((heading, content))

    lines = [
        f"# {number} · {title}",
        "",
        "> **PRE-DICTATION WORKING DRAFT — not Austin dictation.**",
        "> Use this page to speak naturally. The bullets are a factual route through",
        "> the lesson, not lines that need to be read exactly. The old research prose",
        "> is retained at the bottom only so no calculation or caveat disappears.",
        "",
        "## Suggested opening",
        "",
        suggested_opening(intro, title),
        "",
        "## Teach it in this order",
        "",
    ]

    if not standard:
        standard = [("Main explanation", body)]

    for index, (heading, content) in enumerate(standard, 1):
        lines += [f"### {index}. {sentence_case_heading(heading)}", ""]
        section_notes = notes_for(content)
        if not section_notes:
            lines.append("- Explain this section in your own words from the reference below.")
        else:
            for note in section_notes:
                if note.startswith(("- ", "* ", "|", "> ", "1. ", "2. ", "3. ", "4. ", "5. ", "6. ")):
                    lines.append(note)
                else:
                    lines.append(f"- {note}")
        lines.append("")

    decision = notes_for(special.get("YOUR DECISION", ""))
    app = notes_for(special.get("PUT IT IN ORANGE PLAN", ""))
    finish = notes_for(special.get("YOU ARE DONE WHEN", special.get("HOMEWORK", "")))
    sequence = notes_for(special.get("SEQUENCE NOTE", ""))

    lines += ["## Close without manufacturing a payoff line", ""]
    if decision:
        lines.append("**Decision the learner needs to make:**")
        lines.extend(f"- {note}" for note in decision)
        lines.append("")
    if app:
        lines.append("**App or walkthrough handoff — do not read a click path twice:**")
        lines.extend(f"- {note}" for note in app)
        lines.append("")
    if finish:
        lines.append("**What should be true before they move on:**")
        lines.extend(f"- {note}" for note in finish)
        lines.append("")
    if sequence:
        lines.append("**Sequence note for the editor, not a scripted transition:**")
        lines.extend(f"- {note}" for note in sequence)
        lines.append("")

    lines += [
        "## Reference only — do not dictate this section",
        "",
        "<details>",
        "<summary>Open the researched draft when you need a number, caveat, or example</summary>",
        "",
        body,
        "",
        "</details>",
    ]
    return number, title, "\n".join(lines)


SCRIPT_1_3 = """TELEPROMPTER SCRIPT — segment 1.3
1.3 Read your starting retirement date and the confidence number you will run later
~4 min at 155 wpm · DICTATION-READY WORKING DRAFT — NOT YET AUSTIN DICTATION
APP VERIFIED: production main b0888802cbe3fd3769816c9f1352b424bd4bff1c
============================================================

In today's lesson, we're going to cover what the retirement age you saw at the end of onboarding actually means, because I don't want you to look at that number like Orange Plan already built your entire financial plan.

Onboarding only asked you for enough information to give you a useful starting point. It has your age, income, spending, a rough amount of Bitcoin and other assets, where most of those assets are held, and the Bitcoin growth model you selected.

It does not have every real account and holding yet. It also does not have all of your debts, future expenses, cost basis, Social Security, withdrawal strategy, tax planning, or the other decisions we're going to build throughout the course.

So the age is useful, but it is still based on rough information.

The way the calculation works is pretty simple. Orange Plan takes that one set of inputs and assumptions, projects the plan year by year, and checks different retirement ages. It finds the earliest age where that projection can fund your spending through the life-expectancy assumption in the plan.

I would not call this an average projection, because there are not hundreds or thousands of different market paths being averaged together during onboarding. It is one projection using the growth and inflation assumptions you selected.

That is why changing the Bitcoin growth model can move the age so much. A more aggressive model is going to grow the balance faster and move the estimate earlier. A more conservative model is going to move it later.

I still think this is useful because it quickly tells you whether retirement looks roughly close or far away, and it shows you how much the assumptions can change the answer. I just would not treat it like the final date yet.

You also are not going to see a confidence percentage during onboarding. That is intentional. Showing someone an 82% confidence number when the accounts and spending are still rough would make the result look much more precise than the information underneath it.

After the full plan is built, Orange Plan is going to run it through 1,000 different market paths. Those paths are going to include the real balances, spending, debts, taxes, contributions, future life events, withdrawal strategy, and everything else that has been added to the plan.

If 820 of those 1,000 paths fund the plan as written, the confidence number is 82%. That does not mean there is exactly an 18% chance that you go broke. It means 180 of the modeled paths would have required some kind of adjustment, like working longer, spending less, or changing another part of the plan.

Later, you are also going to choose the confidence target you want the retirement date to meet. The finished earliest retirement date is going to be the first age that clears that target, not just the first age where this one deterministic projection works.

For now, I would use the onboarding age as a starting point. Write down the age you saw, and then think about which rough input is most likely to change when we replace it with the real information. For most people that is going to be spending, the actual account balances, future expenses, or the growth assumptions.

Then use the Foundation walkthrough below this video to add your real accounts and current holdings and review the assumptions behind the estimate. We are not going to enter every other part of the plan or run the full confidence check in this module.
"""

MASTER_1_3 = """## 1.3 Read your starting retirement date and the confidence number you will run later
*`TEACH` · ~650 words · ~4 min*

**By the end of this lesson, you can:**

- Explain what the onboarding retirement age actually calculates
- Tell the deterministic starting estimate from the later 1,000-path confidence check
- Know why onboarding does not show a confidence percentage
- Know what Foundation replaces next

---

In today's lesson, we're going to cover what the retirement age shown at the end of onboarding actually means.

Onboarding uses rough inputs: age, income, spending, rough Bitcoin and other-asset balances, the broad tax home of the non-Bitcoin assets, and the selected Bitcoin growth model. It does not yet contain every real account, holding, debt, future expense, cost-basis record, Social Security input, tax decision, or retirement-income strategy.

### What the onboarding age calculates

The onboarding age comes from one deterministic projection. Orange Plan applies the selected assumptions, projects the plan year by year, checks different retirement ages, and finds the earliest age where that projection can fund spending through the life-expectancy assumption.

It is not an average of many paths. Onboarding does not run Monte Carlo, and it does not show a confidence percentage.

The estimate is useful because it gives the learner a quick starting point and makes the effect of the growth assumption visible. A more aggressive Bitcoin model generally moves the age earlier; a more conservative model generally moves it later.

### Why confidence waits

A percentage based on rough accounts and spending would create false precision. After the plan is built, Orange Plan runs the real plan through 1,000 different market paths. The confidence number is the share of those paths that funded the plan as written.

An 82% result means 820 of the 1,000 modeled paths funded the plan as entered. It does not mean there is a precisely measured 18% chance of going broke; the unsuccessful modeled paths may require an adjustment such as working longer, spending less, or changing another part of the plan.

The learner later chooses a confidence target. The finished earliest retirement date is the first age that clears that target, rather than merely the first age where the single deterministic projection works.

### Before the Foundation walkthrough

Write down the onboarding age and identify the rough input most likely to change when the real information is entered. Then use the Foundation walkthrough to add real accounts and current holdings and review the assumptions behind the estimate. Income, debt, life events, tax history, Social Security, retirement income, and the full confidence check stay in the modules that own them.
"""

LESSON_TEXT_1_3 = """# Read your starting retirement date and the confidence number you will run later

The age shown during onboarding comes from **one deterministic projection** using the rough inputs and growth model selected during setup. Orange Plan checks different retirement ages and finds the earliest age where that projection can fund spending through the life-expectancy assumption.

It is not an average of many paths, and onboarding does not run Monte Carlo or show a confidence percentage.

After the full plan is built, Orange Plan runs 1,000 market paths using the real accounts, spending, debts, taxes, future expenses, contributions, and retirement-income decisions. The confidence number is the share of those modeled paths that funded the plan as written.

An 82% result means 820 of 1,000 modeled paths funded the entered plan. It does not mean there is a precisely measured 18% chance of going broke; the other paths may require an adjustment.

## Before the walkthrough

Write down the onboarding age and the rough input most likely to change. Then open **Build Your Plan → Foundation** to replace the rough asset estimate with real accounts and current holdings and review the assumptions behind it.
"""


def replace_master_lesson(number: str, replacement: str) -> None:
    path = ROOT / "MASTER-COURSE.md"
    text = read(path)
    pattern = re.compile(
        rf"(?ms)^## {re.escape(number)} [^\n]*\n.*?(?=^## \d+\.\d+ |^# Unit \d+ |^<!-- ADVANCED-GATE:START -->|\Z)"
    )
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"Expected one MASTER-COURSE section for {number}; found {len(matches)}")
    match = matches[0]
    write(path, text[: match.start()] + replacement.rstrip() + "\n\n" + text[match.end() :])


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    # Correct and simplify the next chronological lesson in the canonical layers.
    write(SCRIPTS / "01-3_read-your-retirement-date-and-confidence.md", SCRIPT_1_3)
    replace_master_lesson("1.3", MASTER_1_3)
    write(ROOT / "lesson-text/01-3_read-your-retirement-date-and-confidence.md", LESSON_TEXT_1_3)

    if DRAFTS.exists():
        shutil.rmtree(DRAFTS)
    DRAFTS.mkdir(parents=True)

    rows: list[tuple[str, str, str, str]] = []
    for path in sorted([*SCRIPTS.glob("*.md"), *(SCRIPTS / "advanced").glob("*.md")]):
        upper = path.name.upper()
        if "WALKTHROUGH" in upper or "DEMO" in upper or path.name == "VOICE-GUIDE.md":
            continue
        text = read(path)
        number = lesson_number(text, path)
        title = title_from(text, number)
        if number in DICTATED_NUMBERS or "AUSTIN DICTATION" in text[:1200]:
            rows.append((number, title, "Austin dictation", str(path.relative_to(ROOT))))
            continue

        number, title, draft = draft_for(path)
        relative = path.relative_to(SCRIPTS)
        draft_path = DRAFTS / relative
        write(draft_path, draft)
        status = "full working draft" if number == "1.3" else "teaching brief + research reference"
        rows.append((number, title, status, str(draft_path.relative_to(ROOT))))

    def sort_key(row: tuple[str, str, str, str]) -> tuple[int, int, int]:
        number = row[0]
        advanced = 1 if number.startswith("A") else 0
        clean = number.lstrip("A")
        major, minor = clean.split(".")
        return advanced, int(major), int(minor)

    rows.sort(key=sort_key)
    order = [
        "# Dictation prep order",
        "",
        "Use the files in `dictation-drafts/` for every lesson that Austin has not yet dictated.",
        "They are intentionally working notes rather than polished teleprompter copy. The old",
        "research prose is collapsed at the bottom of each file so facts and caveats remain available.",
        "",
        "When Austin dictates a lesson, replace the canonical file in `scripts/`, update the master",
        "and student text, and mark the prep file complete or remove it.",
        "",
        "| Lesson | Status | Work from |",
        "|---|---|---|",
    ]
    for number, title, status, path in rows:
        order.append(f"| **{number}** · {title} | {status} | `{path}` |")
    write(ROOT / "DICTATION-PREP-ORDER.md", "\n".join(order))

    policy = """# Pre-dictation draft policy

## Why this layer exists

A researched lesson is not automatically an Austin script. The previous workflow labelled editor-shaped prose as spoken-ready, which made Austin spend dictation time fighting the writing structure instead of improving the teaching.

## Source of truth

- `scripts/` contains Austin dictation where it exists and the protected research script where it does not.
- `dictation-drafts/` is the working surface Austin should use before he dictates a non-dictated lesson.
- `MASTER-COURSE.md`, `MASTER-ADVANCED.md`, and `lesson-text/` preserve the full reference, calculations, source qualifications, and learner-facing text.

## What a prep file should do

A prep file gives Austin a natural opener, a factual teaching order, the worked examples and caveats that cannot be lost, and a clear app/finish handoff. It should not manufacture a hook, payoff line, three-part slogan, or identical `Your decision / Put it in / You are done when` spoken structure.

## After dictation

Austin's recorded words become the authority. Clean transcription errors and verify math or app behavior, but do not compress his useful repetition or replace his planning judgment. App clicks remain in the walkthrough unless Austin deliberately wants to mention the location in the teaching lesson.
"""
    write(ROOT / "PRE-DICTATION-DRAFT-POLICY.md", policy)

    # Regenerate the layers affected by the factual and canonical 1.3 rewrite.
    for command in (
        ["python3", "tools/build-module-gates.py"],
        ["python3", "tools/build-scripts.py"],
        ["python3", "tools/build-scripts.py", "--advanced"],
        ["python3", "tools/split-modules.py"],
        ["python3", "tools/split-modules.py", "--advanced"],
        ["python3", "tools/build-onefile.py"],
        ["python3", "tools/build-circle-structure.py"],
        ["python3", "tools/build-dictation-order.py"],
        ["python3", "tools/build-film-order.py"],
        ["python3", "tools/build-shoot-list.py"],
        ["python3", "tools/build-production-checklist.py"],
        ["python3", "tools/course-metrics.py"],
    ):
        run(command)


if __name__ == "__main__":
    main()
