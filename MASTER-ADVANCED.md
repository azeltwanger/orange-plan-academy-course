# Advanced library

Generated from canonical `scripts/`. New prose is a pre-dictation draft, not a claim Austin already said it. Production notes and member checkpoints are not spoken.

# A1.1 — Test an assumption without making the model tell you what you want

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

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

---

# A3.1 — Build a Bitcoin-loan operating sheet from the actual contract

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

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

---

# A3.2 — Compare financing terms that a simple payment hides

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

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

---

# A4.1 — Check price context before a large allocation change

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

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

---

# A5.1 — Build a multi-year conversion comparison

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

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

---

# A5.2 — Prepare a harvesting transaction that matches the tax record

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

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

---

# A5.3 — Evaluate a state move as a household decision

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/01-modeling-financing-and-tax.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

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

---

# A6.1 — Compare healthcare and tax decisions in the same year

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: HEALTH_TAX_REVIEW
Sources: RETIREMENT, TAX, PRIMARY, OWNER
Use when: early-retirement income choices affect coverage assistance or Medicare premiums.

### Read aloud

The income number used for healthcare assistance is not always the same as the cash the household spends. That distinction can make the tax and coverage decisions interact.

A taxable sale can provide spending cash while only the gain enters the relevant income calculation. A taxable Traditional withdrawal or Roth conversion can add much more income for the same amount of cash moving. Qualified Roth distributions and cash already held have different treatment. Use the current rules for the specific program.

Build one year's comparison from the same spending need. Include the proposed withdrawals, realized gains, conversion, other income, estimated tax, and net coverage cost. Then compare the alternatives on total cash and future after-tax resources, not only on the federal tax line.

For example, an additional conversion may create a manageable income-tax cost but reduce a premium credit. The combined cost can make a smaller conversion preferable. In another household, paying the higher current cost may still be worthwhile for future tax flexibility. The conclusion depends on the actual estimates and current-year rules.

Marketplace assistance, household size, coverage eligibility, and reconciliation rules can change. Update the marketplace income estimate when the real situation changes, and verify how any advance credit will be reconciled. Do not assume a prior year's expanded assistance applies indefinitely.

At the Medicare transition, enrollment and income-related premium rules require another review. The relevant income measurement and lookback can differ from the marketplace calculation. A large transaction in an earlier year may affect a later premium, subject to the rules and any available reconsideration process.

HSA contributions need a separate eligibility check. Current law, the actual coverage, other coverage, and Medicare enrollment matter. Preserve records for qualified expenses and avoid assuming every high-deductible or low-premium arrangement is HSA-eligible.

A non-insurance option should be compared with clear retained risk. Its lower scheduled payment is not equivalent to an insurance policy's covered-benefit obligation. Review current terms, exclusions, and the household's ability to carry unfunded costs.

Return to the core plan with a realistic coverage cost, the correct dates for each person, and a tax decision reviewed under the same assumptions. Before leaving existing coverage or executing a material conversion, verify the current quotes, eligibility, enrollment deadlines, and tax interactions with the appropriate professionals.

### Production notes

Use current IRS PTC/Notice2026-05 and Healthcare.gov/Medicare/SSA sources. No personal medical story or provider-price recommendation. Actual quotes remain private and current. Return to 6.3 and 5.4.

### Member checkpoint

- Compare tax and coverage costs on the same annual income assumptions.
- Verify eligibility and reconciliation/enrollment requirements.
- Update the baseline only after the chosen path is understood.

---

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

---

# A6.3 — Verify an early-retirement account-access route

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: TAX_REVIEW
Sources: RETIREMENT, TAX, PRIMARY
Use when: taxable assets alone do not cover early years or a special access rule may improve the plan.

### Read aloud

Start with the amount and year you need to fund. Then identify the exact account and the rule that could make it available. Early access is an account-specific planning problem.

Regular Roth IRA contributions have distribution-ordering treatment different from conversion amounts and earnings. Keep the contribution and conversion records needed to support the amount you plan to use. A five-year rule for a conversion and the requirements for a qualified Roth distribution are related concepts with different jobs.

The workplace-plan exception commonly called the Rule of 55 generally depends on qualifying separation from service and distributions from the relevant employer plan. It does not apply to an IRA simply because the owner is fifty-five. Special rules can apply to certain workers. Verify the account, separation timing, and plan distribution options before relying on the exception.

A rollover can change the access path. Moving an employer-plan balance to an IRA may remove a plan-specific exception that would have been useful. A rollover should therefore be evaluated against the intended early-retirement funding before it is executed.

