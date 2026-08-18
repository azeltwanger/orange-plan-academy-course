# Orange Plan Academy — course ↔ app contract

**Status:** active repair map  
**App source reviewed:** `azeltwanger/orange-plan` at `c78a00aa1ecc6d41d61bd38ed3ae12951652397e` on 2026-08-18  
**Course branch:** `course-repair/app-match-voice-pass`

This document is the contract between the Academy and the shipped app. It exists so the course does not become either:

- a collection of financial concepts that never turn into a plan, or
- a click-by-click product tour that breaks every time the interface changes.

## The outcome

A student finishes with a usable Bitcoin financial plan and can answer two questions for every important result:

1. **What decision did I make?**
2. **Where did this number come from?**

The course teaches the financial-planning concept first, simplifies it into a decision the student can make, and then demonstrates that decision on one continuous demo household in Orange Plan.

## Source-of-truth order

When the course and app disagree, use this order:

1. **Shipped app behavior on current `main`** — what the student can actually click and save.
2. **Austin's stated planning judgment** — the recommendation and reasoning.
3. **This contract** — the course structure and teaching sequence.
4. **Teach scripts and walkthrough sheets.**
5. **Slides and older coaching decks** — useful visual and example material, but not the current app map.

A specification or mockup is not a shipped surface. It can shape the course structure, but an exact walkthrough is not recorded until Austin has used the preview end to end.

## The five-part module pattern

Every core module follows the same path.

1. **Explain the concept.** What planning problem does this solve?
2. **Make the decision.** What judgment still belongs to the student?
3. **Show the demo household.** Continue the same household from the prior module.
4. **Put it in Orange Plan.** Enter, save, or apply the decision using the current app.
5. **Verify the result.** Read what changed and state the module's finish line.

A walkthrough is not a general tour of the page. It shows only the screens and controls needed to complete the module's decisions.

## The number-provenance rule

The most repeated question in client calls was some version of:

> **Where did this number come from?**

Every walkthrough must answer the following four lines the first time an important output appears.

### WHERE THIS NUMBER COMES FROM

- **WHAT IT MEANS** — the plain-language question this number answers.
- **CALCULATED FROM** — the upstream inputs used to calculate it.
- **EDIT SOURCE** — the one place the student changes those inputs.
- **THIS AFFECTS** — the important results downstream that move with it.

Example:

> **Surplus**  
> **WHAT IT MEANS:** what is left after taxes, living costs, and debt payments.  
> **CALCULATED FROM:** income − taxes − living spending − debt payments.  
> **EDIT SOURCE:** Cash Flow and the underlying income, spending, and debt rows.  
> **THIS AFFECTS:** reserve funding, contribution routing, and the retirement projection.

Do not say that every number has one literal database field. The useful promise is narrower: the course shows the student where the inputs live and what the output changes.

## Saved input, preview, and scenario

The old blanket line **“If you didn't click Apply, it didn't happen”** is false app-wide.

Orange Plan has three kinds of state:

- **Saved plan inputs.** Direct fields such as planned retirement age, baseline spending, confidence target, and Cash Flow settings save when the field is committed or autosaved.
- **Strategy previews.** Pages can show a proposed strategy or comparison without changing the saved plan. These surfaces use their own Save or Apply action.
- **Scenarios.** A saved what-if remains separate from the plan until the user deliberately applies a supported change.

Every walkthrough must say which of the three the student is looking at. Never turn one page's save behavior into an app-wide rule.

## One demo household

All core walkthroughs use the same household and carry its state forward.

The demo household needs enough complexity to teach the course without becoming a circus:

- two adults or one adult plus a clearly documented spouse assumption,
- earned income,
- normal and bare-bones spending,
- cash reserve,
- at least one taxable account and one retirement account,
- Bitcoin held in at least one account,
- one ordinary debt,
- one known future cost,
- Social Security or another retirement income source,
- enough tax diversity to show taxable, tax-deferred, and Roth,
- no Bitcoin-backed loan in the core baseline.

Optional or advanced lessons may add a temporary copy of the household with the relevant feature, such as a Bitcoin-backed loan. Do not contaminate the core demo with every edge case.

Each walkthrough starts with a short **DEMO STATE** block and ends with a **WHAT CHANGED** block. A student should be able to follow the numbers from one module into the next.

## Core course map

| Module | Planning decision | Primary app surface | Numbers that must be explained | Walkthrough result |
|---|---|---|---|---|
| 0 · Start Here | How the course and AI will be used | AI Review / Preferences | What the AI reads versus what the engine calculates | Safety rule and memory choice are deliberate |
| 1 · Baseline | Which inputs and assumptions the first plan will use | Accounts, onboarding, Plan → Retirement | Net worth, planned age, confidence target, plan confidence, earliest date | Verified first plan and starting snapshot |
| 2 · Cash Flow | Normal spending, bare-bones spending, surplus, reserve target | Cash Flow | Income, taxes, living, debt payments, surplus, reserve target and current months | Cash flow and reserve policy are saved |
| 3 · Debt | The job of each debt and the ceiling the household will not cross | Strategy → Debt | DTA, DTI, payment, payoff timing, BTC-loan LTV only when applicable | Every debt has a deliberate treatment |
| 4 · Allocation | Target mix, time-horizon jobs, and where new contributions go | Strategy → Allocation plus Cash Flow routing | Current mix, target mix, drift, available contribution dollars, timeframe funding | Target and next-dollar policy are saved |
| 5 · Tax | Which tax moves are relevant and when | Strategy → Tax | Cost basis, realized gain, estimated tax, tax buckets, conversion comparison | One current tax action or a deliberate pass |
| 6 · Retirement Income | Spending target, income gap, withdrawal order, and annual guardrails | Plan → Income | Spending target, income floor, gap, first-year funding, withdrawals, Bitcoin sold/retained, reserve, loan balance at death when borrowing is used | Retirement paycheck and policy are saved |
| 7 · Custody | The custody setup and recovery process the household can actually operate | Protect plus off-app recovery work | Readiness counts and checklist status only; never secrets | Recovery is tested and the no-secrets map exists |
| 8 · Estate | Who acts, what documents exist, and how the family starts | Protect plus legal/provider records | Beneficiary status, coverage gap, projected estate, readiness | Family handoff path is real, not only entered in the app |
| 9 · Maintain | What changes monthly, annually, and before a major decision | Cash Flow, Plan, Scenarios, Report | Current inputs, stale confidence, scenario deltas, report metrics | Review cadence, scenarios, report, and backup are saved |

