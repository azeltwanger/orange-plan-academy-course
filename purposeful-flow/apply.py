#!/usr/bin/env python3
from __future__ import annotations

import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP_SHA = "b0888802cbe3fd3769816c9f1352b424bd4bff1c"


def clean(value: str) -> str:
    return textwrap.dedent(value).strip() + "\n"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, value: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(value.rstrip() + "\n", encoding="utf-8")


def replace_lesson(path: str, number: str, replacement: str, next_number: str | None = None) -> None:
    text = read(path)
    if next_number:
        pattern = re.compile(
            rf"(?ms)^## {re.escape(number)} [^\n]*\n.*?(?=^## {re.escape(next_number)} )"
        )
    else:
        pattern = re.compile(
            rf"(?ms)^## {re.escape(number)} [^\n]*\n.*?(?=^## A?\d+\.\d+ |^# Unit |^# Advanced Module |\Z)"
        )
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"{path}: expected one lesson {number}, found {len(matches)}")
    match = matches[0]
    write(path, text[:match.start()] + replacement.rstrip() + "\n\n" + text[match.end():])


def replace_block(path: str, pattern: str, replacement: str, label: str) -> None:
    text = read(path)
    updated, count = re.subn(pattern, replacement.rstrip(), text, count=1, flags=re.M | re.S)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match in {path}, found {count}")
    write(path, updated)


def to_master_body(script_body: str) -> str:
    lines: list[str] = []
    for line in script_body.strip().splitlines():
        match = re.match(r"^== (.+) ==$", line)
        if match:
            title = match.group(1).strip().capitalize()
            lines.append(f"### {title}")
        else:
            lines.append(line)
    return "\n".join(lines).strip()


SOURCE = clean(r'''
# Austin source material — purposeful pre-dictation course flow

**Received:** 2026-08-26
**Source:** Austin's direct course-revision instructions

## Exact direction

> No I want you to do a pass before I dictate so it's easier to dictate and not all copywriting slop so dictation is faster and easier.

> Am I reading this or are we doing this in the walkthrough? Need a clean segue like, "I will show you exactly how to enter it during the walkthrough lesson."

> A trend I'm noticing is filler copywriting speak and not helpful advice driving someone to a decision. Each lesson needs to be in my voice and purposeful, explaining the concepts.

> This section is more about life events for your plan, future cash flow awareness and planning, how to add life events to the plan, and how they work.

> We completely missed how to direct flows and investments with surplus. Need to walk someone through how to do this.

> Be mindful about the best course flow for teaching, and our current app because some of this may be slightly different.

## Course decisions captured

1. The existing editor-shaped teleprompter scripts are research references until Austin dictates them.
2. Teach lessons explain the concept and the decision. The module walkthrough performs the data entry and click path.
3. Core lessons do not have to speak the same "Your decision / Put it in Orange Plan / You are done when" template.
4. Module 2 owns current cash flow, reserve sizing, and expected future life events.
5. A future purchase financed with debt is entered as a future event; Module 3 owns the debt policy and whether the obligation is acceptable.
6. Module 4 must explicitly connect surplus to contribution accounts and then to the investments purchased inside those accounts.
7. Current app behavior is verified before course wording is changed.
''')
write("source-material/2026-08-26-purposeful-course-flow.md", SOURCE)

COURSE_FLOW_AUDIT = clean(f'''
# Course flow audit against the current Orange Plan app

**Verified app:** `azeltwanger/orange-plan` production `main` at `{APP_SHA}`

## What the app actually does

### Build Your Plan

- **Foundation:** personal details, real accounts, and real holdings.
- **Cash flow:** income, living expenses, reserve target, and expected life events.
- **Debt:** current debts and the debt-strategy review.
- **Allocation:** account timeframes, target mix, and allocation review.
- **Tax, retirement income, Protect, and Run your plan** follow afterward.

The current Build Your Plan rail does **not** have a separate completion task for contribution routing. That is an app-tracking gap, not a reason to omit the work from the course.

### Cash Flow

The Cash Flow page calculates current surplus from income, taxes, living expenses, and debt payments. The waterfall then applies the available amount in this order:

1. Cash reserve
2. Extra debt payments saved on the Debt page
3. Contribution rows

Contribution rows can be added by account type. Depending on the row, the app supports:

- **Custom $/mo**
- **Fill to match**
- **Max**
- **Leftover** or **Fixed** for taxable
- Traditional, Roth, or split treatment where supported
- **Current mix**, **Set mix**, or **Choose holdings** for what the contribution buys

The app caps the amount actually routed when requested contributions exceed available surplus.

### Life events

The current Life Events editor can model expected future changes in:

- income and business income
- recurring or one-time spending
- family and college costs
- home purchases, sales, and relocation
- new debt
- windfalls, inheritances, and asset sales
- pensions, Social Security, and sabbaticals

The course should not read every event type. It should teach the inputs that make an event useful: what changes, when it changes, how much, how long it lasts, whether the amount should inflate, and how the household expects to fund it.

## Best teaching flow

### Module 1 — Foundation

Replace rough onboarding data with real accounts, holdings, and assumptions.

### Module 2 — Cash flow, reserve, and expected changes

1. Find true surplus and normal/bare-bones spending.
2. Set the reserve policy.
3. Add expected future income and spending changes as life events.
4. Use the walkthrough to enter and verify those items.

Module 2 identifies the surplus. It does not finish directing every investment dollar.

### Module 3 — Debt

Enter current debts, decide what each debt is doing, and save any extra-payment strategy. If a future event creates a new loan, the event records the future obligation; this module supplies the debt policy used to judge it.

### Module 4 — Allocation and directing surplus

1. Set the target mix.
2. Give accounts and holdings a timeframe.
3. Decide how the remaining surplus is divided among contribution account types.
4. Decide what each account's new contributions buy.
5. Use the walkthrough to configure the actual contribution rows and verify the applied total does not exceed available surplus.

## Product gap to keep visible

The course now treats contribution routing as required Module 4 work even though Build Your Plan currently marks Allocation complete from timeframes and target mix alone. A future app change should add a contribution-plan task or an equivalent review state.
''')
write("COURSE-FLOW-AUDIT.md", COURSE_FLOW_AUDIT)

