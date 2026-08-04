# Unit 5 · Module 4 — Debt Strategy

*See debt as a tool, set your tolerance, read the two ratios with their guideline bands, watch LTV drift on Bitcoin-backed loans, know the four offense plays, and assign every debt a job.*

## 5.1 Defense: tolerance first, then the two ratios
*`TEACH + APP` · 1,077 words · ~5 min*

**By the end of this lesson, you can:**

- Know your own debt tolerance before running any math
- Calculate your debt-to-income and debt-to-assets
- Have every debt in the app with complete terms
- Read your verdict line and your stress number

---
Most people ask how fast they can get to zero debt. A better question: what level of debt lets this plan grow without making it fragile?

This module covers both sides. Defense (the debt that keeps you safe) and offense (the debt that actually builds wealth). Start with defense, because defense sets the boundaries offense gets to play inside of.

### Tolerance first

The math sets a range. Your psychology decides where you sit inside it.

Peace of mind is a real return. It never shows up in a ratio. If you're carrying a debt level that keeps you up at night, you'll probably abandon the plan in the middle of a drawdown, which is a bigger risk than the interest rate.

If carrying no debt lets you sleep, that's the right answer for you. The rest of this module still helps you decide what to clean up first.

Be honest about which one you have. Debt that annoys you and debt that keeps you up at night are two different problems with two different answers.

### Debt as a tool

Debt isn't just a problem to eliminate. Held on purpose, debt does three jobs:

1. **Liquidity.** Cash stays accessible. Bad month, you cover bills without forced-selling into a drawdown.
2. **The spread.** Cheap debt vs higher expected returns. Invest the difference. Every dollar of 3% debt held while capital earns more than 3% is earning you the spread (Lesson 3).
3. **Tax advantage.** Borrow instead of selling, avoid capital gains. Keep the Bitcoin, get the cash (Lesson 3 and Module 5).

Businesses hold debt on purpose because it lets them grow. The right question isn't "how do I get to zero?" It's "what level helps me grow?"

### The two ratios

#### Debt-to-Income (DTI)

**Total monthly debt payments ÷ monthly income (before tax).**

Measures monthly survival. Debt gets paid out of cash flow, so this is the share of every paycheck already committed before you've bought groceries.

DTI is your stability anchor. It barely moves in a Bitcoin drawdown, because it's driven by income, not asset prices.

| DTI | Status |
|---|---|
| Under 36% | Healthy |
| 36 to 43% | Acceptable |
| Over 43% | High-risk |

#### Debt-to-Assets (DTA)

**Total debt ÷ total assets.**

Measures capacity: how much of what you own is already spoken for. This one moves with the Bitcoin price (next lesson).

| DTA | Status |
|---|---|
| Under 30% | Healthy |
| 30 to 60% | Caution |
| Over 60% | High-risk |

For most households, 10 to 40% is workable. A healthy business runs 30 to 60% DTA depending on the industry.

**DTI asks whether you survive this month. DTA asks how much room you've got to make a move at all.**

### The couple's numbers

Income: $190,000/yr = $15,800/mo gross.

- Debt: $280,000 mortgage at 3.25% + $18,000 car loan at 7% = **$298,000**
- Assets: $175k BTC + $90k funds + $30k cash + $450k house = **$745,000**

**DTA:** $298k ÷ $745k = **40%.** Top of the workable range.

**DTI:** ~$1,850/mo payments against $15,800/mo income = **~12%.** Well inside healthy.

Two different reads. Their monthly is fine. Their balance sheet is at the ceiling. Both are true. And DTA is the one that moves when Bitcoin does.

So those are your two ratios on paper. Now let's get them out of your head and into the app, because the app runs the stress test on top of them, and that's the number you actually manage against.

> 🎥 **SCREEN SHARE STARTS HERE — capture segment 5.1-B.** Everything above is teleprompter A-roll (segment 5.1-A); everything below is screen capture. This heading is the edit cut point.

### Now put it in the app

Set aside about five minutes. Have every debt's balance, rate, minimum payment, and term ready.

⚠ There's no fixed/variable field on a debt in this app. Don't hunt for one.

#### Step 1: Enter every debt

**Strategy → Debt → Add debt** opens the **Add debt** dialog.

Fields, in order:

