# Advanced library

Generated from canonical `scripts/`. New prose is a pre-dictation draft, not a claim Austin already said it. Production notes and member checkpoints are not spoken.

# A1.1 — Test an assumption without making the model tell you what you want

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: APP_CAPTURE
Sources: FOUNDATION, BRAIN, APP, PRIMARY
Use when: a preset or holding-specific assumption materially changes a decision.

### Read aloud

Use an advanced assumption when it answers a specific question the normal starting choices do not express. Write that question first. Then change one thing so you can explain what caused the different result.

Separate expected growth from uncertainty around the path. Two models can have similar long-term growth and very different drawdowns or sequences. A deterministic projection applies one path. A simulation samples paths under its distribution, correlation, and other rules. Those design choices matter alongside the return assumption you choose.

A power-law model, a declining growth schedule, and a flat annual rate express different assumptions. A fitted historical relationship is not a guarantee that future adoption or price follows it. Compare the decision under a lower or slower path rather than relying on one model name as proof of conservatism.

Use the same starting assets, spending, taxes, and timing when comparing return models. Then identify exactly what changed. A higher return, lower volatility, lower inflation, and a later retirement date changed together make it difficult to understand the source of improvement.

Holding overrides deserve particular care. A spot Bitcoin fund can reasonably inherit a supported Bitcoin return rule while remaining a security for tax and custody. A Bitcoin operating company, leveraged fund, futures product, or covered-call structure needs its own treatment. An unsupported override should not make its leverage, operating costs, or distribution risk disappear.

For the Reed household, test one slower-growth alternative and inspect the first funding shortfall or difficult year. If the retirement plan only works under a highly favorable path, the useful response may be more saving, later timing, less spending, or different financing. Improving the assumption to make the number recover does not improve the household's resources.

Record the model, the reason for using it, the most important limitation, and a less favorable comparison. Use the current methodology documentation to understand what the engine actually tests. Avoid claiming a simulation proves risks it does not model, such as a lender's failure probability.

For the Reeds, an early year and a later year can reveal whether the chosen declining path says what they thought it said. Keep their spending, contributions and intended retirement timing fixed while comparing slower growth. Then inspect the first difficult funding year. The useful result is knowing which household decision depends on that assumption—not finding enough hidden adjustments to produce a preferred date.

Return to the main plan with a starting model you can explain, one useful comparison, and the limitation that matters most. If the comparison answers the question, stop. More settings do not automatically make the plan more reliable.

### Production notes

Use APP model/methodology as sole source for actual implementation. No unsupported claims of median calibration, correlation, fat tails, deterministic replay, or exact volatility schedule. Exact custom-period UI is capture-gated. Return to 1.4 and 6.7.

### Member checkpoint

- State the modeling question and one changed assumption.
- Compare the same plan under a less favorable path.
- Record the baseline, sensitivity, and limitations.

### Source-led visual and teaching notes — not spoken

Show the written question, one changed assumption, unchanged household choices, and the affected funding year. Actual rates, methodology and outputs require the approved build.

Editorial reason: Make advanced modeling a bounded sensitivity question with a clear return to the core plan.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Prepare the current saved assumptions and one reviewed lower-growth alternative. Show the early/later rates, compare the same household inputs, and inspect the funding year that explains the difference. Verify exact custom-period/override controls, unchanged baseline and result identity before recording. Do not manufacture volatility, correlation, replay or provider-failure claims. Return to 1.4 and 6.7.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.

---

# A3.1 — Build a Bitcoin-loan operating sheet from the actual contract

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
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

---

# A3.2 — Compare financing terms that a simple payment hides

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: LENDING_REVIEW
Sources: DEBT, OWNER, PRIMARY
Use when: a large purchase, business acquisition, or home-equity offer has complex terms.

### Read aloud

A small starting payment can hide a large later obligation. Compare the whole schedule and exit before choosing a complex financing offer, including what changes when the interest-only period or promotional terms end.

Begin with the same purchase price, amount financed, and date across alternatives. Record cash paid at closing, recurring payments, fees, principal remaining each year, and any balloon or settlement. Then identify what happens after a rate reset or the end of an interest-only period.

For a cash-out refinance, compare the cost on the entire replacement mortgage with keeping the old mortgage and funding only the new need another way. A lower advertised rate on one small alternative is not meaningful if the comparison ignores a large old balance being repriced.

For seller financing, read the security interest, guarantees, default remedies, payment schedule, and final balloon. For business debt, test the cash available after payroll, working capital, maintenance, taxes, and ordinary operating costs. A projected sale of the business is a different repayment source from recurring cash flow.

A home-equity investment can have a settlement tied to future home value or appreciation, with contractual adjustments and fees. Run low, middle, and high future home values at the actual settlement date. Check what happens on sale, refinancing, death, or failure to maintain required conditions. No monthly payment does not mean there is no future obligation.

Securities-backed credit also requires a purpose check. Non-purpose lines generally restrict using proceeds to buy securities. Margin arrangements have different rules and can expose holdings to rapid maintenance changes or sale. Verify the actual agreement before using a source for an investment purchase.

Retirement-plan loans depend on plan-specific availability and repayment rules. Evaluate employment changes, missed payments, potential tax consequences, and the effect on contribution capacity. The fact that some interest returns to the account does not eliminate those costs.

For the Reed renovation comparison, include a smaller project and a delay alongside financing. For an additional Bitcoin purchase, run that investment as a separate decision. A loan that is reasonable for an essential project may still be inappropriate for speculative expansion.

