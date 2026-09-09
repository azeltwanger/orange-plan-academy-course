# For your situation — collected teaching notes

Generated from `scripts/`. Spoken text is under Read aloud; production notes and checkpoints are not narration. Owner review and actual app/device recording remain separate.

This is a reference index, not a second course or a higher level. The A-prefixed IDs and filename are retained for existing links. Use a lesson when its stated situation applies, then return to the indicated walkthrough.

# A1.1 — Test an assumption without making the model tell you what you want

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: APP_CAPTURE
Sources: FOUNDATION, BRAIN, APP, PRIMARY
Use when: You need custom assumptions or a holding-specific model to answer a planning question.
After lesson: 1.4
Complete before: Complete before relying on the custom assumption or override.
Return to: W01 chapter 8, then lesson 1.5

### Read aloud

Use this lesson when you need to test an assumption the normal settings don't express. Start with the question you want the comparison to answer.

Suppose the plan supports your preferred retirement date under the current Bitcoin path, but you want to know what happens when growth slows earlier. State that question before touching the inputs.

Keep the household's spending, dates, contributions and accounts unchanged. Then compare a supported slower path. Read one early year and one later year so you can see whether the path actually represents what you intended.

A flat annual return, a declining schedule and a power-law path can produce similar averages while describing different years. The label is less important than the sequence it creates for the money you intend to spend.

Expected growth is also different from uncertainty around it. A model's volatility, correlations and distribution assumptions affect the range and sequence of outcomes. Don't reduce uncertainty simply to make a desired retirement date pass. Use the current methodology to understand which controls are available and what they change.

Now inspect the consequence. Does the slower path create an early funding gap, a larger later withdrawal, or a different taxable account balance? That tells you which household decision is sensitive to the assumption.

For example, more money available before work stops may address an early shortfall. Extending the horizon might expose a later one. Those are different problems; neither is solved by editing several unrelated inputs until the score recovers.

Holding-specific overrides need the same discipline. A spot Bitcoin fund can track a Bitcoin exposure model while remaining a security for custody and tax. A company associated with Bitcoin has business and financing effects too. A leveraged or distribution-focused fund has a structure that a simple Bitcoin growth override may not represent.

If the engine cannot represent an important feature, label the limitation. Do not make the feature disappear by selecting the return you hoped the security would earn. A separate analysis or a simpler comparison may be more honest than a detailed-looking but inappropriate override.

After the first controlled test, a combined stress can be useful. Lower returns and a later income start may occur together. Name both changes so the comparison is understood as a combined scenario, not evidence of which one caused the result.

Keep a receipt of the inputs and result identity. Without it, you can end up comparing an old baseline with a new scenario and attribute the difference to the wrong setting.

Keep the starting assumptions and the comparison, then note which planning decision changes under the different result. Return to your plan when that question is answered.

### Visual and source notes — not spoken

ExistingAdvancedmodelscope and Foundation methodology retained; no unsupportedcorrelation/fat-tail/replayclaims. Moredepththan1.4: supportableoverride,controlledsensitivity,combinedstressseparate and resultidentity. Actualmethodologyapprovedbuildonly.

### Production notes

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Keep the saved household fixed; display one supported early/later return path, change only the intended assumption, read the first changed funding year and return to Current. Narration: “This is the one belief we are testing. These household choices stayed the same. Which decision becomes harder under this path?” Show actual methodology/resultidentity; no syntheticvolatilityorproviderprobability.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Answer one modeling question through a supported controlled comparison and return the affected decision to the core plan.

---

# A3.1 — Plan how to manage a Bitcoin-backed loan

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: TAX_LENDING_REVIEW
Sources: DEBT, BRAIN, PRIMARY, APP
Use when: You have, or are seriously considering, a Bitcoin-backed loan.
After lesson: 3.6
Complete before: Complete before borrowing or relying on a collateral-response plan.
Return to: W03 chapters 5–6, then lesson 4.1

### Read aloud

A low starting loan-to-value ratio can stop describing the loan you actually have. Interest accumulates, collateral changes, and the lender's agreement still governs what happens.

Have the loan agreement ready. We'll put its balance, dates, and response rules on one sheet so you know what to monitor and what to do.

Read the full balance, not just the original principal. Record interest treatment, fees, maturity, collateral quantity, price source and the actual warning, collateral-call and liquidation provisions. Those are separate contract events. A notice is not a promised grace period unless the agreement actually provides it.

Use the source's simple illustration. A $25,000 loan against $100,000 of collateral starts at 25% LTV. If 12% interest is added for one year using a simplified annual calculation, the debt becomes $28,000.

Now suppose the collateral is worth $50,000. LTV is $28,000 divided by $50,000, or 56%. The original 25% is no longer the relevant number.

With a purely hypothetical 80% liquidation line, $28,000 of debt reaches that line at $35,000 of collateral. That is a 65% decline from the original $100,000 value, before further interest or fees. Actual accrual and contract terms can change the result.

Next, choose a personal review point before the event you're trying to avoid. Don't call the review point safe; explain what action it initiates.

For an arithmetic example, suppose you were considering returning this $28,000 loan and $50,000 collateral position to 50% LTV. Repaying $3,000 would leave $25,000 against $50,000. Adding $6,000 of eligible collateral would leave $28,000 against $56,000. Both reach 50% in that simplified instant.

They are not the same household decision. Repayment uses cash and reduces debt. Adding collateral leaves the debt and puts more assets into the lending arrangement. The response needs money or eligible collateral actually available, and the ratio could move again before the action completes.

Write the limit on further collateral separately. Protecting one loan should not automatically expose the entire Bitcoin position. If that limit is reached, identify the alternative response before the crisis.

Then test the principal exit. If repayment depends on refinancing, what happens when a new loan is unavailable? If it depends on a sale, include the timing, price and tax uncertainty. A long flat market can be difficult even without an immediate liquidation event.

Add the operational failure case too. A provider interruption can affect access even when LTV is low. Confirm the actual rights, custody structure and available response; the simulation doesn't supply a counterparty guarantee.

Finally, name the person monitoring the sheet and the backup person who knows the first steps. Keep secrets out of it. The sheet should point to verified contacts and safe instructions, not contain private keys or complete recovery material.

Review the actual contract and tax treatment before borrowing or changing collateral. Check that the sheet includes the full balance, relevant dates and thresholds, and the cash or collateral for each response. The lender's rights still depend on the agreement; the sheet doesn't guarantee time to act.

### Visual and source notes — not spoken

