# A6.2 — Test a multi-year sell-versus-borrow strategy

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: TAX_LENDING_REVIEW
Sources: RETIREMENT, DEBT, APP, PRIMARY
Use when: recurring retirement borrowing is a serious alternative to asset sales.

### Read aloud

A borrowing strategy that preserves Bitcoin this year still has to fund later spending and repay the debt. Follow the policy through difficult years and the exit, not just the first year's retained balance.

Hold the spending, retirement timing, and market assumptions constant. Compare the current funding plan with the proposed policy. Read the annual cash need, sales, loans, interest, debt balance, collateral, and eventual repayment. Include the years after a weak market, not only the years when price growth easily covers the debt.

The source of repayment matters. Selling later, using another account, paying from income, refinancing, or leaving an estate obligation are different plans. Each has costs and uncertainties. A strategy that repeatedly borrows to pay interest can grow the obligation even when household spending is unchanged.

Use an assumptions receipt. Which rate is fixed, and how is the rate modeled over time? What collateral is eligible? How is interest paid? What happens at a contractual threshold? Which parts of the proposed policy are actually supported by the engine?

A hybrid described as selling within a tax limit and then borrowing still needs the exact limit, tax assumptions, and residual borrowing path explained. A policy label cannot replace the year detail.

Stress lower Bitcoin growth, an early drawdown, higher rates, longer life, and reduced refinancing availability. Also record risks the simulation does not quantify, such as provider failure or changes in contractual access. A higher chance-of-success output is not proof those risks are acceptable.

Estate assumptions deserve particular caution. Inherited basis, the taxable estate, loan settlement, liquidity, beneficiary treatment, and jurisdiction can change the outcome. Do not build the entire strategy on a slogan about never selling or avoiding all tax at death. Use current legal and tax review of the intended structure.

For the Reed household, a borrowing scenario must preserve the current reserve and early-access needs and must not silently create an actual loan record. If the family eventually adopts a policy, it moves through the supported Preview and save flow. An executed loan is recorded separately with its real terms.

For the Reeds, compare the same household spending under sales, another available funding source, and the proposed borrowing policy. Inspect a year after weak returns. Has interest added to the loan, is more Bitcoin pledged, and what resource is still available to respond? A favorable final balance can hide a difficult period the household would have had to survive first.

Return with one funding policy, its repayment and estate assumptions, the risks not measured by the simulation, and a review rule. Declining recurring borrowing is a complete decision. No strategy is established by the phrase 'never sell' when its later obligations remain unexplained.

### Production notes

D63 engine-preservation contract governs support and limitations. No fabricated liquidation frequency, counterparty probability, or estate-tax guarantee. Show current/preview assumptions and actual year outputs only. Return to 6.6–6.8.

### Member checkpoint

- Inspect the debt and collateral path across difficult years.
- State repayment and estate assumptions explicitly.
- Record unsupported risks and the conditions for changing policy.

### Source-led visual and teaching notes — not spoken

Year-by-year cash delivered, sale proceeds, borrowing, interest, total debt, collateral, accessible reserves and repayment. Keep existing debt separate from a hypothetical policy and show unmodeled provider risk alongside the result.

Editorial reason: Follow recurring borrowing through liquidity stress and eventual repayment rather than first-year retention.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Keep the baseline and spending unchanged while comparing supported policies. Read the assumptions receipt, a weak-market year, rate changes and the repayment path. Identify unsupported refinancing/counterparty/estate assumptions rather than invent a probability. Verify current-versus-preview and actual-loan separation. Return to 6.6–6.8.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.
