# Separate walkthrough recording scripts

These are future-design scripts, prepared against PR #227. Capture each chapter separately after its screen/procedure is verified. Only each Narration block is spoken. The clean files linked below exclude directions, overlays and verification notes.

## W01 — [Build the first working plan](scripts/working/W01_build-the-first-working-plan.md)

### Chapter 1 — Find the first task · after 0.1

[Clean teleprompter take](teleprompter/walkthrough/W01-01.txt)

**Show:**

Open the intended Home → Your Plan entry, then Plan → Build & improve. Point to the next incomplete source record. Show the four destinations only as orientation. Use a separate three-line card for the existing mortgage, expected college support and possible renovation.

**Narration:**

We're going to start building the plan from the information you have today. Here on Home, I'll open the plan and use Build & improve to get to the next piece we need.

Before we add anything, notice the difference between these three examples. The Reeds' mortgage already exists, so it's a debt. College support is a future commitment with dates attached. The renovation is still an idea, so we'll compare it separately.

Let's begin with the first account that needs attention, with the latest statement beside it. We'll work through that record before moving on, so we can see where each number comes from.

**Overlay:**

Current fact · Expected change · Possible choice

**Verify:**

The next task opens its actual owner, not a duplicate form. Starting Plan is clearly preliminary and has no success percentage. Return to the same task after viewing its record.

**Capture dependency:**

PR #227 foundation contract: Home/Plan/Build & improve and Starting Plan states on the approved implementation head. Confirm actual task ownership and empty-state behavior; no invented probability or minimum-input requirement.

### Chapter 2 — Review accounts and holdings · after 1.2

[Clean teleprompter take](teleprompter/walkthrough/W01-02.txt)

**Show:**

Use Home → Your Money to open the category-filtered Accounts view and one account detail. Review the existing checking account ($18,000), Alex Roth ($145,000) and direct-Bitcoin location (3.4 BTC) in separate takes. Use the approved contextual add/update entry only where a record is missing.

**Narration:**

Here we're looking at one account from the money category on Home. Before getting into what it owns, I'm matching its name, owner and account type to the statement. If it's already entered, this is the record we're reviewing. Adding another would count the same money twice.

Alex's Roth IRA tells us the account type, but we still need the investments inside it. For cash, we're checking the balance. For the Bitcoin location, we're checking the quantity and where the coins are held, using a plain name without recovery information.

After a correction is saved, I'll reopen the account beside the same statement. That lets us see whether the record now describes what the household actually owns.

**Overlay:**

One account · Correct owner/type · Holdings explain the balance

**Verify:**

One record per account. Quantity, total, owner/type and source date survive the saved readback. Direct Bitcoin and fund exposure retain different identities.

**Capture dependency:**

Foundation account-detail and maintenance writer paths, scoped ownership and truthful update dates. Fixture amounts require frozen-price treatment; actual holdings, HSA/education composition and any missing owners require a separately reviewed capture extension. Do not choose example tickers to fill gaps.

### Chapter 3 — Read what the connection supplies · after 1.2

[Clean teleprompter take](teleprompter/walkthrough/W01-03.txt)

**Show:**

Open account detail → How this account updates in an authorized synthetic connected-source case. Read the actual capability receipt for balance, holdings, activity and purchase details, including an incomplete case and its supported next step.

**Narration:**

This account is connected, but let's look at what that connection actually supplies. The balance tells us the total. Holdings explain what's inside it. Activity and purchase details answer different questions about how it got there.

If the total arrived without the investments, the statement can help us fill in that composition. Missing purchase history can stay with the tax question it needs to answer. We're also looking at when the financial information was last confirmed; opening the page today doesn't make an older balance current.

That tells us what's ready to use and which part still needs our input. Next we'll look at an account where we know the total but need to explain the investments.

**Overlay:**

Balance · Holdings · Activity · Purchase details

**Verify:**

The receipt describes the actual supplied products and timestamps. Missing positions are not shown as cash, zero holdings or fully synced; one supported next action is identified.

**Capture dependency:**

D34/D62 capability receipts and financial-fact freshness. Capture requires certified synthetic evidence and the approved receipt/recovery UI. No live credentials, provider connection, paid refresh or staged provider response.

### Chapter 4 — Explain a balance-only investment account · after 1.2

[Clean teleprompter take](teleprompter/walkthrough/W01-04.txt)

**Show:**

At the same $145,000 Roth account, use Holdings needed → Add investments. Enter verified positions or use the accepted mutually exclusive Estimated mix path. Where identities are unresolved, show the source $116,000 spot-fund exposure/$29,000 stocks only as the estimated categories they support.

**Narration:**

We know this Roth account is worth $145,000. What we're doing here is explaining that balance, so the plan knows how the money is invested.

When the statement supplies actual investment names and quantities, those are what we use. If all we have is an approximate mix, it stays labeled as an estimate. The Reeds' teaching example has $116,000 of spot Bitcoin-fund exposure and $29,000 of stocks inside the same $145,000 account. Those amounts explain the total; they don't increase it.

Any cash needs to come from the statement too. We won't make an unexplained remainder into cash just to finish the record. After saving, let's reopen the account and make sure the composition explains the same total once. Any remaining difference stays visible until we can explain it.

**Overlay:**

Fictional categories: $116,000 + $29,000 = one $145,000 account

**Verify:**

Exact positions or Estimated mix is the saved composition, never both added together. Unknown basis/date remains unknown; no fake purchase, cash remainder or extra balance appears.

**Capture dependency:**

D65 complete balance-only workflow, multi-position entry, classification, estimated/exact mutual exclusion, discrepancy state, atomic save and reload. Keep this chapter pending if the approved implementation cannot perform the full path.

### Chapter 5 — Attach history to what you already own · when relevant records are available after 1.2

[Clean teleprompter take](teleprompter/walkthrough/W01-05.txt)

**Show:**

In one account detail, use Upload account activity or the supported purchase-details route for a reviewed fictional buy/transfer chain. Show an overlap already present and its deduplication treatment. Record a transfer to self-custody through the accepted transfer flow, not a sale/repurchase substitute.

**Narration:**

This part is useful when you have purchase or transfer records for holdings already in your plan. If those records don't apply, or you don't have them yet, note what's missing and continue to chapter six for the monthly picture. You don't need to repair an unrelated old purchase before you do that.

Here, the purchase explains Bitcoin already included in today's holdings. It isn't a new purchase today. As we follow it from the exchange to the wallet, the transfer keeps the original history attached. If the same purchase is already here, accepting it again would give us a duplicate.

I'll compare the household quantity before and after the history is attached. It only changes if we've identified a real position that was missing. Otherwise, we've learned more about the same Bitcoin. Unsupported purchase details stay unknown, and we can move on to the monthly starting picture.

**Overlay:**

Existing holding + supporting history = the same Bitcoin counted once

**Verify:**

No duplicate quantity, transaction or lot; transfer retains history and basis without a taxable-sale substitution. Deliberate overlap is recognized; unresolved discrepancy remains visible.

**Capture dependency:**

Certified upload adapter, scoped mapping, transfer ledger, history/position reconciliation and deduplication receipt. A safe synthetic fixture needs dates, fees and provenance supplied before capture. Missing history does not block unrelated cash-flow work.

### Chapter 6 — Enter the starting monthly picture · after 1.2

[Clean teleprompter take](teleprompter/walkthrough/W01-06.txt)

**Show:**

Open Cash Flow → Income, Taxes and withholding, Everyday spending, Debt payments and Saving and investing as needed. Enter original source state only. Present the exact Reed cash bridge as a separate teaching graphic, never a fabricated app result.

**Narration:**

Now we're connecting the accounts to the money moving through the household each month. The first thing I'm checking is what each income amount includes. Alex's gross pay is before deductions. Morgan's example income is after ordinary business costs, but the equipment payment is counted separately. Those meanings need to match the fields.

In our teaching calculation, gross income is about $19,417 a month. After the $4,000 tax allowance, $10,800 living costs and about $3,342 required debt, there's $1,275. Alex's $775 contribution leaves $500 for other priorities. The employer's $387.50 goes into retirement saving; it isn't bill money.

Let's follow the app's actual result from its income and tax inputs. If it differs from the illustration, we need to understand those inputs before assigning another transfer. That's the monthly picture we'll use when we record the retirement question next.

**Overlay:**

Fictional bridge: $1,275 before employee − $775 = $500; employer $387.50 separate

**Verify:**

Original spending remains $10,800. Required payments and payroll deductions are counted once. The source provision is distinguished from calculated tax and any genuine discrepancy is explained.

**Capture dependency:**

D32/D48 income and withholding semantics, payroll election, business-loan inclusion, debt source and employer-match route. Exact inputs: $19,416.67 − $4,000 provision − $10,800 − $3,341.67 = $1,275. No balancing override to force the app to $500; approved tax jurisdiction and payroll details are required.

### Chapter 7 — Record each person’s retirement question · after 1.2

[Clean teleprompter take](teleprompter/walkthrough/W01-07.txt)

**Show:**

Use Plan → Build & improve to reach the accepted retirement timing and spending owners. Enter Alex’s intended age 52, Morgan’s separately supported timeline and the reviewed fictional spending/benefit/horizon extension. Show each date and dollar basis before saving.

**Narration:**

With the starting facts in place, we can enter the work-change question you wrote down at the beginning. Alex wants work to become optional at 52. That records his intention; the calculation will test whether it can be funded. Morgan's income stays on its own timeline.

For retirement spending, we'll begin with current costs, remove the ones that really end and add healthcare or other costs that begin. The dollar units shown here matter, so we don't apply inflation twice. Any Social Security or pension estimate belongs to the right person and start date.

Once this is saved, we have a question to test. A missing benefit estimate stays visible until there's a source for it. Next we'll read the assumptions the plan uses to look beyond today's facts.

**Overlay:**

Work date · Spending basis · Each person’s income · Horizon

**Verify:**

Saved timing affects the correct person once. Spending units, horizon and sourced benefits survive readback; no missing benefit is replaced with invented income.

**Capture dependency:**

Approved timing/spending owners and date conventions. Source fixture supplies age-52 intent, not birth dates or a final benefit quote. Do not automatically adopt the separate $96,000/$12,000/$40,000 retirement illustration as the baseline.

### Chapter 8 — Read assumptions and test one change · after 1.4

[Clean teleprompter take](teleprompter/walkthrough/W01-08.txt)

**Show:**

Open Plan → Overview → Assumptions to identify the approved build's actual new-plan standard preset and read its saved path, inflation, income growth and horizon. Retain it unless a reasoned change is being demonstrated. Use Plan → Scenarios for one less-favorable growth comparison with all household choices unchanged. Inspect early/later path years, then return to Current without adopting it.

**Narration:**

These are the assumptions behind the plan we just built. We'll start with the app's standard preset for a new plan and read what it means. You can keep it while you learn; changing it needs a reason beyond making the result look better.

I'm looking at the return path in an early year and a later year, then inflation and the planning horizon. A declining growth path can be quite different from one fixed annual rate. Now we'll make a separate weaker-growth comparison with retirement timing, spending and contributions unchanged.

Let's follow the first year where the funding differs and see which income or account has to do more. That tells us which household decision becomes harder under this assumption. Then we'll return to the current plan. Testing a weaker path doesn't choose it as the new starting assumption, and we can read the main result with that distinction clear.

**Overlay:**

One changed assumption · Same household choices

**Verify:**

Current and comparison identities remain explicit; only the selected assumption changes. Results are current for that comparison; returning leaves saved Current unchanged.

**Capture dependency:**

Approved Assumptions and Scenarios owners, actual new-plan preset identity, custom-path availability, holding classification and result-receipt identity. Confirm the standard preset exists and show its real name/values; do not infer a default risk level. No preset percentages or calculated outcome is supplied by the script; show the actual approved build.

### Chapter 9 — Read the first complete result · after 1.5

[Clean teleprompter take](teleprompter/walkthrough/W01-09.txt)

**Show:**

Read Plan → Overview’s full-Plan receipt: chosen timing/spending/horizon, displayed percentage and exact successful count. Open the first year after the work change and its funding detail. If the plan is still preliminary, demonstrate the specific missing input instead of presenting full results.

**Narration:**

Here we're ready to read the first complete result. I'll start with the work date, spending and horizon, because the percentage describes that question. The successful-path count tells us how many modeled futures funded it under these rules; it doesn't promise what happens to this family.

Let's open the first year after work changes and follow the income, costs and taxes, then what investments have to supply. If that withdrawal is surprising, the event or obligation behind it is what we need to understand.

From there, we can choose a fact to correct or a realistic change to compare. If the starting plan fits, keeping it is a valid result too, with its important limitation still visible. In the next take, we'll use Ask to help trace one of these numbers back to its source.

**Overlay:**

Question tested → successful paths → funding year → next action

**Verify:**

Percentage/count use the same full-Plan receipt, inputs and horizon. No chosen age is passed off as a calculated result. The year detail supports the explanation and no illustration is inserted into the interface.

**Capture dependency:**

D16/D50 preliminary-to-full states, exact standard, successful count, missing-input gating and automatic result currentness. The generic 790/1,000 teaching example must remain outside the app. No invented Refresh/Recalculate shell control.

### Chapter 10 — Trace an Ask explanation · after 1.5

[Clean teleprompter take](teleprompter/walkthrough/W01-10.txt)

**Show:**

Open Ask with the populated plan and ask a specific question about a visible result. Follow the actual response back to its source rows. Add a separately captured current market-report or outside-AI-summary demonstration only after availability and content verification.

**Narration:**

Let's use Ask for a question we can check against the plan. I'm asking it to walk from income to the monthly amount remaining and explain what's already been deducted. That gives us something concrete to compare with the cash-flow rows.

The date, income, taxes and existing contribution all need to match. If they don't, we keep that question open and find the difference before changing the plan. We can use the same approach for a retirement withdrawal or a missing tax input.

