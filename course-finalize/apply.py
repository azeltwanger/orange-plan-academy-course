#!/usr/bin/env python3
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


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one exact match, found {count}")
    return text.replace(old, new, 1)


def sub_once(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    text, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one regex match, found {count}")
    return text


def replace_advanced_lesson(text: str, number: str, replacement: str) -> str:
    pattern = re.compile(
        rf"(?ms)^## {re.escape(number)} [^\n]*\n.*?(?=^## A\d+\.\d+ |^# Advanced Module |\Z)"
    )
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"advanced lesson {number}: expected one section, found {len(matches)}")
    match = matches[0]
    return text[:match.start()] + replacement.rstrip() + "\n\n" + text[match.end():]


def add_header_source(path: str, source_line: str) -> None:
    text = read(path)
    if source_line in text:
        return
    divider = "=" * 60
    if divider not in text:
        raise RuntimeError(f"{path}: teleprompter divider missing")
    head, body = text.split(divider, 1)
    head = head.rstrip() + "\n" + source_line + "\n"
    write(path, head + divider + body)


DICTATION_SOURCE_MAP = r'''# Dictation source map

This file says which words came from Austin, what an editor changed, and where the original source lives. It exists so a future edit cannot call generated prose "dictation" or silently overwrite a planning position.

## Source record

Original source: `source-material/2026-08-25-module-0-1-dictation.md`.

The original is preserved as supplied. The live scripts are allowed to fix sequencing, grammar, app paths, and verified math, but the change has to be named here.

## 0.1 · How to use this course

Austin's note was: **"Looks good in my voice for now."** The existing `AUSTIN DICTATION` script remains the authority. The 2026-08-25 lifecycle pass only changed references that became factually wrong after onboarding and Build Your Plan changed.

## 0.2 · How to use Orange Plan AI

**Source type:** Austin direction, not line-by-line dictation.

Austin directed the lesson to focus on benefits and actual use: the buttons, useful prompts, the daily Bitcoin market report, asking questions as plan numbers update, finding missing considerations, and exporting a privacy-scrubbed file to a preferred AI. The rewritten script follows that brief. Privacy remains, but it no longer owns the lesson.

**Editorial work:** app behavior was verified against the Orange Plan code. The script is labelled `SPOKEN-PROSE VERSION (calibrated)`, not `AUSTIN DICTATION`, because Austin gave the target and examples rather than a complete spoken script.

## 1.1 · What to gather before you build the plan

**Source type:** Austin dictation, especially items 4 through 7.

Preserved positions include:

- log in and verify every debt balance and current rate
- gather the actual employer-match formula, pension, deferred compensation, and stock-option information
- begin thinking through expected future income and expenses
- start cost-basis reconstruction now, download every exchange and brokerage CSV, and keep the files in one folder
- gathering everything up front is easier, but gathering it module by module is also valid

**Editorial work:** the live script separates gathering from entering. Foundation enters real accounts and holdings. Cash Flow enters income, spending, reserve, and life events. Debt enters loans. Tax reconstructs history and basis. No planning recommendation was replaced.

## 1.2 · The three layers of a plan, and setting your assumptions

**Source type:** Austin dictation.

Preserved positions include:

- baseline contains today's facts plus the assumptions used to project them
- expected changes belong in life events
- hypothetical questions belong in Scenarios
- Orange Plan projects a retirement plan; it is not a forever coffee-category budgeting app
- assumptions drive tax planning, contributions, retirement withdrawals, and other downstream decisions
- lean conservative, use declining Bitcoin returns, take inflation seriously, and choose assumptions you could defend out loud
- Power Law is Austin's preferred starting point; Moderate is the step down; Conservative is the more cautious choice
- test a more bullish case as a scenario rather than rewriting the baseline to get a better answer

**Editorial work:**

1. The preview/apply paragraph Austin called "tacked on" was removed from 1.2 and moved to the Retirement Income walkthrough, where the learner first needs it.
2. The clicks for assumptions live in the Foundation walkthrough. The teach lesson names the decision and points forward rather than reading the same click path twice.
3. The dictated 4% inflation example said roughly $105,000. Verified compounding is roughly $144,000 after 15 years on $80,000, so the live script corrects the math and preserves the teaching point.

## Rule for future edits

A script labelled `AUSTIN DICTATION` must link to a retained source or transcript. A script labelled `SPOKEN-PROSE VERSION` may preserve Austin's position and voice calibration, but it may never be presented as his original wording.
'''
write("DICTATION-SOURCE-MAP.md", DICTATION_SOURCE_MAP)

