# W02 — Verify cash flow, set the Reserve, and add expected events

Status: CONVERSATIONAL_CAPTURE_REVIEW — revised demonstration narration; actual app/device capture remains pending.
Kind: capture
Gate: APP_CAPTURE
Sources: CASHFLOW, DICTATION, OWNER, APP

### Production basis — not spoken

Use PR #227 accepted direction at reference head `21fedfbb1290bfdd637f3b0879bf7e7d6bfdbbc2`; the [latest directive](https://github.com/azeltwanger/orange-plan/pull/227#issuecomment-5618008737) governs future behavior. This is a capture manuscript, not proof that the planned screens or writers ship. The unchanged example household data and a separately reviewed synthetic extension supply all household facts. Use separate takes after the paired lessons. Only Narration blocks are spoken; overlays are added in editing. All amounts inside an app recording must come from its actual inputs and result. Common rules: [stepwise script standard](../../production/STEPWISE-SCRIPT-STANDARD.md).

#### Chapter 1 — Follow the monthly money · after 2.1

**Show:** Open Cash Flow → Income and Taxes and withholding, then the summary’s debt and saving routes. Reconcile original income with a synthetic pay-stub/statement source. Show the precise example household bridge as its own graphic.

**Narration:**

We've entered a starting monthly picture. Here we're checking whether it agrees with the records before using the amount left over. I'll begin with the income source, because gross pay still has deductions to account for while a bank deposit already has them taken out. In our example, the partner's ordinary business costs are deducted, but the equipment payment remains separate.

In our original teaching calculation, $1,275 before the client's $775 contribution becomes $500 afterward. The employer adds $387.50 to retirement money. Let's follow where the remaining household cash actually went: checking, saving or a cost we haven't included.

Any difference needs resolving at its source. A withholding change affects cash available and the amount still due; it doesn't by itself change the calculated tax obligation. Once the income side makes sense, we can look more closely at the spending period.

**Overlay:** Original example: $1,275 − $775 employee = $500; employer $387.50 separate

**Verify:** Income and deductions reconcile without double subtraction; original $10,800 living remains active. Actual tax output is not forced to the $4,000 teaching provision.

**Capture dependency:** D32/D48 income/withholding owners, employee election and business payment convention. Full-precision bridge and tax jurisdiction must be verified; synthetic records need actual period/timing. No reduction, Reserve transfer or future contribution starts here.

#### Chapter 2 — Verify spending and bill timing · after 2.1

**Show:** Open Cash Flow → Your Plan uses and Everyday spending → Verify Spending. Compare the method, source period and categories. Resolve one material uncertainty supported by the synthetic transaction set; show a purchase/settlement pair, annual bill and bill/payday timeline.

**Narration:**

Here we're checking the method and months behind the spending number. A recent permanent change may make newer records more useful, but the annual bills still need a place in that amount.

This grocery purchase is spending. The card payment settles it, so counting both would repeat the cost. Repayment of an older balance is a separate debt need. And a generic $1,200 annual premium represents $100 a month, even if eleven monthly statements don't show the bill.

Once the supported estimate is saved, let's look at when the money leaves. Checking needs enough for the bills before the next paycheck, with saving arranged around that need. That gives us a current amount we can trust before comparing a spending change.

**Overlay:** Method + source period · Purchase counted once · $1,200/year = $100/month

**Verify:** Supported classifications preserve raw evidence; no blanket exclusion of all card payments. The saved method/value agrees with the chosen period, annual costs and known recent changes.

**Capture dependency:** D32 selector methods (12-month average, Typical month, Recent 3-month trend, Manual), D33 category/correction behavior and saved readback. Capture only implemented methods. Annual premium and pay dates remain separate generic graphics unless the reviewed synthetic record supplies them.

#### Chapter 3 — Compare a sustainable spending change · after 2.1

**Show:** Use a Keep/Cut/Reduce teaching card beside the original spending. In Plan → Scenarios compare original living $10,800 with proposed $9,600, other inputs unchanged. Return to Current; use a clearly named reduced-spending rehearsal state for later course arithmetic only after the fictional choice is explicit.

**Narration:**

