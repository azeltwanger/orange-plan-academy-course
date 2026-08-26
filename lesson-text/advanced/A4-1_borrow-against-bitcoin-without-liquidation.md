# A4.1 · Borrow against Bitcoin without turning a drawdown into liquidation

**Publication gate:** Research complete. Verify the exact lender terms, margin-call rules, liquidation rules, custody model, and current app fields before recording any provider-specific example.

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
