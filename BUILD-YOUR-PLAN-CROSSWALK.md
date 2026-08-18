# Build Your Plan ↔ Orange Plan Academy crosswalk

**Standing rule:** **Build Your Plan is the syllabus.**

The Academy does not maintain a separate planning sequence, checklist, or vocabulary beside the app. The app is the workbook. The Academy explains the decision, teaches the financial-planning concept, demonstrates it on the continuous demo household, and then sends the learner into the matching **Build Your Plan** step.

This file is the routing layer between the app and the course. Exact `app_step_id`, labels, routes, and completion rules are filled from the working preview after Austin has completed the flow end to end. Do not record exact click paths from a mockup.

## The learner flow inside every Build Your Plan step

1. **Decision** — what must the learner decide?
2. **Concept** — what financial-planning idea makes the decision understandable?
3. **Trade-off** — what improves, what gets worse, and what can go wrong?
4. **Demo** — show the decision on the same demo household used throughout the course.
5. **Complete the app step** — enter, save, or apply the decision in Build Your Plan.
6. **Read the result** — explain where the important number came from and what moved downstream.
7. **Finish line** — distinguish the app checkmark from the human planning decision.

The app checkmark means the required data exists. The Academy checkpoint means the learner understood the decision and made it deliberately. A step is complete only when both are true.

## Provisional course mapping

The final row labels come from the shipped Build Your Plan preview. Until then, this is the curriculum contract.

| Build Your Plan area | Core Academy teaching | Planning output |
|---|---|---|
| **Baseline & assumptions** | Module 1 | Verified accounts, holdings, income, debts, life events, starting assumptions, confidence target, and first retirement read |
| **Cash Flow & Reserve** | Module 2 | Normal spending, bare-bones spending, reliable surplus, reserve target, and funding plan |
| **Debt** | Module 3 | A deliberate treatment for every debt and a ceiling the household will not cross |
| **Allocation & Contributions** | Module 4 | Target allocation, time-horizon jobs, account placement, and the next-dollar route |
| **Tax** | Module 5 | Cost-basis readiness, relevant tax windows, and one current action or a deliberate pass |
| **Retirement Income** | Module 6 | Starting spending target, income floor, gap, first-year funding, withdrawal order, and annual guardrails |
| **Protect** | Modules 7–8 | Tested recovery, no-secrets custody map, beneficiaries, executor path, heir letter, and family handoff |
| **Finish, test, and maintain** | Module 9 | Scenarios, report, encrypted backup, monthly review, annual review, and update triggers |

**Module 0 is orientation before Build Your Plan.** It teaches how to use the course and the AI safely. It is not a separate financial-planning area.

If the shipped app combines, splits, or renames any area, the course follows the app. Do not preserve a course module boundary merely because it existed first.

## Lesson metadata required before filming

Every core lesson or walkthrough must identify:

- `app_step_id`
- `app_step_label`
- `primary_route`
- `planning_decision`
- `app_completion_rule`
- `human_completion_rule`
- `demo_household_version`
- `last_verified_app_commit`

Concept lessons should survive ordinary interface changes. Walkthrough sheets are replaceable and are re-verified whenever the route, label, save behavior, or completion rule changes.

## Number provenance inside every step

For each important result, the walkthrough says:

- **WHAT IT MEANS**
- **CALCULATED FROM**
- **EDIT SOURCE**
- **THIS AFFECTS**

This is mandatory for outputs such as surplus, reserve target, debt ratios, target allocation, projected tax, plan confidence, earliest retirement date, retirement spending target, first-year funding, Bitcoin sold or retained, and estate readiness.

## Advanced material

Advanced lessons live under the Build Your Plan step that triggers them. They are not a second required course.

Examples:

- Monte Carlo mechanics → Baseline & assumptions
- Per-holding return and income overrides → Baseline & assumptions
- Bitcoin-backed loans → Debt or Retirement Income, depending on the decision
- Roth conversions and harvesting → Tax
- Pre-Medicare healthcare → Retirement Income
- Trusts and complex custody → Protect

Each advanced lesson begins with a condition visible in the learner's plan:

> **Watch this only if [condition]. Otherwise this Build Your Plan step is complete without it.**

Advanced lessons never block core progress unless the learner's own plan makes the issue necessary.

## No parallel checklist

`MODULE-CHECKPOINTS.md`, Circle module pages, walkthrough sheets, and the Build Your Plan UI must all describe the same completion outcome.

When they disagree:

1. verify current shipped app behavior,
2. update this crosswalk,
3. update the affected course checkpoint and walkthrough,
4. update the concept lesson only when the financial decision changed.

The learner should never have to wonder whether the course and the app are asking them to build two different plans.
