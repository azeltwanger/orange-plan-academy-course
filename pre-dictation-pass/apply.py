#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIVIDER = "=" * 60
ARCHIVE_ROOT = ROOT / "archive" / "pre-dictation-copywriting-scripts-2026-08-26"

# These are Austin's words or the retained full-dictation calibration lesson.
# They do not get structurally rewritten by this pass.
PROTECTED_DICTATION = {
    "scripts/00-1_how-to-use-this-course.md",
    "scripts/01-1_what-to-gather-before-you-build-the-plan.md",
    "scripts/01-2_set-your-growth-and-inflation-assumption.md",
    "scripts/02-2_size-your-cash-reserve-in-months-of-spen.md",
}

GENERIC_ENDINGS = {
    "YOUR DECISION",
    "PUT IT IN ORANGE PLAN",
    "YOU ARE DONE WHEN",
}

EXACT_SLOP_REWRITES = {
    "That's the whole product.": "The loan is cash today in exchange for interest and Bitcoin held by the lender until the loan is repaid.",
    "That is too simple.": "That leaves out several other rules that can change the real cost.",
    "That is only the first pass.": "That only gives you the first part of the answer.",
    "Three documents, three jobs.": "Each document has a separate job, so the family is not relying on one file to carry legal authority, process instructions, and wallet recovery details.",
    "The response is always the same.": "For each one, write down the failure and the specific backup or process that keeps it from reaching the entire balance.",
    "State income tax is one line.": "State income tax is only one part of the cost of moving.",
    "That is the wrong comparison.": "That comparison leaves out the interest, collateral risk, and what happens if Bitcoin falls.",
    "The goal isn't to have the AI make every decision for you.": "I would use the AI to help you understand the plan, find missing information, and compare the trade-offs before you decide.",
    "The goal is not to have the AI make every decision for you.": "I would use the AI to help you understand the plan, find missing information, and compare the trade-offs before you decide.",
}

NEW_1_3_BODY = r'''[[OPEN — speak this naturally]]

In today's lesson, we're going to cover what the retirement age from onboarding actually means, and why it is going to change as you build the rest of your plan.

Onboarding only asked for a small amount of information. It used your age, income, spending, rough asset totals, where those assets are held, and the Bitcoin growth model you selected. That was enough to give you a useful starting point without making you build the entire plan before you saw anything.

But it is still a rough starting point. It does not know every real account and holding yet. It does not know all of your debts, future expenses, cost basis, Social Security, withdrawal strategy, or the tax decisions you might make later.

[[BEAT — explain how the age is calculated]]

The age you see in onboarding comes from one set of assumptions. It is not an average of 1,000 different market outcomes.

The technical word for this is deterministic. That just means that if you give the app the same numbers and the same assumptions, it is going to give you the same answer.

Orange Plan projects the plan at different retirement ages and looks for the earliest age where that projection can keep funding the spending you entered through the life-expectancy assumption. So if age 51 runs out of money but age 52 makes it through the end of the projection, onboarding is going to show age 52.

The different growth-model options work the same way. When you click Conservative, Moderate, Aggressive, or Power Law, the app runs the same calculation with that growth model and shows how much the assumption changes the age.

I think this is useful because it gives you an immediate sense of whether the plan is close or whether there is a large gap. But I would not treat that age like a promise. The inputs are still rough, and there has only been one projected path so far.

[[BEAT — explain why confidence waits]]

The app does not show a Monte Carlo confidence number during onboarding.

A percentage like 82% looks extremely precise. I do not think it makes sense to give somebody that level of precision when the app is still working from a few rough totals and none of the real planning decisions have been entered yet.

After you finish building the plan, Orange Plan is going to run it through 1,000 different market paths. Some of those paths are going to be fairly normal. Some are going to have a bad market right after retirement. Some are going to have higher inflation or several weak years stacked together.

The confidence number is simply the percentage of those 1,000 paths where the plan was able to fund everything that you entered.

So if 820 out of 1,000 paths make it through the plan, the result is 82% confidence. That does not mean there is exactly an 18% chance that you go broke. It means 180 of the modeled paths could not fund the exact spending and decisions in the plan without something changing.

That distinction matters because a real person can adjust. You can spend less after a bad year, work longer, delay a large purchase, change when you take Social Security, or make another decision. The confidence number is testing the plan as written so you can see how much room it has before one of those adjustments becomes necessary.

[[BEAT — connect the finished date to the confidence target]]

Once the real plan is built, you are also going to choose the confidence level you want the retirement date to meet. The default is 80%, but the app lets you change it.

At that point, the earliest retirement date is going to mean something different from the onboarding age. It is going to be the first age where the full 1,000-run test reaches the confidence target you selected.

So the onboarding age answers: when does this one rough projection first work?

The finished date answers: after the real plan is entered, what is the earliest age that reaches the confidence level I chose across 1,000 different paths?

[[BEAT — explain what changes next]]

The first thing we are going to replace is the rough account information. In the Foundation walkthrough, you are going to add your real accounts, enter what each one actually holds, and review the assumptions that powered the onboarding estimate.

We are not going to enter everything in that walkthrough. Income and spending belong in Cash Flow. Debts belong in the Debt module. Cost basis and transaction history belong in Tax. Retirement spending, Social Security, and the withdrawal strategy belong in Retirement Income.

That order gives you a chance to understand each decision before you enter it, instead of filling out one giant setup form without knowing what the numbers are going to affect.

So write down the onboarding age because it gives you a starting point. Just expect it to move as the rough information is replaced with the real plan.

Then watch the Foundation walkthrough below this video, where I'll show you how to replace the estimated accounts and holdings with what you actually own.

<!-- CHECKPOINT, NOT SPOKEN: The learner can explain that onboarding uses one deterministic projection from rough inputs, while the finished earliest date is searched against the chosen confidence target after the full plan is run through 1,000 paths. -->'''


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_teach_script(path: Path) -> bool:
    name = path.name.upper()
    if name == "VOICE-GUIDE.MD":
        return False
    if "WALKTHROUGH" in name or "DEMO" in name:
        return False
    return path.suffix.lower() == ".md"


