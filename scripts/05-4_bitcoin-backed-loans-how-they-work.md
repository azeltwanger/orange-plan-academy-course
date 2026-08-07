TELEPROMPTER SCRIPT — segment 5.4
5.4 Bitcoin-backed loans: how they actually work
~14 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
============================================================

In today's lesson, we're going to cover Bitcoin-backed loans: how they actually work, how the numbers move, and what happens when they go wrong.

This is the highest-stakes lesson in the course, so I'm going to cover the whole mechanism before we get anywhere near whether you'd want one.

== WHAT A BITCOIN-BACKED LOAN ACTUALLY IS ==

You pledge some Bitcoin as collateral. A lender holds it, and gives you cash. You pay interest on that cash. And when you pay the loan back, you get your Bitcoin returned to you.

That's the whole product.

What makes it interesting is that you didn't sell. So in most cases there's no taxable event, and you still own the upside if the price goes up.

What makes it dangerous is that your collateral is the most volatile asset that most people will ever own, and the lender's protection against that volatility is the right to sell your Bitcoin without asking you first.

== LTV, THE ONE NUMBER THAT RUNS EVERYTHING ==

LTV stands for loan-to-value. It's just your loan balance divided by what your collateral is worth.

So if you borrow $50,000 against $200,000 of Bitcoin, your LTV is 25%.

There are two things that move that number, and only one of them is in your control.

The first one is your loan balance, which goes up as interest accrues if you're not paying it down. That part is slow and predictable.

The second one is your collateral value, which moves with the Bitcoin price. That part is fast, and it is not predictable at all.

🎬 GRAPHIC (the most important visual in this lesson): Bitcoin price line falling while the LTV bar climbs. Mark the margin call line and the liquidation line as fixed horizontal lines so the viewer watches LTV cross them.

LTV rises a lot faster than the price falls, and that's because the price is in the denominator. People underestimate this every time.

Say you start at 25% LTV. If Bitcoin falls 50%, your collateral just got cut in half, so that same loan is now covering half as much, and your LTV goes to 50%. If Bitcoin falls 70%, your 25% LTV becomes about 83%. And if it falls 80%, you're at 125%, which means your loan is now worth more than the Bitcoin backing it.

That's why your starting LTV matters more than anything else in this lesson. It's the only variable you actually control before the market takes over.

== THE THREE LINES EVERY LOAN HAS ==

Your lender is going to set three thresholds. Learn them in order, because that's the order you'd hit them in.

The first one is the margin call line. It's usually somewhere around 65 to 70% LTV, though every lender is different. When you cross it, the lender contacts you and gives you a window to fix it, and that window can be as short as 24 to 72 hours.

The second one is the liquidation line, usually around 80 to 85%. If you cross that, or if you don't fix a margin call in time, the lender sells your Bitcoin to bring the loan back in range. You don't get a vote.

And the third is the release line, which is the good news, and a lot of borrowers don't know it exists. If the price rises enough that your LTV drops well below where you started, a lot of lenders will release some of that collateral back to you, or let you request it.

== WHAT YOU CAN DO AT A MARGIN CALL ==

When the call comes, you have three options, and you want to know which one is yours long before the phone rings.

Option one is to top up, which means sending more Bitcoin as additional collateral. That lowers your LTV without selling anything, and it's the option most people take. But it does mean you need to be holding unpledged Bitcoin that you can move quickly.

Option two is to pay down, which means sending cash to reduce the loan balance. Same effect on your LTV, just from the other side. That requires having cash available in exactly the week that your net worth is falling.

And option three is to do nothing and get liquidated. The lender sells enough of your Bitcoin to fix the ratio, at whatever the price happens to be that day, which by definition is going to be a bad price.

Notice that two of those three options require you to have something held in reserve. If you take a loan with every spare satoshi already pledged and no cash cushion, you have exactly one option at a margin call, and it's the bad one.

== PARTIAL VERSUS FULL LIQUIDATION ==

If it does come to liquidation, lenders handle it differently, and the app models both ways.

Partial liquidation means they sell only enough of your collateral to get you back under the threshold. You keep the rest, and the loan continues.

Full liquidation means they close the whole position. The loan gets settled, and whatever collateral is left over comes back to you.

Ask your lender which one they do before you sign anything, because it completely changes what a bad month costs you.

== THE TYPES OF PROVIDER ==

I'm not going to name specific companies, because that landscape changes and any list I give you today is going to be stale. What doesn't change is the structure, so you can sort any provider into one of these buckets.

The first one is custodial lenders. You send your Bitcoin to the company and they hold it. It's the simplest to use. The risk is exactly the one from the custody module: in a legal sense it's their Bitcoin now, and if they fail, you're a creditor standing in line. Several large ones failed in 2022 and their customers lost everything.

The second one is collaborative-custody lenders. Your collateral sits in a multisig arrangement, often two-of-three, where you hold a key, the lender holds a key, and a third party holds a key. The lender can't move your Bitcoin on their own. That structure is the reason a lot of Bitcoiners will use one of these and never touch a custodial one.

