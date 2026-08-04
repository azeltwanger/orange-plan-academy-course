<artifact
  data-placement-id="outcomes-6a64f0a69381ba8c5122f7af"
  data-artifact-id="6a6754643a9be21a8d113311"
  data-params='{"items":["Enter every retirement-income input in the app","Set your withdrawal order and watch the outcome strip respond","Save a spending target at your chosen confidence stop","Run the 50% drawdown scenario to pressure-test your paycheck"]}'
></artifact>

# Walkthrough: build the paycheck in Orange Plan

You have your spending, floor, gap, bridge years, withdrawal order, and 60-80-95 guardrails. This walkthrough turns all of that into an actual retirement paycheck the app runs on your numbers.

Set aside about 20 minutes. This one only works when the plan is already in the retirement phase. Several controls are gated on `currentAge >= retirementAge`.

## Prerequisites

- Baseline spending set.
- Social Security amount known, as a monthly figure. The app's field is $/mo.
- Cash reserve size decided.
- Run the Monte Carlo once first. Until it runs, the three confidence stops fall back to placeholder positions with no $/yr labels.

⚠ Reserve months quirk: the **Target months** control offers only **None**, **1**, **3**, **6**, or **12 mo**. If your reserve is 18 months (for example $120k on $80k of spending), that value only renders if it's already saved in the data. Don't try to click your way to it.

## Step 1: Confirm the spending number

**Plan → Retirement**. The inputs row sits under the hero.

Field **Baseline spending** reads $/yr. Field **Retire at age** sits beside it. Autosave chip: **Saved ✓**.

⚠ This is the only place baseline spending is editable inline. The Income page reads it, never sets it.

Enter one number that includes healthcare and lumpy costs. Debt payments stay out of it. The app carries those separately, same as the Living row.

## Step 2: Add the healthcare-bridge expense

**Plan → Retirement → Life events → Add event** opens a drawer titled **Add life event**.

Type: **Expense Change**. *"Change in annual expenses."*

Fields:

| Field | Value |
|---|---|
| Age | Your retirement age (for example, 60). |
| Amount ($) | Your bridge premium (for example, the ACA plan cost). |
| Duration (years) | 5, if retiring at 60 and Medicare at 65. |

⚠ There's no "ending at 65" control on Expense Change events. You set a duration. The placeholder reads *"Leave empty for permanent."*

## Step 3: Build the floor (Social Security)

**Settings → Your Plan → Planning profile → Social Security** subheading.

| Field | Enter |
|---|---|
| Your SS Benefit | $4,300 **per month** (not per year). |
| SS Start Age | 62 to 70. |

⚠ The field is monthly. $51,600 per year goes in as **4300**, not **51600**.

Everything below this line arrives whether markets cooperate or not.

⚠ There's no "income floor" panel on the Income page. The floor renders as **Income Floor** in the projection-chart hover tooltip and as the stacked bands in the income-sources chart. Look on the chart, not for a numeric panel.

## Step 4: See the gap and the bridge

**Plan → Income → Income Blueprint** tab.

Page heading: **Retirement income**. Section eyebrow: **Income sources**. Subheading: **Where your money comes from**.

Click a bar on the chart to open a drawer headed **Age {N} · {year}**. Drawer rows include **Income Floor** and **Spending need**.

Open **Year-by-year detail → Retirement years** table. Look at the **Gap** column.

Count your bridge years out loud. Multiply by the early-year gap.

⚠ Shortfall pill: if the plan breaks, **Shortfall starts age {N}** appears top-right of the section.

## Step 5: Set the withdrawal order

**Plan → Income → Income Blueprint tab → Withdrawal order** (section eyebrow: **Income strategy**). The controls are the page now. Nothing hides behind an Advanced toggle anymore.

Read the **outcome strip** first. Three tiles, projected live from whatever the controls below say:

| Tile | What it is |
|---|---|
| **Bitcoin at {life expectancy}** | What's still unsold at the end. |
| **After-tax net worth at {life expectancy}** | The family-facing number. |
| **Lifetime taxes** | The cost of the order you chose. |

While you have unapplied changes, each tile shows a signed delta against your saved plan. That's the comparison now: move a control, watch the three numbers move.

Four preset chips: **Balanced · Preserve Bitcoin · Blended drawdown · Avoid early penalties**. A chip is a shortcut — it sets the controls below to that strategy's positions, nothing more.

Two segmented controls, and they are two separate orders:

| Control | Options |
|---|---|
| **Which accounts to draw from** | Default order, Blended, or **Custom phases**. |
| **What to sell inside an account** | Bitcoin last, Proportional, Blended, or Custom. |

⚠ Accounts and assets are two separate orders. Set both.

⚠ **There is no "Tax bracket fill" chip.** The bracket-fill move from Modules 5 and 6 lives in **Custom phases**: add a phase, set its rule to **Bracket-aware**, and pick the ceiling (an ordinary-income bracket or a capital-gains threshold). The engine's default withdrawal behavior already bracket-fills year by year — the phase control is how you steer it deliberately. Watch **Lifetime taxes** in the strip while you do.

Nothing saves while you experiment. **Apply to plan** commits the draft. **Revert** walks it back.

⚠ If you saw an earlier cut of this lesson: the comparison table (**Compare strategies**, winner badges, the **Lasts to** column) is gone. The live strip replaced it. Same three numbers, now updating as you click instead of rendering as a one-shot table.

## Step 6: Calibrate the operating plan (95 / 80 / 60)

**Plan → Income → Retirement operating plan → What you can spend**.

Three stops, all three $/yr amounts visible at once:

