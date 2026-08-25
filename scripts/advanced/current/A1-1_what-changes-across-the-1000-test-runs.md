TELEPROMPTER SCRIPT — Advanced A1.1
A1.1 What changes across the 1,000 test runs?
~7 min at 155 wpm · VOICE-MATCHED DRAFT — Austin review + app assumption receipt pending
============================================================

> **Watch this only if you want to understand what sits underneath the confidence result or you are deciding whether to trust the current model. Otherwise the Core explanation of confidence is enough.**

The real question is not whether Monte Carlo can predict the future.

It cannot.

The useful question is: **what does Orange Plan hold constant, what changes across the 1,000 test runs, and why does that make the confidence result more useful than one straight-line projection?**

== THE PLAN STAYS THE SAME ==

Each test run starts with the same saved household.

The account balances, Bitcoin quantity, debts, income, spending, life events, retirement date, tax settings, contribution plan, and withdrawal strategy are the plan being tested.

Orange Plan does not secretly improve the plan in the good runs or weaken it in the bad ones.

What changes is the market and inflation experience the saved plan has to live through.

Some runs get strong returns early. Some get a major decline close to retirement. Some get several weak years together. Inflation can also arrive differently, which changes what the spending target costs over time.

The confidence result is the share of those runs where the saved plan lasted through the planning age without the household changing the plan.

== WHY THE PATHS STAY THE SAME WHEN YOU COMPARE A DECISION ==

Orange Plan uses a stable set of simulated market paths when you compare one version of the plan with another.

That matters.

Imagine changing inflation from 3% to 4% and then also giving the new version 1,000 entirely different markets. If confidence falls, you would not know how much came from inflation and how much came from a luckier or worse random sample.

Using the same market paths on both sides makes the difference easier to interpret. The household changed one input; the simulated markets stayed comparable.

== WORK THE DEMO INFLATION TEST ==

The demo household retires when Alex is 55 and spends $100,000 a year in today's dollars.

With 3% inflation, the current engine candidate produces **94.6% confidence** at that retirement date.

The household then changes only inflation to 4% in a Scenario. The same retirement date, same spending today, same holdings, same contributions, and same saved strategy remain in place.

Confidence falls to **91.6%**.

That 3-point change is not saying 4% inflation will happen. It is showing what one additional point of annual spending growth does to this plan across the same test environment.

The result also tells us something useful about the decision. The plan becomes weaker, but the household does not suddenly need to abandon age 55. It still has substantial cushion.

That is how I would use Monte Carlo: not to search for one perfect probability, but to see which decision meaningfully changes the plan.

== WHY BITCOIN IS NOT MODELED LIKE A BOND FUND ==

The current Orange Plan assumptions use a fat-tailed Bitcoin return distribution rather than a normal bell curve.

That means extreme positive and negative years remain more likely than they would in a normal model. The current static assumption set also starts Bitcoin volatility high and lets it decline toward a floor as the projection moves forward.

Stocks, bonds, real estate, cash, inflation, and the other modeled assets have their own volatility and relationships. The paths are correlated rather than pretending every asset moves independently.

The maintained app receipt owns the exact version, dates, caps, volatility settings, and correlation matrix. Those are current product assumptions, not permanent financial laws.

The Advanced lesson should help you understand the model. It should not encourage you to tune every statistical control until the answer looks better.

== WHAT THE MODEL STILL DOES NOT KNOW ==

It does not know the order of future returns.

It does not know whether a tax law changes, a lender fails, a family member needs support, or the household changes spending during a bad period.

And it cannot prove that the current Bitcoin model is the right model for the next 40 years.

What it can do is test the same financial plan across many difficult and favorable sequences using one explicit set of assumptions.

That is more honest than one smooth line, as long as the assumptions and source data are kept current.

== THREE WAYS TO USE THIS WITHOUT OVERFITTING ==

First, use the built-in model as the Baseline unless you have a real reason to change it.

Second, test one reasonable alternate view as a Scenario. Lower Bitcoin returns, higher inflation, or a major drawdown near retirement can answer a real question.

Third, look for a decision that remains acceptable across more than one reasonable view. A plan that works only under the most favorable assumption is fragile even when the screen shows a precise number.

== WHERE THE NUMBER COMES FROM ==

**What it means:** the share of simulated market and inflation paths where the saved plan lasts through the planning age.

**Calculated from:** the full saved plan applied to the current versioned Monte Carlo assumptions and paths.

**Edit source:** the household inputs and assumptions being tested; the statistical model itself is product-owned.

**This affects:** confidence, earliest target-qualified date, spending references, Scenario differences, and strategy-risk results.

== YOUR DECISION ==

Decide whether the built-in model is a reasonable Baseline for this plan and which one alternate assumption is worth testing.

== PUT IT IN ORANGE PLAN ==

Review the current assumptions receipt, keep the Baseline intact, and create a Scenario that changes one assumption rather than several.

== YOU ARE DONE WHEN ==

You can explain what stays fixed, what changes across the test runs, why the same paths are used for comparisons, and which decision the alternate Scenario is supposed to test.

**Return to Core:** update the Baseline only when your underlying planning view changed. Otherwise keep the alternate view in Scenarios and return to the retirement result.
