# Bitcoin-backed loans: how they actually work

You pledge Bitcoin as collateral, a lender holds it and gives you cash, you pay interest, and when you repay you get the Bitcoin back. Because you didn't sell, there's usually no taxable event and you keep the upside. The danger: your collateral is the most volatile asset you own, and the lender's protection against that is the right to sell it without asking you.

## LTV: the number that runs everything

**Loan balance ÷ collateral value.** Borrow $50,000 against $200,000 of Bitcoin = 25% LTV.

Two things move it. Your balance creeps up as interest accrues (slow, predictable). Your collateral moves with the Bitcoin price (fast, unpredictable).

**LTV rises faster than the price falls**, because the price is in the denominator:

| Price falls | A 25% LTV becomes |
|---|---|
| 50% | 50% |
| 70% | 83% |
| 80% | 125% (loan exceeds collateral) |

Starting LTV is the only variable you control before the market takes over.

## The three lines

1. **Margin call** (often ~65–70%). The lender contacts you and gives you a window, sometimes 24–72 hours, to fix it.
2. **Liquidation** (often ~80–85%). Cross it, or miss the margin-call window, and the lender sells your Bitcoin. You don't get a vote.
3. **Release** (varies). If the price rises and your LTV drops well below where you started, many lenders release collateral back to you.

## What you can do at a margin call

- **Top up**: send more Bitcoin as collateral. Requires unpledged Bitcoin you can move fast.
- **Pay down**: send cash to cut the balance. Requires cash in the exact week your net worth is falling.
- **Do nothing**: the lender liquidates at whatever the price is that day.

⚠ Two of the three require something held in reserve. A loan with every satoshi pledged and no cash cushion has one option, and it's the bad one.

**Partial liquidation** sells only enough to get you back under the line and the loan continues. **Full liquidation** closes the whole position. Ask which one your lender does.

## Types of provider

- **Custodial**: they hold your Bitcoin. Simplest, and legally it's theirs. If they fail you're a creditor. Several large ones failed in 2022 and customers lost everything.
- **Collaborative custody**: collateral sits in multisig (often 2-of-3) with you, the lender, and a third party each holding a key. The lender can't move it alone.

**Rehypothecation is the question that separates them.** It means the lender loans your collateral out to someone else while holding it, and it's the practice most responsible for the 2022 failures. Ask directly, get it in writing, and treat anything short of a clear "no" as a risk unrelated to the Bitcoin price.

**Seven questions for any provider:**

1. Do you rehypothecate collateral?
2. Custodial or collaborative multisig, and who holds which key?
3. Your exact margin call and liquidation LTVs?
4. How much notice at a margin call, and how do you contact me?
5. Partial or full liquidation?
6. Do you release collateral when LTV falls, automatically or on request?
7. Rate, fixed or variable, and any origination or early-repayment fees?

## Worked example

The couple pledges 1.75 BTC (worth $175,000 at an illustrative $100,000/coin) and borrows $35,000 for a renovation. **20% starting LTV.**

| BTC price | Collateral | LTV | Status |
|---|---|---|---|
| $100,000 | $175,000 | 20% | Comfortable |
| $70,000 | $122,500 | 29% | Normal correction |
| $50,000 | $87,500 | 40% | Half the value gone, still fine |
| $30,000 | $52,500 | 67% | Margin call |
| $25,000 | $43,750 | 80% | Liquidation |

A 75% drawdown (a normal Bitcoin bear) takes 20% LTV to the edge. That's what starting at 20% buys: it survives a normal bear, barely. **The same loan at 50% starting LTV hits a margin call on a 40% drop**, which is an ordinary Tuesday in Bitcoin.

## Rules before you borrow

1. Start low enough to survive a 70–80% drawdown. Usually 20–25%, not the 40–50% a lender will offer.
2. Keep unpledged Bitcoin or cash you can reach fast.
3. Know your lender's three lines and write them down.
4. Decide your action at each line now, in writing, while nothing is falling.
5. Never borrow for something you can't stop paying for.

## In the app

**Strategy → Debt → Add debt**, Bitcoin-backed type. Enter lender, start date, term, **collateral in BTC quantity** (not dollars), **Margin call LTV**, **Liquidation LTV**, **Auto top-up**, and **Liquidation strategy** (Full or Partial).

⚠ Enter your lender's real thresholds. The defaults are common values, and a plan built on the wrong lines tells you a comforting story that isn't yours.

**Strategy → Debt → Collateral rules** models the behavior across the projection: *Auto top-up (global default)* · *Margin call %* (triggers top-up) · *Top-up target %* (what it tops back down to) · *Liquidation %* · *Release trigger %*.

**How it's modeled:** the engine walks the loan year by year alongside the Bitcoin price path. Interest accrues, price moves, LTV recalculates. Cross the top-up trigger and it tops up from available Bitcoin; cross liquidation and it sells per your strategy. Pledged Bitcoin is protected from ordinary withdrawals, so the plan won't spend collateral you've committed. **Collateral release is modeled too**, so a rising price frees pledged Bitcoin back into your plan.

Run a 50% drawdown scenario with the loan in place and you're seeing its real behavior, not an assumption.

## Your decision

**Whether to borrow at all, and if so, at what starting LTV and with which provider.**

1. **Start with whether you need the money.** The cheapest loan is the one you don't take.
2. **Compare honestly against selling.** Selling costs tax and upside. Borrowing costs interest and adds liquidation risk. One is expensive, the other is risky.
3. **Pick your starting LTV from the drawdown you want to survive**, not from what you're allowed to borrow.
4. **Pick the provider on structure, not rate.** A better rate at a lender who rehypothecates isn't a better deal.
5. **If you couldn't fund a margin call, you can't afford the loan.**

## Homework

1. Decide whether a Bitcoin-backed loan belongs in your plan at all. "No" is legitimate and common.
2. If considering one, take the 7 questions to two or three lenders and compare answers side by side.
3. Write your maximum starting LTV and your action at each of the three lines.
4. Model it in the app with real thresholds, then run the 50% drawdown scenario against it.
