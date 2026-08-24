#!/usr/bin/env python3
"""One-time tightening pass before Austin begins the Core voice review.

The changes are intentionally small: remove every current voice-lint warning,
make the review status honest, create a line-level hold register, and expand the
stale-output audit so the dictation packet cannot regress to retired numbers.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


def replace(path: str, old: str, new: str) -> None:
    content = read(path)
    count = content.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one exact match, found {count}: {old!r}")
    write(path, content.replace(old, new, 1))


def punctuate_lists(path: str) -> None:
    lines = read(path).splitlines()
    separator = next((index for index, line in enumerate(lines) if line.startswith("====")), 3)
    changed: list[str] = []
    for index, line in enumerate(lines):
        if index <= separator:
            changed.append(line)
            continue
        stripped = line.strip()
        is_list = bool(re.match(r"^(?:- |\d+\. )", stripped))
        if not is_list or not stripped:
            changed.append(line)
            continue
        if stripped.endswith(","):
            line = line[:-1] + "."
        elif stripped[-1] not in ".?!:;":
            line += "."
        changed.append(line)
    write(path, "\n".join(changed) + "\n")


# Natural first-person and app/demo anchors. These make abstract sections sound
# like Austin teaching a real planning decision rather than gaming a style score.
replace(
    "scripts/00-1_how-to-use-this-course.md",
    "Later, the walkthroughs use one continuous demo household and track the relevant Build Your Plan work in the app. They show the current screen, implement the decision, explain the resulting number, and return to the build flow.",
    "Later, the walkthroughs use one continuous demo household and track the relevant Build Your Plan work in the app. They show the current screen, implement the decision, explain the resulting number, and return to the build flow.\n\nIn our demo, the same household carries from the first baseline through the final report, so every decision has a visible downstream effect.",
)
replace(
    "scripts/00-2_how-the-ai-works-what-it-reads-what-it-n.md",
    "Orange Plan AI is an explanation layer for the financial plan. It is not a second calculator sitting beside it.",
    "I think of Orange Plan AI as an explanation layer for the financial plan. It is not a second calculator sitting beside it.",
)
replace(
    "scripts/02-3_fund-a-known-future-cost-the-six-questio.md",
    "Add the expected bill as a life event and identify the account or contribution route funding it.",
    "In Orange Plan, add the expected bill as a life event and identify the account or contribution route funding it.",
)
replace(
    "scripts/02-4_optional-college-is-a-funding-stack.md",
    "Do not begin with the published price of four years at a school the child may never attend.",
    "I would not begin with the published price of four years at a school the child may never attend.",
)
replace(
    "scripts/02-4_optional-college-is-a-funding-stack.md",
    "Model the household commitment as the life event, track the education savings and contribution route, and update the stack when the date and actual costs become clearer.",
    "In Orange Plan, model the household commitment as the life event, track the education savings and contribution route, and update the stack when the date and actual costs become clearer.",
)
replace(
    "scripts/04-2_break-your-accounts-down-by-holding-type.md",
    "Do not begin by guessing that Reserve should be 10%, Bridge 20%, and Legacy 70%.",
    "I would not begin by guessing that Reserve should be 10%, Bridge 20%, and Legacy 70%.",
)
replace(
    "scripts/04-2_break-your-accounts-down-by-holding-type.md",
    "Correct the holdings, review the combined current mix, and assign the Reserve, Bridge, Healthcare Bridge, and Legacy roles supported by the current Allocation page and account records.",
    "In Orange Plan, correct the holdings, review the combined current mix, and assign the Reserve, Bridge, Healthcare Bridge, and Legacy roles supported by the current Allocation page and account records.",
)
replace(
    "scripts/04-4_asset-location-which-account-each-holdin.md",
    "These are starting principles, not rules that automatically require a trade.",
    "I would treat these as starting principles, not rules that automatically require a trade.",
)
replace(
    "scripts/04-4_asset-location-which-account-each-holdin.md",
    "== RUN THE DEMO LOCATION ==\n\n- Reserve cash stays in the liquid taxable cash account.",
    "== RUN THE DEMO LOCATION ==\n\nIn our demo, the location choices are:\n\n- Reserve cash stays in the liquid taxable cash account.",
)
replace(
    "scripts/06-1_your-spending-income-floor-gap-and-bridg.md",
    "Do not reduce that to “everything unlocks at 59½.”",
    "I would not reduce that to “everything unlocks at 59½.”",
)
replace(
    "scripts/06-2_set-your-withdrawal-order-and-refill-rul.md",
    "I generally think about the pools this way:",
    "I think about the pools this way:",
)
replace(
    "scripts/07-2_set-up-a-hardware-wallet-and-test-recove.md",
    "A small practice wallet or spare device is often the better first test.",
    "I would rather use a small practice wallet or spare device for the first test.",
)
replace(
    "scripts/07-2_set-up-a-hardware-wallet-and-test-recove.md",
    "Orange Plan records status and date. The real custody process supplies the proof.",
    "In Orange Plan, the app records status and date. The real custody process supplies the proof.",
)
replace(
    "scripts/07-3_single-points-of-failure-account-hardeni.md",
    "Rank the top three by cost of loss, then fix the first one.",
    "I would rank the top three by cost of loss, then fix the first one.",
)
replace(
    "scripts/08-2_split-access-dual-control-and-redundancy.md",
    "Do not invent cryptography with scissors and envelopes.",
    "I would not invent a threshold with scissors and envelopes.",
)
replace(
    "scripts/08-2_split-access-dual-control-and-redundancy.md",
    "Record custody type, component roles at a process level, people, provider, configuration-record location, and test date in Protect and the Family Custody Map.",
    "In Orange Plan, record custody type, component roles at a process level, people, provider, configuration-record location, and test date in Protect and the Family Custody Map.",
)
replace(
    "scripts/08-3_the-heir-letter-and-the-dead-mans-switch.md",
    "Keep it short enough to follow.",
    "I would keep it short enough to follow.",
)
replace(
    "scripts/08-3_the-heir-letter-and-the-dead-mans-switch.md",
    "Create the no-secrets letter in Protect, verify recipients, record the storage plan, and decide whether automated delivery is an additional path.",
    "In Orange Plan, create the no-secrets letter in Protect, verify recipients, record the storage plan, and decide whether automated delivery is an additional path.",
)

for flagged in (
    "scripts/00-1_how-to-use-this-course.md",
    "scripts/04-1_set-the-bitcoin-allocation-you-can-hold.md",
    "scripts/04-3_order-your-contributions-which-account-g.md",
    "scripts/06-1_your-spending-income-floor-gap-and-bridg.md",
    "scripts/06-3_guardrails-how-much-you-can-spend-each-y.md",
    "scripts/08-3_the-heir-letter-and-the-dead-mans-switch.md",
):
    punctuate_lists(flagged)

# Austin can begin voice/judgment review now. UI and professional checks remain
# approval and filming gates rather than a reason to leave all 28 scripts idle.
replace(
    "CURRENT-COURSE.md",
    "**Austin's final voice-and-judgment read has not started.**",
    "**Austin's voice-and-judgment review is ready to begin. Final lesson approval still waits on each lesson's named UI or professional hold.**",
)
replace(
    "CURRENT-COURSE.md",
    "## Next work before Austin reads once\n\n1. Verify the reconciled candidate on the deployed pages and create eight final receipts.\n2. Send and apply the scoped external professional reviews.\n3. Use the deployed Build Your Plan flow end to end and record exact step metadata.\n4. Finalize visuals and walkthroughs from accepted receipts.\n5. Give Austin the scripts for one voice-and-judgment read.",
    "## Work that runs alongside Austin's review\n\n1. Austin reviews the current scripts in `DICTATION-ORDER.md` and dictates only voice or judgment changes.\n2. Verify the reconciled candidate on the deployed pages and create eight final receipts.\n3. Send and apply the scoped external professional reviews.\n4. Use the deployed Build Your Plan flow end to end and record exact step metadata.\n5. Finalize visuals and walkthroughs from accepted receipts.\n6. Clear each named hold, reconcile lesson text, and mark the corrected lesson `AUSTIN APPROVED` after one clean final read.",
)
replace(
    "AUSTIN-REVIEW-INDEX.md",
    "**Do not begin the final batch read yet.** The scripts are current, but the applicable UI receipt and external-review holds should be resolved first so Austin reads each lesson only once.",
    "**Begin the voice-and-judgment review now, using the wave order below.** Review the stable concept prose and dictate replacements where the wording or judgment is not yours. Do not mark a lesson `AUSTIN APPROVED` until its named UI or professional hold is cleared and the corrected lesson receives one clean final read.",
)
replace(
    "PRE-DICTATION-QA.md",
    "| Austin final voice review | **NOT STARTED** | Begins after applicable UI and professional holds are resolved |",
    "| Austin voice-and-judgment review | **READY TO BEGIN** | Review stable concept prose now; `AUSTIN APPROVED` still waits on each lesson's named UI or professional hold |",
)
replace(
    "PRE-DICTATION-QA.md",
    "## Definition of ready for Austin\n\nA lesson moves to Austin only when:\n\n- no known structural change remains,\n- every spoken demo value is an approved input or reconciled app result,\n- the deployed label/state has been checked where the lesson names the UI,\n- applicable external corrections are applied,\n- script and lesson text agree,\n- and contradictory slide material is already identified.",
    "## Definition of ready for Austin review\n\nA lesson can enter voice-and-judgment review when:\n\n- no known structural change remains,\n- every spoken demo value is an approved input or reconciled app result,\n- any unresolved UI or professional passage is named in the hold register rather than hidden,\n- script and lesson text agree on the decision and finish line,\n- and contradictory slide material is already identified.\n\nA lesson becomes `AUSTIN APPROVED` only after the deployed label/state and applicable external corrections are checked, the current script and lesson text are reconciled, and Austin completes one clean final read of that corrected lesson.",
)
replace(
    "FILMING-READINESS.md",
    "| Austin final voice/judgment review | HOLD |",
    "| Austin voice/judgment review | **AUSTIN — READY TO BEGIN**; final approval still waits on named UI/professional holds |",
)

# Make the stale-output audit cover the production review packet it previously
# missed. That old packet still carried retired $80k/$120k retirement figures.
replace(
    "tools/demo_output_stale_audit.py",
    "    ROOT / \"BUILD-YOUR-PLAN-CROSSWALK.md\",\n)",
    "    ROOT / \"BUILD-YOUR-PLAN-CROSSWALK.md\",\n    ROOT / \"DICTATION-ORDER.md\",\n    ROOT / \"AUSTIN-REVIEW-INDEX.md\",\n    ROOT / \"PRE-DICTATION-QA.md\",\n)",
)
replace(
    "tools/demo_output_stale_audit.py",
    "    \"BUILD-YOUR-PLAN-CROSSWALK.md\": (\"seven missions\", \"app_completion_rule\", \"human_completion_rule\"),\n}",
    "    \"BUILD-YOUR-PLAN-CROSSWALK.md\": (\"seven missions\", \"app_completion_rule\", \"human_completion_rule\"),\n    \"DICTATION-ORDER.md\": (\"25,\", \"94.6%\", \"$270,000\", \"$101,948\", \"0.079251 BTC\"),\n}\n",
)

hold_register = """# Austin review hold register