# -------------------------------------------------------------------------
# 2.2 — remove duplicated app instructions from the spoken lesson.
# -------------------------------------------------------------------------
reserve_path = "scripts/02-2_size-your-cash-reserve-in-months-of-spen.md"
reserve = read(reserve_path)
reserve_close = clean(r'''
== BEFORE THE WALKTHROUGH ==

For now, write down your bare-bones spending and the number of months you want to hold. In the walkthrough for this module, I'll show you exactly where to enter both numbers in Orange Plan, how the app calculates the reserve target, and how to compare that target with the cash you already have.

You're finished with this lesson when those two numbers are written down and you can explain what the reserve is protecting you from: having a bad month force you to sell Bitcoin at the wrong time.
''')
reserve, count = re.subn(
    r"(?ms)^== (?:YOUR DECISION|PUT IT IN ORANGE PLAN|BEFORE THE WALKTHROUGH) ==\n.*\Z",
    reserve_close,
    reserve,
    count=1,
)
if count != 1:
    raise RuntimeError(f"2.2 close: expected one replace, found {count}")
write(reserve_path, reserve)

# -------------------------------------------------------------------------
# 2.3 — life events and future cash-flow planning, not a rigid lane lecture.
# -------------------------------------------------------------------------
SCRIPT_23_BODY = clean(r'''
In today's lesson, we're going to cover the future changes that need to be in your plan so Orange Plan is not projecting today's income and spending forever.

Your Cash Flow page starts with what is true right now. If you make $150,000 and spend $80,000 today, the projection needs a starting point, so it carries those numbers forward using the assumptions in the plan.

But real life is not going to stay exactly the same. You might change jobs, take a sabbatical, buy a house, replace a car, have a child, help pay for college, receive an inheritance, or take on a new loan. If you have a good reason to expect one of those changes and it is large enough to affect the plan, it belongs in Life Events.

== WHAT COUNTS AS A LIFE EVENT ==

A life event is a future change you genuinely expect to happen. It can change income, spending, assets, debt, taxes, or the timing of when money becomes available.

The key word is expect. If you are reasonably confident that you are going to replace a car in 5 years, that belongs in the plan. If you are only asking what would happen if you bought a much larger house someday, that is a scenario. It stays separate so the hypothetical does not quietly become part of your baseline.

This is the same distinction we covered in the Foundation module. Life Events are expected changes. Scenarios are questions.

== WHAT YOU NEED TO DECIDE ==

Before you enter an event, write down 5 things.

First, what is actually changing? Is income going up or down? Is this a one-time purchase? Is it a new annual expense? Is an asset being sold? Is a loan being added?

Second, when does it start? A cost next year affects the plan very differently from the same cost 12 years from now.

Third, is it one time or recurring? If it repeats, how long does it last? College may last 4 years. Childcare may last several years. A raise may continue for the rest of the projection.

Fourth, what amount are you actually planning around? Use the amount you genuinely expect to be responsible for, not the largest possible sticker price you can find.

Fifth, how do you expect to pay for it? The answer could be future cash flow, money already set aside, a planned asset sale, financing, or some combination of them.

== WHERE DEBT FITS ==

Debt is one possible funding source, so it cannot disappear from this conversation.

Let's say you plan to buy a $40,000 vehicle in 5 years and expect to put $10,000 down and finance the rest. The plan needs the purchase and the future loan terms. Otherwise it either assumes you paid the whole $40,000 in cash or ignores the future payment.

This lesson is not deciding whether that loan is a good idea. The Debt module is where you decide what level of debt you are comfortable with, which rates you would accept, and what job a loan has in the plan. Life Events makes sure the future obligation actually exists in the projection.

== WHERE BITCOIN FITS ==

A future expense needs an intentional funding plan. It does not automatically need to be fully funded before you keep buying Bitcoin or working on every other goal.

Bitcoin can remain part of the funding plan 5 years out. I would not automatically move the entire future expense into cash at that point. But the closer you get to the date, the less the amount you have firmly committed should depend on Bitcoin being at a favorable price.

The flexible portion can stay exposed longer. The amount you absolutely cannot come up short on should gradually move toward a funding source you can rely on. I am not giving one fixed percentage for every household because the right answer depends on how flexible the date and the amount actually are.

== WHY THIS CHANGES THE PLAN ==

Once a life event is saved, Orange Plan can change the projected cash flow in the correct years. That can move the retirement date, change how much needs to be saved, create a future debt payment, change taxes, or show that a cost is already covered by future income.

This is why I do not want you to treat Life Events like a list of dreams. Add the changes you have a real reason to expect. Test the uncertain ideas later in Scenarios.

== BEFORE THE WALKTHROUGH ==

Make a short list of the future income and spending changes you already know about. For each one, write the timing, amount, duration, and likely funding source.

In the walkthrough for this module, I'll show you exactly how to add those events, how one-time and recurring events work, where a future loan is entered, and how to keep a hypothetical question out of your baseline plan.
''')