Preserve25k×1.12=28k,28/50=56%,28/.8=35kand65%decline. Newresponsecomparisonrepay3k=>25/50=50%;add6k=>28/56=50%;personalratioillustrationnotrecommendedtrigger. Contractaccrual,fees,warning/call/liquidationanddiscretionmustbeverified. NoReedloanintroduced.

### Production notes

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

On a separate labeled operating sheet reveal25k→28k,50kcollateral,56%LTV;compare3krepayment versus6kcollateraladdition;theninspectactualreviewedcontractdatesandexit. Narration: “Both responses change the ratio, but one spends cash and the other exposes more collateral. Which resource is available without taking money from the bills?” Noapplicationorcollateralmovement.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Complete the contract-derived operating sheet with actual full balance, thresholds, exit, funded responses and exposure limits.

---

# A3.2 — Compare financing terms that a simple payment hides

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: LENDING_REVIEW
Sources: DEBT, OWNER, PRIMARY
Use when: A financing option includes a balloon, changing payment phases, shared appreciation, or another unusual contract term.
After lesson: 3.5
Complete before: Complete before choosing that financing or relying on its modeled cost.
Return to: W03 chapter 4, then lesson 3.6

### Read aloud

Two offers can have similar starting payments and very different final obligations. This lesson is for a financing proposal with terms a simple monthly-payment comparison does not capture.

Put the purchase price, cash needed and date at the top. Keep those the same across alternatives. Then build the schedule from closing through the exit.

Record cash paid upfront, fees, interest rate and resets, each payment phase, principal remaining, and any final balloon or contingent settlement. The last row is not optional. It is where some of the most important cost can be hiding.

The earlier interest-only example makes the point. Paying interest on $20,000 for five years leaves the $20,000 principal outstanding. If the planned exit is another loan, add the case where refinancing is declined. The payment schedule hasn't become workable until the household has an acceptable response.

For a cash-out refinance, compare the entire replacement mortgage. A household might want a relatively small amount of new cash but have to reprice a much larger existing balance. Compare that with keeping the old mortgage and financing only the new need separately.

A seller-financed purchase may use a low starting payment and a large balance due later. Read the security interest, guarantees, restrictions and default remedies. For a business purchase, compare the debt service with cash after payroll, operating needs, maintenance and taxes—not with sales alone.

A home-equity investment or shared-appreciation agreement needs its actual settlement formula. It is not a zero-rate loan just because no monthly interest payment appears. Calculate what would be owed under lower, unchanged and higher home values at the relevant dates. Include valuation adjustments, fees, sale or refinancing triggers and other conditions from the contract.

Then ask where the settlement money comes from. A favorable-looking paper gain doesn't provide cash unless a sale or another funded route is available. The agreement may influence when you can move or refinance, which belongs in the life comparison.

Securities-backed credit adds a use restriction check. A non-purpose line generally cannot fund purchases or trading of securities; a margin loan is a different arrangement. Neither should be substituted for the other simply because both use an investment account as collateral.

Retirement-plan loans add employment and plan-rule consequences. Read what happens if the job ends or payments fail, and how repayment affects other saving. Interest returning to the plan doesn't make the lost flexibility and investment exposure irrelevant.

For the Reeds' project illustration, keep a smaller project and a delay alongside financing. The current Reserve and extra-card plan already uses the available cash. Unless a new source or a changed commitment is identified, another payment is not funded. Leaving the project unchosen is a reasoned outcome—not a failed financing exercise.

When a term isn't supported in Orange Plan, keep the actual schedule in the existing reviewed comparison worksheet. Don't replace it with a conventional loan and describe the whole agreement as modeled. Read the unsupported obligation alongside any app result before drawing a conclusion.

Read the comparison from the first payment through the final settlement. What do you pay, what remains owed, and how does the household fund it? Get any missing contract answer before choosing the offer.

### Visual and source notes — not spoken

Existingadvancedcontractscope;nowfullschedule/exit/refinancingrefusal isjobnotrepeatingCoremenu. HELOC/HEI/SBLOC/planloan mechanism references remaininprimarysourceindex; actuallegalagreementcontrol. No unsupportedapp modeling or producthierarchy.

### Production notes

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Build one reviewed offer from closing to finalsettlement,comparekeepingexistingfinance,andshowrefinanceunavailable. Narration: “The small payment ends here. This is what is still owed. Show the source that pays it.” Unsupportedterms useexistingexternalworksheetnotfakefields.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Explain all payment phases and final settlement under a weaker case before choosing the complex financing proposal.

---

# A4.1 — Check price context before a large allocation change

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: OWNER_REVIEW
Sources: ALLOCATION, BRAIN, CLIENT_THEMES
Use when: You are about to make a large investment purchase, sale, or allocation change and need to choose its timing.
After lesson: 4.7
Complete before: Complete before the large transaction; routine funded contributions do not need this detour.
Return to: W04 chapters 7–8, then lesson 5.1

### Read aloud

A large price move can make an investment decision feel urgent even when your financial situation hasn't changed. Before a large purchase or sale, separate the purpose of the transaction from the feeling created by the chart.

Is the purchase part of the target you already chose? Is the cash genuinely available for long-term investing? Is the sale funding a bill with a deadline? Those facts matter before the price opinion.

You may compare investing a lump sum with buying in stages. Staging changes the timing of exposure; it doesn't guarantee a better purchase price.

Here is a deliberately simple example with no fees. A household has $20,000 earmarked for Bitcoin. At a hypothetical price of $100,000, investing all of it buys 0.2 Bitcoin.

Instead, it could invest $10,000 now and keep $10,000 for later. If the later price were $50,000, those purchases would total 0.3 Bitcoin. If the later price were $200,000, they would total 0.15 Bitcoin.

The staged method helps in the falling-price example and buys less in the rising-price example. We haven't assigned probabilities or found a perfect entry rule. We've exposed the trade-off in waiting with part of the money.

Someone may choose staging because it makes a large change easier to maintain. Another may choose the lump sum because the allocation and purpose are settled and they prefer immediate exposure. The process should fit the person's decision, not claim timing skill the example doesn't establish.

A recurring contribution already funded by ordinary cash flow doesn't need a new market thesis every payday. This check is for a large change, not a reason to turn routine saving into daily hesitation.

A sale has its own constraint. A committed payment next month may need dependable funding even when you expect Bitcoin to rise. A flexible expense has a different decision window. Don't give money with a fixed bill the same freedom as uncommitted long-term investments.

Market indicators and valuation models can provide context. Record what the indicator measures, its date and its limits. A relationship can change, and a signal can remain extreme much longer than expected. It cannot tell you the exact day the market turns.