Governmental 457(b) arrangements can have different additional-tax treatment, with important distinctions for rollover money and other conditions. Identify what the account actually is rather than assuming all workplace savings share the same rules.

Substantially equal periodic payments, often called SEPP or 72(t) payments, can provide another route. The amount, approved method, account structure, and required duration need careful verification. The arrangement generally must continue for at least five years or until age fifty-nine and a half, whichever is later, subject to applicable exceptions. An improper modification can trigger retroactive additional tax and interest.

That rigidity is why this is an advanced option. A member who needs a flexible bridge may find a fixed periodic-payment commitment poorly matched to changing spending. The account balance, investment path, and other resources must support the schedule.

For Alex and Morgan, first price the actual gap and test whether contribution routing can build enough accessible money. Then compare a verified special-access route only if it materially helps. Each spouse's age and accounts must be treated separately.

The planning sheet should identify the account, expected distribution, tax treatment, exception relied on, evidence required, and actions that would invalidate the plan. Have a qualified tax professional verify it before the first distribution or rollover.

Return to the retirement-paycheck plan with the approved access assumptions and a recordkeeping process. A technically possible exception is useful only when the household can execute and maintain it correctly.

### Production notes

IRS Pub590-B, early-distribution exception chart, and SEPP guidance. No individualized SEPP calculation or execution without verified account data and review. Distinguish rule55 and governmental457, Roth IRA and workplaceRoth. Return to 6.2 and 4.3.

### Member checkpoint

- Identify the exact account, amount, year, and access rule.
- Verify rollover and ongoing-compliance consequences.
- Obtain review before any distribution dependent on an exception.

---

# A7.1 — Compare passphrase, multisig, and professional support

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: DEVICE_CUSTODY_REVIEW
Sources: CUSTODY, DICTATION, PRIMARY, OWNER
Use when: the basic custody arrangement leaves a named failure that another architecture may address.

### Read aloud

Begin with the failure you want to address. A passphrase, multisig, and professional custody solve different problems and create different responsibilities.

A passphrase changes the wallet derived from the recovery material. It adds another exact secret to preserve. A wrong passphrase can produce a different valid wallet, which makes testing and documentation important. It does not create a second cryptographic signer or a legal approval process.

Multisig requires a defined combination of keys. A two-of-three policy can survive one unavailable key if the other required resources remain usable. It also requires configuration information and compatible recovery tools. Test which combinations work, including a provider-independent path when the arrangement claims to provide one.

Collaborative support can help a household maintain that process. Read which key the provider holds, what it can and cannot do, the approval process, recovery fees, identity requirements, and what happens if it disappears. Provider involvement is not automatically equivalent to provider control of the entire asset.

Institutional custody may simplify key management and family administration, but it creates a contractual and counterparty dependence. Review ownership, segregation, withdrawal restrictions, legal process, and the exact services offered. A retirement or brokerage structure adds its own wrapper and beneficiary rules.

An intentional split can preserve direct control over one portion and professional support for another. Define the purpose and maximum exposure of each portion. More methods are useful only when they remove meaningful dependence without creating an unmaintainable process.

Use a non-secret comparison table: protection gained, new failure introduced, recovery requirements, family usability, cost, and review cadence. Keep the signing material and sensitive configuration outside the ordinary course workbook.

Before moving meaningful funds, conduct a small-value test using current vendor instructions. Verify the complete recovery path, not merely the ability to sign one transaction today. Involve the professional needed for the actual arrangement.

Return to the core custody map with the simplest architecture that meets the household's requirements and can be maintained over time. A complex setup that only one person understands has not solved the family problem.

### Production notes

Exact BIP39/passphrase and multisig configuration claims need current primary vendor/spec verification. No funded seed demonstration. Attorney/custody coordination for actual family design. Return to 7.1–7.2 and 8.2.

### Member checkpoint

- Name the failure each proposed architecture addresses.
- Test the complete recovery path and dependencies.
- Document the non-secret choice and retained risks.

---

# A7.2 — Decide which custody responsibilities the household can maintain

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: CUSTODY_REVIEW
Sources: CUSTODY, BRAIN, CLIENT_THEMES
Use when: the household is uncertain whether a custody arrangement fits its actual capability and time.

### Read aloud

Choose a custody arrangement the household can maintain during ordinary life and under stress. Technical capability today is only part of that decision.

List the recurring responsibilities. Maintaining backups, checking provider changes, verifying addresses, managing authentication, updating devices, testing recovery, and keeping the family process current all take attention. A procedure you are unlikely to repeat should not be the only protection for life-changing assets.