SCRIPT_23 = clean(f'''
TELEPROMPTER SCRIPT — segment 2.3
2.3 Plan for future income, expenses, and life events
~7 min at 155 wpm · DICTATION-READY WORKING DRAFT — NOT YET AUSTIN DICTATION
APP VERIFIED: production main {APP_SHA}
SOURCE: source-material/2026-08-26-purposeful-course-flow.md
============================================================

{SCRIPT_23_BODY}
''')
write("scripts/02-3_fund-a-known-future-cost-the-six-questio.md", SCRIPT_23)

MASTER_23 = clean(f'''
## 2.3 Plan for future income, expenses, and life events
*`TEACH` · ~{len(SCRIPT_23_BODY.split()):,} words · ~{len(SCRIPT_23_BODY.split())/155:.0f} min*

**By the end of this lesson, you can:**

- Decide which future changes belong in Life Events instead of Scenarios
- Describe an event by its timing, amount, duration, inflation treatment, and funding source
- Include a future loan without confusing event entry with debt strategy
- Explain how much of a future cost can still depend on Bitcoin as the date approaches

---

{to_master_body(SCRIPT_23_BODY)}
''')
replace_lesson("MASTER-COURSE.md", "2.3", MASTER_23, "2.4")

LESSON_23 = clean(r'''
# Plan for future income, expenses, and life events

Orange Plan starts from today's cash flow and projects it forward. Life Events tell the plan where you reasonably expect that cash flow, an asset, or a debt to change.

## Life event or scenario?

| Use Life Events when… | Use Scenarios when… |
|---|---|
| You genuinely expect the change | You are testing a possibility |
| The event belongs in the plan of record | You do not want the baseline changed |
| You can estimate timing and amount | The question is still exploratory |

Examples of expected events include a raise, sabbatical, large purchase, home purchase or sale, child costs, college, a new loan, inheritance, asset sale, or relocation.

## Information to decide before entry

1. **What changes?** Income, spending, asset, debt, tax jurisdiction, or another plan input.
2. **When?** The start age or date.
3. **How long?** One time, recurring, or a fixed duration.
4. **How much?** The amount you genuinely expect to be responsible for.
5. **Inflation treatment:** whether the amount is stated in today's dollars or as a future nominal amount.
6. **Funding source:** future cash flow, money already saved, an asset sale, financing, or a combination.

## Debt and future purchases

A future purchase can include a new loan. Entering the future obligation makes the projection include its down payment and payments. The Debt module separately decides whether the future debt fits the household's debt policy.

## Bitcoin and a future cost

**A future expense needs an intentional funding plan. It does not automatically need to be fully funded before every other goal.**

**Bitcoin can remain part of the funding plan 5 years out.** As the date approaches, the firmly committed amount should become less dependent on Bitcoin's price. No fixed Bitcoin percentage applies to every event.

## App reference

The walkthrough demonstrates **Plan → Retirement → Life events → Add event**. The editor groups events into Income, Spending, Family, Housing, Debt, Assets, and Retirement. Add expected changes here; keep hypothetical questions in Scenarios.

## Complete when

Every material expected change has a timing, amount, duration, and likely funding source, or you have truthfully selected **Nothing major coming** in Build Your Plan.
''')
write("lesson-text/02-3_fund-a-known-future-cost-the-six-questio.md", LESSON_23)

VISUAL_23 = clean(r'''
# 2.3 · How a life event changes the plan

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious

A life event is an expected future change, not a hypothetical scenario. It enters the timeline once and then changes future income, spending, assets, debt, or taxes in the years where it applies.

## The visual

A simple left-to-right flow with 4 cards:

1. **Expected change** — example: vehicle in 5 years
2. **Event details** — date, amount, one-time/recurring, duration, inflation
3. **Funding plan** — future cash flow, saved cash, Bitcoin/asset sale, financing, or a mix
4. **Projection changes** — future cash flow, debt payment, taxes, retirement date

Below the flow, show a small split:

- **Life event:** reasonably expected; becomes part of the plan
- **Scenario:** a question; stays separate

## Bitcoin callout

Use the exact line: **Bitcoin can remain part of the funding plan 5 years out.** Show the firmly committed amount becoming less Bitcoin-dependent as the date approaches. Do not show a fixed percentage or an automatic all-cash cutoff.

## Debt callout

A future loan belongs in the event so the projection includes it. The Debt module decides whether the obligation fits the household's debt policy.
''')
write("visuals/2-3_cost-lanes.md", VISUAL_23)

