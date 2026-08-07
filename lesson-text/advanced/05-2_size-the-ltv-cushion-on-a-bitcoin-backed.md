# Size the LTV cushion on a Bitcoin-backed loan

Two dynamics that make a Bitcoin balance sheet different.

## Your DTA moves with Bitcoin

Bitcoin up → DTA drops → you feel safe and want to borrow more (usually near the top). Bitcoin down → DTA spikes exactly when stress peaks, and if there's no room left, that's where forced selling happens.

The couple at 40% DTA: Bitcoin doubles → 32% (8 free points, no action taken). Bitcoin halves → 45% (same debts, now over the range).

**Rules:** stay conservative when Bitcoin is high, use room when it's low, anchor to the full cycle rather than today's print, and use DTI as your floor, because it doesn't move with price.

## The LTV cushion

For any Bitcoin-backed borrowing: **LTV = loan ÷ collateral value.** The loan is fixed; the collateral moves daily. The gap between your starting LTV and the lender's liquidation line is the entire drawdown you can live through.

$50,000 collateral, 80% liquidation line:

| Borrow | Starting LTV | Liquidation at | Survivable drop |
|---|---|---|---|
| $12,500 | 25% | $15,625 | 69%, at the edge of history (2018: −84%, 2022: −77%) |
| $6,250 | 12.5% | $7,812 | 84%, survives a 2018-style bear |

Halving the starting LTV moves the danger line dramatically further away.

**Size the cushion for a 70–80% drawdown minimum**: that's a normal cycle. In practice: start at 20–25% LTV, not 40–50%.

## Your decision

**Your maximum starting LTV, and what you'll do at each severity level.**

1. **Size the cushion to a normal bear market.** A 70–80% drawdown is the normal case for Bitcoin.
2. **Work backwards from that.** Surviving one usually means starting far lower than a lender will let you borrow.
3. **Decide your actions before the chip appears**, because by then the price is falling and you're deciding at your worst.
4. **Write all three responses now**: near margin call, at margin call, liquidation zone.

## Homework

1. Enter your lender's real thresholds on the loan in the app: starting LTV, top-up line, liquidation line.
2. Decide your action at each of the three severity levels before you're at one of them.
3. If you have a loan, open its detail view and read today's cushion against those lines.