**Purpose:** let Austin review and dictate the stable Core now without confusing a pending product or professional check with a course-wide rewrite.

## Rule

Review the whole lesson for voice, judgment, example, and finish line. When a named hold appears, mark it `APP` or `PRO` and keep moving. Do not replace reconciled numbers from memory. A held line blocks `AUSTIN APPROVED` and filming, not the rest of the lesson's review.

## UI holds

| Lesson | Check before final approval | Stable review work that can happen now |
|---|---|---|
| 0.2 | Current AI privacy and optional-memory controls | Engine-versus-AI distinction and no-secrets rule |
| 1.2 | Saved / Previewing / Scenario labels | Baseline, life event, Scenario, and assumption distinctions |
| 1.3 | 94.6%, May 2032, household-retirement labels and rounding | Confidence interpretation and decision framing |
| 2.1 | $3,761 source rows and post-debt label | Normal/bare-bones spending and repeatable route |
| 2.2 | $30,000 / 6-month display | Reserve basis, months, and trade-off |
| 3.1 | DTI, DTA, and 2027 payoff display | Treatment for each debt and household ceiling |
| 4.1 | $270,000 denominator, excluded 529, and above-band state | Target, band, denominator, and drawdown judgment |
| 4.2 | Current account-job controls | Holding-versus-wrapper and timeframe-job explanation |
| 4.3 | $500 debt already inside Cash Flow and $3,500 account route | Next-dollar logic and no-double-counting explanation |
| 6.1 | First retirement-year need, income, and draw rows | Spending, phased floor, gap, and Bridge explanation |
| 6.2 | Account/holding source labels, projected BTC price, and units | Funding-strategy judgment and reconciliation method |
| 6.3 | Spending-card labels and annual-policy controls | $100,000 lifestyle decision and guardrail judgment |
| 9.1 | Current review/report/export states | Monthly, annual, and major-event cadence |
| 9.2 | 4% Scenario and report labels | Scenario discipline and finished-plan interpretation |

