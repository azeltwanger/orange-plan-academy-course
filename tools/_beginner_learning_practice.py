# Temporary literal practice prompts. No fake participant responses or scored user outcomes.
# These live in existing Member checkpoint sections, not a new workbook.
# Fields: problem, task, reasoning check, changed circumstance, application.
PRACTICE = {
'1.5': (
 'You want to stop work at 55. A friend says to enter a higher investment return until the plan approves 55.',
 'Explain what would change in that comparison and what would not. Then choose a real choice worth testing instead.',
 'A higher return changes the assumed future, not the money saved or the life funded today. After checking the facts, a real comparison might change saving, spending or work timing. Keep the other inputs the same first so you can explain the effect. No particular retirement age or confidence result is the required answer.',
 'Suppose the plan already supports your intended life under the assumptions you chose. Do you have to change the plan? No. Keeping it can be a reasoned decision; note what assumption or event you will review.',
 'Use your intended date and spending. State the current answer, one assumption behind it, and either the next comparison or your reason to keep the plan.'),
'2.1': (
 'In a separate practice household, $6,000 reaches checking each month. A $400 workplace retirement contribution already came out of pay before that deposit. Regular spending from checking is $4,500, including required debt payments. A $1,200 annual bill is not included. There are no other costs or transfers in this simplified case.',
 'Use a calculator to find the monthly amount left after allowing for the annual bill. Does the $400 workplace contribution need to come out of the bank deposit again?',
 '$1,200 divided by 12 is $100 a month. $6,000 minus $4,500 minus $100 leaves $1,400. Do not subtract the $400 again: the deposit is after that contribution. The household is already saving that $400. The $1,400 is available for decisions, not permission to assign it several times.',
 'Now a bank review shows that the $4,500 already included the $100 monthly allowance for that annual bill. Remove the duplicate allowance; the remainder is $1,500. Fix what the spending number includes rather than inventing more income.',
 'Trace your actual deposits and costs. Before choosing a new transfer, explain what is already deducted and which irregular bills still need an allowance. A real shortfall or unresolved mismatch stays visible.'),
'3.3': (
 'A practice household has $1,000 a month left after required debt payments and its existing payroll saving. Its current working choice is $300 to the Reserve. Someone proposes another $900 for extra debt payments.',
 'Does that fit? Show the amount available for extra debt if the $300 Reserve contribution stays.',
 '$300 plus $900 is $1,200, which is $200 more than the available $1,000. Keeping $300 for the Reserve leaves $700 for extra debt. That $700 is a budget limit under these facts, not the recommended payment for every household. Required payments were already counted.',
 'The household then chooses $600 for the Reserve because of its income risk and available cash. That leaves $400 for extra debt. Explain the benefit of more cash and the cost of slower debt repayment. Another supported split is acceptable; it needs a household reason and must fit the money available.',
 'Put your intended extra debt payments beside your chosen Reserve contribution. Explain why you prefer that split, then name the event that would make you review it.'),
'4.3': (
 'A separate practice household has $400,000 of financial assets. It wants to test $200,000 in Bitcoin. It has already chosen a $30,000 Reserve and a separate $10,000 purchase next year, both funded from these assets. It expects not to use the remaining money for at least twelve years and wants broad ownership of businesses alongside Bitcoin.',
 'Find the cash amount and the amount left for long-term investments. Explain why broad stock funds are a relevant choice for the remaining job. Do not use the sample course percentages as the reason.',
 '$30,000 plus $10,000 is $40,000 for the stated cash jobs. $400,000 minus $200,000 minus $40,000 leaves $160,000. That gives 50% Bitcoin, 10% cash and 40% remaining. Broad stock funds fit the stated wish for business ownership without picking only a few companies; compare actual holdings, costs and overlap before choosing a fund. Other investments can be reasonable when the purpose or preferences differ. This is not a recommended allocation.',
 'Now the household chooses to have another $60,000 available in cash for separate retirement payments. It keeps the same Bitcoin amount for this comparison. Cash becomes $100,000 and the other long-term money becomes $100,000: 50%, 25% and 25%. It cannot keep the original $160,000 investment and count the same $60,000 as new cash. Explain what keeping more cash gives up. The Bitcoin amount can also be revisited when the total plan does not fit.',
 'Use your own spending jobs and investment preferences. Compare two relevant arrangements and explain why you prefer one. Timeframes are uses of money, not a requirement to open three accounts or use the same mix in every account.'),
'4.7': (
 'You have $300 a month available for a new investment. The money is intended for a work break in three years. A taxable account permits access for that use. You have not verified any early-withdrawal route from your retirement account. A card payment may free another $200 later, but the card is not paid off yet.',
 'Explain what can be planned now, which access question is unresolved, and whether a $500 transfer is affordable today.',
 'Only $300 is currently available. The possible $200 belongs to a later phase. Compare a receiving account with access for the work break; do not treat an unverified retirement-account exception as available funding. This is not a rule that all retirement money is locked up. Verify the particular route before relying on it. Choosing an account also does not choose the investment or complete a purchase.',
 'The work break is canceled and this new saving is now intended for much later retirement. Revisit the account comparison, including eligibility, tax treatment, costs and investment choices. The earlier taxable-account preference need not remain the best choice for the changed job.',
 'For each current contribution, state the source, amount, start condition, receiving account and intended investment. Explain why the account and investment fit the time you need the money. Check a future payment before activating the extra transfer.'),
'5.1': (
 'You are comparing a sale for $8,000. Supported records give the units being sold a $5,000 basis. Ignore fees only for this arithmetic exercise. No tax rate, other income or holding period is supplied.',
 'Find the gain. Can you determine the tax bill from those two numbers alone?',
 '$8,000 minus $5,000 gives a $3,000 gain. It is not a $3,000 tax bill, and the full $8,000 is not all gain. The tax calculation still needs the relevant income, holding period, account treatment and rules. You have completed the gain calculation, not the entire tax decision.',
 'The purchase record is missing instead. Do not set basis to zero to get an answer. Identify the missing history and avoid relying on an unsupported tax cost, while continuing with the facts you do know.',
 'For a sale you are considering, separate proceeds, supported basis, gain, estimated tax and cash left for the intended use. Identify exactly which unknown would change the comparison.'),
'5.4': (
 'Use the lesson’s simplified $30,000 conversion with $6,000 of additional tax paid from separate assets. The comparison without a conversion keeps those separate assets invested. All other assumptions remain as stated in the lesson.',
 'Explain why comparing only the final Roth and Traditional balances is incomplete. Then identify the current money used for tax.',
 'The tax-payment assets have a cost too: the no-conversion version keeps them and their later growth. Compare total after-tax resources and usable early money, not just the bigger Roth account. Equal assumed tax rates in the simplified doubling example produce equal total spendable amounts; that is not a prediction that real strategies always tie.',
 'Now only $4,000 is available for additional tax after other commitments. The assumed $6,000 bill is $2,000 short. A smaller conversion, waiting or another genuinely available source needs comparing. Do not guess a new conversion amount by scaling a real tax bill without recalculating it; marginal rates and other effects can change.',
 'Compare no conversion and a manageable proposed amount using the same life and assumptions. Name the tax source, what using it gives up and what could make a different amount preferable. The correct conclusion can be no conversion.'),
'6.3': (
 'Two imaginary coverage choices have the following ordinary-year estimates. A: $6,000 of premiums plus $4,000 of other costs. B: $4,000 of premiums plus $7,000 of other costs. These are practice numbers, not policy quotes.',
 'Compare the totals. Is the lower-premium choice automatically less expensive or the better coverage?',
 'A totals $10,000; B totals $11,000. The lower premium does not establish the lower complete cost. The totals still do not establish which policy fits: check covered care, network, limits, dates and the household’s difficult-year cash need.',
 'A excludes a medicine the household needs. The earlier ordinary-year estimate no longer settles the comparison. Check the actual uncovered cost and alternatives before selecting coverage. Do not change the estimate to preserve the first answer.',
 'Compare the actual coverage you can obtain and fund. Explain the ordinary-year cost, the important retained risk and the dates when each person’s coverage changes.'),
'6.8': (
 'A separate retirement practice case has $72,000 of annual cash costs, including an assumed complete tax estimate and all required payments. Reliable gross income is $24,000. It has $72,000 of cash assigned only to the remaining spending gap. Hold returns, interest, taxes and other costs fixed for this arithmetic exercise.',
 'Find the annual and monthly gap. How many months would the cash cover at that pace, before any refill? Does the cash remove the need for a longer-term funding plan?',
 'The annual gap is $48,000: $72,000 minus $24,000. That is $4,000 a month. $72,000 divided by $4,000 is eighteen months. The cash is a finite part of the existing assets, not extra wealth and not proof of lifetime funding. State the source and decision for the next refill.',
 'Reliable gross income rises to $36,000, with the stated costs held fixed just for this exercise. The gap becomes $36,000 a year or $3,000 a month, so the same cash covers twenty-four months. In the actual plan, update taxes and other linked costs too. The Reserve’s job depends on the spending gap, not a copied percentage of assets.',
 'Read your next year’s spending, income, investment withdrawals and cash together. Explain the choice, the next review point and a workable response if the planned adjustment cannot cover essential bills.'),
'7.4': (
 'You recovered a small practice wallet successfully. Your long-term Bitcoin is in a different wallet whose backup has not been checked. A helper can find the account list but does not know which recovery process applies.',
 'What has been proved? What is still unfinished? Explain a safe next step without revealing or moving any real secrets or funds.',
 'The test proves the practice setup only. The funded wallet needs its own appropriate, non-destructive-first verification under the official procedure. Its recovery status stays unverified meanwhile. The helper needs the correct safe starting instructions and contact; a plan-data backup is not a wallet backup.',
 'Two backup copies are in the same place. A loss affecting that place can affect both. Compare a manageable way to reduce the shared failure, with security and lawful family access considered together. Do not publish exact locations or recovery material in the exercise.',
 'Use your actual non-secret custody map. Identify the normal operator, backup person, proof that applies to each setup and the first action when the operator is absent. Never perform a destructive wallet test merely to complete this exercise.'),
'8.3': (
 'A family helper knows how to use a Bitcoin wallet, but it has not been established that the helper has authority to use the owner’s assets. The family can find a collection of documents but not a clear first contact.',
 'Explain what the starting letter should help them do. Does technical skill or possession of a login settle legal authority?',
 'The first page should direct the reader to the appropriate authorized person and legitimate provider or technical process. Technical ability and account credentials do not create legal authority. Confirm the role for incapacity separately from the role after death; use the existing documents and professional contact to resolve the specific authority question.',
 'The first contact is unavailable. The packet needs an agreed backup route the family can find, not an instruction to guess passwords or send recovery words to someone offering help.',
 'Ask a consenting person to explain the first steps from your safe instructions. Correct the unclear step. Do not send sensitive files or claim a successful rehearsal until it actually happens.'),
'9.3': (
 'Your checked budget had $500 a month available after bills and existing commitments. Take-home income now falls by $400, and the other costs stay the same. The old $500 investment transfer is still scheduled.',
 'What fact needs updating, how much is now available, and which choice needs review?',
 '$100 is now available. Leaving the $500 transfer unchanged would require another $400 from somewhere. Update the real income, then compare the transfer and other flexible choices. Essential bills and required payments still count. A higher assumed Bitcoin return does not replace this month’s missing cash.',
 'The income change is only a job you are thinking about, not a change that happened. Keep it in a scenario until chosen. Current facts and a proposed response are different. A quiet month with no material change can end with no strategy edit.',
 'Classify one actual change or unexplained number in your own plan. Find its source, make the supported correction or comparison, and explain what it changes downstream.'),
'10.2': (
 'Consider stopping work one year earlier than in your current plan. This is only an idea to compare, not an instruction to retire.',
 'Without copying the Reeds, explain which inputs change, what stays fixed for the first comparison, and where the extra year’s spending would come from.',
 'Change the intended work and income timing for the right person, keep spending and investment assumptions fixed first, and inspect the affected funding years. Additional withdrawals and fewer contributions may change the result. No retirement result can be invented from this prompt. Identify the actual source and any access or tax condition before calling the extra year funded.',
 'Now suppose only one partner reduces work while the other continues. Do not end both incomes. Recheck the household gap and compare the specific choices it affects, not every strategy at once.',
 'Explain one preference in your own plan, the fact that supports it, a realistic alternative and the circumstance that would make you revisit it. Different plans are acceptable. A missing consequential fact is a specific question to resolve—not evidence the plan works.')
}
# The 13 prompts have different purposes. They are not 13 simulated people or measured outcomes.
# They are displayed after the lesson, with reasoning initially hidden in the reading artifact.
WALKTHROUGH_PRACTICE = {
'W01': ('1.5', 'After chapter 9, let the member explain a starting result and choose one comparison without supplying the example\'s settings. Use the 1.5 practice prompt first if the distinction between changing an assumption and changing a household decision is unclear.'),
'W03': ('3.3', 'After chapter 3, have the member fit their own Reserve and extra-debt choices into the same available amount. The 3.3 practice case tests the arithmetic first. Do not grade the choice by whether its split matches the Reeds.'),
'W04': ('4.3', 'After chapter 3, use the changed-facts 4.3 practice case before returning to the member\'s portfolio. Ask what the non-Bitcoin money is for and why the selected investments fit. At chapters 7–8 use the 4.7 exercise to separate current contributions, later money, account access and the actual purchase.'),
'W05': ('5.1', 'Use the 5.1 practice case after the first sale explanation. Before finalizing chapter 4, ask the 5.4 tax-funding question and require the no-conversion resources to remain visible. Professional verification supports the specific transaction; it is not the learner\'s answer to the entire decision.'),
'W06': ('6.8', 'Use the 6.3 cost comparison where coverage is discussed, then the 6.8 spending-gap practice at the annual review. The member must explain the actual source, finite cash and what changes under different income. Use their own figures only after the approved build represents the relevant facts; no exercise number is an engine result.'),
'W07': ('7.4', 'Use the 7.4 no-secrets practice to check that the member distinguishes a practice recovery, actual-wallet proof and a family starting map. The correct next action can be obtaining a safe, scoped check. No wallet operation is authorized by the exercise.'),
'W08': ('8.3', 'Use the 8.3 role-and-contact practice, then a consented tabletop with the member\'s own safe starting instructions. Ask the reader for the first action rather than narrating every step for them. Do not claim authority, delivery or successful comprehension from this written prompt.'),
'W09': ('9.3', 'Use the 9.3 changed-income case to separate current facts, proposed responses and hypothetical events. A different example investment return is not a solution to an actual cash shortfall. Then repeat the decision with the member\'s relevant facts.'),
'W10': ('10.2', 'Use the 10.2 earlier-work-change question as a transfer check. Ask the member to explain how they would begin a new decision, not repeat a remembered allocation or score. Record actual uncertainty; a simulated answer does not certify the member or the plan.')
}
