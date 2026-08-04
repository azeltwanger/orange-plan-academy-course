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
- two questions: which account? · all available history? (Yes / No, or I'm not sure)
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

## □ 3 · Ground the three buckets
**Plan → Retirement → click a year on the chart → drawer → Account mix**
- collapsed: "N% tax-free" + 3-segment bar → expand: Taxable / Tax-deferred / Tax-free
- "if it's 100% one bucket, this walkthrough is going to be short — a mix is what makes the levers work"

## □ 4 · Model a Roth conversion — ⚠ SLOW DOWN
**Strategy → Tax → Moves this year → Roth conversion** (right side: "None modeled" / "~$X lifetime")
- **Compare strategies** table computes on open: Strategy · After-tax NW @{age} · Saved · Cost
- **Selected strategy** tiles: Lifetime saved · NW impact · Window · Total tax cost
- **Customize schedule → Conversion schedule:** timeline (Amount converted / Tax cost) · per-year rows · hover for "Projected year-end traditional" + IRMAA when it applies
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