For the Reeds, a better-looking entry does not create cash on top of the Reserve and extra-card claims. A loan to enlarge the purchase is another decision, with its own repayment and downside—not a small adjustment to timing.

Write down the amount you can afford, the reason for the purchase or sale, and the pace you've chosen. Also note what would change that decision—a new cash need or a revised allocation, for example.

Once the large transaction is settled, return to the ordinary contribution plan. You don't need to repeat this price review every payday.

### Visual and source notes — not spoken

Newgeneric20k allocationtimingmechanics:100kprice lump=.2BTC;halfnow+half50k=.3;halfnow+half200k=.15. Nofees,marketprobabilities,currentpriceorperformanceclaim. Sourcecontext notliveprediction. Clarifyordinaryrecurringcontributionsdonotrequireconstantindicatorchecks.

### Production notes

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Use separate no-fee20k/100kgraphic and two laterprices50k/200k;tieproposedpacebacktoactualcashpurpose. Narration: “Waiting buys more in this path and less in the other. The decision is which timing exposure you are choosing, not a guaranteed better entry.” Noactualtradeorforecast.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Choose a deliberate affordable implementation pace, knowing both directions of the timing trade-off and the fact that would change the plan.

---

# A5.1 — Build a multi-year conversion comparison

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: TAX_REVIEW
Sources: TAX, RETIREMENT, PRIMARY, APP
Use when: You are considering Roth conversions across several years.
After lesson: 5.4
Complete before: Complete before relying on a multi-year conversion schedule.
Return to: W05 chapter 4, then lesson 5.5

### Read aloud

A conversion can make sense this year and be too expensive next year. A multi-year strategy needs to use the actual income windows rather than repeat the same amount until the end of the chart.

Start with the unchanged plan. Mark employment income, healthcare coverage, benefits, required distributions and the resources funding the early years. Then choose a limited schedule to compare.

The core lesson explained conversion tax and its funding source. Here we will look at increments and changing years.

For a separate illustrative tax calculation, suppose converting the first $20,000 adds $4,000 of current cost. Converting another $20,000 adds $6,000 more. The first portion costs 20%; the second costs 30%. Together, a $40,000 conversion costs $10,000, or 25% on average.

Looking only at that average hides the decision about the second portion. If the household's comparable future tax cost is expected to be 25% under the simplified assumptions, the first portion has a different trade-off from the second. This is an example of incremental reasoning, not a real tax calculation or a prediction of future brackets.

Now add the next year. If employment resumes or a pension starts, the conversion window may shrink. A larger amount now could deserve another comparison. If a lower-income year is approaching, waiting may be more useful. The schedule follows those circumstances.

For each version, keep the same lifestyle and market assumptions. Compare no added conversions, a modest schedule and a larger early schedule. Record the conversion, spending withdrawal and tax-payment source separately each year.

Read the early-access balances as well as later tax. A schedule that consumes the taxable bridge to pay tax can leave the household with more Roth money and less usable cash when it needs it. That is part of the cost, not an unrelated issue.

Then compare after-tax resources at the same dates. Include the return and tax treatment of the money that would otherwise have paid conversion tax. Don't rank strategies only by the size of the final Roth or lifetime tax paid.

Test the assumptions that make the preferred schedule win. What if later tax rates are lower? What if growth is slower or one spouse dies earlier? A surviving household can have a different filing and income picture. If the model doesn't support a relevant effect, analyze it separately rather than infer it from the score.

A market decline may let the same conversion dollars move more units. That can be useful, but it doesn't pay the tax or guarantee recovery. The current cash source and the longer-term reason still need to work.

Before execution in each actual year, verify income, deductible and nondeductible amounts, required distributions, healthcare effects and the custodian process. The proposal is a review range and rule, not a permanent promise to convert an unchanged amount for ten years.

Choose the schedule you prefer and record the assumptions that make it worthwhile. Before the next conversion, update the current-year figures and confirm the actual amount. Include the tax payment in the same cash-flow plan as spending.

### Visual and source notes — not spoken

Newillustrativeincremental-cost values20k/4kandnext20k/6k=>40k/10k25%average;future25%assumptionisnotforecastorReedtaxrate. Comparecurrentmarginalincrement,liquidityandfutureaftertaxresources. No scheduleexecuted orfixedannualconversionguarantee.

### Production notes

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Show genericincremental-cost table separately,thencompareactualreviewedno/modest/larger conversionscheduleswithsame spending. Narration: “The next part costs more than the first. Read the cash used now and the later after-tax resources before choosing how much.” No fabricatedtaxorhealthoutputs.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Select a bounded conversion schedule with after-tax and liquidity justification and a current-year review rule.

---

# A5.2 — Prepare a harvesting transaction that matches the tax record

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: TAX_REVIEW
Sources: TAX, PRIMARY, APP
Use when: You intend to harvest a gain or loss through a specific sale.
After lesson: 5.5
Complete before: Complete before executing the harvesting transaction.
Return to: W05 chapters 5–6, then lesson 6.1

### Read aloud

A tax-harvesting comparison is not ready for execution just because a spreadsheet found the smallest gain. The units must exist, the selection must be valid, and the resulting record must match what actually happened.

Use this lesson when you have a specific candidate sale. Begin with the account or wallet, quantity, supported basis, holding period and intended exposure afterward.

The course's three-lot example produces $8,400, $16,800 or $9,600 of gain from the same $20,000 sale. Those are alternatives only to the extent the relevant units can actually be identified and sold under the applicable rules.

Suppose the lowest-gain row depends on a missing purchase confirmation. Don't choose it and hope the record appears later. Resolve the evidence or compare an alternative whose basis and identification can be supported.

Now prepare the identification before the required deadline. The actual asset, location, custodian and transaction year determine the rules. Broker-held digital assets and an unhosted wallet can have different procedures. Temporary relief in a particular year is not permanent permission to reconstruct any preferred lot choice after the sale.

A planning app's selection is not automatically an instruction received by a broker or a legally adequate record. Keep the evidence of the actual instruction or contemporaneous identification required for the transaction.

For a loss harvest, check the replacement exposure before placing the sale. Automatic purchases, reinvestment, another account and a spouse's relevant activity can affect a securities wash-sale analysis. Don't assume a Bitcoin fund and directly held Bitcoin have identical treatment. Obtain current review of the actual transaction rather than repeat an old crypto-tax shortcut.

For a gain harvest, update the rest of the year's income. A conversion or business-income change can consume the same favorable room. Federal gain treatment alone doesn't establish the full state, healthcare or other income-sensitive cost.

Before the sale, complete the review and required identification. Afterward, keep the confirmation and reconcile the units, proceeds, and remaining holdings. If you first move coins between your own wallets, keep their purchase history attached; the transfer is not a new purchase.

