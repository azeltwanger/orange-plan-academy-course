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

## A1.1 How Orange Plan models Bitcoin: fat tails, correlations, floors and caps
*`TEACH` · ~400 words · ~3 min*

> **Gate.** Watch this if you want to defend your confidence number rather than
> take it on faith, or if you are about to hand your report to someone who will
> ask how the simulation works. Core 2.3 teaches how to *read* the number; this
> is how it is *built*.

**By the end of this lesson, you can:**

- Explain why a normal bell curve is the wrong model for Bitcoin
- Say what the floors and caps on the fat tail are anchored to
- Explain why the assets are correlated rather than independent

---

In today's lesson, we're going to open up the simulation behind your confidence number, because you shouldn't have to take a number on faith to trust it.

### Why bitcoin needs a fat-tailed model

Most models out there assume returns follow a normal bell curve. And if you point one of those at Bitcoin, it's going to tell you that a year down 70% basically never happens. Anyone who's been in Bitcoin for more than a cycle knows that's wrong.

Bitcoin has had years down more than 70%, and it's had years where it tripled. Those extreme years show up in Bitcoin's history far more often than a bell curve would predict. That's what "fat tails" means — the extremes on both ends stay likely, instead of vanishing the way they do in a normal distribution.

So the engine uses a fat-tailed distribution for Bitcoin, calibrated to its actual return history. If you built a plan on a bell-curve model of Bitcoin, the plan would look sturdier than it actually is.

### Volatility and correlations

Every asset in the simulation gets its own volatility. Bitcoin runs at roughly 50%, easing toward 20% as it matures — which is about three times as far as stocks move in a typical year. And that, by the way, is exactly why a Bitcoin holder needs a bigger cash reserve than a stock holder does.

The extremes are grounded in reality too. Bitcoin's single-year floor in the model is set just past its worst actual year, and there's a cap on the upside so the fat tail doesn't produce years that never happened.

The assets also don't run independently, because markets move together in the real world. Bitcoin and stocks are tied at a correlation of about 0.35 — they don't move in lockstep, but they tend to fall in the same years more often than not. And inflation runs negatively correlated with stocks, so in the paths where your costs rise, your balances tend to fall. Those relationships come from long-term capital market research.

### What this means for your number

None of this makes the model right. It makes it honest about what it doesn't know, which is a different and more useful thing.

A model that assumed Bitcoin behaved like a bond fund would hand you a confidence number that looked wonderful and meant nothing. What you're getting instead is a number built on the assumption that the extremes stay likely, because for Bitcoin, they have.

### Homework

Your homework for this lesson is to:

1. Open your assumptions and confirm you could defend each one out loud. That's the standard, and it's the same standard the report's assumptions section is held to.
2. If any of them came from wanting a better answer rather than from information, change it back.



# Advanced Module 2 — Cash-Flow Optimization

*Reference material only. No filmed lessons.*

# Advanced Module 3 — Debt and Bitcoin-Backed Loans

## A3.1 Borrow against Bitcoin without getting liquidated
*`TEACH + APP` · ~2,460 words · ~16 min*

> **Gate.** Only if you are actually considering a Bitcoin-backed loan, or
> already hold one. If the answer is no, skip it. No is the common answer.

**By the end of this lesson, you can:**

- Explain how a Bitcoin-backed loan works, end to end
- Read LTV and know what moves it
- Size a cushion that survives a normal Bitcoin drawdown
- Know exactly what happens at a margin call, a top-up, and a liquidation
- Tell the difference between the main types of provider
- Model a loan in Orange Plan with rules that match your lender

---

Bitcoin-backed loans: how they actually work, how the numbers move, and what happens when they go wrong. This is the highest-stakes lesson in the Academy, so the whole mechanism comes first, before anything about whether you'd want one.

### What a Bitcoin-backed loan actually is

You pledge Bitcoin as collateral. A lender holds it and gives you cash. You pay interest on that cash. When you pay the loan back, your Bitcoin comes back.

**What makes it interesting:** you didn't sell, so in most cases there's no taxable event and you still own the upside.