Now we can use the spending records to compare a change you'd actually make. With Keep, Cut and Reduce, we're asking which costs are worth their price, which you no longer choose and which could cost less without giving up something you need. Fees and lost coverage belong in that last decision.

Our example household's proposal cuts living costs by $1,200 a month. In the teaching example, that changes the amount available from $500 to $1,700. They still need to identify the bills that make it possible. We'll compare the proposal first, then record when the real change begins and update current spending once it has happened. Saving a lower figure doesn't cancel a service.

For the Reserve and Debt examples that follow, we're testing this reduced-spending version. Your actual surplus stays unchanged until those spending changes happen. Keep that distinction with the number as we move on.

**Overlay:** Proposed: living $10,800 → $9,600; available $500 → $1,700

**Verify:** Original and reduced states are distinguishable; no fabricated cancellations or early adoption. Saving amount, effective date and outside action are visible; $7,200 Reserve essentials are never substituted for normal living.

**Capture dependency:** Approved scenario/preview mechanism, effective-date semantics, return-to-Current and save/reload. Source does not itemize the $1,200 reduction. Actual app tax differences must be explained rather than balanced away.

#### Chapter 4 — Set the Reserve target and existing sources · after 2.3

**Show:** Open Cash Flow → Cash reserve, inspect essential spending and select months. Use What counts toward this reserve to assign eligible existing funds, including partial assignment only if implemented. Present $7,200 × 6 = $43,200; $32,000 assigned; $11,200 gap from one state.

**Narration:**

Let's give the Reserve a target using the essential costs from the lesson. Our example household's $7,200 includes required household debt, so we're not adding those payments again. Testing six months gives a $43,200 target.

Now we're looking at the existing money available for that job. Checking money for near-term bills, tax money and other committed amounts stay out of this assignment. Access matters too: pledged Bitcoin or money you can't readily use isn't the same as available cash.

The example assigns $32,000, leaving $11,200 to fund. We haven't added an asset; we've given existing money a job. After saving, I'll reopen the assignment so we can see the same sources and gap. Then we'll compare how quickly to close it beside the debt.

**Overlay:** Fictional: $7,200 × 6 = $43,200; minus $32,000 = $11,200 gap

**Verify:** Sources total once, remain their original assets and retain partial amounts on readback. Essential debt is not doubled. Target, assigned amount and gap share one state; unavailable/unpriced funds do not create a complete total.

**Capture dependency:** D49 reserve role and partial-assignment writer, eligibility, schema reconciliation and exact target/gap display. D32 Cash reserve ownership. Do not mimic a missing partial-assignment control or claim the teaching arithmetic is captured output.

#### Chapter 5 — Choose the Reserve pace beside Debt · after 2.3

**Show:** Carry the same gap into the approved Reserve funding/contribution owner. Show proposed $500/month beside the reduced-state $1,700 pool and anticipated $1,200 extra-card claim. Use a separate cash-coverage comparison for dependents or reliance on one income, then return to the unchanged example household split.

**Narration:**

We're still testing the reduced-spending version with $1,700 available. Your actual surplus stays unchanged until those spending changes happen. At $500 a month, the $11,200 Reserve gap takes 22.4 months, reaching the target with part of the twenty-third deposit before interest or withdrawals. That's almost two years to consider alongside the risk we're covering.

I'd give accessible cash more weight when dependents rely on one income and an interruption would otherwise require more borrowing. Building it faster may be worth slower extra-debt repayment, with required payments still covered. Our example household has a stable paycheck and variable business income; they aren't a single-income example.

Their proposed $500 Reserve pace leaves $1,200 of the same $1,700 for the card. We'll carry that split into Debt before settling it. The bank transfer comes after the combined decision, when we know the two choices fit together.

**Overlay:** Proposed: $500 Reserve + $1,200 extra card = $1,700 once

**Verify:** Pace is affordable from the same pool, gap stays visible and required payments remain covered. Faster Reserve is explained as a conditional trade-off, not a new example household contribution or fixed threshold.

**Capture dependency:** Actual contribution owner, pace save/readback and any affordability display. Final transfer is outside the app. Keep the 22.4 arithmetic off an app screen unless its semantics match; no invented calendar funding date or automatic recommendation.