# -------------------------------------------------------------------------
# 2.5 — current-app walkthrough for cash flow, reserve, and life events.
# -------------------------------------------------------------------------
WALK_25 = clean(r'''
# 2.5 · WALKTHROUGH — Build cash flow, reserve, and life events

**Screen capture · 10 steps · ~16 min**

> **DO** = click path · **SEE** = point at this · **⚠** = don't get this wrong
> Narrate in your own words. Nothing here is a teleprompter script.

## Before you record

- [ ] 2–3 months of categorized transactions linked or imported
- [ ] Bare-bones card: **$5,000/mo · 6 months**
- [ ] One expected life event ready to enter, including date, amount, duration, and funding source
- [ ] Clean browser and no personal data on screen

---

## □ 1 · Read current surplus

**DO** Cash Flow → **This month**

**SEE** Income minus taxes, living expenses, and debt payments. The remaining amount is what can move through the waterfall.

**⚠** A deficit shows $0 available now. Reserve and contribution settings can still hold a future plan, but do not pretend money is currently being routed.

---

## □ 2 · Enter each income source

**DO** Open **Income** under Breakdown → **+ Add income source**

**SEE** One row per earner or recurring source. Use the correct income type because taxes differ.

**⚠** If a source type is missing from the menu, check whether it is already on the list.

---

## □ 3 · Enter living expenses

**DO** Open **Living** under Breakdown and enter the normal monthly amount or categories.

**SEE** Living is separate from taxes and debt payments.

**⚠** Do not put the paycheck in Living. Do not add current loan payments twice. Current debts are entered and reviewed in Module 3.

---

## □ 4 · Verify spending against real transactions

**DO** Verify Spending → **Review** → **By month**

**SEE** Linked or imported spending compared with the number saved in the plan.

**DO** Review at least 2 normal months. Exclude a genuine one-time item rather than lowering the plan to hide it.

**⚠** A missing spending account can make the average look falsely low.

---

## □ 5 · Set the reserve policy

**DO** Reserve settings

Set, in the current render order:

1. **Target months**
2. **Reserve basis** — Current spending or Bare-bones
3. **Monthly build cap**
4. **Bare-bones essentials** when that basis is selected

**SEE** Orange Plan calculates the reserve target from the selected monthly basis and target months.

**⚠** The teach lesson chooses the two numbers. This walkthrough performs the entry.

---

## □ 6 · Read and protect the reserve

**SEE** Step 1 of Routing: current reserve, target, and estimated time to fund it.

**DO** On Dashboard, add a Shield to the exact cash holding used as the emergency reserve.

**⚠** The Shield identifies the holding. It does not create cash or change the target.

---

## □ 7 · Add one expected life event

**DO** Plan → Retirement → **Life events** → **Add event**

**SEE** Current categories: Income, Spending, Family, Housing, Debt, Assets, and Retirement.

Choose an event that genuinely belongs in the baseline. Enter:

- start age or date
- amount
- one-time or recurring treatment
- duration when applicable
- inflation treatment when offered
- the event-specific funding or destination fields

**DEBT EXAMPLE** A future home or vehicle purchase can include a down payment, loan amount, rate, and term. Entering the event makes the future obligation exist in the projection. Module 3 owns the debt policy; do not re-teach it here.

---

## □ 8 · Keep scenarios separate

**DO** Save the event and point to the years it changes.

**SAY** Expected changes belong in Life Events. A question such as “What if we buy a much larger house?” belongs in Scenarios until the household decides it is actually part of the plan.

**⚠** Do not change the baseline merely to test an idea.

---

## □ 9 · Explain where the rest of the surplus gets handled

**DO** Return to Cash Flow → Routing.

**SEE** The 3 claims on surplus:

1. **Cash reserve** — configured in this module
2. **Extra debt** — decided and entered in Module 3
3. **Contributions** — account amounts and investments configured in Module 4

**SAY** This module proves the surplus and sets the reserve. Module 4 is where the remaining amount is directed into actual account types and investments.

---

## □ 10 · Confirm Build Your Plan

**DO** Build Your Plan → Cash flow

Confirm:

- income is entered
- living expenses are entered
- reserve target is set
- expected life events are entered, or **Nothing major coming** is selected truthfully

Optional: run **Review Cash Flow & Reserve** after the entries are complete.

**END**
''')
write("scripts/02-5_WALKTHROUGH_cashflow-and-reserve.md", WALK_25)