**What makes it dangerous:** your collateral is the most volatile asset most people will ever own, and the lender's protection against that volatility is the right to sell your Bitcoin without asking you first.

### LTV, the one number that runs everything

Loan-to-value is your loan balance divided by what your collateral is worth. Borrow $50,000 against $200,000 of Bitcoin and your LTV is 25%.

Two things move that number, and only one is in your control:

- **Your loan balance** rises as interest accrues. Slow and predictable.
- **Your collateral value** moves with the Bitcoin price. Fast, and not predictable at all.

> 🎬 **GRAPHIC (the most important visual in this lesson).** Bitcoin price line
> falling 75% across the screen while the LTV bar climbs from 25% toward 100%.
> Draw the margin-call and liquidation lines as fixed horizontal marks, so the
> viewer watches LTV cross them. This single animation IS the lesson.

LTV rises much faster than the price falls, because the price is in the denominator. People underestimate this every time.

| Bitcoin falls | 25% LTV becomes |
|---|---|
| 50% | 50% |
| 70% | ~83% |
| 80% | 125% — the loan is worth more than the collateral |

**Your starting LTV matters more than anything else here.** It's the only variable you control before the market takes over.

### The three lines every loan has

Learn them in the order you'd hit them.

| Line | Typical | What happens |
|---|---|---|
| **Margin call** | ~65–70% LTV | The lender contacts you with a window to fix it, sometimes as short as 24–72 hours |
| **Liquidation** | ~80–85% LTV | The lender sells your Bitcoin to bring the loan back in range. You don't get a vote |
| **Release** | well below your start | Many lenders release collateral back to you, automatically or on request |

Every lender is different. These are shapes, not your numbers.

### Sizing the cushion

The gap between where your loan starts and the liquidation line is the entire drawdown you can live through.

Post $50,000 of Bitcoin as collateral with a lender whose liquidation LTV is 80%:

| Borrow | Starting LTV | Liquidation point | Drop it survives |
|---|---|---|---|
| $12,500 | 25% | $15,625 | 69% |
| $6,250 | 12.5% | $7,812 | 84% |

Bitcoin fell 84% in 2018 and 77% in 2022, so a 69% cushion sits inside drawdowns that have actually happened. Cut the starting LTV in half and the danger line moves dramatically further away. **That's the lever, and it's the only one you get.**

Size the cushion to survive a 70–80% drawdown at minimum, because that's the normal Bitcoin cycle and not a worst case. In practice that usually means starting at **10–15% LTV**, not the 40 or 50% a lender will happily hand you.

### A worked example

The couple holds 1.75 Bitcoin. At an illustrative $100,000/coin that's $175,000. They want $35,000 for a kitchen renovation and don't want to sell, because selling means a taxable gain and giving up the upside. They pledge all 1.75 BTC and borrow $35,000: a **20% starting LTV**.

| BTC price | Collateral | LTV | Read |
|---|---|---|---|
| $100,000 | $175,000 | 20% | Comfortable |
| $70,000 | $122,500 | 29% | Normal correction |
| $50,000 | $87,500 | 40% | Half the value gone, still fine |
| $30,000 | $52,500 | 67% | Margin call territory |
| $25,000 | $43,750 | 80% | Liquidation |

A 75% drawdown, a completely normal Bitcoin bear market, takes them from 20% right to the edge. That's what starting at 20% buys: it survives a normal bear, and it just barely survives it.

Run the same loan at a **50% starting LTV** and a 40% price drop hits the margin call. A 40% drop is an ordinary Tuesday in Bitcoin, not a bear market.

### What you can do at a margin call

Three options, and you want to know which one is yours long before the phone rings.

1. **Top up.** Send more Bitcoin as collateral. Lowers LTV without selling, and it's what most people do. Requires unpledged Bitcoin you can move quickly.
2. **Pay down.** Send cash to reduce the balance. Same effect from the other side. Requires cash available in exactly the week your net worth is falling.
3. **Do nothing and get liquidated.** The lender sells at whatever the price is that day, which by definition is a bad price.

**Two of the three require something held in reserve.** Take a loan with every spare satoshi pledged and no cash cushion, and you have exactly one option at a margin call — the bad one.