add_header_source(
    "scripts/00-2_how-the-ai-works-what-it-reads-what-it-n.md",
    "SOURCE: source-material/2026-08-25-module-0-1-dictation.md · Austin direction, editor-shaped script",
)
add_header_source(
    "scripts/01-1_what-to-gather-before-you-build-the-plan.md",
    "SOURCE: source-material/2026-08-25-module-0-1-dictation.md · Austin dictation, revised only for current course sequence",
)
add_header_source(
    "scripts/01-2_set-your-growth-and-inflation-assumption.md",
    "SOURCE: source-material/2026-08-25-module-0-1-dictation.md · Austin dictation; verified math and walkthrough split documented in DICTATION-SOURCE-MAP.md",
)

# ---------------------------------------------------------------------------
# Advanced Library: lock the lifecycle, convert the two remaining generated
# scripts to calibrated spoken prose, and give every lesson a finish line.
# ---------------------------------------------------------------------------

advanced = read("MASTER-ADVANCED.md")
advanced = sub_once(
    advanced,
    r"\*\*Course 2 of 2\.\*\*.*?\n---",
    r'''**Course 2 of 2.** Optional. The A-numbers are final, and each section mirrors the core module that owns the decision.

Complete the matching core Build Your Plan area first. The core walkthrough enters the real data and establishes the plan of record. An advanced lesson starts from that completed area and goes deeper only when its gate is true.

Nothing here is required to finish a plan. Each lesson opens with a gate you can check against your own situation or screen. If the condition does not apply, that planning area is complete without the lesson.

Advanced lessons do not recreate onboarding, rebuild Foundation, or run the first confidence check. They may explain a result, model a triggered decision, or compare a scenario. A preview or scenario stays separate from the plan until the app explicitly applies it.

Every advanced video closes with a decision and a short homework/finish line. The student-facing text carries current figures and verification notes that should not be frozen into a video.

---''',
    "advanced lifecycle intro",
    flags=re.S,
)

A4_MASTER = r'''## A4.1 The price context check: naming the emotion before a big move

*`TEACH` · ~430 words · ~3 min*

> **Gate.** Watch this before any Bitcoin-heavy move: a large buy, selling to
> lock in gains, or taking a Bitcoin-backed loan. Your allocation decision is
> complete without it.

**By the end of this lesson, you can:**

- Run two lookback windows before a Bitcoin-heavy move
- Separate what the recent price makes you feel from what the longer trend says
- Decide whether the plan or the price is driving the move

---

This is a short check to run before any Bitcoin-heavy move. A large buy, a sale to lock in gains, or a Bitcoin-backed loan can all be reasonable decisions. The problem is that the exact same decision can also be an emotional reaction to the last few months.

The point of this check is not to tell you whether to buy, sell, or borrow. It is to name what is in the room before you decide.

### Two lookbacks

Start with the recent window: 3, 6, 9, and 12 months.

That window tells you what you are feeling. If Bitcoin is up 40% in three months, there is probably some FOMO in the decision. If it is down 40%, there is probably fear. You do not need to pretend either one is not there. You just need to name it.

Then zoom out to 2 to 5 years.

That window tells you what has actually happened over a meaningful period. It shows the direction of the trend instead of the mood of the last week.

The recent window names the emotion. The long window gives it context.

### Put the proposed move back against the plan

Now describe the move without using today's price as the reason.

Why does it fit your allocation target, cash reserve, debt ceiling, tax plan, or retirement-income strategy? What problem is it solving? What would still make the decision reasonable if Bitcoin moved the other direction next month?

If you cannot explain it without saying that the price has been going up or going down, the price is probably doing more of the work than the plan is.

That does not automatically make the move wrong. It means you should wait a beat, open the owning page or scenario, and make sure the numbers support what the emotion wants to do.

### Your decision

Whether this move is the plan talking or the price talking.

### Homework

1. Write the move in one sentence without mentioning the recent Bitcoin price.
2. Write what the 3-to-12-month window makes you feel and what the 2-to-5-year window shows.
3. Open the owning plan page or scenario and confirm the move still makes sense against the rules you already set.

You are done when you can defend the move from the plan even if the last three months of price action were reversed.
'''
advanced = replace_advanced_lesson(advanced, "A4.1", A4_MASTER)