If you use an outside AI review, read the actual summary before sharing it. A restore backup has a different purpose, and removing a name doesn't remove every private detail. What we're taking forward is the fact or choice we need to work on. Next we'll go into Cash Flow and check how the monthly amount matches your records.

**Overlay:**

Ask for the source · Match the date and inputs · Choose the action yourself

**Verify:**

Actual response is traceable and no saved input changes implicitly. Export is identified correctly and inspected; no wallet secrets, credentials or assumed anonymization.

**Capture dependency:**

Approved Ask route/context/permissions and source links. Market report requires real date and sources; external AI feature requires actual availability and reviewed export schema/privacy. No staged AI answer, connected account action or outside message is authorized by this manuscript.

## W02 — [Verify cash flow, set the Reserve, and add expected events](scripts/working/W02_verify-cash-flow-set-the-reserve-and-add-expected-events.md)

### Chapter 1 — Follow the monthly money · after 2.1

[Clean teleprompter take](teleprompter/walkthrough/W02-01.txt)

**Show:**

Open Cash Flow → Income and Taxes and withholding, then the summary’s debt and saving routes. Reconcile original income with a synthetic pay-stub/statement source. Show the precise Reed bridge as its own graphic.

**Narration:**

We've entered a starting monthly picture. Here we're checking whether it agrees with the records before using the amount left over. I'll begin with the income source, because gross pay still has deductions to account for while a bank deposit already has them taken out. Morgan's ordinary business costs are deducted, but the equipment payment remains separate.

In our original teaching calculation, $1,275 before Alex's $775 contribution becomes $500 afterward. The employer adds $387.50 to retirement money. Let's follow where the remaining household cash actually went: checking, saving or a cost we haven't included.

Any difference needs resolving at its source. A withholding change affects cash available and the amount still due; it doesn't by itself change the calculated tax obligation. Once the income side makes sense, we can look more closely at the spending period.

**Overlay:**

Original example: $1,275 − $775 employee = $500; employer $387.50 separate

**Verify:**

Income and deductions reconcile without double subtraction; original $10,800 living remains active. Actual tax output is not forced to the $4,000 teaching provision.

**Capture dependency:**

D32/D48 income/withholding owners, employee election and business payment convention. Full-precision bridge and tax jurisdiction must be verified; synthetic records need actual period/timing. No reduction, Reserve transfer or future contribution starts here.

### Chapter 2 — Verify spending and bill timing · after 2.1

[Clean teleprompter take](teleprompter/walkthrough/W02-02.txt)

**Show:**

Open Cash Flow → Your Plan uses and Everyday spending → Verify Spending. Compare the method, source period and categories. Resolve one material uncertainty supported by the synthetic transaction set; show a purchase/settlement pair, annual bill and bill/payday timeline.

**Narration:**

Here we're checking the method and months behind the spending number. A recent permanent change may make newer records more useful, but the annual bills still need a place in that amount.

This grocery purchase is spending. The card payment settles it, so counting both would repeat the cost. Repayment of an older balance is a separate debt need. And a generic $1,200 annual premium represents $100 a month, even if eleven monthly statements don't show the bill.

Once the supported estimate is saved, let's look at when the money leaves. Checking needs enough for the bills before the next paycheck, with saving arranged around that need. That gives us a current amount we can trust before comparing a spending change.

**Overlay:**

Method + source period · Purchase counted once · $1,200/year = $100/month

**Verify:**

Supported classifications preserve raw evidence; no blanket exclusion of all card payments. The saved method/value agrees with the chosen period, annual costs and known recent changes.

**Capture dependency:**

D32 selector methods (12-month average, Typical month, Recent 3-month trend, Manual), D33 category/correction behavior and saved readback. Capture only implemented methods. Annual premium and pay dates remain separate generic graphics unless the reviewed synthetic record supplies them.

### Chapter 3 — Compare a sustainable spending change · after 2.1

[Clean teleprompter take](teleprompter/walkthrough/W02-03.txt)

**Show:**

Use a Keep/Cut/Reduce teaching card beside the original spending. In Plan → Scenarios compare original living $10,800 with proposed $9,600, other inputs unchanged. Return to Current; use a clearly named reduced-spending rehearsal state for later course arithmetic only after the fictional choice is explicit.

**Narration:**

Now we can use the spending records to compare a change you'd actually make. With Keep, Cut and Reduce, we're asking which costs are worth their price, which you no longer choose and which could cost less without giving up something you need. Fees and lost coverage belong in that last decision.

The Reeds' proposal cuts living costs by $1,200 a month. In the teaching example, that changes the amount available from $500 to $1,700. They still need to identify the bills that make it possible. We'll compare the proposal first, then record when the real change begins and update current spending once it has happened. Saving a lower figure doesn't cancel a service.

For the Reserve and Debt examples that follow, we're testing this reduced-spending version. Your actual surplus stays unchanged until those spending changes happen. Keep that distinction with the number as we move on.

**Overlay:**

Proposed: living $10,800 → $9,600; available $500 → $1,700

**Verify:**

Original and reduced states are distinguishable; no fabricated cancellations or early adoption. Saving amount, effective date and outside action are visible; $7,200 Reserve essentials are never substituted for normal living.

**Capture dependency:**

Approved scenario/preview mechanism, effective-date semantics, return-to-Current and save/reload. Source does not itemize the $1,200 reduction. Actual app tax differences must be explained rather than balanced away.

### Chapter 4 — Set the Reserve target and existing sources · after 2.3

[Clean teleprompter take](teleprompter/walkthrough/W02-04.txt)

**Show:**

Open Cash Flow → Cash reserve, inspect essential spending and select months. Use What counts toward this reserve to assign eligible existing funds, including partial assignment only if implemented. Present $7,200 × 6 = $43,200; $32,000 assigned; $11,200 gap from one state.

**Narration:**

Let's give the Reserve a target using the essential costs from the lesson. The Reeds' $7,200 includes required household debt, so we're not adding those payments again. Testing six months gives a $43,200 target.

Now we're looking at the existing money available for that job. Checking money for near-term bills, tax money and other committed amounts stay out of this assignment. Access matters too: pledged Bitcoin or money you can't readily use isn't the same as available cash.

The example assigns $32,000, leaving $11,200 to fund. We haven't added an asset; we've given existing money a job. After saving, I'll reopen the assignment so we can see the same sources and gap. Then we'll compare how quickly to close it beside the debt.

**Overlay:**

Fictional: $7,200 × 6 = $43,200; minus $32,000 = $11,200 gap

**Verify:**

Sources total once, remain their original assets and retain partial amounts on readback. Essential debt is not doubled. Target, assigned amount and gap share one state; unavailable/unpriced funds do not create a complete total.

**Capture dependency:**

D49 reserve role and partial-assignment writer, eligibility, schema reconciliation and exact target/gap display. D32 Cash reserve ownership. Do not mimic a missing partial-assignment control or claim the teaching arithmetic is captured output.

### Chapter 5 — Choose the Reserve pace beside Debt · after 2.3

[Clean teleprompter take](teleprompter/walkthrough/W02-05.txt)

**Show:**

Carry the same gap into the approved Reserve funding/contribution owner. Show proposed $500/month beside the reduced-state $1,700 pool and anticipated $1,200 extra-card claim. Use a separate cash-coverage comparison for dependents or reliance on one income, then return to the unchanged Reed split.

**Narration:**

We're still testing the reduced-spending version with $1,700 available. Your actual surplus stays unchanged until those spending changes happen. At $500 a month, the $11,200 Reserve gap takes 22.4 months, reaching the target with part of the twenty-third deposit before interest or withdrawals. That's almost two years to consider alongside the risk we're covering.

I'd give accessible cash more weight when dependents rely on one income and an interruption would otherwise require more borrowing. Building it faster may be worth slower extra-debt repayment, with required payments still covered. The Reeds have a stable paycheck and variable business income; they aren't a single-income example.

Their proposed $500 Reserve pace leaves $1,200 of the same $1,700 for the card. We'll carry that split into Debt before settling it. The bank transfer comes after the combined decision, when we know the two choices fit together.

**Overlay:**

Proposed: $500 Reserve + $1,200 extra card = $1,700 once

**Verify:**

Pace is affordable from the same pool, gap stays visible and required payments remain covered. Faster Reserve is explained as a conditional trade-off, not a new Reed contribution or fixed threshold.

**Capture dependency:**

Actual contribution owner, pace save/readback and any affordability display. Final transfer is outside the app. Keep the 22.4 arithmetic off an app screen unless its semantics match; no invented calendar funding date or automatic recommendation.

### Chapter 6 — Add an expected event and trace its funding · after 2.4

[Clean teleprompter take](teleprompter/walkthrough/W02-06.txt)

**Show:**

Open Plan → Overview → Life events. Add the reviewed expected vehicle need and one person’s income change, with explicit recurrence and units. Inspect the affected year’s income/costs/funding. Put the possible renovation in Plan → Scenarios and return to Current. Rehearse a planned change becoming current.

**Narration:**

Here we're adding an expected change to the plan. The amount, date and frequency describe what happens: a vehicle purchase happens once, while an income change belongs to the person and period it affects. The dollar basis tells us whether we're using today's estimate or a future quote before applying inflation.

Let's follow it into the affected year and see how it's funded. Income, existing savings and an investment withdrawal leave different resources afterward. Adding the event tells the plan an expense is coming; it doesn't start a separate saving transfer.

We'll keep the possible renovation in its own comparison until it's chosen. And when a planned change becomes today's fact, the old event needs reconciling so it doesn't happen twice. If college is part of your plan, the next take applies this to its several years of payments. Otherwise, you're ready to carry the expected costs into Debt.

**Overlay:**

Event: amount · timing · recurrence · units · funding

**Verify:**

Expense and income changes occur once at the correct time/person; source funding is supported, not inferred. Renovation remains separate; planned-to-current update creates no duplicate effect.

**Capture dependency:**

Life-event owner, supported source/account attribution, recurrence, inflation units, event-to-asset/debt treatment and save/readback. Reed vehicle timing is about three years; exact dates and amount need capture extension. Generic $30,000 car is not a fixture price. Unsupported attribution remains unresolved.

### Chapter 7 — Fit education support beside the same cash · optional after 2.5

[Clean teleprompter take](teleprompter/walkthrough/W02-07.txt)

**Show:**

Use Plan → Life events for the annual commitment and the existing education resource view/worksheet for assignment by child. Show $20,000 × 4 = $80,000; $58,000 split $29,000 each; $51,000 gap; $850/month flat-cost, no-growth benchmark over 60 months. Inspect actual modeled tuition years only with reviewed dates and account facts.

**Narration:**

Let's place the college commitment beside the money we've already assigned. In this example the parents intend to help with $20,000 a year for four years. Of the existing education money, $29,000 goes toward the older child's commitment, with the other $29,000 kept for the younger child. That leaves $51,000 to fund.

Having all of it ready in five years, with flat costs and no growth, takes $850 a month. But the proposed $500 Reserve and $1,200 extra card already use the $1,700 available. So the useful decision is what changes, or what still needs answering before the college commitment is funded.

If saving begins after the card ends, we'll recalculate with fewer months remaining. Then we can inspect the tuition years and the income and accounts actually paying them. That commitment goes with us into Debt, so the next choice doesn't use the same money again.

**Overlay:**

$51,000 ÷ 60 = $850/mo; existing $1,700 is already assigned

**Verify:**

Resources are allocated once, without changing ownership/beneficiaries. Benchmark assumptions stay visible; no extra $850 is silently saved. Actual future income and account funding support the chosen commitment or the unresolved trade-off.

**Capture dependency:**

Reviewed dates, education owners/beneficiaries, qualification/tax treatment, timing and any event-specific account attribution. No aid award, return, auto-529 route or hypothetical loan is presumed. Use the worksheet when the exact benchmark is not a supported app result.

## W03 — [Set debt jobs and test one financing decision](scripts/working/W03_set-debt-jobs-and-test-one-financing-decision.md)

### Chapter 1 — Verify payments and changing terms · after 3.1

[Clean teleprompter take](teleprompter/walkthrough/W03-01.txt)

**Show:**

Use Home → Your Money → Debt and open one existing debt detail at a time. Review the card, mortgage and interest-only HELOC against authorized fictional records. Read current balance, rate, required payment, rate-reset/maturity and security terms; use contextual Add or update only for a verified change.

**Narration:**

We're going to look at what the existing debts require before deciding about extra payments. Here I'll match the balance, rate and required payment to the lender record. The card's $405 minimum isn't all principal: the rough first-month illustration has about $235 of interest and $170 of principal before purchases or fees. The actual statement has its own billing rules.

The home-equity line has a different issue. Its interest-only payment leaves principal to repay later, so the payment-change date and exit matter. Let's keep those beside the cash-flow picture.

The teaching payments are about 17% of gross income, but the original example has only $500 after other costs and Alex's contribution. The ratio doesn't give us extra payment money. That $500 and any proposed spending change are the starting point for choosing what each debt does next.

**Overlay:**

Required payment → interest + principal; DTI does not equal surplus

**Verify:**

Correct debt record, source and terms survive readback. Required/extra payments remain separate. HELOC date or guarantee omissions remain missing facts rather than inferred defaults.

**Capture dependency:**

PR #227 Debt detail owner/contextual writer, payment schedule and source freshness. Exact card billing/minimum rules and HELOC maturity require the reviewed extension. No debt is duplicated or newly adopted by this review.

### Chapter 2 — Separate household leverage from loan collateral · after 3.6

[Clean teleprompter take](teleprompter/walkthrough/W03-02.txt)

**Show:**

Read included household assets and debt, with net worth separately. Use the unchanged balance-sheet and partial-stress graphics unless the exact app scenario is verified. Then show fixed-debt 50%/25% initial LTV to an assumed 80% liquidation threshold in a separate generic comparison.

**Narration:**