Decide your action at each line in writing, while nothing is falling. The moment the chip appears, the price is dropping and you'll be deciding at your absolute worst.

### Partial versus full liquidation

**Partial** means they sell only enough collateral to get you back under the threshold; you keep the rest and the loan continues. **Full** means they close the whole position, settle the loan, and return whatever collateral is left.

Ask which one your lender does before you sign, because it completely changes what a bad month costs you.

### The types of provider

No company names here; that landscape changes and any list goes stale. The structure doesn't.

- **Custodial lenders.** You send your Bitcoin and they hold it. Simplest to use. The risk is exactly the one from the custody module: in a legal sense it's their Bitcoin now, and if they fail you're a creditor standing in line. Several large ones failed in 2022 and their customers lost everything.
- **Collaborative-custody lenders.** Collateral sits in a multisig arrangement, often 2-of-3: you hold a key, the lender holds a key, a third party holds a key. The lender can't move your Bitcoin alone.

**Rehypothecation** is the question that separates them: does the lender lend your collateral out to someone else while holding it? It's the practice most directly responsible for the 2022 blowups. Ask directly, get the answer in writing, and treat anything other than a clear no as a risk that has nothing to do with the Bitcoin price.

**The 7 questions for any provider:**

1. Do you rehypothecate collateral?
2. Are you custodial or collaborative multisig, and who holds which key?
3. What are your exact margin call and liquidation LTVs?
4. How much notice do I get at a margin call, and how do you contact me?
5. Do you do partial or full liquidation?
6. Do you release collateral when LTV falls, and is that automatic or on request?
7. What's the interest rate, fixed or variable, and are there origination or early repayment fees?

> ⚠ Borrowing against your Bitcoin is the highest-stakes move in the Academy.
> Nothing here is telling you to take one of these loans. Lending terms,
> margin-call rules, and who actually holds your collateral vary a lot by
> lender. Read the actual agreement and run it past somebody who represents you
> before signing.

### The rules to write down before you borrow

1. **Start low enough to survive a 70–80% drawdown.** For most people, 10–15%.
2. **Keep unpledged Bitcoin or cash you can reach fast**, so a margin call has a good answer.
3. **Know your lender's three lines**, written down where you'll find them.
4. **Decide your action at each line in writing**, while nothing is falling.
5. **Never borrow for something you can't stop paying for.** A loan against a volatile asset funding a fixed obligation is how people get forced out at the bottom.

### Modeling the loan itself

Orange Plan models this as a real position inside your plan, not a calculator off to the side.

**Strategy → Debt → Add debt → Bitcoin-backed.** The form asks for what matters: lender, start date and term, collateral in **Bitcoin quantity** rather than dollars, margin call LTV, liquidation LTV, whether auto top-up is on, and whether the lender does full or partial liquidation.

⚠ **Enter your lender's real thresholds.** The app ships with common defaults; leave those and the plan tells you a comforting story that isn't yours.

**Collateral rules** is where the behavior gets modeled across the whole projection: auto top-up as a global default, the margin call percent that triggers a top-up, the top-up target it tops back down to, the liquidation percent, and the release trigger.

That last one is easy to miss and it matters: the app models **collateral release**, so a rising price that drops your LTV below the trigger frees collateral back into your plan instead of leaving it pledged forever.

The engine walks the loan forward year by year alongside the Bitcoin price path. Interest accrues, the price moves, LTV recalculates. Cross the top-up trigger and the model tops up from available Bitcoin. Cross liquidation and it sells per your chosen strategy and records the event. Pledged Bitcoin is protected from ordinary withdrawals, so the plan won't spend collateral you've committed.

Practically: run a 50% drawdown scenario with a loan in place and you're watching the loan's real behavior in that drawdown, not an assumption about it.

> 🎥 **SCREEN SHARE STARTS HERE — capture segment A3.1-B.** Everything above is teleprompter A-roll (segment A3.1-A); everything below is screen capture. This heading is the edit cut point.

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

**Whether to borrow at all, and if so, at what starting LTV and with which provider.**

How to think about it:

1. **Start with whether you need the money at all.** The cheapest loan is the one you don't take.
2. **Compare it honestly against selling.** Selling costs tax and upside; borrowing costs interest and adds a liquidation risk selling doesn't have. One is expensive, the other is risky, and those aren't the same kind of problem.
3. **Pick your starting LTV from the drawdown you want to survive**, not from what you're allowed to borrow.
4. **Pick your provider on structure, not rate.** A better rate at a lender who rehypothecates is not a better deal.

**If you couldn't fund a margin call, you can't afford the loan.**

### Homework

1. Decide whether a Bitcoin-backed loan belongs in your plan at all. No is completely legitimate, and it's the common answer.
2. If you're considering one, take the 7 provider questions to two or three lenders and put their answers side by side. The differences between lenders are the whole decision.
3. Model it in the app using your lender's real thresholds, not the defaults, and write down your specific action at each of the three severity levels.
4. Run the 50% drawdown scenario against it and watch what happens.



## A3.2 The four ways debt can build wealth
*`TEACH + APP` · 883 words · ~4 min*

> **Gate.** Watch this if you are carrying debt you could pay off but are choosing not to, or you are weighing whether to. If every debt already has a job you can defend, your debt policy is complete without it.

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

> 🎥 **SCREEN SHARE STARTS HERE — capture segment A3.2-B.** Everything above is teleprompter A-roll (segment A3.2-A); everything below is screen capture. This heading is the edit cut point.

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

# Advanced Module 4 — Allocation and Asset Location

## A4.1 The price context check: naming the emotion before a big move

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

# Advanced Module 5 — Tax Strategies

## 6.3 RMD risk and Roth conversions
*`TEACH` · 954 words · ~7 min*

> **Gate.** Watch this only when all three are true on your own Tax page: you hold meaningful pre-tax retirement assets, you expect lower-income years before forced distributions begin, and you have a way to pay the conversion tax that is not the converted money. All three, not two. If Orange Plan does not show that combination, your core tax plan is complete without it.

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

> **Gate.** Watch this if your Tax page shows either harvestable losses or unused 0% gains room this year. If it shows neither, there is nothing to harvest and your tax plan is complete.

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

## A5.3 State taxes and relocation: what the lever is actually worth
*`TEACH` · ~610 words · ~4 min*

> **Gate.** Watch this if either is true: you are actually considering a move,
> or your Tax page shows an unrealized gain large enough that your state's rate
> would change what you do. If moving is not on the table, your tax plan is
> complete without this.

**By the end of this lesson, you can:**

- Price the state lever on your own largest realistic sale
- Explain why residency is a legal standard rather than an address
- Sequence advice, move, and sale in the order that survives an audit

---

### The one dial that pays every year

The state you live in, specifically the state you're a resident of in the year you sell, can add double digits to the tax on a gain, or nothing at all.

You sell, you realize a gain, and you owe federal tax. Then your state can tax that same gain at its own rate. Most states tax a capital gain as regular income, with no special long-term rate. And a handful of states don't tax income at all. The state that charges you is the one you're a resident of in the year you sell, not the one you lived in when you bought.

Let me put numbers on it. Today, the couple sits on $115,000 of unrealized gain in their Bitcoin. If they realize that in a state with a roughly 9% rate, the state's cut is about $10,700. Take the same sale in Texas, and it's zero.

Now scale it to retirement. Same two states, on a $500,000 realized gain, which is a normal retirement-year sale for a Bitcoin-heavy household. The high-tax state takes about $46,500. The no-tax state takes nothing. Same Bitcoin, same sale, same federal bill. A $46,500 swing on one transaction.

And those saved dollars don't disappear. They go back into the plan and compound. I ran California against Florida for someone once, and the difference was about $5,800 a year. Over 5 years, that was $57,000 routed into Bitcoin instead of a state treasury.

One more thing that makes this lever different: it pays every year. Most tax moves in this module are one-shot, you make them in a particular year. A lower state rate applies to every sale you make for as long as you live there.

Now, three honest warnings.

First, moving is more than tax. It's family, work, community, roots. Those aren't things a tax number should decide, and no tax saving is worth a life you don't want.

Second, residency is a legal standard, not an address change. States look at your domicile: where your days are spent, where your home is, where your work and family are, where your life actually happens. You cannot buy this lever with a mailbox.