A7_2_MASTER = r'''## A7.2 What self-custody actually asks of you

*`TEACH` · ~470 words · ~3 min*

> **Gate.** Optional throughout. Watch it if you are weighing whether you want
> the whole job of self-custody, or if the weight of it is what has been
> stopping you. Your custody plan is complete without it.

**By the end of this lesson, you can:**

- Name the responsibility self-custody transfers to you
- Decide whether you want the whole job, part of it, or none of it
- Match that honest answer to the custody level you can actually maintain

---

A client put this better than I ever have.

He said that with self-custody, you are the point of failure. And you are not only the failure point. You are also the attack vector.

Then he made the point that most of life does not work this way. We outsource violence to the police. We outsource security to banks and other institutions. A big part of civilization is handing the hard and dangerous jobs to people whose job it is to carry them.

Bitcoin gives you the ability to take one of those jobs back.

That is why custody can feel heavier than the rest of a financial plan. It is not another investment checkbox. You are accepting a responsibility that somebody else carries for nearly every other asset you own.

### What the whole job includes

The whole job is not just owning a hardware wallet.

It includes protecting the recovery material, keeping the process usable, testing that recovery works, maintaining the devices and software, noticing new single points of failure, and making sure somebody besides you can follow the process when your family needs it.

The device is one part. The ongoing responsibility is the job.

### Three honest answers

The first honest answer is that you want the whole job. That can be the right choice when the amount, your skill, and your willingness to maintain it all line up.

The second answer is that you want part of it. That is what collaborative custody is for, and it is why a hardened institution can legitimately hold part of a stack. You keep some control and hand off some responsibility.

The third answer is that you do not want the job right now. That is also a real answer. Taking responsibility you will not maintain is not more sovereign. It is just a new way to lose access.

If you do take the job, being a little paranoid is appropriate. You should feel the weight. The goal is not fear. The goal is to build a process strong enough that you do not need to think about it every day.

### Your decision

Whether you want the whole job, part of it, or none of it right now.

### Homework

1. Write which parts of custody you are willing to own and which parts you want help carrying.
2. Name the one recovery or maintenance task you would need to prove before moving more Bitcoin into self-custody.
3. Match the answer to the custody level from the core module. Do not choose a more complicated setup than your household can operate.

You are done when the custody setup matches the responsibility you are actually willing to maintain, not the identity you want it to signal.
'''
advanced = replace_advanced_lesson(advanced, "A7.2", A7_2_MASTER)

# A8.1 is now part of the dictation package. It remains blocked from publication
# until estate-attorney review; it is no longer an intentionally unrecorded item.
advanced = re.sub(
    r"(?ms)^> ⬜ \*\*NO FILMING PLANNED.*?(?=\n\n)",
    "> 🎙 **SCRIPT PREPARED.** Dictation may be recorded; do not publish until the estate-attorney review is signed off in `LEGAL-REVIEW-PACKET.md`.",
    advanced,
)
advanced = advanced.replace(
    "> **Reference, not a capture.** This lesson is text-only for v1, so the steps\n> below are written for a reader working through the app on their own screen.",
    "> **Reference, not a separate screen capture.** The steps below are written for a reader working through the app on their own screen; the talking-head lesson can be recorded without an additional capture.",
)
advanced = advanced.replace(
    "Lesson numbers are kept from the core course during the migration and are\nrenumbered to A-numbers once the structure is final.\n\n",
    "",
)
write("MASTER-ADVANCED.md", advanced)