After the trade, match the actual units, time, proceeds, fees and selected history with the confirmation. Verify the remaining lots and current holding quantity. A tax report should explain the position left over, not just the realized result.

Keep a small transaction packet with the source evidence and reason for the decision. It supports the professional review and reporting. An export labeled tax data is not a filed return, and it doesn't establish that every classification was correct.

Proceed only when the units, tax treatment, and instructions are supported. You may decide the benefit isn't worth the costs or remaining uncertainty. Record that decision rather than leave the trade waiting without a reason.

### Visual and source notes — not spoken

DatedIRS Notice2026-20 reliefchecked forbrokerheldunits2026onlyeligiblecontemporaneousrecords; usermaterialframestransactionsequence. No after-factdropdownassurance;wash-saleanalysisasset/account/yearspecific. PreserveForm8949dataexport≠filedform,privateevidenceandremaininglotcontinuity.

### Production notes

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Prepareonefictionallotcasewithtimelyidentificationevidenceandoneunknownrecord;readreplacementconditionsandpost-traderemaininglots usingclearlystagedrecord. Narration: “This row is an available choice only when the units and the identification process are supported.” Noactualexecution.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Prepare an eligible transaction packet with timely identification, replacement review and post-execution reconciliation—or deliberately pass.

---

# A5.3 — Compare the full cost of moving states

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: TAX_ESTATE_REVIEW
Sources: TAX, ESTATE, PRIMARY
Use when: A possible state move could affect your spending or the tax on a planned sale or withdrawal.
After lesson: 5.3
Complete before: Complete before relying on the move’s tax treatment; residency still needs professional review.
Return to: W05 chapter 3, then lesson 5.4

### Read aloud

A lower-tax state can make a large sale look much cheaper. But the move changes more than the tax line, and changing an address in the app does not establish legal residency.

Use this lesson when moving is a real household possibility, not merely a way to improve a projection.

Start with where you would actually be willing to live and why. Work, family support, schools, healthcare, housing and community belong in that decision. Then compare the full recurring costs and the one-time move.

A simple example shows why. Suppose a hypothetical move saves $10,000 a year in one tax category but adds $8,000 in housing and insurance. The recurring cash improvement is $2,000 before other differences. If moving costs $20,000, that cost needs to be included too. These invented figures illustrate a complete comparison, not any state's rates or a relocation recommendation.

The move may still be worthwhile for the life it provides. Or the tax advantage may be much less important after the other costs are counted. The useful answer is a household decision, not the lowest rate on a map.

A large Bitcoin sale near the move adds a separate legal and tax question. Domicile, time spent, work, homes, family ties and state-source income can matter under the jurisdictions' actual rules. Updating a driver's license or brokerage address may be evidence, but no single checkbox automatically settles every state's claim.

Before relying on the tax result, have a professional familiar with both states review the real timeline and sources of income. Business income, rent, deferred compensation or other items may remain connected to the former state. Do not move a sale date in the records or claim a residency that the facts do not support.

The financial scenario should include the expected effective date and all material cost changes. Keep the current location in the saved starting plan while the move is only a possibility. Once chosen, expected life events can reflect it without presenting that app entry as a legal determination.

Review the other arrangements affected by the move. Estate documents, healthcare directives, insurance, business registrations and provider services may need attention. A lower income tax does not compensate for a coverage gap or a legal document no longer suited to the household.

Let's compare the household's costs before and after the move, including the moving expense. Then identify the sale or withdrawal whose tax treatment depends on residency and take that timing question to a professional familiar with both states.

Decide whether the move fits the life you want as well as the costs. Keep any residency or income-source question unresolved until the relevant facts have been reviewed.

### Visual and source notes — not spoken

Newgeneric10ktaxsaving−8kothercost=2krecurring;20kmovecostnotguaranteedbreakeven. Noactualstatepairresearchedorclaimed. Jurisdictionfactsandprofessionalreviewprecedereliance. Nochangeofaddressshortcuts.

### Production notes

**Moved out of narration in the language pass:** The following source wording records production/evidence limits, not instructions to read to members. Its substantive limits remain in force.

In the demonstration, compare current and proposed household cash flow, include moving costs, then isolate the transaction-specific residency question. Use actual current jurisdictional research only when the locations are known. There is no reason to invent a state-specific threshold for a generic example.

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Separate genericcostillustrationfromrealstateproposal;showrecurringcosts,movedateandtwojurisdictionquestions. Narration: “This is the financial comparison. The legal residency conclusion needs the real facts reviewed separately.” Noresidencyassertionorfilingchange.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Compare complete household costs and life effects, then obtain specific two-jurisdiction residency/source-income review before relying on transaction timing.

---

# A6.1 — Compare healthcare and tax decisions in the same year

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: HEALTH_TAX_REVIEW
Sources: RETIREMENT, TAX, PRIMARY, OWNER
Use when: A withdrawal, gain, or conversion could change the cost or eligibility of healthcare coverage.
After lesson: 6.3
Complete before: Complete before adopting the affected income and coverage plan.
Return to: W06 chapter 3, then lesson 6.4

### Read aloud

A conversion can look inexpensive on the income-tax line and still make healthcare more expensive. Before using an income window, compare the two together.

This lesson is for a year when coverage or premiums depend on the household's income. We already chose a coverage direction in Retirement Income. Now we are testing whether a proposed withdrawal or conversion changes its cost.

Start with the same household, coverage dates and spending in both versions. List income, taxable withdrawals, realized gains and the proposed conversion. Then use the program's actual income definition. It may differ from the income number you usually recognize on the tax return.

For a taxable sale, the whole cash amount is not necessarily income. Basis and gain matter. A fully taxable Traditional withdrawal can add much more income than a sale providing similar spending cash. Qualified Roth treatment and cash already held are different again.

Here is a separate illustration of the combined-cost calculation. Suppose a $10,000 conversion adds $2,000 of income tax. On its own, that looks like a 20% cost.

Now suppose the same conversion increases the household's net coverage cost by $1,500 under the applicable program calculation. The immediate combined cost is $3,500, or 35% of the amount converted.

Those are hypothetical amounts to show the calculation, not a subsidy estimate or tax bracket. Compare the combined cost before deciding whether to convert. A smaller amount may change the result; a larger one needs a reason worth its added cost.

For Marketplace coverage, verify the current year's eligibility and assistance rules, household size, coverage options and income estimate. Update the estimate when actual circumstances change and understand how advance assistance will be reconciled. Do not assume last year's rules continue unchanged.