# -------------------------------------------------------------------------
# 4.3 — replace strict waterfall slop with the actual unresolved decision
# and the current app's three-part contribution model.
# -------------------------------------------------------------------------
SCRIPT_43_BODY = clean(r'''
In today's lesson, we're going to connect the surplus you found in Cash Flow to the actual accounts and investments that are going to receive the money.

By this point, 3 things are already known. You know how much monthly surplus is real. You know the reserve and debt rules that get first claim on it. And you have a target allocation and timeframes for what the portfolio is supposed to do.

The contribution plan has to connect all 3.

== THE 3 QUESTIONS FOR EACH DOLLAR ==

The first question is what job the money has. Is it finishing the reserve, paying extra toward a debt, funding a known Bridge need, or building long-term wealth?

The second question is which account or tax wrapper should receive it. That might be a 401(k), HSA, Roth IRA, traditional account, 529, taxable brokerage, or personally held Bitcoin.

The third question is what the account is going to buy. The account name does not answer that. A 401(k) contribution can buy stocks, bonds, cash, or another available holding. A taxable contribution can buy Bitcoin, stocks, or a mix.

So the complete instruction is not “put $1,000 into the 401(k).” It is “put $1,000 into the 401(k), use this tax treatment, and invest it this way.”

== THE DEFAULT ORDER STILL NEEDS AUSTIN'S RULE ==

🔴 HOLD FOR AUSTIN DICTATION — F22

The final lesson still needs Austin's exact answer for:

1. the normal default order;
2. the items that usually come first;
3. the conditions that override that order;
4. how taxable Bridge savings, taxable Bitcoin, HSA, Roth, and traditional accounts are compared; and
5. when deliberately splitting the available amount is the right answer.

The client-call evidence rules out the old strict instruction that every earlier account must be maxed before any later account receives a dollar. The final rule is a default with named overrides, not an inflexible ladder.

== WHAT THE APP CURRENTLY LETS YOU SET ==

Orange Plan does not ask you to drag account rows into a custom order. It asks you to configure the account types you actually use.

For most retirement-account rows, the contribution mode can be Custom dollars per month, Fill to match, or Max. Taxable can take the leftover after the earlier fixed requests, or a fixed amount.

Where the account supports it, you can also choose Traditional, Roth, or a split.

Then every row has an investment instruction: keep the account's current mix, set an asset-class mix, or choose the specific holdings that new contributions buy.

If the requested amounts exceed the surplus available after reserve and debt, the app limits the amount actually applied. That is why the walkthrough has to end by reconciling what you requested with what can really be funded.

== DELIBERATE SPLITTING ==

More than one destination can be valid at the same time. A household may need taxable Bridge money for early-retirement access while also wanting the current tax deduction from a traditional contribution. Another household may capture a match and direct the rest toward taxable Bitcoin.

A split is not automatically indecision. It needs a reason attached to each side and the total still has to fit inside the surplus.

== BEFORE THE WALKTHROUGH ==

Write down every account type you can contribute to, the employer match rules, the current reserve and debt claims, the amount of taxable money needed before retirement-account access, and which investments are actually available inside each account.

During the Module 4 walkthrough, I'll show you how to add the contribution rows, set the monthly amount or mode, choose tax treatment where the app supports it, direct what each account buys, and verify that the applied total matches the surplus available.
''')

SCRIPT_43 = clean(f'''
TELEPROMPTER SCRIPT — segment 4.3
4.3 Direct your surplus: choose the account and what it buys
~6 min at 155 wpm · DICTATION-READY STRUCTURE — AUSTIN RULE STILL REQUIRED

🔴 HOLD FOR REDICTATION — DO NOT FILM AS FINAL (F22)
APP VERIFIED: production main {APP_SHA}
SOURCE: source-material/2026-08-26-purposeful-course-flow.md
============================================================

{SCRIPT_43_BODY}
''')
write("scripts/04-3_order-your-contributions-which-account-g.md", SCRIPT_43)

MASTER_43 = clean(f'''
## 4.3 Direct your surplus: choose the account and what it buys
*`TEACH` · ~{len(SCRIPT_43_BODY.split()):,} words · ~{len(SCRIPT_43_BODY.split())/155:.0f} min*

> 🔴 **F22 — Austin dictation still required.** The app mechanics and teaching flow are verified. Austin's default order, overrides, and deliberate-split rule remain the only missing planning judgment.

**By the end of this lesson, you can:**

- Separate the money's job, account wrapper, and investment instruction
- Compare contribution destinations without assuming every tax-advantaged account must be maxed first
- Understand the current contribution modes and investment-routing controls in Orange Plan
- Reconcile planned contributions with the surplus actually available

---

{to_master_body(SCRIPT_43_BODY)}
''')
replace_lesson("MASTER-COURSE.md", "4.3", MASTER_43, "4.4")

LESSON_43 = clean(r'''
# Direct your surplus: choose the account and what it buys

> 🔴 **Austin dictation still required for the default order, overrides, and deliberate-split rule.** The app mechanics below are current.

A complete contribution instruction answers 3 questions:

1. **What job does the money have?** Reserve, extra debt, Bridge, or long-term growth.
2. **Which account receives it?** 401(k), HSA, Roth IRA, traditional account, 529, taxable, or personally held Bitcoin.
3. **What does that account buy?** Current mix, an asset-class mix, or specific holdings.

## Current app controls

| Control | Current choices |
|---|---|
| Contribution mode | Custom $/mo, Fill to match, Max; taxable uses Leftover or Fixed |
| Tax treatment | Traditional, Roth, or split where supported |
| How it invests | Current mix, Set mix, Choose holdings |
| Surplus limit | Requested contributions are capped by the amount available after reserve and extra debt |

## The rule Austin still needs to dictate

- normal default order
- strong priorities that usually come first
- facts that override the default
- how taxable Bridge, taxable Bitcoin, HSA, Roth, and traditional accounts compare
- when a deliberate split is correct

The prior strict rule—max every earlier rung before a later destination receives anything—is retired.

## Walkthrough handoff

The Module 4 walkthrough adds the actual account types, chooses each mode and amount, selects the investments, and reconciles the total with available surplus.
''')
write("lesson-text/04-3_order-your-contributions-which-account-g.md", LESSON_43)