Consider an absence. If the usual operator is traveling, ill, or unavailable for months, who can identify the correct first step? That person may need a professional helper rather than direct access to every secret. The legal authority and technical role should fit together.

Also consider how you respond to pressure. Someone who tends to rush when a support message sounds urgent needs a strong pause-and-verify routine. A more complex interface can increase mistakes even when the underlying security model is sound.

For the Reed household, Alex may be more comfortable with wallet operations while Morgan prefers a documented process with professional support. The plan can accommodate both preferences by defining which portion is directly controlled and how the family starts recovery. It does not need to force both people to become experts in every technical detail.

Use small test operations to find gaps. Can you verify a destination? Restore the intended wallet? Recognize a passphrase mismatch? Contact the provider through a known channel? Explain which information should never be disclosed? Those practical answers are more useful than saying you are generally comfortable with technology.

If the work is excessive, simplify. Fewer independently maintained methods may be better than a large collection of accounts and backups with unclear ownership. Professional support can be a deliberate choice when it solves a real operational need, subject to its own risks.

Finish with the responsibilities you will own, the ones a provider or professional will handle, and the way you will verify they remain covered. Return to the core custody choice with a process the household will actually use.

### Production notes

No shame-based sovereignty or mandatory wealth ladder. No assertion support removes counterparty risk. Fictional roles are pedagogical and not statements about actual clients or Austin. Return to 7.1 and 7.4.

### Member checkpoint

- Assign recurring responsibilities and an absence path.
- Test practical capabilities rather than assuming comfort.
- Simplify or add support where a named responsibility is uncovered.

---

# A7.3 — Test correlated failures across providers and methods

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: CUSTODY_REVIEW
Sources: CUSTODY, BRAIN, PRIMARY
Use when: several accounts or custody methods appear diversified but may share dependencies.

### Read aloud

Multiple accounts do not automatically create independent protection. Trace the dependencies behind each method.

Two exchanges may rely on the same custodian. Two devices may share a software path. Several backups can be stored in one disaster zone. Different accounts may all be recoverable through the same email and phone. A family can have many documents and still depend on one person to interpret them.

Draw a simple dependency map. For each meaningful pool, identify the provider, signing method, recovery material, authentication channel, location category, and person who starts the process. Keep exact sensitive details in the separate protected system.

Then test one failure at a time. What becomes unavailable if the email is lost? If one provider stops serving customers? If a device and its nearby backup are destroyed? If the operator is absent? Which remaining resources actually restore access, and how has that been verified?

Also test combinations that plausibly occur together. A home disaster may affect devices, paper records, and communication access. A provider event may affect several branded services. A family emergency may reduce the time and expertise available to solve a technical problem.

For Alex and Morgan, an intentional split should reduce exposure to the failures they care about. It should not merely create another login or move Bitcoin between two services sharing the same underlying dependence. The amount assigned to each method should reflect both its job and the consequence of failure.

A lender is another custody exposure. A loan can be modest relative to total wealth while a large share of the Bitcoin is held as collateral. Record that dependence in the same family risk picture rather than isolating it in a separate borrowing spreadsheet.

The outcome is a short list of meaningful changes: separate a recovery dependence, reduce a provider concentration, prove an independent recovery path, or simplify a process. No system eliminates every risk. The objective is to know which failures remain and keep any one of them from unnecessarily controlling the whole plan.

Return to Protect with the completed non-secret map, the tested path, and the next review trigger. Revisit when the balance becomes materially larger or a provider, person, or device changes.

### Production notes

No unsupported security claims about named providers. Independence must be verified from actual architecture, not branding. Do not publish configuration/locations or detailed recovery sequences. Return to 7.3 and 8.2.

### Member checkpoint

- Map shared dependencies and correlated failures.
- Verify an independent recovery route where claimed.
- Choose a targeted change and a review trigger.

---

# A7.4 — Understand UTXOs before consolidating coins

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: DEVICE_CAPTURE
Sources: CUSTODY, PRIMARY
Use when: the household has many small Bitcoin receipts or is considering consolidation or coin control.

### Read aloud

A Bitcoin balance can consist of many separate unspent transaction outputs, usually called UTXOs. When you spend, the wallet selects outputs as inputs and creates new outputs for the recipient and any change.

Transaction fees depend primarily on the transaction's data weight and the fee rate, not simply on the dollar amount being sent. Spending many small outputs can require more transaction data than spending one larger output of the same total value.

