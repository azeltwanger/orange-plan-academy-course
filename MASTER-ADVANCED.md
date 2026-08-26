# Orange Plan Academy — Advanced Bitcoin Planning Library

> ## ⛔ Read `AUSTIN-AUTHORITY.md` before editing any lesson.
>
> Austin's dictated planning recommendation is the authority. You may fix math
> and facts (A), flag contradictions (B), and you may **not** rewrite a planning
> judgment (C) without his explicit direction. Open items live in
> `AUTHORITY-FLAGS.md`.

**Course 2 of 2.** Optional. The A-numbers are final, and each section mirrors the core module that owns the decision.

Complete the matching core Build Your Plan area first. The core walkthrough enters the real data and establishes the plan of record. An advanced lesson starts from that completed area and goes deeper only when its gate is true.

Nothing here is required to finish a plan. Each lesson opens with a gate you can check against your own situation or screen. If the condition does not apply, that planning area is complete without the lesson.

Advanced lessons do not recreate onboarding, rebuild Foundation, or run the first confidence check. They may explain a result, model a triggered decision, or compare a scenario. A preview or scenario stays separate from the plan until the app explicitly applies it.

Every advanced video closes with a decision and a short homework/finish line. The student-facing text carries current figures and verification notes that should not be frozen into a video.

---

# Advanced Module 1 — Modeling and Assumptions

## A1.1 How Orange Plan models Bitcoin: fat tails, correlations, floors and caps
*`TEACH` · ~400 words · ~3 min*

> **Gate.** Watch this if either is true on your own screen: changing one
> assumption moved your Plan page's confidence number by more than 10 points and
> you want to know why, or you are about to hand your report to someone who will
> ask how the simulation works. If your number is stable and nobody is auditing
> it, core 1.3 already taught you to *read* it and your plan is complete without
> this. This lesson is how the number is *built*.

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

Size the cushion to survive a 70–80% drawdown at minimum, because that's the normal Bitcoin cycle and not a worst case. In practice that means starting somewhere between **10 and 20% LTV**, not the 40 or 50% a lender will happily hand you.

Where you land inside that range is a risk tolerance call (Austin, 2026-08-08), and the ends buy different things:

| Starting LTV | Liquidation at an 80% line | Survives |
|---|---|---|
| 10% | a fall of about 87% | every drawdown in Bitcoin's history |
| 15% | a fall of about 81% | 2022 (−77%), not 2018 (−84%) |
| 20% | a fall of 75% | neither 2022 nor 2018 |

Both ends are defensible. The worked example below sits at 20%, the top of the range.

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

No company names here; lenders change and any list goes stale. The structure doesn't.

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

1. **Start low enough to survive a 70–80% drawdown.** Somewhere between 10 and 20%, closer to 10 the more of that drawdown you want to live through.
2. **Keep unpledged Bitcoin or cash you can reach fast**, so a margin call has a good answer.
3. **Know your lender's three lines**, written down where you'll find them.
4. **Decide your action at each line in writing**, while nothing is falling.
5. **Never borrow for something you can't stop paying for.** A loan against a volatile asset funding a fixed obligation is how people get forced out at the bottom.

### Modeling the loan itself

Orange Plan models this as a real position inside your plan, not a calculator off to the side.

**Strategy → Debt → Add debt → Bitcoin-backed.** The form asks for what matters: lender, start date and term, collateral in **Bitcoin quantity** rather than dollars, margin call LTV, liquidation LTV, whether auto top-up is on, and whether the lender does full or partial liquidation.

⚠ **Enter your lender's real thresholds.** The app ships with common defaults; leave those and you are modelling somebody else's lender, not yours.

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

*`TEACH` · ~430 words · ~3 min*

> **Gate.** Watch this before any Bitcoin-heavy move: a large buy, selling to
> lock in gains, or taking a Bitcoin-backed loan. Your allocation decision is
> complete without it.

**By the end of this lesson, you can:**

- Run two lookback windows before a Bitcoin-heavy move
- Separate what the recent price makes you feel from what the longer trend says
- Decide whether the plan or the price is driving the move

---

This is a short check to run before any Bitcoin-heavy move. A large buy, a sale to lock in gains, or a Bitcoin-backed loan can all be reasonable decisions. The problem is that the exact same decision can also be an emotional reaction to the last few months.

The point of this check is not to tell you whether to buy, sell, or borrow. It is to name what is in the room before you decide.

### Two lookbacks

Start with the recent window: 3, 6, 9, and 12 months.

That window tells you what you are feeling. If Bitcoin is up 40% in three months, there is probably some FOMO in the decision. If it is down 40%, there is probably fear. You do not need to pretend either one is not there. You just need to name it.

Next, use the 2-to-5-year window.

That window tells you what has actually happened over a meaningful period. It shows the direction of the trend instead of the mood of the last week.

The recent window names the emotion. The long window gives it context.

### Put the proposed move back against the plan

Now describe the move without using today's price as the reason.

Why does it fit your allocation target, cash reserve, debt ceiling, tax plan, or retirement-income strategy? What problem is it solving? What would still make the decision reasonable if Bitcoin moved the other direction next month?

If you cannot explain it without saying that the price has been going up or going down, the price is probably doing more of the work than the plan is.

That does not automatically make the move wrong. It means you should wait a beat, open the owning page or scenario, and make sure the numbers support what the emotion wants to do.

### Your decision

Whether this move is the plan talking or the price talking.

### Homework

1. Write a plain explanation of the move without mentioning the recent Bitcoin price.
2. Write what the 3-to-12-month window makes you feel and what the 2-to-5-year window shows.
3. Open the owning plan page or scenario and confirm the move still makes sense against the rules you already set.

You are done when you can defend the move from the plan even if the last three months of price action were reversed.

# Advanced Module 5 — Tax Strategies

## A5.1 RMD risk and Roth conversions
*`TEACH` · ~1,095 words · ~7 min*

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

In today's lesson, we're going to cover why a large traditional account can create forced taxable income later, and how Roth conversions can reduce that risk during the years when you control more of the income.

### What an RMD is

