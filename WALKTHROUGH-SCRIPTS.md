# Separate walkthrough recording scripts

These are future-design scripts, prepared against PR #227. Capture each chapter separately after its screen/procedure is verified. Only each Narration block is spoken. The clean files linked below exclude directions, overlays and verification notes.

## W01 — [Build the first working plan](scripts/working/W01_build-the-first-working-plan.md)

### Chapter 1 — Find the first task · after 0.1

[Clean teleprompter take](teleprompter/walkthrough/W01-01.txt)

**Show:**

Open the intended Home → Your Plan entry, then Plan → Build & improve. Point to the next incomplete source record. Show the four destinations only as orientation. Use a separate three-line card for the existing mortgage, expected college support and possible renovation.

**Narration:**

We're going to start building the plan from the information you have today. Here on Home, I'll open the plan and use Build & improve to get to the next piece we need.

Before we add anything, notice the difference between these three examples. Our example household's mortgage already exists, so it's a debt. College support is a future commitment with dates attached. The renovation is still an idea, so we'll compare it separately.

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

Use Home → Your Money to open the category-filtered Accounts view and one account detail. Review the existing checking account ($18,000), [Client] Roth IRA ($145,000) and direct-Bitcoin location (3.4 BTC) in separate takes. Use the approved contextual add/update entry only where a record is missing.

**Narration:**

Here we're looking at one account from the money category on Home. Before getting into what it owns, I'm matching its name, owner and account type to the statement. If it's already entered, this is the record we're reviewing. Adding another would count the same money twice.

The client's Roth IRA tells us the account type, but we still need the investments inside it. For cash, we're checking the balance. For the Bitcoin location, we're checking the quantity and where the coins are held, using a plain name without recovery information.

After saving, I'll reopen the account beside the statement to check the result. The next three takes handle specific record questions: what a connection supplies, a balance without holdings, and purchase history. Use the ones that apply. If your accounts are already explained, continue to chapter six for the monthly picture.

**Overlay:**

One account · Correct owner/type · Holdings explain the balance

**Verify:**

One record per account. Quantity, total, owner/type and source date survive the saved readback. Direct Bitcoin and fund exposure retain different identities.

**Capture dependency:**

Foundation account-detail and maintenance writer paths, scoped ownership and truthful update dates. Fixture amounts require frozen-price treatment; actual holdings, HSA/education composition and any missing owners require a separately reviewed capture extension. Do not choose example tickers to fill gaps.

### Chapter 3 — Read what the connection supplies · only for a connected account after 1.2

[Clean teleprompter take](teleprompter/walkthrough/W01-03.txt)

**Show:**

Open account detail → How this account updates in an authorized synthetic connected-source case. Read the actual capability receipt for balance, holdings, activity and purchase details, including an incomplete case and its supported next step.

**Narration:**

This account is connected, but let's look at what that connection actually supplies. The balance tells us the total. Holdings explain what's inside it. Activity and purchase details answer different questions about how it got there.

If the total arrived without investments, that doesn't mean the balance is cash. The statement can help explain the composition in the next take. Missing purchase history stays with the question it needs to answer. We're also checking when the financial information was last confirmed; opening the page today doesn't make an older balance current.

If the account still needs its investments explained, the next take shows how to do that. If the holdings are complete, use the history take only for relevant records; otherwise, continue to the monthly cash-flow setup.

**Overlay:**

Balance · Holdings · Activity · Purchase details

**Verify:**

The receipt describes the actual supplied products and timestamps. Missing positions are not shown as cash, zero holdings or fully synced; one supported next action is identified.

**Capture dependency:**

D34/D62 capability receipts and financial-fact freshness. Capture requires certified synthetic evidence and the approved receipt/recovery UI. No live credentials, provider connection, paid refresh or staged provider response.

### Chapter 4 — Explain a balance-only investment account · only when holdings are missing after 1.2

[Clean teleprompter take](teleprompter/walkthrough/W01-04.txt)

**Show:**

At the same $145,000 Roth account, use Holdings needed → Add investments. Enter verified positions or use the accepted mutually exclusive Estimated mix path. Where identities are unresolved, show the source $116,000 spot-fund exposure/$29,000 stocks only as the estimated categories they support.

**Narration:**

We know this Roth account is worth $145,000. What we're doing here is explaining that balance, so the plan knows how the money is invested.

When the statement supplies actual investment names and quantities, those are what we use. If all we have is an approximate mix, it stays labeled as an estimate. In our example, there's $116,000 of spot Bitcoin-fund exposure and $29,000 of stocks inside the same $145,000 account. Those amounts explain the total; they don't increase it.

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

Use this take when you have purchase or transfer records for holdings already in the plan. Gather the exchange or brokerage records you can access; the price paid and relevant costs help establish purchase history for later tax work. If those records don't apply or aren't available, note what's missing and continue to chapter six. You don't need to repair an unrelated old purchase first.

Here, the purchase explains Bitcoin already in today's holdings. It isn't a new purchase today, so we don't invent today's date and price. The transfer from exchange to wallet moves the same position and history; it doesn't create a sale and repurchase. If the purchase is already here, accepting it again would duplicate it.

For a Roth account, you don't need every internal trade just to identify today's holdings. Contribution, conversion and distribution records have separate jobs when we examine access and taxes.

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

Open Cash Flow → Income, Taxes and withholding, Everyday spending, Debt payments and Saving and investing as needed. Enter original source state only. Present the exact example household cash bridge as a separate teaching graphic, never a fabricated app result.

**Narration:**

Now we're connecting the accounts to the money moving through the household each month. The first thing I'm checking is what each income amount includes. The client's gross pay is before deductions. Their partner's example income is after ordinary business costs, but the equipment payment is counted separately. Those meanings need to match the fields.

In our teaching calculation, gross income is about $19,417 a month. After the $4,000 tax allowance, $10,800 living costs and about $3,342 required debt, there's $1,275. The client's $775 contribution leaves $500 for other priorities. The employer's $387.50 goes into retirement saving; it isn't bill money.

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

Use Plan → Build & improve to reach the accepted retirement timing and spending owners. Enter [Client]’s intended age 52, [Partner]’s separately supported timeline and the reviewed fictional spending/benefit/horizon extension. Show each date and dollar basis before saving.

**Narration:**

With the starting facts in place, we can enter the work-change question you wrote down at the beginning. The client wants work to become optional at 52. That records their intention; the calculation will test whether it can be funded. Their partner's income stays on its own timeline.

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

Open Cash Flow → Income and Taxes and withholding, then the summary’s debt and saving routes. Reconcile original income and deductions with synthetic pay-stub/statement sources, then trace the remainder. Recall the original $500 illustration only to identify the state; do not replay the W01 arithmetic.

**Narration:**

We've entered the monthly picture. Now let's compare the income and deductions with their source records, then follow the money the plan says is left. In the original illustration that was $500; the app's actual amount needs to agree with its actual inputs.

I'll look for that remainder in checking, savings or a cost we haven't included. If it doesn't agree, we correct the underlying record before assigning another transfer. A tax payment set aside for later still has that job even if it's sitting in savings.

Once the income and deductions reconcile, we'll check the spending period and bill timing. That's where annual costs or a short week before payday can explain why a monthly total hasn't worked in practice.

**Overlay:**

Trace the remainder → resolve its source → use the verified amount

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

Our example household's proposal cuts living costs by $1,200 a month. In the teaching example, that changes the amount available from $500 to $1,700. They still need to identify the bills that make it possible. We'll compare the proposal first, then record when the real change begins and update current spending once it has happened. Saving a lower figure doesn't cancel a service.

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

Let's give the Reserve a target using the essential costs from the lesson. Our example household's $7,200 includes required household debt, so we're not adding those payments again. Testing six months gives a $43,200 target.

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

Carry the same gap into the approved Reserve funding/contribution owner. Show proposed $500/month beside the reduced-state $1,700 pool and anticipated $1,200 extra-card claim. Use a separate cash-coverage comparison for dependents or reliance on one income, then return to the unchanged example household split.

**Narration:**

We're still testing the reduced-spending version with $1,700 available. Your actual surplus stays unchanged until those spending changes happen. At $500 a month, the $11,200 Reserve gap takes 22.4 months, reaching the target with part of the twenty-third deposit before interest or withdrawals. That's almost two years to consider alongside the risk we're covering.

