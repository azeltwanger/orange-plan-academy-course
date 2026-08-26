#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from config import (
    ADVANCED_FILENAMES,
    ADVANCED_ORDER,
    APP_COMMIT,
    CORE_FILENAMES,
    DICTATED,
    MODULES,
    OPTIONAL,
    PROFESSIONAL_GATES,
    VISUALS,
)
from core_a import CORE as CORE_A
from core_b import CORE as CORE_B
from core_c import CORE as CORE_C
from core_d import CORE as CORE_D
from core_e import CORE as CORE_E
from advanced_a import ADVANCED as ADV_A
from advanced_b import ADVANCED as ADV_B
from advanced_c import ADVANCED as ADV_C
from advanced_d import ADVANCED as ADV_D
from walkthroughs_a import WALKTHROUGHS as WALKS_A
from walkthroughs_b import WALKTHROUGHS as WALKS_B
from walkthroughs_c import WALKTHROUGHS as WALKS_C
from walkthroughs_d import WALKTHROUGHS as WALKS_D

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
ADV_SCRIPTS = SCRIPTS / "advanced"
LESSON_TEXT = ROOT / "lesson-text"
ADV_LESSON_TEXT = LESSON_TEXT / "advanced"
MODULE_DIR = ROOT / "modules"
ADV_MODULE_DIR = MODULE_DIR / "advanced"

CORE = {}
for part in (CORE_A, CORE_B, CORE_C, CORE_D, CORE_E):
    CORE.update(part)
ADVANCED = {}
for part in (ADV_A, ADV_B, ADV_C, ADV_D):
    ADVANCED.update(part)
WALKS = {}
for part in (WALKS_A, WALKS_B, WALKS_C, WALKS_D):
    WALKS.update(part)

DICTATED_TITLES = {
    "0.1": "How to use this course",
    "1.1": "What to gather before you build the plan",
    "1.2": "The three layers of a plan, and setting your assumptions",
    "2.2": "Size your cash reserve in months of spending",
}

DICTATED_PATHS = {
    "0.1": SCRIPTS / "00-1_how-to-use-this-course.md",
    "1.1": SCRIPTS / "01-1_what-to-gather-before-you-build-the-plan.md",
    "1.2": SCRIPTS / "01-2_set-your-growth-and-inflation-assumption.md",
    "2.2": SCRIPTS / "02-2_size-your-cash-reserve-in-months-of-spen.md",
}