RMD stands for required minimum distribution.

It is the minimum amount the tax rules require an owner or beneficiary to distribute from certain retirement accounts.

For an owner, the yearly amount is generally the prior December 31 balance divided by the life-expectancy factor that applies to that person.

The applicable starting age depends on the birth cohort.

Under current law, age 73 applies to the intermediate cohort, and age 75 applies to people who attain age 74 after 2032. The couple in this course is 45 now, so their current-law planning age is 75.

Roth IRAs and designated Roth plan accounts do not require lifetime distributions from the original owner under current law. Beneficiaries still have distribution rules.

### Why the account can become a problem

Traditional retirement money is not bad money.

The problem is a mismatch between the deduction you received while contributing and the forced income the account may create later.

The couple contributes $16,500 per year including the employer match in the illustration.

At a flat 7% illustration for 15 years, that grows to roughly $415,000 around age 60. Left for another 15 years at the same flat rate, it is roughly $1.14 million around age 75.

Using the current age-75 Uniform Lifetime factor of 24.6 as an illustration, the first required distribution would be roughly $46,000 before adding Social Security or any other income.

Those are illustration assumptions, not a projection promise. The app should calculate the actual roadmap from the saved account, return, and tax assumptions.

### Why bitcoin exposure makes the sensitivity larger

Now run an intentionally extreme sensitivity check.

A flat 20% return on the same annual contributions would produce roughly $1.19 million after 15 years, then more than $18 million after another 15 years if that flat return continued.

At the same illustrative divisor, the forced distribution would be hundreds of thousands of dollars.

That is not the return assumption I would use as the baseline. It is a sensitivity example showing why a fast-growing asset inside a traditional account deserves attention before the forced-distribution years arrive.

### What a roth conversion does

A Roth conversion moves money from a traditional account into Roth.

The taxable amount generally enters ordinary income in the conversion year. The converted amount then sits in the Roth bucket, where qualified distributions can be tax-free and the original owner has no lifetime RMD under current law.

The conversion is not free. You are choosing when to recognize the income.

The planning opportunity appears when today's all-in cost is lower than the cost you reasonably expect later, or when reducing the traditional balance creates flexibility the household values.

### The RMD itself cannot be converted

Once an RMD is due for a year, the required amount has to come out. That required amount is not eligible to be converted.

A conversion can happen in the same year after the RMD is satisfied, but the required distribution is already taxable income and already fills part of the year's room.

That is one reason the years before RMDs can be valuable.

### Lower price, more units for the same dollar conversion

The conversion amount is measured in dollars on the conversion date.

If Bitcoin is held inside the traditional account, a lower Bitcoin price means the same dollar conversion can move more Bitcoin units into Roth.

That can be useful, but it is not a reason to time the market with taxes. The tax bill, available cash, future growth assumption, and household risk all still matter.

### Do not stop at the bracket

The course used to frame the decision as filling a bracket without spilling into the next one.

That is only the first pass.

A conversion can also affect Marketplace credits, the taxable portion of Social Security, Medicare IRMAA, NIIT, capital-gain room, state tax, deductions, and credits.

So model the all-in marginal cost of the next conversion dollar.

There may be a point where the federal bracket has not changed, but the healthcare or state-tax cost makes the next dollar unattractive.

### Paying the tax

When possible, paying the conversion tax from taxable cash or another outside source keeps the full converted amount in Roth.

That is generally cleaner than withholding part of the conversion, especially before age 59½, when an amount not converted may also be treated as an early distribution unless an exception applies.

But "always pay from outside" is not a universal command. Liquidity, reserve needs, tax basis, and the rest of the plan still come first.

### The beneficiary rule is not one sentence

The old script said the children would simply have 10 years to empty an inherited traditional account.

Many nonspouse designated beneficiaries do face a 10-year outside deadline. But eligible designated beneficiaries have exceptions, and annual distribution requirements within the 10 years can depend on when the owner died and whether RMDs had started.

So traditional money can leave heirs with a shorter distribution window and a larger tax problem. The exact schedule depends on the current beneficiary rules and the family's tax situation, so I would verify this part with the CPA.

### The decision frame

A conversion is attractive when:

- the household is in a genuinely lower all-in marginal-cost year;
- taxable liquidity can cover the tax without weakening the reserve;
- the traditional balance is on track to create forced income later;
- the household values more Roth flexibility;
- the plan remains strong after paying the tax.

A conversion is less attractive when:

- it destroys Marketplace credits or triggers another threshold;
- the tax has to come from money the household needs soon;
- the later rate is likely to be lower;
- the move is being sized from a bracket table without the rest of the return.

### Homework

1. Open the Tax roadmap and identify the first low-income year before the applicable RMD age.
2. Model three conversion sizes, including zero.
3. Read federal tax, state tax, healthcare or Medicare effects, capital-gain room, and ending account balances together.
4. Take the result to the tax professional as a proposed range, not a filing instruction.

You are done when you know which years deserve an annual conversion review and what all-in cost would make you stop.


## A5.2 Harvesting losses and gains
*`TEACH` · ~812 words · ~5 min*

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

In today's lesson, we're going to cover two moves that sound opposite but solve the same problem.

Loss harvesting records a loss when the tax value of the loss is useful.

Gain harvesting records a gain when the tax cost is low enough to justify a higher basis.

Neither move begins with the market. Both begin with your records and the whole tax return.

### Loss harvesting

A capital loss first offsets capital gains.

If total capital losses still exceed gains, an individual can generally deduct the current annual limit against income and carry the unused loss into future years.

The value of the loss depends on what it offsets.

A loss used against a high-rate short-term gain can be more valuable than a loss carried for years and eventually used against a lower-rate long-term gain.

So do not multiply every harvested loss by one marginal tax rate and call that the savings.

### The lot has to be identified

Suppose the couple owns one low-basis Bitcoin lot and one recent high-basis lot.

If the recent lot is below its acquisition price, they may have a loss to realize while keeping the older low-basis lot.

But the lot does not become the tax lot because the app calls it HIFO.

For self-custody, the particular units have to be identified in the books and records no later than the transaction, and the records have to establish those units left the wallet.