## Professional and real-world holds

| Lesson | Hold owner | Check before final approval |
|---|---|---|
| 4.4 | CPA / plan provider | Tax-location claims and provider implementation boundaries |
| 5.1 | CPA | Lot reconstruction, identification, and filing-grade execution language |
| 5.2 | CPA | Tax-window, Roth, RMD, state, and current-action wording |
| 6.2 | CPA | Tax ceiling and phase implementation |
| 7.1–7.3 | Custody practitioner + supported device/provider process | Recovery, authentication, failure-domain, and family-test wording |
| 8.1–8.3 | Colorado estate attorney + custody practitioner where applicable | Authority, documents, provider records, dual control, heir letter, and delivery |
| 8.4 | Licensed insurance professional | Coverage, tax, quote, contract, and self-insurance wording |

## What never waits on an external reviewer

- Austin's own planning judgment.
- Whether a sentence sounds like Austin.
- Whether the Alex and Jordan example helps.
- Whether a lesson owns one decision.
- Whether the learner can state the finish line.
- Removing repetition, filler, jargon, or a recommendation Austin does not believe.

## Final-clearance sequence

1. Apply the UI receipt or professional correction only to the named passage.
2. Reconcile the matching lesson text and visual brief.
3. Rerun all audits.
4. Austin reads the corrected lesson cleanly once.
5. Mark `AUSTIN APPROVED`.

Walkthroughs remain separate screen recordings and are not part of the 28-script dictation pass.
"""
write("AUSTIN-REVIEW-HOLD-REGISTER.md", hold_register)

print("Applied pre-review script tightening, readiness updates, and hold register.")
