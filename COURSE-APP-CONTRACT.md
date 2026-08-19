# Orange Plan Academy — course ↔ app contract

**Status:** active pre-dictation contract  
**App source verified:** `azeltwanger/orange-plan` `main` at `8019bfcf14387f2e15746b18707534bfcb7eb4e5` on 2026-08-19  
**Course branch:** `course-repair/app-match-voice-pass`  
**Exact walkthrough status:** hold until Austin completes the deployed Build Your Plan preview end to end

## The contract

Orange Plan owns the saved data and calculations. The Academy teaches the financial-planning concept, the trade-off, Austin's judgment, and the decision the learner still has to make.

A student finishes each planning area able to answer:

1. **What decision did I make?**
2. **Where did the important number come from?**
3. **What changed in the plan after the decision?**
4. **What still requires real-world or professional proof?**

The course must not become either a textbook disconnected from implementation or a click tour that breaks whenever a button moves.

## Source-of-truth order

When the course and product disagree:

1. **Current accepted app behavior** — what the learner can actually view, save, preview, and export
2. **Austin's stated planning judgment** — the recommendation and reasoning
3. **Verified tax, legal, custody, insurance, and mathematical facts**
4. **This contract and the current course outline**
5. **Current scripts and lesson text**
6. **Walkthrough sheets**
7. **Slides and older coaching decks**

A specification, mockup, old route, or source file is not proof that a customer-facing feature has shipped.

## Durable teaching loop

Every core planning area follows this loop:

1. **Name the decision.**
2. **Teach only the concept needed to make it intelligently.**
3. **Show what gets better, worse, or more fragile.**
4. **Continue the canonical demo household.**
5. **Trace the important number to its source.**
6. **State the learner's decision and the checkable finish line.**
7. **Use the versioned walkthrough to implement it in the current app.**

The concept video avoids temporary button names. The walkthrough owns the current route, control, save behavior, and screenshot.

## Number provenance

The first time a material output appears in a planning area, teach:

- **WHAT IT MEANS** — the plain-language question the output answers
- **CALCULATED FROM** — the upstream inputs and strategy used
- **EDIT SOURCE** — where the learner changes the real source rather than the displayed output
- **THIS AFFECTS** — the important downstream results that should move

Example:

> **Surplus**  
> **WHAT IT MEANS:** recurring money available after current obligations.  
> **CALCULATED FROM:** income − estimated taxes − living spending − required debt payments.  
> **EDIT SOURCE:** the underlying Cash Flow, income, spending, tax, or debt rows.  
> **THIS AFFECTS:** reserve funding, extra debt, contributions, future balances, confidence, and earliest date.

The useful promise is not that every output has one database field. It is that the learner knows which source facts and saved decisions created it.

## App state: saved input, preview, or Scenario

The old blanket instruction **“If you did not click Apply, it did not happen”** is false app-wide.

Orange Plan has three distinct states:

- **Saved inputs.** Direct Plan fields and other committed settings save under the behavior of that page.
- **Strategy previews.** A proposed strategy can change the displayed comparison without changing the saved plan until that surface's Save or Apply action is used.
- **Scenarios.** A saved what-if remains beside the baseline until a real decision is applied to its owning source page.

Every walkthrough names which state the learner is viewing. A page-specific save rule is never taught as a universal app rule.

## Current app facts verified for the course

### Plan → Retirement

The current retirement inputs are:

- **Planned retirement age**
- **Baseline spending**
- **Confidence target**

The Plan confidence target:

- defaults to **80%**,
- accepts whole percentages from **50% through 99%**,
- represents the minimum share of **1,000 test runs** that must remain funded through planning age,
- and is used to find the earliest retirement date reaching the selected target.

The confidence result at the planned age and the earliest target-qualified date come from the same test-run framework. The core course does not teach a second deterministic retirement date beside it.

### Plan → Income

Income has two separate retirement-spending decisions:

1. **Starting-spending selection** — calculated Conservative, Balanced, and Aggressive reference amounts around 95%, 80%, and 60%, plus the learner's current Plan amount when distinct
2. **Annual spending policy** — the saved paycheck and its annual review behavior

The current preset policy uses:

- lower trigger **60%**,
- target **80%**,
- upper trigger **95%**,
- maximum one-year correction **10%** toward the target amount.

The exact 60/80/95 preset is Orange Plan's product policy assembled from researched components. The course does not present it as one published researcher's exact parameter set.

The Income spending target, withdrawal strategy, Plan confidence target, and annual policy have separate ownership and save lifecycles. The course must not imply that changing one automatically changes the others.

### Encrypted export

Orange Plan currently creates a passphrase-protected encrypted export for secure storage and portability.

**In-app plan restore is temporarily unavailable.** Therefore:

- the course does not call the export a restorable backup the learner can use today,
- the learner keeps the active plan and source records intact,
- the passphrase is stored separately from the file,
- and the restore process is reverified before a future walkthrough teaches import.

The readable PDF and encrypted export have different jobs. Neither contains Bitcoin secrets.

### Build Your Plan

A dedicated customer-facing Build Your Plan flow is **not confirmed as shipped on current `main`** from the current route and test inventory. Product specifications, curriculum content, and preview work exist, but they do not establish the exact deployed flow.

Accordingly:

- the course architecture and concept-to-decision mapping are complete now,
- `BUILD-YOUR-PLAN-CROSSWALK.md` remains the provisional routing contract,
- spoken concept lessons use durable area names rather than step numbers,
- no exact click path is filmed from a mockup or specification,
- and final `app_step_id`, labels, routes, completion rules, and screenshots wait for the deployed preview Austin has personally completed.