For broker-held Bitcoin after 2025, the broker has to receive an instruction using identifiers it accepts no later than the transaction, and the taxpayer keeps substantiation.

If the identification fails, the current default generally uses the earliest-acquired units in that wallet or account.

That can turn a planned loss into an unexpected gain.

### Wash-sale treatment

Under current federal law, the wash-sale rule in section 1091 applies to stock or securities.

Spot Bitcoin is generally treated as property rather than stock or a security for this rule, so selling spot Bitcoin at a loss and repurchasing it has generally not triggered the stock wash-sale rule.

That statement is deliberately narrow.

A tokenized stock or another digital asset that is itself a stock or security can be covered. Congress can change the law. State treatment can differ. Verify the rule in the year you act.

### The real cost of the round trip

The tax value is only one side.

The other side includes:

- trading spread and fees;
- network fees;
- price movement between sale and repurchase;
- recordkeeping and lot-identification risk;
- a higher future gain because the repurchased units have a new basis;
- the effect on holding period.

A harvest is useful when the present value of the tax benefit is worth more than those costs and the future tax trade-off.

### Gain harvesting

Gain harvesting does the reverse.

You deliberately realize a long-term gain in a year when the all-in tax cost is low, then reacquire the position and establish a higher basis.

A federal zero-percent capital-gain rate does not automatically make the move free.

Ordinary taxable income fills the stack first. State tax may apply. A larger gain can reduce Marketplace credits, trigger NIIT at higher income, or affect other income-based rules.

So the usable gain room is the amount the whole return can absorb at an acceptable all-in cost.

### A simple example

Assume a taxable Bitcoin lot is worth $100,000 with $40,000 of basis.

Selling the lot realizes a $60,000 gain.

If the whole gain fits in an acceptable all-in tax window, the household can repurchase and reset basis near $100,000.

If only half fits before another threshold becomes expensive, harvesting the full lot is not the right move. Sell the amount that fits, or pass.

### Hifo is a policy, not the strategy

Highest-in, first-out can reduce current gain when the identification rules are met.

But it is not always the best long-term choice.

Using the highest-basis units now leaves the lowest-basis units for later. That may be exactly what the household wants, or it may create a larger gain in a future year when the rate is worse.

The decision is not "HIFO good, FIFO bad."

It is which identified units create the best lifetime tax path while preserving the custody and spending plan.

### Homework

1. Reconcile the lots and mark which units are actually identifiable under the current wallet or broker rules.
2. Model one loss harvest and one gain harvest.
3. Include fees, spread, state tax, ACA or Medicare effects, NIIT, holding period, and the future-basis consequence.
4. Save the move as a modeled possibility until the tax professional confirms the current-year return treatment.

You are done when the app shows the tax benefit, the execution cost, and the future basis together—and when passing is allowed to be the right answer.


## A5.3 State taxes and relocation: what the lever is actually worth
*`TEACH` · ~488 words · ~3 min*

> **Gate.** Watch this if either is true: you are actually considering a move,
> or your Tax page shows an unrealized gain large enough that your state's rate
> would change what you do. If moving is not on the table, your tax plan is
> complete without this.

**By the end of this lesson, you can:**

- Price the state lever on your own largest realistic sale
- Explain why residency is a legal standard rather than an address
- Sequence advice, move, and sale in the order that survives an audit

---

In today's lesson, we're going to price the state-tax difference without pretending a map can decide where you live or where a state can tax you.

### The lever can be large

A large taxable Bitcoin gain can produce very different state results.

Some states impose no individual income tax. Others tax capital gains as income, use separate rates, or apply special rules.

The app can compare two state assumptions against the same modeled sale. That is useful because it turns "this state is expensive" into a dollar estimate on your own plan.

Do not freeze one example rate into the video. The current rate, deduction, credit, and local-tax rules belong in the app or current source.

### The sale date is not the whole residency test

The course used to imply that the state where you live in the year of sale is the whole answer.

It is not.

States can look at domicile, statutory residency, days in the state, the location of a home, family and business ties, part-year residency, source income, community-property rules, and the ownership structure involved.

Changing an address does not necessarily change domicile. Leaving a state does not necessarily end every source-based tax claim.

That makes the order important:

1. Decide whether the move makes sense for the life you want.
2. Before a large transaction, learn what the old state and the new state require to establish or end residency.
3. Document the real move rather than manufacturing a tax paper trail.
4. Model the transaction only after the legal residency assumption is defensible.

### Price the whole move

State income tax is one line.

Also price:

- housing and property tax;
- insurance;
- healthcare access and premiums;
- travel back to family or business;
- local sales and other taxes;
- legal and moving costs;
- the value of the life you are leaving.

A tax saving can be real and still not be worth the move.

### The right output

The output of this lesson is not "move to a no-tax state."

It is one of three answers:

- moving is already part of the life plan, and the tax difference affects timing;
- moving is genuinely on the table, and the tax difference deserves professional modeling;
- moving is not on the table, so the state tax is a cost the plan should include rather than a problem to keep revisiting.

### Homework

1. Run the same modeled gain under the current state and one realistic alternative.
2. Add the major non-income-tax costs of the move.
3. Write whether the move is a lifestyle decision, a real option, or not an option.
4. Before acting, have a professional in the relevant state confirm domicile, part-year, source-income, and transaction treatment.

You are done when the state-tax difference is a number inside a real life decision, not a reason to move on its own.


# Advanced Module 6 — Retirement Strategies

## A6.1 Health insurance between retiring and Medicare
*`TEACH` · ~754 words · ~5 min*

> **Gate.** Watch this if your plan has you stopping work before 65. If your retirement date is 65 or later, Medicare starts when the paycheck stops and this does not apply to you.

**By the end of this lesson, you can:**

- Compare COBRA, ACA marketplace, and health-sharing for early retirement
- Understand how MAGI affects your ACA subsidy
- See the tension between Roth conversions and healthcare subsidies
- Price your healthcare bridge three ways

---

In today's lesson, we're going to price the healthcare bridge between leaving work and becoming eligible for Medicare.