For Medicare, identify the year whose income affects the premium and the year when that premium is paid. This is not the same calculation or timing as Marketplace assistance. A transaction now can affect a later bill, subject to the current rules and any available reconsideration process.

In a couple, the two people may have different coverage during the same year. One may be on Medicare while the other uses a Marketplace or employer plan. Review both effects instead of assigning the entire household one coverage switch.

HSA contributions need a separate eligibility check. The coverage, other insurance and Medicare enrollment can matter. A lower premium or high deductible alone does not establish eligibility, and enrollment timing can affect whether a contribution is permitted.

Then follow the cash. Where will the additional tax and premium cost come from? If the preferred conversion consumes money needed for early retirement or medical out-of-pocket costs, include that consequence. A higher future Roth balance doesn't make the immediate shortfall disappear.

Use the app only for effects it actually calculates. A verified outside coverage calculation may need to sit beside the model result. Label it clearly rather than assume an unmodeled subsidy remained unchanged.

Choose the coverage and the withdrawal or conversion together, using their combined cost. Confirm the enrollment, eligibility, and tax details before giving up coverage or making the transaction. Enter the same income and costs in the retirement plan.

### Visual and source notes — not spoken

Core healthcare and tax mechanisms are assumed understood; this advanced lesson completes the combined-cost comparison. The $10,000 conversion, $2,000 tax and $1,500 coverage increase are new illustrative inputs, not current subsidy thresholds or a Reed result. Combined $3,500 / $10,000 = 35%. Marketplace annual income, Medicare lookback, individual coverage dates and HSA eligibility require current verification; external calculations must be labeled.

### Production notes

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Place the generic $2,000 tax and $1,500 coverage change beside the $10,000 conversion on a separate graphic. Then compare an actual reviewed household year with current coverage and income rules. Narration: “The tax line is only part of the cost. Add the change in what this household pays for coverage, then decide whether the conversion still serves its purpose.” Keep external coverage results labeled; no invented quotes.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Choose a coordinated income/coverage proposal using the complete current cost and verify the actual enrollment and tax prerequisites.

---

# A6.2 — Test a multi-year sell-versus-borrow strategy

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: TAX_LENDING_REVIEW
Sources: RETIREMENT, DEBT, APP, PRIMARY
Use when: You are considering borrowing in more than one year to fund retirement spending.
After lesson: 6.6
Complete before: Complete before relying on recurring borrowing, not after the first loan.
Return to: W06 chapter 6, then lesson 6.7

### Read aloud

Borrowing once for a temporary need is different from borrowing every year to fund retirement. A recurring strategy has to carry the earlier loans while adding the next year's spending.

This lesson follows that accumulation through the difficult period and the exit. It doesn't stop when the first loan lets you avoid a sale.

Hold the spending need, starting assets and market assumptions constant. Compare the current sale-based policy with the proposed borrowing policy. For each year, read cash delivered, fees, interest paid or added, ending debt, collateral and the source of eventual repayment.

A simple example shows why the debt path matters. Suppose a household borrows $20,000 at the beginning of year one and adds 10% interest at the end. It owes $22,000.

At the start of year two, it borrows another $20,000 for that year's spending. The balance becomes $42,000 before interest. Adding another 10% leaves $46,200 owed at year-end.

The two years provided $40,000 of spending and created $6,200 of interest in this simplified example. Actual contracts accrue differently, and fees or changing rates can add other costs. But even with unchanged annual spending, the obligation grew faster than the new cash received.

Bitcoin might appreciate enough to support that strategy under the chosen assumptions. It might not. Compare a long flat period, an early decline and a higher interest path, not just a strong ending price.

At each difficult year, ask whether the household could continue. Does the lender require more collateral? How much of the Bitcoin is now pledged? Is there cash to respond without taking money from essential bills? Could the agreement end before the assumed market recovery?

The repayment source needs a date and an amount. Selling later, using another account, paying from income or refinancing are different plans. Refinancing is not guaranteed by the fact that the first loan was approved.

A hybrid policy can combine sales and borrowing. For example, the household might sell a limited amount under a reviewed tax strategy and borrow for a remainder. Explain the actual sale, gain, tax and residual cash need. A policy name does not establish that every year's bill has been funded.

Compare after-tax resources at matching dates. Borrowing preserves more assets initially but also leaves a liability. A sale reduces assets but avoids the new interest and collateral exposure. Looking only at Bitcoin retained or total gross assets can favor the wrong version of the household's position.

Estate assumptions deserve particular care. Debt does not disappear because the plan ends at death. Basis treatment, estate obligations, beneficiary rules, legal ownership and settlement liquidity need review for the actual jurisdiction and assets. Don't build the result on a slogan about never selling or avoiding every tax.

Provider failure and interrupted access may not be represented in the simulation. Record those limits separately. A favorable chance-of-success output is not a probability that a lender will remain solvent or honor a hoped-for extension.

Keep a borrowing proposal separate until you choose it. Alex and Morgan do not already have a Bitcoin-backed loan, so we are testing a possible strategy rather than reading an existing obligation.

Choose the funding approach after reading the debt, collateral, and repayment path. Write down when you would stop adding debt or reduce it. You may decide recurring borrowing asks more of the household than you are willing to carry.

### Visual and source notes — not spoken

Existing recurring-retirement-borrowing scope. New generic beginning-of-year loans of $20,000 with end-of-year simple 10% capitalization: year 1 $22,000; year 2 ($22,000+$20,000)*1.10=$46,200; total spending $40,000 and interest $6,200. This is not a lender rate quote, actual accrual method or adopted Reed loan. Preserve supported D63 behavior, contract risks, same net spending and after-tax comparison; no estate-tax guarantee.

### Production notes

**Moved out of narration in the language pass:** The following source wording records production/evidence limits, not instructions to read to members. Its substantive limits remain in force.

For the Reeds, this remains a comparison unless a borrowing policy is deliberately adopted. Their source does not contain a Bitcoin-backed loan. A modeled policy and an executed loan record are not the same thing.

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Show the two-year $20,000 borrowing illustration separately from the app, then inspect a supported actual policy after a weak market and at repayment. Narration: “This year starts with last year's debt still outstanding. Add the next spending need and follow both the interest and the collateral before judging the ending wealth.” No loan application or claim that a lender remains available.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Explain the multi-year debt and collateral path, exit and after-tax trade-off, with a defined rule for stopping or reducing new borrowing.

---

# A6.3 — Check access to retirement accounts before 59½

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: TAX_REVIEW
Sources: RETIREMENT, TAX, PRIMARY
Use when: Your plan relies on using retirement-account money before 59½.
After lesson: 6.2
Complete before: Complete before counting on the access route or making a rollover that could change it.
Return to: W06 chapter 2, then lesson 6.3

