# Orange Plan Academy — Advanced Bitcoin Planning Library

**Course 2 of 2.** Optional. Sections mirror the core modules so every advanced
lesson has an obvious home.

Nothing here is required to finish a plan. Each lesson opens with a gate: a
condition you can check on a screen in Orange Plan. If the condition does not
apply to you, that planning area is **complete** without this lesson.

Lesson numbers are kept from the core course during the migration and are
renumbered to A-numbers once the structure is final.

---

# Advanced Module 1 — Modeling and Assumptions

*Reference material only. No filmed lessons.*

# Advanced Module 2 — Cash-Flow Optimization

*Reference material only. No filmed lessons.*

# Advanced Module 3 — Allocation and Asset Location

## A3.1 The price context check: naming the emotion before a big move

*`TEACH` · 380 words · ~3 min*

> **Gate.** Watch this before any Bitcoin-heavy move: a large buy, selling to
> lock in gains, or taking a Bitcoin-backed loan. Your allocation decision is
> complete without it.

**By the end of this lesson, you can:**

- Run the two lookback windows before a Bitcoin-heavy move
- Tell what you are feeling apart from what is actually true
- Decide whether the plan or the price is making the decision

---
This one runs before any Bitcoin-heavy move. Its job is to name the emotion in the room.

#### Two lookbacks

- **Recent (3, 6, 9, 12 months):** what you're feeling. Bitcoin up 40% in three months, you're feeling FOMO. Down 40%, you're feeling fear.
- **Long (2 to 5 years):** what's actually true. The direction of the trend, not the mood of last week.

Run both. Recent tells you which emotion you're carrying into the decision. Long tells you whether it's aligned with reality or reacting against it.

#### What the check does and doesn't do

It doesn't decide the move. It names the emotion so you can act on the plan instead of the mood.

Before a big move (buying a large position, selling to lock in gains, taking out a Bitcoin-backed loan), if the recent 3-6 month price move is dramatic, you're probably reacting to it. Wait a beat. Is this the plan making the decision, or the price?

### Your decision

**Whether this move is the plan talking or the price talking.**

If the recent 3-to-6-month move is dramatic, wait a beat and ask it straight
before you act.

# Advanced Module 4 — Debt and Bitcoin-Backed Loans

## 5.2 Size the LTV cushion on a Bitcoin-backed loan
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


### Your decision

**Your maximum starting LTV, and exactly what you'll do at each severity level.**

How to think about it:

1. **Size the cushion to a normal bear market, not a mild one.** A 70 to 80% drawdown is the normal case for Bitcoin, and that's what the cushion has to survive.
2. **Work backwards from that.** Surviving a normal bear usually means starting far lower than lenders will let you borrow.
3. **Decide your actions before the chip appears**, because the moment it does, the price is falling and you'll be making the decision at your worst.
4. **Write down all three responses now**: what you do when the loan gets close to a margin call, what you do at a margin call, and what you do in the liquidation zone.

### Homework

1. Enter your lender's real thresholds on the loan in the app: starting LTV, top-up line, liquidation line. The cushion is only honest if those are your lender's numbers.
2. Decide your action at each of the three severity levels before you're at one of them.
3. If you already have a loan, open its detail view and read today's cushion against those lines.

Everything so far has been defense: know your ratios, protect the cushion, don't get liquidated. The other half is what debt is actually for.

## 5.4 How Bitcoin-backed loans work: LTV, margin calls, liquidation
*`TEACH` · 1,750 words · ~11 min*

**By the end of this lesson, you can:**

- Explain how a Bitcoin-backed loan works, end to end
- Read LTV and know what moves it
- Know exactly what happens at a margin call, a top-up, and a liquidation
- Tell the difference between the main types of provider
- Model a loan in Orange Plan with rules that match your lender

---

This is the highest-stakes lesson in the course, so I'm going to go slowly and cover the whole mechanism before we talk about whether you'd want one.

### What a Bitcoin-backed loan actually is

You pledge Bitcoin as collateral. A lender holds it and gives you cash. You pay interest. When you repay the loan, you get your Bitcoin back.

That's the whole product. What makes it interesting is that **you didn't sell**, so in most cases there's no taxable event, and you still own the upside if the price rises.

What makes it dangerous is that **your collateral is the most volatile asset most people will ever own**, and the lender's protection against that volatility is the right to sell your Bitcoin without asking you.

### LTV: the one number that runs everything

LTV means loan-to-value. It's your loan balance divided by the value of your collateral.

Borrow $50,000 against $200,000 of Bitcoin, and your LTV is 25%.

Two things move that number, and only one of them is in your control:

- **Your loan balance goes up** as interest accrues, if you're not paying it down. That's slow and predictable.
- **Your collateral value moves with the Bitcoin price.** That's fast and it is not predictable.

Here's the part people underestimate. **LTV rises much faster than the price falls**, because the price is in the denominator.

Start at 25% LTV. If Bitcoin falls 50%, your LTV doesn't go to 50%, it goes to **50%** — your collateral halved, so the same loan is now half-covered. Fall 70%, and 25% LTV becomes **83%**. Fall 80%, and it becomes **125%**, meaning your loan is worth more than your collateral.

That's why starting LTV matters more than any other decision in this lesson. It's the only variable you control before the market takes over.

### The three lines every loan has

Your lender sets three thresholds. Learn them as a sequence, because that's how you'll experience them:

**1. The margin call line.** Typically somewhere around 65 to 70% LTV, but every lender is different. When you cross it, the lender contacts you and gives you a window, sometimes 24 to 72 hours, to fix it.

**2. The liquidation line.** Typically around 80 to 85%. If you cross this, or if you don't fix a margin call in time, the lender sells your Bitcoin to bring the loan back into range. You don't get a vote.

**3. The release line.** This one's the good news, and a lot of borrowers don't know it exists. If the price rises enough that your LTV drops well below where you started, many lenders will release some collateral back to you, or let you request it.

### What you can actually do at a margin call

You have three options, and you should know which one is yours before you ever get the call:

- **Top up.** Send more Bitcoin as collateral. This lowers your LTV without selling anything, and it's the option most people take. But it means you have to be holding unpledged Bitcoin you can send quickly.
- **Pay down.** Send cash to reduce the loan balance. Same effect on LTV, from the other direction. This requires cash on hand in exactly the week your net worth is falling.
- **Do nothing and get liquidated.** The lender sells enough of your Bitcoin to fix the ratio, at whatever the price is that day, which by definition is a bad price.

⚠ Notice that two of your three options require you to *have something in reserve*. A loan taken with every spare satoshi already pledged and no cash cushion has exactly one option at a margin call, and it's the bad one.

### Partial versus full liquidation

If it comes to liquidation, lenders handle it differently, and the app models both:

