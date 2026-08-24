# Read your retirement date and confidence number

The retirement page shows four related values:

1. **Planned retirement age** — the household retirement start, displayed using the primary person's age
2. **Confidence target** — the minimum standard selected by the learner
3. **Confidence result** — the share of 1,000 test runs that lasted through planning age
4. **Earliest target-qualified date** — the first date that reaches the selected target

## Planned age and spending

The demo household uses:

- Household retirement start: **when Alex is 55**
- Retirement living spending: **$100,000/year in today's dollars**
- Planning age: **95**

The current app uses one household retirement date. Jordan is two years younger, but there is not a separate spouse-retirement-age setting in this saved plan. A March retirement date still creates partial-year household wages before retirement begins.

Baseline spending is annual living spending, not gross income and not debt payments already modeled separately.

The $100,000 retirement lifestyle is deliberately higher than the current $80,000 working-life spending because the household expects more travel and healthcare.

## Confidence target

At an 80% target, the app looks for the first date where at least 800 of 1,000 runs lasted through planning age.

- Higher target generally means more cushion and a later earliest date.
- Lower target may mean an earlier date and more adjustment risk.

Eighty percent is a starting point, not a universal correct answer.

## Canonical demo result

The reproducible engine checkpoint reports:

| Output | Result |
|---|---:|
| Confidence at the household retirement start, Alex age 55 | **94.6%** |
| Earliest date reaching the 80% target | **May 2032 · Alex age 51** |
| Confidence at that boundary | **80.0%** |

A 94.6% result means about 946 of the 1,000 runs lasted through planning age under the saved plan.

It is not a literal 5.4% probability of bankruptcy. The test holds the plan constant; a real household can adjust spending, work, savings, timing, or strategy.

The earliest date changes the household retirement start. The age is labelled using Alex because Alex is the primary person. Each spouse's Social Security still keeps its own start age.

The output creates options; it does not automatically tell the household to move retirement from 55 to 51.

## One test-run framework

Read confidence at the planned age and the earliest date meeting the target together. Both come from the same test-run process; there is no separate deterministic retirement result being compared with Monte Carlo.

The Plan target is separate from the starting-spending choices and annual spending guardrails on the Income page.

## Where confidence comes from

- **What it means:** share of runs lasting through planning age
- **Calculated from:** the entire saved plan, including the household income transition at retirement
- **Edit source:** the underlying input or decision being tested
- **This affects:** the plan verdict and earliest target-qualified date

## Done when

The learner can explain all four numbers, identify that the displayed age controls the household retirement start, defend the spending input, and name one lever to test rather than changing several inputs at once.