### Read aloud

An early-distribution exception can make retirement money useful before 59½. It can also be misapplied because someone remembers the name of a rule but not which account, person or date it requires.

Before relying on an access route, connect the exact distribution with the rule that permits it.

Start with the funding gap and the account intended to supply it. Then separate three questions: will the plan or custodian allow the withdrawal, is ordinary income tax due, and is an additional early-distribution tax avoided? A yes to one is not automatically a yes to the others.

A Roth IRA is a good example. Distribution ordering distinguishes regular contributions, conversions and earnings. Regular contributions generally come out first. That does not make the full account balance available on the same terms.

Keep records of contributions and conversions, including prior distributions. A conversion's separate five-year additional-tax rule is not the same as the conditions for a qualified Roth distribution. A Roth workplace account has its own rules; don't apply Roth IRA ordering to it by name alone.

The workplace-plan exception commonly called the Rule of 55 generally depends on separating from service during or after the calendar year in which the relevant age is reached, and taking distributions from the qualifying employer plan. It is not an IRA exception merely because the owner is 55. Certain public-safety workers have different provisions.

That makes a rollover a consequential decision. Moving the account to an IRA may change an access route you were about to use. Check the retirement funding before submitting the rollover, not after discovering that the new account has different rules.

A governmental 457(b) arrangement can have different additional-tax treatment too. Amounts rolled in from other types of plans or IRAs can require separate treatment. Identify what the account and the money actually are.

Substantially equal periodic payments—often called SEPP or 72(t) payments—provide another possible route. The calculation method, account balance, age, payment schedule and permitted changes need careful verification. This is not a flexible withdrawal plan that you can casually alter when spending changes.

The required period generally lasts until the later of five years from the first payment or age 59½, subject to applicable exceptions. For an illustration based on exact birthdays, beginning at 54 would run to 59½, which is five and a half years. Beginning at 58 would run to 63, because five years is later than reaching 59½.

Those examples explain duration, not eligibility or an approved withdrawal amount. Exact dates matter. An improper modification can create retroactive additional tax and interest. The allowed method and account setup should be reviewed before the first dependent distribution.

Now ask whether the route fits the household, even if technically available. Can the assets and other resources support the required payments through a weak market? Would the schedule force withdrawals you don't need later? Does it remove flexibility that another funding source would preserve?

For Alex and Morgan, review each spouse separately. Alex's age doesn't unlock Morgan's accounts. First check whether planned saving and taxable resources can fund the early years, then compare a special route only where it materially helps.

Finish a short access record: account, person, expected amount and date, tax treatment, exception relied on, supporting evidence, and actions that could invalidate the plan. Have the relevant tax professional and provider verify it before the rollover or withdrawal.

Confirm that the access route applies to this account, this person, and these dates before relying on the withdrawal. Then return to the retirement timeline and check the years it funds.

### Visual and source notes — not spoken

IRS substantially-equal-periodic-payments page, early-distribution exception chart and 401(k) participant distribution guidance checked September 8, 2026. Age examples assume first payment on the stated birthday only to illustrate duration: 54 to 59.5 = 5.5 years; 58 to 63 = 5 years. Exact dates, permitted method, single-account treatment, modification exceptions and recapture require professional verification. No individualized SEPP payment is calculated. Roth IRA and workplace Roth, contributions/conversions/earnings, plan permission, ordinary tax and additional-tax exceptions remain separate.

### Production notes

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Use one actual fictional bridge interval and the intended account. Read the person, separation/withdrawal dates, source records and rule. Compare a rollover before and after only where its access effect is verified. Narration: “This exception belongs to this account and these circumstances. Moving the money can change the route, so we check before submitting the rollover.” No individual SEPP amount without complete review.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Verify an account- and person-specific access route, dates, evidence and invalidating actions before a dependent rollover or distribution.

---

# A7.1 — Compare passphrase, multisig, and professional support

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: DEVICE_CUSTODY_REVIEW
Sources: CUSTODY, DICTATION, PRIMARY, OWNER
Use when: You are choosing or changing a passphrase, multisig, or professionally supported custody arrangement.
After lesson: 7.1
Complete before: Complete before moving meaningful funds into the new arrangement.
Return to: W07 chapter 1, then lesson 7.2 and its safe recovery work

### Read aloud

You may be considering a passphrase, multisig or professional support because the basic setup leaves something important exposed. Start by naming that exposure. Each option solves a different problem and introduces different responsibilities.

A passphrase changes the wallet derived from the backup material. It can add protection when the backup alone is exposed, provided the passphrase remains separate and secure under a well-designed process. It also adds an exact secret you must preserve.

A wrong passphrase can open a different valid wallet. That is why checking a word list alone is not full proof that the intended passphrase wallet can be recovered. The backup, passphrase and verification of the intended wallet need to work together. A passphrase isn't a second cryptographic signer or a legal approval step.

Multisig requires a specified combination of independent keys. A two-of-three policy can authorize a transaction with two of the three keys. If one is unavailable, the remaining two may provide a recovery path—when the configuration, compatible tools and required information are also available.

Buying three devices does not automatically create that arrangement. Loading the same key onto three devices provides copies of one key, not three independent signers. The distinction matters to the failure you're trying to survive.

Collaborative support can help operate a multisig arrangement while the provider holds only one key. Read exactly what the provider can authorize, what it requires, its fees, and how recovery works without it. A claimed provider-independent path should be demonstrated safely before you depend on it.

Institutional custody assigns more of the operational work to a provider. It may simplify administration or the family's starting process. In exchange, you depend on the contract, legal ownership, withdrawal procedures and the provider itself. Read those terms rather than assume an institution supplies unlimited recourse or insurance.

Let's compare the problems. If theft of one backup is the concern, a correctly maintained passphrase or threshold arrangement may address it differently. If the concern is that the family cannot operate an elaborate process, adding another secret may make the situation worse. Support or simplification may solve the actual problem more directly.

A split can keep direct control over one portion and professional support for another. Choose the portions by what they're for and the consequence of a problem with either method. Each additional arrangement needs maintaining.

Before moving meaningful funds, test the proposed improvement against the named failure. Can the intended wallet be recovered when one key, device or provider is missing? Is the configuration available through the protected process? Does the person responsible know how to start?

Use current official instructions and a separate small-value setup for learning. Its successful recovery proves that setup, not a different funded wallet. Actual arrangements need their own appropriate safe verification.