This lesson applies when the paycheck stops before 65 and employer coverage stops with it.

### The bridge is a dated expense

If you retire at 60, the bridge is roughly five years.

The plan needs the premium, expected out-of-pocket cost, and a stress allowance for each year. It also needs the end date, because Medicare changes the coverage structure at 65 even though healthcare costs do not disappear.

### Option one: employer continuation

COBRA or another continuation right may let you keep the employer plan for a limited period.

For many qualifying events, federal COBRA commonly lasts up to 18 months, with longer periods possible in some situations. The household may pay the full premium plus an administrative charge.

The advantage is continuity: same network, deductible structure, and claims process.

The disadvantages are price and the short runway.

Use the actual election notice. Do not assume every employer, event, or state follows the same duration.

### Option two: the marketplace

Marketplace coverage is where tax planning and healthcare planning meet.

The net premium depends on household income, household size, the benchmark plan, location, and the law in the enrollment year.

For 2026, the enhanced pandemic-era subsidy rules no longer continue in the same form. That is exactly why the course should not memorize an old income cliff or an old premium example.

Use the current Marketplace estimate for the ZIP code and ages involved.

Also price the out-of-pocket side. Cost-sharing reductions apply only to eligible households enrolled in a Silver plan, and eligibility changes with income.

### Magi is part of the premium

A Roth conversion, large taxable gain, business income, or retirement distribution can raise Marketplace income and reduce a premium tax credit.

That does not make the tax move wrong. It means the premium change is part of the tax cost.

The tax page and healthcare worksheet have to use the same income assumption. A conversion modeled without the premium effect is incomplete.

### Option three: a health-sharing arrangement

Austin's family uses CrowdHealth, and that personal experience can stay in the lesson as personal experience.

The category has to be described accurately.

A health-sharing arrangement is not health insurance. It generally does not create the same legal obligation to pay a claim, and the terms, exclusions, waiting periods, pre-existing-condition rules, member responsibility, and provider process vary by organization.

Price the exact current membership and read the current member agreement. Do not generalize one program's rules to the category.

HSA eligibility is a separate question. A sharing membership does not by itself create an HSA-eligible high-deductible health plan. Verify the actual coverage and current tax rules before making contributions.

### Option four: a spouse or other eligible plan

A spouse's employer plan, retiree coverage, a union plan, or another special eligibility path can be the best bridge when it is available.

The right comparison uses the incremental family premium, deductible, network, and employer contribution—not only the employee's headline premium.

### The comparison

For each real option, record:

- monthly premium;
- deductible and out-of-pocket maximum;
- network and prescription fit;
- expected routine cost;
- worst plausible annual cost;
- tax-credit or tax-deduction assumptions;
- duration and the next enrollment trigger;
- whether the arrangement is insurance and what payment is legally guaranteed.

### At 65

Medicare eligibility changes the bridge, but enrollment timing, employer coverage, HSA contributions, Medigap, Medicare Advantage, prescription coverage, and IRMAA can all matter.

Do not wait until the final month to learn those rules. Put a Medicare review on the calendar before 65.

### Put it in the plan

Enter the best current estimate as a dated expense change from retirement until Medicare eligibility.

Then run a high-cost scenario that uses the out-of-pocket maximum or another defensible stress year.

The app may model the spending and tax result without reproducing every Marketplace or Medicare rule. The current quote and eligibility determination still come from the official enrollment source.

### Homework

1. Price every option actually available to the household.
2. Use the same income assumption in the tax and healthcare comparison.
3. Enter the base bridge cost and one stress case.
4. Put the next enrollment and Medicare review dates on the calendar.

You are done when the bridge has a current source, an end date, and a high-cost case—and when a health-sharing membership is never described as insurance.


## A6.2 Sell, borrow, or hold: funding a year of spending
*`TEACH` · ~943 words · ~6 min*

> **Gate.** Watch this once you are inside about five years of retiring, or already drawing income. It prices the three ways to fund a year against each other; before that, the withdrawal order in core is the decision that matters.

*Advanced. Borrow-vs-sell is a decision that only fires if you're considering asset-backed lending against Bitcoin. Skim unless the trigger applies to you.*

**By the end of this lesson, you can:**

- Understand three ways to fund retirement from a Bitcoin-heavy plan
- Price sell, borrow, and hold on one year of spending
- Understand why LTV cushion is the whole borrow decision
- Mix the three tools across years

---

In today's lesson, we're going to compare three ways a Bitcoin-heavy household can fund one year: sell, borrow, or hold and spend from another bucket.

This lesson fires when retirement is close enough that the household is actually deciding how next year's spending gets funded.

### One year, three different costs

Use the same annual spending need for all three paths.

The comparison is not about which one sounds most Bitcoin-aligned. It is about what each path costs the plan in taxes, interest, liquidity, risk, and family complexity.

### Path one: sell

Selling Bitcoin creates cash with no loan to manage.

The tax is based on the gain in the specifically identified units, not the gross sale proceeds.

A low-income year may place some long-term gain in a lower federal capital-gain band. But ordinary income fills the stack first, state tax may apply, and the gain can affect Marketplace credits, NIIT, or other thresholds.

So "the gain is in the zero-percent band" is a modeled federal statement, not a promise that the transaction costs nothing.

The upside is simplicity and no liquidation or lender risk.

When you sell, you are giving up the Bitcoin, paying any tax on the gain, and giving up whatever future growth those units would have had.

### Path two: borrow

Borrowed cash is generally not income when there is a real obligation to repay.

That does not make the entire strategy tax-free.

Interest accrues. The loan can be liquidated. A lender sale of collateral is a taxable disposition. Debt cancellation can create income. The lender and custody structure add risks that have nothing to do with the tax code.

The tax comparison therefore cannot stop at "loan proceeds are not taxable."

It has to include:

- interest and fees;
- the LTV path under a major drawdown;
- any collateral top-up reserve;
- the tax from a forced or planned collateral sale;
- counterparty and rehypothecation terms;
- repayment source;
- the estate's obligation if the loan remains at death.

Borrowing can be useful when it is small relative to collateral, the repayment source is clear, and the household values keeping the position.