And third, sequence matters. High-tax states audit large exits, especially a big sale that lands right after a move. They know the pattern. If the sale is large enough, get state-tax advice first, then make the move, then make the sale. In that order.

So treat this one as lifestyle plus residency plus legal planning that happens to save you tax, not the other way around.

### Your decision

Your decision here is whether the state lever is worth acting on for you, and if it is, in what order.

Price it on your own largest realistic sale before you weigh anything else, because the number is either large enough to be part of a life decision or it isn't. If it is, the order is state-tax advice first, then the move, then the sale. Never the other way around.

### Homework

Your homework for this lesson is to:

1. Look up your state's treatment of long-term capital gains, and check whether it has a special rate or taxes them as ordinary income.
2. Run your largest realistic retirement-year sale against your current state's rate, then against a no-tax state. That difference is what the lever is worth to you.
3. If the number is big enough to matter, write down what would have to be true about family, work, and community for a move to make sense at all, before you look at the tax number again.


# Advanced Module 6 — Retirement Strategies

## 7.2 Health insurance between retiring and Medicare
*`TEACH` · 800 words · ~6 min*

> **Gate.** Watch this if your plan has you stopping work before 65. If your retirement date is 65 or later, Medicare starts when the paycheck stops and this does not apply to you.

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

> **Gate.** Watch this once you are inside about five years of retiring, or already drawing income. It prices the three ways to fund a year against each other; before that, the withdrawal order in core is the decision that matters.

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
- $600,000 taxable Bitcoin
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

**The couple's borrowing capacity, priced.** Austin's default is 10 to 15% LTV — the same number A4.1 sizes the cushion against.

- 10-15% of $600,000 collateral = $60,000 to $90,000 of capacity.
- One year of spending, $80,000, eats most of it. Two years running puts them at a ratio a normal bear market liquidates.

Add a year of interest. At 10-11%, $80,000 grows to about $88,000 a year later with nothing paid.

Drop Bitcoin 50%. Collateral is now $300,000. $88,000 against $300,000 = **29% LTV**, and a 75% drop — the normal Bitcoin bear — puts it at **59%**, inside margin-call territory.

The cushion is gone. They can't borrow again next year, and they're one leg down from liquidation.

Borrow from strength, not from a trap. A loan taken calmly at low LTV with a plan is a different product from one taken in a drawdown because you're cornered.

**Where borrowing works and doesn't:**

- **Works.** LTV is low, liquidity is behind it, you're comfortable holding it.
- **Doesn't.** As the foundation of a retirement paycheck. One year of spending uses the whole capacity. The second year has nowhere to come from.

Borrowing is a tool for a year, not a plan for a decade.

### Tool 3: Hold (buying compounding, and maybe more)

Don't touch the Bitcoin. Spend from the Reserve ($120,000).

The $600,000 keeps compounding.

Under current law (verify), it passes to heirs with a **step-up in basis**. If their basis is $100,000:

- $600,000 - $100,000 = **$500,000** of embedded gain that passes untaxed.

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

## A7.3 Concentration: one institution, one vendor, one firmware
*`TEACH` · ~815 words · ~5 min*

> **Gate.** Watch this if either is true on your own screen: (1) your
> non-self-custodied Bitcoin sits at a single institution and losing access to
> it for a few months would change your life, or (2) every satoshi you own is
> behind one model of one device from one manufacturer. If neither is true,
> your custody plan is complete without this.

**By the end of this lesson, you can:**

- Tell a concentration failure apart from a custody failure
- Decide whether your custodial Bitcoin belongs at more than one institution
- Name what your entire self-custodied stack is trusting
- Decide honestly whether you can maintain a second setup at all

---

### Don't hold it all at one institution

You picked a custody level in the core course. This lesson asks a different question about the same stack: how concentrated is it? Not what type of custody, but how many baskets.

Start with whatever you have not self-custodied yet. How many institutions is it sitting in?

Those 2022 failures weren't self-custody failures. They were concentration failures. The customers who lost everything are the ones who had everything in one place.