VISUAL_43 = clean(r'''
# 4.3 · One surplus, 3 decisions

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious

Directing surplus is not only an account-order decision. Each dollar needs a job, an account wrapper, and an investment instruction.

## The visual

One monthly-surplus card flows through 3 side-by-side decisions:

1. **Job** — Reserve · extra debt · Bridge · long-term growth
2. **Account** — 401(k) · HSA · Roth · traditional · taxable · 529
3. **Investment** — current mix · asset-class mix · specific holdings, including Bitcoin where available

Below the 3 cards, show one reconciliation bar:

**Available after Reserve and Debt** versus **Requested contributions** versus **Applied contributions**.

If requested exceeds available, the applied bar stops at available and is labeled **limited by available surplus**.

## Do not show

- A mandatory six-rung ladder
- Every earlier account maxed before any later account
- One universal ordering that ignores taxable Bridge needs, Bitcoin access, current tax rate, or household liquidity

## Producer note

F22 still needs Austin's default order, named overrides, and deliberate-split rule. This visual can be finalized after that dictation without changing its 3-decision structure.
''')
write("visuals/4-3_contribution-waterfall.md", VISUAL_43)

# -------------------------------------------------------------------------
# 4.5 — show the end-to-end surplus → account → investment flow in the
# current app.
# -------------------------------------------------------------------------
WALK_45 = clean(r'''
# 4.5 · WALKTHROUGH — Direct surplus into accounts and investments

**Screen capture · 12 steps · ~20 min**

> **DO** = click path · **SEE** = point at this · **⚠** = don't get this wrong
> Narrate in your own words. Nothing here is a teleprompter script.

## Before you record

- [ ] Cash Flow shows a believable monthly surplus
- [ ] Reserve target and monthly build cap are saved
- [ ] Any extra-debt strategy is saved on the Debt page
- [ ] Salary income and employer match details are available for the 401(k) example
- [ ] At least one taxable account or Bitcoin holding exists for the taxable example
- [ ] Target mix and account timeframes are ready to set

---

## □ 1 · Start with the amount that can actually be routed

**DO** Cash Flow → This month

**SEE** Current surplus before the waterfall.

**SAY** This number came from Module 2. Do not create a contribution plan from gross income or a hoped-for surplus.

---

## □ 2 · Read the claims ahead of contributions

**DO** Cash Flow → Routing

**SEE**

1. Cash reserve
2. Extra debt
3. Contributions

**SAY** The contribution pool is what remains after the first 2 saved policies. Module 4 does not re-decide the reserve or debt strategy.

---

## □ 3 · Confirm account timeframes

**DO** Strategy → Allocation → Funding your timeframes → **Assign accounts**

Assign accounts to Reserve, Bridge, or Legacy based on the job they perform.

**⚠** The app may infer a default. Confirm or change it. A Funded or Behind badge is information, not an automatic order to direct every new dollar there.

---

## □ 4 · Save the target mix

**DO** Allocation → Your target mix → Edit targets

**SEE** Percentages must total 100%, plus the saved drift band.

**SAY** The target describes the portfolio you are trying to build. The contribution rows determine how new money moves toward it.

---

## □ 5 · Open the contribution plan

**DO** Cash Flow → Routing → Step 3 **Contributions**

**DO** **+ Add account type** for each account type the household can actually fund.

Examples: 401(k), Roth IRA, HSA, 529, taxable.

**⚠** These are contribution account types, not a second list of the user's current balances.

---

## □ 6 · Set the amount or mode on each row

Open each contribution row.

Current choices:

- **Custom $/mo**
- **Fill to match** when salary and match terms are available
- **Max** when the app has a current limit for that account type
- Taxable: **Leftover** or **Fixed**

**SEE** The row shows requested monthly amount and applied monthly amount.

**⚠** Annual limits and match calculations are app inputs, not numbers to memorize in the video.

---

## □ 7 · Complete the employer-match example

**DO** 401(k) → Fill to match

Enter the match rate and the percent of pay the employer matches up to.

**SEE** The calculated annual target and captured match.

**⚠** If Fill to match is disabled, read the missing prerequisite shown by the app: salary income or match details.

---

## □ 8 · Choose tax treatment where supported

**DO** On the employer-plan row, choose Traditional, Roth, or Split.

**SAY** This is the tax-wrapper decision. It is separate from what the contribution buys.

**⚠** Do not present one treatment as universal. The tax module supplies the bracket and lifetime-tax comparison.

---

## □ 9 · Tell each account what to buy

**DO** Open **How it invests**.

Current choices:

- **Current mix** — new money follows the account's saved mix
- **Set mix** — enter Bitcoin, stocks, bonds, cash, and other percentages totaling 100%
- **Choose holdings** — route to eligible existing holdings, asset classes, or a new security supported by the editor

Use 2 examples:

1. A 401(k) with a stock/bond or available Bitcoin-exposure mix
2. Taxable set to Leftover and directed toward the intended taxable holding, such as personally held Bitcoin or a taxable Bridge mix

**⚠** “401(k)” answers where the money goes. “Bitcoin / stocks / bonds” answers what it buys. Show both.

---

## □ 10 · Demonstrate a deliberate split

Use Custom amounts on 2 valid destinations so the viewer can see that the plan can fund more than one need.

Example structure only: employer match plus taxable Bridge or Bitcoin. Do not present the example split as the universal F22 rule.

**SEE** Each row has its own reason, amount, and investment instruction.

---

## □ 11 · Reconcile requested and applied amounts

**SEE** Any row labeled **limited by available surplus**.

Add the applied contribution rows and compare them with the contribution pool after Reserve and Extra debt.

**SAY** The saved targets can be higher than today's available amount, but the app only applies what the waterfall can fund. Planned and currently applied are not the same number.

**⚠** If the contribution plan has an unexplained leftover, either assign taxable to Leftover or make an intentional decision to leave cash unallocated.

---

## □ 12 · Confirm the full flow

Read the complete chain on screen:

**Income → taxes/living/debt → surplus → reserve → extra debt → contribution account → investment holding.**

Optional: run **Route with AI** to compare the current amount with a different planned amount, then use a saved Scenario to test the result.

**PRODUCER NOTE** Build Your Plan currently checks timeframes and target mix but does not have a separate contribution-plan checkbox. The course still treats this walkthrough as required Module 4 work.

**END**
''')
write("scripts/04-5_WALKTHROUGH_route-it.md", WALK_45)