A4_SCRIPT = r'''TELEPROMPTER SCRIPT — segment A4.1
A4.1 The price context check: naming the emotion before a big move
~3 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
SOURCE: MASTER-ADVANCED.md · preserves the existing price-context decision
============================================================

This is a short check to run before any Bitcoin-heavy move.

A large buy, a sale to lock in gains, or a Bitcoin-backed loan can all be reasonable decisions. But the exact same decision can also be an emotional reaction to the last few months.

The point of this check is not to tell you whether to buy, sell, or borrow. It is to name what is in the room before you decide.

== TWO LOOKBACKS ==

Start with the recent window: 3, 6, 9, and 12 months.

That window tells you what you are feeling. If Bitcoin is up 40% in three months, there is probably some FOMO in the decision. If it is down 40%, there is probably fear.

You do not need to pretend either one is not there. You just need to name it.

Then zoom out to 2 to 5 years.

That window tells you what has actually happened over a meaningful period. It shows the direction of the trend instead of the mood of the last week.

The recent window names the emotion. The long window gives it context.

== PUT THE MOVE BACK AGAINST THE PLAN ==

Now describe the move without using today's price as the reason.

Why does it fit your allocation target, cash reserve, debt ceiling, tax plan, or retirement-income strategy? What problem is it solving? What would still make the decision reasonable if Bitcoin moved the other direction next month?

If you cannot explain it without saying that the price has been going up or going down, the price is probably doing more of the work than the plan is.

That does not automatically make the move wrong. It means you should wait a beat, open the owning page or scenario, and make sure the numbers support what the emotion wants to do.

== YOUR DECISION ==

Whether this move is the plan talking or the price talking.

== HOMEWORK ==

Write the move in one sentence without mentioning the recent Bitcoin price.

Then write what the 3-to-12-month window makes you feel and what the 2-to-5-year window shows.

Finally, open the owning plan page or scenario and confirm the move still makes sense against the rules you already set.

You are done when you can defend the move from the plan even if the last three months of price action were reversed.
'''
write("scripts/advanced/A4-1_the-price-context-check-naming-the-emoti.md", A4_SCRIPT)

A7_2_SCRIPT = r'''TELEPROMPTER SCRIPT — segment A7.2
A7.2 What self-custody actually asks of you
~3 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
SOURCE: MASTER-ADVANCED.md · preserves the existing custody-responsibility position
============================================================

A client put this better than I ever have.

He said that with self-custody, you are the point of failure. And you are not only the failure point. You are also the attack vector.

Then he made the point that most of life does not work this way. We outsource violence to the police. We outsource security to banks and other institutions. A big part of civilization is handing the hard and dangerous jobs to people whose job it is to carry them.

Bitcoin gives you the ability to take one of those jobs back.

That is why custody can feel heavier than the rest of a financial plan. It is not another investment checkbox. You are accepting a responsibility that somebody else carries for nearly every other asset you own.

== WHAT THE WHOLE JOB INCLUDES ==

The whole job is not just owning a hardware wallet.

It includes protecting the recovery material, keeping the process usable, testing that recovery works, maintaining the devices and software, noticing new single points of failure, and making sure somebody besides you can follow the process when your family needs it.

The device is one part. The ongoing responsibility is the job.

== THREE HONEST ANSWERS ==

The first honest answer is that you want the whole job. That can be the right choice when the amount, your skill, and your willingness to maintain it all line up.

The second answer is that you want part of it. That is what collaborative custody is for, and it is why a hardened institution can legitimately hold part of a stack. You keep some control and hand off some responsibility.

The third answer is that you do not want the job right now. That is also a real answer. Taking responsibility you will not maintain is not more sovereign. It is just a new way to lose access.

If you do take the job, being a little paranoid is appropriate. You should feel the weight. The goal is not fear. The goal is to build a process strong enough that you do not need to think about it every day.

== YOUR DECISION ==

Whether you want the whole job, part of it, or none of it right now.

== HOMEWORK ==

Write which parts of custody you are willing to own and which parts you want help carrying.

Name the one recovery or maintenance task you would need to prove before moving more Bitcoin into self-custody.

Then match the answer to the custody level from the core module. Do not choose a more complicated setup than your household can operate.

You are done when the setup matches the responsibility you are actually willing to maintain, not the identity you want it to signal.
'''
write("scripts/advanced/A7-2_what-self-custody-actually-asks-of-you.md", A7_2_SCRIPT)