Keep secret material and sensitive configurations out of ordinary course notes. The comparison should document protection gained, responsibility added, risks retained, cost and the family route—not publish a complete recovery kit.

Choose the arrangement that fits your control and family-access needs, and identify the safe test still required. If the added complexity doesn't solve a meaningful problem, keep the simpler setup.

### Visual and source notes — not spoken

Original custody framework and current passphrase/multisig mechanics, not a wealth-based ladder. Independent keys plus configuration and usable recovery tools are required; duplicating one key is not creating multiple independent signers. Recovery on a practice setup does not certify funded holdings. Current BIP39 and actual vendor/professional procedures control execution. Sensitive descriptors and extended keys are not ordinary public worksheet content.

### Production notes

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Use non-secret architecture diagrams and one named missing component. Show what information and independent keys remain. Narration: “The improvement has to survive the failure we chose. Another copy of the same key solves a different problem from another independent signer.” Any live training test uses separately authorized small-value setup and current instructions.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Choose a custody architecture for a named failure and verify the complete safe recovery path and retained responsibilities.

---

# A7.3 — Check what your custody arrangements share

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: CUSTODY_REVIEW
Sources: CUSTODY, BRAIN, PRIMARY
Use when: Several providers, wallets, people, or recovery routes may share a failure that affects important holdings.
After lesson: 7.4
Complete before: Complete before treating those holdings as independent protection.
Return to: W07 chapter 4, then lesson 8.1

### Read aloud

Having several accounts can feel like diversification, but one shared dependency may still affect all of them. We need to know whether the arrangement is independent where it matters—not just whether it has different logos.

Start with the custody map. For each significant portion, identify the provider, underlying custodian when known, keys or signing policy, recovery channel, location category and responsible person. Keep precise locations and sensitive details in the protected process, not this review copy.

Then remove one dependency at a time. What becomes unavailable if an email account is lost? If a provider stops serving customers? If a location is inaccessible? If the main operator is absent?

Here is a simple example. A household places 30% with provider A and 30% with provider B. Suppose verified documents show both depend on the same underlying custodian. A problem at that custodian can affect 60% of the position, even though there are two provider names.

That 60% is an exposure calculation, not a prediction that all of it will be lost. The actual rights, segregation, recovery and failure determine the consequence. We are identifying how much shares the same dependency.

The remaining 40% might be directly controlled. It is independent of that custodian only if its keys and recovery path really are separate and usable. A label saying self-custody does not prove the household can recover it after the same event.

Authentication is another common link. Two accounts may both rely on one email and phone for recovery. Adding a third account with the same recovery dependence won't solve the problem. A verified independent recovery route may be the better improvement.

Physical storage can create a similar concentration. A device, backup and written instructions in one location may all become unavailable together. Separate copies can help with that event, but their security and legitimate family access still need attention.

Test a plausible combination too. A family emergency can remove the normal operator and reduce the available time to solve a technical issue. A local disaster can affect documents, devices and communication. The response must fit that combined circumstance, not only a tidy one-component diagram.

Include lender-held collateral in this picture. A loan might be modest relative to net worth while a large portion of Bitcoin depends on the lender. Don't review that custody exposure only in the borrowing spreadsheet.

Once you find the shared failure, make a targeted change. That may mean separating recovery, reducing a provider exposure, proving a provider-independent signing path, or simplifying a process so a second person can use it.

More accounts aren't the goal. A change earns its place when it reduces the consequence of a named failure without creating an unmaintainable arrangement.

On the custody map, cross out one provider or recovery route and identify what still works. Check the documents and appropriate safe tests before treating the remaining arrangements as independent.

Record the shared failure, the holdings affected, and the change you've chosen. Update the existing custody map and verify the improvement before relying on it.

### Visual and source notes — not spoken

New generic provider allocation 30%+30%=60% shared exposure with 40% direct. Exposure is not loss probability or guaranteed loss. Brand-level independence must be checked against actual custody/recovery arrangements. Public map omits secret locations/configuration; a legitimate independent recovery path needs evidence.

### Production notes

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Highlight the common custodian in two hypothetical 30% allocations; remove it from the map and separately inspect the 40% direct recovery claim. Narration: “There are two provider names, but this failure affects both. We are measuring shared exposure, not predicting a loss.” Verify real independence outside the diagram.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Identify a shared dependency, its affected exposure and a targeted change with evidence of the independent route claimed.

---

# A7.4 — Understand UTXOs before consolidating coins

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: DEVICE_CAPTURE
Sources: CUSTODY, PRIMARY
Use when: You are considering consolidating Bitcoin outputs or selecting outputs manually for a transaction.
After lesson: 7.2
Complete before: Complete before that wallet transaction; it is not a requirement to consolidate.
Return to: Finish the relevant safe wallet work, then lesson 7.3

### Read aloud

Your Bitcoin balance may look like one number, but the wallet can spend it using several separate unspent transaction outputs, usually called UTXOs. Understanding that helps when fees, privacy or many small receipts become a real issue.

You don't need to manage every output by hand for ordinary use. This lesson is for a consolidation or coin-control decision with a specific purpose.

Think of the wallet's spendable balance as separate pieces created by earlier transactions. A new transaction selects pieces as inputs and creates new outputs, including change when appropriate. The fee depends on the transaction's data size and the selected fee rate—not simply how many dollars you are sending.

Virtual bytes are a measure used for that size. Satoshis are small units of Bitcoin. A fee rate in satoshis per virtual byte lets you compare how much the selected transaction would pay.

For an arithmetic example, a preview of 500 virtual bytes at 2 satoshis per virtual byte gives a fee of 1,000 satoshis. At 20 satoshis per virtual byte, that same size costs 10,000 satoshis.

Those are hypothetical fee calculations, not today's rates. The wallet, script type, inputs, and outputs determine the size of your transaction. Read both its size and fee rate in the preview.

Spending many small outputs can require more transaction data than spending fewer larger outputs. Consolidation combines selected outputs into fewer outputs you control. That can reduce the input work needed for a later payment, but you pay a fee now to do it.

Privacy changes too. Combining outputs can reveal a common-control link between histories that were previously separate. Don't consolidate everything by default just because the fee looks low. A future convenience can come with a link you cannot undo on the public transaction record.

Coin control, when supported, lets you choose which outputs to spend. First identify why you are doing that: preparing for a particular payment, reducing future complexity, or keeping sources separate. Then compare the actual preview with the wallet's ordinary selection.

There isn't a permanent dollar or Bitcoin cutoff for useful consolidation. An output's cost to spend depends on the fee environment and transaction type. A quoted dust threshold from a different script or policy isn't a universal minimum for every wallet.