Use Orange Plan only for the terms its engine can faithfully represent. Keep a separate reviewed schedule for an unsupported balloon, contingent settlement, or other contract feature. Do not substitute a normal amortizing loan and call the full agreement modeled.

Use the earlier interest-only illustration as a check. The lower monthly payment does not remove the twenty-thousand-dollar principal. If the intended repayment is refinancing, ask what the household does when a lender declines. For the Reeds' renovation, keeping the project smaller or waiting can be a better fit for the current cash flow than accepting a payment shape they cannot explain through its final settlement.

Return with the cash used now, payments, remaining principal or contingent settlement, collateral, and a credible exit. Keep any term the model cannot represent in a separately reviewed comparison. An unusual structure earns its place only when its benefit is worth the cost and added responsibility.

### Production notes

CFPB HELOC/home-equity-contract and FINRA SBLOC/margin sources. No financing product recommendation or approval promise. Do not add a fake app capability for HEI, seller-financed business, or contingent settlements. Return to 3.5–3.6.

### Member checkpoint

- Compare full schedules and exit obligations.
- Verify use restrictions, guarantees, and reset/default provisions.
- Label unmodeled terms and obtain contract review.

### Source-led visual and teaching notes — not spoken

Full financing schedule, not just monthly payment: upfront cash, annual payments, principal remaining, reset and exit. Keep the $20,000 illustration distinct from the $30,000 renovation comparison.

Editorial reason: Use the unpaid-principal question to make complex financing a complete decision.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Compare the same purpose and date across the actual candidate structures, plus smaller/delay. Inspect a reset and final settlement, and test a refused refinance. Show unsupported home-equity-contract or balloon terms in a labeled external schedule rather than fake app fields. Contract and tax review precede execution. Return to 3.5–3.6.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.

---

# A4.1 — Check price context before a large allocation change

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: OWNER_REVIEW
Sources: ALLOCATION, BRAIN, CLIENT_THEMES
Use when: a large proposed Bitcoin purchase or sale is being driven by recent price action.

### Read aloud

Before a large purchase or sale, separate the financial reason from the feeling created by the latest price move. The question is what the transaction needs to accomplish and whether its size and timing fit the rest of your plan.

A purchase may be part of a contribution plan, a move toward a chosen target, or a decision to invest cash that now has a long-term job. A sale may fund spending, reduce a risk, or support a tax plan. Those purposes remain useful even when the market is noisy.

Now ask what the recent move is doing to your judgment. A rally can create a feeling that the opportunity is disappearing. A decline can create fear or an urge to increase exposure quickly. Either can cause someone to change an allocation before checking liquidity, debt, and the intended holding period.

For the Reed household, a proposed large Bitcoin purchase must fit the Reserve, the card-payoff plan, the work-optional access needs, and the agreed target. A favorable price view does not create additional monthly cash or remove a lender's collateral rules.

Compare the proposed trade with a paced implementation where appropriate. Buying in stages can change timing risk and behavior, but it can also underperform a single purchase if the price rises. It is a trade-off, not a guaranteed improvement. The household should choose a process it can maintain rather than promise itself a perfect entry.

For a sale, identify the spending need, tax lots, and deadline. A committed near-term bill may require a reliable source even when you expect Bitcoin to rise. A flexible long-term holding can have a different decision window. Treat the two jobs separately.

A market indicator or valuation model can provide context, but its limitations matter. Historical relationships can change, signals can remain extreme, and a model cannot tell you the exact day a market will reverse. Avoid presenting a favored chart as certainty about a trade.

Write down what would make you change the decision. It might be a new cash need, a broken assumption, a different target, or a change in debt capacity. A rule stated before the trade is easier to evaluate than an explanation assembled after the price moves.

Two households can have the same view of Bitcoin and make different choices. One needs money for a committed bill soon; the other has uncommitted long-term funds. The price opinion does not give the first household the second household's flexibility. For the Reeds, the current reserve and extra-card claims already use the available money. A more attractive-looking entry does not create another contribution.

Return to Allocation with a clear purpose, an affordable amount, a chosen implementation pace, and the circumstances that would change the decision. You may keep the recurring plan unchanged. This check should make a large decision more deliberate, not become a prerequisite to every ordinary contribution.

### Production notes

No live price predictions, product recommendations, or implied timing alpha. Avoid saying all large drawdowns are better entries. Optional context check, not a new prerequisite for recurring contributions. Return to 4.2 and 4.7.

### Member checkpoint

- State the financial purpose before the market opinion.
- Compare implementation pace and trade-offs.
- Define the conditions that would change the decision.

### Source-led visual and teaching notes — not spoken

Purpose / cash deadline / resources / pace / trade-off. Use generic contrasting household situations, not a live indicator or promised market entry.

Editorial reason: Distinguish price context from affordability and committed funding dates.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Read the proposed trade beside reserve, debt and near-term needs. Compare one-time and paced execution as a trade-off, without inventing outperformance. Use the same target and show which facts would justify changing it. No live prediction or current security recommendation. Return to 4.2 and 4.7.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.

---

# A5.1 — Build a multi-year conversion comparison

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: TAX_REVIEW
Sources: TAX, RETIREMENT, PRIMARY, APP
Use when: a meaningful Traditional balance and a plausible lower-income window make conversions relevant.

### Read aloud

A multi-year conversion plan should leave the household better positioned after the relevant costs, not merely display a larger total of future taxes avoided. Start with the unchanged plan and compare a limited schedule against the same spending and assumptions.

