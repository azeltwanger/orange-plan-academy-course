# Build Your Plan ↔ Orange Plan Academy walkthrough crosswalk

**Status:** provisional implementation contract  
**App source checked:** `azeltwanger/orange-plan` `main` at `8019bfcf14387f2e15746b18707534bfcb7eb4e5` on 2026-08-19  
**Exact walkthroughs:** hold until Austin completes the deployed Build Your Plan preview end to end

## Standing rule

**Build Your Plan is the navigation spine for the future walkthroughs. It does not have to be the exact syllabus for every concept lesson.**

The Academy groups financial-planning concepts in the order that makes the decisions easiest to understand. The product can group implementation in the order that makes the plan easiest to complete.

A dedicated customer-facing Build Your Plan flow is not confirmed as shipped on the current accepted `main` from the current route and test inventory. Specifications, curriculum content, and preview work do not establish the exact deployed controls. Therefore this file maps decisions now and waits to fill exact product metadata from the working preview Austin has personally used.

Do not record an exact click path from a mockup, specification, route guess, or old course walkthrough.

## What the implementation layer must do

Every final walkthrough:

- enters through the relevant Build Your Plan area,
- begins from the accepted demo checkpoint,
- uses the current page and save behavior,
- implements only the decisions already taught,
- explains where the material outputs came from,
- returns to the build flow,
- and distinguishes the app completion state from the human planning finish line.

## What can differ

The concept course does not need to copy the product flow word for word.

- One module may support more than one build step.
- One build step may depend on concepts from more than one lesson.
- A concept may be taught earlier because the learner needs it before using the related control.
- Debt can remain before Allocation in the Academy even when the product groups or orders them differently.
- Custody and Estate can remain separate modules even when the app groups them under Protect.
- Advanced lessons remain searchable, contextual deep dives rather than required build steps.

Do not break a clear lesson into artificial pieces solely to mirror a screen. Do not make a walkthrough bypass the product flow solely to preserve an old course structure.

## Walkthrough learner loop

1. **Recall the decision** — what did the concept lesson ask the learner to decide?
2. **Open the matching build area** — using the accepted preview label and route.
3. **Continue the demo household** — begin from the prior accepted checkpoint.
4. **Name the state** — saved input, strategy preview, or Scenario.
5. **Implement the decision** — enter, save, or apply only the relevant change.
6. **Read the result** — explain the number and its downstream effects.
7. **Return to Build Your Plan** — show what is complete and what comes next.
8. **State both finish lines** — app completion and human decision completion.

The app checkmark certifies that required data exists. The Academy checkpoint certifies that the learner understood the trade-off and made the decision deliberately.

## Provisional course mapping

The labels below are durable planning-area names, not final UI labels or step numbers.

| Provisional build area | Core Academy teaching | Planning output |
|---|---|---|
| **Baseline & assumptions** | Module 1 | Verified accounts, holdings, income, debts, life events, assumptions, confidence target, and first retirement read |
| **Cash Flow & Reserve** | Module 2 | Normal spending, bare-bones spending, reliable surplus, reserve target, and known-cost funding plan |
| **Debt** | Module 3 | A deliberate treatment for every debt and a household ceiling |
| **Allocation & Contributions** | Module 4 | Bitcoin target and band, time-horizon jobs, account placement, and next-dollar route |
| **Tax** | Module 5 | Quantity and basis readiness, relevant tax windows, and one current action, CPA question, or deliberate pass |
| **Retirement Income** | Module 6 | Retirement spending, income floor, total draw, source strategy, starting paycheck, and annual policy |
| **Protect** | Modules 7–8 | Tested recovery, no-secrets custody map, beneficiaries, legal roles, heir letter, delivery paths, and protection gaps |
| **Finish, test, and maintain** | Module 9 | Scenarios, capstone, report, encrypted export, monthly review, annual review, and update triggers |

**Module 0 is orientation before the build flow.** It teaches how the app, Academy, AI, and security boundary work.

If the deployed preview combines, splits, reorders, or renames an area, first update the walkthrough routing. Change the concept structure only when the actual financial-planning decision changed or the current teaching order became harder to follow.

## Required metadata before recording

Every core walkthrough records:

- `app_step_id`
- `app_step_label`
- `primary_route`
- `accepted_app_commit`
- `verified_date`
- `planning_decisions_implemented`
- `saved_input_or_preview_or_scenario`
- `app_completion_rule`
- `human_completion_rule`
- `demo_household_version`
- `starting_checkpoint`
- `ending_checkpoint`

Concept lessons may name the durable planning area. They do not depend on exact buttons, routes, or completion copy.

## Number provenance inside every walkthrough

For every material output:

- **WHAT IT MEANS**
- **CALCULATED FROM**
- **EDIT SOURCE**
- **THIS AFFECTS**

Required outputs include surplus, reserve target, DTI, DTA, current and target allocation, projected tax, Plan confidence, earliest target-qualified date, retirement spending, total draw, source split, Bitcoin sold or retained, Scenario delta, and Protect readiness.

## Advanced placement

Advanced lessons are linked from the build area that reveals the condition:

- model mechanics and holding overrides → Baseline & assumptions
- Bitcoin-backed loans → Debt or Retirement Income
- conversion sizing and harvesting → Tax
- pre-Medicare healthcare → Retirement Income
- passphrases and multi-key custody → Protect
- trusts and complex estate planning → Protect

Each Advanced lesson opens with:

> **Watch this only if [condition]. Otherwise this part of your plan is complete without it.**

Advanced never blocks core progress when the condition is absent.

## Product-change workflow

When the app changes:

1. verify the accepted customer-facing build,
2. classify the change as concept, walkthrough, demo-output, or no course impact,
3. update this crosswalk,
4. rerun the affected demo checkpoint,
5. update the walkthrough when route, label, state, or completion changed,
6. update the concept only when the decision or explanation changed,
7. rerun the course audit.

The learner should experience one system: the Academy explains and prepares the decision, and Build Your Plan helps implement it.