Here we're separating the household's overall debt from one loan's collateral requirements. The Reeds' included assets are $1,996,000 before subtracting debt. Against $444,500 owed, that's about 22% debt-to-assets. The home and restricted or dedicated accounts aren't all cash available for repayment.

In the partial stress illustration, included assets fall to $1,217,200 while debt stays the same. The ratio moves to about 37%. That shows what a fall in asset values does to the household measure.

Now consider the separate lender test. With fixed debt and an assumed 80% liquidation line, 50% initial LTV reaches it after a 37.5% price fall. Posting enough for 25% initial LTV gives a 68.75% decline to that same line. Those numbers compare upfront collateral. The actual agreement's call, cure and liquidation terms are what go into the response rules, alongside the household's ability to fund them.

**Overlay:**

Household DTA: 22.27% → 36.52% · One loan’s LTV uses pledged collateral

**Verify:**

Assets/debt/net-worth denominators remain distinct. Stress assumptions/exclusions are visible. No Reed Bitcoin loan or integrated worst-case result is fabricated.

**Capture dependency:**

Exact supported asset denominator and scenario fields. Source partial stress: BTC exposure −70%, selected stocks −30%, home −20%; education/health unchanged; vehicle/business values omitted while debts included. Fixed-debt threshold graphics are hypothetical, not lender offers.

### Chapter 3 — Choose and save affordable debt actions · after 3.1

[Clean teleprompter take](teleprompter/walkthrough/W03-03.txt)

**Show:**

In Plan → Scenarios, compare extra card payments against the same current inputs and Reserve claim. Inspect payoff/interest and Cash Flow effect. Use Debt detail’s approved save path only after choosing the action, then read it back. Contrast the low fixed mortgage and review the other debts without fabricating finalized choices.

**Narration:**

We're continuing the reduced-spending test. Your actual surplus stays unchanged until the spending changes happen. Here we're comparing the card with $500 going to the Reserve and $1,200 of extra card principal. The required $405 was already counted, so the total card payment is $1,605.

Let's read the payoff date and interest under that comparison, then see whether required payments and the Reserve still fit. With the mortgage, we're weighing interest avoided against cash becoming home equity. Extra principal may shorten the term without reducing next month's payment, and property costs continue after payoff.

Once you've chosen an affordable action, we'll save it in Debt and reopen it to check the terms. Changing the lender payment is a separate outside step. The saved choice is what we carry back into Cash Flow, so it only uses the money once.

**Overlay:**

Reduced example: $405 required + $1,200 extra = $1,605 card total

**Verify:**

Comparison does not silently change Current; selected save is counted once in Debt and Cash Flow. Mortgage escrow/property costs remain correctly funded. Each other debt has a choice or precise unresolved term.

**Capture dependency:**

Approved future Scenario-to-owner decision flow, extra-payment capacity semantics, debt strategy save/preview behavior, payoff calculation and save/reload. Preserve separate source $500 Reserve and $1,200 extra. No predetermined app payoff date or automatic lender payment.

### Chapter 4 — Compare one financing purpose through its exit · after 3.4; A3.2 when relevant

[Clean teleprompter take](teleprompter/walkthrough/W03-04.txt)

**Show:**

Use Plan → Scenarios for one hypothetical $30,000 project at the reviewed date. Compare cash, a supported taxable sale and one eligible financing arrangement, plus smaller/delay. Read cash retained, payments, fees, collateral and ending principal. Use a separate graphic for $20,000/8%/60-month amortizing-versus-interest-only arithmetic.

**Narration:**

Let's compare one purchase using the same amount and date in each version. Paying $30,000 from the $32,000 Reserve leaves $2,000 for that job. A taxable sale needs enough proceeds after its actual tax cost. Financing keeps cash initially, but the payment has to fit beside the Reserve and card.

The final balance is part of that comparison. In our separate $20,000 example, about $406 a month pays the loan down over five years; about $133 interest-only leaves the $20,000 owed. A refinance needs the full replacement mortgage priced, while unusual terms need their actual settlement formula, guarantees and use restrictions.

We'll keep any contract term the app doesn't represent beside the comparison and resolve it before choosing. A smaller or delayed project may be the affordable answer. Whichever direction you choose, the payment and principal exit go into the debt rules next.

**Overlay:**

Same need/date → cash left → payment → final balance → repayment source

**Verify:**

Equal need and dates, actual source tax, complete repayment shape and constraints. Proposal remains separate; no application or approval. Unsupported settlement terms prevent a model-complete conclusion.

**Capture dependency:**

Reviewed fictional offer/date, taxes/basis, permitted uses and guarantee terms; approved Scenario expressiveness. Generic arithmetic: $405.5279 amortizing, $4,331.6735 total interest; $133.3333 interest-only, $8,000 interest plus principal. HEI/shared appreciation requires its actual formula; do not approximate it as an ordinary loan.

### Chapter 5 — Write funded repayment and response rules · after 3.6; A3.1 when relevant

[Clean teleprompter take](teleprompter/walkthrough/W03-05.txt)

**Show:**

Use the existing debt instructions/worksheet alongside Debt for actual loans or Plan → Scenarios for proposals. Record purpose, amount, payment source, principal exit, dates, fallback, operator and backup. For A3.1 only, use a separate generic $50,000/3.5 BTC sizing graphic and an authorized non-broadcast procedure diagram; do not create a Reed Bitcoin loan or initiate a real top-up.

**Narration:**

This is where the borrowing decision becomes something the household can follow. We're writing where the regular payments come from and how the principal gets repaid. If that uses a sale, the amount, date and response to smaller or late proceeds matter. If it uses refinancing, we need an answer for approval not being available.

Then we can connect a review trigger to the resource and person who will respond. Someone trusted needs a way to recognize a time-sensitive problem and find the safe instructions while you're unavailable. Wallet secrets stay out of this record.

If you're using the Bitcoin-loan lesson, there's a separate sizing example to work through here. We start with the full obligation before deciding how much collateral to post. This example dedicates 3.5 BTC to $50,000 of debt when Bitcoin is $100,000. After an 80% decline, those coins are worth $70,000. If posted in time, that's about 71.4% LTV. At the assumed 80% liquidation line, 3.125 BTC only reaches the boundary. The 3.5 BTC provides some room, but any stricter call-cure or maturity term still has to be met.

The $50,000 opening amount assumes separately funded interest and fees. One hypothetical year of 12% capitalized interest makes it $56,000, exactly 80% of the stressed $70,000. So if costs accrue, the initial principal needs reducing or more Bitcoin needs dedicating before borrowing.

After sizing the debt, posting 1 BTC starts it at 50% LTV and leaves 2.5 BTC reserved in cold storage. Posting all 3.5 starts the same loan at about 14.3%. The smaller initial deposit reduces lender exposure but needs a faster response. Reserved coins only count for lender LTV after they arrive and are credited. That's why the top-up trigger, amount, access time and maximum collateral exposure belong here. An automatic feature can't reach into your cold wallet; the actual funding and confirmation requirements still apply.

Repeat borrowing uses the same supporting resources too. In the recurring illustration, $25,000 becomes $28,000 after 12% interest. The next $25,000 draw makes $53,000, and another 12% makes $59,360. We can't reuse the same spare collateral for each draw. If the payment, timed response or final repayment still lacks a resource, the proposal stays unchosen. Once the rules are supported, we can carry the chosen obligation back into the household cash flow.

**Overlay:**

Debt first → collateral placement second · Posted BTC and dedicated BTC have different jobs

**Verify:**

Ordinary exit and unavailable-operator fallback are usable. Conditional worksheet preserves costs, exact boundary, stricter cure, timely crediting and combined repeated debt. No double-used BTC, automated cold-wallet claim or signed/executed loan.

**Capture dependency:**

Actual contract, advanced modeled terms, saved liquidation selection, cost-accrual rule, source identity and approved scenario receipt. D63 parity/fix-first gates remain app implementation work. Any provider procedure requires safe independently authorized capture with no broadcasting, credentials or secret exposure; illustration is not proof a lender accepts the arrangement.

### Chapter 6 — Carry one debt decision into Cash Flow and Allocation · after 3.6

[Clean teleprompter take](teleprompter/walkthrough/W03-06.txt)

**Show:**

Return to Cash Flow → Debt payments and Saving and investing. Read the saved extra claim from Debt without entering it twice. Show the reduced-state bridge and a distinctly future payoff condition, then hand current/future claims to W04.

**Narration:**

Let's bring the debt choice back to Cash Flow and see the same money one more time. In the reduced-spending illustration, $2,475 before Alex's $775 contribution becomes $1,700 afterward. The $500 Reserve and $1,200 extra-card plan use that amount once, so there isn't another amount to invest now.

When the card is actually paid off, we'll verify which payments ended and whether any charge remains. The example's $405 required plus $1,200 extra would release $1,605 if those were still being paid. That future money needs a new decision; payoff doesn't automatically send it into investments.

What we take into Allocation is today's chosen claims and that future review condition. Then we can decide where contributions go and what they buy, using the money actually available at the time.

**Overlay:**

Today: $1,700 assigned once · After payoff: verify the released $1,605 before routing

**Verify:**

Debt and Cash Flow read one saved state. Required payments, Reserve and payroll saving are not duplicated. Future payoff money does not appear in current surplus or an automatic transfer.

**Capture dependency:**

D37 payoff/removal semantics and D32 saving owner; exact source state, schedule, future start/stop and readback. Preserve W04’s existing conditional allocation illustration. No bank or lender action is implied by the planning save.

## W04 — [Route contributions into usable accounts and intended holdings](scripts/working/W04_route-contributions-into-usable-accounts-and-intended-holdings.md)

### Chapter 1 — Read the current whole portfolio — after 4.3

[Clean teleprompter take](teleprompter/walkthrough/W04-01.txt)

**Show:**

Open Plan → Portfolio and allocation. Expand the included-assets explanation and one account’s holdings. Show the Reed general-subset arithmetic only when the approved app denominator matches it; otherwise show it as a labeled separate teaching graphic and state the actual app scope.

**Narration:**

Here's the portfolio we put together earlier. I'm starting in Plan, under Portfolio and allocation, with Current. Before we decide what to change, I want to make sure this percentage describes everything we intended to include.

In the Reed example, the Bitcoin itself is worth $410,000 and their spot Bitcoin funds are worth $318,000. Together, that's $728,000 of Bitcoin exposure. The funds are investments inside their accounts. The separate 4.1 Bitcoin is split between 3.4 in self-custody and 0.7 with a professional custodian.

I'm opening the included assets so we can see where those dollars came from, along with the stock and cash holdings. If an account contains several investments, we count those holdings once. We don't add the account balance again on top.

Dedicated education and healthcare money still have their own jobs. Once the included holdings agree with our records, we can compare Current with a target using that same group of assets. That gives us a useful starting point for the role we want Bitcoin to have.

**Overlay:**

Cue “with Current.” → Current holdings; cue “Together, that's $728,000” → $410,000 + $318,000 = $728,000, labeled Reed illustration.

**Verify:**

Holdings and totals reconcile without duplicate account balances. Any app denominator difference is explicitly explained; no $1,307,000 total is forced onto an incompatible screen.

**Capture dependency:**

Approved Portfolio and allocation route, eligible-assets denominator, spot-fund classification and exact account/holding composition readback.

### Chapter 2 — Choose Bitcoin’s intended role — after 4.3

[Clean teleprompter take](teleprompter/walkthrough/W04-02.txt)

**Show:**

Display a separate four-path orientation graphic, then the existing target choice in Portfolio and allocation. Do not stage an automatic risk-profile score or add an unimplemented notes field.

**Narration:**

Now that we know the current mix, let's talk about what we want it to become. Before entering a percentage, I'd come back to the role you chose for Bitcoin in the teaching lesson.

These four descriptions can help with that conversation: Foundation, Integration, Optimization and Sovereign. They describe different intentions. Someone with a smaller position isn't behind someone with a larger one.

The amount we test needs to fit the people who share this money and the dates when they'll need it. A position can feel comfortable while markets are rising and very different when a bill arrives during a decline.

For now, we're choosing a starting amount to test. The next step is to put the Reserve and approaching expenses beside it. If those jobs don't have enough funding, we can adjust the proposal before saving a target.

**Overlay:**

Cue “These four descriptions” → Four illustrative paths; cue “before saving a target” → Starting choice → funding check → target.

**Verify:**

The role/range remains a proposed preference; no arbitrary suitability recommendation or saved target is fabricated.

**Capture dependency:**

Target Current/Preview availability, existing choice provenance and absence of automatic save during the orientation scene.

### Chapter 3 — Build the target from funding needs — after 4.3

[Clean teleprompter take](teleprompter/walkthrough/W04-03.txt)

**Show:**

Show separate $1 million arithmetic graphic, then the approved funding rows and target Preview. Read canonical Reserve assignment; identify accessible early-retirement funding. Use a supported stress comparison only after input/result review.

**Narration:**

Let's put some dollars behind that proposed mix. We've already chosen the Reserve, so we're bringing that amount forward and adding any committed expenses that need separate funding.

This is a separate $1 million illustration. The household wants to test $500,000 in Bitcoin. Its $60,000 Reserve and $40,000 purchase use $100,000. That leaves $400,000 for long-term stock exposure: 50% Bitcoin, 40% stocks and 10% cash.

Now suppose two $50,000 retirement payments still need funding, and the household wants that money in cash too. Cash becomes $200,000 and stocks become $300,000. They've given themselves more cash for those first payments, with less remaining in long-term growth investments.

Back in the target comparison, I'm looking at the first important payment and the money that can supply it through a difficult market. If that source is missing, the target still needs work. Once we choose a mix we intend to follow, we can save it and read it beside Current. That saves the target; it doesn't trade the holdings.

**Overlay:**

Cue “a separate $1 million illustration” → Hypothetical household, not Reeds; cue “Cash becomes” → 50/30/20 versus 50/40/10.

**Verify:**