Start with the unchanged plan. Record expected income, spending, taxable-account resources, healthcare years, Social Security, required distributions, and the Traditional and Roth balances. Then choose a bounded conversion schedule to compare against it.

For each year, separate the amount converted from spending withdrawals and the cash used to pay conversion tax. Include the opportunity cost of that tax money. A dollar used for tax today is unavailable for another investment, the Reserve, or a near-term bill.

Use the marginal cost of the proposed conversion. It may span brackets and change other tax or benefit calculations. Marketplace assistance, Social Security taxation, Medicare income-related premiums, state tax, deductions, and credits can alter the total effect.

A sequence of smaller conversions can preserve flexibility, but it can also leave more future taxable growth than a larger early conversion. A large conversion during a market decline may move more units at a lower taxable value, while still creating a cash and access problem. Compare rather than assume.

For the Reed household, hold the retirement spending and market assumptions constant. Compare no added conversion, a modest annual schedule, and a larger early schedule. Read current liquidity, after-tax wealth, future ordinary income, and the surviving spouse or beneficiary implications where supported.

Stress the tax and return assumptions. A strategy based on a large future rate increase can disappoint if withdrawals later occur at lower rates. A strategy that leaves too little taxable money can strain the early-access years even when the Roth balance looks attractive.

The app may model the strategy, but the execution needs current-year verification. Confirm which account may be converted, whether a required distribution must be handled first, any nondeductible basis, the tax-payment method, and the custodian's procedure. Keep planned amounts separate from completed records.

The core example separates a thirty-thousand-dollar conversion from six thousand of hypothetical additional tax. Repeat that separation in every modeled year. If the proposed schedule uses the cash that was supporting the early-retirement bridge or reserve, that is part of its cost. Compare a smaller schedule and no added conversion before treating the future Roth balance as the deciding result.

Choose a range and review rule, with a clear source for each year's tax. Revisit the actual amount using current income and rules before execution. Return to the core tax and withdrawal plan with the comparison understood, not an unchangeable promise to convert for a decade.

### Production notes

IRS Pub590-B/RMD and current tax interaction sources. No assumption all conversions are fully taxable or reversible. Current law and account-specific treatment must be verified. Product comparison primary outcome is total after-tax wealth. Return to 5.4 and 6.4.

### Member checkpoint

- Compare bounded schedules against unchanged spending and assumptions.
- Include tax funding and opportunity cost.
- Verify each actual year's amount before execution.

### Source-led visual and teaching notes — not spoken

Same-date after-tax resources, immediate cash used, access-year funding, and later ordinary income. Keep the $30,000/$6,000 example labeled hypothetical rather than an actual Reed tax result.

Editorial reason: Make conversion schedules account for tax funding and early-year liquidity, not only lifetime tax totals.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Prepare no-added-conversion, modest annual, and larger early alternatives from the same verified inputs. Read cash used for tax, the early-access years, later distributions and after-tax resources at matching dates. Record unmodeled beneficiary or healthcare effects separately. Planned and completed conversions stay distinct. Return to 5.4 and 6.4.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.

---

# A5.2 — Prepare a harvesting transaction that matches the tax record

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: TAX_REVIEW
Sources: TAX, PRIMARY, APP
Use when: an actual taxable holding presents a gain- or loss-harvesting candidate.

### Read aloud

Start with a real candidate holding and the records that support its lots. A harvesting idea is ready to evaluate when you know the units, the identification process, the rest of the year's income, and what exposure you will have afterward.

For a loss, compare current proceeds with adjusted basis and include transaction costs. Identify which existing gains or future tax items the loss may offset. The tax value depends on the actual return and carryforward situation, not simply the size of the loss shown on screen.

For a gain, estimate the amount realized and the effect on the full year's taxable income. A favorable federal capital-gain rate can still come with state tax or other income-related costs. A conversion or unexpected business income can use the same planned tax room.

Verify the identification rules that apply to the asset, account or wallet, custodian, and year. Broker-held digital assets can have different reporting and transitional provisions from assets in an unhosted wallet. Do not assume a software lot-selection preference alone satisfies the requirements.

Replacement exposure needs a separate check. Securities are subject to wash-sale rules under their applicable conditions. Personally held Bitcoin should not be treated as though every stock rule applies identically, but neither should an older crypto-tax article be treated as permanent permission for a particular transaction. Obtain current tax review of the actual sale and any repurchase.

Keep the order clear: model the opportunity, verify the proposed transaction, execute with the provider, then record what actually happened. The recorded proceeds, fees, quantity, identified units, and date should match the confirmation. Reconcile remaining lots and realized activity afterward.

An outside transfer to prepare for a trade may also need to preserve history. Avoid importing the same purchase again at the destination. A network fee and an acquisition cost need their correct supported treatment rather than being hidden by changing quantity until totals match.

For the Reed example, use the three-lot illustration to compare the gain produced by the same sale amount. Then stop before execution and build the evidence checklist. The lowest theoretical tax result is not useful if the records and custodian process do not support it.

In the three-lot example, selling the same amount produces different gains. That comparison is useful only for units you can actually identify under the applicable rules. If the lowest-gain result depends on an unsupported purchase record or a process the custodian cannot carry out, resolve that first or compare an eligible alternative. The best-looking row is not an execution instruction.

Return with either a verified proposed action or a deliberate decision to pass, then record only what actually happens. Preserve the confirmation, remaining-lot continuity and tax-reporting reconciliation. A planning choice made after the sale does not by itself establish that the required identification occurred in time.

### Production notes

