# A3.1 — Build a Bitcoin-loan operating sheet from the actual contract

Status: TEACHING_REPAIR_NEEDED — the prior course-wide pass was rejected for voice and teaching clarity. This component still needs individual repair; it is not approved.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: TAX_LENDING_REVIEW
Sources: DEBT, BRAIN, PRIMARY, APP
Use when: a real or seriously considered Bitcoin-backed loan needs operating rules.

### Read aloud

Take the actual loan agreement and turn it into an operating sheet. Someone should be able to use it to see what is owed, what could trigger action, and how the household would respond without assuming another lender will rescue the plan.

Record the loan amount, collateral quantity, interest rate, how interest is paid or added, fees, maturity, and repayment terms. Add the lender's margin, top-up, and liquidation rules exactly as written. The price source, timing, notice process, and discretion to act can matter during a rapid move.

Calculate loan-to-value from the full debt balance and collateral value. Interest that accrues into the loan raises the numerator even when Bitcoin's price stays unchanged.

For illustration, a twenty-five-thousand-dollar loan against one hundred thousand of collateral starts at twenty-five percent LTV. If twelve percent interest is added for one year in a simplified annual calculation, debt becomes twenty-eight thousand. If collateral value then falls to fifty thousand, LTV is fifty-six percent. The original starting LTV is no longer the relevant measure.

With an illustrative eighty-percent liquidation line, twenty-eight thousand of debt reaches that line when collateral is worth thirty-five thousand. That is a sixty-five-percent decline from the original collateral value, before any additional fees or interest. Use the actual contract and accrual method for a real loan.

Set a personal review level before the contractual action level. Name the response resources: cash repayment, additional collateral, a controlled sale, or another verified source. Give additional collateral its own exposure limit so protecting one loan does not unintentionally move the entire stack to a lender.

Stress an immediate crash, a long flat period, a rate increase, and a refinancing refusal. Consider an interruption in access to the lender or collateral as a separate operational risk. A favorable modeled price path does not certify the counterparty.

Record the maximum total Bitcoin exposure to the arrangement and who can respond when the usual operator is unavailable. Alerts help, but they do not guarantee enough time to act or prevent contractually permitted liquidation.

Look again at the illustration: interest raises the original twenty-five-thousand-dollar loan to twenty-eight thousand. Against fifty thousand of collateral, that is fifty-six percent LTV. The original twenty-five-percent starting ratio no longer describes the situation. Now ask which response resources remain genuinely available. Cash already assigned to essential bills is not automatically spare repayment money, and adding collateral has its own limit on lender exposure.

Keep the real terms, personal review point, contractual action point, response resources and backup operator together. Recheck the sheet as interest, collateral or terms change. An alert and a low starting ratio are useful information; neither is a guarantee that the loan cannot be liquidated or access interrupted.

### Production notes

Hypothetical 12% annual accrual is not a rate quote. Validate 25,000×1.12=28,000;28,000/50,000=56%;28,000/80%=35,000. Never label 25% or the product's 50% default safe. D63 rate-over-time and collateral fields require exact release proof.

### Member checkpoint

- Translate the actual contract into balances, thresholds, dates, and response rules.
- Include accrued interest and a limit on added collateral.
- Verify counterparty and tax questions outside the simulation.

### Source-led visual and teaching notes — not spoken

Retain the labeled $25,000 → $28,000 annual-interest illustration; $50,000 collateral → 56% LTV; hypothetical 80% line at $35,000 collateral. No current loan quote or safety recommendation.

Editorial reason: Follow the existing loan arithmetic through to a funded response and provider-exposure decision.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Use a reviewed fictional agreement and the operating sheet, not a real application. Read full debt, accrual, collateral, thresholds, maturity, notice and discretion; then rehearse income loss, a rapid decline and refinancing refusal. Match any modeled loan fields to the contract and label unsupported terms. No provider contact or actual collateral movement. Return to 3.6 and 6.6.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.
