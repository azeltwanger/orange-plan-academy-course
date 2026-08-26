from __future__ import annotations

from textwrap import dedent


def b(text: str) -> str:
    return dedent(text).strip() + "\n"


FILES = {
"scripts/05-1_cost-basis-what-you-paid-and-how-to-reco.md": b(r'''
TELEPROMPTER SCRIPT — segment 5.1
5.1 Cost basis: what you paid, and how to reconstruct it
~7 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to cover cost basis, which is the record that makes every other tax decision in this module usable.

Quick note before we start: this module is US-specific. The framework still helps outside the US, but the rules and reporting do not travel with it.

== WHAT COST BASIS IS ==

Cost basis is generally what you paid to acquire an asset, adjusted for the costs and events that the tax rules tell you to include.

For a Bitcoin purchase, that normally means the dollars you paid for the Bitcoin plus acquisition costs that belong in basis. Your gain or loss is measured from the amount you receive when you dispose of it, after the adjustments that apply, minus the basis of the units you disposed of.

The important part is that basis is tracked by units or lots. One purchase on one date can have a completely different basis and holding period from another purchase.

== SAME SALE, TWO DIFFERENT TAX BILLS ==

Let's run it on the couple.

They hold 1.75 Bitcoin worth an illustrative $175,000. They acquired it in two lots.

Lot one is 1.5 Bitcoin with a total basis of $45,000, or $30,000 per coin.

Lot two is a quarter Bitcoin with a $15,000 basis, or $60,000 per coin.

Now they sell a quarter Bitcoin for $25,000.

If the identified units come from lot one, the basis is $7,500 and the gain is $17,500.

If the identified units come from lot two, the basis is $15,000 and the gain is $10,000.

Same sale proceeds. Different identified units. Different gain.

That is why "I own 1.75 Bitcoin" is not enough information for a tax plan.

== SPECIFIC IDENTIFICATION IS A RECORD, NOT A RETROSPECTIVE CHOICE ==

For Bitcoin in self-custody, current IRS guidance lets you specifically identify the units you are disposing of when two things are true.

First, no later than the date and time of the transaction, your books and records identify the particular units using enough information to distinguish them, such as acquisition date and time or acquisition price.

Second, you keep records that establish those identified units were actually removed from that wallet.

For Bitcoin held by a broker, the broker decides which identifiers it can accept. After 2025, the instruction generally has to reach the broker no later than the transaction, and you keep your own substantiation.

So HIFO, FIFO, or any other lot rule is not a button you invent after the year is over. It is a documented instruction that has to satisfy the rule for the wallet or account involved.

If specific identification fails, the current default is generally the earliest-acquired units of that asset in that wallet or account.

== TRANSFERS DO NOT ERASE THE HISTORY ==

Moving Bitcoin between wallets you own is generally not a taxable disposition, apart from any Bitcoin used to pay the transaction fee.

But the tax history still has to travel with the Bitcoin.

The blockchain proves that an output moved. It does not prove what you originally paid, whether the acquisition was a purchase, income, gift, inheritance, mining, or something else, or which tax lot you intended to dispose of later.

That is why the useful record connects three things: the acquisition record, the wallet or account movement, and the final disposition.

== RECONSTRUCTING WHAT IS MISSING ==

Start with contemporaneous records.

Download every exchange and brokerage export you can still access. Pull confirmations, old tax files, bank or card statements, email receipts, and wallet transaction history. Match withdrawals and deposits between your own accounts so a transfer is not mistaken for a sale or a new purchase.

Then separate every unresolved item into one of three states.

**Verified.** The source records support the acquisition date, quantity, and basis.

**Estimated for planning.** You have evidence that narrows the range, but not enough to claim the number as settled. Orange Plan can use it for a projection as long as the uncertainty is visible.

**Unproven.** You cannot substantiate a basis yet.

The course used to say the IRS standard was simply "reasonable and documented." That was too broad. Documentation helps, but it does not create a general safe harbor that lets you make up a basis the return can claim.

If a meaningful lot remains unproven, work through the evidence with a tax professional before filing a disposition from it.

== ZERO BASIS IS A STRESS TEST, NOT AN AUTOMATIC LEGAL ANSWER ==

For planning, a zero-basis assumption can show the conservative tax exposure if no basis is allowed.

But do not confuse that stress test with a legal conclusion that the asset definitely has zero basis. And do not invent a number merely to avoid zero.

The honest plan labels what is known, what is estimated, and what is still unproven.

== WHAT CLEAN BASIS UNLOCKS ==

Once the records are clean, you can:

- identify units before a sale;
- see whether a loss actually exists;
- model gain harvesting in a low-tax year;
- compare selling, holding, gifting, or borrowing without guessing at the tax;
- reconcile the app with Form 1099-DA, Form 8949, and your return.

== YOUR DECISION ==

Which lots are verified, which are planning estimates, and which are still unproven.

== PUT IT IN ORANGE PLAN ==

Dashboard → Update Transactions for the history, then Strategy → Tax to review basis and modeled sales.

Use the file, AI-assisted, or manual path that matches the records you have. A linked source appears only when the app has a supported investment source.

== YOU ARE DONE WHEN ==

Every material lot is labeled honestly, the available evidence is saved outside the app, and an unproven lot is visible as an unresolved tax item instead of being silently assigned a number.
'''),

"scripts/05-2_taxable-tax-deferred-and-roth-bracket-wi.md": b(r'''
TELEPROMPTER SCRIPT — segment 5.2
5.2 Taxable, tax-deferred, and Roth: bracket windows and state taxes
~9 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to give each tax bucket a job, find the years when your rate may be lower, and build the roadmap the app will test.

== THE THREE TAX BUCKETS ==

The first bucket is taxable.

This is your brokerage account, Bitcoin held personally, and other taxable property. There is no age restriction on using it. When you sell an appreciated asset, the gain is generally taxed under the capital-gain rules, and the result depends on basis, holding period, total income, state, and the units you identified.

The second bucket is tax-deferred.

Traditional 401(k)s and traditional IRAs generally give you a tax benefit on the way in, then tax distributions as ordinary income later. They also come with required-distribution rules.

The third bucket is Roth.

Roth contributions go in after tax. Qualified Roth distributions are generally tax-free. That word qualified matters. A nonqualified withdrawal can expose earnings to income tax or an additional tax, and conversion amounts can have their own five-year clocks when withdrawn early.

Under current law, Roth IRAs and designated Roth plan accounts do not require lifetime distributions from the original owner.

== THE JOB OF EACH BUCKET ==

Taxable money is the flexible bridge. It can fund years before retirement-account access, pay a Roth-conversion tax from outside the converted account, and create capital-gain planning opportunities.

Tax-deferred money is useful when the deduction today is worth more than the ordinary-income cost you expect later. The risk is letting the account grow into forced distributions that arrive on the government's schedule.

Roth is the long-duration tax-free bucket when the rules for a qualified distribution are met. It is often the last bucket you want to exhaust, but that is a plan decision, not a universal withdrawal command.

== FIND THE WINDOW ==

The tax window is the period when earned income falls but required distributions and other forced income have not yet started.

For an early retiree, it can begin when work ends. Social Security may start later. Required distributions start later still, at the applicable age for that person under current law.

For the 45-year-old couple in this course, current law points to age 75, not 73. A different birth year can produce a different applicable age, so read the current value in the app and IRS guidance rather than memorizing one age for everyone.

The window is useful because the household may control more of the income that fills it.

Possible moves include:

- realizing long-term gains while room remains in a lower capital-gain band;
- converting part of a traditional account to Roth;
- drawing from traditional accounts before required distributions;
- delaying a taxable sale or conversion when another year is cheaper.

== THE BRACKET TOP IS THE STARTING POINT, NOT THE ANSWER ==

A common shortcut is "fill the bracket and stop."

That is too simple.

A conversion or gain can also change:

- how much of Social Security is taxable;
- Marketplace premium tax credits before Medicare;
- Medicare IRMAA later;
- the Net Investment Income Tax;
- state tax;
- capital-gain stacking;
- deductions, credits, and other income-based rules.

So the real question is not only which federal bracket the next dollar enters.

It is: what does the next dollar cost after every rule it touches?

Orange Plan can model the federal, state, and plan-level result. The current-year return still belongs with the tax professional who can see the entire household.

== CAPITAL-GAIN ROOM ==

Long-term capital gains have their own rate bands, but ordinary taxable income fills the stack first.

That means a household does not simply get a separate bucket of gains taxed at zero. The gain sits on top of the other taxable income, and only the portion that fits inside the current zero-rate band receives that rate.

A federal zero rate also does not mean a zero total cost. State tax, ACA credits, NIIT, and other interactions can still move.

== STATE TAX IS A SECOND MODEL ==

State tax deserves its own line because residence is not just the address on the day of a sale.

States can use domicile, statutory residency, part-year rules, source-income rules, community-property rules, and special treatment for trusts or businesses.

The app can compare two state assumptions. It cannot prove that a move changed your legal domicile or that a particular state has no claim on a transaction.

Treat the state comparison as a reason to ask a better question before a large move, not as a residency opinion.

== THE COUPLE'S ROADMAP ==

The couple's working years are high-income years. Their first retirement years may be lower-income years. Social Security begins later, and required distributions later still.

So their roadmap is:

1. Use taxable assets as the bridge.
2. Each year, model gains and Roth conversions together.
3. Check healthcare and state effects before applying anything.
4. Re-run after Social Security, Medicare, or required distributions begin.
5. Keep Roth available for later flexibility rather than spending it by default.

== YOUR DECISION ==

What job each account has, and which years deserve a tax-window review.

== PUT IT IN ORANGE PLAN ==

Strategy → Tax. Read the yearly roadmap, model one sale and one conversion, and keep them as previews until you deliberately apply the plan change.

== YOU ARE DONE WHEN ==

Every account has a tax job, the low-income window is marked on the timeline, and you can explain why the all-in marginal cost—not one bracket label—decides the size of the move.
'''),

"scripts/advanced/A5-1_rmd-risk-and-roth-conversions.md": b(r'''
TELEPROMPTER SCRIPT — segment A5.1
A5.1 RMD risk and Roth conversions
~10 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to cover why a large traditional account can create forced taxable income later, and how Roth conversions can reduce that risk during the years when you control more of the income.

== WHAT AN RMD IS ==

RMD stands for required minimum distribution.

It is the minimum amount the tax rules require an owner or beneficiary to distribute from certain retirement accounts.

For an owner, the yearly amount is generally the prior December 31 balance divided by the life-expectancy factor that applies to that person.

The applicable starting age depends on the birth cohort.

Under current law, age 73 applies to the intermediate cohort, and age 75 applies to people who attain age 74 after 2032. The couple in this course is 45 now, so their current-law planning age is 75.

Roth IRAs and designated Roth plan accounts do not require lifetime distributions from the original owner under current law. Beneficiaries still have distribution rules.

== WHY THE ACCOUNT CAN BECOME A PROBLEM ==

Traditional retirement money is not bad money.

The problem is a mismatch between the deduction you received while contributing and the forced income the account may create later.

The couple contributes $16,500 per year including the employer match in the illustration.

At a flat 7% illustration for 15 years, that grows to roughly $415,000 around age 60. Left for another 15 years at the same flat rate, it is roughly $1.14 million around age 75.

Using the current age-75 Uniform Lifetime factor of 24.6 as an illustration, the first required distribution would be roughly $46,000 before adding Social Security or any other income.

Those are illustration assumptions, not a projection promise. The app should calculate the actual roadmap from the saved account, return, and tax assumptions.

== WHY BITCOIN EXPOSURE MAKES THE SENSITIVITY LARGER ==

Now run an intentionally extreme sensitivity check.

A flat 20% return on the same annual contributions would produce roughly $1.19 million after 15 years, then more than $18 million after another 15 years if that flat return continued.

At the same illustrative divisor, the forced distribution would be hundreds of thousands of dollars.

That is not the return assumption I would use as the baseline. It is a sensitivity example showing why a fast-growing asset inside a traditional account deserves attention before the forced-distribution years arrive.

== WHAT A ROTH CONVERSION DOES ==

A Roth conversion moves money from a traditional account into Roth.

The taxable amount generally enters ordinary income in the conversion year. The converted amount then sits in the Roth bucket, where qualified distributions can be tax-free and the original owner has no lifetime RMD under current law.

The conversion is not free. You are choosing when to recognize the income.

The planning opportunity appears when today's all-in cost is lower than the cost you reasonably expect later, or when reducing the traditional balance creates flexibility the household values.

== THE RMD ITSELF CANNOT BE CONVERTED ==

Once an RMD is due for a year, the required amount has to come out. That required amount is not eligible to be converted.

A conversion can happen in the same year after the RMD is satisfied, but the required distribution is already taxable income and already fills part of the year's room.

That is one reason the years before RMDs can be valuable.

== LOWER PRICE, MORE UNITS FOR THE SAME DOLLAR CONVERSION ==

The conversion amount is measured in dollars on the conversion date.

If Bitcoin is held inside the traditional account, a lower Bitcoin price means the same dollar conversion can move more Bitcoin units into Roth.

That can be useful, but it is not a reason to time the market with taxes. The tax bill, available cash, future growth assumption, and household risk all still matter.

== DO NOT STOP AT THE BRACKET ==

The course used to frame the decision as filling a bracket without spilling into the next one.

That is only the first pass.

A conversion can also affect Marketplace credits, the taxable portion of Social Security, Medicare IRMAA, NIIT, capital-gain room, state tax, deductions, and credits.

So model the all-in marginal cost of the next conversion dollar.

There may be a point where the federal bracket has not changed, but the healthcare or state-tax cost makes the next dollar unattractive.

== PAYING THE TAX ==

When possible, paying the conversion tax from taxable cash or another outside source keeps the full converted amount in Roth.

That is generally cleaner than withholding part of the conversion, especially before age 59½, when an amount not converted may also be treated as an early distribution unless an exception applies.

But "always pay from outside" is not a universal command. Liquidity, reserve needs, tax basis, and the rest of the plan still come first.

== THE BENEFICIARY RULE IS NOT ONE SENTENCE ==

The old script said the children would simply have 10 years to empty an inherited traditional account.

Many nonspouse designated beneficiaries do face a 10-year outside deadline. But eligible designated beneficiaries have exceptions, and annual distribution requirements within the 10 years can depend on when the owner died and whether RMDs had started.

So the estate implication is real—traditional money can pass a compressed tax problem to heirs—but the exact schedule belongs in the current beneficiary rules and the family's tax review.

== THE DECISION FRAME ==

A conversion is attractive when:

- the household is in a genuinely lower all-in marginal-cost year;
- taxable liquidity can cover the tax without weakening the reserve;
- the traditional balance is on track to create forced income later;
- the household values more Roth flexibility;
- the plan remains strong after paying the tax.

A conversion is less attractive when:

- it destroys Marketplace credits or triggers another threshold;
- the tax has to come from money the household needs soon;
- the later rate is likely to be lower;
- the move is being sized from a bracket table without the rest of the return.

== HOMEWORK ==

1. Open the Tax roadmap and identify the first low-income year before the applicable RMD age.
2. Model three conversion sizes, including zero.
3. Read federal tax, state tax, healthcare or Medicare effects, capital-gain room, and ending account balances together.
4. Take the result to the tax professional as a proposed range, not a filing instruction.

You are done when you know which years deserve an annual conversion review and what all-in cost would make you stop.
'''),

"scripts/advanced/A5-2_harvesting-losses-and-gains.md": b(r'''
TELEPROMPTER SCRIPT — segment A5.2
A5.2 Harvesting losses and gains
~9 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to cover two moves that sound opposite but solve the same problem.

Loss harvesting records a loss when the tax value of the loss is useful.

Gain harvesting records a gain when the tax cost is low enough to justify a higher basis.

Neither move begins with the market. Both begin with your records and the whole tax return.

== LOSS HARVESTING ==

A capital loss first offsets capital gains.

If total capital losses still exceed gains, an individual can generally deduct the current annual limit against income and carry the unused loss into future years.

The value of the loss depends on what it offsets.

A loss used against a high-rate short-term gain can be more valuable than a loss carried for years and eventually used against a lower-rate long-term gain.

So do not multiply every harvested loss by one marginal tax rate and call that the savings.

== THE LOT HAS TO BE IDENTIFIED ==

Suppose the couple owns one low-basis Bitcoin lot and one recent high-basis lot.

If the recent lot is below its acquisition price, they may have a loss to realize while keeping the older low-basis lot.

But the lot does not become the tax lot because the app calls it HIFO.

For self-custody, the particular units have to be identified in the books and records no later than the transaction, and the records have to establish those units left the wallet.

For broker-held Bitcoin after 2025, the broker has to receive an instruction using identifiers it accepts no later than the transaction, and the taxpayer keeps substantiation.

If the identification fails, the current default generally uses the earliest-acquired units in that wallet or account.

That can turn a planned loss into an unexpected gain.

== WASH-SALE TREATMENT ==

Under current federal law, the wash-sale rule in section 1091 applies to stock or securities.

Spot Bitcoin is generally treated as property rather than stock or a security for this rule, so selling spot Bitcoin at a loss and repurchasing it has generally not triggered the stock wash-sale rule.

That statement is deliberately narrow.

A tokenized stock or another digital asset that is itself a stock or security can be covered. Congress can change the law. State treatment can differ. Verify the rule in the year you act.

== THE REAL COST OF THE ROUND TRIP ==

The tax value is only one side.

The other side includes:

- trading spread and fees;
- network fees;
- price movement between sale and repurchase;
- recordkeeping and lot-identification risk;
- a higher future gain because the repurchased units have a new basis;
- the effect on holding period.

A harvest is useful when the present value of the tax benefit is worth more than those costs and the future tax trade-off.

== GAIN HARVESTING ==

Gain harvesting does the reverse.

You deliberately realize a long-term gain in a year when the all-in tax cost is low, then reacquire the position and establish a higher basis.

A federal zero-percent capital-gain rate does not automatically make the move free.

Ordinary taxable income fills the stack first. State tax may apply. A larger gain can reduce Marketplace credits, trigger NIIT at higher income, or affect other income-based rules.

So the usable gain room is the amount the whole return can absorb at an acceptable all-in cost.

== A SIMPLE EXAMPLE ==

Assume a taxable Bitcoin lot is worth $100,000 with $40,000 of basis.

Selling the lot realizes a $60,000 gain.

If the whole gain fits in an acceptable all-in tax window, the household can repurchase and reset basis near $100,000.

If only half fits before another threshold becomes expensive, harvesting the full lot is not the right move. Sell the amount that fits, or pass.

== HIFO IS A POLICY, NOT THE STRATEGY ==

Highest-in, first-out can reduce current gain when the identification rules are met.

But it is not always the best long-term choice.

Using the highest-basis units now leaves the lowest-basis units for later. That may be exactly what the household wants, or it may create a larger gain in a future year when the rate is worse.

The decision is not "HIFO good, FIFO bad."

It is which identified units create the best lifetime tax path while preserving the custody and spending plan.

== HOMEWORK ==

1. Reconcile the lots and mark which units are actually identifiable under the current wallet or broker rules.
2. Model one loss harvest and one gain harvest.
3. Include fees, spread, state tax, ACA or Medicare effects, NIIT, holding period, and the future-basis consequence.
4. Save the move as a modeled possibility until the tax professional confirms the current-year return treatment.

You are done when the app shows the tax benefit, the execution cost, and the future basis together—and when passing is allowed to be the right answer.
'''),

"scripts/advanced/A5-3_state-taxes-and-relocation.md": b(r'''
TELEPROMPTER SCRIPT — segment A5.3
A5.3 State taxes and relocation: what the lever is actually worth
~5 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to price the state-tax difference without pretending a map can decide where you live or where a state can tax you.

== THE LEVER CAN BE LARGE ==

A large taxable Bitcoin gain can produce very different state results.

Some states impose no individual income tax. Others tax capital gains as income, use separate rates, or apply special rules.

The app can compare two state assumptions against the same modeled sale. That is useful because it turns "this state is expensive" into a dollar estimate on your own plan.

Do not freeze one example rate into the video. The current rate, deduction, credit, and local-tax rules belong in the app or current source.

== THE SALE DATE IS NOT THE WHOLE RESIDENCY TEST ==

The course used to imply that the state where you live in the year of sale is the whole answer.

It is not.

States can look at domicile, statutory residency, days in the state, the location of a home, family and business ties, part-year residency, source income, community-property rules, and the ownership structure involved.

Changing an address does not necessarily change domicile. Leaving a state does not necessarily end every source-based tax claim.

That makes the order important:

1. Decide whether the move makes sense for the life you want.
2. Before a large transaction, learn what the old state and the new state require to establish or end residency.
3. Document the real move rather than manufacturing a tax paper trail.
4. Model the transaction only after the legal residency assumption is defensible.

== PRICE THE WHOLE MOVE ==

State income tax is one line.

Also price:

- housing and property tax;
- insurance;
- healthcare access and premiums;
- travel back to family or business;
- local sales and other taxes;
- legal and moving costs;
- the value of the life you are leaving.

A tax saving can be real and still not be worth the move.

== THE RIGHT OUTPUT ==

The output of this lesson is not "move to a no-tax state."

It is one of three answers:

- moving is already part of the life plan, and the tax difference affects timing;
- moving is genuinely on the table, and the tax difference deserves professional modeling;
- moving is not on the table, so the state tax is a cost the plan should include rather than a problem to keep revisiting.

== HOMEWORK ==

1. Run the same modeled gain under the current state and one realistic alternative.
2. Add the major non-income-tax costs of the move.
3. Write whether the move is a lifestyle decision, a real option, or not an option.
4. Before acting, have a professional in the relevant state confirm domicile, part-year, source-income, and transaction treatment.

You are done when the state-tax difference is a number inside a real life decision, not a reason to move on its own.
'''),

"scripts/advanced/A6-1_health-insurance-between-retiring-and-me.md": b(r'''
TELEPROMPTER SCRIPT — segment A6.1
A6.1 Health insurance between retiring and Medicare
~8 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to price the healthcare bridge between leaving work and becoming eligible for Medicare.

This lesson applies when the paycheck stops before 65 and employer coverage stops with it.

== THE BRIDGE IS A DATED EXPENSE ==

If you retire at 60, the bridge is roughly five years.

The plan needs the premium, expected out-of-pocket cost, and a stress allowance for each year. It also needs the end date, because Medicare changes the coverage structure at 65 even though healthcare costs do not disappear.

== OPTION ONE: EMPLOYER CONTINUATION ==

COBRA or another continuation right may let you keep the employer plan for a limited period.

For many qualifying events, federal COBRA commonly lasts up to 18 months, with longer periods possible in some situations. The household may pay the full premium plus an administrative charge.

The advantage is continuity: same network, deductible structure, and claims process.

The disadvantages are price and the short runway.

Use the actual election notice. Do not assume every employer, event, or state follows the same duration.

== OPTION TWO: THE MARKETPLACE ==

Marketplace coverage is where tax planning and healthcare planning meet.

The net premium depends on household income, household size, the benchmark plan, location, and the law in the enrollment year.

For 2026, the enhanced pandemic-era subsidy rules no longer continue in the same form. That is exactly why the course should not memorize an old income cliff or an old premium example.

Use the current Marketplace estimate for the ZIP code and ages involved.

Also price the out-of-pocket side. Cost-sharing reductions apply only to eligible households enrolled in a Silver plan, and eligibility changes with income.

== MAGI IS PART OF THE PREMIUM ==

A Roth conversion, large taxable gain, business income, or retirement distribution can raise Marketplace income and reduce a premium tax credit.

That does not make the tax move wrong. It means the premium change is part of the tax cost.

The tax page and healthcare worksheet have to use the same income assumption. A conversion modeled without the premium effect is incomplete.

== OPTION THREE: A HEALTH-SHARING ARRANGEMENT ==

Austin's family uses CrowdHealth, and that personal experience can stay in the lesson as personal experience.

The category has to be described accurately.

A health-sharing arrangement is not health insurance. It generally does not create the same legal obligation to pay a claim, and the terms, exclusions, waiting periods, pre-existing-condition rules, member responsibility, and provider process vary by organization.

Price the exact current membership and read the current member agreement. Do not generalize one program's rules to the category.

HSA eligibility is a separate question. A sharing membership does not by itself create an HSA-eligible high-deductible health plan. Verify the actual coverage and current tax rules before making contributions.

== OPTION FOUR: A SPOUSE OR OTHER ELIGIBLE PLAN ==

A spouse's employer plan, retiree coverage, a union plan, or another special eligibility path can be the best bridge when it is available.

The right comparison uses the incremental family premium, deductible, network, and employer contribution—not only the employee's headline premium.

== THE COMPARISON ==

For each real option, record:

- monthly premium;
- deductible and out-of-pocket maximum;
- network and prescription fit;
- expected routine cost;
- worst plausible annual cost;
- tax-credit or tax-deduction assumptions;
- duration and the next enrollment trigger;
- whether the arrangement is insurance and what payment is legally guaranteed.

== AT 65 ==

Medicare eligibility changes the bridge, but enrollment timing, employer coverage, HSA contributions, Medigap, Medicare Advantage, prescription coverage, and IRMAA can all matter.

Do not wait until the final month to learn those rules. Put a Medicare review on the calendar before 65.

== PUT IT IN THE PLAN ==

Enter the best current estimate as a dated expense change from retirement until Medicare eligibility.

Then run a high-cost scenario that uses the out-of-pocket maximum or another defensible stress year.

The app may model the spending and tax result without reproducing every Marketplace or Medicare rule. The current quote and eligibility determination still come from the official enrollment source.

== HOMEWORK ==

1. Price every option actually available to the household.
2. Use the same income assumption in the tax and healthcare comparison.
3. Enter the base bridge cost and one stress case.
4. Put the next enrollment and Medicare review dates on the calendar.

You are done when the bridge has a current source, an end date, and a high-cost case—and when a health-sharing membership is never described as insurance.
'''),

"scripts/advanced/A6-2_sell-borrow-or-hold-funding-a-year-of-sp.md": b(r'''
TELEPROMPTER SCRIPT — segment A6.2
A6.2 Sell, borrow, or hold: funding a year of spending
~10 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to compare three ways a Bitcoin-heavy household can fund one year: sell, borrow, or hold and spend from another bucket.

This lesson fires when retirement is close enough that the household is actually deciding how next year's spending gets funded.

== ONE YEAR, THREE DIFFERENT COSTS ==

Use the same annual spending need for all three paths.

The comparison is not about which one sounds most Bitcoin-aligned. It is about what each path costs the plan in taxes, interest, liquidity, risk, and family complexity.

== PATH ONE: SELL ==

Selling Bitcoin creates cash with no loan to manage.

The tax is based on the gain in the specifically identified units, not the gross sale proceeds.

A low-income year may place some long-term gain in a lower federal capital-gain band. But ordinary income fills the stack first, state tax may apply, and the gain can affect Marketplace credits, NIIT, or other thresholds.

So "the gain is in the zero-percent band" is a modeled federal statement, not a promise that the transaction costs nothing.

The upside is simplicity and no liquidation or lender risk.

The cost is the Bitcoin sold, the tax, and the lost future participation on those units.

== PATH TWO: BORROW ==

Borrowed cash is generally not income when there is a real obligation to repay.

That does not make the entire strategy tax-free.

Interest accrues. The loan can be liquidated. A lender sale of collateral is a taxable disposition. Debt cancellation can create income. The lender and custody structure add risks that have nothing to do with the tax code.

The tax comparison therefore cannot stop at "loan proceeds are not taxable."

It has to include:

- interest and fees;
- the LTV path under a major drawdown;
- any collateral top-up reserve;
- the tax from a forced or planned collateral sale;
- counterparty and rehypothecation terms;
- repayment source;
- the estate's obligation if the loan remains at death.

Borrowing can be useful when it is small relative to collateral, the repayment source is clear, and the household values keeping the position.

It is fragile when repeated borrowing becomes the paycheck and every new year consumes more collateral capacity.

== PATH THREE: HOLD AND SPEND FROM RESERVE OR BRIDGE ==

The third path is to leave the Bitcoin untouched and fund the year from cash or another Bridge asset.

That preserves the Bitcoin position and avoids a new loan.

The cost is using liquidity that may have another job. The reserve has to remain large enough to protect the plan through a drawdown, and the Bridge has to be replenished under the rule the household already set.

Under current federal law, taxable property inherited at death generally receives a basis tied to date-of-death fair market value.

That general rule has conditions and exceptions. Gifts, certain trusts, property outside the taxable estate, consistent-basis reporting, and future law can produce a different answer.

So an outright taxable Bitcoin holding may receive a basis adjustment under current law. Do not turn that into "all embedded gain disappears" for every ownership structure.

== DO NOT COMPARE A TAX RATE WITH AN INTEREST RATE DIRECTLY ==

A common shortcut compares a 15% capital-gain rate with a 10% loan rate and picks the smaller number.

That is the wrong comparison.

The tax applies to the gain portion once. Interest applies to the loan balance over time, may compound, and may or may not be deductible. A forced sale can add tax later. The Bitcoin sold in path one and the Bitcoin pledged in path two also experience different future paths.

Use dollars over the same time horizon.

== THE FIVE-YEAR VIEW ==

Run each path for one year, then extend it for five.

For selling, track the units sold, basis, tax, and remaining Bitcoin.

For borrowing, track the loan balance, interest, collateral value, LTV, top-ups, repayment, and the outcome under a major drawdown.

For holding, track Reserve and Bridge depletion, refill years, and whether a bad market would force a later sale.

Most households will not choose one path forever. A strong plan can sell in one year, hold in another, and use a small loan for a specific purpose without turning borrowing into the foundation of the retirement paycheck.

== THE FAMILY TEST ==

Before a loan enters the plan, the spouse or person who would inherit the balance should be able to explain:

- who holds the collateral;
- the margin and liquidation lines;
- where repayment comes from;
- what happens after a 50% or 75% decline;
- what happens if the lender fails;
- what the estate has to do if the borrower dies.

If the household cannot explain it, the complexity cost is not priced yet.

== PUT IT IN ORANGE PLAN ==

Plan → Income → Retirement Borrowing compares the borrowing strategy against the saved withdrawal plan.

Read after-tax net worth, loan balance, Bitcoin remaining, taxes, and risk together.

A preview is not the plan until it is deliberately applied.

== HOMEWORK ==

1. Price one year under sell, borrow, and hold.
2. Extend the comparison to five years.
3. Add state tax, ACA or Medicare effects, lender terms, and any basis-at-death assumption.
4. Stress the loan under the lender's actual thresholds.
5. Take the tax outputs to the tax professional and the loan terms to someone who represents the household, not the lender.

You are done when the decision is supported by dollars over the same horizon and the household can explain the risk without using the phrase "Bitcoin will probably go up."
'''),

"lesson-text/05-1_cost-basis-what-you-paid-and-how-to-reco.md": b(r'''
# Cost basis: what you paid, and how to reconstruct it

Cost basis is the acquisition record used to measure gain or loss. For Bitcoin, keep the acquisition date, quantity, amount paid, acquisition costs included in basis, wallet/account movements, and the final disposition.

## Lot identification

- **Self-custody:** identify the units in your books and records no later than the transaction, then retain evidence that those units left the wallet.
- **Broker custody after 2025:** send the broker an instruction using identifiers it accepts no later than the transaction and retain substantiation.
- **No valid identification:** current IRS guidance generally defaults to the earliest-acquired units of that asset within the wallet or account.

HIFO is therefore a documented lot policy, not a retrospective tax button.

## Reconstruct in three states

1. **Verified:** contemporaneous records support the acquisition.
2. **Estimated for planning:** evidence narrows a range, but the number is not settled for a return.
3. **Unproven:** basis has not been substantiated.

Use exchange/broker exports, confirmations, bank statements, prior returns, email receipts, and wallet history. Match transfers between your own wallets so they are not mistaken for sales or new purchases.

A zero-basis assumption can be used as a conservative planning stress test. It is not an automatic legal conclusion, and an unsupported estimate is not automatically acceptable because it was documented.

## Complete when

Every material lot is labeled verified, estimated for planning, or unproven; the source evidence is retained outside Orange Plan; and unresolved basis goes to the tax professional before a return claims it.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/05-2_taxable-tax-deferred-and-roth-bracket-wi.md": b(r'''
# Taxable, tax-deferred, and Roth: bracket windows and state taxes

## Three jobs

- **Taxable:** flexible Bridge money; capital-gain treatment depends on basis, holding period, identification, total income, and state.
- **Tax-deferred:** deduction now, ordinary income later, plus required-distribution rules.
- **Roth:** after-tax contribution or taxable conversion; **qualified** distributions are generally tax-free. Nonqualified earnings or early conversion withdrawals can be different.

The couple's current-law RMD planning age is 75. Other birth years can have a different applicable age. Roth IRAs and designated Roth plan accounts have no lifetime owner RMD under current law.

## Find the window

Look for years after earned income ends but before Social Security, Medicare interactions, and required distributions fill the return. Model gains and Roth conversions together.

The top of a federal bracket is only a starting point. The next dollar can also affect capital-gain stacking, ACA credits, Social Security taxation, Medicare IRMAA, NIIT, state tax, deductions, and credits.

## State comparison

A state comparison is a scenario, not proof of domicile. Residency, part-year, source-income, community-property, entity, and trust rules vary.

## Complete when

Every account has a tax job, the low-income window is marked, and the planned move is sized from its all-in marginal cost rather than one bracket label.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/advanced/A5-1_rmd-risk-and-roth-conversions.md": b(r'''
# RMD risk and Roth conversions

**Gate:** meaningful pre-tax assets, a plausible lower-income window, and a way to pay conversion tax without weakening the plan.

## Current mechanics

- Applicable RMD age is cohort-specific: current law uses 73 for the intermediate cohort and 75 for people attaining age 74 after 2032.
- The couple in this course plans on age 75 under current law.
- Roth IRAs and designated Roth plan accounts have no lifetime owner RMD.
- An RMD due for a year cannot itself be converted.
- Many nonspouse beneficiaries face a 10-year outside deadline, but exceptions and annual-distribution rules can change the schedule.

## Illustration

$16,500 contributed annually for 15 years at a flat 7% is roughly $415,000. Another 15 years at 7% is roughly $1.14 million. At the current age-75 factor of 24.6, that implies an illustrative first RMD around $46,000.

A flat 20% sensitivity produces a much larger result. That is a stress illustration, not a baseline assumption or prediction.

## Conversion decision

Model ordinary tax, capital-gain stacking, Marketplace credits, Social Security taxation, Medicare IRMAA, NIIT, state tax, deductions, and credits together. The bracket top is not the complete answer.

## Homework

Model zero plus two conversion sizes in the low-income window. Use the result as a proposed range for the tax professional, not a filing instruction.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/advanced/A5-2_harvesting.md": b(r'''
# Harvesting losses and gains

## Loss harvesting

Capital losses offset gains first. Remaining net loss may be deductible up to the current annual limit, with the balance carried forward. The value of a loss depends on what it offsets and when.

Specific identification must satisfy the current wallet/account rule before or at the transaction. If it fails, the current default generally uses earliest-acquired units in that wallet or account. HIFO is not a retrospective universal exchange setting.

The federal wash-sale rule currently applies to stock or securities. Spot Bitcoin is generally outside that rule, but tokenized securities, future legislation, and state rules can differ. Verify in the year of action.

## Gain harvesting

A federal 0% long-term capital-gain band does not guarantee zero total cost. Ordinary income fills the stack first; state tax, ACA credits, NIIT, and other rules can move.

## Homework

Model one loss and one gain harvest with fees, spread, holding period, future basis, and every income-based interaction. Passing is a valid result.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/advanced/A5-3_state-taxes-relocation.md": b(r'''
# State taxes and relocation

A large taxable gain can create materially different state results. The app can compare two assumptions, but it cannot determine legal domicile or end another state's claim.

States may consider domicile, statutory residency, days, homes, family and business ties, part-year rules, source income, community property, and the ownership structure involved.

## Process

1. Decide whether the move fits the life plan.
2. Learn the old and new state's residency rules before the transaction.
3. Document the real move.
4. Compare state income tax with housing, property tax, insurance, healthcare, travel, and legal costs.

## Complete when

The tax difference is a number inside a genuine lifestyle decision and state counsel or a qualified tax professional has confirmed the transaction assumptions.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/advanced/A6-1_health-insurance-between-retiring-and-me.md": b(r'''
# Health insurance between retiring and Medicare

**Gate:** the plan stops work before Medicare eligibility.

Price only the options actually available:

- employer continuation such as COBRA, using the exact election notice;
- Marketplace coverage, using the current household income, benchmark plan, location, and current law;
- spouse or other eligible employer/retiree coverage;
- a health-sharing arrangement, clearly labeled **not insurance** and priced from its current member agreement.

Use the same income assumption in the tax and healthcare comparison. Roth conversions, gains, and distributions can change Marketplace premium tax credits.

For each option record premium, deductible, out-of-pocket maximum, network, prescription fit, expected annual cost, high-cost year, tax-credit assumptions, duration, and whether payment is legally guaranteed.

Enter a dated bridge expense through Medicare eligibility and a high-cost scenario. Put Medicare enrollment and HSA coordination on the calendar before 65.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/advanced/A6-2_sell-borrow-or-hold-funding-a-year-of-sp.md": b(r'''
# Sell, borrow, or hold: funding a year of spending

Compare the same spending need over the same horizon.

## Sell

Tax follows the gain in the identified units, not gross proceeds. Include state tax, ACA or Medicare effects, NIIT, and other income-based rules.

## Borrow

Loan proceeds are generally not income because they must be repaid. Interest, fees, liquidation, collateral sale, cancellation, lender failure, and repayment can create costs or tax consequences. Use the lender's actual thresholds.

## Hold and use Reserve/Bridge

Preserves Bitcoin but consumes liquidity with another job. Keep the Reserve and refill rule intact.

Inherited taxable property generally receives date-of-death basis under current law, subject to ownership, estate-inclusion, trust/gift, and consistent-basis exceptions. Do not assume every ownership structure receives the same result.

## Homework

Run all three for one and five years. Compare taxes, interest, loan balance, LTV, Bitcoin remaining, Reserve/Bridge depletion, and family complexity. A mix across years is allowed.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),
}