It is fragile when repeated borrowing becomes the paycheck and every new year consumes more collateral capacity.

### Path three: hold and spend from reserve or bridge

The third path is to leave the Bitcoin untouched and fund the year from cash or another Bridge asset.

That preserves the Bitcoin position and avoids a new loan.

The cost is using liquidity that may have another job. The reserve has to remain large enough to protect the plan through a drawdown, and the Bridge has to be replenished under the rule the household already set.

Under current federal law, taxable property inherited at death generally receives a basis tied to date-of-death fair market value.

That general rule has conditions and exceptions. Gifts, certain trusts, property outside the taxable estate, consistent-basis reporting, and future law can produce a different answer.

So an outright taxable Bitcoin holding may receive a basis adjustment under current law. Do not turn that into "all embedded gain disappears" for every ownership structure.

### Do not compare a tax rate with an interest rate directly

A common shortcut compares a 15% capital-gain rate with a 10% loan rate and picks the smaller number.

That is the wrong comparison.

The tax applies to the gain portion once. Interest applies to the loan balance over time, may compound, and may or may not be deductible. A forced sale can add tax later. The Bitcoin sold in path one and the Bitcoin pledged in path two also experience different future paths.

Use dollars over the same time horizon.

### The five-year view

Run each path for one year, then extend it for five.

For selling, track the units sold, basis, tax, and remaining Bitcoin.

For borrowing, track the loan balance, interest, collateral value, LTV, top-ups, repayment, and the outcome under a major drawdown.

For holding, track Reserve and Bridge depletion, refill years, and whether a bad market would force a later sale.

Most households will not choose one path forever. A strong plan can sell in one year, hold in another, and use a small loan for a specific purpose without turning borrowing into the foundation of the retirement paycheck.

### The family test

Before a loan enters the plan, the spouse or person who would inherit the balance should be able to explain:

- who holds the collateral;
- the margin and liquidation lines;
- where repayment comes from;
- what happens after a 50% or 75% decline;
- what happens if the lender fails;
- what the estate has to do if the borrower dies.

If the household cannot explain it, the complexity cost is not priced yet.

### Put it in orange plan

Plan → Income → Retirement Borrowing compares the borrowing strategy against the saved withdrawal plan.

Read after-tax net worth, loan balance, Bitcoin remaining, taxes, and risk together.

A preview is not the plan until it is deliberately applied.

### Homework

1. Price one year under sell, borrow, and hold.
2. Extend the comparison to five years.
3. Add state tax, ACA or Medicare effects, lender terms, and any basis-at-death assumption.
4. Stress the loan under the lender's actual thresholds.
5. Take the tax outputs to the tax professional and the loan terms to someone who represents the household, not the lender.

You are done when the decision is supported by dollars over the same horizon and the household can explain the risk without using the phrase "Bitcoin will probably go up."


# Advanced Module 7 — Advanced Custody

## A7.2 What self-custody actually asks of you

*`TEACH` · ~470 words · ~3 min*

> **Gate.** Optional throughout. Watch it if you are weighing whether you want
> the whole job of self-custody, or if the weight of it is what has been
> stopping you. Your custody plan is complete without it.

**By the end of this lesson, you can:**

- Name the responsibility self-custody transfers to you
- Decide whether you want the whole job, part of it, or none of it
- Match that honest answer to the custody level you can actually maintain

---

A client put this better than I ever have.

He said that with self-custody, you are the point of failure. And you are not only the failure point. You are also the attack vector.

Then he made the point that most of life does not work this way. We outsource violence to the police. We outsource security to banks and other institutions. A big part of civilization is handing the hard and dangerous jobs to people whose job it is to carry them.

Bitcoin gives you the ability to take one of those jobs back.

That is why custody can feel heavier than the rest of a financial plan. It is not another investment checkbox. You are accepting a responsibility that somebody else carries for nearly every other asset you own.

### What the whole job includes

The whole job is not just owning a hardware wallet.

It includes protecting the recovery material, keeping the process usable, testing that recovery works, maintaining the devices and software, noticing new single points of failure, and making sure somebody besides you can follow the process when your family needs it.

The device is one part. The ongoing responsibility is the job.

### Three honest answers

The first honest answer is that you want the whole job. That can be the right choice when the amount, your skill, and your willingness to maintain it all line up.

The second answer is that you want part of it. That is what collaborative custody is for, and it is why a hardened institution can legitimately hold part of a stack. You keep some control and hand off some responsibility.

The third answer is that you do not want the job right now. That is also a real answer. Taking responsibility you will not maintain is not more sovereign. It is just a new way to lose access.

If you do take the job, being a little paranoid is appropriate. You should feel the weight. The goal is not fear. The goal is to build a process strong enough that you do not need to think about it every day.

### Your decision

Whether you want the whole job, part of it, or none of it right now.

### Homework

1. Write which parts of custody you are willing to own and which parts you want help carrying.
2. Name the one recovery or maintenance task you would need to prove before moving more Bitcoin into self-custody.
3. Match the answer to the custody level from the core module. Do not choose a more complicated setup than your household can operate.

You are done when the custody setup matches the responsibility you are actually willing to maintain, not the identity you want it to signal.

## A7.3 Concentration: one institution, one vendor, one firmware
*`TEACH` · ~486 words · ~3 min*

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

In today's lesson, we're going to find concentration that remains after choosing a custody level.

Custody type and concentration are different questions.

A household can use a strong institution and still have every custodial asset behind one login. It can self-custody and still have every satoshi behind one device model, one firmware family, one wallet implementation, and one recovery process.

### Institution concentration

The 2022 failures showed what happens when customers become unsecured creditors, lose access, or wait through a bankruptcy process.

The lesson is not that every institution fails or that splitting money makes it self-custody.

The lesson is that one institution should not be able to freeze every asset the family needs next month.

I would look at a second independent institution when:

- the custodial amount is large enough that months without access would change the plan;
- the account is part of the emergency or spending bridge;
- one provider holds every taxable, retirement, or lending relationship;
- the second institution genuinely fails in a different way.