# -------------------------------------------------------------------------
# Pre-dictation guide sections.
# -------------------------------------------------------------------------
GUIDE_23 = clean(r'''
## 2.3 · Plan for future income, expenses, and life events

### Start from

> In today's lesson, we're going to cover the future changes that need to be in your plan so Orange Plan is not projecting today's income and spending forever.

### Cover it in this order

1. Orange Plan starts from current cash flow and projects it forward. Life Events tell it where income, spending, assets, debt, or taxes are expected to change.
2. Distinguish an expected event from a scenario. Expected changes become part of the plan; uncertain “what if” questions stay separate.
3. For each event, decide what changes, when it starts, whether it is one-time or recurring, how long it lasts, the amount, and the inflation treatment.
4. Decide the likely funding source: future cash flow, money already saved, an asset sale, financing, or a mix.
5. Include debt without turning this into the debt-policy lesson. A future loan belongs in the event so the projection includes the obligation. Module 3 decides whether that debt is acceptable.
6. Preserve Austin's five-year Bitcoin ruling without a rigid lane table: Bitcoin can remain part of the funding plan 5 years out; the firmly committed amount becomes less Bitcoin-dependent as the date approaches.
7. Explain what changes downstream: future cash flow, debt payments, taxes, savings need, retirement date, and confidence.

### Leave out

- A full timeframe allocation table presented as universal law.
- The instruction to divide every future cost by months remaining.
- Reading the Life Events click path in the teach video.
- Treating every possible dream as a baseline event.

### Handoff

Have the learner make a list of expected changes with timing, amount, duration, and funding source. The Module 2 walkthrough demonstrates how to add them and how a future loan differs from a current debt.
''')
replace_lesson("DICTATION-PREP-CORE.md", "2.3", GUIDE_23, "2.4")

GUIDE_43 = clean(r'''
## 4.3 · Direct your surplus: choose the account and what it buys

**F22 remains Austin's only missing planning rule. The app mechanics and teaching flow are verified.**

### Start from

> In today's lesson, we're going to connect the surplus you found in Cash Flow to the actual accounts and investments that are going to receive the money.

### Cover it in this order

1. Trace the available contribution pool: current surplus, minus the saved reserve route, minus any saved extra-debt amount.
2. Teach 3 separate decisions for every dollar:
   - the job or timeframe;
   - the account/tax wrapper;
   - what the account buys.
3. State Austin's default route and the strong priorities that usually come first.
4. Name the facts that override the default: reserve gap, high-cost debt, employer match, underfunded pre-59½ Bridge, current tax rate, income uncertainty, account investment menu, Bitcoin access, and near-term retirement.
5. Explain how taxable Bridge, personally held Bitcoin, HSA, Roth, and traditional contributions are compared.
6. Explain when a deliberate split is correct. Each side needs a reason and the total must fit the available surplus.
7. Explain the current app controls without reading clicks: Custom, Fill to match, Max, taxable Leftover/Fixed; tax treatment where supported; Current mix, Set mix, or Choose holdings.
8. Explain requested versus applied contributions. The app caps current funding when the saved requests exceed available surplus.

### Austin pickup

> Once the reserve and debt policy are set, my default route for the next dollar is ________. The things that usually come first are ________. I would override that order when ________. A deliberate split makes sense when ________.

### Handoff

The learner brings the real surplus, employer match rules, available account types, Bridge need, and investment choices to the walkthrough. The walkthrough configures every row and reconciles the applied total.
''')
replace_lesson("DICTATION-PREP-CORE.md", "4.3", GUIDE_43, "4.4")