That matters for frequent small withdrawals or long histories of small receipts. A balance may be worth holding, yet parts can be expensive to spend when fees are high. There is no permanent dollar or Bitcoin threshold that is correct in every fee environment.

Consolidation spends several outputs into fewer outputs you control. It can reduce the number of inputs needed later, but it also has a fee today and privacy consequences. Combining outputs can link them on the public transaction graph. Coin control can help manage which outputs are combined when the wallet supports it.

First identify the purpose. Are you reducing future spending complexity, preparing for a planned transaction, or responding to a fee concern? Then check current fee conditions, wallet support, backup status, and the privacy trade-off. Consolidating everything because a course mentioned it is not a useful rule.

Use the correct network and verify the destination through the trusted device process. A transaction to yourself still needs careful review. Confirm that the wallet and tax records preserve the movement and any relevant fee treatment without inventing a new purchase at the current price.

For multisig or other wallet types, input size and recovery requirements can differ. Use the actual wallet's current documentation and test with a small value where appropriate. Avoid manually following a procedure written for a different script type or device.

The separate demonstration uses a small test setup. Match any procedure to your own wallet and backup method before using it. You may conclude that no consolidation is necessary now.

Return to the core custody plan with a deliberate maintenance decision, the privacy and fee trade-offs recorded, and a tested transaction process. The aim is future usability, not maximizing activity on the wallet.

### Production notes

Use Bitcoin developer documentation and current wallet-specific coin-control instructions. No universal dust cutoff, fee quote, address publication, or secret display. Tax treatment of network fees requires applicable review. Return to 7.2–7.4.

### Member checkpoint

- Explain output count, fee weight, and consolidation trade-offs.
- Verify wallet support and recovery before transacting.
- Consolidate only for a defined purpose under a safe current procedure.

---

# A8.1 — Decide whether a trust has a job in the plan

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: ESTATE_TAX_REVIEW
Sources: ESTATE, ESTATE_DECK, PRIMARY, OWNER
Use when: probate, incapacity, beneficiaries, tax, control, or a complex asset creates a specific trust question.

### Read aloud

A trust should solve an identifiable legal or family problem. Start with the job before choosing a structure.

The household may want continuity during incapacity, coordinated administration, privacy, a distribution arrangement for children, management for a vulnerable beneficiary, or planning for tax or creditor concerns. Each objective requires different analysis. Simply owning Bitcoin does not identify which trust, if any, is appropriate.

A revocable living trust can support administration and continuity when properly created and funded. Retaining control generally means the assets remain part of the relevant owner's tax and creditor picture under applicable rules. It is not a universal estate-tax or asset-protection solution.

An irrevocable arrangement can change control, taxation, access, and beneficiary rights. Those consequences can be difficult to reverse. Grantor and non-grantor describe income-tax treatment, not a simple ranking of better and worse trusts. The trustee, powers, funding, distributions, and jurisdiction matter.

Specialized charitable structures, including a charitable lead trust, have specific charitable and remainder-beneficiary purposes and technical tax requirements. They belong in professional design for a household with that actual goal. The attorney and tax professional need to test the proposed funding and obligations under less favorable outcomes, including lower Bitcoin returns.

Bitcoin creates operational questions alongside the legal drafting. Who can authorize investment decisions? Who can sign? How are custody, concentration, fees, recovery, and successor trustees handled? Can the named people actually carry out the trust's requirements? A clause expressing a preference for Bitcoin does not replace review of fiduciary duties and the full document.

The trust also needs to be funded and coordinated with the other assets. Signing a document does not automatically retitle every account or update every beneficiary. Retirement accounts require particular care; do not move or name assets without coordinated tax and legal advice.

For Alex and Morgan, the initial question is whether their legal baseline and beneficiary arrangements solve the family needs. If a trust adds a useful job, they prepare the ownership inventory, intended beneficiaries, desired control, custody methods, and questions for the attorney. If no additional job exists, completing the baseline is a valid outcome.

Return to the family-handoff plan with a professional-reviewed decision, any funding or beneficiary actions, and an operational process matched to the documents. The course worksheet organizes the conversation; the attorney creates and reviews the legal arrangement.

### Production notes

Revocable/irrevocable and grantor/non-grantor are separate classifications. Legacy CLAT/estate-growth examples are retained only as specialized questions, not recommended structures or promised tax results. State-specific law, tax, trust instrument, and custody review required. Return to 8.1–8.3.

### Member checkpoint

- Name the legal or family job a trust would solve.
- Review control, tax, funding, beneficiary, and custody consequences.
- Complete the professional and outside implementation steps honestly.
