# Advanced library — modeling, financing, and tax

Optional, condition-triggered lessons. Complete the related core decision first. These are educational spoken drafts; execution, jurisdiction, contract, and device-specific reviews remain outstanding where named.

## A1.1 — Test an assumption without making the model tell you what you want
Kind: advanced
Gate: APP_CAPTURE
Sources: FOUNDATION, BRAIN, APP, PRIMARY
Use when: a preset or holding-specific assumption materially changes a decision.

### Read aloud

Use this lesson when the standard assumption choices do not express the question you are trying to test. Start by writing that question. “What happens if Bitcoin's growth slows after the first decade?” is specific enough to model. “How do I get the earliest retirement date?” invites the wrong experiment.

Separate expected growth from uncertainty around the path. Two models can have similar long-term growth and very different drawdowns or sequences. A deterministic projection applies one path. A simulation samples paths under its distribution, correlation, and other rules. Those design choices matter alongside the return assumption you choose.

A power-law model, a declining growth schedule, and a flat annual rate express different assumptions. A fitted historical relationship is not a guarantee that future adoption or price follows it. Compare the decision under a lower or slower path rather than relying on one model name as proof of conservatism.

Use the same starting assets, spending, taxes, and timing when comparing return models. Then identify exactly what changed. A higher return, lower volatility, lower inflation, and a later retirement date changed together make it difficult to understand the source of improvement.

Holding overrides deserve particular care. A spot Bitcoin fund can reasonably inherit a supported Bitcoin return rule while remaining a security for tax and custody. A Bitcoin operating company, leveraged fund, futures product, or covered-call structure needs its own treatment. An unsupported override should not make its leverage, operating costs, or distribution risk disappear.

For the Reed household, test one slower-growth alternative and inspect the first funding shortfall or difficult year. If the retirement plan only works under a highly favorable path, the useful response may be more saving, later timing, less spending, or different financing. Improving the assumption to make the number recover does not improve the household's resources.

Record the model, the reason for using it, the most important limitation, and a less favorable comparison. Use the current methodology documentation to understand what the engine actually tests. Avoid claiming a simulation proves risks it does not model, such as a lender's failure probability.

Return to the core plan with one defensible baseline and a saved sensitivity test. Advanced settings should make the decision more transparent, not create a collection of hidden adjustments you cannot explain next year.

### Production notes

Use APP model/methodology as sole source for actual implementation. No unsupported claims of median calibration, correlation, fat tails, deterministic replay, or exact volatility schedule. Exact custom-period UI is capture-gated. Return to 1.4 and 6.7.

### Member checkpoint

- State the modeling question and one changed assumption.
- Compare the same plan under a less favorable path.
- Record the baseline, sensitivity, and limitations.

## A3.1 — Build a Bitcoin-loan operating sheet from the actual contract
Kind: advanced
Gate: TAX_LENDING_REVIEW
Sources: DEBT, BRAIN, PRIMARY, APP
Use when: a real or seriously considered Bitcoin-backed loan needs operating rules.

### Read aloud

The core course explained the decision to borrow. This lesson turns the actual contract into an operating sheet you can follow.

Record the loan amount, collateral quantity, interest rate, how interest is paid or added, fees, maturity, and repayment terms. Add the lender's margin, top-up, and liquidation rules exactly as written. The price source, timing, notice process, and discretion to act can matter during a rapid move.

Calculate loan-to-value from the full debt balance and collateral value. Interest that accrues into the loan raises the numerator even when Bitcoin's price stays unchanged.

For illustration, a twenty-five-thousand-dollar loan against one hundred thousand of collateral starts at twenty-five percent LTV. If twelve percent interest is added for one year in a simplified annual calculation, debt becomes twenty-eight thousand. If collateral value then falls to fifty thousand, LTV is fifty-six percent. The original starting LTV is no longer the relevant measure.

With an illustrative eighty-percent liquidation line, twenty-eight thousand of debt reaches that line when collateral is worth thirty-five thousand. That is a sixty-five-percent decline from the original collateral value, before any additional fees or interest. Use the actual contract and accrual method for a real loan.

Set a personal review level before the contractual action level. Name the response resources: cash repayment, additional collateral, a controlled sale, or another verified source. Give additional collateral its own exposure limit so protecting one loan does not unintentionally move the entire stack to a lender.

Stress an immediate crash, a long flat period, a rate increase, and a refinancing refusal. Consider an interruption in access to the lender or collateral as a separate operational risk. A favorable modeled price path does not certify the counterparty.

