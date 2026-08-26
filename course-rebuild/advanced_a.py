ADVANCED = {
    "A1.1": {
        "title": "How Orange Plan models Bitcoin inside the confidence check",
        "gate": "Research complete. Record after the current Help & Methodology copy and production settings are checked against the same app commit used on camera.",
        "body": r"""
The confidence number is only useful if the market paths are difficult enough to test the plan and honest enough not to flatter the Bitcoin assumption.

Orange Plan does not treat Bitcoin like a generic stock with a slightly larger standard deviation. Bitcoin gets its own return process because the shape of its history is different.

The first difference is the tails. Extreme positive and negative years happen more often than a normal bell curve would suggest. A model built around a polite normal distribution can understate the very outcomes a Bitcoin holder cares about most.

The second difference is asymmetry. Bitcoin has had very large upside years as well as deep drawdowns. The distribution needs to preserve the possibility of both rather than forcing the positive and negative sides into a perfectly symmetrical shape.

The third difference is maturity. A larger asset should not be assumed to keep the same volatility forever. The model allows volatility to decline over time as Bitcoin grows, while still leaving room for difficult sequences.

The fourth difference is correlation. Bitcoin, stocks, inflation, and interest-rate conditions are not independent in every bad year. The simulation links the major asset classes so a stress path can include several problems at once instead of conveniently offsetting each other every time.

The straight-line growth assumption still matters. If you enter an unrealistic return, the simulation cannot rescue the plan from a bad premise. What the calibration does is prevent the random paths from secretly adding another layer of optimism on top of the selected assumption. The median modeled result is checked against the deterministic projection under the same settings.

The comparison also uses matched paths. When you compare retiring at sixty with retiring at sixty-five, or selling with borrowing, both strategies are tested against the same market sequences. One strategy does not get easier weather by accident.

And the result is repeatable. With the same inputs and same saved settings, the confidence result should not jump around merely because you pressed the button twice. If it changes, a market value, plan input, or strategy changed.

The important boundary is that this is still a model. Historical data cannot tell us the exact future distribution, and Bitcoin can behave outside the ranges anybody expected. Use the confidence result to compare decisions and find fragility, not as a promise that a specific percentage will occur.

The current distributions, volatility schedule, correlations, and caps belong in Help & Methodology rather than being frozen into an evergreen recording. Before filming, open that page and verify that the explanation and the production engine still match.
""",
    },
    "A3.1": {
        "title": "Use price context to name the emotion before a large Bitcoin move",
        "gate": "Ready after the current price-context data shown in the app is verified. This lesson is a decision check, not a market-timing system.",
        "body": r"""
Price context does not tell you whether to buy or sell. It tells you what emotion is most likely influencing the decision.

Before a large Bitcoin purchase, allocation change, or loan, compare the current price with several timeframes: a few months ago, one year ago, and several years ago.

A price that has risen quickly creates urgency. The story feels obvious, the risk feels lower because the recent result was good, and the household may increase the allocation or add leverage near the point where the downside in dollars is largest.

A price that has fallen sharply creates the opposite reaction. The thesis feels less certain, losses feel permanent, and a move that was considered reasonable at a higher price suddenly feels impossible. A lower price can also create a genuine opportunity, but only if the cash flow, Reserve, debt, custody, and time horizon can support it.

The context check is a pause, not a signal.

Ask:

- Has the price move changed the financial plan or only the account value?
- Am I increasing risk because recent returns made it feel safe?
- Am I abandoning a supported plan because the drawdown made it feel unsafe?
- Would I make the same decision if the chart were hidden and I only saw the cash-flow, tax, and risk trade-offs?
- What happens if the price moves another fifty percent against me after I act?

Then return to the plan. A large purchase needs a real surplus and a Reserve. A larger allocation needs a drawdown result the household can hold. A loan needs a conservative LTV, a repayment source, and room for a deep drop. A sale needs a reason tied to spending, taxes, or risk rather than relief from the current emotion.

The price context never replaces those decisions. It simply makes the emotional environment visible before it drives them.
""",
    },
    "A4.1": {
        "title": "Borrow against Bitcoin without turning a drawdown into liquidation",
        "gate": "Research complete. Verify the exact lender terms, margin-call rules, liquidation rules, custody model, and current app fields before recording any provider-specific example.",
        "body": r"""
A Bitcoin-backed loan can create liquidity without selling the collateral at the start. It can also turn an ordinary Bitcoin drawdown into a forced sale if the loan is too large or the operating plan is vague.

The first number is loan-to-value: the loan balance divided by the current value of the collateral.

If the loan is fifty thousand dollars and the posted Bitcoin is worth two hundred thousand dollars, the starting LTV is twenty-five percent.

As Bitcoin falls, the collateral value falls and the LTV rises even when the loan balance does not change.

The lender may have a margin-call or top-up level, a liquidation level, or an automatic collateral process. Those terms are contractual and can differ materially. Read the actual agreement rather than assuming one lender works like another.

The useful question is not only today's LTV. It is how far Bitcoin can fall before each trigger.

For a simple example with an eighty-percent liquidation line, a twenty-five-percent starting LTV has much more room than a fifty-percent starting LTV. The relationship is not linear. Starting twice as high can remove most of the crash cushion.

Model the price at the margin call and liquidation line in dollars. A percentage can feel abstract. A statement that the loan becomes critical at a specific Bitcoin price is much easier to monitor.

Then build the operating rules before taking the loan:

- What is the purpose of the proceeds?
- What is the maximum starting LTV?
- At what LTV or Bitcoin price will collateral be added?
- Where will that collateral come from?
- At what point will part of the loan be repaid instead?
- What is the repayment source if Bitcoin stays weak for several years?
- How often is the position checked, and who checks it if you are unavailable?
- What conditions mean no new borrowing?

Separate the loan collateral from the emergency Reserve. Bitcoin held for an automatic top-up is not the same thing as cash available to pay living expenses. And collateral held by a lender is not the same thing as Bitcoin in your own custody.

Counterparty risk matters even when the LTV is conservative. Understand rehypothecation, bankruptcy treatment, withdrawal or collateral-release rules, jurisdiction, insurance claims, and what happens if the lender changes terms or stops operating.

The tax pitch needs nuance too. Loan proceeds generally are not income when a bona fide loan is created. A later liquidation is a sale of collateral and may create a taxable gain or loss. Forgiveness or another restructuring can create different consequences. The phrase "borrow and never pay tax" is not a complete plan.

New borrowing to buy more Bitcoin needs a higher standard than keeping an existing low-rate mortgage. You are adding leverage to the same asset that secures the loan. A price decline hurts the investment and the collateral ratio at the same time.

A strong version starts with a low LTV, a durable repayment source, collateral outside the loan, clear triggers, and proceeds serving a specific job. A weak version begins because the household is short of cash and assumes the next bull market will solve repayment.

Use the app to model the lender-versus-custody chart, the fall-to-trigger prices, interest cost, and estate impact. The app can show the trade-off. It cannot make the contract safer than the actual lender terms.
""",
    },
    "A4.2": {
        "title": "The four ways debt can strengthen a plan, and how each one fails",
        "gate": "Ready as an educational mechanism lesson. Do not recommend a specific loan, lender, rate, or amount.",
        "body": r"""
Debt is useful when it gives the plan more flexibility or growth than the risk it adds. The mechanism matters more than whether the debt sounds good or bad.

The first use is keeping cheap fixed debt while capital does another job.

Paying off a three-percent mortgage creates a guaranteed three-percent return and removes the payment. Keeping it preserves liquidity and may leave the capital invested in an asset expected to earn more. The failure is assuming the expected spread is guaranteed or ignoring a payment that is squeezing the cash flow.

The second use is borrowing instead of selling an appreciated asset.

A loan can avoid an immediate sale and keep the Bitcoin exposure. This can be useful when the tax cost of selling is high and the loan is conservative. It fails when interest, liquidation risk, and counterparty risk are treated as free or when there is no repayment source.

The third use is establishing optional credit before it is needed.

A home-equity line or another facility may be easier to obtain while income is strong. An unused line can provide flexibility later. It fails when the variable rate resets, the line is frozen, or the household treats available credit as permission to spend.

The fourth use is financing an asset or business that produces cash flow or reduces another cost.

A loan can make sense when the financed asset has a clear job and the payment is comfortably supported. It fails when the expected return is speculative, the debt is recourse to the household, or one bad year creates a forced sale elsewhere.

Every use needs the defensive foundation first: a Reserve, manageable required payments, honest stress testing, and a job for the debt.

Compare the full alternatives. Paying cash may create taxes or remove liquidity. Borrowing may preserve assets but add interest and fragility. Doing nothing may keep flexibility but delay the goal.

The planning question is not whether debt can build wealth. It can. The question is whether this specific debt improves the whole plan after the payment, taxes, downside, and behavior are included.
""",
    },
}