- **Partial liquidation** sells only enough collateral to bring you back under the threshold. You keep the rest and the loan continues.
- **Full liquidation** closes the entire position. The loan is settled and your remaining collateral, if any, comes back to you.

Ask your lender which one they do before you sign. It changes what a bad month costs you.

### The types of provider

You don't need me to name specific companies, because the landscape changes and any list I give you goes stale. What doesn't change is the **structure**, so learn to sort providers into these buckets:

**Custodial lenders.** You send your Bitcoin to the company and they hold it. Simplest to use. The risk is the one you already learned in the custody module: it's their Bitcoin now, in a legal sense, and if they fail you're a creditor. Several large ones failed in 2022 and customers lost everything.

**Collaborative-custody lenders.** Your collateral sits in a multisig arrangement, often 2-of-3, where you hold a key, the lender holds a key, and a third party holds a key. The lender cannot move your Bitcoin unilaterally. This structure is the reason a lot of Bitcoiners will use one of these and never a custodial one.

**Rehypothecation is the question that separates them.** Rehypothecation means the lender lends out your collateral to somebody else while they're holding it. It's the practice most directly responsible for the 2022 failures. **Ask directly: do you rehypothecate my collateral? Get the answer in writing.** If the answer is anything other than a clear no, you're taking a risk that has nothing to do with the Bitcoin price.

**The questions to ask any provider:**

1. Do you rehypothecate collateral?
2. Custodial or collaborative multisig, and who holds which key?
3. What are your exact margin call and liquidation LTVs?
4. How much notice do I get at a margin call, and how do you contact me?
5. Partial or full liquidation?
6. Do you release collateral when LTV falls, and is it automatic or on request?
7. What's the interest rate, is it fixed or variable, and are there origination or early-repayment fees?

### A worked example

The couple holds 1.75 Bitcoin. At an illustrative $100,000 a coin, that's $175,000.

They want $35,000 for a kitchen renovation, and they don't want to sell, because selling would trigger a taxable gain and they'd be giving up the upside.

**At a 20% starting LTV**, they pledge all 1.75 BTC and borrow $35,000.

Now walk the price down and watch what happens to that ratio:

| Bitcoin price | Collateral value | LTV | Where they stand |
|---|---|---|---|
| $100,000 | $175,000 | 20% | Comfortable |
| $70,000 | $122,500 | 29% | Normal correction, fine |
| $50,000 | $87,500 | 40% | Half the value gone, still fine |
| $30,000 | $52,500 | 67% | Margin call territory |
| $25,000 | $43,750 | 80% | Liquidation |

A 75% drawdown, which is a normal Bitcoin bear market, takes them from 20% to the edge. **That's what starting at 20% buys you: it survives a normal bear, and it barely survives.**

Run the same loan at 50% starting LTV and a 40% price drop hits the margin call. A 40% drop is an ordinary Tuesday in Bitcoin, not a bear market.

### The rules to write down before you borrow

1. **Start low enough to survive a 70 to 80% drawdown.** For most people that means 20 to 25%, not the 40 or 50% a lender will happily give you.
2. **Keep unpledged Bitcoin or cash you can reach fast**, so a margin call has a good answer.
3. **Know your lender's three lines** and write them down where you'll find them.
4. **Decide your action at each line now**, in writing, while nothing is falling.
5. **Never borrow for something you can't stop paying for.** A loan against a volatile asset funding a fixed obligation is how people get forced out at the bottom.

### Now put it in the app

Orange Plan models all of this, and it models it as a real position in your plan rather than a calculator off to the side.

**Adding the loan: Strategy → Debt → Add debt**, and choose the Bitcoin-backed type. The form asks for the things that actually matter:

| Field | What to enter |
|---|---|
| **Lender** | Whoever you're using (the placeholder shows examples) |
| **Start date** · **Term (months)** · **Maturity / renewal** | Your actual terms |
| **Collateral (BTC)** | The quantity pledged, not the dollar value |
| **Margin call LTV (%)** | Your lender's number, not a default |
| **Liquidation LTV (%)** | Your lender's number |
| **Auto top-up collateral** | On or off, matching what you'd actually do |
| **Liquidation strategy** | Full or Partial, matching your lender |

⚠ Enter your lender's real thresholds. The app ships with common defaults, and a plan modeled on the wrong lines will tell you a comforting story that isn't yours.

**The collateral rules: Strategy → Debt → Collateral rules.** This is where the behavior gets modeled across the whole projection:

- **Auto top-up (global default)** turns automatic topping-up on or off
- **Margin call %** is the LTV that triggers a top-up
- **Top-up target %** is the LTV it tops back down to
- **Liquidation %** is where forced selling happens
- **Release trigger %** is the LTV below which collateral comes back to you

That last one matters and it's easy to miss. **The app models collateral release**, so if Bitcoin rises and your LTV falls below the release trigger, the projection frees that collateral back into your plan rather than leaving it pledged forever.

**How it's modeled:** the engine walks your loan year by year alongside the Bitcoin price path. Interest accrues, the price moves, LTV is recalculated, and if it crosses your top-up trigger the model tops up from available Bitcoin. If it crosses liquidation, the model sells according to your liquidation strategy and records it. Pledged Bitcoin stays protected from ordinary withdrawals, so the plan won't spend collateral you've already committed.

That means when you run a 50% drawdown scenario with a loan in place, you're seeing the loan's actual behavior in that drawdown, not an assumption.

### Your decision

**Whether to borrow at all, and if so, at what starting LTV and with which provider.**

How to think about it:

1. **Start with whether you need the money at all**, because the cheapest loan is the one you don't take.
2. **Compare it honestly against just selling.** Selling costs you tax and upside. Borrowing costs you interest and adds a liquidation risk that selling doesn't have. One is expensive, the other is risky, and they're not the same kind of problem.
3. **Pick your starting LTV from the drawdown you want to survive**, not from what you're allowed to borrow.
4. **Pick the provider on structure, not on rate.** A slightly better rate at a lender who rehypothecates your collateral is not a better deal.
5. **If you can't fund a margin call, you can't afford the loan.** That's the honest test.

### Homework

1. Decide whether a Bitcoin-backed loan belongs in your plan at all. "No" is a completely legitimate and common answer.
2. If you're considering one, take the 7 provider questions to two or three lenders and put their answers side by side. The differences between lenders are the whole decision.
3. Model it in the app with your lender's real thresholds, then run the 50% drawdown scenario against it and see what happens.

## 5.3 The four ways debt can build wealth
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

### Your decision

**Which play you're running, if any, and the rules it runs under.**

How to think about it:

1. **Check it against defense first.** If a play would push you past the ceiling you set, the answer is no and you're done thinking about it.
2. **Name the failure mode out loud** before you name the upside. If you can't say how the play loses, you don't understand it well enough to run it.
3. **"None of them" is a real answer**, and it's the right one for a lot of households.
4. **If you are running one, write the operating rules before any money moves**: what it's for, your maximum size, what makes you unwind it, and who else knows about it.

### Homework

1. Pick your play, or decide you're running none. None is a real answer and the common one.
2. Model it against your baseline as a scenario, and read the confidence number both ways.
3. If you're running one, set its rules before you act: what you borrow against, at what LTV, and what makes you stop.

You've seen what one play does to your plan. Now every debt on the ledger needs a decision, including the ones you're keeping.

# Advanced Module 5 — Tax Strategies

## 6.3 RMD risk and Roth conversions
*`TEACH` · 954 words · ~7 min*

> ✅ **Evergreen policy (Austin, 2026-08-04) replaces item 11.** Figures here
> are already snapshot-framed ("Currently 73 — verify in the year it applies").
> Don't re-verify per year; don't state them as durable facts on camera.

**By the end of this lesson, you can:**

- Understand what an RMD is and why it forces a bracket spike
- See how Bitcoin makes the RMD risk larger
- Understand Roth conversions and how they shrink the RMD bucket early
- Fill your tax bracket without spilling into the next one

---

The buckets-and-brackets lesson opened the low-bracket window. This lesson covers why filling it matters and the main tool for filling it.

### What an RMD is

RMD stands for **Required Minimum Distribution**. Money the government forces you to take out of traditional retirement accounts once you reach a certain age. Currently 73 (verify in the year it applies).

The amount is: **Account balance ÷ IRS life-expectancy divisor**

The divisor shrinks every year you age, so the forced withdrawal climbs. Every dollar is taxed as ordinary income.

### The couple's future RMD

Contributions: $12,000/yr plus employer match (50% up to 6% of $150k salary = $4,500). Total $16,500/yr going in.

- **Age 60:** ~$400,000 balance after 15 more years at a 7% stock assumption.
- **Age 73:** ~$1,000,000 after another 13 years compounding, without new contributions.
- **First RMD:** $1,000,000 ÷ 26.5 ≈ **$38,000**, as ordinary income.

### The RMD stacks with Social Security

At 73: $38,000 (RMD) + $51,600 (Social Security) = **$90,000** of ordinary income the couple didn't ask for. And it climbs every year, because the divisor shrinks.

That can push you over the IRMAA (Income-Related Monthly Adjustment Amount) thresholds and trigger higher Medicare premiums. A tax problem becomes a health-premium problem.

If they never spend it, their heirs inherit the tax problem with the account.

### Why Bitcoin holders should care more

Take the same contributions, but with Bitcoin exposure inside the traditional account at 20% growth:

| Age | Balance | RMD |
|---|---|---|
| 60 | ~$1.2M | — |
| 73 | ~$12.5M | **~$470,000/yr** of ordinary income |

At whatever rate the government sets in that decade.

### The fix: shrink the bucket early

Shrink the tax-deferred bucket on your terms, in your window. The tool is a **Roth conversion**.

**What a Roth conversion is.** Move money from a traditional account into a Roth account in a year you choose. Pay ordinary income tax on the amount you move, now. In exchange, that money never faces an RMD again, and grows tax-free from that day forward.

You're trading a low rate you chose (now) for a high rate you'd have been forced into (later). And you're shrinking the balance the RMD divisor gets applied to.

### Fill the bracket, don't spill

- Look at your room from the buckets-and-brackets lesson.
- Convert just enough to reach the top of your current low bracket.
- Stop before you spill. Every dollar past the line gets the next bracket's rate.

Every converted dollar stays at the rate you chose.

### Running the conversion on the couple

At 60 with basically no earned income:

| Step | Amount |
|---|---|
| Convert | ~$100,000 |
| Minus standard deduction (~$31,400) | -$31,400 |
| Equals taxable | ~$68,000 |
| At the 12% bracket, tax owed | **~$7,700** |

Verify deductions and brackets in the year you convert.

Repeat four years running (60-64) and the $400,000 balance is gone before it becomes a million. Total cost: ~$30,000 in tax, on their schedule, to retire a bill heading for a much higher rate.

### Pay the tax from outside the Roth

If you convert $30,000 and the tax bill is $3,600, pull that $3,600 from taxable Bitcoin or checking, not from the Roth itself.

Pay it from the Roth and only ~$26,400 lands in tax-free space. Pay it from outside and the full $30,000 keeps compounding tax-free.

### The conflict to flag

The buckets-and-brackets lesson showed ~$68,000 of empty 0% capital-gains room in that same window. Conversion income is ordinary income. It stacks underneath your capital gains. Filling the bracket with a conversion pushes some of those gains out of 0% into 15%.

The two moves compete for the same window, in the same years. **Model them together.**

### Conversions aren't the only tool

Plain withdrawals work too. Take money out of tax-deferred before RMD age, fill a bracket with it, spend it as income. Same bucket-shrinking effect, no conversion needed.

Choice between converting and withdrawing comes down to how much money you have and how much time before RMDs start.

For completeness: 72(t) allows penalty-free early access on a rigid schedule. Real, but strictly professional-review territory.

### Homework

- Estimate your tax-deferred balance at 73.
- Divide by ~26 for a first-year RMD estimate. Add Social Security.
- If the total pushes you into a higher bracket than your bridge years, a Roth conversion schedule is worth modeling.
- Build the model. Bring it to your CPA.

## 6.4 Harvesting losses and gains
*`TEACH` · 1,156 words · ~8 min*