def body_from_script(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    divider = "=" * 60
    if divider not in text:
        return text.strip() + "\n"
    return text.split(divider, 1)[1].strip() + "\n"


def replace_close(body: str, replacement: str) -> str:
    marker = re.search(r"\n== YOUR DECISION ==\n", body)
    if not marker:
        return body.rstrip() + "\n\n" + replacement.strip() + "\n"
    return body[: marker.start()].rstrip() + "\n\n" + replacement.strip() + "\n"


def clean_dictated(number: str) -> str:
    body = body_from_script(DICTATED_PATHS[number])

    if number == "0.1":
        body = re.sub(
            r"^>>> I CHANGED TWO THINGS.*?Nothing else in your dictation was touched\.\s*",
            "",
            body,
            flags=re.S,
        )
        body = body.split("\n============================================================\nNOT YET DICTATED", 1)[0].rstrip()
        body = body.replace(
            "5. Then debt, where every debt you have gets a job and you set the level of debt you won't go past.\n"
            "6. Then your investment plan, which is your allocation and where every next dollar goes.",
            "5. Then your investment plan, which is your allocation and where every next dollar goes.\n"
            "6. Then debt, where every debt gets a job and the extra-payment decision feeds back into that contribution plan.",
        )
        final_line = "Alright, and with that, thanks for being here, and I'll see you in the first lesson."
        body = body.replace(final_line, "").rstrip()
        body += r"""

== WHO THIS COURSE IS BUILT FOR ==

One thing to get out of the way up front, so I only have to say it once.

The tax, estate, insurance, Social Security, Medicare, and retirement-account sections use US rules and examples. Those rules can change, and the legal and tax details are not portable from one country or state to another.

The rest of the framework travels much better: cash flow, the Reserve, allocation, debt risk, custody, retirement math, scenarios, and the review process.

Orange Plan now supports an international planning profile for the basic plan data, but the detailed tax calculations and the professional material in this course are still centered on the United States. If you live outside the US, build the current position, cash flow, allocation, retirement projection, and custody plan, then take the tax and estate decisions to qualified professionals in your country.

The way of thinking can still be useful. The local rules have to be mapped correctly.

Alright, and with that, thanks for being here, and I'll see you in the first lesson.
"""

    elif number == "1.1":
        body = body.replace(
            "Debt enters every debt with its current balance, rate, and payment.\n\n"
            "Tax imports historical transactions and reconstructs cost basis.",
            "Allocation assigns the major accounts to Reserve, Bridge, or Legacy, sets the target mix, and builds the contribution plan from the surplus.\n\n"
            "Debt enters every debt with its current balance, rate, and payment, decides the extra-payment amount, and then returns that amount to the contribution waterfall.\n\n"
            "Tax imports historical transactions and reconstructs cost basis.",
        )
        body = replace_close(
            body,
            "You do not need to enter any of this yet. Put the statements, exports, employer information, and rough future-event list in one place. In the Foundation walkthrough, we'll use the personal details, account list, and current holdings first. The rest stays in the folder until the module that teaches the decision and owns the data.",
        )

    elif number == "1.2":
        body = replace_close(
            body,
            "Before the walkthrough, choose the growth model and inflation assumption you would actually defend, not the pair that produces the earliest date. In the Foundation walkthrough, I'll show you where to review what onboarding selected, where the custom assumptions live, and how to save the baseline once without repeating the click path in this lesson.",
        )

    elif number == "2.2":
        body = replace_close(
            body,
            "Before the walkthrough, choose the number of months that fits your income stability, dependents, fixed costs, and comfort with selling during a drawdown. In the walkthrough, I'll show you where to enter the bare-bones monthly amount, select the Reserve basis and months, and choose the monthly build cap. Orange Plan calculates the target from those inputs and shows the gap; you do not type the target multiplication manually.",
        )

    return body.strip() + "\n"


def count_words(body: str) -> int:
    lines = [line for line in body.splitlines() if not line.startswith("🎬 VISUAL")]
    return len(re.findall(r"\b[\w’'-]+\b", "\n".join(lines)))


def teach_header(number: str, title: str, body: str, source: str, dictated: bool = False) -> str:
    words = count_words(body)
    minutes = words / 155
    if dictated:
        status = "AUSTIN DICTATION — cleaned only for current app flow, factual corrections, and walkthrough separation"
    else:
        status = "PRE-DICTATION FILMING DRAFT — rebuilt from Austin's decks, dictation, research, and current app"
    return (
        f"TELEPROMPTER SCRIPT — segment {number}\n"
        f"{number} {title}\n"
        f"{words:,} words · ~{minutes:.1f} min at 155 wpm · {status}\n"
        f"SOURCE: {source}\n"
        + "=" * 60
        + "\n\n"
    )


def advanced_header(number: str, title: str, body: str, gate: str) -> str:
    words = count_words(body)
    minutes = words / 155
    return (
        f"ADVANCED TELEPROMPTER SCRIPT — segment {number}\n"
        f"{number} {title}\n"
        f"{words:,} words · ~{minutes:.1f} min at 155 wpm · PRE-DICTATION FILMING DRAFT\n"
        f"PUBLICATION GATE: {gate}\n"
        + "=" * 60
        + "\n\n"
    )


def to_markdown(body: str, include_visuals: bool = True) -> str:
    out = []
    for line in body.strip().splitlines():
        m = re.fullmatch(r"== (.+) ==", line.strip())
        if m:
            out.append(f"### {m.group(1).title()}")
        elif line.startswith("🎬 VISUAL —"):
            if include_visuals:
                out.append(f"> **Visual:** {line.split('—', 1)[1].strip()}")
        else:
            out.append(line)
    return "\n".join(out).strip() + "\n"


def strip_first_heading(text: str) -> str:
    lines = text.strip().splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return "\n".join(lines).lstrip()


def prepare_dirs() -> None:
    for directory in (SCRIPTS, ADV_SCRIPTS, LESSON_TEXT, ADV_LESSON_TEXT, MODULE_DIR, ADV_MODULE_DIR):
        directory.mkdir(parents=True, exist_ok=True)

    keep_script_docs = {"README.md", "VOICE-GUIDE.md"}
    for path in SCRIPTS.glob("*.md"):
        if path.name not in keep_script_docs:
            path.unlink()
    for path in ADV_SCRIPTS.glob("*.md"):
        path.unlink()
    for path in LESSON_TEXT.glob("*.md"):
        path.unlink()
    if ADV_LESSON_TEXT.exists():
        for path in ADV_LESSON_TEXT.glob("*.md"):
            path.unlink()
    for path in MODULE_DIR.glob("*.md"):
        path.unlink()
    if ADV_MODULE_DIR.exists():
        for path in ADV_MODULE_DIR.glob("*.md"):
            path.unlink()


def build_core_records() -> dict[str, dict]:
    records = {}
    for number in DICTATED:
        records[number] = {
            "title": DICTATED_TITLES[number],
            "source": "Austin dictation; current course order and current-app handoffs applied in the filming rebuild",
            "body": clean_dictated(number),
            "dictated": True,
        }
    for number, record in CORE.items():
        body = record["body"].strip() + "\n"
        if number == "6.3":
            body = body.replace(
                "In the walkthrough, we'll run the first full confidence check, choose the target, save the retirement spending plan, and show where the annual guardrail and refill decision will be made in later years.",
                "Module 9 runs the first full confidence check after every Build Your Plan area is complete. This module teaches the rule and shows where the operating controls live without treating an unfinished plan as the final baseline.",
            )
        records[number] = {**record, "body": body, "dictated": False}
    return records


def write_scripts(core_records: dict[str, dict]) -> None:
    for module in MODULES:
        for number in module["lessons"]:
            rec = core_records[number]
            path = SCRIPTS / CORE_FILENAMES[number]
            path.write_text(
                teach_header(number, rec["title"], rec["body"], rec["source"], rec["dictated"])
                + rec["body"].strip()
                + "\n",
                encoding="utf-8",
            )
        for number in module["captures"]:
            path = SCRIPTS / CORE_FILENAMES[number]
            path.write_text(WALKS[number]["body"].strip() + "\n", encoding="utf-8")

    for number in ADVANCED_ORDER:
        rec = ADVANCED[number]
        path = ADV_SCRIPTS / ADVANCED_FILENAMES[number]
        path.write_text(
            advanced_header(number, rec["title"], rec["body"], rec["gate"])
            + rec["body"].strip()
            + "\n",
            encoding="utf-8",
        )


def master_intro() -> str:
    return f"""# Orange Plan Academy — filming master

**Editorial rebuild completed against Orange Plan main `{APP_COMMIT}`.**

This master uses the following authority order:

1. Austin's dictation for voice, examples, and planning judgment.
2. Austin's slide decks for teaching sequence and required visuals.
3. Current Orange Plan production for fields, calculations, and walkthrough mechanics.
4. Primary-source research for factual accuracy.
5. Older generated scripts only as disposable reference.

A script labeled **AUSTIN DICTATION** preserves Austin's words with only factual, app-flow, or walkthrough-separation edits. A script labeled **PRE-DICTATION FILMING DRAFT** is editorially prepared to make dictation and filming fast, but it does not become Austin-authored merely because it passes automated checks.

The teach lesson explains the concept and helps the student make a decision. The walkthrough performs the clicks, shows what the app calculates, and returns to Build Your Plan. The app's Build Your Plan panel currently lists Debt before Allocation; the course intentionally teaches **Week 3 Allocation + Next-Dollar** and **Week 4 Debt**, then returns the final extra-debt amount to the contribution waterfall.

The first full 1,000-path confidence result is saved in Module 9, after the full baseline is intentionally complete.

## Professional publication gates

- {PROFESSIONAL_GATES['tax']}
- {PROFESSIONAL_GATES['custody']}
- {PROFESSIONAL_GATES['insurance']}
- {PROFESSIONAL_GATES['estate']}

---
"""


def generate_master(core_records: dict[str, dict]) -> str:
    parts = [master_intro()]
    for unit, module in enumerate(MODULES, start=1):
        parts.append(f"\n# Unit {unit} · Module {module['number']} — {module['title']}\n\n")
        parts.append(f"*{module['blurb']}*\n\n")
        parts.append(f"**You will build:** {module['build']}\n\n")
        for number in module["lessons"]:
            rec = core_records[number]
            words = count_words(rec["body"])
            status = "AUSTIN DICTATION" if rec["dictated"] else "PRE-DICTATION FILMING DRAFT"
            optional = " · OPTIONAL" if number in OPTIONAL else ""
            parts.append(f"## {number} {rec['title']}\n\n")
            parts.append(f"*`TEACH` · ~{words/155:.1f} min · {status}{optional}*\n\n")
            parts.append(to_markdown(rec["body"], include_visuals=True))
            parts.append("\n---\n\n")
        for number in module["captures"]:
            parts.append(f"## {number} {WALKS[number]['title']}\n\n")
            parts.append("*`WALKTHROUGH / DEMO` · narrate from the DO / SEE / ⚠ sheet*\n\n")
            parts.append(strip_first_heading(WALKS[number]["body"]))
            parts.append("\n---\n\n")
        parts.append("## Module checkpoint\n\n")
        for item in module["checkpoint"]:
            parts.append(f"- [ ] {item}\n")
        parts.append("\n")
    return "".join(parts).rstrip() + "\n"


def generate_advanced_master() -> str:
    groups: dict[int, list[str]] = {}
    for number in ADVANCED_ORDER:
        module = int(re.match(r"A(\d+)\.", number).group(1))
        groups.setdefault(module, []).append(number)
    parts = [
        "# Orange Plan Academy — Advanced Library\n\n",
        "Every lesson is optional and gated by the condition or professional review stated at the top. These drafts were rebuilt to extend the core course rather than create a competing course sequence.\n\n",
    ]
    title_by_module = {m["number"]: m["title"] for m in MODULES}
    for module, numbers in groups.items():
        parts.append(f"# Advanced Module {module} — {title_by_module.get(module, 'Advanced')}\n\n")
        for number in numbers:
            rec = ADVANCED[number]
            parts.append(f"## {number} {rec['title']}\n\n")
            parts.append(f"> **Gate.** {rec['gate']}\n\n")
            parts.append(to_markdown(rec["body"], include_visuals=True))
            parts.append("\n---\n\n")
    return "".join(parts).rstrip() + "\n"


def generate_lesson_text(core_records: dict[str, dict]) -> None:
    module_by_lesson = {}
    for module in MODULES:
        for number in module["lessons"] + module["captures"]:
            module_by_lesson[number] = module

    for number, filename in CORE_FILENAMES.items():
        if number in core_records:
            rec = core_records[number]
            module = module_by_lesson[number]
            text = [f"# {number} · {rec['title']}\n\n"]
            if number in OPTIONAL:
                text.append("**Optional.** Complete this lesson only when an education goal applies.\n\n")
            text.append(to_markdown(rec["body"], include_visuals=False))
            text.append("\n## Apply it\n\n")
            next_capture = module["captures"][0] if module["captures"] else None
            if next_capture:
                text.append(f"Use walkthrough {next_capture} to enter the decision and confirm what Orange Plan calculated.\n\n")
            text.append("## Module checkpoint\n\n")
            for item in module["checkpoint"]:
                text.append(f"- [ ] {item}\n")
            (LESSON_TEXT / filename.lower().replace("walkthrough_", "walkthrough-")).write_text(
                "".join(text).rstrip() + "\n", encoding="utf-8"
            )
        else:
            module = module_by_lesson[number]
            text = (
                f"# {number} · {WALKS[number]['title']}\n\n"
                "Follow the walkthrough video and the matching Build Your Plan area. The implementation is complete when the real data and applied decision exist in Orange Plan.\n\n"
                "## Module checkpoint\n\n"
                + "\n".join(f"- [ ] {item}" for item in module["checkpoint"])
                + "\n"
            )
            (LESSON_TEXT / filename.lower().replace("walkthrough_", "walkthrough-").replace("demo_", "demo-")).write_text(text, encoding="utf-8")

    for number in ADVANCED_ORDER:
        rec = ADVANCED[number]
        text = (
            f"# {number} · {rec['title']}\n\n"
            f"**Publication gate:** {rec['gate']}\n\n"
            + to_markdown(rec["body"], include_visuals=False)
        )
        (ADV_LESSON_TEXT / ADVANCED_FILENAMES[number]).write_text(text, encoding="utf-8")


def generate_module_files(master: str, advanced_master: str) -> None:
    sections = re.split(r"(?=^# Unit \d+ · Module )", master, flags=re.M)
    for section in sections:
        if not section.startswith("# Unit"):
            continue
        m = re.match(r"# Unit \d+ · Module (\d+) — (.+)", section)
        slug = re.sub(r"[^a-z0-9]+", "-", m.group(2).lower()).strip("-")
        (MODULE_DIR / f"{int(m.group(1)):02d}-{slug}.md").write_text(section.strip() + "\n", encoding="utf-8")

    sections = re.split(r"(?=^# Advanced Module )", advanced_master, flags=re.M)
    for section in sections:
        if not section.startswith("# Advanced"):
            continue
        m = re.match(r"# Advanced Module (\d+) — (.+)", section)
        slug = re.sub(r"[^a-z0-9]+", "-", m.group(2).lower()).strip("-")
        (ADV_MODULE_DIR / f"A{int(m.group(1)):02d}-{slug}.md").write_text(section.strip() + "\n", encoding="utf-8")


def generate_onefile(core_records: dict[str, dict]) -> str:
    parts = ["# Orange Plan Academy — every production script in course order\n\n"]
    teach_count = sum(len(m["lessons"]) for m in MODULES)
    capture_count = sum(len(m["captures"]) for m in MODULES)
    parts.append(f"{teach_count} teach lessons · {capture_count} walkthroughs / demos.\n\n")
    for module in MODULES:
        parts.append(f"# Module {module['number']} — {module['title']}\n\n")
        for number in module["lessons"]:
            parts.append((SCRIPTS / CORE_FILENAMES[number]).read_text(encoding="utf-8").rstrip() + "\n\n---\n\n")
        for number in module["captures"]:
            parts.append((SCRIPTS / CORE_FILENAMES[number]).read_text(encoding="utf-8").rstrip() + "\n\n---\n\n")
    return "".join(parts).rstrip() + "\n"


def generate_docs(core_records: dict[str, dict]) -> None:
    module_rows = []
    dictation_rows = []
    film_rows = []
    for module in MODULES:
        module_rows.append(f"## Module {module['number']} — {module['title']}\n\n**You will build:** {module['build']}\n\n")
        module_rows.extend(f"- [ ] {item}\n" for item in module["checkpoint"])
        module_rows.append("\n")
        for number in module["lessons"]:
            rec = core_records[number]
            status = "Austin dictation integrated" if rec["dictated"] else "Pre-dictation filming draft ready"
            dictation_rows.append(f"- **{number} · {rec['title']}** — {status}\n")
            film_rows.append(f"- 🎙 **{number} · {rec['title']}**\n")
        for number in module["captures"]:
            film_rows.append(f"- 🖥 **{number} · {WALKS[number]['title']}**\n")

    (ROOT / "MODULE-CHECKPOINTS.md").write_text(
        "# Module checkpoints\n\n" + "".join(module_rows), encoding="utf-8"
    )

    (ROOT / "DICTATION-ORDER.md").write_text(
        "# Core-course dictation order\n\n"
        "Work chronologically. The generated prose is a clean starting draft, not a claim that Austin already said it. Dictation replaces the draft while factual and app-parity safeguards remain.\n\n"
        + "".join(dictation_rows),
        encoding="utf-8",
    )

    (ROOT / "FILM-ORDER.md").write_text(
        "# Film order\n\n"
        "Film in course order. Teach lessons make the decision; the walkthrough immediately implements the module before the next module begins.\n\n"
        + "".join(film_rows),
        encoding="utf-8",
    )

    visual_lines = [
        "# Visual and screen-capture map\n\n",
        "Recreate the deck concepts in the current Orange Plan cream / charcoal / orange visual system. Do not screen-capture the old black deck as the finished asset. The old deck supplies the concept and sequence.\n\n",
        f"App screens were rebuilt against Orange Plan main `{APP_COMMIT}`. Recheck exact labels immediately before screen recording because the production app can move after this commit.\n\n",
    ]
    for number, visuals in VISUALS.items():
        title = core_records[number]["title"]
        visual_lines.append(f"## {number} · {title}\n\n")
        visual_lines.extend(f"- {item}\n" for item in visuals)
        visual_lines.append("\n")
    visual_lines.append("## Screen captures\n\n")
    for module in MODULES:
        for number in module["captures"]:
            visual_lines.append(f"- **{number}** — {WALKS[number]['title']}\n")
    (ROOT / "SCREEN-SHOOT-LIST.md").write_text("".join(visual_lines), encoding="utf-8")

    advanced_rows = []
    for number in ADVANCED_ORDER:
        rec = ADVANCED[number]
        advanced_rows.append(f"- **{number} · {rec['title']}** — Pre-dictation draft ready. Gate: {rec['gate']}\n")
    (ROOT / "ADVANCED-DICTATION-ORDER.md").write_text(
        "# Advanced Library dictation order\n\n"
        "The numbering now follows the restored core order: Module 3 is Allocation; Module 4 is Debt. Every lesson is optional.\n\n"
        + "".join(advanced_rows),
        encoding="utf-8",
    )

    circle = ["# Circle structure — final course order\n\n"]
    for module in MODULES:
        circle.append(f"## Module {module['number']} — {module['title']}\n\n")
        circle.append(f"**What you will build:** {module['build']}\n\n")
        circle.append("### Lessons\n\n")
        for number in module["lessons"]:
            rec = core_records[number]
            optional = " · OPTIONAL" if number in OPTIONAL else ""
            circle.append(f"- {number} · {rec['title']}{optional}\n")
        for number in module["captures"]:
            circle.append(f"- {number} · {WALKS[number]['title']}\n")
        circle.append("\n### Checkpoint\n\n")
        circle.extend(f"- [ ] {item}\n" for item in module["checkpoint"])
        circle.append("\n")
    (ROOT / "CIRCLE-STRUCTURE.md").write_text("".join(circle), encoding="utf-8")

    (ROOT / "SLIDE-DECK-AUTHORITY.md").write_text(
        "# Slide-deck and app authority\n\n"
        "## Source hierarchy\n\n"
        "1. Austin's dictation — voice, examples, recommendations, and judgment.\n"
        "2. Austin's slide decks — teaching sequence, decisions, and visual logic.\n"
        "3. Current production app — fields, calculations, labels, and walkthrough mechanics.\n"
        "4. Primary-source research — factual verification.\n"
        "5. Older generated scripts — disposable reference only.\n\n"
        "## Restored course order\n\n"
        "Foundation → Cash Flow + Reserve → Allocation + Next-Dollar → Debt → Tax → Retirement Income → Custody → Estate + Inheritance → Finish, Test + Maintain.\n\n"
        "Build Your Plan remains the implementation roadmap even when its card order differs. Module 3 saves a provisional extra-debt claim; Module 4 finalizes it and returns to the waterfall.\n\n"
        "Teach lessons explain concepts and decisions. Walkthroughs own click paths, data entry, app calculations, saves, and verification.\n",
        encoding="utf-8",
    )

    (ROOT / "AUSTIN-AUTHORITY.md").write_text(
        "# Austin authority\n\n"
        "Austin's dictation controls spoken voice, examples, and planning judgment. Factual corrections, current-app corrections, and safe professional boundaries may be applied without disguising new planning opinions as Austin's words.\n\n"
        "The four currently dictated core scripts are 0.1, 1.1, 1.2, and 2.2. Every other core and advanced teach script is explicitly labeled as a pre-dictation filming draft.\n\n"
        "The slide decks control the teaching sequence. The current production app controls the walkthrough. Build Your Plan controls whether implementation is actually complete.\n\n"
        "No universal college split, contribution priority exception, loan amount, Bitcoin allocation, insurance amount, trust clause, or custody-key split may be invented and attributed to Austin.\n",
        encoding="utf-8",
    )

    status = f"""# Finalization status

## Editorial status

- The full core course has been rebuilt in the restored order: Week 2 Cash Flow + Reserve, Week 3 Allocation + Next-Dollar, Week 4 Debt.
- All 28 core teach lessons have either Austin dictation or a deck-anchored pre-dictation filming draft.
- All 10 core walkthroughs / demos have a current implementation sheet.
- All 14 Advanced lessons have been renumbered, rewritten as pre-dictation drafts, and attached to the correct core module.
- Slide concepts are mapped in `SCREEN-SHOOT-LIST.md` and appear as visual cues inside the teach scripts.
- The first full confidence run now happens in Module 9 after the complete plan is built.

## App reference

Course walkthroughs were reconciled against Orange Plan main `{APP_COMMIT}`. Exact on-screen labels must be rechecked immediately before each screen recording because production can continue changing.

## What remains before publication

- Austin reads / dictates the scripts in chronological order. The drafts are designed to make that pass fast; they are not falsely labeled as his words.
- Targeted professional signoffs remain for tax, custody, insurance, and estate material.
- The hardware-wallet demo requires the exact device and firmware verification receipt.
- Current-year figures, laws, limits, premiums, and provider terms are checked at recording or publication time.

There are no remaining structural course-flow blockers.
"""
    (ROOT / "FINALIZATION-STATUS.md").write_text(status, encoding="utf-8")
    (ROOT / "PRE-DICTATION-RESET-STATUS.md").write_text(
        "# Pre-dictation reset — complete\n\n"
        "The generated architecture was removed and the course was rebuilt from Austin's decks, current app, dictation, and research. Non-dictated lessons are now clearly labeled pre-dictation filming drafts.\n\n"
        "The reset restored Module 3 Allocation and Module 4 Debt, rebuilt future-event and college teaching, added the missing surplus-routing system, separated teach lessons from walkthrough clicks, and deferred the first full confidence run until the completed plan.\n",
        encoding="utf-8",
    )
    (ROOT / "DICTATION-PICKUPS.md").write_text(
        "# Dictation pickups\n\n"
        "There are no structural blockers. Dictate chronologically and change any planning judgment that does not match what you would actually say.\n\n"
        "Pay extra attention while dictating to: the exact college commitment examples; contribution-waterfall exceptions; personal tax and healthcare examples; the amount of custody complexity you personally prefer; and any estate or insurance opinion that should be framed as your experience rather than a universal rule.\n",
        encoding="utf-8",
    )
    (ROOT / "AUTHORITY-FLAGS.md").write_text(
        "# Current authority and publication flags\n\n"
        "## No Austin-authorship blockers\n\n"
        "Every non-dictated lesson is labeled honestly and can be corrected during chronological dictation.\n\n"
        "## External publication gates\n\n"
        + "\n".join(f"- {v}" for v in PROFESSIONAL_GATES.values())
        + "\n\n## Recording-time verification\n\n"
        "- Recheck exact app labels against production.\n"
        "- Recheck current tax law, account limits, healthcare pricing, insurance contracts, estate thresholds, provider terms, and device firmware.\n"
        "- Never record or store a real seed, key, passphrase, PIN, or exact recovery location.\n",
        encoding="utf-8",
    )
    (ROOT / "AUSTIN-VOICE-PASS-REPORT.md").write_text(
        "# Voice and structure rebuild report\n\n"
        "The previous pass removed some obvious phrases but preserved the generated copywriting architecture. This rebuild changed the architecture itself.\n\n"
        "Non-dictated scripts now follow the deck's decision flow, explain the concept before implementation, use practical examples, and end with a natural walkthrough handoff instead of repeating YOUR DECISION / PUT IT IN ORANGE PLAN / YOU ARE DONE WHEN.\n\n"
        "The drafts use Austin's known patterns — plain definitions, why the input matters, a concrete example, personal judgment marked as judgment, and useful repetition — without claiming that generated prose is dictation.\n",
        encoding="utf-8",
    )

    production = f"""# Production checklist

## Before filming any lesson

- [ ] Read the script status line: Austin dictation or pre-dictation filming draft.
- [ ] Open the current production app when the lesson names an app behavior.
- [ ] Confirm the visual cue in `SCREEN-SHOOT-LIST.md`.
- [ ] Remove current figures from spoken video when they belong in lesson text or the app.
- [ ] Confirm no click path is duplicated in the teach lesson.

## Professional gates

- [ ] {PROFESSIONAL_GATES['tax']}
- [ ] {PROFESSIONAL_GATES['custody']}
- [ ] {PROFESSIONAL_GATES['insurance']}
- [ ] {PROFESSIONAL_GATES['estate']}

## Course flow checks

- [ ] Week 2 is Cash Flow + Reserve.
- [ ] Week 3 is Allocation + Next-Dollar.
- [ ] Week 4 is Debt, followed by a return to Cash Flow Routing.
- [ ] Module 1 enters only Foundation data.
- [ ] Module 5 owns historical transactions and cost basis.
- [ ] Module 9 runs the first full confidence check.

## App reference

- [ ] Recheck labels after `{APP_COMMIT}` before screen capture.
"""
    (ROOT / "PRODUCTION-CHECKLIST.md").write_text(production, encoding="utf-8")
    (ROOT / "FILMING-CHECKLIST.md").write_text(production, encoding="utf-8")

    (ROOT / "HANDOFF.md").write_text(
        "# Course handoff\n\n"
        "Start with `FINALIZATION-STATUS.md`, then use `DICTATION-ORDER.md` for A-roll and `FILM-ORDER.md` / `SCREEN-SHOOT-LIST.md` for production. The canonical spoken files are in `scripts/`; the master and student text are synchronized from those scripts by the filming rebuild.\n\n"
        "The course is structurally ready. Austin can dictate chronologically and replace draft wording without re-solving module flow, app ownership, or visual coverage.\n",
        encoding="utf-8",
    )

    (ROOT / "COURSE-REBUILD-REPORT.md").write_text(
        f"# Course rebuild report — 2026-08-26\n\n"
        f"**App reference:** `{APP_COMMIT}`\n\n"
        "## Corrected architecture\n\n"
        "- Restored Week 2 Cash Flow + Reserve, Week 3 Allocation + Next-Dollar, Week 4 Debt.\n"
        "- Kept Build Your Plan as the implementation roadmap without forcing its card order to become the teaching order.\n"
        "- Rebuilt every non-dictated core lesson before Austin's next dictation pass.\n"
        "- Removed the repeated copywriting close and duplicated app-click instructions.\n"
        "- Rebuilt future-event planning around expected cash-flow changes and Life events.\n"
        "- Rebuilt college around the parent commitment, realistic cost, source mix, current app Education target, Bitcoin-versus-529 nuance, and a non-mandatory one-third framework.\n"
        "- Restored the missing contribution-waterfall reasoning and implementation.\n"
        "- Corrected Reserve target ownership: the app calculates basis × months.\n"
        "- Preserved deterministic onboarding and delayed the first full confidence result until Module 9.\n"
        "- Rebuilt and renumbered all Advanced lessons.\n\n"
        "## Known app/course mismatch handled deliberately\n\n"
        "Build Your Plan lists Debt before Allocation. The course teaches Allocation first because that is the deck and teaching flow. The Module 3 walkthrough saves the contribution plan with the current extra-debt claim; Module 4 finalizes debt and returns to Routing.\n\n"
        "## Publication safeguards\n\n"
        + "\n".join(f"- {v}" for v in PROFESSIONAL_GATES.values())
        + "\n",
        encoding="utf-8",
    )

    (ROOT / "README.md").write_text(
        "# Orange Plan Academy course repository\n\n"
        "The canonical production files are in `scripts/`. Start with `FINALIZATION-STATUS.md`.\n\n"
        "## Current course order\n\n"
        "Start Here → Foundation → Cash Flow + Reserve → Allocation + Next-Dollar → Debt → Tax → Retirement Income → Custody → Estate + Inheritance → Finish, Test + Maintain.\n\n"
        "## Production files\n\n"
        "- `DICTATION-ORDER.md` — chronological A-roll.\n"
        "- `FILM-ORDER.md` — full filming order.\n"
        "- `SCREEN-SHOOT-LIST.md` — slide concepts and app captures.\n"
        "- `PRODUCTION-CHECKLIST.md` — gates and preflight.\n"
        "- `MASTER-COURSE.md` / `MASTER-ADVANCED.md` — synchronized editorial masters.\n"
        "- `lesson-text/` — synchronized student text.\n\n"
        "Scripts labeled PRE-DICTATION FILMING DRAFT are ready for Austin's chronological dictation pass but are not represented as existing Austin speech.\n",
        encoding="utf-8",
    )


def remove_obsolete() -> None:
    obsolete = [ROOT / "SLOP-ACCEPTED.md"]
    for path in obsolete:
        if path.exists():
            path.unlink()


def main() -> None:
    core_records = build_core_records()
    prepare_dirs()
    missing_core = set(CORE_FILENAMES) - (set(core_records) | set(WALKS))
    if missing_core:
        raise SystemExit(f"Missing core records: {sorted(missing_core)}")
    if set(ADVANCED_ORDER) != set(ADVANCED):
        raise SystemExit(f"Advanced mismatch: {set(ADVANCED_ORDER) ^ set(ADVANCED)}")

    write_scripts(core_records)
    master = generate_master(core_records)
    advanced_master = generate_advanced_master()
    (ROOT / "MASTER-COURSE.md").write_text(master, encoding="utf-8")
    (ROOT / "MASTER-ADVANCED.md").write_text(advanced_master, encoding="utf-8")
    generate_lesson_text(core_records)
    generate_module_files(master, advanced_master)
    (ROOT / "ALL-SCRIPTS.md").write_text(generate_onefile(core_records), encoding="utf-8")
    generate_docs(core_records)
    remove_obsolete()
    print("Course rebuild applied")


if __name__ == "__main__":
    main()
