TELEPROMPTER SCRIPT — segment 6.1
6.1 Build the retirement spending target, income floor, and portfolio gap
~8 min at 155 wpm · VOICE-MATCHED DRAFT — Austin review pending
============================================================

Retirement income starts with three numbers:

- what the household wants the plan to support,
- what income arrives without selling an asset,
- and what still has to come from the portfolio.

Once those are clear, the bridge years and first-year funding calculation make sense.

== RETIREMENT SPENDING ==

The spending target is annual living spending, not gross income and not debt payments already modeled on their own rows.

Module 2 already separated normal, bare-bones, irregular, and one-time costs. Here we decide which version of life retirement is supposed to fund.

The demo household currently spends $80,000 a year outside debt. It plans for $100,000 of retirement living spending in today's dollars because the early retirement years include more travel and a higher healthcare allowance.

That difference is deliberate. It is not a number that changed because the plan needed a better result.

A dated roof, vehicle, move, or another specific large cost belongs in a life event. A reasonable amount for recurring travel, gifts, and ordinary irregular costs can remain in the annual spending target. Do not count the same cost both ways.

Taxes and any debt still outstanding are modeled separately. So when a retirement-year cash need is higher than $100,000, open the year and see which line created the difference rather than assuming the living-spending input changed.

== THE INCOME FLOOR CHANGES OVER TIME ==

The income floor is money expected to arrive without selling investments.

It can include Social Security, a pension, verified rental or other recurring income, and part-time work during the years the household genuinely plans to earn it.

The demo household plans $20,000 of part-time income during its first 3 retirement years. At age 67, it expects about $52,000 a year of combined Social Security and other durable income in today's dollars.

Those inputs need their real start and end dates. Income that begins at 67 does not fund retirement at 55.

The floor is a timeline, not one permanent number. One spouse may claim before the other, part-time work may end, a pension may begin, or a rental may be sold.

== THE PORTFOLIO-FUNDED GAP ==

The simple living-spending gap is:

> Retirement living spending − recurring income = portfolio-funded gap

During the first 3 retirement years, $100,000 of living spending minus $20,000 of part-time income leaves an $80,000 living-spending gap before taxes, remaining debt, life events, or reserve refill.

After the $52,000 durable income begins, the same $100,000 lifestyle has a $48,000 living-spending gap before those other costs.

The gap is not a sign that the plan failed. It is the part of retirement the investments are supposed to provide.

== TOTAL DRAW IS THE FULL APP CALCULATION ==

The Income page takes the simple idea one step further.

On the left, it shows what the year needs:

- spending,
- taxes and debt costs when applicable,
- and a reserve refill when the saved policy calls for one.

Then it subtracts recurring income.

What remains is the **total draw** from accounts.

The other side shows where that draw comes from, by account and holding when the current projection can identify it.

This is the answer when someone asks why the withdrawal is higher than the spending target. The source is usually tax, debt, a life event, or refill—not a second hidden spending number.

The actual first-year taxes, total draw, and source split for the canonical demo must come from the current `demo-v1-income` checkpoint. They should not be invented in the script.

== PRICE THE BRIDGE YEAR BY YEAR ==

The income bridge runs from retirement until the later income floor turns on.

For the demo household, retirement starts at 55, part-time income ends after 3 years, and the full later income begins at 67. The portfolio job changes during that span rather than remaining one flat annual amount.

There can also be an account-access bridge when a household retires before a particular retirement account can be used without a penalty, exception, or special strategy.

Do not reduce that to “everything unlocks at 59½.” Account type, employment separation, Roth basis, plan rules, and current law can change the available options. The implementation belongs with the current tax review.

The useful question is whether accessible cash and Bridge assets cover the year-by-year draw without forcing the wrong account or a Bitcoin sale during a major decline.

== SOCIAL SECURITY IS A FULL-PLAN COMPARISON ==

Claiming earlier can shorten the period when the portfolio carries the full gap. Waiting can increase the monthly benefit under the current formula while requiring more portfolio funding first.

Compare both effects in the full plan. Health, longevity, spouse and survivor benefits, taxes, portfolio volatility, and the value of earlier cash flow all matter.

Use the current Social Security records and verify the final decision under the rules in effect when claiming is close.

== THE RETIREMENT CASH BUFFER ==

The working reserve protected a lost paycheck. The retirement cash buffer protects portfolio-funded spending.

Cash Flow owns the selected basis and target months. Income shows how the current cash fits the retirement plan.

If the page reports 8 of 18 months funded, that comes from reserve cash divided by the selected monthly basis. It is not 8 months of gross income or 8 months of the entire portfolio.

Build the target before retirement rather than after the first drawdown begins.

== WHERE THESE NUMBERS COME FROM ==

For retirement spending:

**What it means:** annual living spending the saved plan is expected to support.

**Calculated from:** the Baseline spending input and dated life events.

**Edit source:** Plan spending and the specific event—not the Income output.

**This affects:** cash need, confidence, earliest date, spending bands, tax, and withdrawals.

For recurring income:

**What it means:** modeled income arriving without portfolio sales.

**Calculated from:** Social Security, pensions, work, rental, and other verified sources in each year.

**Edit source:** the underlying income record and dates.

**This affects:** gap, Bridge, total draw, tax, and reserve need.

For total draw:

**What it means:** amount needed from accounts after recurring income.

**Calculated from:** spending, tax, debt, life events, refill, and recurring income.

**Edit source:** whichever underlying line created the amount.

**This affects:** account sales, Bitcoin retained, taxes, loans, and long-term results.

== YOUR DECISION ==

Choose the retirement living-spending target, the recurring income sources the household is actually counting on, and whether accessible assets can cover the changing bridge before the full floor begins.

== PUT IT IN ORANGE PLAN ==

Confirm Baseline spending on Plan, verify every retirement-income source and date, and read the current first-year funding calculation on Plan → Income.

Set the cash-buffer basis and months in Cash Flow.

== YOU ARE DONE WHEN ==

You can explain spending, recurring income, the living-spending gap, the full total draw, and the early Bridge without relying on one future Bitcoin price.