A4_TEXT = r'''# The price context check: naming the emotion before a big move

**Watch this if:** you are about to make a Bitcoin-heavy move: a large buy, a sale to lock in gains, or a Bitcoin-backed loan. Your allocation decision is complete without it.

## The two lookbacks

- **Recent, 3 to 12 months:** names what you are feeling. A sharp rise can create FOMO; a sharp fall can create fear.
- **Long, 2 to 5 years:** shows the direction over a meaningful period rather than the mood of the last week.

The recent window names the emotion. The long window gives it context.

## Put the move back against the plan

Describe the move without using today's price as the reason. Explain which existing rule it fits: allocation, reserve, debt ceiling, tax plan, or retirement-income strategy.

A dramatic recent move does not automatically make the decision wrong. It is a reason to wait a beat and verify that the owning page or scenario supports it.

## Your decision

**Whether this move is the plan talking or the price talking.**

## Homework

1. Write the move in one sentence without mentioning recent price action.
2. Write what the recent window makes you feel and what the long window shows.
3. Verify the move against the owning plan page or scenario.

**Complete when:** you can defend the decision even if the last three months of price action were reversed.
'''
write("lesson-text/advanced/A4-1_the-price-context-check.md", A4_TEXT)

A7_2_TEXT = r'''# What self-custody actually asks of you

**Watch this if:** you are weighing whether you want the whole job of self-custody, or the weight of it is what has been stopping you. Your custody plan is complete without it.

## The job you are taking back

Self-custody makes you both the point of failure and a potential attack vector. Bitcoin gives you the ability to take back a responsibility that institutions carry for most other assets.

The whole job is more than owning a device. It includes protecting recovery material, testing recovery, maintaining the setup, finding new single points of failure, and making sure the family process works without you.

## Three honest answers

- **The whole job:** you hold and maintain the complete process.
- **Part of the job:** collaborative custody or a hardened institution carries part of the responsibility.
- **Not right now:** a legitimate answer when you will not maintain the process safely.

More responsibility is not automatically safer. The setup has to match what the household can actually operate.

## Your decision

**Whether you want the whole job, part of it, or none of it right now.**

## Homework

1. Write which custody responsibilities you will own and which you want help carrying.
2. Name the recovery or maintenance task you must prove before moving more Bitcoin.
3. Match the answer to the custody level from the core module.

**Complete when:** the setup matches the responsibility you will actually maintain.
'''
write("lesson-text/advanced/A7-2_what-self-custody-asks-of-you.md", A7_2_TEXT)

# ---------------------------------------------------------------------------
# Lock the Module 2 structure the user already approved: no major restructure,
# optional college at 2.4, walkthrough at 2.5.
# ---------------------------------------------------------------------------

core = read("MASTER-COURSE.md")
core = sub_once(
    core,
    r"(?ms)^> 🔴 \*\*FILMING BLOCKER \(F23\).*?(?=\n\*Find your real surplus)",
    "> ✅ **STRUCTURE LOCKED, 2026-08-25.** College remains optional at 2.4 and the module walkthrough remains 2.5. This preserves the existing course structure; the hand-off on the last required lesson works for students who correctly skip college.\n\n",
    "resolve F23 in master",
)

# Latest app behavior, verified against orange-plan main after PR #217.
core_replacements = [
    (
        "Routing pauses honestly, and you keep going.",
        "Current routing shows $0 for the month, while Reserve and Contributions settings stay editable. You can save the plan that begins when cash flow can support it.",
    ),
    (
        "If you're in deficit mode, the routing block is replaced by *\"This month has no surplus to allocate. Reserve settings stay editable and apply when surplus returns.\"*",
        "If you're in deficit mode, current routing shows $0. Reserve and Contributions settings stay editable, and planned contribution amounts remain saved for later modeled years when the waterfall has capacity.",
    ),
    (
        "The contribution rows only appear once the cash-flow pass from Module 2 has produced a surplus.",
        "Contribution rows remain editable even when current cash flow is negative. The page shows $0 routed now, while a saved planned amount can begin in a later modeled year when the waterfall has capacity.",
    ),
    (
        "Your surplus is routed into **Step 3** of the waterfall. The contribution rows only appear once the cash-flow pass from Module 2 has produced a surplus.",
        "The contribution settings are available even if current surplus is negative. A deficit month routes $0 now, but saved planned amounts can begin in later modeled years when the waterfall has capacity.",
    ),
]
for old, new in core_replacements:
    core = core.replace(old, new)

