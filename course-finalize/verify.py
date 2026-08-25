#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP_COMMIT = "5cf664ab2835635bc571f64eb12c16dbb5a10833"


def run(label: str, command: list[str], log: list[tuple[str, int, str]]) -> None:
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    output = (proc.stdout + proc.stderr).strip()
    log.append((label, proc.returncode, output))
    if proc.returncode != 0:
        raise RuntimeError(f"{label} failed\n{output}")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text.rstrip() + "\n", encoding="utf-8")


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def sections(master: str) -> list[dict[str, str]]:
    hits = list(re.finditer(r"(?m)^## (A\d+\.\d+) ([^\n]+)$", master))
    out = []
    for index, hit in enumerate(hits):
        end = hits[index + 1].start() if index + 1 < len(hits) else len(master)
        body = master[hit.start():end]
        body = re.split(r"(?m)^# Advanced Module ", body)[0]
        out.append({"number": hit.group(1), "title": hit.group(2).strip(), "body": body})
    return out


def gate_text(body: str) -> str:
    match = re.search(r"(?ms)^> \*\*Gate\.\*\*\s*(.*?)(?=\n\n|^\*\*By the end)", body)
    if not match:
        return "MISSING"
    return re.sub(r"\n> ?", " ", match.group(1)).strip()


def script_for(number: str) -> Path:
    prefix = number.replace(".", "-") + "_"
    matches = sorted((ROOT / "scripts" / "advanced").glob(prefix + "*.md"))
    if len(matches) != 1:
        raise RuntimeError(f"{number}: expected one script, found {matches}")
    return matches[0]


def lesson_text_for(number: str) -> Path:
    prefix = number.replace(".", "-") + "_"
    matches = sorted((ROOT / "lesson-text" / "advanced").glob(prefix + "*.md"))
    if len(matches) != 1:
        raise RuntimeError(f"{number}: expected one lesson-text file, found {matches}")
    return matches[0]


def provenance(text: str) -> str:
    head = text[:1200]
    if "AUSTIN DICTATION" in head:
        return "Austin dictation"
    if "SPOKEN-PROSE VERSION" in head:
        return "spoken-prose calibrated"
    return "UNPROTECTED"


def body_words(text: str) -> int:
    return len(text.split("=" * 60, 1)[-1].split())


def make_gate_approval(lessons: list[dict[str, str]]) -> None:
    lines = [
        "# Advanced gate approval",
        "",
        "These conditions decide who is told to watch or skip an Advanced lesson. They are producer-facing and are not read in the video. Austin's approval is required because a gate is a planning judgment, not a copy edit.",
        "",
        "Mark each line **keep**, **change**, or **remove** before the Advanced Library is published in Circle. Dictation can proceed from the lesson script while this page is reviewed, except where a professional-review gate says not to record yet.",
        "",
    ]
    for lesson in lessons:
        lines += [
            f"## ☐ {lesson['number']} · {lesson['title']}",
            "",
            f"> {gate_text(lesson['body'])}",
            "",
            "Decision: ☐ Keep  ☐ Change  ☐ Remove",
            "",
            "Replacement, if any:",
            "",
            "---",
            "",
        ]
    write("ADVANCED-GATE-APPROVAL.md", "\n".join(lines))


def review_status(number: str) -> str:
    if number in {"A5.1", "A5.2", "A5.3", "A6.2"}:
        return "CPA review before recording"
    if number in {"A7.1", "A7.2", "A7.3", "A7.4"}:
        return "Custody-professional review before recording"
    if number == "A8.1":
        return "Ready to dictate; estate-attorney review before publication"
    return "Ready to dictate"