Record the maximum total Bitcoin exposure to the arrangement and who can respond when the usual operator is unavailable. Alerts help, but they do not guarantee enough time to act or prevent contractually permitted liquidation.

Keep this operating sheet separate from a generic course example. Verify tax treatment of borrowing, collateral disposal, repayment, and any cancellation with the appropriate professional. Return to the core debt and retirement-funding records with the real terms and the risks you have deliberately accepted.

### Production notes

Hypothetical 12% annual accrual is not a rate quote. Validate 25,000×1.12=28,000;28,000/50,000=56%;28,000/80%=35,000. Never label 25% or the product's 50% default safe. D63 rate-over-time and collateral fields require exact release proof.

### Member checkpoint

- Translate the actual contract into balances, thresholds, dates, and response rules.
- Include accrued interest and a limit on added collateral.
- Verify counterparty and tax questions outside the simulation.

## A3.2 — Compare financing terms that a simple payment hides
Kind: advanced
Gate: LENDING_REVIEW
Sources: DEBT, OWNER, PRIMARY
Use when: a large purchase, business acquisition, or home-equity offer has complex terms.

### Read aloud

A complex financing offer needs a cash-flow schedule and an exit calculation. The starting payment is only one line.

Begin with the same purchase price, amount financed, and date across alternatives. Record cash paid at closing, recurring payments, fees, principal remaining each year, and any balloon or settlement. Then identify what happens after a rate reset or the end of an interest-only period.

For a cash-out refinance, compare the cost on the entire replacement mortgage with keeping the old mortgage and funding only the new need another way. A lower advertised rate on one small alternative is not meaningful if the comparison ignores a large old balance being repriced.

For seller financing, read the security interest, guarantees, default remedies, payment schedule, and final balloon. For business debt, test the cash available after payroll, working capital, maintenance, taxes, and ordinary operating costs. A projected sale of the business is a different repayment source from recurring cash flow.

A home-equity investment can have a settlement tied to future home value or appreciation, with contractual adjustments and fees. Run low, middle, and high future home values at the actual settlement date. Check what happens on sale, refinancing, death, or failure to maintain required conditions. No monthly payment does not mean there is no future obligation.

Securities-backed credit also requires a purpose check. Non-purpose lines generally restrict using proceeds to buy securities. Margin arrangements have different rules and can expose holdings to rapid maintenance changes or sale. Verify the actual agreement before using a source for an investment purchase.

Retirement-plan loans depend on plan-specific availability and repayment rules. Evaluate employment changes, missed payments, potential tax consequences, and the effect on contribution capacity. The fact that some interest returns to the account does not eliminate those costs.

For the Reed renovation comparison, include a smaller project and a delay alongside financing. For an additional Bitcoin purchase, run that investment as a separate decision. A loan that is reasonable for an essential project may still be inappropriate for speculative expansion.

Use Orange Plan only for the terms its engine can faithfully represent. Keep a separate reviewed schedule for an unsupported balloon, contingent settlement, or other contract feature. Do not substitute a normal amortizing loan and call the full agreement modeled.

Return to the core plan with the total obligation, the collateral exposure, a credible repayment path, and a decision on whether the complexity is worth it. The simplest acceptable financing can be more useful than an arrangement whose economics the household cannot explain.

### Production notes

CFPB HELOC/home-equity-contract and FINRA SBLOC/margin sources. No financing product recommendation or approval promise. Do not add a fake app capability for HEI, seller-financed business, or contingent settlements. Return to 3.5–3.6.

### Member checkpoint

- Compare full schedules and exit obligations.
- Verify use restrictions, guarantees, and reset/default provisions.
- Label unmodeled terms and obtain contract review.

## A4.1 — Check price context before a large allocation change
Kind: advanced
Gate: OWNER_REVIEW
Sources: ALLOCATION, BRAIN, CLIENT_THEMES
Use when: a large proposed Bitcoin purchase or sale is being driven by recent price action.

### Read aloud

Use price context to slow down a large decision and identify what is driving it. Begin with the reason for the trade before looking at a chart.

A purchase may be part of a contribution plan, a move toward a chosen target, or a decision to invest cash that now has a long-term job. A sale may fund spending, reduce a risk, or support a tax plan. Those purposes remain useful even when the market is noisy.

