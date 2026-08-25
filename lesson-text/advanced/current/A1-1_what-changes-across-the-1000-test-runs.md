# What changes across the 1,000 test runs?

> **Watch this only if you want to inspect the model beneath confidence. Otherwise the Core confidence lesson is enough.**

## What stays fixed

Each run uses the same saved:

- accounts and holdings,
- income and spending,
- debts and life events,
- retirement date and planning age,
- tax inputs,
- contributions,
- and withdrawal strategy.

## What changes

The market-return and inflation sequence changes. Some paths are favorable; others contain declines near retirement or several weak years together.

Confidence is the share of runs where the unchanged saved plan lasts through planning age.

## Common paths for comparisons

Orange Plan uses stable simulated paths when comparing versions of the plan. This reduces sampling noise: if one input changes, the confidence difference is more directly tied to that input rather than a completely different random sample.

## Worked example

- 3% Baseline inflation: **94.6% confidence** at Alex age 55
- 4% inflation Scenario: **91.6% confidence**
- Difference: **−3.0 percentage points**

The Scenario changes the cost growth, not the current lifestyle or the market sample. The result is weaker but does not automatically change the retirement decision.

## Current Bitcoin modeling approach

The current app uses a versioned static assumption set with:

- a fat-tailed, skewed Bitcoin distribution,
- high starting Bitcoin volatility that declines toward a floor,
- explicit return caps,
- asset-specific volatility,
- correlated asset and inflation paths,
- and reproducible comparison paths.

The app receipt owns the exact current settings and review date. They are product assumptions, not permanent facts.

## Avoid overfitting

1. Use one reasonable Baseline.
2. Change one assumption in a Scenario.
3. Prefer decisions that remain acceptable under more than one reasonable view.

## Number provenance

- **What it means:** share of paths where the saved plan lasts
- **Calculated from:** full saved plan and current versioned path assumptions
- **Edit source:** planning inputs and assumptions being tested
- **This affects:** confidence, earliest date, spending references, and Scenario differences

## Done when

The learner can explain what is fixed, what varies, and why the alternate Scenario exists.