Near-term costs are counted once, Reserve uses the same source as Cash Flow, target totals 100%, and save/readback preserves the intended target without trading assets.

**Capture dependency:**

Canonical Reserve reader, early-access row attribution, target writer, Current/Preview isolation, supported stress and saved-target receipt.

### Chapter 4 — Fit current contributions and future milestones — after 4.7

[Clean teleprompter take](teleprompter/walkthrough/W04-04.txt)

**Show:**

Open Cash Flow → Saving and investing with the reviewed reduced-spending state. Show employee, employer, Reserve and extra-card claims separately. Show future-only conditions using supported controls or existing toolkit notes when absent.

**Narration:**

We're back in Cash Flow, under Saving and investing, to connect the plan to this month's money. I'm using the reduced-spending version from our earlier comparison, so we need to keep that version consistent here.

The $2,475 before Alex's contribution becomes $1,700 after his $775. Then the $500 Reserve contribution and $1,200 extra card payment use that entire amount. Alex is investing through payroll, but there's no additional investment transfer available from the remaining household cash today.

His employer's $387.50 adds retirement saving separately. It doesn't give the household another $387.50 to spend.

The card payoff gives us a future decision to prepare for. The illustrated $1,605 becomes available only after those payments stop. When that happens, we'll check what was actually released and whether the other bills have changed before starting a new transfer. Reserve completion has its own condition as well. We can prepare those later choices now while keeping today's contribution instructions affordable.

**Overlay:**

Cue “use that entire amount” → $500 + $1,200 = $1,700; cue “only after those payments stop” → Future condition, not today’s cash.

**Verify:**

Current household outflows are affordable once. Employer money is not spendable; future $1,605 is not active and no assumed payoff date is invented.

**Capture dependency:**

Cash Flow contribution treatment, existing savings and employer match, Reserve/extra-debt integration, timing controls and save/readback.

### Chapter 5 — Select a receiving account — after 4.5

[Clean teleprompter take](teleprompter/walkthrough/W04-05.txt)

**Show:**

Start with the funding job, then open the appropriate existing account and relevant private/synthetic provider terms. Verify menu/access/eligibility outside the app where necessary. Do not imply that every account has a Bitcoin option.

**Narration:**

We know what this money needs to do. Now let's find the account that can hold it. I'm starting with the date we'll need to use it, because that can change which account makes sense.

For an early-retirement gap, we need a supported way to get the money out at that time. A tax benefit doesn't help fund the gap if the money is unavailable when the bills arrive.

Here's the provider's investment menu. We're checking that it permits the investment we intend to buy, along with the account's fees, contribution eligibility and remaining room. An HSA, education account or self-employed plan belongs in the comparison when it fits the actual commitment and we're eligible to use it.

If an existing account meets those needs, we can use it. If we need to open another one, that becomes an outside action with a person and a date attached. Once the account and investment are supported, we can compare the tax election where that choice applies.

**Overlay:**

Cue “the date we'll need to use it” → Access date; cue “fees, contribution eligibility and remaining room” → Eligibility / room / menu / fees.

**Verify:**

Receiving account supports the actual purpose, allowed investment and timing; missing eligibility/provider facts are explicit.

**Capture dependency:**

Actual account type, owner, menu, contribution limits for the applicable year and supported future receiving-account selection.

### Chapter 6 — Compare the tax election at equal cost — after 4.5

[Clean teleprompter take](teleprompter/walkthrough/W04-06.txt)

**Show:**

Use separate $1,000 pretax teaching graphic, followed by a reviewed contribution Preview and payroll-cost evidence. State whether actual comparison keeps contributions or household cost equal.

**Narration:**

Let's work through Traditional and Roth at the same household cost. This separate example starts with $1,000 of pretax earnings. At a hypothetical 20% tax rate, that puts $1,000 into deductible Traditional or $800 into Roth.

If both investments double and the Traditional withdrawal is also taxed at 20%, both leave $1,600 available under the stated rules. The Roth withdrawal has to qualify for tax-free treatment. The example helps us compare tax timing without quietly giving one choice a larger starting contribution.

Now I'm looking at the payroll effect of the actual election being considered. If we keep the contribution amount the same while switching to Roth, take-home pay can fall. That extra cost needs to fit beside the Reserve and debt payments we already chose.

Once we've compared that cost, we can select Traditional, Roth or a mix and save the intended contribution choice. This applies to new money. An existing Traditional balance stays where it is unless we arrange a separate conversion, which we'll cover in Tax.

**Overlay:**

Cue “same household cost” → Equal-cost comparison; cue “This applies to new money.” → Contribution election ≠ conversion.

**Verify:**

Comparison basis is clear, required qualification assumptions are present, and updated payroll cash reconciles with the same plan.

**Capture dependency:**

Applicable payroll tax/election evidence, equal-cost versus equal-contribution treatment, contribution Preview and save owner.

### Chapter 7 — Tell each account what to buy — after 4.7

[Clean teleprompter take](teleprompter/walkthrough/W04-07.txt)

**Show:**

Read target/Current in Portfolio and allocation, then receiving amount/investment in Cash Flow → Saving and investing. Show future $1,000/$605 route as a future comparison. Select actual reviewed fictional holdings without inventing security identity.

**Narration:**

We've got the account and an amount we can afford. Let's connect those to the investment the contribution will buy.

First, here's the target gap. In the Reeds' 60% Bitcoin comparison, the target is $784,200 against $728,000 currently held. That $56,200 difference helps us decide where purchases could go over time. It isn't cash available to invest today.

For the future card-payoff example, the proposed split is $1,000 to personally held Bitcoin and $605 to a taxable stock fund. The $500 Reserve contribution stays separate. This new investment route remains inactive until payoff, when we check the actual money released.

For each contribution, I'm connecting the amount to the receiving account and the investment it will buy. We still need to know the product's holdings, fees and strategy. A name that sounds like the investment we want isn't enough to establish what it owns.

Changing future purchases doesn't rebalance the investments already held. A taxable sale would need its own review. Next, we'll take these planned instructions to the provider so the money actually arrives and buys what we intended.

**Overlay:**

Cue “isn't cash available” → Target gap ≠ available contribution; cue “inactive until payoff” → Conditional $1,000 + $605.

**Verify:**

Amount/account/investment/start condition agree; target-to-trade automation is not invented and currently unavailable cash is not routed.

**Capture dependency:**

Supported holding selection, target calculation denominator, next-dollar precision, future conditions and contribution save/readback.

### Chapter 8 — Complete and verify provider instructions — after 4.7

[Clean teleprompter take](teleprompter/walkthrough/W04-08.txt)

**Show:**

Use existing action list with payroll election, account opening, transfer and recurring purchase instructions. Show an authorized synthetic confirmation only if available, otherwise leave the outside action pending. No provider mutation during course preparation.

**Narration:**

The plan now tells us where each contribution is supposed to go. The remaining work happens with the employer, bank or investment provider.

For payroll, that means the amount, tax election and investment instructions for new contributions. A bank transfer also needs a date that fits the bills. Some brokerages receive the cash first and require another instruction to buy the investment, so a successful transfer alone may leave the money sitting in cash.

I'm putting those actions beside the person who will do them and the date. After the first contribution, the provider confirmation lets us check the amount, receiving account and holding purchased against this plan.

If the money arrived but stayed in cash, we still have a purchase instruction to finish unless cash was the intended holding. Until we have that evidence, the action stays pending. Future changes stay tied to the condition that funds them.

That finishes the contribution setup for this stage. Next, we'll work on the purchase records we need when money eventually comes out, so we can understand what a sale would realize for tax.

**Overlay:**

Cue “amount, receiving account and holding purchased” → Deposit ✓ Purchase ✓; cue “Until we have that evidence” → Planned / confirmed.

**Verify:**

Every current provider action has confirmation or a specific owner/date. Future conditions remain future and a saved app choice is not presented as an executed investment.

**Capture dependency:**

Safe synthetic/private evidence workflow, actual provider requirements and a supported non-secret action-status location.

## W05 — [Reconcile tax records and prepare one useful comparison](scripts/working/W05_reconcile-tax-records-and-prepare-one-useful-comparison.md)

### Chapter 1 — Read the gain on a proposed sale — after 5.1

[Clean teleprompter take](teleprompter/walkthrough/W05-01.txt)

**Show:**

Open the applicable taxable holding’s Purchase details from its account or the contextual Tax entry. Preview a supported hypothetical 0.2 BTC sale at $100,000. Show all three source lots in a separate graphic if the actual source units are not loaded.

**Narration:**

Let's look at a sale before placing it. I'm opening the taxable holding and its purchase details so we can see which units we own, when we acquired them and what they cost.

In our separate illustration, selling 0.2 Bitcoin produces $20,000 before fees. The three purchase-price examples give $11,600, $3,200 or $10,400 of basis. That changes the gain to $8,400, $16,800 or $9,600 even though the sale proceeds are the same.

The gain still isn't the tax bill. We need the rest of the tax year's information to estimate that, and we need tax and costs accounted for before treating the proceeds as spending money.

Here, I'm checking which units are actually available and how they must be identified for this transaction. If a cost is missing, we leave it unknown and find its source record before relying on the comparison. Previewing the lot doesn't place a trade or notify the custodian. Once the records support it, we can compare the sale in the context of the year's income.

**Overlay:**

Cue “The gain still isn't the tax bill.” → Proceeds → basis → gain → tax → usable cash; cue “doesn't place a trade” → Preview only.

**Verify:**

The quantity and available lots match source records; missing slices are not silently consumed and gross proceeds are not labeled tax or spending cash.

**Capture dependency:**

D54/D58 purchase details and lot-method confirmation, supported sale Preview, current holding identity and tax output with fees/basis coverage.

### Chapter 2 — Repair the relevant purchase history — after A5.2

[Clean teleprompter take](teleprompter/walkthrough/W05-02.txt)

**Show:**

Use one reviewed synthetic source import, overlapping import, same-owner transfer and unresolved source detail. Capture position/history before and after; show retained original files outside the app without private identifiers.

**Narration:**

We're going to repair the part of the purchase history this decision depends on. I have the source records for this holding, and I'm keeping the original file while we review the imported events.

An overlapping upload may contain purchases we've already entered. Those need to be recognized as the same events, or the history will say we bought more than we did.

A transfer needs the same care. In this no-fee illustration, 0.1 Bitcoin leaves the exchange and reaches the same owner's wallet. Its purchase history follows it. The move doesn't create a second purchase or automatically become a sale.

Now we can compare the remaining units with the current holding. If they don't agree, we'll look for fees, missing activity or duplicates. We keep a missing detail visible while finding the evidence, instead of inventing a purchase to make the numbers match.

When the history agrees, we have a supported basis for the sale comparison. We've improved the records behind the holding without adding that holding to the portfolio a second time.

**Overlay:**

Cue “Its purchase history follows it.” → Same owner, same units, original basis; cue “without adding that holding” → History improves; assets counted once.

**Verify:**

Overlaps deduplicate, same-owner transfer retains quantity/history, and any unresolved evidence stays explicit. No invented historical transaction makes balances agree.

**Capture dependency:**

Certified import event coverage, duplicate and transfer reconciliation, fees, unknown slices and before/after quantity proof.

### Chapter 3 — Find an actual income window — after 5.4

[Clean teleprompter take](teleprompter/walkthrough/W05-03.txt)

**Show:**

From Plan open the contextual Tax strategy/roadmap and a relevant year. Show each spouse’s work/benefit dates, distributions, supported loss carryforward and planned transactions. Use only approved model outputs.

**Narration:**

Here's the tax roadmap. We're looking for a year when the household's income changes enough that a withdrawal or conversion might be worth comparing.

I'm opening the first relevant year and looking at each person's work income and benefits. Distributions, gains, conversions and a supported loss carryforward belong in that same year's picture too. Alex stopping work doesn't automatically make the household's income low if other income continues.

Now we can compare that year with the next important income change. If there's a lower-income interval, we have a reason to examine it. We still need the total cost of adding income, including effects beyond the tax bracket.

We'll start with one amount and identify the money that would pay its tax. The existing plan stays as our baseline. If a missing filing or income record could change this window, that's the fact to obtain before relying on it. Once the year's inputs are supported, we're ready to compare a conversion, a spending withdrawal and leaving the plan as it is.

**Overlay:**

Cue “that same year's picture” → One tax-year picture; cue “start with one amount” → Bounded comparison.

**Verify:**

Year, owner, income sources, RMD dates and transaction state are consistent. No fixed-age RMD assumption or fabricated tax window.

**Capture dependency:**

Contextual Tax route, year-detail parity, actual birth-year/account inputs, loss carryforward persistence and saved-result freshness.

### Chapter 4 — Compare conversion, withdrawal and no change — after 5.4 / A5.1

[Clean teleprompter take](teleprompter/walkthrough/W05-04.txt)

**Show:**

Show separately labeled opportunity-cost graphic, then Current versus a reviewed bounded conversion Preview. Compare smaller amount, no conversion and accessible spending withdrawal where relevant. For A5.1 expand the same comparison over the bounded years.

**Narration:**

We've found a year worth examining. Now let's see whether moving existing Traditional money into Roth actually helps this plan. I'm keeping spending and return assumptions the same and starting with no added conversion, then comparing the proposed amount and a smaller one.

There are three amounts to follow: what moves to Roth, what pays the bills and what pays tax. In our separate teaching example, $30,000 moves to Roth and $6,000 comes out of outside assets for tax. That $6,000 would have remained available and could have grown if we hadn't spent it, so it belongs in the comparison.

I'm reading the first affected year's tax and accessible cash, then the later after-tax resources. An accessible Traditional withdrawal for spending is another choice when it serves this income window. It provides cash for bills; moving money into Roth doesn't do that.

For a multiyear schedule, we'll repeat that check whenever income materially changes. If a conversion leaves the early years short, the amount or timing needs work. Once the tax source and spending fit, we can save the strategy we intend to follow. The actual conversion remains a separate provider transaction.