I'd give accessible cash more weight when dependents rely on one income and an interruption would otherwise require more borrowing. Building it faster may be worth slower extra-debt repayment, with required payments still covered. Our example household has a stable paycheck and variable business income; they aren't a single-income example.

Their proposed $500 Reserve pace leaves $1,200 of the same $1,700 for the card. We'll carry that split into Debt before settling it. The bank transfer comes after the combined decision, when we know the two choices fit together.

**Overlay:**

Proposed: $500 Reserve + $1,200 extra card = $1,700 once

**Verify:**

Pace is affordable from the same pool, gap stays visible and required payments remain covered. Faster Reserve is explained as a conditional trade-off, not a new example household contribution or fixed threshold.

**Capture dependency:**

Actual contribution owner, pace save/readback and any affordability display. Final transfer is outside the app. Keep the 22.4 arithmetic off an app screen unless its semantics match; no invented calendar funding date or automatic recommendation.

### Chapter 6 — Add an expected event and trace its funding · after 2.4

[Clean teleprompter take](teleprompter/walkthrough/W02-06.txt)

**Show:**

Open Plan → Overview → Life events. Add the reviewed expected vehicle need and one person’s income change, with explicit recurrence and units. Inspect the affected year’s income/costs/funding. Put the possible renovation in Plan → Scenarios and return to Current. Rehearse a planned change becoming current. Capture only the event branch relevant to the learner; the optional housing explanation requires its own reviewed synthetic proceeds/cost record before showing calculated results.

**Narration:**

Here we're adding the expected vehicle change. I'll check the amount, date and frequency, then the dollar basis so we don't apply inflation twice. A one-time purchase needs to happen once.

Let's follow it into the affected year. Which account or income pays for it, and what remains afterward? If we're saving ahead, that uses cash flow before the purchase and builds the balance we'll spend. Adding the event doesn't start that separate transfer.

If your event changes income instead, use the right person and start date, and an end date when the change is temporary. We'll keep the possible renovation in a separate scenario until it's chosen.

For a home move, there's an additional funding check here. Sale value has to cover the old mortgage, selling costs and any tax before we count what's left. The next home can need cash upfront as well as a new mortgage, and property tax, insurance, utilities and upkeep may change. Follow those together rather than treating the old home's full value as available cash.

Finally, when an expected change happens, reconcile the old event with today's facts. If a recurring bill ended, current spending now excludes it; keeping a second future reduction would lower spending twice. A completed purchase or new loan needs the same check against its new asset or debt record.

After saving, we'll reopen the affected year to verify the effect once. If college applies, continue to its take. Otherwise, carry the expected costs into Debt.

**Overlay:**

Event: amount · timing · recurrence · units · funding

**Verify:**

Expense and income changes occur once at the correct time/person; source funding is supported, not inferred. Renovation remains separate; planned-to-current update creates no duplicate effect.

**Capture dependency:**

Life-event owner, supported source/account attribution, recurrence, inflation units, event-to-asset/debt treatment and save/readback. Example household vehicle timing is about three years; exact dates and amount need capture extension. Generic $30,000 car is not a fixture price. Unsupported attribution remains unresolved.

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

Let's match each existing debt to the lender record before choosing extra payments. We're checking the balance, rate, required payment and any date when the terms change. I'll use the debts that apply to your household.

With the example card, the $405 minimum isn't all principal. The rough first-month illustration has about $235 of interest and $170 reducing the balance, before new purchases or fees. The real statement has its own billing rules.

For the interest-only home-equity line, $46,000 at the example's 8% rate costs about $307 a month without clearing principal. The payment-change date and repayment source belong beside that figure. With the other example debts, the 6.7% auto loan has a $600 payment and the 7.4% equipment loan has a $480 payment; removing those payments uses different amounts of cash, and the business still has operating needs.

The listed payments are about $3,342 against about $19,417 gross income, roughly 17%. That's payment pressure before tax and other deductions. We'll use the available cash verified earlier to decide about extra payments; the ratio doesn't provide another pool of money.

**Overlay:**

Required payment → interest + principal; DTI does not equal surplus

**Verify:**

Correct debt record, source and terms survive readback. Required/extra payments remain separate. HELOC date or guarantee omissions remain missing facts rather than inferred defaults.

**Capture dependency:**

PR #227 Debt detail owner/contextual writer, payment schedule and source freshness. Exact card billing/minimum rules and HELOC maturity require the reviewed extension. No debt is duplicated or newly adopted by this review.

### Chapter 2 — Separate household leverage from loan collateral · after 3.6

[Clean teleprompter take](teleprompter/walkthrough/W03-02.txt)

**Show:**

Read included household assets and debt, with net worth separately. Use the unchanged balance-sheet and partial-stress graphics unless the exact app scenario is verified. Keep the household-resource comparison here; lender-specific LTV mechanics belong to A3.1 and conditional chapter 5.

**Narration:**

Here we're looking at the resources supporting the household's debt. The example includes $1,996,000 of assets before subtracting $444,500 owed. That's about 22% debt-to-assets; subtracting the debt leaves $1,551,500 net worth.

Notice what those totals include. The home and retirement, education and health accounts have different access rules and other jobs. We also omitted vehicle and business-equipment values while including their debts. This is a teaching balance sheet, not a complete appraisal or a pile of accessible repayment cash.

In the partial stress illustration, Bitcoin exposure falls 70%, selected stocks fall 30% and the home falls 20%. Education and health values are held unchanged. Included assets become $1,217,200, while debt is still $444,500. The ratio rises to about 37%.

That shows what lower values do to the household measure. It doesn't test every bad outcome or tell us what one lender can require. For a collateral-backed loan, the actual agreement and accessible response money need a separate check. If Bitcoin backs your loan, complete the Bitcoin-loan lesson before the collateral walkthrough. We'll record ordinary repayment and fallback when we bring the debt choices back to Cash Flow.

**Overlay:**

Household DTA: 22.27% → 36.52% · One loan’s LTV uses pledged collateral

**Verify:**

Assets/debt/net-worth denominators remain distinct. Stress assumptions/exclusions are visible. No example household Bitcoin loan or integrated worst-case result is fabricated.

**Capture dependency:**

Exact supported asset denominator and scenario fields. Source partial stress: BTC exposure −70%, selected stocks −30%, home −20%; education/health unchanged; vehicle/business values omitted while debts included. Preserve partial scope; no fixed-debt collateral threshold demonstration in this chapter.

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

### Chapter 4 — Compare one financing purpose through its exit · only for a proposal after 3.4 and relevant A3.2 sections

[Clean teleprompter take](teleprompter/walkthrough/W03-04.txt)

**Show:**

Use Plan → Scenarios for one hypothetical $30,000 project at the reviewed date. Compare cash, a supported taxable sale and one eligible financing arrangement, plus smaller/delay. Read cash retained, payments, fees, collateral and ending principal. Use a separate graphic for $20,000/8%/60-month amortizing-versus-interest-only arithmetic.

**Narration:**

Use this take if you're comparing financing. Otherwise, continue to the repayment rules for your existing debts. We'll use the same purchase amount and date in each version. Paying $30,000 from the $32,000 Reserve leaves $2,000 for that job. A taxable sale needs enough proceeds after its actual tax cost. Financing keeps cash initially, but the payment has to fit beside the Reserve and card.

The final balance is part of that comparison. In our separate $20,000 example, about $406 a month pays the loan down over five years; about $133 interest-only leaves the $20,000 owed. A refinance needs the full replacement mortgage priced, while unusual terms need their actual settlement formula, guarantees and use restrictions.

We'll keep any contract term the app doesn't represent beside the comparison and resolve it before choosing. A smaller or delayed project may be the affordable answer. Whichever direction you choose, the payment and principal exit go into the debt rules next.

**Overlay:**

Same need/date → cash left → payment → final balance → repayment source

**Verify:**

Equal need and dates, actual source tax, complete repayment shape and constraints. Proposal remains separate; no application or approval. Unsupported settlement terms prevent a model-complete conclusion.

**Capture dependency:**

Reviewed fictional offer/date, taxes/basis, permitted uses and guarantee terms; approved Scenario expressiveness. Generic arithmetic: $405.5279 amortizing, $4,331.6735 total interest; $133.3333 interest-only, $8,000 interest plus principal. HEI/shared appreciation requires its actual formula; do not approximate it as an ordinary loan.

### Chapter 5 — Size and operate a Bitcoin-backed loan · only after A3.1 when Bitcoin collateral applies

