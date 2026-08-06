TELEPROMPTER SCRIPT — segment 5.4
5.4 Bitcoin-backed loans: how they actually work
1976 words · ~12.7 min at 155 wpm
============================================================

This is the highest-stakes lesson in the course, so I'm going to go slowly and cover the whole mechanism before we talk about whether you'd want one.

== WHAT A BITCOIN-BACKED LOAN ACTUALLY IS ==

You pledge Bitcoin as collateral. A lender holds it and gives you cash. You pay interest. When you repay the loan, you get your Bitcoin back.

That's the whole product. What makes it interesting is that you didn't sell, so in most cases there's no taxable event, and you still own the upside if the price rises.

What makes it dangerous is that your collateral is the most volatile asset most people will ever own, and the lender's protection against that volatility is the right to sell your Bitcoin without asking you.

== LTV: THE ONE NUMBER THAT RUNS EVERYTHING ==

LTV means loan-to-value. It's your loan balance divided by the value of your collateral.

Borrow $50,000 against $200,000 of Bitcoin, and your LTV is 25%.

Two things move that number, and only one of them is in your control:

- Your loan balance goes up as interest accrues, if you're not paying it down. That's slow and predictable.
- Your collateral value moves with the Bitcoin price. That's fast and it is not predictable.

Here's the part people underestimate. LTV rises much faster than the price falls, because the price is in the denominator.

Start at 25% LTV. If Bitcoin falls 50%, your LTV doesn't go to 50%, it goes to 50% — your collateral halved, so the same loan is now half-covered. Fall 70%, and 25% LTV becomes 83%. Fall 80%, and it becomes 125%, meaning your loan is worth more than your collateral.

That's why starting LTV matters more than any other decision in this lesson. It's the only variable you control before the market takes over.

== THE THREE LINES EVERY LOAN HAS ==

Your lender sets three thresholds. Learn them as a sequence, because that's how you'll experience them:

1. The margin call line. Typically somewhere around 65 to 70% LTV, but every lender is different. When you cross it, the lender contacts you and gives you a window, sometimes 24 to 72 hours, to fix it.

2. The liquidation line. Typically around 80 to 85%. If you cross this, or if you don't fix a margin call in time, the lender sells your Bitcoin to bring the loan back into range. You don't get a vote.

3. The release line. This one's the good news, and a lot of borrowers don't know it exists. If the price rises enough that your LTV drops well below where you started, many lenders will release some collateral back to you, or let you request it.

== WHAT YOU CAN ACTUALLY DO AT A MARGIN CALL ==

You have three options, and you should know which one is yours before you ever get the call:

- Top up. Send more Bitcoin as collateral. This lowers your LTV without selling anything, and it's the option most people take. But it means you have to be holding unpledged Bitcoin you can send quickly.
- Pay down. Send cash to reduce the loan balance. Same effect on LTV, from the other direction. This requires cash on hand in exactly the week your net worth is falling.
- Do nothing and get liquidated. The lender sells enough of your Bitcoin to fix the ratio, at whatever the price is that day, which by definition is a bad price.

⚠ Notice that two of your three options require you to have something in reserve. A loan taken with every spare satoshi already pledged and no cash cushion has exactly one option at a margin call, and it's the bad one.

== PARTIAL VERSUS FULL LIQUIDATION ==

If it comes to liquidation, lenders handle it differently, and the app models both:

- Partial liquidation sells only enough collateral to bring you back under the threshold. You keep the rest and the loan continues.
- Full liquidation closes the entire position. The loan is settled and your remaining collateral, if any, comes back to you.

Ask your lender which one they do before you sign. It changes what a bad month costs you.

== THE TYPES OF PROVIDER ==

You don't need me to name specific companies, because the landscape changes and any list I give you goes stale. What doesn't change is the structure, so learn to sort providers into these buckets:

Custodial lenders. You send your Bitcoin to the company and they hold it. Simplest to use. The risk is the one you already learned in the custody module: it's their Bitcoin now, in a legal sense, and if they fail you're a creditor. Several large ones failed in 2022 and customers lost everything.

Collaborative-custody lenders. Your collateral sits in a multisig arrangement, often 2-of-3, where you hold a key, the lender holds a key, and a third party holds a key. The lender cannot move your Bitcoin unilaterally. This structure is the reason a lot of Bitcoiners will use one of these and never a custodial one.

Rehypothecation is the question that separates them. Rehypothecation means the lender lends out your collateral to somebody else while they're holding it. It's the practice most directly responsible for the 2022 failures. Ask directly: do you rehypothecate my collateral? Get the answer in writing. If the answer is anything other than a clear no, you're taking a risk that has nothing to do with the Bitcoin price.

The questions to ask any provider:

1. Do you rehypothecate collateral?
2. Custodial or collaborative multisig, and who holds which key?
3. What are your exact margin call and liquidation LTVs?
4. How much notice do I get at a margin call, and how do you contact me?
5. Partial or full liquidation?
6. Do you release collateral when LTV falls, and is it automatic or on request?
7. What's the interest rate, is it fixed or variable, and are there origination or early-repayment fees?