| Stop | Confidence | Label |
|---|---|---|
| Conservative | 95% | *"more cushion"* |
| Balanced | 80% | *"your target"* |
| Aggressive | 60% | *"higher spend"* |

Click a stop and the hero moves live. No save happens.

Run the Monte Carlo with the button **Recheck target ↻**. Status pill reads **Recheck needed** or **Rechecked · on track for {year}**.

Save with **Save starting target**.

⚠ The Save button only renders in the retirement phase. Pre-retirement, the copy reads *"The annual policy can be activated at retirement in {year}."*

⚠ The 95-80-60 stops are the target you calibrate to. The 60-80-95 guardrails are the annual triggers that flex around it. The numbers overlap; the jobs are different.

The policy copy names the band and the cap out loud: *"60% lower boundary, 80% target, 95% upper boundary,"* and *"capped at 10% after inflation."*

## Step 7: The annual update, pre-met

Same section, button **Review annual update** (only when an update is due).

Panel: **Annual update ready → {N}% confidence · {N}% inflation for {N} years**.

Four tiles: **Prior**, **After inflation**, **80% target**, **Saved target**.

Before-and-after bars: **Before / After**.

Button: **Apply annual update**.

Status row: **Last checked / Last target update / Next eligible**.

⚠ Inflation applies first, so the total nominal move can exceed the 10% cap. The cap is on the real (after-inflation) move.

⚠ No refill status is on this page. No "Refilling / Paused / Critical" label. The reserve read on this page is the **Reserve buffer** strip: *"{N} yrs / without selling investments,"* or *"No reserve built yet. Spending would sell investments from day one."*

## Step 8: Run the AI review on the income plan

**Plan → Income → Income Blueprint tab → Review income plan** (top right, beside the tab bar).

⚠ The button only renders on the Income Blueprint tab. Switch back if you don't see it.

The review reads: the page context, the on-screen verdict, and your retirement income plan. It also pulls income context, projection years, strategy comparisons, and the tax projection.

Clarifying question: *"What current retirement spending target would you like Orange Plan to use?"*

Answer, then wait while it runs. Read at least one thing it surfaced and say whether you agree.

**When to run it:** once the paycheck order and the guardrails are set. It's a second read on the whole income plan.

⚠ The review explains and reviews. It isn't advice.

## Step 9: Sell, borrow, or hold (Retirement Borrowing tab)

**Plan → Income → Retirement Borrowing** tab.

Modes:

- Bracket-aware
- Borrow-first
- Custom phases
- Legacy option **Sell → borrow** only on older plans.

⚠ Sell-only is the comparison column, not a mode.

Toggle: **Step-up basis on / off**.

Line: *"{amount} debt at death repaid by estate,"* *"modeled, not advice."*

Button: **Apply to plan → Applied to plan ✓**. Undo: **Remove from plan**.

⚠ Nothing moves in your plan until you click Apply. Before that, it's a sandbox.

⚠ There's no "estate value to heirs" figure here. The family-facing number is **After-tax net worth at {age}** in the Income tab's comparison table. The real estate surface is **Protect → Projected legacy**.

## Step 10: Run the AI review on Borrowing Strategy (only if borrowing is in the plan)

**Plan → Income → Retirement Borrowing tab → Borrow vs sell · age {life expectancy} → Review Borrowing Strategy**.

The review reads your Bitcoin loan settings, the Monte Carlo risk state, and the borrow-versus-sell comparison on screen.

Clarifying question (use this verbatim, it demos well): *"What BTC price or percentage drop do you want this strategy to withstand before a forced sale?"*

Answer with a real number. Then let it run.

**When to run it:** only when borrowing is actually in the plan. Sell-only households skip this.

⚠ The review stress-tests the strategy. It won't approve a loan for you.

## Step 11: Pressure-test with the 50% drawdown scenario

**Scenarios → What if... → 50% drawdown after retirement**.

Description ends: *"The classic sequence-of-returns stress test."*

One click creates the scenario and selects it under **Your scenarios**.

⚠ It's in the first four cards. No **See more scenarios** click needed.

That makes Lesson 4's sequence-of-returns risk visible on your own plan.

## What good looks like

- **Three numbers.** Spending, floor, gap. You can say them from memory off one screen.
- **Bridge years.** Count times early-year gap from the Gap column. The Bridge bucket on Strategy → Allocation is actually that size.
- **Confidence at the chosen stop.** At or near 80 after saving. 100 means you're over-saving. Say why on camera.
- **Reserve buffer.** Reads *"{N} yrs · without selling investments"* and covers the bridge.
- **Withdrawal order.** You clicked at least two preset chips, watched **Lifetime taxes** and **Bitcoin at {age}** trade off in the strip, and can say why you applied the one you did.
- **Post-drawdown confidence.** Dips, plan holds with a guardrail-sized adjustment.

## What got built

| # | Item | Where it lives |
|---|---|---|
| 1 | Retirement spending number | Plan → Retirement → Baseline spending |
| 2 | Bridge healthcare premium | Plan → Retirement → Life events → Expense Change |
| 3 | Social Security floor | Settings → Your Plan → Planning profile → Your SS Benefit |
| 4 | A chosen withdrawal order, applied | Plan → Income → Withdrawal order → Apply to plan |
| 5 | Saved spending target at a confidence stop | Plan → Income → Save starting target |
| 6 | (Optional) applied borrow strategy | Plan → Income → Retirement Borrowing → Apply to plan |
| 7 | Sequence-risk scenario, saved | Scenarios → 50% drawdown after retirement |

## Handing it off

The next module covers custody: how to operationally protect the Bitcoin your paycheck depends on.
