# Borrow against Bitcoin without getting liquidated

**Gate:** only if you are actually considering a Bitcoin-backed loan, or already hold one. If not, skip it. No is the common answer.

You pledge Bitcoin as collateral. A lender holds it and gives you cash. You pay interest. When you repay, your Bitcoin comes back.

- **What makes it interesting:** you did not sell, so in most cases there is no taxable event and you keep the upside.
- **What makes it dangerous:** your collateral is the most volatile asset most people will ever own, and the lender's protection against that volatility is the right to sell your Bitcoin without asking you first.

## LTV, the one number that runs everything

**LTV = loan balance ÷ collateral value.** Borrow $50,000 against $200,000 of Bitcoin and your LTV is 25%.

Two things move it, and only one is in your control. Your **loan balance** rises as interest accrues: slow and predictable. Your **collateral value** moves with the price: fast and not predictable at all.

LTV rises much faster than the price falls, because the price is in the denominator.

| Bitcoin falls | 25% LTV becomes |
|---|---|
| 50% | 50% |
| 70% | ~83% |
| 80% | 125%, the loan is worth more than the collateral |

**Your starting LTV matters more than anything else here.** It is the only variable you control before the market takes over.

## The three lines every loan has

| Line | Typical | What happens |
|---|---|---|
| **Margin call** | ~65 to 70% LTV | The lender contacts you with a window to fix it, sometimes as short as 24 to 72 hours |
| **Liquidation** | ~80 to 85% LTV | The lender sells your Bitcoin to bring the loan back in range. You do not get a vote |
| **Release** | well below your start | Many lenders release collateral back to you, automatically or on request |

Every lender is different. These are shapes, not your numbers.

## Sizing the cushion

The gap between your starting LTV and the liquidation line is the entire drawdown you can live through. $50,000 collateral, 80% liquidation line:

| Borrow | Starting LTV | Liquidation at | Survivable drop |
|---|---|---|---|
| $12,500 | 25% | $15,625 | 69%, inside drawdowns that have happened (2018: −84%, 2022: −77%) |
| $6,250 | 12.5% | $7,812 | 84% |

Halving the starting LTV moves the danger line dramatically further away. **That is the lever, and it is the only one you get.**

**Size the cushion for a 70 to 80% drawdown minimum**, because that is a normal Bitcoin cycle and not a worst case. In practice that means starting somewhere between **10 and 20% LTV**, not the 40 or 50% a lender will happily hand you.

Where you land inside that range is a risk tolerance call, and the ends buy different things:

| Starting LTV | Liquidation at an 80% line | Survives |
|---|---|---|
| 10% | a fall of about 87% | every drawdown in Bitcoin's history |
| 15% | a fall of about 81% | 2022 (−77%), not 2018 (−84%) |
| 20% | a fall of 75% | neither 2022 nor 2018 |

Both ends are defensible. Pick on purpose, and know what the choice costs you.

## A worked example

The couple holds 1.75 BTC. At an illustrative $100,000/coin that is $175,000. They want $35,000 for a kitchen renovation and do not want to sell. They pledge all 1.75 BTC and borrow $35,000: a **20% starting LTV**.

| BTC price | Collateral | LTV | Read |
|---|---|---|---|
| $100,000 | $175,000 | 20% | Comfortable |
| $70,000 | $122,500 | 29% | Normal correction |
| $50,000 | $87,500 | 40% | Half the value gone, still fine |
| $30,000 | $52,500 | 67% | Margin call territory |
| $25,000 | $43,750 | 80% | Liquidation |

A 75% drawdown, a completely normal Bitcoin bear market, takes them from 20% right to the edge. At a **50% starting LTV**, a 40% drop hits the margin call, and a 40% drop is an ordinary Tuesday in Bitcoin.

## What you can do at a margin call

1. **Top up.** Send more Bitcoin as collateral. Requires unpledged Bitcoin you can move quickly.
2. **Pay down.** Send cash to reduce the balance. Requires cash available in exactly the week your net worth is falling.
3. **Do nothing and get liquidated**, at whatever the price is that day.