def make_advanced_order(lessons: list[dict[str, str]]) -> None:
    by_num = {lesson["number"]: lesson for lesson in lessons}
    order = [
        "A3.1", "A6.1", "A5.1", "A7.1", "A6.2", "A5.2", "A7.2",
        "A1.1", "A3.2", "A4.1", "A5.3", "A7.3", "A7.4", "A8.1",
    ]
    lines = [
        "# Advanced Library dictation order",
        "",
        "All 14 lessons have protected, spoken-ready teleprompter scripts. Work top to bottom in demand order. A professional-review label means the script is editorially prepared but should not be recorded or published past the stated gate.",
        "",
        "**Before the first take:** read `ADVANCED-GATE-APPROVAL.md`. Gate copy is not spoken, but it controls who sees each lesson.",
        "",
        "| Order | Lesson | Runtime | Provenance | Production status |",
        "|---:|---|---:|---|---|",
    ]
    total_words = 0
    for index, number in enumerate(order, 1):
        lesson = by_num[number]
        script = script_for(number)
        text = script.read_text(encoding="utf-8")
        prov = provenance(text)
        words = body_words(text)
        total_words += words
        minutes = words / 155
        lines.append(
            f"| {index} | **{number}** · {lesson['title']} | {minutes:.1f} min | {prov} | {review_status(number)} |"
        )
    lines += [
        "",
        f"**Total:** {len(order)} lessons · {total_words:,} words · about {total_words / 155:.0f} minutes.",
        "",
        "## Recording rule",
        "",
        "Read the teleprompter script, not the master and not the student text. The master owns course structure and gates. Student text owns current figures and verification notes. The script owns what is spoken.",
        "",
        "## App-dependent lessons",
        "",
        "Before recording A3.1, A3.2, A5.1, A5.2, A6.1, A6.2, and A8.1, open the current Orange Plan screen named in the lesson. Do not read a label that is not visible in the current build.",
    ]
    write("ADVANCED-DICTATION-ORDER.md", "\n".join(lines))


def make_pickups() -> None:
    text = r'''# Dictation pickups and final Austin approvals

This is the only remaining Austin decision sheet. Do not start another broad rewrite pass.

## Blocking pickup 1 · F20 · the 7-to-10-year funding lane

Lesson 2.3 currently names these lanes:

- 0 to 1 year
- 1 to 3 years
- 3 to 7 years
- 10+ years

Seven to ten is intentionally blank because filling it changes the planning rule.

### Start dictating here

> For a known expense that is seven to ten years away, my default is ____________________. The reason is ____________________. As the date gets closer, I would ____________________.

### The line must answer

1. Can Bitcoin be part of this lane?
2. If yes, at what point does the committed amount stop depending on Bitcoin's price?
3. Does the answer change the current ten-year Bridge/Legacy rule, or only explain the transition into it?

**Where it lands:** 2.3 master, script, lesson text, visual lane table, Module 2 checkpoint, and the 2.5 walkthrough.

---

## Blocking pickup 2 · F22 · route the next dollar

The current 4.3 strict waterfall is on hold because the client-call evidence showed that the real decision sometimes compares or splits between taxable bridge savings, retirement accounts, and Bitcoin rather than maxing every earlier rung first.

### Dictate the lesson in this order

1. **The default order.** What normally comes first?
2. **Strong presumptions.** Which items almost always win, such as an employer match or very high-interest debt?
3. **Overrides.** Which facts change the default: an underfunded pre-59½ bridge, variable income, near-term retirement, a tax window, a thin reserve, or something else?
4. **The comparison zone.** How do HSA, Roth, traditional, taxable Bitcoin, and taxable bridge assets get compared?
5. **A deliberate split.** When is dividing the dollar between two valid needs the correct answer rather than indecision?

### Start dictating here

> Once the reserve and debt policy are set, the default route for the next dollar is ____________________. The things that usually come first are ____________________. I would override that order when ____________________. A deliberate split makes sense when ____________________.

**Where it lands:** 4.3 master, protected script, lesson text, Module 4 checkpoint, contribution examples, and 4.5 walkthrough.

---

## Non-blocking approval · F6 · Level 2 family access

Current course position: with one hardware wallet and one seed, the seed goes to the heir with redundant copies, while the executor holds the process rather than the secret. This passes redundancy and accepts that the heir can spend alone.

At the microphone, keep it, correct it, or mark it for a pickup. A change to the underlying design must be made in 8.2 and the custody/estate worksheets before publication.

---

## Non-blocking approval · annual review month

Current live course choice: **November**, so tax actions can still happen before year-end. The older phrase "October or November" is retired unless Austin changes it back deliberately.

---

## Text-layer approval · Advanced gates

Review `ADVANCED-GATE-APPROVAL.md`. These lines are not spoken, so the microphone cannot catch a gate that sends the wrong household to skip a lesson.
'''
    write("DICTATION-PICKUPS.md", text)


