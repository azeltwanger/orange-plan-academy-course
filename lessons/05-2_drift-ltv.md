<artifact
  data-placement-id="outcomes-6a64f09ef52d283414ef787a"
  data-artifact-id="6a6754643a9be21a8d113311"
  data-params='{"items":["Understand how DTA moves with the Bitcoin price","Calculate LTV and how far Bitcoin can drop before liquidation","Size a loan-to-value cushion that survives a normal Bitcoin drawdown"]}'
></artifact>

# Drift and the LTV cushion

Two dynamics that make a Bitcoin balance sheet different from everybody else's.

## Your DTA moves with Bitcoin

Your debt-to-assets ratio doesn't sit still. It moves with the Bitcoin price:

- **Bitcoin up.** DTA drops. Room opens up. You feel safe. You want to borrow more. Usually right near the top.
- **Bitcoin down.** DTA spikes at the exact moment your stress is peaking. If there's no room left, that's where forced selling happens.

The couple landed at 40% DTA with $298,000 debt against $745,000 assets:

- **Bitcoin doubles:** $175k becomes $350k, total assets $920k, DTA drops to **32%.** 8 points of room without doing anything.
- **Bitcoin halves:** $175k becomes $87.5k, total assets $658k, DTA climbs to **45%.** Same debts, same payments. Over the workable range.

The ratio tells you about today's price, but the decision you're making lives for years. Room looks real at the moment it's least real.

**Stay conservative when Bitcoin is high. Use your room when Bitcoin is low.** Anchor to where Bitcoin has been, not to what it's printing today. Use DTI as your floor, since it doesn't move with price.

Austin's own experience: his net worth dropped 75% in 2022. He could hold because nothing on his balance sheet could force him to sell.

## The LTV cushion

For any borrowing backed by your Bitcoin, there's a gap between where your loan starts and the line where the lender takes over. That gap is the entire drawdown you can live through.

**LTV** = loan-to-value = your loan divided by your collateral's current value.

- Your **loan balance** is fixed. It doesn't move when Bitcoin moves.
- Your **collateral value** moves with the price.

If Bitcoin falls, your collateral shrinks, LTV climbs, and it climbs toward the lender's liquidation line. Your starting LTV sets the entire survivable drop.

If you hit the line, the lender force-sells your Bitcoin. At the worst possible moment.

## The math

Say you post $50,000 of Bitcoin as collateral, and the lender's liquidation LTV is 80%.

**Scenario A: borrow $12,500 (25% starting LTV).**

- Liquidation collateral value = $12,500 ÷ 0.80 = **$15,625**.
- Bitcoin has to fall from $50,000 to $15,625 for a margin call. A **69% drop**. Right at the edge of Bitcoin's historical drawdowns (2018: -84%, 2022: -77%). Not enough cushion.

**Scenario B: borrow $6,250 (12.5% starting LTV).**

- Liquidation collateral value = $6,250 ÷ 0.80 = **$7,812**.
- Bitcoin has to fall from $50,000 to $7,812. An **84% drop**. Now you can survive a 2018-style bear.

Cut the starting LTV in half, and the danger line moves much further away.

## Size the cushion for a normal drawdown

If you're borrowing against Bitcoin, size the cushion to survive a **70 to 80% drawdown minimum**. That's the normal Bitcoin cycle, not a worst case.

Usually means starting at **20 to 25% LTV**, not 40 to 50%. Anything higher, and a normal Bitcoin bear becomes a forced-sale event at the worst possible moment.


So that's the math on the cushion. The app draws it, which is easier to read than the arithmetic.

## Now put it in the app

### Step 4: Debt capacity track

**Strategy → Debt → Debt capacity**.

Three zone bands render side by side: **safe, caution,** and **high-risk**.

A marker on the track reads: *"today N.N%."*

Threshold labels beneath: **$0** and **caution N%**.

⚠ Use this to see the drift rule visually. Be conservative when Bitcoin is high (DTA looks low, but that's your cushion). Use the room when Bitcoin is low (DTA looks high, but that's when the cushion is meant to be used). See the drift lesson for the math behind that.

### Step 6: Name the LTV cushion (Bitcoin-backed loans only)

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