== A WORKED EXAMPLE ==

The couple holds 1.75 Bitcoin. At an illustrative $100,000 a coin, that's $175,000.

They want $35,000 for a kitchen renovation, and they don't want to sell, because selling would trigger a taxable gain and they'd be giving up the upside.

At a 20% starting LTV, they pledge all 1.75 BTC and borrow $35,000.

Now walk the price down and watch what happens to that ratio:

┄┄ TABLE (REFERENCE — not prompter-readable; the spoken read must be written above this during voice conversion) ┄┄
| Bitcoin price | Collateral value | LTV | Where they stand |
|---|---|---|---|
| $100,000 | $175,000 | 20% | Comfortable |
| $70,000 | $122,500 | 29% | Normal correction, fine |
| $50,000 | $87,500 | 40% | Half the value gone, still fine |
| $30,000 | $52,500 | 67% | Margin call territory |
| $25,000 | $43,750 | 80% | Liquidation |
┄┄ end table ┄┄

A 75% drawdown, which is a normal Bitcoin bear market, takes them from 20% to the edge. That's what starting at 20% buys you: it survives a normal bear, and it barely survives.

Run the same loan at 50% starting LTV and a 40% price drop hits the margin call. A 40% drop is an ordinary Tuesday in Bitcoin, not a bear market.

== THE RULES TO WRITE DOWN BEFORE YOU BORROW ==

1. Start low enough to survive a 70 to 80% drawdown. For most people that means 20 to 25%, not the 40 or 50% a lender will happily give you.
2. Keep unpledged Bitcoin or cash you can reach fast, so a margin call has a good answer.
3. Know your lender's three lines and write them down where you'll find them.
4. Decide your action at each line now, in writing, while nothing is falling.
5. Never borrow for something you can't stop paying for. A loan against a volatile asset funding a fixed obligation is how people get forced out at the bottom.

== NOW PUT IT IN THE APP ==

Orange Plan models all of this, and it models it as a real position in your plan rather than a calculator off to the side.

Adding the loan: Strategy → Debt → Add debt, and choose the Bitcoin-backed type. The form asks for the things that actually matter:

┄┄ TABLE (REFERENCE — not prompter-readable; the spoken read must be written above this during voice conversion) ┄┄
| Field | What to enter |
|---|---|
| Lender | Whoever you're using (the placeholder shows examples) |
| Start date · Term (months) · Maturity / renewal | Your actual terms |
| Collateral (BTC) | The quantity pledged, not the dollar value |
| Margin call LTV (%) | Your lender's number, not a default |
| Liquidation LTV (%) | Your lender's number |
| Auto top-up collateral | On or off, matching what you'd actually do |
| Liquidation strategy | Full or Partial, matching your lender |
┄┄ end table ┄┄

⚠ Enter your lender's real thresholds. The app ships with common defaults, and a plan modeled on the wrong lines will tell you a comforting story that isn't yours.

The collateral rules: Strategy → Debt → Collateral rules. This is where the behavior gets modeled across the whole projection:

- Auto top-up (global default) turns automatic topping-up on or off
- Margin call % is the LTV that triggers a top-up
- Top-up target % is the LTV it tops back down to
- Liquidation % is where forced selling happens
- Release trigger % is the LTV below which collateral comes back to you

That last one matters and it's easy to miss. The app models collateral release, so if Bitcoin rises and your LTV falls below the release trigger, the projection frees that collateral back into your plan rather than leaving it pledged forever.

How it's modeled: the engine walks your loan year by year alongside the Bitcoin price path. Interest accrues, the price moves, LTV is recalculated, and if it crosses your top-up trigger the model tops up from available Bitcoin. If it crosses liquidation, the model sells according to your liquidation strategy and records it. Pledged Bitcoin stays protected from ordinary withdrawals, so the plan won't spend collateral you've already committed.

That means when you run a 50% drawdown scenario with a loan in place, you're seeing the loan's actual behavior in that drawdown, not an assumption.

== YOUR DECISION ==

Whether to borrow at all, and if so, at what starting LTV and with which provider.

How to think about it:

1. Start with whether you need the money at all, because the cheapest loan is the one you don't take.
2. Compare it honestly against just selling. Selling costs you tax and upside. Borrowing costs you interest and adds a liquidation risk that selling doesn't have. One is expensive, the other is risky, and they're not the same kind of problem.
3. Pick your starting LTV from the drawdown you want to survive, not from what you're allowed to borrow.
4. Pick the provider on structure, not on rate. A slightly better rate at a lender who rehypothecates your collateral is not a better deal.
5. If you can't fund a margin call, you can't afford the loan. That's the honest test.

== HOMEWORK ==

1. Decide whether a Bitcoin-backed loan belongs in your plan at all. "No" is a completely legitimate and common answer.
2. If you're considering one, take the 7 provider questions to two or three lenders and write down their answers side by side.
3. Write your maximum starting LTV, and your specific action at each of the three lines.
4. Model it in the app with your lender's real thresholds, then run the 50% drawdown scenario against it and see what happens.
