# Temporary individually authored edits and contextual placements; removed before integration.
EDITS = {
'A1.1': [
("Use this lesson when the normal assumptions", "Use this lesson when you need to test an assumption the normal settings don't express. Start with the question you want the comparison to answer."),
("The solution is a starting model", "Keep the starting assumptions and the comparison, then note which planning decision changes under the different result. Return to your plan when that question is answered.")
],
'A3.1': [
("This lesson turns a specific Bitcoin-loan contract", "Have the loan agreement ready. We'll put its balance, dates, and response rules on one sheet so you know what to monitor and what to do."),
("Before borrowing or changing collateral, verify", "Review the actual contract and tax treatment before borrowing or changing collateral. Check that the sheet includes the full balance, relevant dates and thresholds, and the cash or collateral for each response. The lender's rights still depend on the agreement; the sheet doesn't guarantee time to act.")
],
'A3.2': [
("Finish with a comparison that answers", "Read the comparison from the first payment through the final settlement. What do you pay, what remains owed, and how does the household fund it? Get any missing contract answer before choosing the offer.")
],
'A4.1': [
("Before acting, write the affordable amount,", "Write down the amount you can afford, the reason for the purchase or sale, and the pace you've chosen. Also note what would change that decision—a new cash need or a revised allocation, for example."),
("Return to the ordinary contribution plan", "Once the large transaction is settled, return to the ordinary contribution plan. You don't need to repeat this price review every payday.")
],
'A5.1': [
("Finish with the preferred bounded schedule,", "Choose the schedule you prefer and record the assumptions that make it worthwhile. Before the next conversion, update the current-year figures and confirm the actual amount. Include the tax payment in the same cash-flow plan as spending.")
],
'A5.2': [
("Then work through the operational sequence:", "Before the sale, complete the review and required identification. Afterward, keep the confirmation and reconcile the units, proceeds, and remaining holdings. If you first move coins between your own wallets, keep their purchase history attached; the transfer is not a new purchase."),
("The outcome can be a verified proposed", "Proceed only when the units, tax treatment, and instructions are supported. You may decide the benefit isn't worth the costs or remaining uncertainty. Record that decision rather than leave the trade waiting without a reason.")
],
'A5.3': [
("In the demonstration, compare current and proposed", "Let's compare the household's costs before and after the move, including the moving expense. Then identify the sale or withdrawal whose tax treatment depends on residency and take that timing question to a professional familiar with both states."),
("Finish with the full life-and-cost comparison", "Decide whether the move fits the life you want as well as the costs. Keep any residency or income-source question unresolved until the relevant facts have been reviewed.")
],
'A6.1': [
("Those are invented amounts,", "Those are hypothetical amounts to show the calculation, not a subsidy estimate or tax bracket. Compare the combined cost before deciding whether to convert. A smaller amount may change the result; a larger one needs a reason worth its added cost."),
("Finish with one coordinated choice", "Choose the coverage and the withdrawal or conversion together, using their combined cost. Confirm the enrollment, eligibility, and tax details before giving up coverage or making the transaction. Enter the same income and costs in the retirement plan.")
],
'A6.2': [
("For the Reeds, this remains a comparison", "Keep a borrowing proposal separate until you choose it. Alex and Morgan do not already have a Bitcoin-backed loan, so we are testing a possible strategy rather than reading an existing obligation."),
("Finish with the preferred funding policy,", "Choose the funding approach after reading the debt, collateral, and repayment path. Write down when you would stop adding debt or reduce it. You may decide recurring borrowing asks more of the household than you are willing to carry.")
],
'A6.3': [
("The solution isn't knowing that early-access rules exist.", "Confirm that the access route applies to this account, this person, and these dates before relying on the withdrawal. Then return to the retirement timeline and check the years it funds.")
],
'A7.1': [
("An intentional split can combine direct control", "A split can keep direct control over one portion and professional support for another. Choose the portions by what they're for and the consequence of a problem with either method. Each additional arrangement needs maintaining."),
("Return with the simplest arrangement", "Choose the arrangement that fits your control and family-access needs, and identify the safe test still required. If the added complexity doesn't solve a meaningful problem, keep the simpler setup.")
],
'A7.3': [
("In the demonstration, we'll cross out", "On the custody map, cross out one provider or recovery route and identify what still works. Check the documents and appropriate safe tests before treating the remaining arrangements as independent."),
("Finish with the failure identified,", "Record the shared failure, the holdings affected, and the change you've chosen. Update the existing custody map and verify the improvement before relying on it.")
],
'A7.4': [
("Those are invented previews,", "Those are hypothetical fee calculations, not today's rates. The wallet, script type, inputs, and outputs determine the size of your transaction. Read both its size and fee rate in the preview."),
("The solution may be a selective consolidation,", "Compare the fee paid now, the possible saving on a later payment, and the privacy cost. Consolidate only the outputs that fit your purpose—or leave them alone when a transaction wouldn't improve the situation.")
],
'A8.1': [
("For the Reeds, the source doesn't establish", "A household's Bitcoin holdings alone don't tell us which trust, if any, it needs. Start with the family objective and review the actual people, assets, and legal circumstances with the attorney."),
("The finished decision is either", "Decide whether the baseline documents meet the need or a trust adds a specific benefit. If you proceed with a trust, identify who completes the legal work, funds it, and coordinates beneficiaries and custody. Confirm those steps rather than stop at signing the document."),
("Return to the family packet with the result.", "Update the family packet with the resulting authority and starting instructions.")
]
}
MOVE_TO_NOTES = {'A5.3':['In the demonstration, compare current and proposed'], 'A6.2':['For the Reeds, this remains a comparison'], 'A8.1':['For the Reeds, the source doesn\'t establish']}
# These records become metadata in their canonical lessons, not a second curriculum source.
ROUTES = {
'A1.1': ('1.4', 'You need custom assumptions or a holding-specific model to answer a planning question.', 'Complete before relying on the custom assumption or override.', 'W01 chapter 8, then lesson 1.5'),
'A3.1': ('3.6', 'You have, or are seriously considering, a Bitcoin-backed loan.', 'Complete before borrowing or relying on a collateral-response plan.', 'W03 chapters 5–6, then lesson 4.1'),
'A3.2': ('3.5', 'A financing option includes a balloon, changing payment phases, shared appreciation, or another unusual contract term.', 'Complete before choosing that financing or relying on its modeled cost.', 'W03 chapter 4, then lesson 3.6'),
'A4.1': ('4.7', 'You are about to make a large investment purchase, sale, or allocation change and need to choose its timing.', 'Complete before the large transaction; routine funded contributions do not need this detour.', 'W04 chapters 7–8, then lesson 5.1'),
'A5.1': ('5.4', 'You are considering Roth conversions across several years.', 'Complete before relying on a multi-year conversion schedule.', 'W05 chapter 4, then lesson 5.5'),
'A5.2': ('5.5', 'You intend to harvest a gain or loss through a specific sale.', 'Complete before executing the harvesting transaction.', 'W05 chapters 5–6, then lesson 6.1'),
'A5.3': ('5.3', 'A possible state move could affect your spending or the tax on a planned sale or withdrawal.', 'Complete before relying on the move’s tax treatment; residency still needs professional review.', 'W05 chapter 3, then lesson 5.4'),
'A6.1': ('6.3', 'A withdrawal, gain, or conversion could change the cost or eligibility of healthcare coverage.', 'Complete before adopting the affected income and coverage plan.', 'W06 chapter 3, then lesson 6.4'),
'A6.2': ('6.6', 'You are considering borrowing in more than one year to fund retirement spending.', 'Complete before relying on recurring borrowing, not after the first loan.', 'W06 chapter 6, then lesson 6.7'),
'A6.3': ('6.2', 'Your plan relies on using retirement-account money before 59½.', 'Complete before counting on the access route or making a rollover that could change it.', 'W06 chapter 2, then lesson 6.3'),
'A7.1': ('7.1', 'You are choosing or changing a passphrase, multisig, or professionally supported custody arrangement.', 'Complete before moving meaningful funds into the new arrangement.', 'W07 chapter 1, then lesson 7.2 and its safe recovery work'),
'A7.3': ('7.4', 'Several providers, wallets, people, or recovery routes may share a failure that affects important holdings.', 'Complete before treating those holdings as independent protection.', 'W07 chapter 4, then lesson 8.1'),
'A7.4': ('7.2', 'You are considering consolidating Bitcoin outputs or selecting outputs manually for a transaction.', 'Complete before that wallet transaction; it is not a requirement to consolidate.', 'Finish the relevant safe wallet work, then lesson 7.3'),
'A8.1': ('8.1', 'A trust may help with a specific family, management, or estate objective.', 'Complete before choosing or funding the arrangement, with attorney and tax review.', 'W08 chapter 1, then lesson 8.2')
}