**Overlay:**

Cue “There are three amounts to follow” → Conversion / spending / tax; cue “later after-tax resources” → Include tax-payment opportunity cost.

**Verify:**

After-tax and liquidity comparison includes outside assets, same lifestyle and assumptions. RMD exclusion, basis, healthcare and access prerequisites are recorded; saving does not fabricate execution.

**Capture dependency:**

Sole conversion writer, Current/Preview and scenario isolation, total after-tax result, tax-payment source, supported schedule, healthcare scope and save/reload receipt.

### Chapter 5 — Prepare a tax-sensitive sale or deliberate pass — after A5.2

[Clean teleprompter take](teleprompter/walkthrough/W05-05.txt)

**Show:**

Select a supported fictional candidate with documented lots. Show transaction-purpose and income comparison, identification evidence and replacement review in a private/synthetic packet. Do not place a live trade.

**Narration:**

We have a sale candidate with records we can support. Before doing anything with it, let's come back to its purpose: providing spending money, realizing a gain or realizing a loss. That tells us which costs and benefits to compare with the rest of the year's income.

The units we're planning to sell need to be identified through the process required for this account and transaction date. I'm keeping the acknowledgment or contemporaneous record with the proposal. Choosing units in a planning screen doesn't complete that process with the provider.

For a securities loss sale, replacement investments and automatic purchases matter, including relevant spouse and IRA activity. For a gain harvest, we need to see the income room remaining after other gains and conversions, including state and healthcare effects.

If the expected benefit is too small, or the records still don't support the transaction, keeping the investment is a valid result. We can record that reason and stop there. If we decide to proceed, this remains a proposed transaction until the actual instruction is executed. Then we'll reconcile the confirmation and remaining holdings.

**Overlay:**

Cue “identified through the process required” → Identify before required deadline; cue “a proposed transaction” → Preview → execute → record.

**Verify:**

Candidate has supported basis/units, current identification process, replacement review, income context and intended exposure. No app selection is presented as legal execution.

**Capture dependency:**

Actual supported candidate calculation, asset/account/year-specific identification, replacement tax review, transaction evidence and honest execution status.

### Chapter 6 — Finish the professional and reporting packet — after 5.1 / 5.4 / A5.2

[Clean teleprompter take](teleprompter/walkthrough/W05-06.txt)

**Show:**

Download supported FORM 8949 TAX DATA CSV when relevant and inspect actual columns/coverage. Use existing private packet for focused questions. Show post-trade reconciliation only with labeled synthetic evidence and no real financial actions.

**Narration:**

Let's finish with the records another person would need to review this decision. I'm opening the export first so we can see its dates, units, proceeds, fees and available purchase details. FORM 8949 TAX DATA supports the tax professional's work; it isn't a filed form.

Alongside it, we're including the relevant source records, the proposed transaction, this year's income context and the specific question still unresolved. That might be a missing basis record or how an account rule applies. The packet doesn't need unrelated private files to answer that question.

After an actual transaction, the confirmation lets us compare the recorded units and remaining holdings with what happened. Provider reporting and the filed return also need to agree before we carry those figures into another year. Until confirmation exists, the transaction remains pending.

The useful result here is a decision someone can understand and evidence they can review. Once that is resolved, we can return to the tax-timing comparison or carry the chosen funding approach into the retirement paycheck.

**Overlay:**

Cue “isn't a filed form” → Tax data for review; cue “remaining holdings” → Confirmation → remaining lots → filed record.

**Verify:**

Export scope and omissions are visible; proposed/completed states remain separate; no full sensitive backup, filing claim or invented confirmation.

**Capture dependency:**

Approved export content, source/realized/remaining-lot consistency, private sharing workflow and reviewed synthetic confirmation.

## W06 — [Build and test the retirement paycheck](scripts/working/W06_build-and-test-the-retirement-paycheck.md)

### Chapter 1 — Build the complete cash need — after 6.1

[Clean teleprompter take](teleprompter/walkthrough/W06-01.txt)

**Show:**

Open the first retirement-year detail and drill into canonical spending/income records where corrections are needed. Show separate labeled $108,000/$68,000 and $126,000/$86,000 graphics, never as a Reed calculated result.

**Narration:**

Here's the first year after work stops. We're going to see how much money the household needs and where it comes from. The starting spending number is the cost of living that life, so we don't simply replace today's salary or carry retirement contributions into it.

I'm opening living costs, healthcare, required debt, tax and dated events to see that each appears once. Debt stays separate from ordinary living costs so its payments can end when the loan is paid off. Then we'll look at the income that actually arrives during this year.

In the separate teaching illustration, $108,000 of living and healthcare costs minus $40,000 of gross income gives a rough $68,000 gap. Adding $12,000 of hypothetical tax and $6,000 of debt changes it to $86,000. That's why we need to know what a displayed amount includes before treating it as the withdrawal needed.

If a source record is missing or duplicated, we correct it there. After saving, I'll wait for the updated result and read the funding need again. Gross income, withholding and the complete tax cost need to agree. Then we can look at which money is available during these first retirement years.

**Overlay:**

Cue “each appears once” → Spending + healthcare + debt + tax + events; cue “rough $68,000 gap” → Illustration, not final withdrawal.

**Verify:**

Income and complete outflow reconcile; tax/withholding, events, debt and portfolio distributions are counted once; calculation reflects saved changes.

**Capture dependency:**

Year-detail attribution, canonical income/spending owners, tax-dependent withdrawal math, automatic Plan updating and current result receipt.

### Chapter 2 — Fund the early intervals and benefit dates — after 6.1 / A6.3

[Clean teleprompter take](teleprompter/walkthrough/W06-02.txt)

**Show:**

Show both adults’ timelines and every material funding interval. Open underlying account-access evidence and a supported benefit-timing comparison. Use actual reviewed synthetic estimates and preserve their dollar convention.

**Narration:**

Let's put the early retirement years on the timeline. Alex wants work to become optional at 52. That leaves seven and a half years to 59½, but Morgan has separate dates and account rules. We need both people's timing for the household plan.

I'm opening each period before a new benefit or access route begins. We can see the income that continues and the accessible money assigned to the remaining gap. The Reserve and other committed expenses already have jobs, so we can't spend those same dollars a second time.

If an account needs an early-access exception, we need the owner, amount, dates and provider permission to support it. A rollover that could change that route stays pending while we work through the early-access lesson.

Here's the benefit-timing comparison using the same spending and actual estimates. Waiting may provide more later income, but the intervening years need funding too. We're reading both sides. By the end of each period, we want to see the money supplying it or the specific gap still to solve. Healthcare is the next dated cost we'll add to that picture.

**Overlay:**

Cue “Morgan has separate dates” → Two people, two timelines; cue “specific gap still to solve” → Funding interval readback.

**Verify:**

All material early intervals have supported sources or explicit gaps; source ages, access evidence and inflation convention are correct.

**Capture dependency:**

Person/account access model, separation and distribution rules, actual benefit estimates, spouse/survivor support scope and interval funding output.

### Chapter 3 — Enter coverage costs and transitions — after 6.3

[Clean teleprompter take](teleprompter/walkthrough/W06-03.txt)

**Show:**

Show synthetic/private coverage quote inputs and existing expense/life-event owners. Compare ordinary/difficult-year costs, income effects and person-specific transition dates. Keep unsupported subsidy calculation outside app as a labeled estimate.

**Narration:**

We're adding the coverage that replaces employer insurance. I have the coverage comparison beside the plan so we're using the complete annual cost, including premiums and the additional costs we expect to pay.

In our separate example, $12,000 of premiums plus $3,000 of other costs totals $15,000. The other choice is $8,000 plus $8,000, or $16,000. A smaller premium didn't make it the cheaper year. Here, we'll use the actual quote and keep the difficult-year exposure and its funding visible as well.

A withdrawal or conversion can change the income used for coverage costs. I'm checking that against the same coverage year and including a verified assistance repayment or premium effect where it applies.

Each person also needs the correct transition date. Part B enrollment timing and the Part A effective date matter, especially when HSA contributions continue. Entering the expense doesn't enroll anyone, so that outside action stays pending until coverage is confirmed. Once the dates and costs agree, we can use them in the retirement funding comparison.

**Overlay:**

Cue “complete annual cost” → Premium + ordinary costs; cue “same coverage year” → Income and coverage use one estimate.

**Verify:**

Healthcare is neither omitted nor duplicated, transitions are person-specific, retained risk is funded and subsidy/premium omissions are explicit.

**Capture dependency:**

Supported expense/life-event timing, coverage calculation scope, actual quotes, Marketplace/Medicare income treatment and enrollment/HSA confirmation.

### Chapter 4 — Choose the account and investment supplying cash — after 6.1

[Clean teleprompter take](teleprompter/walkthrough/W06-04.txt)

**Show:**

Open Plan → Retirement strategy → How retirement is funded. Compare supported account order/blend in Current/Preview, then open the same year’s account and asset-sale rows. Show required distributions before discretionary order.

**Narration:**

We know the year's cash need. Now let's follow the money that supplies it. I'm opening How retirement is funded in Retirement strategy and tracing the first year's withdrawal to its account.

Inside that account, we also need to see the investment being sold and the tax created. Choosing an account order doesn't, by itself, tell us which investment supplies the cash.

Required distributions have their own rules, so those remain accounted for. For the remaining spending, we can preview another account order or blend when it addresses an actual tax or access need.

I'm keeping the lifestyle and return assumptions steady while reading cash available for bills, tax paid and balances remaining. Then we'll open a later year to see the effect of that choice over time. If there's also a conversion, it still needs separate spending and tax sources.

If the preferred order runs out of accessible money, we have a source or spending decision left to resolve. Once the funding works and we intend to use it, we can save the choice and read the same year again to confirm the plan reflects it.

**Overlay:**

Cue “the investment being sold” → Account order ≠ asset sale order; cue “cash available for bills” → After-tax spending cash.

**Verify:**

Funding, RMDs, asset sales, conversion and taxes reconcile to the same year and save receipt; no unsupported universal order is staged.

**Capture dependency:**

Supported account-order/blend and asset-sale controls, access conditions, RMD rules, Current/Preview calculation and saved policy/year detail parity.

### Chapter 5 — Use the Reserve through a difficult sequence — after 6.8

[Clean teleprompter take](teleprompter/walkthrough/W06-05.txt)

**Show:**

Use separate sequence arithmetic graphic, then actual retirement Reserve assignment, spending-gap basis, target/floor and supported use/refill behavior. The $52,700/$26,350/$45,000 figures remain a labeled separate teaching case unless explicitly loaded as an extension.

**Narration:**

Let's see how the Reserve helps when returns arrive in an unpleasant order. We're starting with the income already covering retirement spending, then looking at the remaining gap and any separate bills assigned to cash.

In the separate illustration, $1 million with $50,000 beginning-year withdrawals ends at $887,500 after a 20% loss and a 25% gain. Reverse those returns and it ends at $910,000. The same returns leave different amounts because assets were sold for spending along the way. A later recovery can't grow the units we've already sold.

Now I'm opening a weak year in the actual plan. We'll follow the cash used, the Reserve left and the proposed refill. Before it reaches the chosen floor, we need to know where that refill comes from, including sale tax and fees.

If the same money is promised to another payment, it isn't available here too. And if recovery takes longer, the response still needs a funding source. Once we can follow that sequence, the Reserve amount has a practical meaning: we know what it pays and what we'll do as it runs down.

**Overlay:**

Cue “The same returns leave different amounts” → Same returns, different spending path; cue “Before it reaches the chosen floor” → Floor → funded response.

**Verify:**

Reserve is an existing-asset role, gap excludes counted income/tax appropriately, floor is finite and use/refill money is assigned once.

**Capture dependency:**

Canonical Reserve source reader/writer, target/floor basis, modeled refill cadence, funded source/tax and actual weak-year result.

### Chapter 6 — Compare sale, other assets and borrowing — after 6.6

[Clean teleprompter take](teleprompter/walkthrough/W06-06.txt)

**Show:**

Open relevant Current/Preview retirement funding policy; a one-off possible loan stays in Scenarios, and real loans remain Debt. Read the supported assumptions receipt, plan effect and risk added through a weak year and repayment.

**Narration:**

We're comparing ways to fund the same spending on the same date. I'll start with selling, so we can see the tax, cash available and Bitcoin remaining. Then we'll look at another available asset and what that money would otherwise have funded.

Borrowing adds another set of obligations. Here are the terms and funding rules: how interest is handled, what collateral is required, what resources could respond to a problem and how the loan ends.

In the simple illustration, a $20,000 loan at 10% uses $2,000 of cash interest or becomes $22,000 of debt after one year. The actual comparison needs its own modeled terms. A small annual payment doesn't tell us whether the eventual repayment is affordable.

I'm opening a weak period and the repayment year to follow the payment source, lender-specific collateral exposure, any top-up and any sale used to repay. Those risks belong beside the change in the plan result.

The Reeds have no current Bitcoin-backed loan. If we choose ongoing borrowing as part of retirement funding, we save that policy in Retirement strategy. An unchosen one-time loan stays in its scenario. Before relying on a real loan, the separate loan lesson takes us through the actual contract and response resources.

**Overlay:**

Cue “the same spending on the same date” → Equal net spending; cue “beside the change in the plan result” → Plan effect + risk added.

**Verify:**

No new actual loan is created from a scenario; interest/debt/collateral/repayment, fallback and net-spending comparison remain consistent. Unmodeled terms are explicit.

**Capture dependency:**

Accepted borrowing parity: rate path, paid/accrued interest, caps, top-up/release, liquidation, closeout, fallback, collateral availability, Current/Preview and saved-policy evidence.

### Chapter 7 — Test one decision and read its cause — after 6.8, using 1.5 result literacy

[Clean teleprompter take](teleprompter/walkthrough/W06-07.txt)

