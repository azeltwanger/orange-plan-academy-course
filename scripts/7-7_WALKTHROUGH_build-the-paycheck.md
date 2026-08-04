# WALKTHROUGH 7.7 — build the paycheck in Orange Plan (screen share)

**One session, 11 steps (~17 min capture)**

**Before recording:**
□ Plan in RETIREMENT phase (several controls gate on currentAge ≥ retirementAge)
□ Baseline spending set · SS as a MONTHLY figure · reserve size decided
□ Run the Monte Carlo once (else the 3 confidence stops are placeholders with no $/yr)
□ ⚠ Target months offers None/1/3/6/12 only — an 18-month reserve must already be saved in the data; don't click for it
□ Demo household: $80k spend · $120k reserve · $400k taxable BTC · $600k trad · $200k Roth · $51,600/yr SS

---

**Open:** "You have your spending, floor, gap, bridge years, order, and guardrails. This walkthrough turns them into an actual paycheck the app runs on your numbers."

## □ 1 · Confirm the spending number
**Plan → Retirement → inputs row under the hero**
- **Baseline spending** ($/yr) + **Retire at age** · autosave chip "Saved ✓"
- ⚠ only place baseline spending is editable inline — Income page reads it, never sets it
- one number incl. healthcare + lumpy costs · debt payments stay OUT (carried separately)

## □ 2 · Healthcare-bridge expense
**Plan → Retirement → Life events → Add event → drawer "Add life event"**
- type **Expense Change** · Age = retirement age (60) · Amount = bridge premium · **Duration = 5** (retire 60, Medicare 65)
- ⚠ no "ending at 65" control — you set a duration · placeholder: "Leave empty for permanent"

## □ 3 · Build the floor (Social Security)
**Settings → Your Plan → Planning profile → Social Security**
- **Your SS Benefit = 4300 per month** ⚠ NOT 51600 — the field is monthly · SS Start Age 62-70
- "everything below this line arrives whether markets cooperate or not"
- ⚠ no "income floor" panel exists — the floor renders as **Income Floor** in the chart hover + stacked bands. Point at the chart.

## □ 4 · See the gap and the bridge
**Plan → Income → Income Blueprint tab** (heading "Retirement income" · section "Income sources")
- click a bar → drawer "Age {N} · {year}" → rows **Income Floor** + **Spending need**
- **Year-by-year detail → Retirement years → Gap column**
- count bridge years out loud × early-year gap
- ⚠ if the plan breaks: **"Shortfall starts age {N}"** pill top-right

## □ 5 · Set the withdrawal order — ⚠ SLOW DOWN
**Income Blueprint → Withdrawal order** (eyebrow "Income strategy" — controls are the page, no Advanced toggle)
- read the **outcome strip** first: **Bitcoin at {LE}** · **After-tax net worth at {LE}** · **Lifetime taxes** — live, signed deltas while unapplied
- 4 preset chips: Balanced · Preserve Bitcoin · Blended drawdown · Avoid early penalties (a chip just sets the controls)
- TWO separate orders: **Which accounts to draw from** (Default/Blended/Custom phases) + **What to sell inside an account** (Bitcoin last/Proportional/Blended/Custom) — ⚠ set BOTH
- ⚠ no "Tax bracket fill" chip — bracket-fill lives in **Custom phases → rule: Bracket-aware → pick ceiling** · engine already bracket-fills by default; the phase steers it · watch **Lifetime taxes** while doing it
- nothing saves while experimenting · **Apply to plan** commits · **Revert** walks back
- click at least two chips, watch Lifetime taxes vs Bitcoin at {age} trade off, say why you apply the one you do

## □ 6 · Calibrate the operating plan (95/80/60)
**Plan → Income → Retirement operating plan → What you can spend**
- 3 stops, all $/yr visible: Conservative 95% "more cushion" · Balanced 80% "your target" · Aggressive 60% "higher spend"
- click a stop → hero moves live, no save · **Recheck target ↻** → pill "Rechecked · on track for {year}"
- **Save starting target** ⚠ renders only in retirement phase
- ⚠ say once: 95-80-60 stops = the target you calibrate · 60-80-95 guardrails = annual triggers around it. Numbers overlap, jobs differ.
- policy copy names the band + "capped at 10% after inflation"

## □ 7 · The annual update (pre-met)
**Same section → Review annual update** (only when due)
- panel "Annual update ready" → tiles Prior / After inflation / 80% target / Saved target → Before/After bars → **Apply annual update**
- status row: Last checked / Last target update / Next eligible
- ⚠ inflation applies first, so nominal move can exceed 10% — the cap is on the REAL move
- ⚠ no refill status labels exist — the reserve read is the **Reserve buffer** strip: "{N} yrs · without selling investments"

## □ 8 · AI review: income plan
**Income Blueprint tab → Review income plan** (top right ⚠ only renders on this tab)
- asks: "What current retirement spending target would you like Orange Plan to use?"
- answer → wait → read one item, agree/disagree · run once order + guardrails are set
- ⚠ "explains and reviews. It isn't advice."

## □ 9 · Sell, borrow, or hold
**Plan → Income → Retirement Borrowing tab**
- modes: Bracket-aware · Borrow-first · Custom phases (legacy Sell → borrow on older plans) · ⚠ Sell-only is the comparison column, not a mode
- **Step-up basis on/off** toggle · line "{amount} debt at death repaid by estate · modeled, not advice"
- **Apply to plan → Applied ✓** / **Remove from plan** · ⚠ sandbox until Apply
- ⚠ no "estate value to heirs" figure here — family number = After-tax net worth; real estate surface = Protect → Projected legacy

## □ 10 · AI review: borrowing (only if borrowing is in the plan)
**Retirement Borrowing → Borrow vs sell · age {LE} → Review Borrowing Strategy**
- ask verbatim (demos well): "What BTC price or percentage drop do you want this strategy to withstand before a forced sale?" — answer with a real number
- ⚠ stress-tests the strategy. Won't approve a loan. · sell-only households skip

## □ 11 · Pressure-test
**Scenarios → What if... → 50% drawdown after retirement** ("The classic sequence-of-returns stress test")
- one click creates + selects · ⚠ in the first four cards, no See-more needed
- "that makes sequence risk visible on your own plan"

## □ WRAP — spot check
- three numbers from memory (spending / floor / gap) · bridge = count × gap, Bridge bucket actually that size
- confidence at/near 80 after saving (100 = over-saving — say why) · reserve buffer covers the bridge
- an applied withdrawal order you can defend · post-drawdown confidence dips but holds with a guardrail-sized adjustment
- "next module: protecting the Bitcoin this paycheck depends on" → END