This hold protects the concept videos from product churn without making the Academy feel disconnected from the eventual build flow.

## Continuous demo household

All core examples use `DEMO-HOUSEHOLD.md` unless explicitly labelled **illustrative — not the demo household**.

The demo is complex enough to teach the plan but deliberately excludes a Bitcoin-backed loan from the saved core baseline.

Every walkthrough begins with:

- `demo_household_version`,
- starting checkpoint,
- source inputs expected on screen,
- and calculated outputs expected from the last accepted receipt.

Every walkthrough ends with:

- what changed,
- the next checkpoint,
- the app completion state,
- and the human planning finish line.

App-calculated confidence, tax, withdrawal, Bitcoin-sale, estate, Scenario, and readiness outputs are never invented in prose. They come from `DEMO-CHECKPOINT-RUN-SHEET.md` receipts.

## Core course map

| Module | Human planning decision | Durable app area | Important outputs | Human finish line |
|---|---|---|---|---|
| 0 · Start Here | How the learner will use the app, Academy, AI, and security boundary | AI Review / privacy settings | Engine result versus AI explanation | Learner can state app-calculates / AI-explains / learner-decides and the no-secrets rule |
| 1 · Baseline | Which facts, expected changes, assumptions, spending, and confidence target define the first plan | Accounts, onboarding, Plan → Retirement | Net worth, planned age, confidence, earliest target-qualified date | First plan is honest about verified, estimated, and missing data |
| 2 · Cash Flow | Normal spending, bare-bones spending, reliable surplus, reserve, and known-cost funding | Cash Flow | Source rows, surplus, reserve target, months funded | Learner can rebuild the surplus and explain the reserve choice |
| 3 · Debt | Treatment for every debt and the household ceiling | Debt | DTI, DTA, payment, payoff timing | Every debt has a reasoned treatment that preserves required liquidity |
| 4 · Allocation | Bitcoin target, review band, time-horizon jobs, location, and next-dollar route | Allocation plus Cash Flow routing | Current/target mix, drawdown dollars, timeframe funding, route | Learner can state the dollar drawdown and where the next recurring dollar goes |
| 5 · Tax | Basis readiness and the one tax action, CPA question, or deliberate pass | Tax | Quantity, known/unknown basis, estimated tax, tax pools, roadmap | Tax estimate is traceable and unresolved data stays visible |
| 6 · Retirement Income | Spending, income floor, total draw, funding sources, starting paycheck, and annual policy | Plan → Income | Gap, total draw, source split, Bitcoin sold/retained, spending choices, reserve | Retirement paycheck and funding strategy reconcile and can be explained |
| 7 · Custody | Custody job and recoverable setup for each balance | Protect plus real custody work | Checklist/readiness status only | Receive, send, recovery, family practice, and failure-domain work are real, not merely checked |
| 8 · Estate / Insurance | Who acts, which records control, how family starts, and which gaps remain | Protect plus attorney/provider/carrier records | Beneficiary status, readiness, coverage gaps, estate output | Legal authority, technical process, and family instructions connect without exposed secrets |
| 9 · Maintain / Test / Read | Review cadence, useful Scenarios, capstone, and annual records | Transactions, source pages, Scenarios, Report | Scenario deltas, report metrics, action list | Learner can explain the plan in six sentences and owns one to three dated actions |

## App checkmark versus educational completion

The app can confirm that required data exists. It cannot always confirm that the learner made a sound decision or completed the real-world action.

Examples:

- A reserve target exists in the app; the learner can explain why the months fit the household.
- An allocation target exists; the learner can state the dollar loss in a 75% Bitcoin drawdown and still choose to hold it.
- A recovery test is marked; the device and family practice actually worked.
- A beneficiary is recorded; the provider accepted the current designation.
- An heir letter exists; the family understands the first call and the document contains no secret.

Walkthroughs state both finish lines.

## Core versus Advanced

Core contains the concepts every learner needs for a usable plan.

Advanced begins only when a condition is visible in the learner's own plan. Every Advanced lesson opens with:

> **Watch this only if [condition]. Otherwise this part of your plan is complete without it.**

Advanced includes detailed model mechanics, Bitcoin-backed loans, conversion sizing, harvesting, relocation, special account-access methods, pre-Medicare healthcare, sell-versus-borrow, passphrases, multisig implementation, trusts, estate tax, and complex insurance analysis.

Advanced never blocks core progress when the condition is absent.

## Walkthrough metadata required before recording

Every current walkthrough stores:

- `app_step_id`
- `app_step_label`
- `primary_route`
- `accepted_app_commit`
- `verified_date`
- `demo_household_version`
- `starting_checkpoint`
- `ending_checkpoint`
- `planning_decisions_implemented`
- `saved_input_or_preview_or_scenario`
- `app_completion_rule`
- `human_completion_rule`

A route, label, save behavior, or completion-rule change triggers a walkthrough update. A financial-planning decision change triggers a concept review.

## Course-impact rule for app changes

Every customer-facing app change should be classified:

- **none** — no course-facing behavior changed
- **concept update** — the financial question, calculation ownership, or decision changed
- **walkthrough update** — route, label, control, save behavior, or completion rule changed
- **demo-account update** — canonical inputs or calculated checkpoint outputs changed

When the app changes:

1. update this contract and the crosswalk,
2. rerun only the affected demo checkpoint,
3. update the concept only when the decision or explanation changed,
4. update the walkthrough when implementation changed,
5. update the slide only when the visual became false,
6. rerun the course audit.

This is how the Academy stays matched to Orange Plan without rerecording the entire course after every product change.