| Field | Notes |
|---|---|
| Name | For example, "Auto loan" or "First Fidelity mortgage." |
| Type | Mortgage, Credit Card, Auto, Student, BTC-Backed Loan, and so on. |
| Current balance ($) | (n/a) |
| Interest rate (%) | (n/a) |
| Monthly payment ($) | (n/a) |
| Term (months) | (n/a) |

Type-specific fields:

- **Mortgage.** *Payment includes:* principal + interest, or total servicer payment.
- **Credit card or revolving.** *Credit limit / total available ($)*.

Watch for two live diagnostics:

- **Payment below the interest.** The dialog warns: *"Payment doesn't cover interest. Balance will grow."*
- **Healthy payment.** The dialog prints: *"Paid off in ~Nyr Nmo (N payments)."*

Empty state before you add anything: **No debt tracked** and **Add Your First Debt**.

#### Step 2: Read the vitals strip

**Strategy → Debt** shows a four-cell **Debt vitals** strip:

| Cell | Sub-caption |
|---|---|
| Total debt | (n/a) |
| Monthly payments | (n/a) |
| Debt-to-assets | *caution above N%* |
| Debt-to-income | *high-risk above N%* |

Hover the **Ratio bands** tooltip to see the full bands.

- **DTI** is your stability anchor. It barely moves when Bitcoin moves, which makes it the floor to watch.
- **DTA** is the balance-sheet lens. It moves with the Bitcoin price, which is why we manage the drift.

⚠ The DTI cell only renders when your income is known. If it's missing, go back to Cash Flow → Income and add it.

#### Step 3: Read the verdict line

**Strategy → Debt → Financial position**. This is the sentence rendered above the vitals strip.

One-word status, then dot-separated clauses:

| Word | Read |
|---|---|
| Strong | Healthy. Inside your bands, including the stress read. |
| Elevated | Not a failure. It's the agenda for the next 12 months. |
| Stretched | The plan needs a change, not the market. |

The stress clause reads: *"stress test reaches N% of assets."*

⚠ This is the number that matters for a Bitcoin-heavy balance sheet. If a normal bear takes it past your comfort, the leverage is too big. Re-read this at every annual review. It moves with the price, even when your debts don't change.

Common clauses you'll see mixed in:

- *"both ratios inside your bands"*
- *"debt-to-assets in the caution band"*
- *"both ratios above your bands"*

You've got a verdict word and a stress number. Both of them move when Bitcoin moves, and the next lesson is about what to do when they do.

## 5.2 Drift and the LTV cushion
*`TEACH + APP` · 824 words · ~4 min*

**By the end of this lesson, you can:**

- Understand how DTA moves with the Bitcoin price
- Calculate LTV and how far Bitcoin can drop before liquidation
- Size a loan-to-value cushion that survives a normal Bitcoin drawdown

---
Two dynamics that make a Bitcoin balance sheet different from everybody else's.

### Your DTA moves with Bitcoin

Your debt-to-assets ratio doesn't sit still. It moves with the Bitcoin price:

- **Bitcoin up.** DTA drops. Room opens up. You feel safe. You want to borrow more. Usually right near the top.
- **Bitcoin down.** DTA spikes at the exact moment your stress is peaking. If there's no room left, that's where forced selling happens.

The couple landed at 40% DTA with $298,000 debt against $745,000 assets:

- **Bitcoin doubles:** $175k becomes $350k, total assets $920k, DTA drops to **32%.** 8 points of room without doing anything.
- **Bitcoin halves:** $175k becomes $87.5k, total assets $658k, DTA climbs to **45%.** Same debts, same payments. Over the workable range.

The ratio tells you about today's price, but the decision you're making lives for years. Room looks real at the moment it's least real.

**Stay conservative when Bitcoin is high. Use your room when Bitcoin is low.** Anchor to where Bitcoin has been, not to what it's printing today. Use DTI as your floor, since it doesn't move with price.

Austin's own experience: his net worth dropped 75% in 2022. He could hold because nothing on his balance sheet could force him to sell.

### The LTV cushion

For any borrowing backed by your Bitcoin, there's a gap between where your loan starts and the line where the lender takes over. That gap is the entire drawdown you can live through.

**LTV** = loan-to-value = your loan divided by your collateral's current value.

- Your **loan balance** is fixed. It doesn't move when Bitcoin moves.
- Your **collateral value** moves with the price.