And then there's the question that really separates them, which is rehypothecation. Rehypothecation means the lender takes your collateral and lends it out to somebody else while they're holding it. It's the practice most directly responsible for the 2022 blowups. So ask directly: do you rehypothecate my collateral? And get the answer in writing. If the answer is anything other than a clear no, you're taking on a risk that has nothing at all to do with the Bitcoin price.

Here are the 7 questions I'd take to any provider. They're on screen, and they're in the lesson text below the video.

Do you rehypothecate collateral? Are you custodial or collaborative multisig, and who holds which key? What are your exact margin call and liquidation LTVs? How much notice do I get at a margin call, and how do you contact me? Do you do partial or full liquidation? Do you release collateral when LTV falls, and is that automatic or on request? And what's the interest rate, is it fixed or variable, and are there origination or early repayment fees?

== A WORKED EXAMPLE ==

Let's put real numbers on it.

Our couple holds 1.75 Bitcoin. At an illustrative $100,000 a coin, that's $175,000.

They want $35,000 for a kitchen renovation, and they don't want to sell, because selling means a taxable gain and giving up the upside.

So they pledge all 1.75 Bitcoin and borrow $35,000, which puts them at a 20% starting LTV.

Now let's walk the price down and watch that ratio move. The table is on the screen.

At $100,000 a coin they're at 20%, and that's comfortable. Drop to $70,000 and they're at 29%, which is a normal correction and totally fine. Drop to $50,000, so half the value is gone, and they're at 40%, still fine. Drop to $30,000 and they're at 67%, which is margin call territory. And at $25,000 they're at 80%, which is liquidation.

So a 75% drawdown, which is a completely normal Bitcoin bear market, takes them from 20% right to the edge. That's what starting at 20% buys you. It survives a normal bear, and it just barely survives it.

Now run that same loan at a 50% starting LTV, and a 40% price drop hits the margin call. A 40% drop is an ordinary Tuesday in Bitcoin, not a bear market.

== THE RULES TO WRITE DOWN BEFORE YOU BORROW ==

Five rules, and I'd write these down before you borrow a single dollar.

One: start low enough to survive a 70 to 80% drawdown. For most people that's going to mean 10 to 15%, not the 40 or 50% that a lender will happily hand you.

Two: keep unpledged Bitcoin or cash that you can reach fast, so a margin call actually has a good answer.

Three: know your lender's three lines, and write them down somewhere you'll actually find them.

Four: decide your action at each line right now, in writing, while nothing is falling.

And five: never borrow for something you can't stop paying for. A loan against a volatile asset that's funding a fixed obligation is how people get forced out at the bottom.

== NOW PUT IT IN THE APP ==

Orange Plan models all of this, and it models it as a real position inside your plan, not as a calculator sitting off to the side.

You add it under Strategy, then Debt, then Add debt, and you pick the Bitcoin-backed type. The form asks for the things that actually matter: your lender, the start date and term, the collateral in Bitcoin quantity rather than dollars, your margin call LTV, your liquidation LTV, whether auto top-up is on, and whether your lender does full or partial liquidation.

Enter your lender's real thresholds. The app ships with common defaults, and if you leave those in place, the plan is going to tell you a comforting story that isn't actually yours.

Then there's a section called Collateral rules, and this is where the behavior gets modeled across your whole projection. There's auto top-up as a global default, a margin call percent that triggers the top-up, a top-up target percent that it tops back down to, a liquidation percent, and a release trigger percent.

That last one is easy to miss and it matters. The app models collateral release. So if Bitcoin rises and your LTV falls below that release trigger, the projection frees that collateral back into your plan instead of leaving it pledged forever.

Here's how the modeling actually runs. The engine walks your loan forward year by year, right alongside the Bitcoin price path. Interest accrues, the price moves, your LTV gets recalculated, and if it crosses your top-up trigger the model tops up from your available Bitcoin. If it crosses liquidation, the model sells according to the liquidation strategy you picked and records that event. And pledged Bitcoin is protected from ordinary withdrawals, so your plan won't go spend collateral that you've already committed.

What that means practically is that when you run a 50% drawdown scenario with a loan in place, you're watching the loan's real behavior in that drawdown. Not an assumption about it.

== YOUR DECISION ==

Your decision out of this lesson is whether to borrow at all, and if you do, at what starting LTV and with which provider.

Here's how I'd think about it. Start with whether you need the money at all, because the cheapest loan is always the one you don't take. Then compare it honestly against just selling, because selling costs you tax and upside, while borrowing costs you interest and adds a liquidation risk that selling doesn't have. One of those is expensive and the other is risky, and those are not the same kind of problem.

Pick your starting LTV based on the drawdown you want to survive, not based on what you're allowed to borrow. Pick your provider on structure rather than rate, because a slightly better rate at a lender who rehypothecates your collateral is not a better deal.

If you couldn't fund a margin call, you can't afford the loan.

== HOMEWORK ==

Your homework for this lesson is to:

1. Decide whether a Bitcoin-backed loan belongs in your plan at all. No is a completely legitimate answer, and it's the common one.
2. If you're considering one, take those 7 provider questions to two or three lenders and put their answers side by side. The differences between lenders are the whole decision.
3. Model it in the app using your lender's real thresholds, then run the 50% drawdown scenario against it and watch what happens.