[Clean teleprompter take](teleprompter/walkthrough/W03-05.txt)

**Show:**

Conditional A3.1 capture only. Use the existing debt instructions/worksheet alongside Debt for an actual Bitcoin-backed loan or Plan → Scenarios for a proposal. Use a separate generic $50,000/3.5 BTC sizing graphic and authorized non-broadcast procedure diagram. Keep 50%/25% fixed-debt decline-to-threshold graphics here when explaining initial collateral; do not create an example household Bitcoin loan or initiate a real top-up. Ordinary debt instructions are in chapter 6.

**Narration:**

This take is for a Bitcoin-backed loan after you've completed its situation lesson. If that doesn't apply, go to chapter six. We'll use the actual contract and a separate sizing example here, with wallet secrets kept out of the record. We start with the full obligation before deciding how much collateral to post. This example dedicates 3.5 BTC to $50,000 of debt when Bitcoin is $100,000. After an 80% decline, those coins are worth $70,000. If posted in time, that's about 71.4% LTV. At the assumed 80% liquidation line, 3.125 BTC only reaches the boundary. The 3.5 BTC provides some room, but any stricter call-cure or maturity term still has to be met.

The $50,000 opening amount assumes separately funded interest and fees. One hypothetical year of 12% capitalized interest makes it $56,000, exactly 80% of the stressed $70,000. So if costs accrue, the initial principal needs reducing or more Bitcoin needs dedicating before borrowing.

After sizing the debt, posting 1 BTC starts it at 50% LTV and leaves 2.5 BTC reserved in cold storage. Posting all 3.5 starts the same loan at about 14.3%. The smaller initial deposit reduces lender exposure but needs a faster response. With fixed debt and our assumed 80% liquidation line, the 50% starting position reaches it after a 37.5% price fall. Posting enough for 25% initially allows a 68.75% decline to the same line; that comparison shows more upfront collateral, not a preferred starting level. Reserved coins only count for lender LTV after they arrive and are credited. That's why the top-up trigger, amount, access time and maximum collateral exposure belong here. An automatic feature can't reach into your cold wallet; the actual funding and confirmation requirements still apply.

Repeat borrowing uses the same supporting resources too. In the recurring illustration, $25,000 becomes $28,000 after 12% interest. The next $25,000 draw makes $53,000, and another 12% makes $59,360. We can't reuse the same spare collateral for each draw. If the payment, timed response or final repayment still lacks a resource, the proposal stays unchosen. Once the rules are supported, we can carry the chosen obligation back into the household cash flow.

**Overlay:**

Debt first → collateral placement second · Posted BTC and dedicated BTC have different jobs

**Verify:**

The Bitcoin loan's exit and unavailable-operator fallback are usable. Conditional worksheet preserves costs, exact boundary, stricter cure, timely crediting and combined repeated debt. No double-used BTC, automated cold-wallet claim or signed/executed loan.

**Capture dependency:**

Actual contract, advanced modeled terms, saved liquidation selection, cost-accrual rule, source identity and approved scenario receipt. D63 parity/fix-first gates remain app implementation work. Any provider procedure requires safe independently authorized capture with no broadcasting, credentials or secret exposure; illustration is not proof a lender accepts the arrangement.

### Chapter 6 — Carry one debt decision into Cash Flow and Allocation · after 3.6

[Clean teleprompter take](teleprompter/walkthrough/W03-06.txt)

**Show:**

Return to Cash Flow → Debt payments and Saving and investing. Read the saved extra claim from Debt without entering it twice. Record ordinary debt payment source, principal exit, relevant dates, fallback and responsible/backup person in the instructions worksheet beside the debt record. Read the reduced-state assigned amount without replaying the gross-to-net bridge, then show the distinctly future payoff condition and hand current/future claims to W04.

**Narration:**

Let's record the ordinary repayment instructions for each debt you carry or choose. If no debt applies, continue to Allocation with your available cash.

For this obligation, we're naming what pays the regular bill and what repays principal. If a sale is the exit, record the amount, date and response to smaller or late proceeds. If refinancing is planned, include what you'd do if approval isn't available.

Now put any payment-change, review and maturity dates with the person responsible. A trusted backup needs to recognize a time-sensitive problem and find the safe instructions if you're unavailable. Keep secrets out of this record. Collateral borrowers bring in the funded response already worked through in their contract lesson.

Once the choice is saved, let's read it back in Cash Flow. The reduced-spending illustration assigns its $1,700 to $500 Reserve and $1,200 extra card; there's no additional investing amount in that split. Required payments and existing saving were already included.

When the card is actually paid off, verify the payments that ended and any remaining charge. If the $405 required and $1,200 extra were still being paid, that releases $1,605. That future money needs a new decision; it doesn't automatically become an investment transfer today.

We'll take the chosen commitments and that future review condition into Allocation. Then we can choose where contributions go using the money actually available.

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

Open Plan → Portfolio and allocation in Current. Expand included assets and one account's holdings. Reconcile the actual approved denominator with the source portfolio and direct Bitcoin/fund classifications. Do not force the teaching subset onto an incompatible app scope.

**Narration:**

Here's Current in Portfolio and allocation. I'm opening the included assets before changing the target.

I'm checking the Bitcoin held directly and through funds, along with the stock and cash holdings. Each holding belongs in the total once; the account balance doesn't get added again. Dedicated education and healthcare money keep their separate jobs.

Once these holdings agree with the records, we can compare a target using the same group of assets. If a holding is missing or classified incorrectly, that's the first thing to fix.

**Overlay:**

Cue “opening the included assets” → Verify the portfolio scope; cue “using the same group of assets” → Current and target share a denominator.

**Verify:**

Holdings and totals reconcile without duplicate account balances. Any app denominator difference is explicitly explained; no $1,307,000 total is forced onto an incompatible screen.

**Capture dependency:**

Approved Portfolio and allocation route, eligible-assets denominator, spot-fund classification and exact account/holding composition readback.

### Chapter 2 — Choose Bitcoin’s intended role — after 4.3

[Clean teleprompter take](teleprompter/walkthrough/W04-02.txt)

**Show:**

Review the intended Bitcoin role from 4.3, then locate the supported target choice in Portfolio and allocation. Use the existing orientation graphic only as a brief reference if needed. Do not invent a risk-profile score, notes field or saved target.

**Narration:**

Let's bring forward the role you chose for Bitcoin. We're using that intention to set a starting amount to test.

I'm looking at the target choice here, with the household's spending dates beside it. The question now is whether the rest of the portfolio can cover those commitments through a decline. We'll check that before saving the target.

**Overlay:**

Cue “a starting amount to test” → Proposed target; cue “before saving the target” → Check the funding first.

**Verify:**

The role/range remains a proposed preference; no arbitrary suitability recommendation or saved target is fabricated.

**Capture dependency:**

Target Current/Preview availability, existing choice provenance and absence of automatic save during the orientation scene.

### Chapter 3 — Build the target from funding needs — after 4.3

[Clean teleprompter take](teleprompter/walkthrough/W04-03.txt)

**Show:**

Read the canonical Reserve assignment, distinct dated commitments and accessible early-retirement funding. Enter the proposed target in the approved Portfolio Preview. Inspect a supported stress comparison and save/read back only an intended target. The separate $1 million illustration remains in teaching 4.3.

**Narration:**

Here's the Reserve amount we already chose, followed by the approaching expenses that need separate funding. I'm using those amounts to check the cash in the proposed mix.

Now let's look at the first important payment during a difficult market. I want to see the asset that supplies it and what remains afterward. If that payment is unfunded, we can adjust the mix or its funding source and compare again.

Once the proposed mix fits those jobs and we're willing to follow it, we can save the target and read it beside Current. That saves our intention; it doesn't trade the holdings.

**Overlay:**

Cue “approaching expenses that need separate funding” → Count each commitment once; cue “read it beside Current” → Saved target; holdings unchanged.

**Verify:**

Near-term costs are counted once, Reserve uses the same source as Cash Flow, target totals 100%, and save/readback preserves the intended target without trading assets.

**Capture dependency:**

Canonical Reserve reader, early-access row attribution, target writer, Current/Preview isolation, supported stress and saved-target receipt.

### Chapter 4 — Fit current contributions and future milestones — after 4.7

[Clean teleprompter take](teleprompter/walkthrough/W04-04.txt)

**Show:**