**Show:**

Show Current versus one supported spending/work-date/funding change. Read actual percentage/count/horizon/freshness and affected year, using same assumptions except named decision. No illustrative percentage overlays on live result.

**Narration:**

We've found the part of the plan that needs work. Let's test one decision that could address it: spending less, changing the work date or using a different funding source. I'll keep the other assumptions unchanged so we can see what this decision does.

Here's the chance of success, with the matching simulation count and the years it covers. Now I'm opening the year that explains the difference. The percentage matters, but so does what we would actually have to do: live on less, work longer or take on a different funding obligation.

If we find a missing fact, correcting it may make the result less comfortable. We need to use that corrected picture. Raising return assumptions to recover the old percentage would hide the problem we're trying to solve.

Once the household is willing to follow a change, we can save it and confirm that the updated result uses it. If we prefer Current, we leave the comparison unapplied. The next step is to turn that chosen plan into this year's spending and Reserve decision.

**Overlay:**

Cue “test one decision” → One changed input; cue “the year that explains the difference” → Result → funding year → household trade-off.

**Verify:**

Percent/count share the same run; chosen and earliest dates stay separate; preview does not alter saved facts/strategy before Save.

**Capture dependency:**

Approved full-result standard, matching receipt/horizon, Current/Preview isolation, same seeded comparison path where supported and saved-result readback.

### Chapter 8 — Save annual spending and the refill decision — after 6.8

[Clean teleprompter take](teleprompter/walkthrough/W06-08.txt)

**Show:**

Open standing Spending guardrails and then separate annual review. Use approved actual dollar thresholds only after inverse-calculation proof. Show the exact accepted $103,000/55%/$86,000 → $92,700 arithmetic as a clearly separate illustrative graphic. Preview and save the actual selected spending and refill decision.

**Narration:**

Let's bring the review back to the amount the household will spend. I'm looking at the standing guardrail status first, then the annual spending review. The portfolio threshold tells us when to review. The budget proposal tells us what spending we're considering.

We start with the saved budget and apply inflation once. In this separate illustration, $100,000 becomes $103,000. A made-up 55% result crosses the lower trigger, and the made-up amount that would reach the target is $86,000. The 10% correction cap gives us $92,700 for this review. The cap hasn't restored 80% confidence, so we still need to read the difficult years before adopting that amount.

The household then has to identify the expenses that would actually change. Those choices also change the Reserve calculation. With $40,000 of spendable income and withdrawal tax funded separately, the example's remaining gap is $52,700. Its chosen twelve-month target is $52,700, its six-month floor is $26,350, and $45,000 of cash leaves a $7,700 refill gap.

I'm putting the actual refill source and its tax beside the proposed budget. Once those agree, we can save the spending we choose, read the saved amount and set the next review. An urgent income or loan change needs attention sooner. This gives us a decision we can follow for the coming year, and next we'll work on keeping the assets and access behind that plan secure.

**Overlay:**

Cue “this separate illustration” → Hypothetical, not app output; cue “The cap hasn't restored” → $92,700 suggestion ≠ 80% restored; cue “Those choices also change the Reserve calculation.” → Spend / income / Reserve / refill agree.

**Verify:**

Standing levels and budget remain distinct; annual inflation/cap applies once, saved choice preserves planned retirement date, and Reserve/refill/tax use the same adopted state.

**Capture dependency:**

Dollar-threshold inverse solver and denominator, unsolvable-threshold handling, exact 60/80/95 policy and annual cap/inflation semantics, annual-review Current/Preview, canonical spending/Reserve save and receipt parity.

## W07 — [Document the custody choice and actual recovery status](scripts/working/W07_document-the-custody-choice-and-actual-recovery-status.md)

### Chapter 1 — Choose custody for the household job

[Clean teleprompter take](teleprompter/walkthrough/W07-01.txt)

**Show:**

After 7.1, open Protect → Bitcoin access beside the existing Family Custody Map. Select each fictional holding, identify owner and purpose, and record the current arrangement, intended direction and one responsible person. Use Trusted people for the agreed contact rather than creating another contact record.

**Narration:**

We're in Bitcoin access, where we're connecting the custody decision to the actual holdings. The Reeds have directly held Bitcoin, professionally custodied Bitcoin and a Bitcoin ETF in a Roth IRA. Each has its own owner and access process, so we'll work through them separately.

For this holding, we're recording what the money is for and who controls it today. If you're considering a move, that belongs beside the current arrangement as a planned change. We don't want the family reading a future intention as something that's already happened.

The next part is who handles the ordinary work and who has agreed to help if that person is unavailable. An unanswered provider question can stay as the next action here. Once we save and reopen the record, we can check that it still points to the right holding. This is a map of the process, so recovery words and precise secret locations stay in their protected records.

**Overlay:**

Holding / owner / current method / intended change / agreed person

**Verify:**

Saved record belongs to the correct holding; responsibility was actually agreed or is explicitly pending. No invented Reed contact, provider right, insurance or completed transfer.

**Capture dependency:**

Verify Protect's Bitcoin access and Trusted people fields, ownership context, save/reopen behavior and the external map reference on the filming build. If a needed field is absent, show that part in the existing map without simulating an app control.

### Chapter 2 — Record actual recovery evidence

[Clean teleprompter take](teleprompter/walkthrough/W07-02.txt)

**Show:**

After 7.2 and the applicable D07 test, open the actual non-secret test receipt. Show separate rows for the isolated test wallet and each funded setup. Record only the date, method, scope and actual outcome.

**Narration:**

Before we update recovery status, let's look at the evidence we're using. The receipt needs to tell us which wallet was checked, how it was checked, when it happened and what the result was.

That scope matters here. If the receipt is from the separate test wallet, we're recording a result for that wallet. The family's funded wallet keeps its own status until its appropriate safe check is complete. Buying a new device or checking that a word list is valid wouldn't establish the full recovery result.

Where a funded setup has been safely checked, we can record the evidence that actually exists, including any passphrase or multisig requirements covered by the check. When we read the saved entry back, someone else needs to understand both what's been tested and what's left to do. They don't need any recovery material to understand that.

**Overlay:**

Test setup ≠ funded setup / method / date / actual result

**Verify:**

Each status is scoped to actual evidence. No default Tested flag, secrets, descriptors, xpubs or hardware purchase treated as recovery.

**Capture dependency:**

Verify the precise Protect recovery fields and actual D07 or funded-wallet evidence. Device-specific verification remains separate; absent evidence must render pending.

### Chapter 3 — Fix one important account or shared-dependency gap

[Clean teleprompter take](teleprompter/walkthrough/W07-03.txt)

**Show:**

After 7.1 and 7.2, use the existing map to identify one shared recovery email, provider or operator. On an authorized example account only, show a supported security change and legitimate backup-access check. Keep all authentication secrets off capture.

**Narration:**

Let's work on one dependency from the custody map. In this example, several accounts rely on the same recovery email. That gives us a useful place to start: protecting that email affects the access route for more than one account.

We're using the provider's verified security settings to see which sign-in and recovery methods it supports. Where a security key or passkey is available, that's the option we're looking at first. Before removing working access, we need the backup method set up and tested. Passwords, recovery codes and private setup screens stay out of the recording.

Back in the map, we'll record the change only once it's actually completed. A provider question or an agreement we're still waiting for stays open. This improves account access, but the company's custody risk is still there, so that dependency remains in the map.

**Overlay:**

Shared dependency → supported change → backup-access check → actual status

**Verify:**

Actual confirmation exists for completed changes; pending work remains pending. No live client credentials, sensitive identifiers or claimed provider solvency.

**Capture dependency:**

Verify the chosen provider's current authentication and recovery controls on an authorized example account. No universal passkey, withdrawal allowlist or provider-independent recovery claim.

### Chapter 4 — Finish the family starting map

[Clean teleprompter take](teleprompter/walkthrough/W07-04.txt)

**Show:**

Prepare the non-secret custody entries for W08. With an agreed helper, rehearse the first contact and backup contact while the usual operator stays silent. Correct and repeat only an unclear first step.

**Narration:**

The last thing we need from this map is a usable starting point for the family. Let's read the instruction for this holding: who would they contact, and which legitimate process applies if the usual operator is unavailable?

The person who agreed to help can try those first steps while the operator stays quiet. We're looking for whether they can find the first contact and the backup. This rehearsal doesn't involve entering credentials or moving money.

If an instruction stops them, that's the part to correct and try again. If we haven't rehearsed it yet, we'll leave that status pending. We'll take this same map into the family handoff, where the access process connects to the person's authority. And just to keep the two kinds of backup clear: an Orange Plan data backup doesn't restore a Bitcoin wallet.

**Overlay:**

First contact / backup / unclear step / actual rehearsal date

**Verify:**

Actual rehearsal result or honest pending status; agreed contacts; no transfer, impersonation, guessed credentials, secret storage or inferred legal authority.

**Capture dependency:**

Verify supported Protect map/packet outputs separately from financial-data export and restoration. Confirm helper consent and actual rehearsal evidence before showing success.

## D07 — [Prove a wallet backup with a safe test setup](scripts/working/D07_prove-a-wallet-backup-with-a-safe-test-setup.md)

### Chapter 1 — Identify the isolated practice setup

[Clean teleprompter take](teleprompter/walkthrough/D07-01.txt)

**Show:**

After 7.2, show only the non-secret equipment and the exact official procedure. Confirm the device is for a newly created isolated wallet, with no household savings. Record the verified model/firmware/software/backup format in the production receipt.

**Narration:**

In this demonstration, we're checking recovery with a new, isolated test wallet. The device and small amount are set aside for this purpose. The wallet holding the family's savings stays out of the procedure.

Before we begin, let's match the equipment to the official instructions for this exact model, software and backup format. A process for another device may have different requirements. Unexpected or prewritten recovery words are a reason to stop; we need a fresh wallet created through the verified process.

The question this test can answer is whether we can recover and use this wallet through this procedure. It won't verify a different wallet holding the family's Bitcoin. Keeping that scope clear now will help us record an accurate result at the end.

**Overlay:**

New isolated test wallet / exact model + format / no household savings

**Verify:**

Authenticity and current instructions match equipment; no prewritten secret, funded wallet, assumed word count or universal reset sequence. Record reviewer and URL/date.

**Capture dependency:**

Select and independently review the actual device-specific procedure, including test scope and authorized amounts. No model, firmware, backup format or compatible spare is supplied by the manuscript.

### Chapter 2 — Create the test wallet off camera where secrets appear

[Clean teleprompter take](teleprompter/walkthrough/D07-02.txt)

**Show:**

Follow the verified new-wallet procedure. Stop every camera, screen recorder and intermediate capture before secret generation, display, recording or entry. Record recovery material through the approved offline process. Resume only on a non-secret screen.

**Narration:**

We're at the point where the new wallet creates private recovery information. Before any of that appears, the camera and screen recording need to stop. The recovery words, private keys and any passphrase belong in the private offline process, including while they're being recorded or entered.

The wallet is generated through the trusted device process in the official instructions. A secret from a tutorial or prewritten recovery material would give someone else a way to control it, so neither belongs in this setup.

Once the secret screens are closed, we can resume on a non-secret screen. That lets us continue explaining the test without putting the material that controls the wallet into the footage. A later blur wouldn't remove it from the original recording.

**Overlay:**

Capture stopped during secret generation and entry

**Verify:**

No usable secret or sensitive recovery configuration exists in raw, intermediate or published recordings. A later blur does not satisfy this check.

**Capture dependency:**

Verify which exact screens expose secrets and how all capture devices are stopped. Independently inspect raw footage before retaining or distributing it.

### Chapter 3 — Explain the recovery requirements

[Clean teleprompter take](teleprompter/walkthrough/D07-03.txt)

**Show:**

Use generic labels beside the exact reviewed backup format. Distinguish device PIN, backup, any passphrase and, only for an independently reviewed applicable setup, multisig keys/configuration. Show no actual values.

**Narration:**

Before the recovery check, let's be clear about what each piece does. The PIN unlocks the device. The backup recreates the corresponding keys. If this wallet uses a passphrase, the exact passphrase selects the intended wallet.

Those different jobs explain why one piece can't simply replace another. Knowing the PIN doesn't replace a missing backup. And a correct word list doesn't prove that we've recovered a passphrase wallet; we still need the exact passphrase and the intended-wallet check.

Multisig has additional independent-key and configuration requirements, which need the complete reviewed procedure for that arrangement. Here we're covering only the requirements recorded for this test wallet. These labels explain the pieces without showing their private values.

**Overlay:**

PIN: device access / backup: keys / passphrase: intended wallet

**Verify:**

Requirements match actual standard; no universal 12/24-word assumption, secret split or multisig inference. Configurations and extended keys remain sensitive.

**Capture dependency:**

Verify exact supported backup and passphrase behavior, compatible restoration tools and any separately scoped multisig procedure.

### Chapter 4 — Receive a small authorized test amount

[Clean teleprompter take](teleprompter/walkthrough/D07-04.txt)

**Show:**

Verify the receive destination using the actual trusted-device process. Perform only the explicitly authorized trivial inbound transfer. Wait for the appropriate actual confirmation; keep unnecessary addresses and identifiers off capture.

**Narration:**

Now we're giving this test wallet a small, known amount that we can look for after recovery. In the receive process, we'll verify the destination through the trusted device, rather than relying only on the computer display. The network and amount also need to match the transfer authorized for this test.

After the transfer, we need the required actual confirmation before continuing. We'll keep that receipt and a non-secret way to recognize the intended wallet for the recovery comparison.

If the destination or received amount is unexpected, this is where we stop and investigate. Adding meaningful funds wouldn't resolve that uncertainty. The test stays limited to the small amount set aside for it.

**Overlay:**

Verify destination + network + authorized test amount

**Verify:**

Actual destination, network, amount and confirmation agree. No implied authority to transfer household savings or unrelated funds.