Verify current digital-asset identification relief, including IRS Notice2026-20 where applicable. No universal spot-BTC immediate-repurchase safe-harbor claim. FORM8949 data export is not the filed form. Return to 5.1–5.2 and 5.5.

### Member checkpoint

- Verify actual lots, identification, costs, and replacement exposure.
- Separate model, execution, and record stages.
- Reconcile the result with tax reporting and next-year continuity.

### Source-led visual and teaching notes — not spoken

Three-lot comparison alongside evidence, identification timing, replacement exposure and costs. Show proposed → reviewed → external execution → confirmed record; no claimed legal approval from an app dropdown.

Editorial reason: Connect the theoretical harvesting benefit to an eligible transaction and actual record.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Use the existing fictional lot example and one explicitly unknown purchase detail. Compare the sale, review applicable current identification/replacement rules, and prepare the evidence packet. Show a synthetic post-transaction record only as a labeled demonstration; no actual trade. Check repeated history does not add holdings. Return to 5.1–5.2 and 5.5.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.

---

# A5.3 — Evaluate a state move as a household decision

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: TAX_ESTATE_REVIEW
Sources: TAX, ESTATE, PRIMARY
Use when: the household is genuinely considering moving or has income/assets tied to multiple states.

### Read aloud

Evaluate a state move as a household decision. Taxes can be an important benefit, but housing, work, healthcare, family and the cost of moving still have to fit the life you intend to live.

Start with the reason for moving and the realistic locations. Then build the cost difference: housing, property and other taxes, insurance, transport, healthcare, moving expenses, and any income changes. A lower income-tax rate can be offset by higher costs elsewhere.

Tax residency depends on the facts and law, not the address selected in the app. Domicile, time spent, homes, work, family ties, and other evidence can matter. The former state may retain a claim on some income. State-source business, rental, deferred compensation, or other items need specific review.

A large Bitcoin sale near a move makes timing and residency evidence especially important. A brokerage address change alone does not settle where the gain is taxed. Before acting, obtain advice from a professional familiar with both jurisdictions and the actual facts.

For the Reed household, a state scenario should include the full economic changes and the effective date. Keep the current state in the saved baseline until the household chooses and completes the relevant move. Do not use a favorable state assumption to make retirement appear affordable while the family still intends to live elsewhere.

Estate documents, healthcare directives, insurance policies, business registrations, and provider arrangements may also need review after relocation. A legal instrument that worked in one state may need updating for the new circumstances.

Use the model to identify whether the financial difference is meaningful enough to pursue. Then gather the actual rules and implementation requirements. The scenario is a planning comparison; it is not proof of legal residency or a filed tax position.

Before a large Bitcoin sale near a possible move, separate two questions. Does moving improve the household's overall situation? And what do the actual residency and source-income rules mean for the proposed transaction? A favorable address in a scenario does not answer the second question. The household needs the intention, timing and evidence reviewed for both jurisdictions.

Return with a full cost comparison and a specific professional question about the real circumstances. Keep the move hypothetical while it remains an idea. Once the timing and intention support an expected event, record it without treating the app entry as proof of residency or tax treatment.

### Production notes

No state-specific threshold without current jurisdictional research. Generic worksheet does not establish domicile. No tax-avoidance shortcut or backdated-residency advice. Return to 2.4 and 5.3.

### Member checkpoint

- Compare total household costs and life consequences.
- Verify residency and source-income treatment in both jurisdictions.
- Keep the move hypothetical until the intention and timing support a baseline event.

### Source-led visual and teaching notes — not spoken

Current versus proposed household costs with the move date and unresolved legal/tax questions. No invented state thresholds, backdated residency or provider quotes.

Editorial reason: Prevent a modeled tax advantage from replacing the life decision or residency verification.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Compare the same spending needs with the proposed location's actual or clearly hypothetical housing, insurance, healthcare, income and moving costs. Prepare questions for professionals familiar with both states. Record only the intended event, not a legal conclusion. Return to 2.4 and 5.3.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.

---

# A6.1 — Compare healthcare and tax decisions in the same year

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: HEALTH_TAX_REVIEW
Sources: RETIREMENT, TAX, PRIMARY, OWNER
Use when: early-retirement income choices affect coverage assistance or Medicare premiums.

### Read aloud

A tax move can change the cost of healthcare in the same year or a later one. Compare the full effect using one consistent income picture before deciding how much to withdraw or convert.

A taxable sale can provide spending cash while only the gain enters the relevant income calculation. A taxable Traditional withdrawal or Roth conversion can add much more income for the same amount of cash moving. Qualified Roth distributions and cash already held have different treatment. Use the current rules for the specific program.

Build one year's comparison from the same spending need. Include the proposed withdrawals, realized gains, conversion, other income, estimated tax, and net coverage cost. Then compare the alternatives on total cash and future after-tax resources, not only on the federal tax line.

For example, an additional conversion may create a manageable income-tax cost but reduce a premium credit. The combined cost can make a smaller conversion preferable. In another household, paying the higher current cost may still be worthwhile for future tax flexibility. The conclusion depends on the actual estimates and current-year rules.

Marketplace assistance, household size, coverage eligibility, and reconciliation rules can change. Update the marketplace income estimate when the real situation changes, and verify how any advance credit will be reconciled. Do not assume a prior year's expanded assistance applies indefinitely.

At the Medicare transition, enrollment and income-related premium rules require another review. The relevant income measurement and lookback can differ from the marketplace calculation. A large transaction in an earlier year may affect a later premium, subject to the rules and any available reconsideration process.