So for the custodial part of your stack, your exchange balance, any ETF shares, your retirement exposure, the question is whether one company's bad week can take all of it. I'd add a second institution in three cases. When the custodial amount is big enough that losing access for a few months would change your life. When you're using an exchange balance as your emergency pile, because that job needs a backup for the week the account is frozen. And when the institutions actually fail in different ways, because two exchanges are more correlated with each other than an exchange and a brokerage ETF are.

It costs you something, though, and I don't want to gloss over it. Every extra account is another login, another email to secure, another two-factor setup. Three sloppy accounts are worse than one hardened one. Every extra account is another set of tax lots to reconcile. And every extra account is one more row your executor has to find, so if it doesn't make it onto your Family Custody Map, you've effectively hidden money from your own family.

So the honest rule: self-custody is the real answer to counterparty risk. Splitting across institutions is the hedge for whatever isn't self-custodied yet. Add the second institution when the amount justifies the maintenance, and not before.

### No custody setup is trust-free

There's one more layer, and it's the one people miss, because it sounds like self-custody already solves it. Self-custody removes counterparty risk. It does not remove trust. It moves it.

When you hold your own keys, you're still trusting the company that made your hardware wallet. The firmware running on it, including every version you install after this one. That the device generated your seed with real randomness. And whatever wallet software you use to check your balance and build transactions.

None of that is an argument against self-custody. I self-custody, and I think most people holding a meaningful amount should. It's an argument for being honest about what you're actually relying on, because the thing you never examined is the thing that can take all of it.

So the same concentration question applies here. If every satoshi you own is behind one model of one device, running one company's firmware, generated by one implementation, then one trust is holding up your entire stack. That's the same concentration as keeping everything at one exchange. It's just harder to see, because it feels like independence.

Spreading it out is what protects you from a total loss. A second device from a different manufacturer. A multisig where the keys don't all come from one vendor. Or keeping part of the stack in a different custody model entirely.

Now, I'd slow down here, because more setups is not automatically safer. A second device you don't understand, don't back up, and never test is a new way to lose money, not a hedge. So size this to three things: how comfortable you actually are, how much technical ability you want to use, and how much responsibility you're honestly willing to take on. And if the honest answer is that you can only maintain one setup well, run one setup well and keep it simple. Three setups you half understand is how people lose money.

### Your decision

Two decisions, and either one can honestly come back as "not yet."

Whether your custodial Bitcoin should sit at more than one institution, which you decide from the amount rather than from principle. And whether your self-custodied stack should sit behind more than one vendor, which you decide from what you can genuinely maintain.

If the honest answer to both is that you can run one setup well and that's it, then run one setup well. That is a real answer, not a postponed one.

### Homework

Your homework for this lesson is to:

1. For anything not self-custodied, count the institutions it's sitting in and be honest about whether that number matches what's at stake.
2. Go through what your whole stack is trusting: the device, the manufacturer, the firmware, the wallet software. If one answer covers everything you own, decide whether spreading it out is worth the setup you'd have to maintain.
3. Whatever you add, add it to your Family Custody Map the same day. An account your executor can't find is money you hid from your own family.


## A7.4 Wallet operations: UTXOs, dust, consolidation, and addresses
*`TEACH` · ~830 words · ~5 min*

> **Gate.** Watch this before you have made a hundred small transfers, not
> after. It applies if you buy Bitcoin regularly in small amounts, or if your
> wallet already shows a long list of separate chunks under coin control.

**By the end of this lesson, you can:**

- Explain why your balance is a stack of bills rather than a bucket
- Set a transfer threshold as a fee test that does not go stale
- Decide whether you have a consolidation chore waiting
- Use a fresh receiving address every time, and say why it matters

---

In today's lesson, we're going to cover two operational things about moving Bitcoin that almost nobody explains, and both of them came from clients asking me directly.

### Your wallet is a stack of bills

A client asked me what happens to all the small buys he'd made over the years. His worry was that a bunch of tiny purchases might end up stranded, and that's actually a real thing.

Your wallet isn't a bucket with a balance in it. It's more like a wallet full of bills. Every time Bitcoin lands in your wallet, that deposit is its own separate chunk, and the technical name for one of those chunks is a UTXO, an unspent transaction output. Your balance is the sum of the bills, and when you spend, your wallet grabs one or more whole bills to cover the amount. You spend whole bills, not slices of them.