**Two of the three require something held in reserve.** Pledge every spare satoshi with no cash cushion and you have exactly one option, the bad one. Decide your action at each line in writing, while nothing is falling.

## Partial versus full liquidation

**Partial**: they sell only enough to get you back under the threshold; the loan continues. **Full**: they close the position, settle the loan, and return what is left. Ask which one your lender does before you sign.

## The types of provider

- **Custodial.** You send your Bitcoin and they hold it. Simplest to use. In a legal sense it is their Bitcoin now, and if they fail you are a creditor in line. Several large ones failed in 2022 and their customers lost everything.
- **Collaborative custody.** Collateral sits in a multisig arrangement, often 2-of-3: you hold a key, the lender holds a key, a third party holds a key. The lender cannot move your Bitcoin alone.

**Rehypothecation** separates them: does the lender lend your collateral out to someone else while holding it? It is the practice most directly responsible for the 2022 blowups. Ask directly, get it in writing, and treat anything other than a clear no as a risk that has nothing to do with the Bitcoin price.

**The 7 questions for any provider:**

1. Do you rehypothecate collateral?
2. Are you custodial or collaborative multisig, and who holds which key?
3. What are your exact margin call and liquidation LTVs?
4. How much notice do I get at a margin call, and how do you contact me?
5. Do you do partial or full liquidation?
6. Do you release collateral when LTV falls, and is that automatic or on request?
7. What is the interest rate, fixed or variable, and are there origination or early repayment fees?

⚠ Nothing here tells you to take one of these loans. Terms, margin-call rules, and who actually holds your collateral vary a lot by lender. Read the agreement and run it past somebody who represents you before signing.

## The rules to write down before you borrow

1. Start low enough to survive a 70 to 80% drawdown: somewhere between 10 and 20%, closer to 10 the more of that drawdown you want to live through.
2. Keep unpledged Bitcoin or cash you can reach fast.
3. Know your lender's three lines, written where you will find them.
4. Decide your action at each line in writing, while nothing is falling.
5. Never borrow for something you cannot stop paying for.

## In the app

**Strategy → Debt → Add debt → Bitcoin-backed.** Enter lender, start date and term, collateral in **Bitcoin quantity** rather than dollars, margin call LTV, liquidation LTV, auto top-up, and full or partial liquidation.

⚠ **Enter your lender's real thresholds.** The defaults will tell you a comforting story that is not yours.

**Collateral rules** models the behavior across the whole projection: auto top-up, the margin call percent that triggers it, the top-up target, the liquidation percent, and the release trigger. That last one models **collateral release**, so a rising price frees collateral back into your plan instead of leaving it pledged forever.

**Severity chips** on the loan row:

| Chip | Read |
|---|---|
| near margin call | This week's problem. Reduce LTV |
| margin call | Today's problem. Add collateral or pay down now |
| liquidation zone | Emergency |

A healthy loan shows no cushion sentence and no chip. That is healthy, not missing data.

## Your decision

**Whether to borrow at all, and if so, at what starting LTV and with which provider.**

1. **Start with whether you need the money at all.** The cheapest loan is the one you do not take.
2. **Compare it honestly against selling.** Selling costs tax and upside; borrowing costs interest and adds a liquidation risk. One is expensive, the other is risky, and those are not the same kind of problem.
3. **Pick your starting LTV from the drawdown you want to survive**, not from what you are allowed to borrow.
4. **Pick your provider on structure, not rate.** A better rate at a lender who rehypothecates is not a better deal.

**If you could not fund a margin call, you cannot afford the loan.**

## Homework

1. Decide whether a Bitcoin-backed loan belongs in your plan at all.
2. If you are considering one, take the 7 provider questions to two or three lenders and put their answers side by side.
3. Model it in the app using your lender's real thresholds, and write down your action at each of the three severity levels.
4. Run the 50% drawdown scenario against it and watch what happens.