HSA contributions need a separate eligibility check. Current law, the actual coverage, other coverage, and Medicare enrollment matter. Preserve records for qualified expenses and avoid assuming every high-deductible or low-premium arrangement is HSA-eligible.

A non-insurance option should be compared with clear retained risk. Its lower scheduled payment is not equivalent to an insurance policy's covered-benefit obligation. Review current terms, exclusions, and the household's ability to carry unfunded costs.

Suppose you are comparing a conversion with leaving the account alone. Read the additional income tax, then the change in net coverage cost under the current program rules. If assistance falls, that difference belongs in the same comparison. You may still choose the conversion for a useful future benefit, but the immediate cost is larger than the income-tax line alone. No particular reduction in assistance is assumed until the actual household and year are calculated.

Return to the core plan with coverage dates and costs that agree with the tax assumptions, plus the enrollment and execution checks still needed. Verify current quotes and eligibility before leaving existing coverage. Do not build the decision on a prior year's subsidy or HSA rule without checking it.

### Production notes

Use current IRS PTC/Notice2026-05 and Healthcare.gov/Medicare/SSA sources. No personal medical story or provider-price recommendation. Actual quotes remain private and current. Return to 6.3 and 5.4.

### Member checkpoint

- Compare tax and coverage costs on the same annual income assumptions.
- Verify eligibility and reconciliation/enrollment requirements.
- Update the baseline only after the chosen path is understood.

### Source-led visual and teaching notes — not spoken

Same annual spending need; different withdrawals/conversion; resulting tax and net coverage cost. Keep Marketplace income and Medicare lookback concepts separate, with current-year values outside evergreen narration.

Editorial reason: Make income-sensitive healthcare part of the same economic comparison as the tax decision.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Use one reviewed fictional year and compare no-change versus a bounded conversion/withdrawal. Show modeled tax and any verified coverage effect; external calculations remain clearly labeled when the app does not model them. Check each person's transition date and HSA eligibility separately. No personal medical story or invented quote. Return to 6.3 and 5.4.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.

---

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

---

# A6.3 — Verify an early-retirement account-access route

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: TAX_REVIEW
Sources: RETIREMENT, TAX, PRIMARY
Use when: taxable assets alone do not cover early years or a special access rule may improve the plan.

### Read aloud

Before relying on early retirement money, identify the exact account, year and access rule. The question is not whether an exception exists somewhere; it is whether your planned distribution qualifies and remains workable afterward.

Regular Roth IRA contributions have distribution-ordering treatment different from conversion amounts and earnings. Keep the contribution and conversion records needed to support the amount you plan to use. A five-year rule for a conversion and the requirements for a qualified Roth distribution are related concepts with different jobs.

The workplace-plan exception commonly called the Rule of 55 generally depends on qualifying separation from service and distributions from the relevant employer plan. It does not apply to an IRA simply because the owner is fifty-five. Special rules can apply to certain workers. Verify the account, separation timing, and plan distribution options before relying on the exception.

A rollover can change the access path. Moving an employer-plan balance to an IRA may remove a plan-specific exception that would have been useful. A rollover should therefore be evaluated against the intended early-retirement funding before it is executed.

Governmental 457(b) arrangements can have different additional-tax treatment, with important distinctions for rollover money and other conditions. Identify what the account actually is rather than assuming all workplace savings share the same rules.

Substantially equal periodic payments, often called SEPP or 72(t) payments, can provide another route. The amount, approved method, account structure, and required duration need careful verification. The arrangement generally must continue for at least five years or until age fifty-nine and a half, whichever is later, subject to applicable exceptions. An improper modification can trigger retroactive additional tax and interest.

That rigidity is why this is an advanced option. A member who needs a flexible bridge may find a fixed periodic-payment commitment poorly matched to changing spending. The account balance, investment path, and other resources must support the schedule.

For Alex and Morgan, first price the actual gap and test whether contribution routing can build enough accessible money. Then compare a verified special-access route only if it materially helps. Each spouse's age and accounts must be treated separately.

The planning sheet should identify the account, expected distribution, tax treatment, exception relied on, evidence required, and actions that would invalidate the plan. Have a qualified tax professional verify it before the first distribution or rollover.

A rollover illustrates why the order matters. A workplace-plan access route can be useful for a particular separation date, while moving that money to an IRA can change the route. Review the bridge before submitting the rollover. For a rigid periodic-payment arrangement, also ask whether the household can maintain the required schedule when spending or markets change. Technical eligibility is only part of a usable plan.

Return with the amount, timing, exact account, evidence and conditions for the chosen access path. Have the tax professional verify it before the first dependent distribution or rollover. Keep each spouse's records separate and name the actions that could invalidate the plan.

### Production notes

IRS Pub590-B, early-distribution exception chart, and SEPP guidance. No individualized SEPP calculation or execution without verified account data and review. Distinguish rule55 and governmental457, Roth IRA and workplaceRoth. Return to 6.2 and 4.3.

### Member checkpoint

- Identify the exact account, amount, year, and access rule.
- Verify rollover and ongoing-compliance consequences.
- Obtain review before any distribution dependent on an exception.

### Source-led visual and teaching notes — not spoken

Account / person / year / amount / rule / evidence / invalidating action. Keep regular Roth contributions, conversions and earnings separate; no single unlock icon for all retirement accounts.

Editorial reason: Make early-access rules a verified account-specific action sequence, especially before a rollover.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Inspect one bridge year and the actual account intended to fund it. Review the distribution route, tax treatment and ongoing obligations, then compare the same need with accessible taxable resources. Use no individualized SEPP output without complete inputs and professional review. Return to 6.2 and 4.3.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.

