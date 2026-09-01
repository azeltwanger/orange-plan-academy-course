# Advanced Module 4 — Debt Strategy

## A4.1 Borrow against Bitcoin without turning a drawdown into liquidation

*`TEACH` · ~3.6 min · PRE-DICTATION FILMING DRAFT*

> **Publication gate:** Research complete. Verify the exact lender terms, margin-call rules, liquidation rules, custody model, and current app fields before recording any provider-specific example.

A Bitcoin-backed loan can create liquidity without selling the collateral at the start. It can also turn an ordinary Bitcoin drawdown into a forced sale if the loan is too large or the operating plan is vague.

The first number is loan-to-value: the loan balance divided by the current value of the collateral.

If the loan is fifty thousand dollars and the posted Bitcoin is worth two hundred thousand dollars, the starting LTV is twenty-five percent.

As Bitcoin falls, the collateral value falls and the LTV rises even when the loan balance does not change.

The lender may have a margin-call or top-up level, a liquidation level, or an automatic collateral process. Those terms are contractual and can differ materially. Read the actual agreement rather than assuming one lender works like another.

Translate today's LTV into the Bitcoin price and percentage decline that reaches each trigger.

For a simple example with an eighty-percent liquidation line, a twenty-five-percent starting LTV has much more room than a fifty-percent starting LTV. The crash cushion shrinks nonlinearly as the starting LTV rises. Starting twice as high can remove most of the room before liquidation.

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

Separate the loan collateral from the emergency Reserve. Separate the resources by job: automatic top-up Bitcoin protects the loan, cash pays living expenses, and collateral at the lender carries different access and counterparty risk from Bitcoin in your own custody.

Counterparty risk matters even when the LTV is conservative. Understand rehypothecation, bankruptcy treatment, withdrawal or collateral-release rules, jurisdiction, insurance claims, and what happens if the lender changes terms or stops operating.

The tax pitch needs nuance too. A bona fide loan generally provides proceeds without income at origination. A later liquidation sells collateral and may create a taxable gain or loss. Forgiveness or another restructuring can create different consequences. The phrase "borrow and never pay tax" is not a complete plan.

New borrowing to buy more Bitcoin needs a higher standard than keeping an existing low-rate mortgage. You are adding leverage to the same asset that secures the loan. A price decline hurts the investment and the collateral ratio at the same time.

A strong version starts with a low LTV, a durable repayment source, collateral outside the loan, clear triggers, and proceeds serving a specific job. A weak version begins because the household is short of cash and assumes the next bull market will solve repayment.

Use the app to model the lender-versus-custody chart, the fall-to-trigger prices, interest cost, and estate impact. The app can show the trade-off. It cannot make the contract safer than the actual lender terms.

---
## A4.2 The four ways debt can strengthen a plan, and how each one fails

*`TEACH` · ~2.2 min · PRE-DICTATION FILMING DRAFT*

> **Publication gate:** Ready as an educational mechanism lesson. Do not recommend a specific loan, lender, rate, or amount.

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

Debt can build wealth when the specific loan improves the whole plan after the payment, taxes, downside, and household behavior are included. That is the test.

---