# Make transaction-source language conditional instead of claiming every source
# renders for every user.
core = core.replace(
    "There are four answers:\n\n1. **A linked account.** The app connects to your bank and brokerage and pulls transactions automatically.\n2. **A downloaded file.** Most exchanges and brokerages let you download a CSV or Excel export. Upload it and the app parses it.\n3. **Describe one transaction to AI.** Tell Orange Plan AI about a single purchase or sale in plain language. You review every field before it saves.\n4. **I'll enter them myself.** Add a purchase, sale, or transfer by hand. For accounts that don't support linking or a file export.",
    "There are up to four answers. **A linked account** appears only when Orange Plan has a supported linked investment source. The other paths are **a downloaded CSV or Excel file**, **describe one transaction to AI and review every field**, or **enter a purchase, sale, or transfer manually**.",
)
core = core.replace(
    "Four choices:\n\n| Choice | Sub-copy |",
    "Up to four choices. **A linked account** appears only when a supported linked investment source is available.\n\n| Choice | Sub-copy |",
)
write("MASTER-COURSE.md", core)

# Core capture sheets and student text: latest Cash Flow behavior and conditional
# linked-transaction source.
p = "scripts/02-5_WALKTHROUGH_cashflow-and-reserve.md"
text = read(p)
text = text.replace(
    '**⚠** Deficit mode reads *"Spending runs $X/mo ahead of income."* Not a failure. Routing pauses honestly and the module is the fix.',
    '**⚠** Deficit mode reads *"Spending runs $X/mo ahead of income."* Current routing is $0. Reserve and Contributions settings stay editable, so you can save the plan that begins when cash flow can support it.',
)
text = text.replace(
    '**⚠** Deficit mode replaces the routing block with *"This month has no surplus to allocate…"*',
    '**⚠** Deficit mode shows $0 routed now. Reserve and Contributions remain editable. Planned contribution amounts save as future targets and begin in modeled years where the waterfall has capacity.',
)
write(p, text)

p = "lesson-text/02-5_walkthrough-cashflow-reserve.md"
text = read(p)
text = text.replace(
    "1. **Read the verdict**: Cash Flow → This month. A deficit isn't failure; this module is the fix.",
    "1. **Read the verdict**: Cash Flow → This month. A deficit routes $0 now, but Reserve and Contributions stay editable so you can save future targets.",
)
text = text.replace(
    "8. **Read the waterfall order**: Reserve → Extra debt → Contributions (extra-debt amounts live on the Debt page).",
    "8. **Read the waterfall order**: Reserve → Extra debt → Contributions. In a deficit month, current routing is $0 while saved contribution targets can begin in later modeled surplus years.",
)
write(p, text)

p = "scripts/04-5_WALKTHROUGH_route-it.md"
text = read(p)
text = text.replace(
    "- [ ] Surplus routed into **Step 3** of the waterfall (contribution rows only appear with a surplus)",
    "- [ ] Contribution settings visible. A deficit demo is valid: rows remain editable while current routing reads $0",
)
text = text.replace(
    "**⚠** Missing account type → **+ Add account type** at the bottom.",
    "**⚠** Missing account type → **+ Add account type** at the bottom.\n\n**DEFICIT CHECK** If current cash flow is negative, save a planned amount anyway. The row shows $0 routed now, preserves the target, and the projection can fund it in a later surplus year after earlier waterfall steps.",
)
text = text.replace(
    "**⚠** Worth running when the surplus is real and you're stuck between two rungs.",
    "**⚠** Worth running when you are comparing planned amounts, even if the current month routes $0. Keep the distinction clear: planned target versus money available now.",
)
write(p, text)