def is_dictated(path: Path, text: str) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if rel in PROTECTED_DICTATION:
        return True
    header = text.split(DIVIDER, 1)[0]
    if "AUSTIN DICTATION" in header.upper():
        return True
    if re.search(r"SOURCE:.*Austin dictation", header, flags=re.I):
        return True
    return False


def sentence_case(title: str) -> str:
    title = re.sub(r"\s+", " ", title.strip())
    special = {
        "AI": "AI",
        "RMD": "RMD",
        "RMDs": "RMDs",
        "LTV": "LTV",
        "UTXO": "UTXO",
        "UTXOs": "UTXOs",
        "Bitcoin": "Bitcoin",
        "Roth": "Roth",
    }
    words = []
    for index, raw in enumerate(title.lower().split(" ")):
        clean = raw.strip()
        replacement = next((value for key, value in special.items() if clean == key.lower()), None)
        if replacement:
            words.append(replacement)
        elif index == 0:
            words.append(clean[:1].upper() + clean[1:])
        else:
            words.append(clean)
    return " ".join(words)


def comment_block(label: str, content: str) -> str:
    clean = content.strip().replace("--", "—")
    return f"<!-- {label}, NOT SPOKEN:\n{clean}\n-->"


def apply_line_cleanup(text: str) -> str:
    for old, new in EXACT_SLOP_REWRITES.items():
        text = text.replace(old, new)

    # These phrases are common copywriting frames. Reword the frame while
    # retaining the actual claim that follows it.
    text = re.sub(r"\bThe goal is not to\b", "You are not trying to", text)
    text = re.sub(r"\bThe goal isn't to\b", "You are not trying to", text)
    text = re.sub(r"\bThe goal is to\b", "What you are trying to do is", text)
    text = re.sub(r"\bThe point is not to\b", "This is not about", text)

    # Remove a few producer-style phrases that tell Austin how to land a line
    # instead of giving him the point to explain.
    text = re.sub(r"(?m)^Land (?:it|the line):\s*", "", text)
    text = re.sub(r"(?m)^Worth saying:\s*", "", text)
    text = re.sub(r"(?m)^Say it out loud:\s*", "", text)
    return text


def convert_body(body: str) -> str:
    body = apply_line_cleanup(body.strip())
    split = re.split(r"(?m)^==\s*(.+?)\s*==\s*$", body)
    if len(split) == 1:
        return body

    output: list[str] = []
    intro = split[0].strip()
    if intro:
        output.append("[[OPEN — speak this naturally]]\n\n" + intro)

    decision = ""
    app_note = ""
    checkpoint = ""

    for index in range(1, len(split), 2):
        heading = re.sub(r"\s+", " ", split[index].strip().upper())
        content = split[index + 1].strip() if index + 1 < len(split) else ""
        if not content:
            continue

        if heading == "YOUR DECISION":
            decision = content
            continue
        if heading == "PUT IT IN ORANGE PLAN":
            app_note = content
            continue
        if heading == "YOU ARE DONE WHEN":
            checkpoint = content
            continue
        if heading == "HOMEWORK":
            output.append("[[HOMEWORK — read the numbered actions, not this label]]\n\n" + content)
            continue

        output.append(f"[[BEAT — {sentence_case(heading)}]]\n\n{content}")

    if decision:
        output.append("[[CLOSE — say the decision plainly]]\n\n" + decision)
    if app_note:
        output.append(comment_block("APP OR WALKTHROUGH HANDOFF", app_note))
    if checkpoint:
        output.append(comment_block("CHECKPOINT", checkpoint))

    return "\n\n".join(output).strip()


