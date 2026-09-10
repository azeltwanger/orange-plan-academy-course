# W02 — Verify cash flow, set the Reserve, and add expected events

Status: FUTURE_DESIGN_CAPTURE_SCRIPT — complete prepared narration; actual app/device capture remains pending.
Kind: capture
Gate: APP_CAPTURE
Sources: CASHFLOW, DICTATION, OWNER, APP

### Production basis — not spoken

Use PR #227 accepted direction at reference head `21fedfbb1290bfdd637f3b0879bf7e7d6bfdbbc2`; the [latest directive](https://github.com/azeltwanger/orange-plan/pull/227#issuecomment-5618008737) governs future behavior. This is a capture manuscript, not proof that the planned screens or writers ship. The unchanged Reed fixture and a separately reviewed synthetic extension supply all household facts. Use separate takes after the paired lessons. Only Narration blocks are spoken; overlays are added in editing. All amounts inside an app recording must come from its actual inputs and result. Common rules: [stepwise script standard](../../production/STEPWISE-SCRIPT-STANDARD.md).

#### Chapter 1 — Follow the monthly money · after 2.1

**Show:** Open Cash Flow → Income and Taxes and withholding, then the summary’s debt and saving routes. Reconcile original income with a synthetic pay-stub/statement source. Show the precise Reed bridge as its own graphic.

**Narration:**

Open the income source and match its meaning to the records. Gross pay still has deductions to account for; the bank deposit already has them taken out. For Morgan, ordinary business costs are already deducted, but the equipment payment remains separate. In our original teaching calculation, costs leave $1,275 before Alex's $775 contribution and $500 after it. The employer adds $387.50 to retirement money. Now follow where the remaining cash actually went over the period: checking, saving, or a cost missing from the plan. Resolve that difference at its source. Withholding changes cash available and the amount still due; it doesn't by itself change the calculated tax obligation.

**Overlay:** Original example: $1,275 − $775 employee = $500; employer $387.50 separate

**Verify:** Income and deductions reconcile without double subtraction; original $10,800 living remains active. Actual tax output is not forced to the $4,000 teaching provision.

**Capture dependency:** D32/D48 income/withholding owners, employee election and business payment convention. Full-precision bridge and tax jurisdiction must be verified; synthetic records need actual period/timing. No reduction, Reserve transfer or future contribution starts here.

#### Chapter 2 — Verify spending and bill timing · after 2.1

**Show:** Open Cash Flow → Your Plan uses and Everyday spending → Verify Spending. Compare the method, source period and categories. Resolve one material uncertainty supported by the synthetic transaction set; show a purchase/settlement pair, annual bill and bill/payday timeline.

**Narration:**

Read the spending method and the months behind it. Use the records to decide whether that period describes the costs continuing now. A permanent change may make the recent period more useful, but annual bills still need coverage. Here, the grocery purchase is spending and the card payment settles it; counting both would repeat the cost. Keep repayment of an older balance separate. For a generic $1,200 annual premium, allow $100 a month rather than treating eleven months as free. Save the supported spending estimate, then look at payment timing. Keep enough in checking for bills that leave before the next paycheck, and arrange saving after that need is covered.

**Overlay:** Method + source period · Purchase counted once · $1,200/year = $100/month

**Verify:** Supported classifications preserve raw evidence; no blanket exclusion of all card payments. The saved method/value agrees with the chosen period, annual costs and known recent changes.

**Capture dependency:** D32 selector methods (12-month average, Typical month, Recent 3-month trend, Manual), D33 category/correction behavior and saved readback. Capture only implemented methods. Annual premium and pay dates remain separate generic graphics unless the reviewed synthetic record supplies them.

#### Chapter 3 — Compare a sustainable spending change · after 2.1

**Show:** Use a Keep/Cut/Reduce teaching card beside the original spending. In Plan → Scenarios compare original living $10,800 with proposed $9,600, other inputs unchanged. Return to Current; use a clearly named reduced-spending rehearsal state for later course arithmetic only after the fictional choice is explicit.