Open Cash Flow → Saving and investing with the reviewed reduced-spending state. Identify the existing employee/employer entries, Reserve contribution and extra-card payment. Inspect the residual after those claims. Keep the future $1,605 release conditional on actual payoff using supported controls or the existing toolkit.

**Narration:**

We're in Saving and investing, using the reduced-spending version from earlier. I'm checking the employee contribution, Reserve contribution and extra card payment against the same available money.

In this version, those choices use the remaining household cash. The employer contribution adds retirement saving separately; it doesn't increase the money we can transfer from checking.

The card payoff is a future start condition. I'll keep the proposed new investment transfer inactive until the payments actually stop, then check the amount released and any changed bills. Today's instructions now fit today's cash.

**Overlay:**

Cue “use the remaining household cash” → No additional transfer available; cue “until the payments actually stop” → Future contribution stays conditional.

**Verify:**

Current household outflows are affordable once. Employer money is not spendable; future $1,605 is not active and no assumed payoff date is invented.

**Capture dependency:**

Cash Flow contribution treatment, existing savings and employer match, Reserve/extra-debt integration, timing controls and save/readback.

### Chapter 5 — Select a receiving account — after 4.5

[Clean teleprompter take](teleprompter/walkthrough/W04-05.txt)

**Show:**

Open the proposed receiving account and relevant reviewed provider terms. Verify access date, permitted investment, eligibility, contribution room and fees for that account. Show an outside account-opening action only when needed, using the supported action location.

**Narration:**

Let's open the account intended to receive this contribution. I'm checking its owner and access date first, then the provider's investment menu, fees, eligibility and remaining contribution room.

If this money funds early retirement, the account needs a supported way to supply those years. Any unresolved access question goes through the early-access lesson before we rely on it.

An existing account that meets those needs can do the job. If another one needs opening, we'll keep that as an outside action. Now we can compare the tax election where that choice applies.

**Overlay:**

Cue “owner and access date” → Person / account / access; cue “fees, eligibility and remaining contribution room” → Confirm actual provider terms.

**Verify:**

Receiving account supports the actual purpose, allowed investment and timing; missing eligibility/provider facts are explicit.

**Capture dependency:**

Actual account type, owner, menu, contribution limits for the applicable year and supported future receiving-account selection.

### Chapter 6 — Compare the tax election at equal cost — after 4.5

[Clean teleprompter take](teleprompter/walkthrough/W04-06.txt)

**Show:**

Use the reviewed contribution Preview and actual payroll-cost evidence. Identify whether it compares equal household cost or equal deposits. Inspect the take-home effect and residual cash before saving the contribution election. Keep the equal-cost teaching calculation in 4.5.

**Narration:**

Here's the contribution election we're comparing. First, I'm checking whether the comparison holds the household cost equal or keeps the deposits equal. That changes what the numbers mean.

Now let's read the take-home effect beside the Reserve and debt payments. If switching to Roth reduces the paycheck, that cost needs to fit here before we save it.

Once the cost and access needs fit, we can save Traditional, Roth or the intended mix. This changes new contributions. An existing Traditional balance requires the separate conversion decision from Tax.

**Overlay:**

Cue “household cost equal or keeps the deposits equal” → Identify the comparison basis; cue “This changes new contributions.” → Contribution election ≠ conversion.

**Verify:**

Comparison basis is clear, required qualification assumptions are present, and updated payroll cash reconciles with the same plan.

**Capture dependency:**

Applicable payroll tax/election evidence, equal-cost versus equal-contribution treatment, contribution Preview and save owner.

### Chapter 7 — Tell each account what to buy — after 4.7

[Clean teleprompter take](teleprompter/walkthrough/W04-07.txt)

**Show:**

Read Current and target in Portfolio and allocation, then amount/account/investment in Cash Flow → Saving and investing. Preserve the future $1,000/$605 route as a reviewed conditional comparison with the $500 Reserve separate. Do not invent a security identity or trade automation.

**Narration:**

Here's the target beside what we currently own. The shortfall helps us choose where affordable purchases go; it doesn't create cash to invest.

I'm opening each contribution and connecting its amount to the receiving account and the actual investment. For the future card-payoff route, the proposed split remains conditional until payoff. The Reserve contribution continues separately.

Let's check the start condition and investment together before saving. Changing future purchases leaves the existing holdings unchanged. Next, we'll take these instructions to the provider so the money arrives and buys what we intended.

**Overlay:**

Cue “doesn't create cash to invest” → Target gap ≠ available cash; cue “start condition and investment together” → Amount / account / investment / start.

**Verify:**

Amount/account/investment/start condition agree; target-to-trade automation is not invented and currently unavailable cash is not routed.

**Capture dependency:**

Supported holding selection, target calculation denominator, next-dollar precision, future conditions and contribution save/readback.

### Chapter 8 — Complete and verify provider instructions — after 4.7

[Clean teleprompter take](teleprompter/walkthrough/W04-08.txt)

**Show:**

Use the existing action list for necessary payroll elections, account opening, transfers and recurring purchases. Attach authorized synthetic confirmation only if available; otherwise leave the action pending with an owner/date. Do not perform provider mutations during preparation.

**Narration:**

The plan tells us where the contributions are supposed to go. Here are the employer, bank or investment-provider actions still needed.

I'm putting a person and date beside each one. After the first contribution, we'll compare the confirmation with the amount, receiving account and investment in this plan. A transfer can succeed while the cash is still waiting to be invested, so we're checking both the deposit and the purchase.

Until that evidence exists, the action stays pending. That finishes contribution setup. Next, we'll work on the purchase records needed when an investment is eventually sold.

**Overlay:**

Cue “both the deposit and the purchase” → Deposit ✓ Purchase ✓; cue “the action stays pending” → Planned / confirmed.

**Verify:**

Every current provider action has confirmation or a specific owner/date. Future conditions remain future and a saved app choice is not presented as an executed investment.

**Capture dependency:**

Safe synthetic/private evidence workflow, actual provider requirements and a supported non-secret action-status location.

## W05 — [Reconcile tax records and prepare one useful comparison](scripts/working/W05_reconcile-tax-records-and-prepare-one-useful-comparison.md)

### Chapter 1 — Read the gain on a proposed sale — after 5.1

[Clean teleprompter take](teleprompter/walkthrough/W05-01.txt)

**Show:**

Open the applicable taxable holding's Purchase details and a supported sale Preview. Trace actual available units, acquisition records, supported basis, gain/loss, estimated tax and usable cash. Keep the full three-lot illustration in teaching 5.1; do not fabricate app units or results.

**Narration:**

Let's open the taxable holding and its purchase details before placing a sale. I'm checking the units available, their acquisition records and supported cost.

Now we can follow the proposed sale from proceeds through basis and gain to estimated tax and cash left for its purpose. The tax estimate needs the rest of the year's income; the gain alone doesn't tell us the bill.

If a cost is missing, we leave it unknown and find the source before relying on that comparison. Previewing a lot doesn't notify the custodian or place a trade. If we're preparing the transaction, we'll take the supported choice into the records lesson next.

**Overlay:**

Cue “from proceeds through basis and gain” → Proceeds → basis → gain → tax → usable cash; cue “doesn't notify the custodian” → Preview only.

**Verify:**

The quantity and available lots match source records; missing slices are not silently consumed and gross proceeds are not labeled tax or spending cash.

**Capture dependency:**

D54/D58 purchase details and lot-method confirmation, supported sale Preview, current holding identity and tax output with fees/basis coverage.

### Chapter 2 — Repair the relevant purchase history — after A5.2

[Clean teleprompter take](teleprompter/walkthrough/W05-02.txt)

**Show:**

Use reviewed synthetic source records: one relevant import, overlapping events, a same-owner transfer and an unresolved detail. Show position/history before and after. Preserve original files without exposing private identifiers. Demonstrate actual deduplication and transfer reconciliation, not the teaching arithmetic.

**Narration:**

I have the original source file beside this holding. Let's review what the import adds before accepting it.

These overlapping entries need to match the events already present. I'm also checking that the exchange withdrawal and same-owner wallet receipt stay connected to the original purchase history.

Now let's compare the remaining units with the holding. If they disagree, we'll trace fees, missing activity or duplicates. We leave an unresolved detail visible while obtaining the evidence. Once these agree, we can use the supported history for the sale without adding the holding a second time.

**Overlay:**

Cue “connected to the original purchase history” → Same-owner transfer preserves history; cue “without adding the holding a second time” → Reconcile history; count assets once.

**Verify:**