**Capture dependency:**

Confirm inbound-transfer authorization, current receive-verification procedure and required confirmation standard for the selected setup.

### Chapter 5 — Check the backup before any destructive step

[Clean teleprompter take](teleprompter/walkthrough/D07-05.txt)

**Show:**

Use the supported non-destructive backup check, or a safely prepared compatible spare process, first. Preserve the working source. All secret-entry capture remains stopped. Stop on any failure or mismatch.

**Narration:**

Before any destructive step, we need to know that the backup can support the recovery. We're keeping the working device intact while we use its official backup-check process. If the reviewed procedure uses a compatible spare, the original remains available while we check it.

The check includes any passphrase or configuration requirements for this wallet. Recording stops before private information is entered, just as it did during setup.

If the check fails, we stop here and preserve the working access. Verified official instructions or support may help us investigate, but support doesn't need the secret. Resetting the device or sending more funds would add risk while the mismatch is still unresolved. A successful, supported check is what lets us consider the next part of this isolated test.

**Overlay:**

Working access intact / failed check: stop

**Verify:**

No reset after failed check; no meaningful funds added; no secret shared with support. A supported safe check must justify the next step.

**Capture dependency:**

Verify the actual non-destructive or spare-device procedure and failure handling. If unsupported or unclear, keep the test stopped rather than inventing menu steps.

### Chapter 6 — Recover the intended wallet within the reviewed test

[Clean teleprompter take](teleprompter/walkthrough/D07-06.txt)

**Show:**

Perform the reviewed recovery on a compatible spare or, only if expressly part of the isolated test procedure, reset/restore the test device. Never wipe the funded primary wallet. Stop all capture during secret entry. Compare known wallet evidence and test funds afterward.

**Narration:**

We're now using the recovery method specified for this isolated test. All private entry stays off camera. When the wallet opens, we'll compare its known identifier or address with our test record, then check for the expected test funds.

Both parts matter. A valid empty wallet isn't enough, because a passphrase mistake can open another valid wallet. If the identity or funds don't match, we'll stop and leave the result unresolved.

Successful recovery means the evidence matches this intended test wallet. It doesn't tell us that another wallet is recoverable. The family's funded wallet stays outside the test, and we never wipe it as part of this demonstration.

**Overlay:**

Intended wallet identity + expected test funds

**Verify:**

Actual identity and funds match or status is failed/pending. No funded wallet wipe, universal recovery sequence or troubleshooting through meaningful transfers.

**Capture dependency:**

Verify exact restore compatibility, trusted identifier check and authorized isolated reset if applicable. Device steps remain blocked until that procedure is reviewed.

### Chapter 7 — Verify controlled spending and the fee

[Clean teleprompter take](teleprompter/walkthrough/D07-07.txt)

**Show:**

Review a separately authorized trivial outbound transaction using the recovered test setup and current trusted-device procedure. Read destination, amount and actual fee. Confirm only within the authorized test and wait for actual evidence.

**Narration:**

Seeing the expected balance is useful, but we also want to know whether the recovered setup can authorize a payment. That's the purpose of the small outbound transaction separately authorized for this test.

Before confirming, we'll check the destination, amount and fee through the trusted device. If any detail differs from the intended transaction, we stop. The fee we use is the actual fee shown for this transaction; there's no universal fee or minimum-output amount to copy from a video.

Once the payment has the required confirmation, we'll keep that evidence with the test record. That lets us distinguish seeing funds from demonstrating controlled spending through the recovered setup.

**Overlay:**

Destination / amount / actual fee / actual confirmation

**Verify:**

Explicit outbound authorization, reviewed procedure and actual confirmation. No secret exposure, needless address publication, fee guarantee or implied household transaction authority.

**Capture dependency:**

Verify current spending workflow, authorized destination/amount, fee display and confirmation evidence for the chosen test setup.

### Chapter 8 — Record what was proved and what was not

[Clean teleprompter take](teleprompter/walkthrough/D07-08.txt)

**Show:**

Complete the non-secret test receipt with setup, exact method, date, actual outcome and limitations. Independently inspect all raw/intermediate/output footage for secrets. Hand only the scoped status to W07 chapter 2.

**Narration:**

Let's finish by recording exactly what this test showed. The receipt identifies the wallet, the recovery method, the date and the actual outcome. We'll include the receive, recovery and spending checks that completed, with anything unfinished left unresolved.

That receipt stays separate from the status of a different funded wallet. The funded wallet needs its own appropriate safe verification, even when this practice test succeeds.

In Bitcoin access, we can now record the scoped result and the next action without storing the recovery material. An Orange Plan data backup concerns plan information; it doesn't recover Bitcoin signing keys. We'll take this receipt into the custody walkthrough so the family can see what's been checked and what still needs attention.

**Overlay:**

This setup / this method / actual outcome / remaining work

**Verify:**

Independent secret-free raw/output review and truthful test scope. No manufacturer endorsement, blanket recovery certification or funded-wallet claim.

**Capture dependency:**

Obtain actual hardware evidence, independent security review and exact safe record fields before footage release. No capture approval or learner completion is established by this manuscript.

## W08 — [Build and rehearse the family handoff](scripts/working/W08_build-and-rehearse-the-family-handoff.md)

### Chapter 1 — Connect people, documents and beneficiaries

[Clean teleprompter take](teleprompter/walkthrough/W08-01.txt)

**Show:**

After 8.1, open Protect → Trusted people, Estate documents and Who receives what. Compare the existing household role/document inventory with actual signed-document and provider-beneficiary evidence. Show agreed, proposed, executed and unresolved states separately.

**Narration:**

We're starting with the people because the documents need to support the jobs those people may have to do. In Trusted people, we'll identify the person for financial matters, the person for healthcare and the intended estate representative, along with who has agreed and who can be the backup.

Now we can connect each role to Estate documents. A name in this record isn't a legal appointment. For a financial power of attorney, we're checking that it's durable, meaning its authority can continue if you're incapacitated. We also need to know when it takes effect and which powers it actually grants.

Who receives what gives us another comparison to make with the institution's own beneficiary record. The primary beneficiary is the first person designated. The contingent beneficiary is the backup who receives if the primary can't under the account's rules. If that record differs from what you intend, the provider or document update remains an open action. We'll save the status the evidence supports.

**Overlay:**

Agreed person / authority / document status / provider beneficiary record

**Verify:**

No nominated executor treated as appointed, draft as executed, trusted contact as withdrawal authority or proposed beneficiary as filed. P11 durability/effective scope preserved.

**Capture dependency:**

Verify actual Protect fields and owner scope. Applicable law, signed documents and provider acceptance establish authority; this recording does not supply a legal instrument.

### Chapter 2 — Connect authority to practical access

[Clean teleprompter take](teleprompter/walkthrough/W08-02.txt)

**Show:**

After 8.1 or relevant A8.1 work, open Bitcoin access and the existing ownership map. Trace direct Bitcoin, professional custody and retirement-account exposure for incapacity and death separately. Review immediate legally available household cash.

**Narration:**

Now that we have the people and authority, let's follow one asset through the access process. The owner, the person authorized for this situation and the process that person uses all need to connect.

Direct Bitcoin requires a lawful route to the protected recovery process. Professionally held Bitcoin has the provider's family-access requirements. A retirement account has its beneficiary and distribution process. Telling someone to use the owner's login doesn't establish the authority or give them the proper route.

We'll look at incapacity and death separately because the authorized person and process can change. While that longer process is underway, the household still needs to pay essential bills. So we're also identifying cash that's legally available at that time. If authority, access or immediate cash is missing, that's the specific next action we'll carry forward.

**Overlay:**

Owner → authorized role → access process / immediate bills

**Verify:**

Lawful authority and technical access remain distinct. Cash availability is confirmed rather than assumed. No universal seed/passphrase split or inferred trust funding.

**Capture dependency:**

Verify provider procedures, supported Bitcoin access fields and the actual household documents. Keep unavailable or legally unresolved access explicit.

### Chapter 3 — Write and rehearse the first-page handoff

[Clean teleprompter take](teleprompter/walkthrough/W08-03.txt)

**Show:**

Open Instructions for your family and the existing Heir Letter. Connect the safe first instructions to the Family Custody Map and Plan packet/Executor Packet. Use the editorial sample paragraph as a labeled example; rehearse with an agreed helper.

**Narration:**

This is the page someone may read when they're already under a lot of stress. In Instructions for your family, we're keeping the opening straightforward: the first person to contact, how to verify that contact and where to start with household payments. The supporting account and document references can sit in the packet.

Let's read that first paragraph as the family would read it. Any wallet secret, password or exact secret-storage location belongs in its protected process. We'll date these instructions and identify who keeps them current so the family can tell what they're looking at.

Then we'll try the first steps with the person who agreed to help. Can they find the letter, reach the first contact information and find the backup without asking the usual operator? If something stops them, we'll correct that instruction and repeat that part. The actual rehearsal result tells us more than the fact that we've written a letter.

**Overlay:**

Find letter → first contact → backup contact → repair missing instruction

**Verify:**

Actual finding/opening and rehearsal evidence before success status. No sensitive recovery configuration or unperformed legal review. Sharing is for the agreed household purpose.

**Capture dependency:**

Verify editor/save behavior, Plan packet output and permitted references to existing protected records. Confirm actual helper consent and document accessibility.

### Chapter 4 — Verify the communication backstop

[Clean teleprompter take](teleprompter/walkthrough/W08-04.txt)

**Show:**

If no check-in service is used, show the findable family instructions and backup contact, then continue to chapter 5. Otherwise, open Check-in plan only after the filming build proves its actual capability. Read timing, recipient, cancellation and false-alarm behavior. Send only a separately agreed harmless test to an authorized recipient, or demonstrate the existing external service as external.

**Narration:**

A check-in service is optional. If you don't use one, the family still needs findable instructions and a backup contact; you can continue to the insurance review from there.

If you do use a service, let's look at the arrangement you actually have. Its timing, recipient, message and false-alarm process determine how useful it will be. We're checking how to cancel or correct a message as well as how it's triggered.

The way to check delivery is a harmless test agreed with the recipient beforehand. The message needs to say it's a test and contain no recovery secrets. Then we can see whether it arrives and whether the recipient can open the safe instructions.

Until that happens, delivery stays unverified and the test remains an action. Even after it works, we'll keep another way for the family to reach the instructions if the service is unavailable.

**Overlay:**

Actual timing / agreed recipient / harmless test / delivery / fallback

**Verify:**

No assumed 90-day interval, delivery guarantee, false emergency, automatic key release or unsolicited message. An unavailable capability remains a production dependency.

**Capture dependency:**

Verify Check-in plan enablement, scheduling, consent, cancellation and real delivery on the capture build. Do not simulate an unshipped service or perform a real emergency trigger.

### Chapter 5 — Complete the risk and insurance decision

[Clean teleprompter take](teleprompter/walkthrough/W08-05.txt)

**Show:**

After 8.4, use the existing insurance audit beside redacted policy evidence. Work one risk from needs through accessible resources and actual benefits. Show the accepted hypothetical arithmetic only as illustration; update premiums and future costs through Cash Flow or Life events as applicable.

**Narration:**

For the insurance review, we'll take one event at a time. In the audit, we're comparing what the household would need to cover with the resources and policy benefits actually available for that event.

The life-coverage illustration gives us a simple example. A ten-year shortfall of $400,000 in today's dollars, less $100,000 that's separately available and $200,000 of coverage, leaves $100,000 to investigate. That calculation assumes zero return after inflation, taxes and fees, with later needs funded separately. Those assumptions stay beside the number.

Your own policy gives us the benefit, term, waiting period and exclusions to work from. Once we see the uncovered amount, we can record whether you intend to carry that risk or investigate a change. Related premiums belong in Cash Flow, and an expected future cost belongs in Life events where applicable. The policy change itself happens with the provider; we'll record its effective date once it's real, keeping needed protection until any replacement is approved and active.

**Overlay:**

Illustration: $400k need − $100k assets − $200k coverage = $100k gap

**Verify:**

Actual benefits, needs and resources stay distinct; no invented insurance solver, quote, adopted Reed policy or coverage cancellation. Necessary replacement must be active before recording old protection as safely removed.

**Capture dependency:**

Verify applicable Cash Flow/Life event fields and current policy evidence. Qualified review is specific to unresolved terms or the chosen transaction; no blanket attorney gate.

## W09 — [Complete a monthly review and an annual review](scripts/working/W09_complete-a-monthly-review-and-an-annual-review.md)

### Chapter 1 — Complete a quiet monthly review

[Clean teleprompter take](teleprompter/walkthrough/W09-01.txt)

**Show:**

From 9.1's monthly route, open Home. Read material issues, source dates, Your Money and any meaningful Recent Activity. Open the relevant account's How this account updates. Check Cash Flow's Your Plan uses, Reserve and confirmed upcoming Life events. Finish a genuinely quiet fixture without inventing an action.

**Narration:**

For an ordinary monthly check, Home is our starting point. Before interpreting a balance, let's look at its date. If an account needs attention, How this account updates tells us what's automatic and what still needs input. Seeing a provider's name doesn't tell us that its purchase history came through.

Then we're comparing this month's records with what we expected to happen. Did the contribution arrive, and was it invested as intended? In Cash Flow, we'll check the spending source, the cash Reserve and the next confirmed life event so the upcoming cash needs are still represented.

The saved Plan has its own date and status. Prices can be current while its calculation is older, so we need to read the result that belongs to the current inputs. A price move by itself isn't a reason to rewrite the assumptions.

If those records are current and there's no new decision, we're finished with this month's check. We can keep the next reminder and close the plan.

**Overlay:**

Monthly: source dates / expected changes / cash needs / current result

**Verify:**

A quiet outcome is supported by the actual fixture. No forced task, refresh request, repeated strategy change or universal runtime claim. No loan monitoring reduced to monthly cadence.

**Capture dependency:**