Two accounts using the same email, phone, identity provider, bank, or underlying custodian may not be as independent as they look.

### The cost of another account

Every extra account adds another password, authenticator, recovery process, tax record, beneficiary form, and executor row.

Three weak accounts can be worse than one hardened account.

Add an institution only when the reduced concentration is worth the maintenance and the family map is updated immediately.

### Vendor concentration in self-custody

Self-custody removes the chosen custodian's control. It does not remove every dependency.

A hardware wallet still depends on device hardware, firmware, backup standards, wallet software, supply chain, and the user's recovery process.

Using a second vendor or implementation can reduce a correlated vendor or firmware failure.

It does not guarantee safety. A second setup that nobody understands adds human and recovery risk.

### Different failure domains

Diversification only helps when the second path is actually independent.

Examples:

- a hardware wallet from another manufacturer with a compatible but independently implemented recovery path;
- multisig keys from different device vendors;
- part self-custody and part institution;
- separate email, authentication, and recovery paths for custodial accounts.

The goal is not to collect devices. It is to prevent one flaw, provider, credential, household event, or process error from reaching everything.

### Your decision

Whether the current amount justifies a second institution or independent signing path—and whether the household can maintain it well.

### Homework

1. Draw every custodial and self-custody dependency.
2. Circle any one provider, credential, vendor, firmware family, or location that reaches the entire stack.
3. Decide whether to reduce that concentration or accept it deliberately.
4. Add every new account or setup to the family map the same day.

You are done when the remaining concentration is visible, deliberate, and small enough that one failure does not destroy the household plan.


## A7.4 Wallet operations: UTXOs, dust, consolidation, and addresses
*`TEACH` · ~648 words · ~4 min*

> **Gate.** Watch this before you have made a hundred small transfers, not
> after. It applies if you buy Bitcoin regularly in small amounts, or if your
> wallet already shows a long list of separate chunks under coin control.

**By the end of this lesson, you can:**

- Explain why your balance is a stack of bills rather than a bucket
- Set a transfer threshold against Austin's 0.01–0.02 BTC rule of thumb, and know the fee test the number is protecting
- Decide whether you have a consolidation chore waiting
- Use a fresh receiving address every time, and say why it matters

---

In today's lesson, we're going to cover the wallet operations that matter after the hardware and recovery process are working.

### Your balance is a set of outputs

Bitcoin does not maintain one account balance inside the protocol.

A wallet tracks unspent transaction outputs, or UTXOs. Each incoming transaction can create one or more outputs the wallet may later spend as inputs.

When you spend, the wallet selects enough inputs to fund the payment and usually creates change back to a new wallet-controlled output.

### Why small outputs matter

Fees depend partly on how much transaction data has to be included.

Spending many small inputs can require more data than spending one larger input.

That does not mean every small UTXO is protocol dust.

Dust has a technical policy meaning tied to the cost of spending an output. Separately, an output can be economically unattractive to spend at a high fee rate even when it is not protocol dust.

The planning question is whether the fee to spend the output later would be material relative to the output.

### Austin's transfer rule

Austin's rule of thumb is to accumulate small exchange purchases and transfer around 0.01 to 0.02 Bitcoin at a time rather than moving every small buy immediately.

That is not a Bitcoin rule and it is not a permanent threshold.

Before using it, check:

- the current fee environment;
- the amount exposed to the exchange while waiting;
- withdrawal fees and minimums;
- whether the future spend fee would still be a rounding error;
- the household's counterparty-risk limit.

If the exchange balance becomes larger than the household is willing to expose, move it even when the threshold has not been reached.

### Consolidation

Consolidation spends several UTXOs to a new output controlled by the same wallet.

It can reduce the number of inputs a later transaction needs, especially when performed during a low-fee period.

It also has costs.

Combining outputs can link activity that was previously less obviously related, reducing privacy. It creates an on-chain transaction and fee now. It can also produce a larger output that becomes a more obvious target for future coin selection.

So consolidation is not automatic cleanup. It is a fee-versus-privacy decision.

Do not consolidate in an emergency, during a high-fee spike, or merely because the wallet shows many rows.

### Address use

Use a fresh receive address when the wallet provides one.

Address reuse can make payments easier to link and can expose more of the wallet's activity to counterparties or observers.

The wallet should verify the receive address on the trusted hardware display before a meaningful transfer.

A descriptor or extended public key can reveal many addresses and wallet history. It cannot sign by itself, but it is privacy-sensitive and belongs in the recovery plan rather than in public notes.

### Labels and coin control

Labeling acquisition source and purpose can help with tax records, privacy decisions, and future coin selection.

Coin control is an advanced tool. Selecting the wrong output can break the intended tax identification, combine private clusters, or create inefficient change.

Use it only when you understand the wallet's behavior and the tax record is made no later than the transaction.

### Your decision

The transfer threshold, whether consolidation is currently justified, and which privacy trade-off you accept.

### Homework

1. Open coin control or the wallet's UTXO view without changing anything.
2. Identify very small outputs, labels, and repeated addresses.
3. Estimate the fee to spend them at a normal and high fee rate.
4. Decide whether to leave them, consolidate during a low-fee period, or change the future transfer threshold.
5. Update the annual custody review with the decision.

You are done when the threshold is tied to current fees and counterparty exposure, and consolidation is treated as a privacy decision rather than housekeeping.


## A7.1 Advanced custody: passphrase, multisig, and collaborative
*`TEACH` · ~1,127 words · ~7 min*

> **Gate.** Watch this if your custody setup fails one of the two access tests from the estate module: one person can spend alone, or one lost copy could permanently stop recovery. If your Level 2 design passes test two and you have accepted failing test one deliberately, your custody plan is complete.

**By the end of this lesson, you can:**

- Tell passphrase, collaborative multisig, and DIY multisig apart by what each one buys and costs
- Build a passphrase strong enough to protect a stack (the 7-random-word standard)
- Vet a collaborative-custody provider with four questions
- Back up the multisig config file the way you back up a key

---

In today's lesson, we're going to compare three ways to add separation beyond a single-signature wallet: a passphrase, independent multisig, and collaborative multisig.

