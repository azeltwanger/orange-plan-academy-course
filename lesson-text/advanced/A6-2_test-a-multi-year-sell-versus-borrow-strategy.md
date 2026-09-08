# A6.2 — Test a multi-year sell-versus-borrow strategy

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: TAX_LENDING_REVIEW
Sources: RETIREMENT, DEBT, APP, PRIMARY
Use when: recurring retirement borrowing is a serious alternative to asset sales.

### Read aloud

A retirement borrowing strategy needs to be evaluated across many years. Preserving more Bitcoin in the first year is only one part of the outcome.

Hold the spending, retirement timing, and market assumptions constant. Compare the current funding plan with the proposed policy. Read the annual cash need, sales, loans, interest, debt balance, collateral, and eventual repayment. Include the years after a weak market, not only the years when price growth easily covers the debt.

The source of repayment matters. Selling later, using another account, paying from income, refinancing, or leaving an estate obligation are different plans. Each has costs and uncertainties. A strategy that repeatedly borrows to pay interest can grow the obligation even when household spending is unchanged.

Use an assumptions receipt. Which rate is fixed, and how is the rate modeled over time? What collateral is eligible? How is interest paid? What happens at a contractual threshold? Which parts of the proposed policy are actually supported by the engine?

A hybrid described as selling within a tax limit and then borrowing still needs the exact limit, tax assumptions, and residual borrowing path explained. A policy label cannot replace the year detail.

Stress lower Bitcoin growth, an early drawdown, higher rates, longer life, and reduced refinancing availability. Also record risks the simulation does not quantify, such as provider failure or changes in contractual access. A higher chance-of-success output is not proof those risks are acceptable.

Estate assumptions deserve particular caution. Inherited basis, the taxable estate, loan settlement, liquidity, beneficiary treatment, and jurisdiction can change the outcome. Do not build the entire strategy on a slogan about never selling or avoiding all tax at death. Use current legal and tax review of the intended structure.

For the Reed household, a borrowing scenario must preserve the current reserve and early-access needs and must not silently create an actual loan record. If the family eventually adopts a policy, it moves through the supported Preview and save flow. An executed loan is recorded separately with its real terms.

Return to Retirement Income with one chosen funding policy, an explicit explanation of the additional risks, and a review rule. A decision to use limited sales and decline recurring borrowing can be just as complete as choosing a carefully bounded loan strategy.

### Production notes

D63 engine-preservation contract governs support and limitations. No fabricated liquidation frequency, counterparty probability, or estate-tax guarantee. Show current/preview assumptions and actual year outputs only. Return to 6.6–6.8.

### Member checkpoint

- Inspect the debt and collateral path across difficult years.
- State repayment and estate assumptions explicitly.
- Record unsupported risks and the conditions for changing policy.