def update_header(header: str) -> str:
    lines = header.rstrip().splitlines()
    changed = False
    for index, line in enumerate(lines):
        if "SPOKEN-PROSE VERSION" in line:
            prefix = line.split("·", 1)[0].rstrip() if "·" in line else ""
            runtime = prefix + " · " if prefix else ""
            lines[index] = runtime + "SPOKEN-PROSE VERSION — PRE-DICTATION PLAIN DRAFT"
            changed = True
            break
    if not changed:
        lines.append("SPOKEN-PROSE VERSION — PRE-DICTATION PLAIN DRAFT")
    note = "DICTATION NOTE: Facts and order are set. Bracketed cues and HTML comments are not spoken. Change the wording naturally while preserving the claim."
    if note not in lines:
        lines.append(note)
    return "\n".join(lines)


def lesson_title(text: str, fallback: str) -> str:
    for line in text.splitlines()[:8]:
        if re.match(r"^(?:A?\d+\.\d+)\s+", line.strip()):
            return line.strip()
    return fallback


def replace_factual_onboarding_language() -> None:
    old = (
        "The age is a deterministic estimate. The app takes the numbers you entered, "
        "applies the selected growth model, and finds the earliest age where that one "
        "average projection can fund the spending target."
    )
    new = (
        "The onboarding age comes from one deterministic projection. That means the same "
        "inputs and assumptions produce the same answer. Orange Plan tests different "
        "retirement ages and finds the earliest one where that projected plan lasts through "
        "the life-expectancy assumption. It is not averaging 1,000 market paths during onboarding."
    )
    candidates = [
        ROOT / "MASTER-COURSE.md",
        ROOT / "lesson-text" / "01-3_read-your-retirement-date-and-confidence.md",
    ]
    for path in candidates:
        if not path.exists():
            continue
        text = read(path)
        if old in text:
            write(path, text.replace(old, new, 1))
        elif "one average projection" in text:
            raise RuntimeError(f"Could not safely replace stale onboarding language in {path}")


def add_voice_policy() -> None:
    path = ROOT / "scripts" / "VOICE-GUIDE.md"
    text = read(path)
    marker = "## Dictation-derived rules (diffed against the same content written by AI)"
    section = r'''## Pre-dictation draft policy — 2026-08-26

A non-dictated lesson is not supposed to impersonate Austin's final voice. It is a research-complete speaking draft that makes his real dictation faster.

- Use bracketed **OPEN / BEAT / CLOSE / HOMEWORK** cues as navigation. They are not spoken.
- Do not force every lesson through `YOUR DECISION`, `PUT IT IN ORANGE PLAN`, and `YOU ARE DONE WHEN` as three spoken sections. The decision may be spoken naturally; app clicks and checklist language can remain non-spoken notes for the walkthrough and student layer.
- Prefer a plain explanation, the reason it changes the plan, one concrete example, and the practical decision.
- Preserve technical qualifications, verified math, and app behavior even when the sentence has to stay more formal.
- Once Austin dictates a lesson, replace the draft with his words and change the provenance label to `AUSTIN DICTATION`.

'''
    if "## Pre-dictation draft policy — 2026-08-26" not in text:
        if marker not in text:
            raise RuntimeError("VOICE-GUIDE insertion marker missing")
        text = text.replace(marker, section + marker, 1)
        write(path, text)