If Bitcoin falls, your collateral shrinks, LTV climbs, and it climbs toward the lender's liquidation line. Your starting LTV sets the entire survivable drop.

If you hit the line, the lender force-sells your Bitcoin. At the worst possible moment.

### The math

Say you post $50,000 of Bitcoin as collateral, and the lender's liquidation LTV is 80%.

**Scenario A: borrow $12,500 (25% starting LTV).**

- Liquidation collateral value = $12,500 ÷ 0.80 = **$15,625**.
- Bitcoin has to fall from $50,000 to $15,625 for a margin call. A **69% drop**. Right at the edge of Bitcoin's historical drawdowns (2018: -84%, 2022: -77%). Not enough cushion.

**Scenario B: borrow $6,250 (12.5% starting LTV).**

- Liquidation collateral value = $6,250 ÷ 0.80 = **$7,812**.
- Bitcoin has to fall from $50,000 to $7,812. An **84% drop**. Now you can survive a 2018-style bear.

Cut the starting LTV in half, and the danger line moves much further away.

### Size the cushion for a normal drawdown

If you're borrowing against Bitcoin, size the cushion to survive a **70 to 80% drawdown minimum**. That's the normal Bitcoin cycle, not a worst case.

Usually means starting at **20 to 25% LTV**, not 40 to 50%. Anything higher, and a normal Bitcoin bear becomes a forced-sale event at the worst possible moment.


So that's the math on the cushion. The app draws it, which is easier to read than the arithmetic.

> 🎥 **SCREEN SHARE STARTS HERE — capture segment 5.2-B.** Everything above is teleprompter A-roll (segment 5.2-A); everything below is screen capture. This heading is the edit cut point.

### Now put it in the app

#### Step 4: Debt capacity track

**Strategy → Debt → Debt capacity**.

Three zone bands render side by side: **safe, caution,** and **high-risk**.

A marker on the track reads: *"today N.N%."*

Threshold labels beneath: **$0** and **caution N%**.

⚠ Use this to see the drift rule visually. Be conservative when Bitcoin is high (DTA looks low, but that's your cushion). Use the room when Bitcoin is low (DTA looks high, but that's when the cushion is meant to be used). See the drift lesson for the math behind that.

#### Step 6: Name the LTV cushion (Bitcoin-backed loans only)

No Bitcoin-backed loan? Skip this step.

If you have one: **Strategy → Debt → the Bitcoin-backed loan row**. The row shows **LTV N%** inline. Click the name to open the detail view.

Detail sub-header: **Bitcoin-backed loan**.

The track shows ticks for **margin call N%** and **liquidation N%**.

Tiles: **Loan balance**, **Collateral**, **Collateral value**, **Interest rate**.

⚠ A healthy loan shows no cushion sentence and no severity chip. That's healthy, not missing data.

Once severity is past healthy, a line appears: *"A N% drop triggers a margin call at $X BTC · liquidation at $Y."* Read both the percent and the dollar amount. Those numbers tell you the exact drop you can survive before you borrow a cent.

The three severity chips:

| Chip | Read |
|---|---|
| near margin call | This week's problem. Reduce LTV. |
| margin call | Today's problem. Add collateral or pay down now. |
| liquidation zone | Emergency. |

⚠ **Watch** is not a severity word on screen. It's an internal state that renders no chip.


Everything so far has been defense: know your ratios, protect the cushion, don't get liquidated. The next lesson is the other half, which is what debt is actually for.

## 5.3 Offense: the four debt plays
*`TEACH + APP` · 883 words · ~4 min*

**By the end of this lesson, you can:**

- Understand the four offensive debt plays and what each earns
- Recognize the failure mode of each play
- Match a household to the right play (or to none)
- Write operating rules before taking on Bitcoin-backed debt

---
Defense set the boundaries. This lesson covers the other half: how debt actually builds wealth.

Four plays. Each with a failure mode. Leverage is a power tool: it can help you build faster, but it can take your hand off.

### Play 1: The spread

Borrow at a low rate. Keep your capital invested in something you expect to outperform that rate. Compound the difference.

**The spread** = what your money earns minus what your debt costs.

Every dollar of 3% debt held while capital earns more than 3% is earning you the difference. Paying that debt off early doesn't earn a return. It just stops the interest at exactly the debt's rate, guaranteed, and gives up whatever the capital could have done instead.

