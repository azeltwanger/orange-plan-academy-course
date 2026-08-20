# Build Your Plan ↔ Orange Plan Academy walkthrough crosswalk

**Status:** concept and checkpoint mapping complete; exact implementation metadata pending deployed end-to-end use  
**Customer-facing concept review:** `azeltwanger/orange-plan` `main` at `8019bfcf14387f2e15746b18707534bfcb7eb4e5` on 2026-08-19  
**Reproducible demo engine:** app branch commit `3105664da5dd77c57bf6d489e28b8f3a5e3d3eb5` on 2026-08-20  
**Exact walkthroughs:** hold until Austin completes the deployed Build Your Plan flow end to end

## Standing rule

**Build Your Plan is the navigation spine for walkthroughs. It is not required to be the exact syllabus for every concept lesson.**

The Academy groups planning concepts in the order that makes decisions easiest to understand. The product can group implementation in the order that makes the plan easiest to complete.

Specifications, mockups, code branches, and prior walkthroughs do not establish the exact deployed controls. Do not record a click path until Austin has used that customer-facing flow and the course has recorded the stable step metadata.

## Current work that is already complete

The course does not need Build Your Plan to discover the planning outputs. The approved synthetic household already has reconciled engine candidates for:

- confidence and earliest target-qualified date,
- Cash Flow and reserve,
- debt ratios and payoff,
- Allocation denominator, current mix, target, band, and drawdown,
- tax/basis status,
- Retirement Income spending choices, total draw, sources, and Bitcoin units,
- and the 4% inflation Scenario.

Those results define what each walkthrough must verify. Build Your Plan still owns the exact implementation path, completion state, and next-step navigation.

## What the implementation layer must do

Every final walkthrough:

- enters through the relevant Build Your Plan area,
- begins from the accepted demo checkpoint,
- uses the current route and save behavior,
- implements only the decision already taught,
- names Saved / Previewing / Scenario / read-only state,
- explains where material outputs came from,
- returns to the build flow,
- and distinguishes the app completion rule from the human planning finish line.

## What can differ

- One Academy module may support more than one build step.
- One build step may depend on concepts from more than one lesson.
- A concept may be taught earlier because it is required before using a later control.
- Debt can remain before Allocation in the Academy even when the product orders them differently.
- Custody and Estate can remain separate lessons even when the app groups them under Protect.
- Advanced lessons remain contextual deep dives rather than required steps.

Do not break a clear lesson into artificial pieces solely to mirror a screen. Do not bypass the deployed product flow solely to preserve an old course order.

## Walkthrough learner loop

1. **Recall the decision** — what did the concept lesson ask the learner to decide?
2. **Open the matching build area** — using the accepted label and route.
3. **Continue the same household** — begin from the prior accepted checkpoint.
4. **Name the product state** — saved input, preview, Scenario, or read-only result.
5. **Implement only that decision.**
6. **Read the result** — explain meaning, source, edit location, and effect.
7. **Return to Build Your Plan.**
8. **State both finish lines** — app completion and human completion.

The app checkmark certifies the product's required data or action state. The Academy checkpoint certifies that the learner understood the trade-off and made the decision deliberately.

---

# Provisional planning-area mapping

The labels below are durable planning-area names, not final UI labels or step numbers.

| Provisional build area | Core teaching | Starting checkpoint | Ending checkpoint | Human planning output |
|---|---|---|---|---|
| **Baseline & assumptions** | Module 1 | approved inputs | `demo-v1-baseline` | Verified/estimated/missing data, assumptions, household retirement date, confidence target, first result |
| **Cash Flow & Reserve** | Module 2 | `demo-v1-baseline` | `demo-v1-cashflow` | Normal/bare-bones spending, post-debt capacity, reserve, known-cost funding plan |
| **Debt** | Module 3 | `demo-v1-cashflow` | `demo-v1-debt` | Treatment for every debt, extra-principal decision, household ceiling |
| **Allocation & Contributions** | Module 4 | `demo-v1-debt` | `demo-v1-allocation` | App denominator, Bitcoin target/band, jobs, location, $3,500 post-debt account route |
| **Tax** | Module 5 | `demo-v1-allocation` | `demo-v1-tax` | Quantity/basis readiness, tax windows, one action, CPA question, or pass |
| **Retirement Income** | Module 6 | `demo-v1-tax` | `demo-v1-income` | Spending, phased income floor, need, draw, source strategy, $100,000 paycheck, annual policy |
| **Protect** | Modules 7–8 | `demo-v1-income` | `demo-v1-protect` | Real recovery work, no-secrets map, legal/provider records, heir letter, delivery, protection gaps |
| **Finish, test, maintain** | Module 9 | `demo-v1-protect` | `demo-v1-final` | Scenarios, capstone, report, PDF/export, actions, review cadence |