Verify Home issue/source state, How this account updates, Cash Flow source period, Reserve and current Plan receipt. Do not invent Recent Activity or a manual Recalculate control.

### Chapter 2 — Resolve one meaningful exception

[Clean teleprompter take](teleprompter/walkthrough/W09-02.txt)

**Show:**

Use the existing contribution-left-in-cash example. Trace the actual account record through contextual Add or update and source evidence. If instruction was never executed, keep the provider action outside the app; if data is wrong, use the supported correction and authoritative receipt. Show uncertain and deferred status honestly.

**Narration:**

Let's follow the contribution that needs attention. In this account, we're comparing the date and amount with the provider's record, then looking for the investment that was supposed to be purchased. The money arriving and the investment being bought are two different things.

If the purchase instruction never completed, that's something to resolve with the provider. Entering a purchase in Orange Plan wouldn't make it happen. If the purchase did happen and the activity is missing here, we can use the account's supported update or import process instead.

Before adding anything, let's read the receipt. The balance and imported activity may already describe the same money, and we don't want a duplicate. After the supported correction, we'll check the affected total.

If we still don't have the evidence, the issue stays open with the missing information identified. Remind me later can give us time to get that answer; it doesn't mean the question has been resolved.

**Overlay:**

Expected contribution → provider evidence → actual purchase or cash → correct action

**Verify:**

No balancing purchase, duplicate import, silent deletion or invented executed trade. Resolved, deferred and uncertain remain distinct. Plan updates only for modeled changes.

**Capture dependency:**

Verify account-context actions, source coverage, history/balance reconciliation and receipt on the filming build. Outside provider instructions and actual execution need separate evidence.

### Chapter 3 — Complete the annual system review

[Clean teleprompter take](teleprompter/walkthrough/W09-03.txt)

**Show:**

From 9.1's annual route, open the previous dated plan and Annual Plan Refresh. On a first review with no previous version, date the current plan and start the record from it. Review six areas using canonical owners: spending/Reserve in Cash Flow and retirement strategy; Portfolio and allocation; Debt; Tax opportunities; Bitcoin access; family documents/beneficiaries/insurance. Use an actual debt-payoff fixture before redirecting a former payment.

**Narration:**

The annual review gives us room to revisit the decisions behind the plan. Last year's dated plan is a useful comparison if you have it. For a first annual review, we'll date the current plan and start the record from here.

There are six areas to work through, starting with spending and the Reserve. If you're retired, the next year's spending and refill need to be considered together in the spending review. If you're working, we're checking whether the target and funding pace still fit.

From there, Portfolio and allocation let us review any changed purpose or timeframe. Debt statements show what remains owed, and the tax review brings up available windows and approaching deadlines. In Protect, we're checking custody, family contacts, beneficiaries, documents and insurance.

Here's how that becomes a real action: if a debt has ended, we'll confirm the payoff before assigning the old payment. Then we can check today's cash needs and choose its destination in Saving and investing. The provider instruction is still a separate step.

We'll record the changes you actually adopt and the outside work still needed. Choices that continue to fit can stay as they are.

**Overlay:**

Annual: spending/Reserve / allocation / debt / tax / custody / family/insurance

**Verify:**

Actual spending policy, input dates and comparison scope preserved. No automatic rebalance, presumed beneficiary sufficiency, destructive annual wallet test or prematurely available payoff money.

**Capture dependency:**

Verify each owner route, Current/Preview spending and contribution flows, actual payoff milestone and supported annual review. Current thresholds and policy terms remain specifically verified, not supplied by the manuscript.

### Chapter 4 — Handle a real change and a proposed response separately

[Clean teleprompter take](teleprompter/walkthrough/W09-04.txt)

**Show:**

From 9.1's immediate-change route, use a labeled fictional income change. Save the fact in Cash Flow → Income at its supported effective timing. Inspect required spending/debt/Reserve, then compare a contribution response in Saving and investing. Reconcile any old future event already reflected in current facts.

**Narration:**

This example is for an income change that's already happened. We're updating the actual source and timing in Income under Cash Flow. Leaving the other facts alone lets us see what this change does.

Now we can compare the new cash flow with the bills, required debt payments and Reserve needs. That gives us the context for a possible contribution change in Saving and investing. The income change is a fact; the new contribution amount is still a choice. Current and Preview let us compare that choice before saving the one you intend to follow.

If we'd already modeled this change as a future event, we also need to reconcile the event so it isn't applied twice. Then we'll wait for the saved result to include the change before reading its effect.

A career break you're only considering stays in Scenarios. And if a number is unexplained, we'll trace its source or ask a focused support question. Changing several other inputs to get the old percentage back would leave the original problem unresolved.

**Overlay:**

Changed fact → cash needs → proposed response → explicit save

**Verify:**

Correct owner and timing; no duplicate event, invented calculation, compensating return override or unadopted preview in Current. Immediate obligations continue while an app issue is investigated.

**Capture dependency:**

Verify Income timing, event lifecycle, Saving and investing Current/Preview, save/update receipts and result freshness. If unsupported, identify the blocked scene rather than claim it completed.

### Chapter 5 — Keep the next review usable

[Clean teleprompter take](teleprompter/walkthrough/W09-05.txt)

**Show:**

Save a dated summary/action record through actual supported views. Open Profile → Data & privacy → Export to inspect available export scope. Keep any sensitive backup separately; restoration is independently verified in a disposable authorized environment, never demonstrated by restoring over the current household plan. Create actual monthly/annual reminders externally if no app scheduler exists.

**Narration:**

We're leaving a short record for the next time you open the plan: the date, what you adopted and why. Any outside action still needed gets a responsible person and a due date. If it depends on something happening first, that condition goes with it.

The export options tell us what we can save. Let's read that scope before saving or sharing the file. A readable summary helps someone understand the plan; a supported restoration backup has a different job. If this export supports restoration, we'll keep it protected and record its actual restoration status separately. A report or data export on its own doesn't establish that the plan can be restored.

We'll also put the monthly and annual reviews on the calendar, with loan thresholds, tax deadlines and important life changes on their own timing. Writing down an intention to create a reminder doesn't create it.

At the next review, this dated record gives us somewhere to start. We can see what changed without rebuilding the reasoning from memory.

**Overlay:**

Dated decisions / actual action status / next reminder / separate protected backup

**Verify:**

Actual save/reopen and export scope; no calendar event inferred from a note, assumed restore capability or sensitive file shared. Superseded instructions remain dated rather than current.

**Capture dependency:**

Verify Profile export labels/formats/privacy and report save path. Restore is not promised by the future contract; any restoration test requires actual supported safe capability and separate evidence.

## W10 — [Read, explain, and save the finished plan](scripts/working/W10_read-explain-and-save-the-finished-plan.md)

### Chapter 1 — Read one coherent saved plan

[Clean teleprompter take](teleprompter/walkthrough/W10-01.txt)

**Show:**

Open Plan → Overview, then Your Plan report. Check the active saved-plan identity, chance-of-success receipt, target date, spending, horizon and assumptions. Keep the existing Household Plan Summary beside the matching report; don't use landing-page figures.

**Narration:**

We're going to read the plan as one connected set of decisions. In Plan Overview, let's first check that this is the saved plan you intend to follow, along with its result date and status. Then we'll open the matching Your Plan report.

The retirement date, spending and planning horizon tell us what we're asking this plan to do. The assumptions and spending policy explain the conditions behind its chance of success. That result is useful, but it doesn't settle every household risk.

Before comparing an improvement, let's read any accuracy issue or missing information. A wrong fact needs correcting first. If the facts are sound and the plan is weaker than you need, we can identify the unfunded period or assumption driving that weakness and choose one response to compare.

We'll keep this same saved plan open as we follow the funding. That way, the attractive result and the details we're relying on belong to the same set of choices.

**Overlay:**

One saved plan / date / spending / horizon / assumptions / limits

**Verify:**

Report and summary reference the same current receipt. No placeholder probability, invented retirement date, landing number or more optimistic assumption described as accuracy improvement.

**Capture dependency:**

Verify actual Your Plan report implementation, source/result identity, stale/pending states and missing-input explanations. Manuscript completion does not establish engine or report parity.

### Chapter 2 — Follow the important funding years

[Clean teleprompter take](teleprompter/walkthrough/W10-02.txt)

**Show:**

From the same result, open How retirement is funded/Retirement strategy and supported year details. Inspect the first retirement year, benefit start, material event and later tax-sensitive transition. Show actual income, complete spending, taxes, withdrawals, source accounts and remaining assets without fabricated attribution.

**Narration:**

This is where we turn the retirement plan into a picture of where the money to live on comes from. Let's start with the first retirement year and follow the money that pays the bills. We're looking at the income arriving, the complete spending need and the amount that has to come from assets. The source accounts, taxes and debt payments help explain that year's full requirement.

Then we'll move to the next important change, perhaps a benefit starting or a major planned expense. The account paying for it needs to be accessible at that time. We also need to check that we've left enough for the other jobs assigned to those assets.

The Reserve and spending-response rules tell us how the plan responds if things weaken. As we read them, we're looking at what would change and what resources would remain afterward.

If an account's access rule or a funding source is unresolved, we'll leave that gap visible and identify the next step to resolve it. The headline result can't supply evidence that we don't yet have.

**Overlay:**

Critical year: income / complete spending / taxes / source / remaining resources

**Verify:**

Actual supported output and source attribution only. No invented account access, future benefit, dividend, loan payoff or result. Blocking uncertainty stays visible.

**Capture dependency:**

Verify year-level outputs, tax inclusion, withdrawal source attribution and policy links on the capture build. Pause a scene if the current output cannot support its claim.

### Chapter 3 — Finish the plan and share only when useful

[Clean teleprompter take](teleprompter/walkthrough/W10-03.txt)

**Show:**

Review current cash flow/contributions, the selected spending state and the next real action in the same saved plan. Use existing Household Plan Summary only for useful household sharing. Trace an actual question to its owner rather than creating another scenario for completion.

**Narration:**

Now let's connect the long-term plan to the next month of implementation. We need to see where the contribution goes, what it buys, and how it fits alongside the Reserve transfer and any extra debt payment in the same cash flow.

The Reeds show why the timing matters. Their $500 current amount and $1,700 spending-reduction comparison come from different spending choices. The extra $1,605 from ending card payments is future money. We need the same consistency in your plan before assigning a dollar to its next job.

From here, we'll read the next real action and what would show that it's complete. If you share household decisions, the summary can help you explain the spending, investment mix and first retirement funding period. The calculations can stay in the app; share what's useful for that conversation.

You don't need to prepare a separate presentation to finish this. Any unresolved decision takes us back to the part of the plan where it can actually be addressed.

**Overlay:**

Use one spending state / future payoff money stays future / next real action

**Verify:**

No mixed cash-flow states or requirement to copy Reed choices. Household sharing optional; no invented learner outcome, submission or instructor approval.

**Capture dependency:**

Verify current chosen cash-flow state and actual contribution owner. Capture only the matching summary and saved result; real outside implementation remains separate.

### Chapter 4 — Prepare the specific professional handoffs

[Clean teleprompter take](teleprompter/walkthrough/W10-04.txt)

**Show:**

For an actual open issue only, prepare the existing focused CPA, estate, coverage or lending packet. Include decision, relevant evidence, exact question and deadline. Inspect any exported fields before saving for a recipient; no message is sent by this manuscript.

**Narration:**

If one of your open decisions needs outside help, we can make that conversation more useful now. We're starting with the decision you're considering and the specific question that blocks it, then adding the relevant records and deadline.

For a tax question, those records might be the income, account and purchase details behind the proposed transaction. For estate access, they might be ownership, authority and the provider's requirements. Neither packet needs recovery secrets.

Before sharing an export, let's read what it includes and remove information unrelated to the question. The status also needs to reflect where we are: prepared until it's sent, and awaiting an answer until the answer arrives. The packet helps someone review the question; preparing it doesn't complete the transaction or give us the professional answer.

If there's no decision that needs that help, there's no extra packet to create here. We can continue to saving the plan and its actual next steps.

**Overlay:**

Decision / relevant evidence / exact question / deadline / actual status

**Verify:**

No automatic message, appointment, filing, legal approval or professional response inferred. No general full-backup sharing or sensitive custody material.

**Capture dependency:**

Verify export content/privacy, intended recipient and actual question. A professional prerequisite applies to the dependent decision, not every course action.

### Chapter 5 — Save the operating plan and implementation record

[Clean teleprompter take](teleprompter/walkthrough/W10-05.txt)

**Show:**

Save/reopen the dated report and existing Household Plan Summary/action list through supported paths. Record adopted choices, unresolved blockers, confirmed outside actions and conditional future tasks. Inspect Profile → Data & privacy → Export; keep a protected backup only within verified scope. Record actual calendar reminders separately.

**Narration:**

The dated plan and its action record belong together. As we save them, we'll distinguish a choice you've made from an action that's happened. A provider confirmation, an investment purchase or a signed and effective document gives us evidence of completion. Planned work keeps its own status.

Future actions need their conditions too. If a transfer depends on a loan payment ending, it starts after that payment ends. Recording who will change the instruction and how they'll confirm it makes that future step easier to follow.

We'll keep the monthly and annual reminders, with urgent monitoring on its own schedule. If the product supports an appropriate restoration backup, it needs protected storage and an explicit restoration status. A report isn't automatically that backup.

The last thing to leave visible is your next real action and any question still blocking a major decision. When you come back for a review, this dated record lets you pick up from the plan you're actually following.

**Overlay:**

Saved choices / completed actions / open blockers / future triggers / next review

**Verify:**

Actual save/reopen, export scope and outside evidence. No restore guarantee, video-watched equals implemented plan, arbitrary task quota or invented release approval.

**Capture dependency:**

Verify report and Profile export behavior, backup scope and safe restoration separately. Calendar and provider execution need actual evidence; no restore over the member's live plan.