def module_contains(number: str) -> bool:
    pattern = re.compile(rf"(?m)^## {re.escape(number)} ")
    return any(pattern.search(path.read_text(encoding="utf-8")) for path in (ROOT / "modules" / "advanced").glob("*.md"))


def make_advanced_audit(lessons: list[dict[str, str]], check_log: list[tuple[str, int, str]]) -> None:
    lines = [
        "# Advanced Library dictation-readiness audit",
        "",
        "Generated after the finalization pass.",
        "",
        "| Lesson | Script provenance | Words | Gate | Master | Script | Student text | Generated module | Homework |",
        "|---|---|---:|---|---|---|---|---|---|",
    ]
    ready = 0
    total_words = 0
    for lesson in lessons:
        number = lesson["number"]
        script_path = script_for(number)
        script = script_path.read_text(encoding="utf-8")
        lesson_text = lesson_text_for(number).read_text(encoding="utf-8")
        prov = provenance(script)
        words = body_words(script)
        total_words += words
        gate = gate_text(lesson["body"])
        homework = bool(re.search(r"(?im)^== HOMEWORK ==|^### Homework|^## Homework", script + "\n" + lesson_text))
        complete = prov != "UNPROTECTED" and gate != "MISSING" and homework and module_contains(number)
        ready += int(complete)
        lines.append(
            f"| **{number}** · {lesson['title']} | {prov} | {words:,} | {'yes' if gate != 'MISSING' else 'NO'} | yes | yes | yes | {'yes' if module_contains(number) else 'NO'} | {'yes' if homework else 'NO'} |"
        )
    lines += [
        "",
        f"**Result:** {ready} of {len(lessons)} lessons have a protected script, gate, student text, generated module, and finish line.",
        f"**Runtime:** {total_words:,} spoken words, about {total_words / 155:.0f} minutes.",
        "",
        "## Repository gates",
        "",
    ]
    for label, code, output in check_log:
        lines += [
            f"### {'PASS' if code == 0 else 'FAIL'} · {label}",
            "",
            "```text",
            output[-5000:] or "(no output)",
            "```",
            "",
        ]
    write("ADVANCED-DICTATION-AUDIT.md", "\n".join(lines))


def make_final_status(lessons: list[dict[str, str]], check_log: list[tuple[str, int, str]]) -> None:
    production = read("PRODUCTION-CHECKLIST.md")
    blocker_lines = []
    in_blockers = False
    for line in production.splitlines():
        if "CORE FILMING BLOCKERS" in line:
            in_blockers = True
            continue
        if in_blockers and line.startswith("> ###"):
            break
        if in_blockers and line.startswith("> -"):
            blocker_lines.append(line[2:].strip())
    pass_count = sum(code == 0 for _, code, _ in check_log)
    lines = [
        "# Course finalization status",
        "",
        "## Editorial status",
        "",
        "- The ten-module core structure is locked.",
        "- Austin's 0.2 / 1.1 / 1.2 source is retained and mapped to the live scripts.",
        "- All 14 Advanced Library lessons have protected spoken-ready scripts, gates, student text, generated modules, and finish lines.",
        f"- Core and Advanced app references were aligned to Orange Plan main at `{APP_COMMIT}`, including contribution planning during a current deficit.",
        "- Module 2 order is final: 2.4 optional college, 2.5 walkthrough.",
        "",
        "## Ready to dictate now",
        "",
        "- Core lessons not named under the blockers below.",
        "- Advanced lessons labelled **Ready to dictate** in `ADVANCED-DICTATION-ORDER.md`.",
        "- A8.1 is script-ready, but publication waits for estate-attorney review.",
        "",
        "## Austin pickups still required",
        "",
        "- F20: one sentence for the 7-to-10-year future-cost lane.",
        "- F22: the next-dollar default order, overrides, and deliberate-split rule.",
        "- Advanced gate approval is text-layer approval, not spoken dictation.",
        "",
        "The exact prompts are in `DICTATION-PICKUPS.md`.",
        "",
        "## Current generated filming blockers",
        "",
        *(blocker_lines or ["None."]),
        "",
        "## Professional review gates",
        "",
        "- Bitcoin-aware CPA before recording Module 5 and A5.1, A5.2, A5.3, A6.2.",
        "- Custody professional before recording Module 7 and A7.1 through A7.4.",
        "- Insurance professional before recording 8.4.",
        "- Estate attorney before publishing A8.1 and the executor materials in 8.1 / 8.5.",
        "",
        "These are external signoffs, not unfinished course editing.",
        "",
        "## Verification",
        "",
        f"{pass_count} of {len(check_log)} final repository checks passed.",
    ]
    write("FINALIZATION-STATUS.md", "\n".join(lines))