The goal is not maximum complexity. It is removing a specific failure without creating a recovery process your family cannot operate.

### Start with the two tests

Test one: can one person or one stolen item authorize a spend?

Test two: can one lost item or one unavailable person permanently block recovery?

A passphrase and multisig answer those tests in different ways.

### A bip39 passphrase

A BIP39 passphrase is an optional string used with a compatible mnemonic backup to derive a different wallet.

It is not simply an extra recovery word appended to the list.

Every possible passphrase derives a valid wallet. A typo does not produce an error. It produces a different wallet, often one with a zero balance.

That means the exact passphrase is part of the recovery material for the intended wallet.

The mnemonic without the passphrase can still derive the standard wallet. Whether that standard wallet is empty, a decoy, or used for a small balance is a deliberate design choice—not something the protocol does automatically.

### What the passphrase buys

If the mnemonic and passphrase are stored separately, finding one does not reveal the intended passphrase wallet.

Operationally, the household can place the two elements with different people or locations.

But this is not cryptographic multisig. There are not two independent signers and there is no threshold policy enforced on-chain.

Anyone who obtains both elements can derive the wallet. Losing either can make the intended wallet unrecoverable.

### Austin's passphrase rule

Austin's course rule is a long randomly generated passphrase, often seven random words, written and backed up offline.

That is an operational recommendation, not a BIP39 minimum and not a universal password rule.

Whatever method you choose, the passphrase must be generated without a human pattern, recorded exactly, kept separate from the mnemonic, backed up on its own side, and tested on the intended wallet.

Do not enter it into a password manager, AI, generic cloud note, or everyday computer merely because it is called a passphrase.

### Independent multisig

In a 2-of-3 multisig wallet, any two signing keys can authorize a spend and one key cannot.

That threshold can pass both tests: no single key spends, and one key can be lost.

The signing keys are only part of the recovery package.

The household also needs the wallet policy or descriptor and enough script, derivation, and key-origin information for compatible software to reconstruct the wallet.

A descriptor can reveal wallet structure, public keys, and addresses. Protect it for privacy and back it up for availability.

It cannot sign by itself.

One signing key stored with the descriptor is still one signing key in a 2-of-3 wallet. The old course incorrectly said that combination quietly created single-key control. It does not.

### Where the policy lives

The policy or descriptor can be copied more freely than a signing secret because it cannot spend, but do not publish it.

Keep redundant copies in places the recovery team can reach. Avoid storing the only policy copy inside one hardware wallet or only with one provider.

The goal is that any intended two-key recovery team can reconstruct the wallet without guessing derivation paths or depending on one company.

### Key distribution

A common 2-of-3 design places keys in separate failure domains.

For example:

- one key with the owner;
- one key in a separate secure location or with a trusted participant;
- one key with a collaborative provider or another independent location.

The exact people and locations are estate and threat-model decisions.

Do not put two keys, or their sufficient backups, in the same safe, household, office, or provider if the purpose is to survive that failure.

### Collaborative multisig

Collaborative custody uses a provider for setup, policy coordination, recovery assistance, transaction review, or one signing key.

Do not assume the label guarantees provider independence.

Verify:

1. What is the actual threshold?
2. Which signing keys does the client control?
3. Can the client meet the threshold without the provider?
4. Has the client exported the wallet policy or descriptor?
5. Which compatible software can reconstruct and spend without the provider?
6. What happens if the provider disappears, is enjoined, or changes terms?
7. Can the provider delay or veto a transaction under the contract or software workflow even when it cannot sign alone?

A provider cannot move a true 2-of-3 wallet with only one key. But the practical recovery claim is only proven after the client restores the policy and signs with the client-controlled threshold outside the provider's normal interface.

### Passphrase versus multisig

Choose a passphrase when the household wants a smaller increase in hardware and software complexity and can protect two exact recovery elements.

Choose multisig when on-chain threshold signing, loss tolerance, and distributed control justify the operational work.

Choose collaborative multisig when the household values assistance and has verified that provider independence is real rather than promised.

### Testing

For a passphrase wallet:

- recover on a spare compatible setup;
- enter the exact passphrase;
- verify the intended wallet fingerprint or address;
- confirm the standard no-passphrase wallet is understood;
- test the family process without revealing both elements to one unintended person.

For multisig:

- export and restore the policy or descriptor;
- verify the intended receive address on each signing device;
- create a small test transaction;
- sign with each intended two-key combination, or at least every combination the recovery plan depends on;
- prove one key cannot complete the transaction;
- for collaborative custody, complete a provider-independent recovery test.

### The family and estate layer

The access map names roles and process, not secrets.

The legal plan names who has authority. The key plan names who can technically sign. Those two systems must agree, but one does not replace the other.

A trustee, executor, heir, or provider holding one key does not automatically have legal control or unilateral technical control. The governing documents and full signing policy decide the result together.

### Your decision

Which failure you are removing and why the added complexity is worth maintaining.

### Homework

1. Write the two access-test answers for the proposed setup.
2. Inventory every required recovery element, including the policy or descriptor.
3. Run the exact spare-device or provider-independent recovery test.
4. Update the no-secrets custody map and legal plan so roles match the signing policy.

You are done when the setup survives the failure it was built for and the family can recover it without the vendor, without guessing, and without one unintended person holding enough to spend.


# Advanced Module 8 — Advanced Estate Planning

## A8.1 Advanced: do you need a trust, and which one?
*`TEACH` · ~1,202 words · ~8 min*

> **Gate.** Watch this once the **core estate gate in 8.5** has lit up and put you
> at Level 3 or 4 — a trust or coordinated plan. This lesson does not re-run that
> gate; it explains the options after it fires. Most households run the gate in
> 8.5, get a no, and are finished.

> 🎙 **SCRIPT PREPARED.** Dictation may be recorded; do not publish until the estate-attorney review is signed off in `LEGAL-REVIEW-PACKET.md`.

**By the end of this lesson, you can:**

- Say what the core gate's Level 3/4 answer actually commits you to
- Match trust type to purpose, and know which one does *not* lower an estate tax bill
- Ask the one attorney question that keeps a trustee from being obliged to sell your Bitcoin