Overlaps deduplicate, same-owner transfer retains quantity/history, and any unresolved evidence stays explicit. No invented historical transaction makes balances agree.

**Capture dependency:**

Certified import event coverage, duplicate and transfer reconciliation, fees, unknown slices and before/after quantity proof.

### Chapter 3 — Find an actual income window — after 5.4

[Clean teleprompter take](teleprompter/walkthrough/W05-03.txt)

**Show:**

Open the contextual Tax strategy/roadmap and a relevant year. Inspect both people's work/benefit dates, distributions, supported loss carryforward and planned transactions against their source evidence. Compare the next material income change with actual approved outputs.

**Narration:**

Here's the tax roadmap. I'm opening the year we're considering, with each person's work income, benefits and planned transactions.

Let's compare it with the next important income change. We need the household's full picture, including distributions, gains and any supported loss carryforward, before calling this a useful window.

If an income or filing record could change that picture, that's the fact to obtain first. Otherwise, we'll use this year to compare one conversion amount, the cash paying its tax and the option of leaving the plan as it is.

**Overlay:**

Cue “the household's full picture” → One tax-year picture; cue “compare one conversion amount” → Bounded comparison.

**Verify:**

Year, owner, income sources, RMD dates and transaction state are consistent. No fixed-age RMD assumption or fabricated tax window.

**Capture dependency:**

Contextual Tax route, year-detail parity, actual birth-year/account inputs, loss carryforward persistence and saved-result freshness.

### Chapter 4 — Compare conversion, withdrawal and no change — after 5.4 / A5.1

[Clean teleprompter take](teleprompter/walkthrough/W05-04.txt)

**Show:**

Start with Current and preview a reviewed bounded conversion, smaller amount and accessible spending withdrawal where relevant. Trace actual conversion dollars, tax source, first-year liquidity and later after-tax resources. For A5.1 extend the same comparison through the bounded years and material income transitions. Do not replay the teaching opportunity-cost graphic.

**Narration:**

I'm keeping spending and return assumptions the same while comparing this conversion with no added conversion and a smaller amount.

Here's what moves to Roth, the cash paying the tax and the separate source for living expenses. Let's read the first affected year's accessible money, then the later after-tax resources, including the outside money retained if we don't convert.

An accessible Traditional withdrawal may instead supply the spending needed in this window. For a multiyear schedule, we'll check each material income transition and set the annual review.

If conversion tax leaves the early years short, the amount or timing needs work. Once it fits, we can save the intended strategy. The custodian transaction and tax payment remain separate actions.

**Overlay:**

Cue “the cash paying the tax and the separate source for living expenses” → Conversion / tax / spending; cue “outside money retained if we don't convert” → Compare total after-tax resources.

**Verify:**

After-tax and liquidity comparison includes outside assets, same lifestyle and assumptions. RMD exclusion, basis, healthcare and access prerequisites are recorded; saving does not fabricate execution.

**Capture dependency:**

Sole conversion writer, Current/Preview and scenario isolation, total after-tax result, tax-payment source, supported schedule, healthcare scope and save/reload receipt.

### Chapter 5 — Prepare a tax-sensitive sale or deliberate pass — after A5.2

[Clean teleprompter take](teleprompter/walkthrough/W05-05.txt)

**Show:**

Use the supported synthetic transaction candidate and its current-year comparison. Show timely lot-identification evidence and reviewed replacement instructions, including applicable automatic/spouse/IRA activity. Use the private packet for requirements the app does not represent; do not place a trade.

**Narration:**

Here is the supported sale candidate and the reason for it. I'm putting the lot-identification instruction beside the process and deadline required for this account. We need the provider acknowledgment or applicable contemporaneous record.

For a loss sale, let's check the replacement review, including automatic purchases and relevant spouse or IRA activity. For a gain harvest, let's confirm the remaining income room after other planned transactions.

If the benefit no longer justifies the costs, we can keep the investment and record that reason. If we proceed, the proposal stays pending until the actual trade is executed. Then we reconcile what happened.

**Overlay:**

Cue “the process and deadline required for this account” → Timely identification; cue “stays pending until the actual trade is executed” → Proposed / executed.

**Verify:**

Candidate has supported basis/units, current identification process, replacement review, income context and intended exposure. No app selection is presented as legal execution.

**Capture dependency:**

Actual supported candidate calculation, asset/account/year-specific identification, replacement tax review, transaction evidence and honest execution status.

### Chapter 6 — Finish the professional and reporting packet — after 5.1 / 5.4 / A5.2

[Clean teleprompter take](teleprompter/walkthrough/W05-06.txt)

**Show:**

Assemble the focused private/synthetic packet for the actual decision. For a conversion, include income/account records, applicable IRA basis and required-distribution records, proposed amount, tax-payment source and custodian instructions. For a taxable sale, inspect the actual FORM 8949 TAX DATA export's columns, dates and coverage when relevant. Demonstrate post-trade/remaining-lot reconciliation only for that sale route, with labeled synthetic confirmation and no real financial action.

**Narration:**

Let's put together the records for the decision you're actually making, along with the unresolved question.

For a conversion, bring the income and account records, the amount under consideration, the tax-payment source and the custodian's instructions. You can finish that packet without preparing a taxable-sale export.

For a taxable sale, open the relevant export and check its coverage. FORM 8949 TAX DATA supports the tax professional's work; it isn't a filed form. After an actual trade, compare its confirmation with the used units and remaining holdings, then reconcile provider reporting and the filed return.

Whichever route applies, keep the proposal separate from the confirmed transaction. Then return to tax timing or bring the chosen funding approach into the retirement paycheck.

**Overlay:**

Cue “it isn't a filed form” → Tax data for review; cue “the used units and remaining holdings” → Confirmation → remaining lots → filed record.

**Verify:**

Packet matches the decision; conversion-only work does not require a taxable-sale export or lot reconciliation. Relevant export scope and omissions are visible; proposed/completed states remain separate; no full sensitive backup, filing claim or invented confirmation.

**Capture dependency:**

Approved export content, source/realized/remaining-lot consistency, private sharing workflow and reviewed synthetic confirmation.

## W06 — [Build and test the retirement paycheck](scripts/working/W06_build-and-test-the-retirement-paycheck.md)

### Chapter 1 — Build the complete cash need — after 6.1

[Clean teleprompter take](teleprompter/walkthrough/W06-01.txt)

**Show:**

Open the first retirement-year detail. Drill into canonical spending, healthcare, debt, tax, events and income where corrections are needed. Reconcile the actual complete cash need and refreshed result; keep the $68,000/$86,000 illustration in teaching 6.1.

**Narration:**

Here's the first year after work stops. I'm opening living costs, healthcare, required debt, tax and dated events to check that each appears once. The spending describes the life we're funding; it doesn't carry retirement contributions forward as living costs.

Now let's read the income arriving in that year and the gap the accounts need to supply. I'm checking what that displayed gap includes, especially tax and debt.

If something is missing or duplicated, we'll correct its source and wait for the updated result. Once the income, withholding and full costs agree, we can follow the money available for this year.

**Overlay:**

Cue “each appears once” → Spending / healthcare / debt / tax / events; cue “what that displayed gap includes” → Reconcile the complete funding need.

**Verify:**

Income and complete outflow reconcile; tax/withholding, events, debt and portfolio distributions are counted once; calculation reflects saved changes.

**Capture dependency:**

Year-detail attribution, canonical income/spending owners, tax-dependent withdrawal math, automatic Plan updating and current result receipt.

### Chapter 2 — Fund the early intervals and benefit dates — after 6.1 / A6.3

[Clean teleprompter take](teleprompter/walkthrough/W06-02.txt)

**Show:**

Inspect both people's reviewed work, benefit and access dates. Follow every material early funding interval and its supported accounts, with Reserve/commitments counted once. When A6.3 applies, connect the actual person/account/route evidence before relying on it. Show a supported benefit-timing comparison using reviewed estimates and their dollar convention.

**Narration:**

Let's open the periods before another income or account-access route begins. I'm checking both people's dates, then the source supplying each gap.

Money assigned to the Reserve or another commitment keeps that job. If this interval depends on early retirement-account access, we'll attach the evidence for this person, account and withdrawal. A rollover that could change the route stays pending.

Here's the benefit-timing comparison. We'll look at the extra funding needed while waiting as well as the later benefit, using the same spending and actual estimates. Each period now needs either a supported source or a specific gap we still have to solve.

**Overlay:**