> ✅ **Fixed in course 2026-07-29:** the stale hand-off ("relocation as a tax
> lever" — a lesson that was folded into 6.2) now points at the walkthrough.
> Item 23 closed. Still item-14 evidence that the relocation lesson was merged.
>
> ⚠ Wash-sale exemption for Bitcoin: lesson says verify — include in item 11.

**By the end of this lesson, you can:**

- Understand what tax-loss and tax-gain harvesting are
- Identify harvest opportunities lot by lot
- Choose the right lot-accounting method (FIFO vs HIFO) for a sale
- Run the fee check before harvesting

---

Everything so far has been about acting in low-tax years. This lesson adds a second trigger: acting when the price moves.

Because Bitcoin moves so much, you get chances to lock in tax outcomes that stocks rarely give you.

Two tools go in opposite directions:

- **Harvest losses** at the dips.
- **Harvest gains** when your bracket is low.

### What harvesting means

Both tools work the same way:

- Sell a lot to make the gain or loss real for tax purposes.
- Buy back so what you own barely changes.

That lets you choose the year the tax result lands in, without changing your position.

### Tool 1: Harvest losses (Bitcoin is down)

Sell a lot sitting below your basis and capture the loss.

**The couple's lots after a 60% fall.** Bitcoin fell 77% in 2022, so a 60% fall is a normal cycle. Their $175,000 stack is now worth $70,000.

| Lot | Basis | Basis/coin | Value after 60% fall | Harvest room |
|---|---|---|---|---|
| Hardware (1.5 BTC) | $45,000 | $30,000 | Still profitable | None |
| Exchange (0.25 BTC) | $15,000 | $60,000 | ~$10,000 | **$5,000 loss** |

Sell the 0.25 BTC for ~$10,000, buy it right back for $10,000. The $5,000 loss is real for tax purposes.

**How losses get used.** Losses offset in this order:

- Capital gains first, dollar for dollar.
- Ordinary income next, currently up to $3,000/yr (verify).
- The rest carries forward.

Running the couple's $5,000 loss:

| Step | Applied | Value |
|---|---|---|
| Offset gains | $0 (none this year) | $0 |
| Offset ordinary income | $3,000 at 22% | ~$660 |
| Carries forward | $2,000 | Future years |

The trade-off: when they buy that lot back, basis drops from $15,000 to $10,000. That takes the deduction now and grows the gain reported later. Usually worth it.

### Choosing which lot to sell: FIFO vs HIFO

Say you have 8 lots of 0.5 BTC each from 2023-2025, with Bitcoin now at $70,000. You want to sell 1 BTC.

| # | Price paid | BTC | Basis | Gain/loss at $70k |
|---|---|---|---|---|
| 1 | $20,000 | 0.5 | $10,000 | +$25,000 |
| 2 | $30,000 | 0.5 | $15,000 | +$20,000 |
| 3 | $40,000 | 0.5 | $20,000 | +$15,000 |
| 4 | $60,000 | 0.5 | $30,000 | +$5,000 |
| 5 | $65,000 | 0.5 | $32,500 | +$2,500 |
| 6 | $90,000 | 0.5 | $45,000 | -$10,000 |
| 7 | $100,000 | 0.5 | $50,000 | -$15,000 |
| 8 | $105,000 | 0.5 | $52,500 | -$17,500 |

**FIFO (first-in, first-out).** The exchange default. Sells lots 1 and 2.

- Basis $25,000, sale $70,000, gain **$45,000**.
- Tax at 15% long-term: **$6,750**.

**HIFO (highest-in, first-out).** Selected at time of sale. Sells lots 8 and 7.

- Basis $102,500, sale $70,000, loss **$32,500**.
- Tax on the sale: **$0**.
- Plus a $32,500 loss you can now use.

Same sale, same coins, $6,750 vs $0. The exchange picks FIFO by default. HIFO is a choice you make at the time of sale, and it needs the wallet-by-wallet cost basis you built in the cost-basis lesson to defend.

> ⚠ **HIFO guardrails.** Skip any lot held less than 12 months (short-term rates are much higher). Under 2025 wallet-reporting rules, the coins you sell must come from the wallet those specific lots live in.

### The fee check: is the harvest worth it?

Before you sell-and-rebuy, sanity check:

**Loss × your tax rate** vs **trade amount × fee rate × 2** (both sides of the trade)

If the left side is bigger, worth doing. If not, skip.

On a $10,000 harvestable loss at 22%, selling and rebuying $35,000 of Bitcoin at 1.5% fees each way:

- Tax benefit: $10,000 × 22% = **$2,200**
- Fees: $35,000 × 1.5% × 2 = **$1,050**
- Net: **+$1,150**, worth it.

Same trade at 3% fees each way? Fees jump to $2,100, harvest barely clears. Small lots at high-fee venues aren't always worth it.

### Tool 2: Harvest gains (your bracket is low)

Sell to realize gains on purpose in a year your capital-gains rate is low or zero. Buy back at the same price. Reset your basis higher for free.

**Running it on the couple at 60.** Same 0.25 BTC from the cost-basis lesson:

| Step | Amount |
|---|---|
| Sale proceeds | $25,000 |
| Minus basis | -$7,500 |
| Gain (all long-term) | $17,500 |
| Tax at 0% (inside 0% LTCG bracket) | **$0** |
| Buy back at | $25,000 |
| **New basis** | **$25,000** |

Nothing about their stack changed. The basis on that quarter coin went from $7,500 to $25,000. That's $17,500 of future gain that no longer exists. At a future 15%, $2,625 of tax they now never pay.

**Two jobs the 0% bracket does:**

- Saves tax on the sale you made that year (obvious).
- Resets your basis higher for free, one year at a time (missed by almost everyone).

A 0% year is worth using even in a year you don't need the money.

### The window conflict

Roth conversion income competes for the same room. Ordinary conversion income stacks under gains and can push them out of 0%. Model them together.

### The Bitcoin wash-sale note

Under current treatment, Bitcoin does not have the wash-sale rule that stocks have. You can sell at a loss and buy right back the same day. For stocks, that would disallow the loss for 30 days.

> ⚠ Verify wash-sale treatment in the year you act. This has been proposed to change.

### Homework

Two checks against your lots:

- Losses sitting unharvested from the last drawdown?
- Gains you could realize this year at 0%?

Those two answers are what you take to your CPA.

# Advanced Module 6 — Retirement Strategies

## 7.2 Health insurance between retiring and Medicare
*`TEACH` · 800 words · ~6 min*

**By the end of this lesson, you can:**

- Compare COBRA, ACA marketplace, and health-sharing for early retirement
- Understand how MAGI affects your ACA subsidy
- See the tension between Roth conversions and healthcare subsidies
- Price your healthcare bridge three ways

---

Under current law, Medicare starts at 65. Retire at 55, and that's 10 years of coverage you have to buy yourself, because employer coverage ends when the job does.

A 10-year bill in front of anyone retiring early. Usually the largest single line inside the bridge years.

### Three paths (plus one short-term option)

**Short-term: COBRA.** Keeps your exact employer plan for up to 18 months (verify).

- You keep your plan, doctors, and network.
- Now you pay all of the premium, plus a small admin fee.

Bridge to the bridge. A first-year option, not a decade solution. Expensive but zero disruption.

**Path 1: The marketplace (ACA).** The default for most early retirees. Metal tiers are cost-sharing levels, not quality levels:

| Tier | Premium | Deductible | Notes |
|---|---|---|---|
| Bronze | Lowest | Highest | May pair with an HSA |
| Silver | Middle | Middle | Benchmark tier for subsidies. Extra cost-sharing help at lower incomes. |
| Gold | Higher | Lower out-of-pocket | Wins if you use a lot of care |

> ⚠ Illustrative pricing. Verify current at healthcare.gov. An unsubsidized couple in their late 50s can face four figures a month.

Almost nobody who plans well pays sticker price.

**The subsidy scales with your income.** The subsidy lowers your monthly premium, and its size scales with income:

- Lower income → bigger credit → lower net premium.
- Higher income → smaller credit → sticker price at the top.

The income it looks at is your **MAGI** (Modified Adjusted Gross Income): the income the subsidy math sees.

In early retirement, your MAGI is partly a choice, which puts your premium partly under your control:

- Spend from cash or taxable dollars that are mostly basis → income on paper is low → subsidy goes up.
- Realize gains, take traditional-account dollars, or do Roth conversions → MAGI goes up → subsidy goes down.

Engineer a modest MAGI and the same Silver plan's net premium can fall by hundreds or thousands a month. Thresholds move every year. Verify.

In the bridge years, your health premium is partly a tax-planning output.

**The tension: subsidy vs Roth conversion.** Same shape as the tax module's window conflict. One low-income window, multiple planning moves competing for it.

A big Roth conversion raises your MAGI, which shrinks or kills the subsidy that same year. You can max the window for subsidies or for conversions, but not both.

A conversion decision is also a healthcare decision. Model both paths, pick deliberately, revisit every year. Flagship question for your CPA.

**Path 2: Health-sharing.** Austin's family uses CrowdHealth, so he can speak from experience.

> ⚠ Health-sharing is not insurance. It's a crowdfunding membership where members fund each other's medical bills.

How it works:

- Pay a monthly membership amount.
- Cover a fixed member responsibility on a health event (a few hundred dollars).
- Bills above that get crowdfunded, with cash-pay pricing negotiated up front.

Trade-offs:

- **Not insurance.** No legal guarantee any bill gets funded.
- **Pre-existing conditions.** Limited, phased participation.
- **Cash-pay medicine.** No network. You're the payer.
- **Typically not HSA-qualified.** Joining usually means giving up new HSA contributions. Verify current law.

Best fit: relatively healthy households comfortable managing bills directly, with a solid reserve.

Verify terms and pricing before deciding.

### The decision frame

Bridge years × annual cost of each path, side by side. Then add soft factors: health status, comfort with a non-guaranteed model, HSA plans, provider preferences.

### In the plan

Healthcare is a line inside your retirement spending number (from the spending-floor lesson). The bridge premium is an expense with an end date at 65.

In the app: enter as an **Expense Change** life event with a duration (5 years if you retire at 60). No "end age" field; you set a duration.

One thing the app doesn't do: model a Roth conversion, and it shows the tax side in full but doesn't price what the higher MAGI does to your subsidy. That's the worksheet.

### At 65: one income rule swaps for another

Income still drives your healthcare cost, just under a different rule. Subsidies stop; Medicare IRMAA surcharge thresholds take over (covered in the tax module).

### Homework

Price your bridge three ways:

- COBRA (first year only).
- A Silver plan at the MAGI you'd actually run.
- Current health-sharing membership pricing.

Most people have never seen those three numbers side by side. The comparison is the decision.

## 7.4 Sell, borrow, or hold: funding a year of spending
*`TEACH` · 730 words · ~5 min*

*Advanced. Borrow-vs-sell is a decision that only fires if you're considering asset-backed lending against Bitcoin. Skim unless the trigger applies to you.*

**By the end of this lesson, you can:**

- Understand three ways to fund retirement from a Bitcoin-heavy plan
- Price sell, borrow, and hold on one year of spending
- Understand why LTV cushion is the whole borrow decision
- Mix the three tools across years

---

Three ways to fund your life from a Bitcoin-heavy plan. Each costs something different. Here's each priced on one year of the couple's retirement:

- Age 60
- Spending $80,000/yr
- $400,000 taxable Bitcoin
- $120,000 Reserve

### Tool 1: Sell (buying simplicity)

Sell $80,000 of Bitcoin to cover the year.

Split into basis and gain:

- **Basis:** about $20,000 (a quarter of it, illustrative).
- **Long-term gain:** about $60,000.

In a low-income year, that $60,000 of gain can land in the 0% capital-gains bracket and cost almost nothing.

- **Upside.** One year of spending, no counterparty, no loan to manage.
- **Downside.** Bitcoin is gone.

Best when spending is modest and simplicity is worth something in itself.

### Tool 2: Borrow (buying upside)

Borrow $80,000 against the Bitcoin. No taxable event. Bitcoin keeps compounding.

**LTV is the whole decision.** LTV = loan balance ÷ collateral value. A 20% LTV means you've borrowed 20 cents against every dollar of Bitcoin.

The ratio moves for two reasons:

1. Interest pushes the balance up.
2. A price drop pulls the collateral down.

The ratio can climb fast without you doing anything. The starting ratio is the whole decision.

**The couple's borrowing capacity, priced.** Austin's default is 10 to 20% LTV.

- 10-20% of $400,000 collateral = $40,000 to $80,000 of capacity.
- One year of spending is the entire capacity at the conservative limit.

Add a year of interest. At 10-11%, $80,000 grows to about $88,000 a year later with nothing paid.

Drop Bitcoin 50%. Collateral is now $200,000. $88,000 against $200,000 = **44% LTV**.

The cushion is gone. They can't borrow again next year, and they're one leg down from liquidation.

Borrow from strength, not from a trap. A loan taken calmly at low LTV with a plan is a different product from one taken in a drawdown because you're cornered.

**Where borrowing works and doesn't:**

- **Works.** LTV is low, liquidity is behind it, you're comfortable holding it.
- **Doesn't.** As the foundation of a retirement paycheck. One year of spending uses the whole capacity. The second year has nowhere to come from.

Borrowing is a tool for a year, not a plan for a decade.

### Tool 3: Hold (buying compounding, and maybe more)

Don't touch the Bitcoin. Spend from the Reserve ($120,000).

The $400,000 keeps compounding.

Under current law (verify), it passes to heirs with a **step-up in basis**. If their basis is $100,000:

- $400,000 - $100,000 = **$300,000** of embedded gain that passes untaxed.

That turns "not selling" from a preference into a tax strategy.

Never selling the core can be a legitimate estate move, as long as it's funded by the Reserve and Bridge instead of by sales.

### In the app

**Plan → Income → Retirement Borrowing** prices all three side by side against a plain sell-as-you-go baseline. What you read off it:

- **After-tax net worth at {age}.** The family-facing number.
- Any loan balance the estate has to repay at death.
- A step-up assumption you can flip on and off.

It's a sandbox. Nothing touches your plan until you apply it.

### The decision frame: four questions

1. **Taxes.** What's the tax bill on each path this year?
2. **Liquidation risk.** Does the loan survive a 50% Bitcoin drop?
3. **Cash flow.** Is the annual capacity enough to matter?
4. **Family comfort.** Does your spouse understand the loan structure?

Match the tool to the answers. You can mix them: a sell year, a borrow year, a hold-forever core.

### Homework

Run all three on one year of your own spending. Not to pick a winner, but to know the numbers behind each. Then price them across a five-year window. What does five years of borrow-only cost in interest and LTV drift? What does five years of sell-only cost in taxes?

Bring the outputs to the household and CPA conversation.

# Advanced Module 7 — Advanced Custody

## A7.2 What self-custody actually asks of you

*`TEACH` · 300 words · ~2 min*

> **Gate.** Optional throughout. Watch it if you are weighing whether you want
> the whole job of self-custody, or if the weight of it is what has been
> stopping you. Your custody plan is complete without it.

**By the end of this lesson, you can:**

- Name what self-custody actually transfers to you
- Decide honestly whether you want the whole job, or part of it

---
A client put this better than I ever have.

He said: with self-custody, you are the point of failure. And not just the failure, you're the attack vector. And then he made the point that most of life doesn't work this way. We outsource violence to the police. We outsource security to the banks. That's basically what civilization is, handing off the hard, dangerous jobs to somebody whose job it is.

And Bitcoin asks you to take one of those jobs back.

I think that's right, and it explains why custody feels heavier than the rest of this course. It isn't just another checkbox. It's you accepting a responsibility that, for every other asset you own, somebody else carries for you.

Two things follow from that.

The first one is that it's completely reasonable to not want the whole job. That's what collaborative custody exists for, and it's why a hardened exchange position is a legitimate setup for part of your stack. Taking the job back is a choice, not an obligation.

The second one is that if you do take it, being a little paranoid is appropriate, not a character flaw. You should feel the weight. The people who get hurt are usually the ones who didn't.

### Your decision

**Whether you want the whole job.**

It is completely reasonable not to. That is what collaborative custody exists
for, and it is why a hardened exchange position is a legitimate setup for part
of a stack. Taking the job back is a choice, not an obligation.

## 8.5 Advanced custody: passphrase, multisig, and collaborative
*`TEACH` · 1,354 words · ~9 min*

**By the end of this lesson, you can:**

- Tell passphrase, collaborative multisig, and DIY multisig apart by what each one buys and costs
- Build a passphrase strong enough to protect a stack (the 7-random-word standard)
- Vet a collaborative-custody provider with four questions
- Back up the multisig config file the way you back up a key

---

Once you're at Level 3 or 4, "advanced" means removing the single points of failure a single-device, single-seed setup has. Every setup here takes one of those "only ones" and splits it into two. You pay for that in complexity, and in what your family has to be able to do.

### The three paths

**Two definitions:**

- **Passphrase.** An extra word you choose on top of your seed. The wallet doesn't open without both.
- **Multisig (multi-signature).** The wallet is secured by several separate keys, and more than one has to sign before Bitcoin moves. A common setup is two-of-three: three keys, any two can spend, losing any single one costs nothing.

**The three paths:**

**Path 1: Passphrase single-sig.** One seed plus a hidden extra word.

- **Best for.** A modest stack.
- **Buys you.** The simplest advanced plan a family can follow.
- **Watch out for.** A forgotten passphrase locks the funds permanently. No reset mechanism. The passphrase gets its own backup, stored separately from the seed. Practice with a small amount first.

**Making the passphrase strong (the 7-word standard).**

A passphrase you make up yourself is the weak point of the whole setup. Humans pick quotes, song lyrics, names, and dates, and attackers run exactly those lists first. The fix is randomness you didn't choose:

- **Use 7 random words** picked from a wordlist by dice or by an offline generator (the diceware method, or a password manager's passphrase generator with the device offline). Not words you thought of. Random means the tool picked them, not you.
- **Why 7:** each word drawn at random from a standard 7,776-word list multiplies the guesses needed by 7,776. Seven words is roughly 90 bits of entropy, about 1,700,000,000,000,000,000,000,000,000 combinations. A machine guessing a trillion combinations per second would need millions of years. Four or five words is where "pretty good" lives; seven is the floor for money that has to stay safe forever.
- **Never:** personal facts, quotes, lyrics, addresses, pet names, keyboard patterns, or a password you use anywhere else. If it means something to you, it's guessable.
- **Exactness matters.** A wallet passphrase is case-sensitive and unforgiving. Record it exactly, letter for letter, on paper or steel. It never gets typed into anything online.
- **The same standard covers three things:** the wallet passphrase, the password manager's master password, and the encrypted plan-backup passphrase from the walkthroughs. One method, three uses.

The trade-off is built in: a passphrase strong enough to be unguessable is also unrecoverable if lost. That's why it gets its own backup, stored separately from the seed, and why you practice with a small amount first.

**Path 2: Collaborative multisig.** You hold two keys, a provider holds one, plus the configuration.

- **Best for.** A meaningful balance, or heirs who aren't technical.
- **Buys you.** A professional on call to guide them.
- **Watch out for.** An annual fee and some vendor dependence. The provider's one key can't spend on its own, so they never actually custody your Bitcoin.

**How collaborative custody actually works, and why the key count matters.** It's a two-of-three: three keys exist, any two can move Bitcoin. You hold two of them. The provider holds the third.

That split produces two properties worth understanding before you decide:

- **They can never take your Bitcoin.** One key out of a required two spends nothing. They are a co-signer, not a custodian. This is the difference between collaborative custody and an exchange.
- **They can never lock you out.** You already hold two keys, which is a spending quorum by itself. You do not need their permission or their participation to move your own money.

So what you're actually buying is three things: a key you didn't have to store yourself, a copy of the configuration file held by someone whose job is not losing it, and a human being who will pick up the phone and walk your family through recovery on the worst week of their lives. That third one is the whole reason this path exists.

**Before you pick a provider, verify these four:**

1. **Can you recover with the provider gone?** They should hand you the configuration file, or descriptor, and it should work in open-source wallet software they don't control. If the answer is "you'd have to call us," that's a custodian wearing a multisig costume.
2. **Is there a documented inheritance process?** What exactly happens when your executor calls, and what proof do they require?
3. **What's the annual fee**, and what happens to your wallet if you stop paying it?
4. **What do they require from you**, in identity verification and in privacy terms, to open the account?

The honest downside is that you're depending on a company continuing to exist across a timeline measured in decades. That's a real risk. But it's bounded by the key count: the worst case is a provider that vanishes, and you spend an afternoon recovering with your two keys and the config file. Compare that to the DIY worst case, where the person who understood the setup is the one who died.

**Path 3: DIY multisig.** You hold every key, and the configuration, yourself.

- **Best for.** Technically proficient people.
- **Buys you.** Maximum privacy and full independence.
- **Watch out for.** Your heirs inherit the complexity with no professional to guide them. This path trades your family's recovery odds for your independence.

**Compare across four rows:**

| | Passphrase | Collaborative multisig | DIY multisig |
|---|---|---|---|
| Single point of failure | Still one seed to protect | None (2-of-3) | None (2-of-3) |
| Maintenance load | Lowest | Shared with provider | Highest |
| Heir-friendliness | Good, if documented | Best. Heirs get guided. | Hardest. No help coming. |
| Cost and independence | Free, fully sovereign | Fee plus vendor | Free, fully sovereign |

Look at all four rows before picking. Technical people often stop at row one and end up with something their family can't use.

**Running the table on the same household.** $175,000 of Bitcoin. He's 45 and healthy. Wife has never restored a wallet. Kids are 10 and 12.

- **DIY multisig** wins row one. But it hands a widow and two middle-schoolers a recovery job nobody in the house can do.
- **Collaborative** is a real option, and if the stack triples it's the right one. But they'd be paying an annual fee for a problem they don't have yet.
- **Passphrase path fits.** One seed, one extra word, split between two people. The only path his wife could realistically be walked through in an afternoon.

Match the setup to your family and your stack. Only add complexity when it buys real risk reduction.

### The config file: the multisig piece that gets people killed

The keys hold the money. The **config** is the file that records how those keys connect into one wallet: which keys, the 2-of-3 rule, the technical addresses. That file is the map.

- The keys are the money.
- The config is the only file that says which wallet those keys open.

With the config, your heirs have three seeds in separate locations plus the map. The wallet reassembles. Without it, they can have all three seeds in hand and still be locked out.

Not hypothetical. A man dies with a 2-of-3 multisig holding ~$300,000. Everything right on the keys: three seeds, three separate locations, executor holds one, family finds all three. They recover nothing. $300,000 lost to a missing file.

**The config file's superpower: it's public.** The config has no spending power. Losing it to a thief costs you privacy, not coins. You can back it up aggressively, in a way you'd never back up a seed.

> ⚠ The config file is a recovery dependency. Back it up wherever you back up keys. Keep extra copies. Make sure someone besides you knows it exists.

A collaborative provider holds the config for you. On top of the support, the annual fee is buying the one file your heirs can't reconstruct on their own.

### Homework

- Decide whether an advanced setup is warranted at all. Staying at a well-run Level 2 is a legitimate answer.
- If you're adding a passphrase, generate it with 7 random words from a wordlist, using dice or an offline generator. Back it up separately from the seed, and practice with a small amount first.
- If you're considering collaborative custody, ask a provider the four questions and get the answers in writing before you pay anything.
- If you're running multisig, go find your config file, back it up, and tell one other person it exists.

# Advanced Module 8 — Advanced Estate Planning

## 9.5 Advanced: do you need a trust, and which one?
*`TEACH + APP` · 1,923 words · ~9 min*

**By the end of this lesson, you can:**

- Run your household through the trust-need gate
- Match trust type to purpose

---
> **Advanced. Most plan-builders don't need a trust. Run the eight-trigger gate first. If it doesn't light up, the baseline is your plan.** Skim unless the trigger applies.


**Most of you don't need what's in this lesson.** Stopping at the baseline is a valid outcome.

A **trust** is a legal container that owns things, with three roles:

- **Grantor.** The person who puts assets in. That's you.
- **Trustee.** Whoever manages what's inside, under the rules you wrote.
- **Beneficiary.** Whoever it's all for.

You can hold more than one of those at the same time, and that matters a lot.

### Two kinds, one question: did you keep control?

#### Revocable living trust

You can change or cancel it any time. Usually you're grantor, trustee, and beneficiary all at once while alive. Nothing about your day changes.

Buys you three things:

1. **Avoids probate.** Assets titled in the trust's name aren't yours at death, they're the trust's, so there's nothing for the court to settle.
2. **Keeps things private.** Probate is public record. A trust isn't.
3. **Smooth handoff if you're incapacitated.** The successor trustee steps in.

**What it does NOT buy: a lower estate tax bill.** The estate tax follows control, not paperwork. If you can cancel the trust and take everything back tomorrow, then for tax purposes the assets are still yours.

Here's what happens when someone doesn't know that. They sit down with a salesperson, pay $3,000-4,000 for a revocable living trust, and walk out believing they just protected their estate from taxes. They didn't. They bought probate avoidance and privacy at a tax-shelter price, and nobody corrected them.

#### Irrevocable trust

The opposite trade: you give up control and generally can't undo it. In exchange:

1. **Removes the assets from your taxable estate.**
2. **Can shield them from creditors and lawsuits.**

It works for the same reason the revocable one doesn't: you actually gave the assets away. The trust owns them, not you.

**For a Bitcoin holder, the future growth escapes your estate too.** You move an asset out at its value on the day you transfer it, and everything it becomes after that grows outside the line. **That makes the tool worth the most when you expect the most growth.**

Cost: flexibility, permanently.

### The eight-trigger gate

Federal estate tax touches a tiny fraction of estates. For most people the honest answer is no.

**Group A: size and tax:**

1. Is your estate near or above the **federal exemption**? (Verify the current number.)
2. Does your **state** run its own estate or inheritance tax?
3. Is most of your wealth in a **fast-appreciating asset**?
4. Could **future growth** push you over the line?

**Group B: family and control:**

5. Do you have a **blended family**?
6. **Minor children** or a **special-needs heir**?
7. Do you want to control **when and how** heirs receive assets?
8. Is there a **creditor, lawsuit, or divorce** concern, or a strong desire to avoid probate?

More yeses = more reason to go past a will. Few or none = the baseline is enough. **The gate turns this into a counting exercise you run on your own numbers.**

### Running the gate on the couple

- **Near federal exemption?** No, not close.
- **State estate tax?** Texas. No.
- **Most wealth in a fast-appreciating asset?** Yes.
- **Could future growth cross the line?** Open question.
- **Blended family / special-needs heir?** No.
- **Minor children?** Yes. 10 and 12.
- **Control over when heirs receive assets?** Only because the kids are minors. A will handles that with a guardian nomination and a provision holding a minor's share until they're older.
- **Creditor / lawsuit / divorce concern?** No.
- **Avoid probate?** Mildly, and Texas probate is relatively painless.

**Two clear yeses, one open question, five nos.** That's not a trust household. It's a Level 2 baseline household: attorney-supervised will with guardian nomination, coordinated with the access split. Saves them $3,000-4,000 and a lot of complexity.

**Re-run the gate every year.** The fourth trigger (future growth) is the one that flips.

### Bitcoin in a trust: the design problem

Tax logic makes irrevocable worth doing. What makes it hard is **who holds the keys.**

- If the trust legally owns the Bitcoin but **you're the only one who can move it**, you've written a document that doesn't match reality.
- If the **trustee holds everything**, you've handed one person unilateral access. The exact thing the access split lesson removes.

**With multisig there's a clean answer: the trustee holds one key, never the seed.** One key can't spend, but it makes the trustee a real participant in a structure they legally control, without unilateral access.

Legal structure and key plan get designed together, with an attorney who understands both.

### Two misconceptions

- **"Trusts are for the ultra-rich."** Wrong. A special-needs heir or a blended family can make a trust the right call at modest wealth.
- **"Everyone needs a trust."** Also wrong. A large, simple estate may not need one yet. Size alone isn't a trigger. The gate is.

### Homework

Run all eight triggers on your household. Count your yeses. If zero or one, the baseline is your plan. Re-run the gate once a year. If more than that, take the five attorney questions from the executor lesson to two or three candidates.


### Now put it in the app

One thing not to do on camera: do not say a federal exemption figure out loud. The app prints one on screen. The number changes with law, and a video should not age out.

#### Pre-flight

The Protect legacy section reads the **baseline projection**, not a scenario. That single fact matters (see Step B3).

- **Have the plan's projection warm** before you record. The section shows *"Running your baseline projection…"* while it loads.
- **Set State of residence** in the legacy drawer, or the state row reads *"select a state of residence below"* and the state-caveat beat has nothing behind it.

⚠ **The app's federal exemption comparison is not filing-status aware.** It applies one flat exemption regardless of married/single. A married couple's real line is different. The app doesn't model it. Name that limitation once when you get to the federal row.

#### Step B1: Read the projected estate

**Protect → section "Projected legacy."**

Sub-line: *"What your plan leaves behind at age {N} ({year})."*

Two columns:

**Left. "Bitcoin remaining"**. BTC quantity, split into:

- **"Liquid"**
- **"Pledged as loan collateral"**

**Right. "Projected estate after debt"**. With three rows:

- **"Gross assets"**
- **"Less remaining debt"**
- **"After tax"** (tagged **est.**)

⚠ **Dollar toggle: "Today's $ / Nominal $". Defaults to Today's $.** This is the number at the *end* of the plan, so nominal dollars will look bigger. Flip it once, deliberately, and name which one you're reading. If you say "future dollars" without flipping, you're describing something the screen isn't showing.

#### Step B2: Open the ledger. Where the tax actually lands

**Same section → "See details →."**

Drawer opens under **"The math behind these numbers."**

The right-hand ledger is **"After tax. Modeled"** · caption *"by account type & state."*

Rows in order:

| # | Row | What it is |
|---|---|---|
| 1 | **Estate after debt** | The gross starting point |
| 2 | **Income tax, inherited tax-deferred** | *"ordinary income to heirs · 10-year rule"* |
| 3 | **State estate tax** | Modeled from your state selector |
| 4 | **Federal estate tax** | With the exemption comparison as sub-caption |
| 5 | **After-tax estate** | The number that reaches heirs |

⚠ **The exemption line is the Federal row's sub-caption.** It reads either *"under exemption at current law"* or *"over the {amount} exemption at current law."* Point at it; don't repeat the number.

Controls below the ledger: **"State of residence"** and **"Heir marginal rate."** Set both before you read the number aloud.

⚠ **When there's no federal tax, that row reads "" (muted).** That dash is the good outcome. Say so on camera. A dash here means the estate clears the line under current law; there's nothing to plan around.

The number that matters is the last row: **After-tax estate.** Not the gross. Not the pre-tax.

#### Step B3: The growth dial. Move the assumption

The Protect legacy number reads the **baseline plan.** Scenarios don't move it. To see the estate move, change the plan's own growth assumption.

**Plan → Retirement → "Edit assumptions" → section "Bitcoin."**

Two model cards:

| Model | Curve | Blended |
|---|---|---|
| **Conservative** | 20% → 6% | ~16% blended |
| **Moderate** | 30% → 8% | ~22% blended |

- Switch to **Conservative** → return to Protect → read **"After-tax estate."**
- Switch to **Moderate** → return to Protect → read it again.

⚠ **Set the assumption back to where it started before you finish.** This step is a read, not a decision. You want the number under both cases; you don't want the plan itself to move because you were curious.

Change nothing but the growth assumption and watch the estate move. That's allocation-plus-time. The whole conversation, in one dial.

#### Step B4: Compare to the line + the state caveat

Back on Protect → the **"Federal estate tax"** and **"State estate tax"** rows.

**Under the line** in every growth case you'd defend → *"that's a good outcome"*. Close the tab. Most households live here.

**Over the line** under assumptions you actually believe → the trust conversation is warranted. That's not "definitely owe tax". It's "worth an attorney hour this year."

The state row's sub-caption names your state and its note when a state estate tax applies.

⚠ **A handful of states run their own estate tax at far lower thresholds** than the federal exemption. It's a local-attorney question rather than a plan-modeling one. Name it once.

#### Step B5: Record this module's decisions

Off-app, in your notes or a shared document.

- **Estate tax: under the line, or over it?** Under which growth case.
- **State flag.** Yes / no, and which state.
- **Attorney conversation.** This year, or deferred to the annual review.
- **Executor and backup.** Asked and accepted.
- **Your estate level, 1 to 3.** From the self-triage.
- **Access-split status.** Set / tested / not yet.
- **Insurance gaps.** Flagged on the Coverage Audit worksheet.
- **If the trust gate said yes:** the five attorney questions go into the interview.

Optional artifact: **Protect header → Download estate summary.**

⚠ **That is not the encrypted plan backup.** The backup lives at Settings → Data & backups → Export Plan, and it belongs to the annual review, not here.

Say the close on camera: for most households, running this number earns you the right to stop thinking about it until next year.

#### Where this module's work lives

| # | Item | Where it lives |
|---|---|---|
| 1 | Heir letter, app record (contacts, content, PDF export) | Protect → Heir letter → Edit heir letter → Download PDF |
| 2 | Heir letter, family-ready page | Course toolkit → **06 The Heir Letter** (PDF) |
| 3 | Dead man's switch, armed | Protect → Dead man's switch → Turn on with a first check-in |
| 4 | Beneficiaries current | Protect → Beneficiaries → Add beneficiary |
| 5 | AI-assisted draft (optional) | Protect → Heir letter assistant → Draft with AI |
| 6 | Executor Packet, walked and signed | Course toolkit → **08 Executor Packet** (PDF), section 6 signed |
| 7 | Estate + insurance decisions | Recorded decision + Coverage Audit worksheet |
| 8 | Projected estate read | Protect → Projected legacy → Projected estate after debt |
| 9 | After-tax number + exemption comparison | Protect → See details → After-tax estate / Federal estate tax |
| 10 | State of residence + heir marginal rate | Protect → legacy drawer selects |

---


Do not buy structure until the gate lights up, and design the legal and key plans together.
