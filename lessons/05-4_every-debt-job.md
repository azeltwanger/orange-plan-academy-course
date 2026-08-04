<artifact
  data-placement-id="outcomes-6a64f09fbcc6a9b2091e5400"
  data-artifact-id="6a6754643a9be21a8d113311"
  data-params='{"items":["Break the \u0027pay off debt or invest?\u0027 question into three separate decisions","Sort each debt into eliminate, evaluate, strategic, or monitor by its rate","Give every debt on your balance sheet a job and a reason"]}'
></artifact>

# Every debt gets a job

The module finishes when every debt on your balance sheet has a **job** attached to it, with a reason why.

## Three questions, not one

When there's surplus money at the end of the month, most people ask one question: *"Should I pay off debt first?"*

That's actually three separate decisions:

1. **Keep stacking.** Continue Bitcoin accumulation from monthly surplus.
2. **Pay down faster.** Accelerate payoff on debt you already have.
3. **Add new leverage.** Take on new debt to buy Bitcoin.

Each one gets a different standard, because each one carries a different risk:

- **Buying Bitcoin from surplus** risks money you already own.
- **Paying debt down faster** trades a guaranteed return for flexibility you give up.
- **Adding new leverage** risks money you don't have yet, against an asset that can fall 80%.

Austin's own household in one year: yes on 1, no on 2 (kept the mortgage), no on 3 (didn't add new leverage). Three separate answers on one balance sheet.

## The six possible jobs

Every debt on your list gets one of these, plus a reason:

- **Minimum only.** Pay the required payment, nothing extra.
- **Extra principal.** Pay above the minimum.
- **Refinance.** Get a better rate.
- **Consolidate.** Combine at a better rate.
- **Pay off in full.** Kill it.
- **Monitor.** For asset-backed loans, watched by LTV and cushion, not by rate.

## The four tiers (by rate)

| Tier | Rate | Default job |
|---|---|---|
| **Eliminate** | Over 10% | Kill it. This debt is a guaranteed loss you can't outrun. |
| **Evaluate** | 7 to 10% | Situational. Depends on your balance sheet and tolerance. |
| **Strategic** | Under 7% | Cheap money doing a job. Prepaying just locks in the rate. |
| **Monitor** | Asset-backed | Watch the LTV cushion, not the rate. |

The thresholds are set against what your money reasonably earns. Above 10% beats almost any investment; under 7% doesn't. The 7-10% band is where the tie gets broken by your own numbers.

The app renders these as **Low-cost (under 7%)**, **Mid-cost (7 to 10%)**, and **High-cost (over 10%)**, with Bitcoin-backed loans in a separate **Monitor** bucket.

## Running the couple's debts

| Debt | Rate | Tier | Job |
|---|---|---|---|
| $280,000 mortgage | 3.25% | Strategic | Minimum only |
| $18,000 car loan | 7% | Evaluate | Minimum only |

**Mortgage.** At 3.25% versus a 20% Bitcoin growth assumption, the interest saved from prepaying is dwarfed by the Bitcoin foregone. Keep it, as long as the payment is comfortable and the reserve is solid.

**Car loan.** Sits at the Strategic/Evaluate boundary. Their DTI is 12% (nowhere near strained), so the payment isn't hurting anything. Killing it from cash would drop the reserve below target for 1.5 points of balance-sheet improvement, which isn't worth the trade. Keep it on minimums.

They have no Bitcoin-backed loan, so no debt in the Monitor tier.

## Homework

Line up every debt with its rate. Assign each one to a tier and write down the job and the reason:

- 24% credit card → Eliminate. Guaranteed 24% loss.
- 8% car loan → Evaluate. Depends on your DTI and reserve.
- 5.5% student loan → Strategic. Below expected returns.
- 3% mortgage → Strategic. Keep on purpose.
- 25% LTV Bitcoin-backed loan → Monitor. Watch the cushion.

Every debt should have a decision, not a feeling.


So let's put a job on every row.

## Now put it in the app

### Step 5: Give every debt a job

**Strategy → Debt → the ledger**, grouped into **High-cost** and **Low-cost**.

Each row has an inline selector in its subline. Three options:

| Option | Then enter |
|---|---|
| Minimum payments | (n/a) |
| Extra payments | A **$/mo** field appears with *"/mo extra"* alongside it. |
| Lump sum payoff | Amount (**Full balance** placeholder) plus a date. |

Right-hand status on each row:

- A **payoff month** target date.
- **minimums ok** for low-cost and open-ended.
- **no payoff path** if the row is deliberately open-ended, or unpayable at current terms.

⚠ A mortgage or margin row offers a different option set: **Interest only**, or **Let interest accrue** / **Pay interest monthly**. Those replace the standard three.

#### The job assignment rule

- The group (High-cost or Low-cost) is the app's read. Your job can differ, but you have to say why.
- Every row needs a job. The module is done when every row has one.

Default jobs by band:

| App group | Rate | Default job |
|---|---|---|
| High-cost (over 10%) | Above 10% | Lump sum payoff with a date, or Extra payments if the balance is too big to lump. |
| Low-cost (under 10%) | 3.25% mortgage, low-rate auto | Minimum payments. Held on purpose. |
| BTC-backed | Usually 7 to 10% | Minimum payments, with LTV monitored (Step 6). |

⚠ A 20%+ credit card on anything other than **Lump sum payoff with a date** is the one hard call in this module. Do it, or explain why you're not.

⚠ With no high-cost debts, only **Low-cost** renders, which is the healthy read. The app hides empty groups.


### Route the extra dollars

**Cash Flow → Routing · waterfall order → step 2 Extra debt.** Managed on the Debt page, shown on Cash Flow. One number, two screens.
### Step 8: Run the AI review on debt strategy

**Strategy → Debt → Review Debt Strategy** (page header, beside Add debt). Mobile label: **Review debt**.

The review reads your debt context, the verdict line you just read, and your tax context. It can also run a Bitcoin-loan scenario if you have one.

It asks: *"Do you want the fastest next move, or a full review of payoff order, payment burden, and leverage?"*

Take the full review.

Read at least one thing it surfaced out loud and say whether you agree. Your tolerance can override the math. Show that.

**When to run it:** after every debt has a job. It's a second read on payoff order and leverage, not a substitute for the decisions you just made.

⚠ The review explains and reviews. It isn't advice, and it will never name a specific lender or rate.

With a Bitcoin-backed loan in your plan, the panel adds a **BTC-loan safety check** to the menu.


Every row has a job. Last thing is to check the work.