Before transacting, verify the wallet setup and recovery status. Use the correct network and the trusted device process to confirm the destination. A self-transfer still sends real funds and deserves the same address and fee checks as another payment.

Preserve the ownership and purchase history in the records. Moving coins to your own new output does not automatically mean you acquired the Bitcoin again at today's price. Real transaction-fee treatment needs the appropriate supported tax handling rather than an invented balancing purchase.

The demonstration uses a separate small-value setup. It shows the available outputs, actual preview and privacy comparison without publishing sensitive addresses or recovery material. Match the procedure to the exact wallet and software before using it with your own holdings.

Compare the fee paid now, the possible saving on a later payment, and the privacy cost. Consolidate only the outputs that fit your purpose—or leave them alone when a transaction wouldn't improve the situation.

### Visual and source notes — not spoken

Current Trezor coin-control and UTXO documentation and COLDCARD UTXO management support input, fee and privacy mechanisms; no universal dust value carried into narration. New hypothetical 500 vB at 2 or 20 sat/vB gives 1,000 or 10,000 sats. Actual size depends on wallet/script and inputs/outputs. No live fee quote, specific address, real secret, blanket consolidation or tax-basis reset. Device capture remains gated.

### Production notes

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Use an approved practice wallet to inspect actual output selection and fee preview; show the generic multiplication separately. Narration: “This is the fee for this transaction shape. Consolidating may simplify a later payment, but it spends fees now and links these outputs.” No broadcast until explicitly authorized and exact procedure verified; no sensitive identifiers filmed.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Choose a justified consolidation, coin-control action or deliberate pass after reading the actual fee/privacy trade-off and safe procedure.

---

# A8.1 — Decide whether a trust has a job in the plan

Status: SPOKEN_EDIT_REVIEW — line-edited for direct spoken teaching; examples and planning decisions retained. Owner voice approval and filming remain separate.
Adapted source: original source materials and current course decisions recorded in delivery/teaching-revision.md; prior versions remain in Git history.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: conditional
Gate: ESTATE_TAX_REVIEW
Sources: ESTATE, ESTATE_DECK, PRIMARY, OWNER
Use when: A trust may help with a specific family, management, or estate objective.
After lesson: 8.1
Complete before: Complete before choosing or funding the arrangement, with attorney and tax review.
Return to: W08 chapter 1, then lesson 8.2

### Read aloud

Owning Bitcoin doesn't automatically tell you to create a trust. Start with the family or legal problem you want a trust to solve, then compare it with the simpler arrangements already available.

You might need continuing management for a child, support for a vulnerable beneficiary, continuity during incapacity, privacy or coordination across assets. Those are different objectives, and they can call for different structures.

Consider a family that simply needs current beneficiaries, executed baseline documents and a findable custody process. A trust doesn't substitute for those unfinished steps. It must add a useful job.

Now consider a family that wants money managed for a child over many years rather than distributed outright. That continuing management is a specific objective to discuss with the attorney. The distribution terms, trustee and successor process then need to match it.

A revocable living trust can support administration and continuity when properly created and funded. Retaining control generally leaves the assets within the owner's relevant tax and creditor picture. It is not automatically an estate-tax reduction or a creditor shield.

An irrevocable arrangement can change control, access, taxation and beneficiary rights. Those effects can be difficult to undo. Read the consequences before treating loss of control as a minor detail in a tax strategy.

Grantor and non-grantor describe income-tax treatment. They are not synonyms for revocable and irrevocable, or a ranking from basic to advanced. The powers, terms, funding and applicable law determine how the arrangement operates.

Specialized charitable structures, including a charitable lead trust, belong to a household with a real charitable and beneficiary objective. A high expected Bitcoin return is not enough reason to select one. The obligations need testing under less favorable returns, with qualified legal and tax design.

Bitcoin adds an operational question to the drafting. Who can make investment decisions? Who can sign? How are custody, recovery, provider dependence and successor trustees handled? A clause expressing enthusiasm for Bitcoin does not eliminate fiduciary duties or make keys recoverable.

Then finish funding and coordination. Signing a document doesn't automatically retitle accounts, update beneficiaries or move assets under its control. Retirement accounts need particular care; naming a trust or moving assets can have important distribution and tax consequences.

Use the ownership inventory and custody map with the attorney. Identify which accounts belong to the trust, which use a beneficiary process, and which stay outside. Confirm the custodian or provider can actually implement the intended arrangement.

A household's Bitcoin holdings alone don't tell us which trust, if any, it needs. Start with the family objective and review the actual people, assets, and legal circumstances with the attorney.

Decide whether the baseline documents meet the need or a trust adds a specific benefit. If you proceed with a trust, identify who completes the legal work, funds it, and coordinates beneficiaries and custody. Confirm those steps rather than stop at signing the document.

Update the family packet with the resulting authority and starting instructions.

### Visual and source notes — not spoken

Estate framework preserves revocable/irrevocable separately from grantor/non-grantor, trust purpose and actual funding. Charitable lead structures remain specialized professional questions, not return-driven recommendations. State law, beneficiary treatment, tax and provider implementation require actual review. No legal instrument, Bitcoin waiver or guaranteed estate-tax savings is drafted.

### Production notes

**Moved out of narration in the language pass:** The following source wording records production/evidence limits, not instructions to read to members. Its substantive limits remain in force.

For the Reeds, the source doesn't establish a particular trust, estate size requiring a structure, or legal instrument ready to sign. The teaching example organizes the questions. It should not invent a trust recommendation to make the course appear more complete.

The uploaded retirement YouTube script supplies delivery and progression only: a recognized problem, enough explanation, a worked example and an actionable conclusion. Its financial formulas, return assumptions, price table, withdrawal rates and guarantees are not adopted. New connecting wording and generic illustrations are editorial proposals, not prior Austin dictation or client facts. See delivery/teaching-revision.md for original sources, source differences, examples and narrow outside checks.

Exact app controls, inputs, calculations, save behavior and recordings remain subject to the paired walkthrough checks. Professional, device and real learner evidence are separate from this written draft. No course edit executes an account, trade, loan, transfer, legal document or message.

### Demonstration plan — not spoken

Put the existing ownership map beside one family objective and compare baseline documents with a proposed trust job. Narration: “What does this structure add, and which assets would actually come under it? Signing the document and funding it are different steps.” Prepare attorney questions, not legal clauses or transfers.

The demonstration is a prepared instruction, not evidence that the app, device, provider or professional action has occurred. Match the actual input and result before recording.

### Member checkpoint

Resolve the trust purpose with qualified review and identify actual funding, beneficiary, custody and successor actions or a simpler baseline.