**Narration:**

Start with a cost you would actually change. Keep it when the value is worth the price. Cut an expense you no longer choose. Reduce the price or amount of something you still want, after checking fees and any lost coverage. The Reeds' proposal reduces living costs by $1,200 a month. In the teaching example that changes remaining money from $500 to $1,700. They still need to identify the bills that make the reduction possible. Compare the proposal first. Record when the real change begins, then update current spending when it has happened. Saving a lower figure doesn't cancel a service or make the saving appear in the bank. In the Reserve and Debt examples that follow, we're testing this reduced-spending version. Your actual surplus stays unchanged until the spending changes happen.

**Overlay:** Proposed: living $10,800 → $9,600; available $500 → $1,700

**Verify:** Original and reduced states are distinguishable; no fabricated cancellations or early adoption. Saving amount, effective date and outside action are visible; $7,200 Reserve essentials are never substituted for normal living.

**Capture dependency:** Approved scenario/preview mechanism, effective-date semantics, return-to-Current and save/reload. Source does not itemize the $1,200 reduction. Actual app tax differences must be explained rather than balanced away.

#### Chapter 4 — Set the Reserve target and existing sources · after 2.3

**Show:** Open Cash Flow → Cash reserve, inspect essential spending and select months. Use What counts toward this reserve to assign eligible existing funds, including partial assignment only if implemented. Present $7,200 × 6 = $43,200; $32,000 assigned; $11,200 gap from one state.

**Narration:**

Start with essential spending. The Reeds' $7,200 includes required household debt payments, so we don't add them again. We're testing six months, which gives a $43,200 target. Now choose what existing money counts. Leave checking money for near-term bills, tax money and other committed amounts out of this assignment. Check access as well as value; pledged Bitcoin or money you can't readily use isn't equivalent to available cash. The example assigns $32,000, leaving $11,200 still to fund. This is a job for existing money, not another asset. Save the assignment and reopen it to check the same sources and gap.

**Overlay:** Fictional: $7,200 × 6 = $43,200; minus $32,000 = $11,200 gap

**Verify:** Sources total once, remain their original assets and retain partial amounts on readback. Essential debt is not doubled. Target, assigned amount and gap share one state; unavailable/unpriced funds do not create a complete total.

**Capture dependency:** D49 reserve role and partial-assignment writer, eligibility, schema reconciliation and exact target/gap display. D32 Cash reserve ownership. Do not mimic a missing partial-assignment control or claim the teaching arithmetic is captured output.

#### Chapter 5 — Choose the Reserve pace beside Debt · after 2.3

**Show:** Carry the same gap into the approved Reserve funding/contribution owner. Show proposed $500/month beside the reduced-state $1,700 pool and anticipated $1,200 extra-card claim. Use a separate cash-coverage comparison for dependents or reliance on one income, then return to the unchanged Reed split.

**Narration:**

We're testing the reduced-spending version with $1,700 available. Your actual surplus stays unchanged until those spending changes happen. At $500 a month, the $11,200 gap takes 22.4 months, reaching the target with part of the twenty-third monthly deposit, before interest or withdrawals. Decide whether the household can carry that gap while income is interrupted. I'd give accessible cash more weight when dependents rely on one income and the bills otherwise need more borrowing. Building cash faster may be worth slower extra-debt repayment, with required payments still covered. The Reeds have a stable paycheck and variable business income; they aren't a single-income example. Their proposed $500 Reserve pace leaves $1,200 of the same $1,700 for the card. Keep that split visible when you move to Debt. Arrange the bank transfer only after the combined choice is settled.

**Overlay:** Proposed: $500 Reserve + $1,200 extra card = $1,700 once

**Verify:** Pace is affordable from the same pool, gap stays visible and required payments remain covered. Faster Reserve is explained as a conditional trade-off, not a new Reed contribution or fixed threshold.