**Austin has done this himself:** put 5% down on his house instead of 20%. The difference went into Bitcoin. He still carries that mortgage on purpose.

#### Failure mode

The spread is expected; the payment is a certainty.

- Payment strains your cash flow → bad.
- Asset underperforms for years → bad.
- Variable rate resets upward → spread narrows or flips.

Only counts when the payment is comfortable **and** the reserve is solid.

### Play 2: Borrow, don't sell

Instead of selling Bitcoin, access liquidity by borrowing against it. **Loan proceeds generally aren't taxable.** You're getting cash without triggering capital gains, and your Bitcoin position stays intact.

Why isn't a loan taxed? You haven't made anything on it. You borrowed money you have to pay back. Selling turns paper gains into real ones, which is when tax shows up.

Strong when you have:

- A large, low-basis position where selling means a big tax bill
- An expense that fits your plan
- A solid reserve
- A conservative LTV

#### Failure mode

The weak version is "borrow instead of ever selling."

A Bitcoin-backed loan brings four risks at once:

1. **Liquidation risk.** Bitcoin drops enough, they force-sell.
2. **Interest cost.** The loan isn't free.
3. **Counterparty risk.** Your lender can fail.
4. **Repayment risk.** In a long bear, you have a loan you can't pay off without selling anyway.

A loan that's fine at 30% LTV becomes a crisis if Bitcoin gets cut in half.

The play gives you the choice of *when* to sell, rather than avoiding selling altogether. Only holds if the cushion holds.

### Play 3: Strategic Bitcoin-backed borrowing

Used deliberately, a drawdown is the moment to borrow into strength. Access liquidity or buy more when the rest of the plan is solid.

#### Austin's two guardrails

**1. Cap concentration.** Austin is careful about putting more than 10 to 20% of Bitcoin with any single lender. Some portion will always stay in cold storage, never seeing a lender.

**2. Operating rules written before any money moves:**

- **Purpose.** What specifically will this money be used for?
- **Maximum LTV.** The ceiling.
- **Top-up trigger.** The LTV level where you add collateral.
- **Repay trigger.** The LTV level where you pay down principal.
- **No-go conditions.** Situations where you close the loan immediately.
- **Monitoring.** Who watches it, how often.
- **50-80% drawdown plan.** The exact steps when Bitcoin falls hard.

Every hard call made in advance of the day you'd make it badly.

#### Failure mode

Starting at a high LTV turns a normal bear into a crisis. New leverage to buy Bitcoin demands a much higher standard than keeping existing low-rate debt.

### Play 4: Keep low-rate debt on purpose

The "why would I pay off a 3% mortgage" move. If the capital works harder inside the plan **and** the payment is comfortable, retiring cheap debt early is the worse choice. Guaranteed low return, given-up flexibility.

A cheap mortgage is an asset you're holding on purpose. Keep it as long as the payment is comfortable.

#### Set up credit access before you need it

Establish a HELOC or credit line while your income is strong, then leave it alone. Puts the option in place while lenders are happy to give it. Their enthusiasm evaporates at exactly the moment you'd want the line most.

#### Failure mode

An unused line can still tempt you into bad decisions. Variable rates can reset against you. Operating rules first.

### The retirement variation

Play 2 has a retirement version: borrowing against Bitcoin instead of selling to create retirement income. The app compares three borrowing strategies against a sell-only baseline:

- **Bracket-aware.** Borrows only up to a tax bracket you set, then switches to selling.
- **Borrow-first.** Leans on the loan before it sells anything.
- **Custom phases.** Switch strategies by age.

Module 6 covers this in depth.

### Every play is a comparison

Each of the four plays is a comparison, not a rule. Each only works inside the boundaries defense set.


So let's run one. Pick the play you're most tempted by and put it against your own baseline.

> 🎥 **SCREEN SHARE STARTS HERE — capture segment 5.3-B.** Everything above is teleprompter A-roll (segment 5.3-A); everything below is screen capture. This heading is the edit cut point.

### Now put it in the app

**Scenarios → Custom scenario** to compare pay-off-versus-invest.

Model one play against your baseline. Read the confidence number both ways. Your target debt range is a spoken decision — there's no field for it in the app.

You've seen what one play does to your plan. Now every debt on the ledger needs a decision, including the ones you're keeping.