## Confidence controls — keep the jobs separate

Orange Plan now has three confidence-related decisions. The course must not merge them.

| Control | Where it lives | Question it answers |
|---|---|---|
| **Plan confidence target** | Plan → Retirement | How many of the 1,000 test runs must stay funded before Orange Plan calls a date the earliest retirement date? |
| **Starting retirement spending target** | Plan → Income | How much annual spending should the retirement plan start with? |
| **Annual guardrails** | Plan → Income | When does the saved retirement paycheck get reduced, held, or increased after retirement? |

The Plan confidence target defaults to 80%, but 80% is a starting point rather than a magic number. Raising the target generally moves the earliest date later; lowering it generally moves the date earlier and accepts a greater chance that future adjustments will be needed.

Use **test runs**, not paths, futures, simulated markets, or separate deterministic-versus-Monte-Carlo language in the core course.

## Build Your Plan integration

The course should eventually enter each area through **Build Your Plan**, but exact click paths wait for a working preview Austin has personally completed.

Until that exists:

- build the concept-to-decision mapping now,
- use current primary page names in temporary walkthrough sheets,
- do not record speculative screens from a mockup,
- do not number areas as “area 3” or “step 4” in spoken copy,
- use durable names such as Cash Flow, Debt, Allocation, Tax, Income, and Protect.

When Build Your Plan ships, each area must show:

1. the lessons that teach the decision,
2. the app inputs required for completion,
3. the app's completion rule,
4. the student's human decision rule,
5. the next area.

The app checkmark certifies that required data exists. The module checkpoint certifies that the student made the planning decision. Those are related, but not always identical.

## Core versus Advanced

The split is correct, but the student experience should be **one core course with contextual optional deep dives**, not two courses they feel obligated to finish.

### Core belongs in the linear path when it is required to build a usable plan

Core answers:

- What do I own, owe, earn, and spend?
- What assumptions am I using?
- When could I retire at my chosen confidence target?
- How much reserve do I need?
- What is the job of each debt?
- Where does the next dollar go?
- What tax records and windows matter?
- How will retirement pay me?
- Can I and my family recover the Bitcoin?
- Who acts if I cannot?
- How do I keep the plan current?

### Advanced is gated by a condition on the student's own plan

Advanced includes:

- how the Monte Carlo model is built,
- Bitcoin-backed borrowing,
- deeper leverage strategy,
- a pre-Medicare healthcare bridge,
- Roth conversion optimization,
- tax-loss or gain harvesting,
- relocation analysis,
- sell-versus-borrow comparisons,
- trusts, estate-tax planning, and complex custody.

Each advanced lesson starts with one short gate:

> **Watch this only if [condition visible in your plan]. Otherwise your plan is complete without it.**

Advanced lessons do not count toward core progress. Empty mirrored “advanced modules” should not appear in the student interface. The best placement is the existing **Optional next levels** section at the bottom of the relevant core module, plus a searchable Advanced Library for reference.

## Voice rule

Scripts are useful and fast to edit. Keep them.

The voice pass is not a ban on authored scripts; it is a quality standard:

- explain the cause before the recommendation,
- use the demo household rather than generic claims,
- keep the exact app term when it matters,
- say “I think” when it is Austin's judgment rather than a fact,
- remove manufactured slogans, clever reversals, consultant language, and fake reassurance,
- preserve useful spoken repetition when it helps someone follow the numbers,
- end with the decision, where it goes in the app, and the checkable finish line.

Lesson 2.2 remains the strongest current calibration sample because it began as Austin's dictation. Client-call language is a second source for the questions and confusions real users actually have.

## Walkthrough recording contract

Every walkthrough sheet contains:

1. **DEMO STATE** — the exact starting state and the numbers that should already be visible.
2. **DECISIONS FROM THE LESSONS** — what the student is about to implement.
3. **DO** — the current click path.
4. **SEE** — the result to point at.
5. **WHERE THIS NUMBER COMES FROM** — the four-line provenance block for each important output.
6. **WHAT CHANGED** — before and after in the demo household.
7. **DONE WHEN** — the app state and the human decision that complete the module.

Optional AI buttons, edge cases, recovery branches, and unusual account types belong in separate reference demos unless they are required to finish the module.

## Change workflow

When the app changes:

1. Update this contract's affected row.
2. Update the teach lesson only when the financial concept or decision changed.
3. Update the walkthrough whenever labels, save behavior, or the route changed.
4. Update the slides only when the visual teaches a retired concept or wrong fact.
5. Re-record only the affected video, not the entire module.

Before a lesson is filmed, confirm:

- the concept is still correct,
- the demo decision is clear,
- the app path was clicked on the current preview or `main`,
- every important number has a provenance explanation,
- the closing checkpoint matches the app and the human decision.
