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