# -------------------------------------------------------------------------
# Checkpoints: checkable outcomes without forcing spoken headings.
# -------------------------------------------------------------------------
checkpoints = read("MODULE-CHECKPOINTS.md")
checkpoints = re.sub(
    r"(?ms)^Each lesson closes with the same three beats, and the module checklist is the\nsum of them:\n\n> \*\*YOUR DECISION\*\*.*?\n\n---",
    """The spoken lessons do not have to repeat one closing template. The module checklist owns the checkable finish line. A teach lesson explains the concept and leaves the learner with the decision or number needed for the walkthrough; the walkthrough performs the entry.\n\n---""",
    checkpoints,
    count=1,
)
MODULE_2_CP = clean(r'''
## Module 2 — Cash flow, reserve, and expected changes

**You will build:** A true surplus, both spending levels, a reserve policy, and the future income and spending changes the projection needs.

**You are done when:**

- [ ] Your true surplus is a number in the app, not an estimate
- [ ] You have two spending numbers: normal and bare-bones
- [ ] Your reserve target is set in months, the spending basis is correct, and the app shows the calculated target and current funding
- [ ] Every material expected change has a timing, amount, duration, and inflation treatment, or **Nothing major coming** is selected truthfully
- [ ] Each major future expense has a likely funding source: future cash flow, money already saved, an asset sale, financing, or a deliberate mix
- [ ] A future loan is modeled as part of the event, while the debt policy is handled separately in Module 3
- [ ] For a cost 5 years away, you can explain which part may still depend on Bitcoin and which firmly committed amount becomes less Bitcoin-dependent as the date approaches
- [ ] College, only if it applies: you can state the family commitment and the funding sources rather than using the full sticker price by default
- [ ] **Build Your Plan → Cash flow** shows complete

---
''')
checkpoints = re.sub(
    r"(?ms)^## Module 2 — .*?(?=^## Module 3 — )",
    MODULE_2_CP,
    checkpoints,
    count=1,
)
MODULE_4_CP = clean(r'''
## Module 4 — Allocation, asset location, and directing surplus

**You will build:** A target mix, account timeframes, an asset-location plan, and a complete instruction for where new surplus goes and what it buys.

**You are done when:**

- [ ] Your Bitcoin allocation is a percentage you have stress-tested at the current balance
- [ ] Every account has a deliberate Reserve, Bridge, or Legacy job
- [ ] Your target mix totals 100% and the drift band is saved
- [ ] You can separate the money's job, the account wrapper, and the investment purchased inside it
- [ ] Every contribution account type you intend to use has an amount or mode: Custom, Fill to match, Max, Leftover, or Fixed as applicable
- [ ] Tax treatment is set where the account supports Traditional, Roth, or Split
- [ ] Every active contribution row has an investment instruction: Current mix, Set mix, or Choose holdings
- [ ] Requested and applied contributions have been reconciled with the surplus available after Reserve and Extra debt
- [ ] F22 is complete when you can state your default route, the facts that override it, and whether the current answer is one destination or a deliberate split

> **App note:** Build Your Plan currently tracks account timeframes and target mix but not contribution routing as a separate task. The course still treats the contribution plan as required Module 4 work.

---
''')
checkpoints = re.sub(
    r"(?ms)^## Module 4 — .*?(?=^## Module 5 — )",
    MODULE_4_CP,
    checkpoints,
    count=1,
)
write("MODULE-CHECKPOINTS.md", checkpoints)

# -------------------------------------------------------------------------
# Remove the repository rule that manufactured the repeated spoken template.
# Claim parity still protects substantive positions.
# -------------------------------------------------------------------------
registry = read("CLAIM-REGISTRY.md")
registry = re.sub(
    r"(?ms)^## Three-beat closure\n.*\Z",
    clean(r'''
## Lesson completion without a forced spoken template

Module checkpoints remain checkable, but a core lesson is no longer required to speak the same 3 headings.

- The teach lesson explains the concept, decision, or number.
- The module walkthrough performs the app entry.
- The module checkpoint verifies that the finished plan now contains the result.
- A natural walkthrough handoff is used only on the last required teach lesson in a module.

The claim registry protects substantive planning positions across master, script, student text, generated module, and visual. It does not force copywriting structure into Austin's narration.
'''),
    registry,
    count=1,
)
write("CLAIM-REGISTRY.md", registry)

checker = read("tools/check-layer-parity.py")
checker = checker.replace(
    "  BEATS      a lesson closing beat present in some layers but not others\n",
    "",
)
checker = checker.replace(
    "Exit 1 on any failure. Coverage notes and deliberate beat exemptions are\nreported but do not fail.\n",
    "Exit 1 on any coverage or claim-parity failure.\n",
)
checker = re.sub(
    r"(?ms)^# --- CHECK 3: three-beat closure .*?(?=^# --- report )",
    "",
    checker,
    count=1,
)
write("tools/check-layer-parity.py", checker)

voice = read("scripts/VOICE-GUIDE.md")
VOICE_SECTION = clean(r'''
## Completion without a copywriting template — Austin, 2026-08-26

Do not force every core lesson to speak these 3 headings:

- Your decision
- Put it in Orange Plan
- You are done when

That repeated shape makes editor-written scripts sound manufactured. The decision and finish line still exist, but they live where they are useful:

- the teach video explains the concept and leaves the learner with the number or decision;
- the walkthrough performs the clicks and verifies the result;
- the module checkpoint carries the formal completion test.

A teach script may end with one natural sentence that hands off to the walkthrough. Most lessons simply finish the explanation and stop. Never add a miniature click path merely because a template has an empty slot.

''')
if "## Completion without a copywriting template — Austin, 2026-08-26" not in voice:
    marker = "## Teach-lesson closings + walkthrough hand-off"
    if marker not in voice:
        raise RuntimeError("VOICE-GUIDE closing marker missing")
    voice = voice.replace(marker, VOICE_SECTION + marker, 1)
write("scripts/VOICE-GUIDE.md", voice)

# Remove the one-time dictation-prep builders so this reviewed guide cannot be
# silently regenerated back to the earlier structure.
for rel in [
    "tools/build-dictation-prep.py",
    "tools/refine-dictation-drafts.py",
    "tools/fix-teach-handoffs.py",
    ".github/workflows/build-dictation-prep.yml",
    "dictation-prep-trigger/RUN",
]:
    path = ROOT / rel
    if path.exists():
        path.unlink()

print("purposeful course-flow pass applied")