Now the part that costs money. Every chunk you spend adds to the fee, and that fee doesn't care how big the chunk is. So a very small deposit can become uneconomical to move, because the fee to spend it approaches or exceeds what it's worth. That's what people mean by dust.

If you've been buying small amounts regularly, you can end up with a wallet made of a hundred tiny chunks. Nothing is lost. But the day you go to move it all, you're paying to spend every one of those chunks at once, and if fees are high that day, it gets expensive.

### The two fixes

There are two fixes, one for going forward and one for what you already have.

Going forward, transfer on a threshold rather than on a schedule. Instead of moving every small buy to cold storage the day it happens, let them accumulate on the exchange and move them in one transaction.

Now, I'm deliberately not going to give you a fixed number of Bitcoin here, because the right threshold moves with the price and with what fees are doing. The test that doesn't go stale is this: look at what it would cost in fees to spend that chunk later, and ask whether that's a rounding error against the chunk or a real bite out of it. If a transfer's fee is a meaningful percentage of what you're transferring, it's too small. Check fees on the day, because they swing enormously.

The trade-off is real, though, and worth saying out loud. Everything waiting for the threshold is sitting on an exchange, which is exactly the counterparty risk the custody module is about. So the threshold is a fee decision bounded by a custody decision. If the accumulating balance gets big enough to worry you, move it and pay the fee.

For what you already hold, the fix is consolidation. You send those small chunks to yourself in one transaction, which combines them into one bigger chunk. Do it deliberately on a day when fees are low, not on the day you urgently need to move money. It's a chore for a quiet Sunday and an annual custody review item, not an emergency.

### Addresses are public

The second thing is addresses. Another client was surprised to learn that if somebody knows one of your receiving addresses, they can look up the entire history of that address on the blockchain. Bitcoin's ledger is public. That's the whole design.

So if you use the same receiving address over and over, you've handed anyone who has it a running total of everything you've ever received there. That's not a theft risk directly. It's a privacy risk that becomes a personal safety question once somebody can tie an address to your name.

The fix is easy. Use a fresh receiving address every time you receive. Modern wallets generate a new one automatically and it's usually the default, so mostly this is about not overriding it. And don't post an address publicly and then keep using it.

This is also another reason to check the address on the device screen every single time. It should be a new one, and if it isn't, something is worth understanding before you send.

### Your decision

Your decision here is your transfer threshold, stated as a fee test rather than a fixed amount, and whether you have a consolidation chore waiting.

### Homework

Your homework for this lesson is to:

1. Open your wallet and look at how many separate chunks your balance is actually made of. Most wallets will show you this; some call it coin control.
2. Check what fees are doing today, and write down your transfer threshold as a fee test: the smallest transfer where the fee to spend it later is still a rounding error.
3. If you're holding a pile of small chunks, put consolidation on your annual review as a low-fee-day chore.
4. Confirm your wallet is generating a fresh receiving address each time, and that you haven't published one you keep reusing.


## 8.5 Advanced custody: passphrase, multisig, and collaborative
*`TEACH` · 1,354 words · ~9 min*

> **Gate.** Watch this if your custody setup fails one of the two access tests from the estate module: one person can spend alone, or one lost copy could permanently stop recovery. If your Level 2 design passes test two and you have accepted failing test one deliberately, your custody plan is complete.

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


### Building the estate split on each path

The estate module gives you the two tests: can one person spend alone, and can one lost copy permanently stop recovery. What it deliberately doesn't do is show you how to build a setup that passes both, because that's a custody decision. So here's how each path carries the split.

On the passphrase path, Anthony Park calls this poor man's multisig, and it works because of how a passphrase behaves. Seed plus passphrase produces a completely different wallet than the seed alone. Same words, different passphrase, different set of coins. So the seed by itself opens a real wallet that's empty, and the passphrase by itself is a word that opens nothing. Two objects, each worthless alone, which is exactly what lets you hand each one to a different person.

