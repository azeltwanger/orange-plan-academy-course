# Build Your Plan ↔ Orange Plan Academy walkthrough crosswalk

**Standing rule:** **Build Your Plan is the navigation spine for the walkthroughs. It does not have to be the exact syllabus for every concept lesson.**

The Academy can group and order financial-planning concepts in the way that makes them easiest to understand. The app can group the work in the way that makes the plan easiest to complete. Those structures should support each other without being forced into a one-for-one match.

What must track exactly enough is the implementation layer:

- the walkthrough enters through the relevant **Build Your Plan** step,
- it uses the current app page and save behavior,
- it shows the same demo household carrying forward,
- it explains where the important numbers came from,
- it completes the work that the Build Your Plan step is asking for,
- and it returns to the build flow so the learner can see what is complete and what comes next.

This file is the routing layer between the app and the course. Exact `app_step_id`, labels, routes, and completion rules are filled from the working preview after Austin has completed the flow end to end. Do not record exact click paths from a mockup.

## What can differ

The course does **not** need to copy the Build Your Plan structure word for word.

- One course module may support more than one Build Your Plan step.
- One Build Your Plan step may depend on concepts taught across more than one lesson.
- A concept may be taught earlier because the learner needs it before the matching app control appears.
- Debt can remain before allocation in the Academy even if the app groups or orders those areas differently.
- Custody and estate can remain separate teaching modules even if the app groups both under Protect.
- Advanced lessons can stay in a searchable library while being linked from the relevant build area.

Do not break a clear lesson into artificial pieces simply to mirror a product screen. Do not make a walkthrough ignore the product flow simply to preserve an old course outline.

## The learner flow for each walkthrough

1. **Recall the decision** — what did the concept lesson ask the learner to decide?
2. **Open the matching Build Your Plan step** — this is the stable entry point.
3. **Continue the demo household** — start from the state produced by the prior walkthrough.
4. **Implement the decision** — enter, save, or apply it on the current app page.
5. **Read the result** — explain where the important number came from and what moved downstream.
6. **Return to Build Your Plan** — show whether the step is complete and where the learner goes next.
7. **State the finish line** — distinguish the app checkmark from the human planning decision.

The app checkmark means the required data exists. The Academy checkpoint means the learner understood the trade-off and made the decision deliberately. They should point to the same planning outcome without needing identical wording.

## Provisional course mapping

The final row labels come from the shipped Build Your Plan preview. Until then, this is the walkthrough-routing contract.

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

If the shipped app combines, splits, reorders, or renames an area, first update the walkthrough routing. Change the concept structure only when the financial-planning decision itself has changed or the old order has become harder to follow.

## Walkthrough metadata required before filming

Every core walkthrough must identify:

- `app_step_id`
- `app_step_label`
- `primary_route`
- `planning_decisions_implemented`
- `app_completion_rule`
- `human_completion_rule`
- `demo_household_version`
- `last_verified_app_commit`

A concept lesson may list the Build Your Plan area it supports, but it should not depend on exact button labels or routes. Walkthrough sheets are replaceable and are re-verified whenever the route, label, save behavior, or completion rule changes.

## Number provenance inside every walkthrough

For each important result, the walkthrough says:

- **WHAT IT MEANS**
- **CALCULATED FROM**
- **EDIT SOURCE**
- **THIS AFFECTS**

This is mandatory for outputs such as surplus, reserve target, debt ratios, target allocation, projected tax, plan confidence, earliest retirement date, retirement spending target, first-year funding, Bitcoin sold or retained, and estate readiness.

## Advanced material

Advanced lessons should be discoverable from the Build Your Plan area that makes them relevant. They do not have to become steps in the core walkthrough.

Examples:

- Monte Carlo mechanics → Baseline & assumptions
- Per-holding return and income overrides → Baseline & assumptions
- Bitcoin-backed loans → Debt or Retirement Income, depending on the decision
- Roth conversions and harvesting → Tax
- Pre-Medicare healthcare → Retirement Income
- Trusts and complex custody → Protect

Each advanced lesson begins with one condition visible in the learner's plan:

> **Watch this only if [condition]. Otherwise this part of your plan is complete without it.**

Advanced lessons never block core progress unless the learner's own plan makes the issue necessary.

## Aligned finish lines, not identical structures

`MODULE-CHECKPOINTS.md`, Circle module pages, walkthrough sheets, and the Build Your Plan UI should all point toward the same finished plan. They do not have to use the same number of sections or the same exact language.

When they disagree about the actual work required:

1. verify current shipped app behavior,
2. update this crosswalk,
3. update the affected walkthrough and course checkpoint,
4. update the concept lesson only when the planning decision or explanation changed.

The learner should feel that the course is helping them complete Build Your Plan—not that they are following two separate systems.