def main() -> None:
    paths = sorted((ROOT / "scripts").glob("*.md")) + sorted((ROOT / "scripts" / "advanced").glob("*.md"))
    protected_before = {
        rel: digest(ROOT / rel)
        for rel in PROTECTED_DICTATION
        if (ROOT / rel).exists()
    }

    converted: list[dict[str, str]] = []
    protected: list[dict[str, str]] = []
    archive_manifest: list[str] = []

    for path in paths:
        if not is_teach_script(path):
            continue
        original = read(path)
        rel = path.relative_to(ROOT).as_posix()
        title = lesson_title(original, path.stem)

        if is_dictated(path, original):
            protected.append({"path": rel, "title": title})
            continue

        if DIVIDER not in original:
            raise RuntimeError(f"Teach script divider missing: {rel}")

        archive_path = ARCHIVE_ROOT / path.relative_to(ROOT / "scripts")
        write(archive_path, original)
        archive_manifest.append(archive_path.relative_to(ROOT).as_posix())

        header, body = original.split(DIVIDER, 1)
        header = update_header(header)
        if rel == "scripts/01-3_read-your-retirement-date-and-confidence.md":
            new_body = NEW_1_3_BODY
            mode = "manual rebuild"
        else:
            new_body = convert_body(body)
            mode = "plain structural draft"

        write(path, header + "\n" + DIVIDER + "\n\n" + new_body)
        converted.append({"path": rel, "title": title, "mode": mode})

    # Genuine dictation must be byte-for-byte unchanged.
    for rel, before in protected_before.items():
        after = digest(ROOT / rel)
        if before != after:
            raise RuntimeError(f"Protected Austin dictation changed: {rel}")

    replace_factual_onboarding_language()
    add_voice_policy()

    archive_index = [
        "# Archived pre-dictation copywriting scripts",
        "",
        "These files preserve the research-complete prose that existed before the plain-draft pass. They are reference material only. The active `scripts/` files are the versions Austin should dictate from.",
        "",
        *[f"- `{item}`" for item in archive_manifest],
    ]
    write(ARCHIVE_ROOT / "README.md", "\n".join(archive_index))

    order_lines = [
        "# Pre-dictation order",
        "",
        "Use the active file under `scripts/`. Bracketed cues and HTML comments are not spoken. Replace the wording naturally as you dictate; the facts, examples, and required qualifications are already in order.",
        "",
        "## Already Austin dictation — do not redraft unless Austin chooses to",
        "",
        *[f"- **{item['title']}** — `{item['path']}`" for item in protected],
        "",
        "## Plain drafts ready for Austin",
        "",
        *[f"- **{item['title']}** — {item['mode']} — `{item['path']}`" for item in converted],
        "",
        "## Remaining authorship blocker",
        "",
        "Lesson **4.3** still needs Austin's actual next-dollar default order, the override rules, and when a deliberate split is appropriate. Its current file is now easier to speak through, but the unresolved planning judgment remains clearly marked as F22.",
    ]
    write(ROOT / "PRE-DICTATION-ORDER.md", "\n".join(order_lines))

    report = [
        "# Pre-dictation plain-draft pass",
        "",
        "**Completed:** 2026-08-26",
        "",
        "## Purpose",
        "",
        "The earlier voice pass removed several obvious AI phrases but left the generated copywriting architecture in place. This pass changes the job of every non-dictated teleprompter file: it is now a plain speaking draft that makes Austin's chronological dictation faster, not a polished imitation of his final voice.",
        "",
        "## What changed",
        "",
        f"- {len(converted)} non-dictated core and Advanced teach scripts converted to plain speaking drafts.",
        f"- {len(protected)} genuine-dictation scripts left byte-for-byte unchanged.",
        "- Repetitive spoken `YOUR DECISION / PUT IT IN ORANGE PLAN / YOU ARE DONE WHEN` sections were removed from generated scripts. Decisions remain as a simple close; click paths and checklist language are non-spoken notes.",
        "- Every remaining content heading became a bracketed navigation cue rather than a polished section title.",
        "- The original generated prose was archived before conversion.",
        "- Lesson 1.3 was rebuilt manually around the verified production behavior: one deterministic onboarding projection, no Monte Carlo confidence at the reveal, and the full 1,000-path confidence search after the plan is built.",
        "",
        "## Converted scripts",
        "",
        *[f"- `{item['path']}` — {item['mode']}" for item in converted],
        "",
        "## Protected dictation",
        "",
        *[f"- `{item['path']}`" for item in protected],
    ]
    write(ROOT / "PRE-DICTATION-PLAIN-DRAFT-PASS.md", "\n".join(report))

    manifest = {
        "converted": converted,
        "protected": protected,
        "archive": archive_manifest,
    }
    write(ROOT / "pre-dictation-pass-manifest.json", json.dumps(manifest, indent=2))

    print(f"converted {len(converted)} non-dictated scripts; protected {len(protected)} Austin-dictated scripts")


if __name__ == "__main__":
    main()