Cue “both people's dates” → Two people, two timelines; cue “a specific gap we still have to solve” → Funding interval readback.

**Verify:**

All material early intervals have supported sources or explicit gaps; source ages, access evidence and inflation convention are correct.

**Capture dependency:**

Person/account access model, separation and distribution rules, actual benefit estimates, spouse/survivor support scope and interval funding output.

### Chapter 3 — Enter coverage costs and transitions — after 6.3

[Clean teleprompter take](teleprompter/walkthrough/W06-03.txt)

**Show:**

Use reviewed synthetic/private coverage quotes and supported expense/life-event owners. Enter the selected full costs, ordinary/difficult-year exposure and person-specific transition dates. Connect the applicable verified income effects; show unmodeled assistance/premium costs as labeled outside estimates with their source.

**Narration:**

I have the selected coverage quote beside the plan. Let's enter the full annual cost, with the difficult-year exposure and the cash available for it.

I'm checking the withdrawal or conversion against the same coverage year's income estimate. Any verified assistance repayment or premium effect needs funding too; an effect the app doesn't calculate still belongs in the estimate.

Now we'll set each person's transition dates and confirm the Part B timing and Part A effective date where relevant, including the HSA contribution cutoff. Entering an expense doesn't enroll anyone. We'll keep that outside action pending until coverage is confirmed.

**Overlay:**

Cue “the full annual cost” → Premiums + care costs + retained risk; cue “the same coverage year's income estimate” → Income and coverage agree.

**Verify:**

Healthcare is neither omitted nor duplicated, transitions are person-specific, retained risk is funded and subsidy/premium omissions are explicit.

**Capture dependency:**

Supported expense/life-event timing, coverage calculation scope, actual quotes, Marketplace/Medicare income treatment and enrollment/HSA confirmation.

### Chapter 4 — Choose the account and investment supplying cash — after 6.1

[Clean teleprompter take](teleprompter/walkthrough/W06-04.txt)

**Show:**

Open Plan → Retirement strategy → How retirement is funded. Compare supported account order/blend in Current/Preview and inspect the matching year's account withdrawals, investment sales, tax and remaining resources. Preserve required distributions, access rules and separate conversion funding. Save/read back only the intended policy.

**Narration:**

I'm opening How retirement is funded and tracing the first year's withdrawal to its account, the investment sold and the tax created.

Required distributions stay accounted for. For the remaining spending, let's preview the account order or blend we're considering. I'll keep the other assumptions steady while reading cash for bills and balances left, then open a later funding year.

If that choice runs out of accessible money, we still have a source or spending decision to resolve. Once we intend to follow it, we can save the policy and read the same year again to confirm that the plan reflects it.

**Overlay:**

Cue “its account, the investment sold and the tax created” → Account → asset sale → spending cash; cue “a later funding year” → Check the next source as well.

**Verify:**

Funding, RMDs, asset sales, conversion and taxes reconcile to the same year and save receipt; no unsupported universal order is staged.

**Capture dependency:**

Supported account-order/blend and asset-sale controls, access conditions, RMD rules, Current/Preview calculation and saved policy/year detail parity.

### Chapter 5 — Use the Reserve through a difficult sequence — after 6.8

[Clean teleprompter take](teleprompter/walkthrough/W06-05.txt)

**Show:**

Open an actual supported weak retirement year and follow Reserve use, remaining cash, target/floor and refill source with sale taxes/fees. Use the canonical spending-gap basis and distinct commitments. Keep the separate annual Reserve example in teaching 6.8; do not replay sequence arithmetic or invent a modeled sequence.

**Narration:**

Let's open a weak year and follow the cash used for spending. Here's what remains in the Reserve, beside its chosen target and floor.

Now I'm looking at the proposed refill. Which asset supplies it, what tax or fees apply, and is that money already promised elsewhere? If we wait, there still needs to be a funded response before the Reserve reaches its floor.

We'll also look farther into the difficult period. A longer wait for recovery needs a source for the next bills. Once we can follow that, the Reserve amount tells us what it supports and what we'll do as it runs down.

**Overlay:**

Cue “its chosen target and floor” → Cash available / target / floor; cue “a funded response before the Reserve reaches its floor” → Refill source + costs.

**Verify:**

Reserve is an existing-asset role, gap excludes counted income/tax appropriately, floor is finite and use/refill money is assigned once.

**Capture dependency:**

Canonical Reserve source reader/writer, target/floor basis, modeled refill cadence, funded source/tax and actual weak-year result.

### Chapter 6 — Compare sale, other assets and borrowing — after 6.6

[Clean teleprompter take](teleprompter/walkthrough/W06-06.txt)

**Show:**

Compare supported retirement funding choices for the same net spending/date. Keep actual loans in Debt, a possible one-time loan in Scenarios, and an adopted recurring policy in Retirement strategy. Bring verified contract/model terms and A3.1's funded responses; inspect a weak year, accrual, repayment, sale tax and remaining assets. No simple-interest teaching graphic.

**Narration:**

We're comparing the same spending on the same date. I'll start with the sale, then another available asset, reading the tax, usable cash and resources left.

If you aren't considering borrowing, you can finish with the sale or other funding source you've compared. If borrowing is part of the decision, bring in the loan terms and funded responses from the loan review. Let's open a weak period and the repayment year to follow interest, any added debt, collateral needs and the source that pays the loan off.

Those consequences belong beside the plan result. Our example household has no current Bitcoin-backed loan; a possible one-time loan stays in its scenario. An ongoing retirement borrowing policy can be saved only as the strategy we intend to follow, with the separate loan review completed before we rely on it.

**Overlay:**

Cue “the same spending on the same date” → Equal net spending; cue “the repayment year” → Follow the loan through its exit.

**Verify:**

No new actual loan is created from a scenario; interest/debt/collateral/repayment, fallback and net-spending comparison remain consistent. Unmodeled terms are explicit.

**Capture dependency:**

Accepted borrowing parity: rate path, paid/accrued interest, caps, top-up/release, liquidation, closeout, fallback, collateral availability, Current/Preview and saved-policy evidence.

### Chapter 7 — Test one decision and read its cause — after 6.8, using 1.5 result literacy

[Clean teleprompter take](teleprompter/walkthrough/W06-07.txt)

**Show:**

Use an actual identified retirement funding problem and one supported spending/work-date/funding comparison. Inspect the matching result receipt, count, horizon, freshness and affected year, without repeating the result-literacy lesson. Confirm household trade-off and current/preview isolation; save only an intended choice.

**Narration:**

Here's the retirement year that needs work. Let's compare one change that addresses it, keeping the other assumptions steady.

I'm reading the changed result and opening that year again to see why it moved. Does the change supply the missing cash? What does the household have to do differently, and what happens to a later funding year?

We'll use corrected facts even if they make the result less comfortable. Once we're willing to follow the change, we can save it and confirm the result reflects it. Otherwise, Current stays in place. Now we can turn that chosen plan into the annual spending decision.

**Overlay:**

Cue “one change that addresses it” → One changed decision; cue “opening that year again to see why it moved” → Result → cause → household trade-off.

**Verify:**

Percent/count share the same run; chosen and earliest dates stay separate; preview does not alter saved facts/strategy before Save.

**Capture dependency:**

Approved full-result standard, matching receipt/horizon, Current/Preview isolation, same seeded comparison path where supported and saved-result readback.

### Chapter 8 — Save annual spending and the refill decision — after 6.8

[Clean teleprompter take](teleprompter/walkthrough/W06-08.txt)

**Show:**

Read the standing spending guardrail status separately from the annual budget review. Use approved actual dollar thresholds only after inverse-calculation proof. Inspect saved spending, one inflation adjustment, applicable 60/80/95 policy and annual 10% cap, remaining funding difficulty, household spending choice, Reserve target/floor and funded refill. Save and read back the accepted budget; keep all invented arithmetic in teaching 6.8.

**Narration:**

I'm reading the standing guardrail status first, then opening the annual spending review. The portfolio threshold tells us when to review; this proposal is the budget we're considering.

Let's check the saved spending, the inflation adjustment and any suggested correction. If the annual correction is capped, that doesn't mean the target has been restored. We still need to read the remaining difficult years and identify the expenses the household would actually change.

Now I'm checking the Reserve against that same budget and spendable income. Here's its target, floor, current assigned cash and any refill needed. The refill needs an available source with its tax and costs included.