#### Chapter 6 — Add an expected event and trace its funding · after 2.4

**Show:** Open Plan → Overview → Life events. Add the reviewed expected vehicle need and one person’s income change, with explicit recurrence and units. Inspect the affected year’s income/costs/funding. Put the possible renovation in Plan → Scenarios and return to Current. Rehearse a planned change becoming current.

**Narration:**

Here we're adding an expected change to the plan. The amount, date and frequency describe what happens: a vehicle purchase happens once, while an income change belongs to the person and period it affects. The dollar basis tells us whether we're using today's estimate or a future quote before applying inflation.

Let's follow it into the affected year and see how it's funded. Income, existing savings and an investment withdrawal leave different resources afterward. Adding the event tells the plan an expense is coming; it doesn't start a separate saving transfer.

We'll keep the possible renovation in its own comparison until it's chosen. And when a planned change becomes today's fact, the old event needs reconciling so it doesn't happen twice. If college is part of your plan, the next take applies this to its several years of payments. Otherwise, you're ready to carry the expected costs into Debt.

**Overlay:** Event: amount · timing · recurrence · units · funding

**Verify:** Expense and income changes occur once at the correct time/person; source funding is supported, not inferred. Renovation remains separate; planned-to-current update creates no duplicate effect.

**Capture dependency:** Life-event owner, supported source/account attribution, recurrence, inflation units, event-to-asset/debt treatment and save/readback. Example household vehicle timing is about three years; exact dates and amount need capture extension. Generic $30,000 car is not a fixture price. Unsupported attribution remains unresolved.

#### Chapter 7 — Fit education support beside the same cash · optional after 2.5

**Show:** Use Plan → Life events for the annual commitment and the existing education resource view/worksheet for assignment by child. Show $20,000 × 4 = $80,000; $58,000 split $29,000 each; $51,000 gap; $850/month flat-cost, no-growth benchmark over 60 months. Inspect actual modeled tuition years only with reviewed dates and account facts.

**Narration:**

Let's place the college commitment beside the money we've already assigned. In this example the parents intend to help with $20,000 a year for four years. Of the existing education money, $29,000 goes toward the older child's commitment, with the other $29,000 kept for the younger child. That leaves $51,000 to fund.

Having all of it ready in five years, with flat costs and no growth, takes $850 a month. But the proposed $500 Reserve and $1,200 extra card already use the $1,700 available. So the useful decision is what changes, or what still needs answering before the college commitment is funded.

If saving begins after the card ends, we'll recalculate with fewer months remaining. Then we can inspect the tuition years and the income and accounts actually paying them. That commitment goes with us into Debt, so the next choice doesn't use the same money again.

**Overlay:** $51,000 ÷ 60 = $850/mo; existing $1,700 is already assigned

**Verify:** Resources are allocated once, without changing ownership/beneficiaries. Benchmark assumptions stay visible; no extra $850 is silently saved. Actual future income and account funding support the chosen commitment or the unresolved trade-off.

**Capture dependency:** Reviewed dates, education owners/beneficiaries, qualification/tax treatment, timing and any event-specific account attribution. No aid award, return, auto-529 route or hypothetical loan is presumed. Use the worksheet when the exact benchmark is not a supported app result.

### Member checkpoint

The current monthly amount reconciles to records, and any proposed spending reduction remains separate until it happens. The Reserve has a target, eligible assigned sources, a visible gap and an affordable funding pace beside Debt. Expected events appear once at their dates, with their funding understood or a specific unresolved source identified. If college support applies, its amount and resources fit beside the same monthly money. Each chosen outside change has a next action; a planning entry alone is not a bank transfer or completed cancellation.

### Source and continuity notes — not spoken

The paired teaching scripts retain their deck/source IDs and dated research boundaries. Original dictation, accepted Reserve reference and prior manuscripts remain preserved; this stepwise rewrite follows Austin’s September 10 authorization. It changes no household fixture, financial model, provider state, learner account or real-world financial instruction. Build-dependent proof, final voice review and any qualified review remain separate.