p = "lesson-text/04-5_walkthrough-route-it.md"
text = read(p)
text = text.replace(
    "Follow along with the video (~20 minutes). Prerequisites: a salary income source entered for the 401(k) owner, and surplus routed into waterfall step 3.",
    "Follow along with the video (~20 minutes). Prerequisite: a salary income source for the 401(k) owner. Contribution settings remain editable in a deficit month; the row shows $0 routed now while the planned target stays saved for later surplus years.",
)
text = text.replace(
    "6. **Configure the 401(k) row**: mode **Fill to match**; enter both match fields; check \"captures $X/mo\" shows the full match.",
    "6. **Configure the 401(k) row**: mode **Fill to match**; enter both match fields. In a deficit month, save the target even though current routing is $0; it can begin when a later modeled year has capacity.",
)
write(p, text)

p = "scripts/01-4_WALKTHROUGH_module-1-set-up-and-verify.md"
text = read(p)
old = '''**SEE** Four choices:

1. A linked account
2. A downloaded CSV/Excel file
3. Describe one transaction to AI, then review every field
4. Enter a purchase, sale, or transfer manually'''
new = '''**SEE** Up to four choices:

1. A linked account, only when a supported linked investment source is available
2. A downloaded CSV/Excel file
3. Describe one transaction to AI, then review every field
4. Enter a purchase, sale, or transfer manually'''
text = replace_once(text, old, new, "Module 1 transaction choices")
write(p, text)

p = "lesson-text/01-5_walkthrough-baseline-lap.md"
text = read(p).replace(
    "3. Open **Update Transactions** and review the linked, file, AI-assisted, and manual paths.",
    "3. Open **Update Transactions** and review the file, AI-assisted, and manual paths. A linked-account path appears only when a supported linked investment source is available.",
)
write(p, text)

p = "scripts/09-3_WALKTHROUGH_annual-review-scenarios-report.md"
text = read(p)
text = text.replace(
    '**⚠** In deficit mode the routing block reads *"This month has no surplus to allocate…"* That\'s an honest read, and the pass still happened.',
    '**⚠** In deficit mode current routing is $0. Reserve and Contributions settings stay editable, and the pass still happened.',
)
text = text.replace(
    "**SEE** Four choices: A linked account · A downloaded file · Describe one transaction to AI · I'll enter them myself",
    "**SEE** Up to four choices. A linked account appears only when supported; file, AI-assisted, and manual entry remain available.",
)
write(p, text)

p = "lesson-text/09-3_walkthrough-annual-review-scenarios-report.md"
text = read(p)
text = text.replace(
    "1. **Cash Flow → This month**: read the surplus verdict; only actual changes get entered. Deficit months pause routing honestly; the pass still happened.",
    "1. **Cash Flow → This month**: read the surplus verdict; only actual changes get entered. A deficit month routes $0 now while Reserve and Contributions settings remain editable.",
)
text = text.replace(
    "2. **Enter transactions**: Dashboard → Update Transactions (four paths: linked account, file, describe to AI, manual). Nothing enters the plan without your review.",
    "2. **Enter transactions**: Dashboard → Update Transactions. File, AI-assisted, and manual paths are available; a linked-account path appears only when supported. Nothing enters the plan without review.",
)
write(p, text)

# ---------------------------------------------------------------------------
# Authority and handoff: resolve the structural F23 item, leave Austin's two
# genuine content decisions visible, and surface gate approval instead of hiding
# it in prose.
# ---------------------------------------------------------------------------

authority = read("AUTHORITY-FLAGS.md")
authority = sub_once(
    authority,
    r"(?ms)^### F23 .*?(?=^### F\d+ |^# |\Z)",
    r'''### F23 ✅ RESOLVED · Module 2 order stays 2.4 optional college, 2.5 walkthrough

Austin explicitly authorized the course-wide update without a major restructure. The existing order is now locked: lesson 2.4 is the optional college funding stack, lesson 2.5 is the walkthrough, and the hand-off stays on the last required teach lesson so a student who correctly skips college still reaches the walkthrough.

This is no longer a filming blocker.

''',
    "resolve authority F23",
)
authority = authority.replace(
    "### F7 · Gate conditions on seven advanced lessons",
    "### F7 · Advanced gate conditions — surfaced for Austin approval",
)
authority = authority.replace(
    "**Austin decides:** read the seven `> **Gate.**` lines in `MASTER-ADVANCED.md`\nand confirm or change them. They are all in one place for exactly this reason.",
    "**Austin decides:** review `ADVANCED-GATE-APPROVAL.md`, which now puts every live gate on one page with the owning lesson. This remains an approval item rather than a silent editorial decision, but it no longer requires hunting through the master.",
)
write("AUTHORITY-FLAGS.md", authority)