## 5.4 Every debt gets a job
*`TEACH + APP` · 1,085 words · ~5 min*

**By the end of this lesson, you can:**

- Break the 'pay off debt or invest?' question into three separate decisions
- Sort each debt into eliminate, evaluate, strategic, or monitor by its rate
- Give every debt on your balance sheet a job and a reason

---
The module finishes when every debt on your balance sheet has a **job** attached to it, with a reason why.

### Three questions, not one

When there's surplus money at the end of the month, most people ask one question: *"Should I pay off debt first?"*

That's actually three separate decisions:

1. **Keep stacking.** Continue Bitcoin accumulation from monthly surplus.
2. **Pay down faster.** Accelerate payoff on debt you already have.
3. **Add new leverage.** Take on new debt to buy Bitcoin.

Each one gets a different standard, because each one carries a different risk:

- **Buying Bitcoin from surplus** risks money you already own.
- **Paying debt down faster** trades a guaranteed return for flexibility you give up.
- **Adding new leverage** risks money you don't have yet, against an asset that can fall 80%.

Austin's own household in one year: yes on 1, no on 2 (kept the mortgage), no on 3 (didn't add new leverage). Three separate answers on one balance sheet.

### The six possible jobs

Every debt on your list gets one of these, plus a reason:

- **Minimum only.** Pay the required payment, nothing extra.
- **Extra principal.** Pay above the minimum.
- **Refinance.** Get a better rate.
- **Consolidate.** Combine at a better rate.
- **Pay off in full.** Kill it.
- **Monitor.** For asset-backed loans, watched by LTV and cushion, not by rate.

### The four tiers (by rate)

| Tier | Rate | Default job |
|---|---|---|
| **Eliminate** | Over 10% | Kill it. This debt is a guaranteed loss you can't outrun. |
| **Evaluate** | 7 to 10% | Situational. Depends on your balance sheet and tolerance. |
| **Strategic** | Under 7% | Cheap money doing a job. Prepaying just locks in the rate. |
| **Monitor** | Asset-backed | Watch the LTV cushion, not the rate. |

The thresholds are set against what your money reasonably earns. Above 10% beats almost any investment; under 7% doesn't. The 7-10% band is where the tie gets broken by your own numbers.

The app renders these as **Low-cost (under 7%)**, **Mid-cost (7 to 10%)**, and **High-cost (over 10%)**, with Bitcoin-backed loans in a separate **Monitor** bucket.

### Running the couple's debts

| Debt | Rate | Tier | Job |
|---|---|---|---|
| $280,000 mortgage | 3.25% | Strategic | Minimum only |
| $18,000 car loan | 7% | Evaluate | Minimum only |

**Mortgage.** At 3.25% versus a 20% Bitcoin growth assumption, the interest saved from prepaying is dwarfed by the Bitcoin foregone. Keep it, as long as the payment is comfortable and the reserve is solid.

**Car loan.** Sits at the Strategic/Evaluate boundary. Their DTI is 12% (nowhere near strained), so the payment isn't hurting anything. Killing it from cash would drop the reserve below target for 1.5 points of balance-sheet improvement, which isn't worth the trade. Keep it on minimums.

They have no Bitcoin-backed loan, so no debt in the Monitor tier.

### Homework

Line up every debt with its rate. Assign each one to a tier and write down the job and the reason:

- 24% credit card → Eliminate. Guaranteed 24% loss.
- 8% car loan → Evaluate. Depends on your DTI and reserve.
- 5.5% student loan → Strategic. Below expected returns.
- 3% mortgage → Strategic. Keep on purpose.
- 25% LTV Bitcoin-backed loan → Monitor. Watch the cushion.

Every debt should have a decision, not a feeling.


So let's put a job on every row.

> 🎥 **SCREEN SHARE STARTS HERE — capture segment 5.4-B.** Everything above is teleprompter A-roll (segment 5.4-A); everything below is screen capture. This heading is the edit cut point.

### Now put it in the app

#### Step 5: Give every debt a job

**Strategy → Debt → the ledger**, grouped into **High-cost** and **Low-cost**.

Each row has an inline selector in its subline. Three options:

| Option | Then enter |
|---|---|
| Minimum payments | (n/a) |
| Extra payments | A **$/mo** field appears with *"/mo extra"* alongside it. |
| Lump sum payoff | Amount (**Full balance** placeholder) plus a date. |