---

In today's lesson, we're going to decide whether the estate plan has a problem that deserves a trust conversation.

We are not going to diagnose a trust from net worth, Bitcoin conviction, or one checkbox.

A trust is a fiduciary relationship governed by a legal instrument. The trustee holds or administers property for beneficiaries under those terms.

Calling it a container can be useful shorthand, but ownership, control, tax treatment, creditor rights, and fiduciary duties depend on the actual document and state law.

### The gate is a conversation trigger

The core module names complexity triggers:

- minor or vulnerable beneficiaries;
- blended family or conflicting beneficiary groups;
- business ownership;
- property in more than one state;
- privacy or probate concerns;
- incapacity planning;
- a custody setup another person must operate;
- a potentially taxable estate;
- a concentrated asset a fiduciary may be asked to retain.

One trigger does not mechanically mean a trust is required.

It means the attorney conversation has a real question to solve.

### Revocable living trust

A revocable living trust can support incapacity management and can avoid probate for assets properly titled or assigned to it.

Signing a trust does not move every asset into it. An unfunded trust does not avoid probate for property that still passes through the probate estate.

A revocable trust generally remains within the grantor's control and estate. It usually does not create federal estate-tax savings merely because the title includes the word trust.

Privacy can improve because a trust instrument is not automatically filed like a probated will, but administration, litigation, beneficiary rights, and state law can still expose information.

### Irrevocable trust

An irrevocable trust can change ownership, control, estate inclusion, income taxation, creditor exposure, and basis.

None of those results happens automatically.

The effect depends on:

- whether the transfer was completed;
- which powers the grantor retained;
- who can benefit;
- whether the trust is a grantor trust for income tax;
- withdrawal or substitution powers;
- creditor-access rules;
- the governing state;
- gift and generation-skipping consequences;
- whether the property remains in the taxable estate for basis purposes.

Do not use "irrevocable" as a synonym for "outside the estate" or "protected from creditors."

### Taxable estate versus succession problem

The first attorney question is what problem the household has.

A succession problem can exist at modest wealth: minor children, a special-needs beneficiary, a blended family, a business, or a complicated custody process.

An estate-tax problem depends on current federal and state law, ownership, deductions, prior gifts, and future values.

A fast-growing asset can make future estate exposure worth modeling. It does not by itself tell you to give up control today.

Model at least two defensible growth cases, then ask the attorney and CPA which ownership structures preserve the plan's tax and basis goals.

### Bitcoin ownership and the key plan

The legal owner and the signing policy have to match.

If a trust owns Bitcoin but the trustee has no practical way to carry out authorized transactions, the document and custody plan are misaligned.

If one trustee holds enough signing material to act alone, the household may have recreated the single-person risk the custody module tried to remove.

Multisig can distribute technical signing power, but one key does not automatically define legal control.

The trust instrument should state the trustee's authority and duties. The wallet policy should state the technical threshold. The recovery map should show how the authorized team can act. Those three layers must agree.

### The prudent-investor issue

Most states follow some form of prudent-investor law.

The general framework evaluates the portfolio as a whole and ordinarily favors diversification unless the governing instrument, purposes, circumstances, or state law support another approach.

A trustee asked to hold a concentrated Bitcoin position needs explicit, state-specific planning.

There is not one universal sentence called "the Bitcoin waiver" that solves every state and every trust.

The attorney should consider the tools available in that jurisdiction, which may include:

- express authority to retain or concentrate in a named asset;
- modification of the diversification duty;
- a directed-trust structure;
- a special trustee, trust protector, or investment adviser;
- trustee selection based on willingness and competence;
- consent, release, accounting, or exculpation procedures allowed by law;
- a process for liquidity, taxes, distributions, and rebalancing.

The correct question is:

"How will this trust authorize and protect a fiduciary who is expected to retain concentrated Bitcoin, and what limits still cannot be waived under this state's law?"

### The basis trade-off

Inherited property generally receives a date-of-death basis under current federal law.

Property transferred during life, property excluded from the estate, and property in different trust structures can have different basis consequences.

A strategy that reduces estate tax can create more capital-gain exposure, and the reverse can also be true.

That is why the estate attorney and CPA model the ownership and basis result together.

### The couple's result

The couple has minor children and concentrated Bitcoin, so the conversation is real.

The course cannot conclude from those facts alone that a revocable trust, irrevocable trust, or attorney-supervised will is definitely the right answer.

The output is a scoped attorney question:

- how should assets be held for the children;
- who has authority during incapacity and after death;
- which assets avoid probate already;
- whether a funded revocable trust improves administration;
- whether future estate exposure justifies advanced planning;
- how the custody threshold and fiduciary roles should align.

"Trust not currently indicated" can still be a finished answer after that review.

### What to remove from the decision

Do not choose a trust because:

- someone said every homeowner needs one;
- Bitcoin might go up;
- a trust sounds more private;
- an online form says the estate is complex;
- one generic irrevocable-trust benefit sounds attractive;
- a provider wants the structure to fit its custody product.

Choose only after the legal, tax, custody, and family jobs are named.

### Read it in orange plan

Protect → Projected legacy shows a planning estimate under the saved baseline.

Use it to identify whether the estate may cross a current federal or state planning line under assumptions you would defend.

The app does not establish legal domicile, determine a filing-status-specific exemption, draft a trust, transfer title, or prove that a fiduciary duty has been modified.

Change an assumption only as a scenario or temporary read, then return it to the saved baseline.

### Homework

1. Run the core complexity triggers and write the actual problem, not a trust type.
2. Read the projected after-tax estate under at least two defensible growth paths.
3. Inventory which assets pass by beneficiary form, joint ownership, will, or current trust.
4. Take the digital-asset, basis, fiduciary-retention, and custody-policy questions to a state-licensed estate attorney and the tax questions to the CPA.
5. Record the dated result, including "no trust currently indicated."

You are done when the household knows the problem the trust would solve, the ownership and key plan agree, and no one has treated a generic trust label as the answer.