---

# A7.1 — Compare passphrase, multisig, and professional support

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: DEVICE_CUSTODY_REVIEW
Sources: CUSTODY, DICTATION, PRIMARY, OWNER
Use when: the basic custody arrangement leaves a named failure that another architecture may address.

### Read aloud

Choose a more advanced custody arrangement only after naming the failure it needs to address. A passphrase, multisig, professional custody and collaborative support solve different problems and require different recovery information.

A passphrase changes the wallet derived from the recovery material. It adds another exact secret to preserve. A wrong passphrase can produce a different valid wallet, which makes testing and documentation important. It does not create a second cryptographic signer or a legal approval process.

Multisig requires a defined combination of keys. A two-of-three policy can survive one unavailable key if the other required resources remain usable. It also requires configuration information and compatible recovery tools. Test which combinations work, including a provider-independent path when the arrangement claims to provide one.

Collaborative support can help a household maintain that process. Read which key the provider holds, what it can and cannot do, the approval process, recovery fees, identity requirements, and what happens if it disappears. Provider involvement is not automatically equivalent to provider control of the entire asset.

Institutional custody may simplify key management and family administration, but it creates a contractual and counterparty dependence. Review ownership, segregation, withdrawal restrictions, legal process, and the exact services offered. A retirement or brokerage structure adds its own wrapper and beneficiary rules.

An intentional split can preserve direct control over one portion and professional support for another. Define the purpose and maximum exposure of each portion. More methods are useful only when they remove meaningful dependence without creating an unmaintainable process.

Use a non-secret comparison table: protection gained, new failure introduced, recovery requirements, family usability, cost, and review cadence. Keep the signing material and sensitive configuration outside the ordinary course workbook.

Before moving meaningful funds, conduct a small-value test using current vendor instructions. Verify the complete recovery path, not merely the ability to sign one transaction today. Involve the professional needed for the actual arrangement.

Test the proposed improvement under the failure you named. If a component or provider is unavailable, can the remaining resources recover the intended wallet under that actual setup? A second device is not automatically a second signer, and a passphrase is not a substitute for a tested threshold policy. Adding complexity helps only when the household can still maintain and recover the arrangement.

Return with the simplest method that meets the household's control and continuity needs, the risk it still retains, and the exact safe test required. Keep configuration and secrets in the protected recovery process, not the ordinary family worksheet.

### Production notes

Exact BIP39/passphrase and multisig configuration claims need current primary vendor/spec verification. No funded seed demonstration. Attorney/custody coordination for actual family design. Return to 7.1–7.2 and 8.2.

### Member checkpoint

- Name the failure each proposed architecture addresses.
- Test the complete recovery path and dependencies.
- Document the non-secret choice and retained risks.

### Source-led visual and teaching notes — not spoken

Protection gained / new responsibility / failure retained / recovery requirements / family starting path. No secret strings, descriptor contents or universal passphrase-split design.

Editorial reason: Evaluate advanced custody against a specific unavailable-component case rather than complexity or wealth level.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Compare the actual methods using public specifications and the relevant provider agreement. Rehearse the non-secret absence path and separately verify the claimed signing/recovery combinations on a safe test setup. A practice test does not certify a different funded wallet. Return to 7.1–7.2 and 8.2.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.

---

# A7.2 — Decide which custody responsibilities the household can maintain

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: CUSTODY_REVIEW
Sources: CUSTODY, BRAIN, CLIENT_THEMES
Use when: the household is uncertain whether a custody arrangement fits its actual capability and time.

### Read aloud

Decide which custody responsibilities you and your household can realistically maintain. The right arrangement needs to work during ordinary life and when the person most comfortable with the technology is unavailable.

List the recurring responsibilities. Maintaining backups, checking provider changes, verifying addresses, managing authentication, updating devices, testing recovery, and keeping the family process current all take attention. A procedure you are unlikely to repeat should not be the only protection for life-changing assets.

Consider an absence. If the usual operator is traveling, ill, or unavailable for months, who can identify the correct first step? That person may need a professional helper rather than direct access to every secret. The legal authority and technical role should fit together.

Also consider how you respond to pressure. Someone who tends to rush when a support message sounds urgent needs a strong pause-and-verify routine. A more complex interface can increase mistakes even when the underlying security model is sound.

For the Reed household, Alex may be more comfortable with wallet operations while Morgan prefers a documented process with professional support. The plan can accommodate both preferences by defining which portion is directly controlled and how the family starts recovery. It does not need to force both people to become experts in every technical detail.

Use small test operations to find gaps. Can you verify a destination? Restore the intended wallet? Recognize a passphrase mismatch? Contact the provider through a known channel? Explain which information should never be disclosed? Those practical answers are more useful than saying you are generally comfortable with technology.

If the work is excessive, simplify. Fewer independently maintained methods may be better than a large collection of accounts and backups with unclear ownership. Professional support can be a deliberate choice when it solves a real operational need, subject to its own risks.

Suppose one member of the household is comfortable operating the wallet and the other prefers a documented process with professional help. The handoff can respect both. The second person needs to recognize the first safe action and the right contact; they do not need every secret or technical detail in the opening letter. Check that the designated support actually provides the role you are relying on.

Return with responsibilities assigned, a backup starting path, and a test that shows what still needs work. Simplify or add appropriate support when a critical responsibility has no reliable owner. Professional help is a deliberate trade-off, not a claim that operational or counterparty risk disappears.

### Production notes