Your heir holds the seed. Your executor holds the passphrase. Together they have full access, apart they have nothing. That's test one, passed by design.

Now test two, and this is the trap. Seed plus passphrase is a two-of-two. Both pieces are required every single time. So if the seed card is lost in a fire, the passphrase opens nothing. And if the executor dies without passing the passphrase on, the seed opens an empty wallet. Either one is a total, permanent loss with nobody having done anything wrong. Half of a two-of-two is zero.

Which means each half needs its own backup, on its own side. A second steel copy your heir controls, or one their own successor can reach, never anywhere the passphrase holder can also get to. The passphrase written once, sealed, held by the executor or whoever he names after him, never in the same house or the same safe as the seed.

On the multisig path, a two-of-three vault passes both tests structurally, without you engineering the backups yourself. Any two of the three can spend, so losing one key entirely is survivable, and no single holder can spend alone. Both tests, handled by the arithmetic.

The distribution that makes it work as an estate plan: you hold two keys, so nothing about your day changes and you spend on your own just like today. Your executor holds the third as a sealed seed card, and since one key alone can't spend, they can't touch anything while you're alive. If you're with a collaborative provider, they hold the remaining key and never your seed phrase. After you're gone, your executor and the provider hold two keys between them, which meets the threshold, and the provider verifies who the executor is and walks them through it. Your heirs get a guided recovery instead of a technical exam.

The one thing to get right is where the config file sits. An executor's key stored next to the config file is one step from control, and that quietly turns your two-of-three into a single-key setup. So the config lives in a password manager, never printed, never stored with any physical key.

So with a passphrase you're splitting two different objects between two people. With multisig the keys are already separate, and the job becomes keeping the config away from whoever holds a key. Same principle, different setup.

### Homework

- Decide whether an advanced setup is warranted at all. Staying at a well-run Level 2 is a legitimate answer.
- If you're adding a passphrase, generate it with 7 random words from a wordlist, using dice or an offline generator. Back it up separately from the seed, and practice with a small amount first.
- If you're considering collaborative custody, ask a provider the four questions and get the answers in writing before you pay anything.
- If you're running multisig, go find your config file, back it up, and tell one other person it exists.

# Advanced Module 8 — Advanced Estate Planning

## 9.5 Advanced: do you need a trust, and which one?
*`TEACH + APP` · 1,923 words · ~9 min*

> **Gate.** Watch this if your Protect page's projected estate crosses the trust gate, or you have a minor child, a blended family, property in more than one state, or a beneficiary who should not receive a lump sum. Most households run the gate, get a no, and are finished.

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

### The duty that can force your trustee to sell

Before you hire anybody to draft this, one piece of law makes a Bitcoin trust different from every other trust, and it is the most expensive thing here to not know.

A **trustee** is whoever manages the trust for the beneficiaries. Trustees are generally held to a **prudent-investor standard**: manage the assets the way a careful, reasonable investor would. One thing that standard treats as careful is **diversification**.

So a trustee holding a large, concentrated Bitcoin position is on the wrong side of that duty by default. They can be legally pressured to sell it, and if they don't, they can be personally liable to the beneficiaries. **That duty puts your trustee's own money on the opposite side of your Bitcoin thesis**, whether or not concentration was what you intended.

**The fix is a waiver** written into the trust document, releasing the trustee from the duty to diversify this particular asset. It reframes holding the Bitcoin as the prudent thing rather than the exposed thing. Not automatic, not boilerplate: an attorney has to decide to draft it in.

**What happens when nobody asks.** Our couple lights up the gate a decade from now. The stack has done what they hoped, and they pay a good local attorney to build a trust around it. Documents clean, signing perfect. Then he dies, and the trustee sells the Bitcoin. All of it. The trustee sold the exact asset the trust was built to hold, doing exactly what the standard asked of them.

The attorney wasn't careless. The conversation never happened. The problem was a question nobody asked, not a skill nobody had.

> **So one question goes on top of the attorney checklist from the executor
> lesson:** *for a trust, will you waive the prudent investor rule, so the
> trustee isn't obligated to diversify out of Bitcoin?* An attorney who hasn't
> heard that question before hasn't drafted this kind of plan.

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