**Capture dependency:** Actual contribution owner, pace save/readback and any affordability display. Final transfer is outside the app. Keep the 22.4 arithmetic off an app screen unless its semantics match; no invented calendar funding date or automatic recommendation.

#### Chapter 6 — Add an expected event and trace its funding · after 2.4

**Show:** Open Plan → Overview → Life events. Add the reviewed expected vehicle need and one person’s income change, with explicit recurrence and units. Inspect the affected year’s income/costs/funding. Put the possible renovation in Plan → Scenarios and return to Current. Rehearse a planned change becoming current.

**Narration:**

Enter the expected event with its amount, date and frequency. A vehicle purchase happens once; an income change belongs to the person and period it affects. Check whether the amount is today's estimate or a future quote before applying inflation. Now open the affected year and trace what funds the need. Income, existing savings and an investment withdrawal have different consequences for what remains. The event records an expense; it doesn't start a separate saving transfer. Keep the renovation in its own comparison until chosen. When a planned change later becomes today's fact, reconcile the old event too so the plan doesn't apply it twice.

**Overlay:** Event: amount · timing · recurrence · units · funding

**Verify:** Expense and income changes occur once at the correct time/person; source funding is supported, not inferred. Renovation remains separate; planned-to-current update creates no duplicate effect.

**Capture dependency:** Life-event owner, supported source/account attribution, recurrence, inflation units, event-to-asset/debt treatment and save/readback. Reed vehicle timing is about three years; exact dates and amount need capture extension. Generic $30,000 car is not a fixture price. Unsupported attribution remains unresolved.

#### Chapter 7 — Fit education support beside the same cash · optional after 2.5

**Show:** Use Plan → Life events for the annual commitment and the existing education resource view/worksheet for assignment by child. Show $20,000 × 4 = $80,000; $58,000 split $29,000 each; $51,000 gap; $850/month flat-cost, no-growth benchmark over 60 months. Inspect actual modeled tuition years only with reviewed dates and account facts.

**Narration:**

Record the help the parents intend to provide: $20,000 a year for four years in this example. Assign $29,000 of the education money to the older child and keep the other $29,000 for the younger child. That leaves $51,000 for the older child's commitment. Having it all ready in five years, with flat costs and no growth, takes $850 a month. Now put that claim beside the proposed $500 Reserve and $1,200 extra card payments. They already use the $1,700. Choose what changes or keep the college funding decision open. If saving starts after the card ends, recalculate with fewer months remaining. Then inspect the tuition years and the income and accounts actually funding them.

**Overlay:** $51,000 ÷ 60 = $850/mo; existing $1,700 is already assigned

**Verify:** Resources are allocated once, without changing ownership/beneficiaries. Benchmark assumptions stay visible; no extra $850 is silently saved. Actual future income and account funding support the chosen commitment or the unresolved trade-off.

**Capture dependency:** Reviewed dates, education owners/beneficiaries, qualification/tax treatment, timing and any event-specific account attribution. No aid award, return, auto-529 route or hypothetical loan is presumed. Use the worksheet when the exact benchmark is not a supported app result.

### Member checkpoint

The current monthly amount reconciles to records, and any proposed spending reduction remains separate until it happens. The Reserve has a target, eligible assigned sources, a visible gap and an affordable funding pace beside Debt. Expected events appear once at their dates, with their funding understood or a specific unresolved source identified. If college support applies, its amount and resources fit beside the same monthly money. Each chosen outside change has a next action; a planning entry alone is not a bank transfer or completed cancellation.

### Source and continuity notes — not spoken

The paired teaching scripts retain their deck/source IDs and dated research boundaries. Original dictation, accepted Reserve reference and prior manuscripts remain preserved; this stepwise rewrite follows Austin’s September 10 authorization. It changes no household fixture, financial model, provider state, learner account or real-world financial instruction. Build-dependent proof, final voice review and any qualified review remain separate.
