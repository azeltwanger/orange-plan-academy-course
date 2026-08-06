# 7.7 · WALKTHROUGH — Build the paycheck

**Screen capture · 11 steps · ~17 min**

> **DO** = click path · **SEE** = point at this · **⚠** = don't get this wrong
> Narrate in your own words. Nothing here is scripted.

---

## Before you record

- [ ] Plan in **RETIREMENT phase** (several controls gate on currentAge ≥ retirementAge)
- [ ] Baseline spending set · SS entered as a **MONTHLY** figure · reserve size decided
- [ ] **Run the Monte Carlo once** — else the three confidence stops are placeholders with no $/yr
- [ ] Target months offers None/1/3/6/12 only. An 18-month reserve must already be in the plan data — don't click for it
- [ ] Demo household: $80k spend · $120k reserve · $600k taxable BTC · $400k trad · $200k Roth · $51,600/yr SS (combined)
- [ ] Clean browser, notifications off

---

## □ 1 · Confirm the spending number

**DO** Plan → Retirement → inputs row under the hero

**SEE** **Baseline spending** ($/yr) + **Retire at age** · autosave chip *"Saved ✓"*

**⚠** This is the only place baseline spending is editable inline. The Income page reads it, never sets it.

**⚠** One number, including healthcare and lumpy costs. Debt payments stay OUT — they're carried separately.

---

## □ 2 · Healthcare-bridge expense

**DO** Plan → Retirement → Life events → **Add event** → drawer *"Add life event"*

**DO** Type **Expense Change** · Age = retirement age (60) · Amount = bridge premium · **Duration = 5** (retire 60, Medicare 65)

**⚠** There's no "ending at 65" control. You set a duration. Placeholder reads *"Leave empty for permanent."*

---

## □ 3 · Build the floor (Social Security)

**DO** Settings → Your Plan → Planning profile → Social Security

**DO** Your SS Benefit = **4300 per month**

**⚠ NOT 51600.** The field is monthly. This is the single most common entry error in the app.

**DO** SS Start Age 62–70

**⚠** Everything below this line arrives whether markets cooperate or not.

**⚠** There's no "income floor" panel. The floor renders as **Income Floor** in the chart hover and the stacked bands. Point at the chart.

---

## □ 4 · See the gap and the bridge

**DO** Plan → Income → **Income Blueprint** tab (heading *"Retirement income"* · section *"Income sources"*)

**DO** Click a bar → drawer *"Age {N} · {year}"*

**SEE** Rows **Income Floor** + **Spending need**

**DO** **Year-by-year detail → Retirement years → Gap column**

**⚠** Count the bridge years out loud and multiply by the early-year gap. That product is the whole Bridge bucket.

**SEE** If the plan breaks: **"Shortfall starts age {N}"** pill, top right

---

## □ 5 · Set the withdrawal order — SLOW DOWN

**DO** Income Blueprint → **Withdrawal order** (eyebrow *"Income strategy"* — the controls are the page, no Advanced toggle)

**SEE** Read the **outcome strip** FIRST: **Bitcoin at {LE}** · **After-tax net worth at {LE}** · **Lifetime taxes** — live, signed deltas while unapplied

**SEE** Four preset chips: Balanced · Preserve Bitcoin · Blended drawdown · Avoid early penalties

**⚠** A chip just sets the controls. It isn't a separate mode.

**DO** Set BOTH orders — they're separate:
- **Which accounts to draw from** (Default / Blended / Custom phases)
- **What to sell inside an account** (Bitcoin last / Proportional / Blended / Custom)

**⚠** There's no "Tax bracket fill" chip. Bracket-fill lives in **Custom phases → rule: Bracket-aware → pick ceiling**. The engine already bracket-fills by default; the phase steers it. Watch **Lifetime taxes** while you do it.

**⚠** Nothing saves while you experiment. **Apply to plan** commits, **Revert** walks it back.

**DO** Click at least two chips, watch Lifetime taxes trade off against Bitcoin at {age}, and say why you apply the one you apply

---

## □ 6 · Calibrate the operating plan (95/80/60)

**DO** Plan → Income → Retirement operating plan → **What you can spend**

**SEE** Three stops, all with $/yr visible: Conservative 95% *"more cushion"* · Balanced 80% *"your target"* · Aggressive 60% *"higher spend"*

**DO** Click a stop → hero moves live, nothing saves → **Recheck target ↻** → pill *"Rechecked · on track for {year}"*

**DO** **Save starting target**

**⚠** That button renders only in retirement phase.

**⚠** Say this once, clearly: the 95-80-60 stops are the target you calibrate. The 60-80-95 guardrails are the annual triggers around it. The numbers overlap, the jobs are different.

**SEE** Policy copy names the band + *"capped at 10% after inflation"*

---

## □ 7 · The annual update (pre-met)

**DO** Same section → **Review annual update** (renders only when due)

**SEE** Panel *"Annual update ready"* → tiles Prior / After inflation / 80% target / Saved target → Before/After bars → **Apply annual update**

**SEE** Status row: Last checked / Last target update / Next eligible

**⚠** Inflation applies first, so the nominal move can exceed 10%. The cap is on the REAL move.

**⚠** There are no refill status labels. The reserve read is the **Reserve buffer** strip: *"{N} yrs · without selling investments."*

---

## □ 8 · AI review — income plan

**DO** Income Blueprint tab → **Review income plan** (top right)

**⚠** It only renders on this tab.

**SEE** Asks: *"What current retirement spending target would you like Orange Plan to use?"*

**DO** Answer → wait → read one item, agree or disagree

**⚠** Run it once the order and guardrails are set, not before.

**⚠** It explains and reviews. It isn't advice.

---

## □ 9 · Sell, borrow, or hold

**DO** Plan → Income → **Retirement Borrowing** tab

**SEE** Modes: Bracket-aware · Borrow-first · Custom phases (legacy Sell → borrow on older plans)

**⚠** Sell-only is the comparison column, not a mode.

**SEE** **Step-up basis on/off** toggle · line *"{amount} debt at death repaid by estate · modeled, not advice"*

**DO** **Apply to plan → Applied ✓** / **Remove from plan**

**⚠** It's a sandbox until you Apply.

**⚠** There's no "estate value to heirs" figure here. The family number is After-tax net worth; the real estate surface is Protect → Projected legacy.

---

## □ 10 · AI review — borrowing (only if borrowing is in the plan)

**DO** Retirement Borrowing → Borrow vs sell · age {LE} → **Review Borrowing Strategy**

**DO** Ask it verbatim (this demos well): *"What BTC price or percentage drop do you want this strategy to withstand before a forced sale?"* → answer with a real number

**⚠** It stress-tests the strategy. It won't approve a loan.

**⚠** Sell-only households skip this step entirely.

---

## □ 11 · Pressure-test

**DO** Scenarios → What if... → **50% drawdown after retirement** (*"The classic sequence-of-returns stress test"*)

**⚠** It's in the first four cards. No See-more needed.

**⚠** That's sequence risk made visible on their own plan — the abstract risk from 7.6 with their numbers in it.

---

## □ WRAP — spot check off the screen

- [ ] Three numbers from memory: spending / floor / gap
- [ ] Bridge = count × gap, and the Bridge bucket is actually that size
- [ ] Confidence at or near 80 after saving (100 means over-saving — say why)
- [ ] Reserve buffer covers the bridge
- [ ] An applied withdrawal order you can defend out loud
- [ ] Post-drawdown confidence dips but holds with a guardrail-sized adjustment

**END**