No shame-based sovereignty or mandatory wealth ladder. No assertion support removes counterparty risk. Fictional roles are pedagogical and not statements about actual clients or Austin. Return to 7.1 and 7.4.

### Member checkpoint

- Assign recurring responsibilities and an absence path.
- Test practical capabilities rather than assuming comfort.
- Simplify or add support where a named responsibility is uncovered.

### Source-led visual and teaching notes — not spoken

Responsibility owner, backup, frequency and proof. Use fictional conditional roles instead of asserting unverified capabilities of the Reeds or actual clients.

Editorial reason: Translate comfort and support preferences into specific owned responsibilities and an absence plan.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Walk the non-secret task list: address verification, recovery check, account authentication, provider changes and family instructions. Rehearse the unavailable-operator case with a consented listener and record actual gaps. No real secret sharing or claimed test before it happens. Return to 7.1 and 7.4.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.

---

# A7.3 — Test correlated failures across providers and methods

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: CUSTODY_REVIEW
Sources: CUSTODY, BRAIN, PRIMARY
Use when: several accounts or custody methods appear diversified but may share dependencies.

### Read aloud

Two accounts are only useful protection against a failure when that failure does not take out both. Trace the shared provider, recovery channel, location and person behind each method before calling the arrangement independent.

Two exchanges may rely on the same custodian. Two devices may share a software path. Several backups can be stored in one disaster zone. Different accounts may all be recoverable through the same email and phone. A family can have many documents and still depend on one person to interpret them.

Draw a simple dependency map. For each meaningful pool, identify the provider, signing method, recovery material, authentication channel, location category, and person who starts the process. Keep exact sensitive details in the separate protected system.

Then test one failure at a time. What becomes unavailable if the email is lost? If one provider stops serving customers? If a device and its nearby backup are destroyed? If the operator is absent? Which remaining resources actually restore access, and how has that been verified?

Also test combinations that plausibly occur together. A home disaster may affect devices, paper records, and communication access. A provider event may affect several branded services. A family emergency may reduce the time and expertise available to solve a technical problem.

For Alex and Morgan, an intentional split should reduce exposure to the failures they care about. It should not merely create another login or move Bitcoin between two services sharing the same underlying dependence. The amount assigned to each method should reflect both its job and the consequence of failure.

A lender is another custody exposure. A loan can be modest relative to total wealth while a large share of the Bitcoin is held as collateral. Record that dependence in the same family risk picture rather than isolating it in a separate borrowing spreadsheet.

The outcome is a short list of meaningful changes: separate a recovery dependence, reduce a provider concentration, prove an independent recovery path, or simplify a process. No system eliminates every risk. The objective is to know which failures remain and keep any one of them from unnecessarily controlling the whole plan.

For example, adding a second provider does little for a recovery problem when both logins depend on the same unavailable email and phone. Fixing that dependency may be more useful than adding a third account. Likewise, separate brands may share a custodian. Verify the actual arrangement before deciding which portion of the plan is protected from that failure.

Return with the shared failure you identified, the targeted change, and the way its independence will be tested. Keep sensitive locations and complete recovery routes outside the ordinary map. More accounts are justified when they reduce a meaningful consequence the family can still manage.

### Production notes

No unsupported security claims about named providers. Independence must be verified from actual architecture, not branding. Do not publish configuration/locations or detailed recovery sequences. Return to 7.3 and 8.2.

### Member checkpoint

- Map shared dependencies and correlated failures.
- Verify an independent recovery route where claimed.
- Choose a targeted change and a review trigger.

### Source-led visual and teaching notes — not spoken

Non-secret dependency map with one failure highlighted across multiple pools. Include lender-held collateral in the same exposure picture; no actual addresses, credentials or detailed recovery sequences.

Editorial reason: Make apparent diversification a testable dependency question rather than account count.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Remove one hypothetical provider, email/phone recovery route, location category or operator from the map. Identify which pools remain usable and what evidence supports the alternative path. Review one correlated combination. Keep the result a design/test plan until the real safe test is completed. Return to 7.3 and 8.2.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.

---

# A7.4 — Understand UTXOs before consolidating coins

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: DEVICE_CAPTURE
Sources: CUSTODY, PRIMARY
Use when: the household has many small Bitcoin receipts or is considering consolidation or coin control.

### Read aloud

Before consolidating Bitcoin, understand what you are combining and why. A balance can be made of many unspent outputs. Spending more inputs can affect transaction size, fees and privacy, even when the total Bitcoin sent is the same.

Transaction fees depend primarily on the transaction's data weight and the fee rate, not simply on the dollar amount being sent. Spending many small outputs can require more transaction data than spending one larger output of the same total value.

That matters for frequent small withdrawals or long histories of small receipts. A balance may be worth holding, yet parts can be expensive to spend when fees are high. There is no permanent dollar or Bitcoin threshold that is correct in every fee environment.

Consolidation spends several outputs into fewer outputs you control. It can reduce the number of inputs needed later, but it also has a fee today and privacy consequences. Combining outputs can link them on the public transaction graph. Coin control can help manage which outputs are combined when the wallet supports it.

First identify the purpose. Are you reducing future spending complexity, preparing for a planned transaction, or responding to a fee concern? Then check current fee conditions, wallet support, backup status, and the privacy trade-off. Consolidating everything because a course mentioned it is not a useful rule.

Use the correct network and verify the destination through the trusted device process. A transaction to yourself still needs careful review. Confirm that the wallet and tax records preserve the movement and any relevant fee treatment without inventing a new purchase at the current price.

For multisig or other wallet types, input size and recovery requirements can differ. Use the actual wallet's current documentation and test with a small value where appropriate. Avoid manually following a procedure written for a different script type or device.