Right-hand status on each row:

- A **payoff month** target date.
- **minimums ok** for low-cost and open-ended.
- **no payoff path** if the row is deliberately open-ended, or unpayable at current terms.

⚠ A mortgage or margin row offers a different option set: **Interest only**, or **Let interest accrue** / **Pay interest monthly**. Those replace the standard three.

##### The job assignment rule

- The group (High-cost or Low-cost) is the app's read. Your job can differ, but you have to say why.
- Every row needs a job. The module is done when every row has one.

Default jobs by band:

| App group | Rate | Default job |
|---|---|---|
| High-cost (over 10%) | Above 10% | Lump sum payoff with a date, or Extra payments if the balance is too big to lump. |
| Low-cost (under 10%) | 3.25% mortgage, low-rate auto | Minimum payments. Held on purpose. |
| BTC-backed | Usually 7 to 10% | Minimum payments, with LTV monitored (Step 6). |

⚠ A 20%+ credit card on anything other than **Lump sum payoff with a date** is the one hard call in this module. Do it, or explain why you're not.

⚠ With no high-cost debts, only **Low-cost** renders, which is the healthy read. The app hides empty groups.


#### Route the extra dollars

**Cash Flow → Routing · waterfall order → step 2 Extra debt.** Managed on the Debt page, shown on Cash Flow. One number, two screens.
#### Step 8: Run the AI review on debt strategy

**Strategy → Debt → Review Debt Strategy** (page header, beside Add debt). Mobile label: **Review debt**.

The review reads your debt context, the verdict line you just read, and your tax context. It can also run a Bitcoin-loan scenario if you have one.

It asks: *"Do you want the fastest next move, or a full review of payoff order, payment burden, and leverage?"*

Take the full review.

Read at least one thing it surfaced out loud and say whether you agree. Your tolerance can override the math. Show that.

**When to run it:** after every debt has a job. It's a second read on payoff order and leverage, not a substitute for the decisions you just made.

⚠ The review explains and reviews. It isn't advice, and it will never name a specific lender or rate.

With a Bitcoin-backed loan in your plan, the panel adds a **BTC-loan safety check** to the menu.


Every row has a job. Last thing is to check the work.

## 5.5 Check your work
*`CHECK` · 355 words · ~2 min*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **5.5**. Beat sheet + required app state: SCREEN-SHOOT-LIST.md.

**By the end of this lesson, you can:**

- Confirm every debt has a job and no row reads no payoff path
- Read your stress number and your confidence number together

---
Four decisions about debt are now in the plan. This is the read that tells you whether they landed.

### What good looks like

- **Debt-to-income** inside the band your income stability earns. This is the floor to watch. It doesn't move with Bitcoin. The caption tells you the line.
- **Debt-to-assets** situational, roughly in the 10 to 35% household range. Remember the drift rule.
- **The verdict word.** Strong is the healthy read. Elevated or Stretched means the plan needs work this year, not that it failed.
- **The stress clause.** *"stress test reaches N% of assets"* is the number that matters. If a normal bear pushes it past your comfort, the leverage is too big.
- **Every ledger row has a job selected**, and the status isn't **no payoff path** unless you deliberately chose open-ended.
- **A low-rate mortgage** sits calmly under **Low-cost** on **Minimum payments**, with a stated reason for keeping it.
- **LTV cushion (if any).** No severity chip is the healthy state. Any chip is this week's action, not this year's.

### What got built

| # | Item | Where it lives |
|---|---|---|
| 1 | Debt inventory with terms | Strategy → Debt → Add debt |
| 2 | A job per debt | Ledger row → payment-strategy selector |
| 3 | Extra-payment amounts | Same row → $/mo extra |
| 4 | Lump-sum payoff date | Same row → amount and date |
| 5 | Extra dollars visible in the waterfall | Cash Flow → Routing step 2 (Extra debt) |
| 6 | Payoff-versus-invest comparison | Scenarios → Custom scenario |
| 7 | AI debt review | Strategy → Debt → Review Debt Strategy |

Open the Dashboard and read your confidence number. Write it down next to the one you wrote at the end of Module 2. That is what four decisions about debt were worth.

### Handing it off

The next module covers tax strategy: cost basis, the three bucket types by tax treatment, Roth conversions, and how to think about your tax bracket across a Bitcoin-heavy plan.