handoff = read("HANDOFF.md")
insert = r'''## Final dictation package — 2026-08-25

- Austin's original 0.2 / 1.1 / 1.2 source is preserved in `source-material/2026-08-25-module-0-1-dictation.md`, with every editorial change named in `DICTATION-SOURCE-MAP.md`.
- All 14 Advanced Library lessons now have a protected, spoken-ready script. A4.1 and A7.2 were the last generated drafts; both are now calibrated spoken prose with homework and a finish line.
- The Advanced Library now follows the same plan lifecycle as core: finish the owning core area first, then take the advanced lesson only when its gate applies.
- Module 2 structure is locked: optional college at 2.4, walkthrough at 2.5. F23 is resolved.
- The course is aligned to Orange Plan main after the contribution-before-surplus change: deficit months route $0 now while Reserve and Contributions settings remain editable and planned contribution targets can begin in later surplus years.
- `ADVANCED-DICTATION-ORDER.md`, `ADVANCED-GATE-APPROVAL.md`, `DICTATION-PICKUPS.md`, and `FINALIZATION-STATUS.md` are the production handoff. Do not start another general rewrite pass.

'''
if "## Final dictation package — 2026-08-25" not in handoff:
    handoff = handoff.replace("---\n\n## Where the project is", "---\n\n" + insert + "## Where the project is", 1)
handoff = re.sub(
    r"(?m)^3\. \*\*F23 · Module 2's ordering\.\*\*.*?(?=\n\n|\n\*\*)",
    "",
    handoff,
)
write("HANDOFF.md", handoff)

# ---------------------------------------------------------------------------
# Production generator: every Advanced lesson gets a dictation line. External
# review gates remain visible and do not get confused with editorial readiness.
# ---------------------------------------------------------------------------

producer = read("tools/build-production-checklist.py")
producer = producer.replace(
    "('Module 7', 'custody professional', 'filming',",
    "('Module 7 and advanced custody lessons A7.1–A7.4', 'custody professional', 'filming',",
)
producer = producer.replace(
    "out += ['', '## ☐ ADVANCED LIBRARY — text first, video in demand order', '',\n        '*Publish every advanced lesson as student-facing TEXT at launch. Film in this order afterwards.*', '']",
    "out += ['', '## ☐ ADVANCED LIBRARY — all 14 scripts prepared; dictate in demand order', '',\n        '*Every Advanced lesson has a protected teleprompter script. Review the status block before recording or publishing a professionally gated lesson.*', '']",
)
producer = sub_once(
    producer,
    r"DEMAND = \[[^\]]*\]",
    "DEMAND = ['A3.1', 'A6.1', 'A5.1', 'A7.1', 'A6.2', 'A5.2', 'A7.2', 'A1.1', 'A3.2', 'A4.1', 'A5.3', 'A7.3', 'A7.4', 'A8.1']",
    "advanced demand list",
    flags=re.S,
)
producer = producer.replace(
    "out.append(f'☐ {j}. {n} {m.group(1)} — 🎙 film (~{runtime.get(n, 0):.0f} min){flag}')",
    "out.append(f'☐ {j}. {n} {m.group(1)} — 🎙 dictate/film (~{runtime.get(n, 0):.0f} min){flag}')",
)
producer = producer.replace(
    "out.append(f'☐ — {m.group(1)} {m.group(2)} — TEXT ONLY for now{flag}')",
    "out.append(f'☐ — {m.group(1)} {m.group(2)} — ⚠ missing from dictation order{flag}')",
)
write("tools/build-production-checklist.py", producer)

# Files generated from the final masters/scripts by verify.py.