# Build generated layers first.
build_log: list[tuple[str, int, str]] = []
for label, command in [
    ("Build module gates", ["python3", "tools/build-module-gates.py"]),
    ("Build core scripts", ["python3", "tools/build-scripts.py"]),
    ("Build Advanced scripts", ["python3", "tools/build-scripts.py", "--advanced"]),
    ("Split core modules", ["python3", "tools/split-modules.py"]),
    ("Split Advanced modules", ["python3", "tools/split-modules.py", "--advanced"]),
    ("Build one-file scripts", ["python3", "tools/build-onefile.py"]),
    ("Build Circle structure", ["python3", "tools/build-circle-structure.py"]),
    ("Build dictation order", ["python3", "tools/build-dictation-order.py"]),
    ("Build film order", ["python3", "tools/build-film-order.py"]),
    ("Build shoot list", ["python3", "tools/build-shoot-list.py"]),
    ("Build production checklist", ["python3", "tools/build-production-checklist.py"]),
    ("Update metrics", ["python3", "tools/course-metrics.py"]),
]:
    run(label, command, build_log)

master = read("MASTER-ADVANCED.md")
lessons = sections(master)
if len(lessons) != 14:
    raise RuntimeError(f"expected 14 Advanced lessons, found {len(lessons)}")

make_gate_approval(lessons)
make_advanced_order(lessons)
make_pickups()

# Hard finalization assertions before the standard gates.
for lesson in lessons:
    number = lesson["number"]
    text = script_for(number).read_text(encoding="utf-8")
    if provenance(text) == "UNPROTECTED":
        raise RuntimeError(f"{number}: script is still generated/unprotected")
    if "== HOMEWORK ==" not in text and "### Homework" not in text:
        raise RuntimeError(f"{number}: no spoken homework/finish line")
    if gate_text(lesson["body"]) == "MISSING":
        raise RuntimeError(f"{number}: missing Advanced gate")

combined = "\n".join(
    path.read_text(encoding="utf-8")
    for path in [ROOT / "MASTER-COURSE.md", *sorted((ROOT / "scripts").glob("*.md")), *sorted((ROOT / "lesson-text").glob("*.md"))]
)
for stale in [
    "contribution rows only appear with a surplus",
    "Routing pauses honestly",
    "Deficit months pause routing honestly",
    "four paths: linked account, file, describe to AI, manual",
]:
    if stale.lower() in combined.lower():
        raise RuntimeError(f"stale current-app wording remains: {stale}")

if not (ROOT / "source-material/2026-08-25-module-0-1-dictation.md").exists():
    raise RuntimeError("Austin source material is not retained")
for path in [
    "scripts/00-2_how-the-ai-works-what-it-reads-what-it-n.md",
    "scripts/01-1_what-to-gather-before-you-build-the-plan.md",
    "scripts/01-2_set-your-growth-and-inflation-assumption.md",
]:
    if "source-material/2026-08-25-module-0-1-dictation.md" not in read(path):
        raise RuntimeError(f"{path}: source header missing")

# Run the repository gates on the final generated tree.
check_log: list[tuple[str, int, str]] = []
for label, command in [
    ("Cross-references", ["python3", "tools/check-crossrefs.py"]),
    ("Layer parity", ["python3", "tools/check-layer-parity.py"]),
    ("Slop scan", ["python3", "tools/slop-scan.py", "--all"]),
    ("Visual coverage", ["python3", "tools/check-visuals.py"]),
    ("Metrics freshness", ["python3", "tools/course-metrics.py", "--check"]),
]:
    run(label, command, check_log)

make_advanced_audit(lessons, check_log)
make_final_status(lessons, check_log)

# Final docs themselves must not introduce stale references.
if "F23" in read("PRODUCTION-CHECKLIST.md"):
    raise RuntimeError("resolved F23 still appears in production blockers")
if "TEXT ONLY for now" in read("PRODUCTION-CHECKLIST.md"):
    raise RuntimeError("Advanced production list still leaves scripts as text-only")