Module 0 is orientation before the build flow.

If the deployed flow combines, splits, reorders, or renames an area, first update walkthrough routing. Change the concept structure only when the actual planning decision or required mental model changed.

---

# Candidate values each area must verify

## Baseline & assumptions

- household retirement start: Alex age 55 / March 2036,
- Plan target: 80%,
- confidence: 94.6%,
- earliest target-qualified date: May 2032 / Alex age 51,
- one household retirement date, not separate spouse dates.

## Cash Flow & Reserve

- modeled tax: $36,862/year,
- required debt: $1,833/month,
- extra auto principal: $500/month,
- post-debt surplus: $3,761/month,
- post-debt account route: $3,500/month,
- operating cushion: $261/month,
- reserve: $30,000 / 6 months.

## Debt

- DTI 11.6%,
- DTA 40.0%,
- auto payoff 2027 / Alex 46.

## Allocation & Contributions

- app scope: $270,000,
- 529 and primary home excluded,
- Bitcoin 64.8%,
- target 50%, band 40–60%, above-band review,
- Bitcoin loss at 75%: $131,250,
- full route: $500 extra debt + $3,500 account contributions.

## Tax

- 1.75 BTC quantity,
- 1.25 BTC / $48,000 known basis,
- 0.40 BTC reconstruction pending,
- 0.10 BTC unknown,
- unresolved basis visibly qualified.

## Retirement Income

- spending choices: $99,317 / $100,000 / $170,216 / $249,904,
- saved paycheck: $100,000 at 94.6%,
- first-year need: $171,383,
- recurring income: $69,435,
- draw: $101,948,
- Bitcoin proceeds: $97,948,
- projected price: $1,235,921,
- units sold: 0.079251 BTC.

## Finish, test, maintain

- 3% baseline: 94.6%,
- 4% inflation Scenario: 91.6%,
- delta: −3.0 percentage points,
- PDF and encrypted export roles separated,
- in-app restore not described as currently available.

Protect cannot be accepted from engine values alone. It requires UI status and real-world proof boundaries.

---

# Required metadata before recording

Every walkthrough records:

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
- `important_number_keys`
- `screenshot_or_recording_reference`
- `known_holds`

Concept lessons may name the durable planning area. They do not depend on exact buttons, step numbers, or completion copy.

## Number provenance inside every walkthrough

For every material output:

- **WHAT IT MEANS**
- **CALCULATED FROM**
- **EDIT SOURCE**
- **THIS AFFECTS**

Required outputs include post-debt surplus, reserve target, DTI, DTA, Allocation scope/current/target, projected tax, Plan confidence, earliest date, total need, recurring income, total draw, source split, Bitcoin sold, spending choices, Scenario delta, and Protect readiness.

## Advanced placement

Advanced lessons are linked from the build area that reveals the condition:

- model mechanics and holding overrides → Baseline & assumptions
- Bitcoin-backed loans → Debt or Retirement Income
- conversion sizing and harvesting → Tax
- pre-Medicare healthcare → Retirement Income
- passphrases and multi-key custody → Protect
- trusts and complex estate planning → Protect

Every Advanced lesson begins:

> **Watch this only if [condition]. Otherwise this part of your plan is complete without it.**

Advanced never blocks Core progress when the condition is absent.

## Product-change workflow

When the app changes:

1. verify the accepted customer-facing build,
2. classify concept, walkthrough, demo-output, professional/reference, or no course impact,
3. update this crosswalk,
4. rerun the affected synthetic checkpoint,
5. update walkthrough route/label/state/completion when implementation changed,
6. update concept only when the planning decision or explanation changed,
7. update visual when it became false,
8. rerun the Academy audit.

The learner should experience one system: the Academy prepares the decision, and Build Your Plan helps implement it.