Once those agree, we can save the chosen spending, read it back and set the next review. An urgent income or loan change needs attention sooner. Next, we'll work on protecting the assets and access behind this plan.

**Overlay:**

Cue “that doesn't mean the target has been restored” → Capped correction ≠ target restored; cue “that same budget and spendable income” → Spending / income / Reserve / refill agree.

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

We're in Bitcoin access, connecting each holding to its custody arrangement. Start with the owner, what the money is for and who controls it today.

Put an intended move beside the current arrangement so the family can tell which process applies now. Then connect the person handling the ordinary work and the agreed backup from Trusted people.

Let's save and reopen the record to check it belongs to the right holding. Provider questions can stay with the next action. This map points to the protected recovery process without containing its secrets.

**Overlay:**

Holding / owner / current method / intended change / agreed person

**Verify:**

Saved record belongs to the correct holding; responsibility was actually agreed or is explicitly pending. No invented example household contact, provider right, insurance or completed transfer.

**Capture dependency:**

Verify Protect's Bitcoin access and Trusted people fields, ownership context, save/reopen behavior and the external map reference on the filming build. If a needed field is absent, show that part in the existing map without simulating an app control.

### Chapter 2 — Record actual recovery evidence

[Clean teleprompter take](teleprompter/walkthrough/W07-02.txt)

**Show:**

After 7.2 and the applicable D07 test, open the actual non-secret test receipt. Show separate rows for the isolated test wallet and each funded setup. Record only the date, method, scope and actual outcome.

**Narration:**

Let's use the recovery receipt to record the wallet checked, method, date and result.

If this is the separate test wallet, its result stays with that wallet. The funded setup keeps its own status until its appropriate safe check is complete. Buying a device or validating a word list doesn't establish full recovery.

For a funded setup with actual evidence, include the passphrase or multisig requirements covered by the check, without recording the sensitive material itself. Read the saved entry back: it needs to show what's verified and the safe next step for anything still open.

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

Prepare the non-secret custody entries for W08. Read the holding's legitimate access process, first contact and agreed backup. Link this existing map to the future family instructions; do not request or stage a separate rehearsal here.

**Narration:**

Before we leave Bitcoin access, let's make this holding's starting route clear. The family needs the legitimate process, first contact and agreed backup if the usual operator is unavailable.

We're preparing the custody part of the handoff here. Keep any missing contact or provider instruction as the next action. In the family walkthrough, we'll connect this same map to the person's legal authority and first-page instructions, then rehearse the complete route once it's ready.

**Overlay:**

Custody map / legitimate starting route / first contact / backup / ready for family handoff

**Verify:**

The non-secret map has a usable starting route or a precise open item. Contacts are agreed or explicitly pending. No separate rehearsal completion, transfer, impersonation, secret storage or legal authority is inferred.

**Capture dependency:**

Verify supported Protect map references and linkage to family instructions. Actual helper rehearsal and evidence belong to W08 chapter 3; no export or wallet-restoration claim is made by this chapter.

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

In Trusted people, connect the financial, healthcare and estate roles to the person who has agreed and the backup.

Now compare Estate documents with the current signed versions. For the financial power of attorney, we're checking durability, when authority takes effect and the powers granted. Keep a proposed role or unfinished document visible until the actual arrangement supports it.

In Who receives what, compare the primary and contingent beneficiaries with the institution's current record. If it differs from your intention, put the specific provider or document update on the action list.

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

Let's follow the custody map we prepared earlier and connect one holding to the person authorized for this situation.

For direct Bitcoin, that means a lawful route to protected recovery. Professional custody uses the provider's family-access process; a retirement account follows its beneficiary and distribution rules. Using the owner's login isn't a substitute for those processes.

Check incapacity and death separately, then identify the cash legally available for immediate household bills while the longer process is underway. A missing authority, access route or cash arrangement gives us a specific action to resolve.

**Overlay:**

Owner → authorized role → access process / immediate bills

**Verify:**

Lawful authority and technical access remain distinct. Cash availability is confirmed rather than assumed. No universal seed/passphrase split or inferred trust funding.

**Capture dependency:**

Verify provider procedures, supported Bitcoin access fields and the actual household documents. Keep unavailable or legally unresolved access explicit.

### Chapter 3 — Write and rehearse the first-page handoff

[Clean teleprompter take](teleprompter/walkthrough/W08-03.txt)

**Show:**

Open Instructions for your family and the existing Heir Letter. Reuse the Family Custody Map prepared in W07 chapter 4 and the Plan packet/Executor Packet references. Write the safe first paragraph, then perform the course's single family-handoff rehearsal with an agreed helper.

**Narration:**

In Instructions for your family, write the page someone can use when they're already under stress: the first person to contact, how to verify that contact and where to begin with household payments. Link the supporting account and document references from the existing packet.

Keep passwords, wallet secrets, sensitive configurations and exact secret-storage locations in the protected recovery process. Date this page and identify who keeps it current.

Now we'll rehearse the complete starting route. Let the agreed helper find the letter, first contact and backup without the usual operator coaching them. No credentials or money need to move. Correct an instruction that stops them and repeat that part; record the actual result or the step still pending.

**Overlay:**

Existing map + authority + first page → one rehearsal → actual result

**Verify:**

Reuse W07's custody preparation. Actual finding/opening and helper rehearsal evidence precede any success status. No sensitive recovery configuration, unperformed legal review, credentials or transfer. Sharing serves the agreed household purpose.

**Capture dependency:**

Verify editor/save behavior, Plan packet output and permitted references to existing protected records. Confirm actual helper consent and document accessibility.

### Chapter 4 — Verify the communication backstop

[Clean teleprompter take](teleprompter/walkthrough/W08-04.txt)

**Show:**

If no check-in service is used, show the findable family instructions and backup contact, then continue to chapter 5. Otherwise, open Check-in plan only after the filming build proves its actual capability. Read timing, recipient, cancellation and false-alarm behavior. Send only a separately agreed harmless test to an authorized recipient, or demonstrate the existing external service as external.

**Narration:**

If you use a check-in service, this is where we'll check how it delivers the family instructions. If you don't, continue to insurance with the findable instructions and backup contact you've already prepared.

Read the service's actual timing, recipient, trigger and cancellation or false-alarm process. Then use a harmless test agreed with the recipient. Label the message as a test and include no recovery secrets.

Check that it arrives and that the recipient can open the safe instructions. Until then, delivery stays unverified. Keep the independent route to those instructions even after the service works.

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

Open the insurance audit beside the actual policy. Work through one material loss, the household need, accessible resources and the benefit that applies.

The life-coverage illustration leaves a $100,000 gap: $400,000 of need, less $100,000 of separately available assets and $200,000 of coverage. It assumes zero return after inflation, taxes and fees, with later needs funded separately.

Use your own policy's benefit, term, waiting period and exclusions to judge the uncovered amount. Record whether you'll carry it or investigate a change, and update the related premium or future cost in Cash Flow or Life events.

Keep needed protection until any replacement is approved and active. Record the provider's effective date when coverage changes.

**Overlay:**

Illustration: $400k need − $100k assets − $200k coverage = $100k gap

**Verify:**

Actual benefits, needs and resources stay distinct; no invented insurance solver, quote, adopted example household policy or coverage cancellation. Necessary replacement must be active before recording old protection as safely removed.

**Capture dependency:**

Verify applicable Cash Flow/Life event fields and current policy evidence. Qualified review is specific to unresolved terms or the chosen transaction; no blanket attorney gate.

## W09 — [Complete a monthly review and an annual review](scripts/working/W09_complete-a-monthly-review-and-an-annual-review.md)

### Chapter 1 — Complete a quiet monthly review

[Clean teleprompter take](teleprompter/walkthrough/W09-01.txt)

**Show:**

From 9.1's monthly route, open Home. Read material issues, source dates, Your Money and any meaningful Recent Activity. Open the relevant account's How this account updates. Check Cash Flow's Your Plan uses, Reserve and confirmed upcoming Life events. Finish a genuinely quiet fixture without inventing an action.

**Narration:**

Home is our starting point for the monthly check. Read any material issue and the source dates. How this account updates shows what still needs input.

Compare the records with what you expected: contributions received, investments purchased and debt payments made. In Cash Flow, check the spending source, Reserve and upcoming confirmed events so the near-term needs are covered.

Then read the Plan's own date and status. Its result needs to include the current inputs before we interpret it.

If the facts are current and nothing needs a decision, that's this month's review finished.

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

