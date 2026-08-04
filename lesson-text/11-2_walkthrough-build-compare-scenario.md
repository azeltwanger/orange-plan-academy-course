# Walkthrough: build and compare a scenario in Orange Plan

Follow along (~15 minutes). Builds two scenarios: one stress test, one choice. Both saved, compared, and Monte Carlo'd.

⚠ **Your baseline has to be real first.** Everything on this page compares against your plan. Stale balances or a spending number you don't believe means you're comparing against fiction. The built-in what-ifs also read your own settings, so a wrong retirement age or state produces the wrong questions.

## The page

**Scenarios** (primary nav). Three zones: **What if...** (built-in presets), **Your scenarios** (*"Saved what-ifs you can reopen and compare"*), and the comparison section below. Top right: **Custom scenario**, plus **Review scenario** once a scenario is selected.

## 1. Create the stress test

**What if... → 50% drawdown after retirement.** One click creates and selects it; the plan re-runs. The description fills in your own retirement age.

The grid shows 4 of 9 presets. **See more scenarios** expands to all of them: Bear Market, 50% drawdown after retirement, Retire earlier, Spend less in retirement, Move to no-tax state, Conservative BTC returns, Moderate BTC returns, Claim Social Security at 62, Claim Social Security at 70.

## 2. Read the comparison

The chip shows the scenario name, then **vs your plan**.

- **Headline row:** Retire at · Spending · Success rate
- **Full comparison metrics** (expand): net worth at retirement, net worth at age 90, lifetime taxes paid, effective tax rate, withdrawal rate at retirement, depletion age, earliest retirement age, BTC at retirement and at life expectancy

Each row shows baseline, scenario, and difference. Matching rows read **no change**.

Ask a stress test exactly one question: **would I still be okay?**

## 3. Run the Monte Carlo

Button **Run Monte Carlo** in the comparison section.

⚠ Until it runs, the success rate isn't a real comparison. The chart updates instantly off the projection, but confidence is a simulation that has to execute.

## 4. Build a custom scenario

**Custom scenario** → **Create scenario** dialog.

1. **Step 1: Choose scenario type.** Seven cards: Life events, Retirement, Savings, Debt, Tax, Markets, Advanced. ⚠ Pick the specific type, not Advanced.
2. **Name + Description.** The placeholder changes with the type. Name it after the *question*, not the answer: "Retire at 55" works, "Better plan" doesn't.
3. **Change one variable.** Save.

## 5. Compare, then manage

Select it under **Your scenarios**, read the headline row, expand full metrics, run the Monte Carlo.

The **⋯** menu gives **Duplicate**, **Edit**, **Delete**. Duplicate is how you build a second scenario differing by exactly one thing without rebuilding it.

⚠ Nothing on this page touches your plan, which is exactly why you can experiment freely.

## 6. AI: Review scenario

Only renders with a scenario selected and the editor closed. It reads your saved scenarios, projection years, life events, and assumptions, and asks which scenario to compare against your plan. Run it when a comparison needs explaining to someone else, or when you can't tell why two scenarios differ. It explains and compares; it doesn't decide.

## Done when

- Two scenarios saved: one stress test, one choice
- Both Monte Carlo'd, so the success rates are real
- The stress test answered out loud, with a lever named if the answer was no
- One variable per scenario, and you can say which
- Your baseline is untouched
- Names that are questions, still readable a year from now

These also unlock the report's "If Bitcoin follows a different path" section, which doesn't render without at least one saved scenario.