The separate demonstration uses a small test setup. Match any procedure to your own wallet and backup method before using it. You may conclude that no consolidation is necessary now.

Use the wallet's fee preview and coin selection to compare a proposed transaction with fewer inputs. The useful question is whether paying a fee now and linking those outputs is worth the possible later simplification. Current fee conditions can change, and the actual size depends on the wallet and transaction. A course example cannot supply a permanent consolidation threshold for your holdings.

Return with a deliberate decision to consolidate or leave the outputs alone, the fee/privacy trade-off understood, and a verified safe transaction process. Match any procedure to your own wallet and backup method. More wallet activity is not itself an improvement.

### Production notes

Use Bitcoin developer documentation and current wallet-specific coin-control instructions. No universal dust cutoff, fee quote, address publication, or secret display. Tax treatment of network fees requires applicable review. Return to 7.2–7.4.

### Member checkpoint

- Explain output count, fee weight, and consolidation trade-offs.
- Verify wallet support and recovery before transacting.
- Consolidate only for a defined purpose under a safe current procedure.

### Source-led visual and teaching notes — not spoken

Generic inputs → recipient/change outputs and a fee-preview comparison; no actual wallet address or live fee quote. Distinguish a self-transfer from a new purchase in tax history.

Editorial reason: Make coin consolidation a conditional maintenance decision with fee and privacy consequences.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

On the separately approved test setup, inspect output selection and the actual fee preview without revealing sensitive identifiers. Compare input counts, explain privacy links and verify the destination on the trusted device. No transaction until the exact wallet procedure and recovery status are reviewed. Return to 7.2–7.4.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.

---

# A8.1 — Decide whether a trust has a job in the plan

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: ESTATE_TAX_REVIEW
Sources: ESTATE, ESTATE_DECK, PRIMARY, OWNER
Use when: probate, incapacity, beneficiaries, tax, control, or a complex asset creates a specific trust question.

### Read aloud

Start with the legal or family job a trust would solve. Owning Bitcoin by itself does not tell you which trust to use, and signing a trust document does not complete the account and custody work needed to make it useful.

The household may want continuity during incapacity, coordinated administration, privacy, a distribution arrangement for children, management for a vulnerable beneficiary, or planning for tax or creditor concerns. Each objective requires different analysis. Simply owning Bitcoin does not identify which trust, if any, is appropriate.

A revocable living trust can support administration and continuity when properly created and funded. Retaining control generally means the assets remain part of the relevant owner's tax and creditor picture under applicable rules. It is not a universal estate-tax or asset-protection solution.

An irrevocable arrangement can change control, taxation, access, and beneficiary rights. Those consequences can be difficult to reverse. Grantor and non-grantor describe income-tax treatment, not a simple ranking of better and worse trusts. The trustee, powers, funding, distributions, and jurisdiction matter.

Specialized charitable structures, including a charitable lead trust, have specific charitable and remainder-beneficiary purposes and technical tax requirements. They belong in professional design for a household with that actual goal. The attorney and tax professional need to test the proposed funding and obligations under less favorable outcomes, including lower Bitcoin returns.

Bitcoin creates operational questions alongside the legal drafting. Who can authorize investment decisions? Who can sign? How are custody, concentration, fees, recovery, and successor trustees handled? Can the named people actually carry out the trust's requirements? A clause expressing a preference for Bitcoin does not replace review of fiduciary duties and the full document.

The trust also needs to be funded and coordinated with the other assets. Signing a document does not automatically retitle every account or update every beneficiary. Retirement accounts require particular care; do not move or name assets without coordinated tax and legal advice.

For Alex and Morgan, the initial question is whether their legal baseline and beneficiary arrangements solve the family needs. If a trust adds a useful job, they prepare the ownership inventory, intended beneficiaries, desired control, custody methods, and questions for the attorney. If no additional job exists, completing the baseline is a valid outcome.

Compare the proposed trust with the simpler baseline. If the need is a clear beneficiary designation and a usable family starting process, identify what extra job the trust adds. If the need is continuing management or controlled distributions for a child or vulnerable beneficiary, explain that specific objective to the attorney. The custody and successor arrangements then need to support the actual legal design, not a generic Bitcoin clause.

Return with a professionally reviewed decision, the funding or beneficiary actions it requires, and the people responsible for operating it. Keep revocability, tax classification, legal control and practical signing authority distinct. The worksheet organizes the conversation; it does not create or validate the trust.

### Production notes

Revocable/irrevocable and grantor/non-grantor are separate classifications. Legacy CLAT/estate-growth examples are retained only as specialized questions, not recommended structures or promised tax results. State-specific law, tax, trust instrument, and custody review required. Return to 8.1–8.3.

### Member checkpoint

- Name the legal or family job a trust would solve.
- Review control, tax, funding, beneficiary, and custody consequences.
- Complete the professional and outside implementation steps honestly.

### Source-led visual and teaching notes — not spoken

Problem → simpler baseline → proposed trust job → legal design → funding/beneficiary actions → custody and successor process. No generic tax-savings result, creditor shield or fixed Bitcoin-concentration waiver.

Editorial reason: Compare a trust with the existing baseline and follow a useful structure through actual funding and operation.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Use the non-secret ownership inventory and intended beneficiary/continuity goals. Prepare focused attorney and tax questions, then identify account, title, beneficiary and recovery changes requiring execution. No drafted legal clauses, named tax structure recommendation or assumed provider acceptance. Return to 8.1–8.3.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.