Now ask what the recent move is doing to your judgment. A rally can create a feeling that the opportunity is disappearing. A decline can create fear or an urge to increase exposure quickly. Either can cause someone to change an allocation before checking liquidity, debt, and the intended holding period.

For the Reed household, a proposed large Bitcoin purchase must fit the Reserve, the card-payoff plan, the work-optional access needs, and the agreed target. A favorable price view does not create additional monthly cash or remove a lender's collateral rules.

Compare the proposed trade with a paced implementation where appropriate. Buying in stages can change timing risk and behavior, but it can also underperform a single purchase if the price rises. It is a trade-off, not a guaranteed improvement. The household should choose a process it can maintain rather than promise itself a perfect entry.

For a sale, identify the spending need, tax lots, and deadline. A committed near-term bill may require a reliable source even when you expect Bitcoin to rise. A flexible long-term holding can have a different decision window. Treat the two jobs separately.

A market indicator or valuation model can provide context, but its limitations matter. Historical relationships can change, signals can remain extreme, and a model cannot tell you the exact day a market will reverse. Avoid presenting a favored chart as certainty about a trade.

Write down what would make you change the decision. It might be a new cash need, a broken assumption, a different target, or a change in debt capacity. A rule stated before the trade is easier to evaluate than an explanation assembled after the price moves.

Return to Allocation with the same target and a deliberate implementation plan, or with a clearly justified proposed change. The outcome should be an action you understand, not another reason to check the market every hour.

### Production notes

No live price predictions, product recommendations, or implied timing alpha. Avoid saying all large drawdowns are better entries. Optional context check, not a new prerequisite for recurring contributions. Return to 4.2 and 4.7.

### Member checkpoint

- State the financial purpose before the market opinion.
- Compare implementation pace and trade-offs.
- Define the conditions that would change the decision.

## A5.1 — Build a multi-year conversion comparison
Kind: advanced
Gate: TAX_REVIEW
Sources: TAX, RETIREMENT, PRIMARY, APP
Use when: a meaningful Traditional balance and a plausible lower-income window make conversions relevant.

### Read aloud

A multi-year conversion plan should compare after-tax resources over time, not simply add up the conversions or future tax savings.

Start with the unchanged plan. Record expected income, spending, taxable-account resources, healthcare years, Social Security, required distributions, and the Traditional and Roth balances. Then choose a bounded conversion schedule to compare against it.

For each year, separate the amount converted from spending withdrawals and the cash used to pay conversion tax. Include the opportunity cost of that tax money. A dollar used for tax today is unavailable for another investment, the Reserve, or a near-term bill.

Use the marginal cost of the proposed conversion. It may span brackets and change other tax or benefit calculations. Marketplace assistance, Social Security taxation, Medicare income-related premiums, state tax, deductions, and credits can alter the total effect.

A sequence of smaller conversions can preserve flexibility, but it can also leave more future taxable growth than a larger early conversion. A large conversion during a market decline may move more units at a lower taxable value, while still creating a cash and access problem. Compare rather than assume.

For the Reed household, hold the retirement spending and market assumptions constant. Compare no added conversion, a modest annual schedule, and a larger early schedule. Read current liquidity, after-tax wealth, future ordinary income, and the surviving spouse or beneficiary implications where supported.

Stress the tax and return assumptions. A strategy based on a large future rate increase can disappoint if withdrawals later occur at lower rates. A strategy that leaves too little taxable money can strain the early-access years even when the Roth balance looks attractive.

The app may model the strategy, but the execution needs current-year verification. Confirm which account may be converted, whether a required distribution must be handled first, any nondeductible basis, the tax-payment method, and the custodian's procedure. Keep planned amounts separate from completed records.

The useful output is a range and a review rule rather than an unchangeable promise to convert the same amount for ten years. Revisit with actual income and current law before each year's transaction. Return to the core plan with the selected strategy and a clear professional handoff.

### Production notes

IRS Pub590-B/RMD and current tax interaction sources. No assumption all conversions are fully taxable or reversible. Current law and account-specific treatment must be verified. Product comparison primary outcome is total after-tax wealth. Return to 5.4 and 6.4.

### Member checkpoint

- Compare bounded schedules against unchanged spending and assumptions.
- Include tax funding and opportunity cost.
- Verify each actual year's amount before execution.

## A5.2 — Prepare a harvesting transaction that matches the tax record
Kind: advanced
Gate: TAX_REVIEW
Sources: TAX, PRIMARY, APP
Use when: an actual taxable holding presents a gain- or loss-harvesting candidate.

### Read aloud