Open the Annual Plan Refresh beside your previous dated plan. If this is the first review, start the record with today's plan.

Begin with spending and the Reserve. In retirement, read the proposed annual budget and refill together through the spending-review process. While working, check the Reserve target and funding pace against the household's current needs.

In Portfolio and allocation, look for a changed purpose or timeframe. A purchase getting closer may need a more dependable funding source. Compare a specific contribution or trade if it addresses that need; a price change alone doesn't require a rebalance.

For Debt, use the actual statement: balance, rate, required payment, maturity and repayment source. If a debt is paid off, confirm that before assigning its old payment to the next cash need or investment.

The tax review connects the year's income with relevant conversions, gains, losses and required distributions. Identify the records, proposed action and deadline while there's still time to act.

In Bitcoin access, check whether a device, provider, sign-in method or helper changed. Existing recovery evidence must still apply. Any new check needs the safe procedure for that setup; an annual review doesn't call for wiping a funded wallet.

Finish with family roles, ownership, beneficiaries, documents and insurance. Confirm that the people and arrangements still fit. Keep the changes you adopt and assign the outside work still needed; leave choices that continue to fit as they are.

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

Record the review date, adopted changes and reasons through supported views. Keep unresolved work with the existing action list. Create actual monthly/annual reminders externally if no app scheduler exists, and inspect their dates. Exporting the final report belongs to W10 chapter 5.

**Narration:**

Leave a short note of this review's date, what changed and why. The existing action list holds anything still needed, including a responsible person, due date and any condition it depends on.

Now set the monthly and annual reminders and check their dates. Keep collateral thresholds, tax deadlines, security issues and important life changes on their own timing.

When you come back, this record gives you a starting point. The final walkthrough will save the completed report alongside it.

**Overlay:**

Review date / adopted changes / open action / actual reminders

**Verify:**

Actual saved review record and created calendar reminders; no calendar event inferred from a note. Superseded instructions remain dated rather than current. Urgent obligations are not limited to scheduled reviews.

**Capture dependency:**

Verify supported review/action fields and the actual reminder mechanism. Use an external calendar if the app has no scheduler. Final report/export behavior is checked in W10 chapter 5.

## W10 — [Read, explain, and save the finished plan](scripts/working/W10_read-explain-and-save-the-finished-plan.md)

### Chapter 1 — Read one coherent saved plan

[Clean teleprompter take](teleprompter/walkthrough/W10-01.txt)

**Show:**

Open Plan → Overview, then Your Plan report. Check the active saved-plan identity, chance-of-success receipt, target date, spending, horizon and assumptions. Keep the existing Household Plan Summary beside the matching report; don't use landing-page figures.

**Narration:**

In Plan Overview, open the saved plan you intend to follow and its matching Your Plan report. Check the result date and status.

Read the retirement date, spending and planning horizon beside the assumptions and spending policy. Together they tell us what this chance-of-success result describes.

If there's missing information, identify it before relying on the result. If the facts are sound but the plan is weaker than you need, find the funding period or assumption driving the weakness and choose one practical response to compare.

Keep this same saved plan open as we follow the money.

**Overlay:**

One saved plan / date / spending / horizon / assumptions / limits

**Verify:**

Report and summary reference the same current receipt; stale/pending and missing-input status remain visible. No placeholder probability, invented retirement date, landing number or more optimistic assumption described as accuracy improvement.

**Capture dependency:**

Verify actual Your Plan report implementation, source/result identity, stale/pending states and missing-input explanations. Manuscript completion does not establish engine or report parity.

### Chapter 2 — Follow the important funding years

[Clean teleprompter take](teleprompter/walkthrough/W10-02.txt)

**Show:**

From the same result, open How retirement is funded/Retirement strategy and supported year details. Inspect the first retirement year, benefit start, material event and later tax-sensitive transition. Show actual income, complete spending, taxes, withdrawals, source accounts and remaining assets without fabricated attribution.

**Narration:**

Start with the first retirement year. Follow the income arriving, full spending need, taxes, debt payments and the amount that comes from assets. Read which accounts provide it and what remains afterward.

Then move to the next important funding change: a benefit begins, a major cost arrives or account access changes. Check that the source is available then and still supports its other jobs.

Read the Reserve and spending-response rules alongside those years. They show what changes if the plan weakens and how the response is funded.

An unresolved access rule or funding source stays visible with the next step to resolve it. The headline result doesn't fill that gap.

**Overlay:**

Critical year: income / complete spending / taxes / source / remaining resources

**Verify:**

Actual supported output and source attribution only. No invented account access, future benefit, dividend, loan payoff or result. Blocking uncertainty stays visible.

**Capture dependency:**

Verify year-level outputs, tax inclusion, withdrawal source attribution and policy links on the capture build. Pause a scene if the current output cannot support its claim.

### Chapter 3 — Finish the plan and share only when useful

[Clean teleprompter take](teleprompter/walkthrough/W10-03.txt)

**Show:**

From the same saved plan, identify the next real implementation action and any question blocking a major decision. Show its responsible person, timing/condition and completion evidence. Use the existing Household Plan Summary only for useful household sharing; do not replay earlier cash-flow arithmetic or create another scenario for completion.

**Narration:**

Now choose the next real action this plan needs. It may be completing an investment instruction, resolving an account-access question or finishing a family arrangement.

Give that action a responsible person, timing and the confirmation you'll use to know it's done. If it depends on a future event, keep that condition with it.

If you share finances, use the summary to talk through the retirement date, spending and important funding years together. Keep the calculations in the app and reuse the existing family handoff for emergency instructions. Any unresolved decision stays connected to the part of the plan where it can be addressed.

**Overlay:**

Next action / responsible person / timing or trigger / completion evidence

**Verify:**

Action belongs to the same saved plan; conditional money is not made available early. Household sharing is optional, with no invented learner outcome, submission or instructor approval.

**Capture dependency:**

Verify the saved-plan action record, actual evidence and matching summary. A conditional task needs its real trigger; outside implementation remains separate from saving the record.

### Chapter 4 — Prepare the specific professional handoffs

[Clean teleprompter take](teleprompter/walkthrough/W10-04.txt)

**Show:**

For an actual open issue only, prepare the existing focused CPA, estate, coverage or lending packet. Include decision, relevant evidence, exact question and deadline. Inspect any exported fields before saving for a recipient; no message is sent by this manuscript.

**Narration:**

If an open decision needs outside help, prepare the specific question and the records needed to answer it. Include the deadline.

For a tax question, that may mean the income, account and purchase details behind the proposed transaction. Estate access may need ownership, authority and provider requirements.

Read an export before sharing it. Remove unrelated information and keep recovery secrets out. Record whether the question is prepared, sent or awaiting an answer.

If you don't need that help for an open decision, continue to saving the report.

**Overlay:**

Decision / relevant evidence / exact question / deadline / actual status

**Verify:**

Professional handoff serves an actual open decision. No automatic message, appointment, filing, legal approval, completed transaction or professional response inferred. No full-backup sharing or sensitive custody material.

**Capture dependency:**

Verify export content/privacy, intended recipient and actual question. A professional prerequisite applies to the dependent decision, not every course action.

### Chapter 5 — Save the operating plan and implementation record

[Clean teleprompter take](teleprompter/walkthrough/W10-05.txt)

**Show:**

Save/reopen the dated Your Plan report and matching Household Plan Summary/action list through supported paths. Keep the existing review record and calendar schedule from W09. Inspect Profile → Data & privacy → Export for actual scope. Any supported restoration backup stays protected with separately verified restoration status; never restore over the member's live plan.

**Narration:**

Save the dated report beside the action list and reopen it to check that it matches the plan we've just read.

In Export, read what the file includes before keeping or sharing it. A report is for reading the plan. If the product supports a restoration backup, keep that sensitive file protected; its restoration capability needs a separate check.

You have the important funding years, the response rules and the next action together in this record. Use it as the starting point when the next review or real life change brings you back.

**Overlay:**

Matching dated report / existing action list / export scope / protected backup if supported

**Verify:**

Actual save/reopen, report/result identity and export scope. Restoration capability and status are separately evidenced; no restore guarantee, inferred outside completion or new reminder task. Keep W09's existing review schedule.

**Capture dependency:**

Verify Your Plan report and Profile export behavior, privacy and scope. A backup or safe restoration procedure cannot be promised from the future contract. Any restoration test needs actual supported capability in a disposable authorized environment; never restore over the member's live plan.
