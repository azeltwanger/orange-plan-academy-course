# WALKTHROUGH 6.5 — model it in Orange Plan (tax, screen share)

**One session, 8 steps (~14 min capture)**

**Before recording:**
□ Last year's return handy · a wallet/exchange export ready
□ ⚠ Harvest room only shows for recorded purchase lots — run the import FIRST or harvest rows are empty
□ US mechanics note for non-US viewers (one line)

---

**Open:** "You have five tax levers: basis, buckets, conversions, harvesting, state. Now every one runs against your own numbers."

## □ 1 · Import transaction history
**Dashboard → Update Transactions → A downloaded file** (⚠ importer is on Dashboard, NOT the Tax page)
- 2 questions: which account? · all available history? (Yes / No, or I'm not sure)
- dedupe note: file is checked against earlier imports — overlaps don't duplicate
- "the app never invents basis — a flagged lot is your reconstruction homework"

## □ 2 · Land on the lots
**Strategy → Tax → Tax lots → View all lots**
- **coverage banner:** "Tax-lot records reconcile" = done · "Cost-basis history is incomplete" → read the counts (full / partial / missing)
- unresolved → **Import or reconcile history** → back to step 1 · "the missing-basis count is your homework list"
- columns: Asset · Purchased · Qty · Cost basis · Avg price · Value · Gain/loss · Term (LT/ST) · Account

**Fixing a wrong lot:** Dashboard → holding row → **Lots** → dialog "Purchase Lots — {asset}" (add/edit/delete)
- neighbors: **Add transaction** (single buy/sell/transfer) · **Transfer** (moves holding + basis, NOT a sale, no taxable event)
- ⚠ two guardrails, both protection not bugs:
  - sold lot is LOCKED ("Purchase lot locked by a sale") — unwind in order: delete sale → fix lot → re-enter
  - "Remaining lot quantity exceeds this holding by X" = almost always a double import — delete the duplicate

## □ 3 · Ground the 3 buckets
**Plan → Retirement → click a year on the chart → drawer → Account mix**
- collapsed: "N% tax-free" + 3-segment bar → expand: Taxable / Tax-deferred / Tax-free
- "if it's 100% one bucket, this walkthrough is going to be short — a mix is what makes the levers work"

## □ 4 · Model a Roth conversion — ⚠ SLOW DOWN
**Strategy → Tax → Moves this year → Roth conversion** (right side: "None modeled" / "~$X lifetime")
- **Compare strategies** table computes on open: Strategy · After-tax NW @{age} · Saved · Cost
- **Selected strategy** tiles: Lifetime saved · NW impact · Window · Total tax cost
- **Customize schedule → Conversion schedule:** timeline (Amount converted / Tax cost) · per-year rows · hover for "Projected year-end traditional"
- **Tax funding picker:** pick **Plan cash flow (withdrawal order)** — "that's paying the tax from outside the Roth" (not Withheld from each conversion)
- **Apply schedule** → 👀 watch "Projected year-end traditional" shrink across the years — "the future RMD getting smaller before it can spike a bracket"

## □ 5 · Harvest room + Form 8949
**Moves this year → Harvest gains / Harvest losses** (eyebrow: **Modeled, not advice**)
- headroom read one section up: **Room this year → Long-term gains → "$X more at 0%"**
- lot-by-lot: lots table preset filters **Review filtered gains / losses**
- **Export 8949** (top right) → `Form8949_{year}.csv` — "the artifact you hand your CPA, not a screenshot"
- toast "No lots to review" = no eligible lots, or step 1 incomplete

## □ 6 · Run the state scenario
**Scenarios → What if... → See more scenarios → Move to no-tax state** (⚠ NOT in the first four cards — expand)
- description: "What if you moved from {your state} to a state with no income tax?"
- one click creates + selects → plan re-runs
- say once: "residency is a legal standard, not a change of address"

## □ 7 · AI review
**Strategy → Tax → Review Tax Strategy** (header, near Download Tax Summary)
- reads tax context + future projection + the conversion comparison
- asks: "Is there a tax event this year that Orange Plan does not yet include?" — answer honestly (big sale, inheritance, business exit)
- read one surfaced item, agree/disagree · run AFTER lots are clean, BEFORE committing a conversion/harvest
- ⚠ "reviews and explains. Does not decide."

## □ 7b · WHERE THE TAX MONEY COMES FROM — ⚠ the #1 confusion
**Say this slowly. Every client gets stuck here.**
- **The conversion tax is NOT paid out of the account you converted.** You do not "withdraw to pay it," and there is no penalty involved.
- It's an ordinary tax bill, due at tax time, paid like any other tax bill: **from cash, or by selling from your taxable account.**
- 👀 point at the two pots on screen: the retirement account (moving) · the taxable account / checking (paying)
- ⚠ **Pay it from OUTSIDE.** Convert $30,000, owe $3,600 — pay from taxable/checking and the full $30,000 compounds tax-free. Pay it from the conversion and only $26,400 lands.
- **Say the client line:** "so we'd be selling from the taxable Bitcoin, not from the account we just converted" — that's the sentence that makes it click

**Then the cash-flow question they'll actually ask: "how do I come up with that money?"**
- Save cash between now and the filing deadline
- Sell some taxable Bitcoin
- Split the conversion across 2 years so each bill is smaller
- ⚠ **Size the conversion to a bill you can actually pay.** Deciding to convert and then discovering the bill is how good moves turn into stress.
- ⚠ Filing deadlines and extension rules are law-set. Point at them, don't quote them, and say: **"confirm the dates and any interest with your CPA before you rely on them."**

**And the Bitcoiner's version of the question: save that money in dollars or in Bitcoin?**
- Dollars = the bill is certain, the money is certain
- Bitcoin = you might have more, you might have less, and the bill doesn't move
- Say it plainly: **a tax bill is a fixed obligation with a date on it. Module 2 said fixed obligations don't get funded by volatile assets.** Same rule here.

## □ 8 · Capture decisions (paper is fine)
1. this year's moves (harvests doing, conversion applying)
2. next low-income-year moves (the bridge window)
3. exact CPA questions with dollar amounts + dates, in order
- write on top: **"Am I leaving low brackets empty?"**

## □ WRAP — spot check
- banner reads reconcile, no missing-basis count · Account mix is a real mix
- conversion fills the bracket, doesn't spill · near-zero lifetime saved = window isn't there this year
- "Projected year-end traditional" visibly shrinks · harvest room read ("$X more at 0%") · 8949 file on disk · state swing framed against the life trade-off
- hand-off: "your CPA doesn't need the app — they need the 8949, the one-page conversion schedule, and your question list" → END