Begin with a specific holding and supported lots. A harvesting idea becomes actionable only when the units, tax treatment, and execution process can be documented.

For a loss, compare current proceeds with adjusted basis and include transaction costs. Identify which existing gains or future tax items the loss may offset. The tax value depends on the actual return and carryforward situation, not simply the size of the loss shown on screen.

For a gain, estimate the amount realized and the effect on the full year's taxable income. A favorable federal capital-gain rate can still come with state tax or other income-related costs. A conversion or unexpected business income can use the same planned tax room.

Verify the identification rules that apply to the asset, account or wallet, custodian, and year. Broker-held digital assets can have different reporting and transitional provisions from assets in an unhosted wallet. Do not assume a software lot-selection preference alone satisfies the requirements.

Replacement exposure needs a separate check. Securities are subject to wash-sale rules under their applicable conditions. Personally held Bitcoin should not be treated as though every stock rule applies identically, but neither should an older crypto-tax article be treated as permanent permission for a particular transaction. Obtain current tax review of the actual sale and any repurchase.

Keep the order clear: model the opportunity, verify the proposed transaction, execute with the provider, then record what actually happened. The recorded proceeds, fees, quantity, identified units, and date should match the confirmation. Reconcile remaining lots and realized activity afterward.

An outside transfer to prepare for a trade may also need to preserve history. Avoid importing the same purchase again at the destination. A network fee and an acquisition cost need their correct supported treatment rather than being hidden by changing quantity until totals match.

For the Reed example, use the three-lot illustration to compare the gain produced by the same sale amount. Then stop before execution and build the evidence checklist. The lowest theoretical tax result is not useful if the records and custodian process do not support it.

Save the transaction documentation with the tax file and reconcile it to the filed return. Carryforwards and basis adjustments need continuity into the next year. Return to the core tax plan with a completed record or a clearly pending action, not a proposed trade labeled as finished.

### Production notes

Verify current digital-asset identification relief, including IRS Notice2026-20 where applicable. No universal spot-BTC immediate-repurchase safe-harbor claim. FORM8949 data export is not the filed form. Return to 5.1–5.2 and 5.5.

### Member checkpoint

- Verify actual lots, identification, costs, and replacement exposure.
- Separate model, execution, and record stages.
- Reconcile the result with tax reporting and next-year continuity.

## A5.3 — Evaluate a state move as a household decision
Kind: advanced
Gate: TAX_ESTATE_REVIEW
Sources: TAX, ESTATE, PRIMARY
Use when: the household is genuinely considering moving or has income/assets tied to multiple states.

### Read aloud

A state move can change taxes, but the decision also changes housing, healthcare, work, family access, and the cost of daily life. Compare those together.

Start with the reason for moving and the realistic locations. Then build the cost difference: housing, property and other taxes, insurance, transport, healthcare, moving expenses, and any income changes. A lower income-tax rate can be offset by higher costs elsewhere.

Tax residency depends on the facts and law, not the address selected in the app. Domicile, time spent, homes, work, family ties, and other evidence can matter. The former state may retain a claim on some income. State-source business, rental, deferred compensation, or other items need specific review.

A large Bitcoin sale near a move makes timing and residency evidence especially important. A brokerage address change alone does not settle where the gain is taxed. Before acting, obtain advice from a professional familiar with both jurisdictions and the actual facts.

For the Reed household, a state scenario should include the full economic changes and the effective date. Keep the current state in the saved baseline until the household chooses and completes the relevant move. Do not use a favorable state assumption to make retirement appear affordable while the family still intends to live elsewhere.

Estate documents, healthcare directives, insurance policies, business registrations, and provider arrangements may also need review after relocation. A legal instrument that worked in one state may need updating for the new circumstances.

Use the model to identify whether the financial difference is meaningful enough to pursue. Then gather the actual rules and implementation requirements. The scenario is a planning comparison; it is not proof of legal residency or a filed tax position.

Finish with the full household reason for the move, a realistic cost comparison, and the questions for the relevant professionals. Return to the core life-event plan only when the date and intention are sufficiently real to include.

### Production notes

No state-specific threshold without current jurisdictional research. Generic worksheet does not establish domicile. No tax-avoidance shortcut or backdated-residency advice. Return to 2.4 and 5.3.

### Member checkpoint

- Compare total household costs and life consequences.
- Verify residency and source-income treatment in both jurisdictions.
- Keep the move hypothetical until the intention and timing support a baseline event.
