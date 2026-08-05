# 6.5 · WALKTHROUGH — Model it (tax)

**Screen capture · 9 steps · ~14 min**

> **DO** = click path · **SEE** = point at this · **⚠** = don't get this wrong
> Narrate in your own words. Nothing here is scripted.

---

## Before you record

- [ ] Last year's return handy · a wallet/exchange export ready
- [ ] **Run the import FIRST.** Harvest room only shows for recorded purchase lots — skip step 1 and the harvest rows are empty
- [ ] One line ready for non-US viewers: these are US mechanics
- [ ] Clean browser, notifications off

---

## □ 1 · Import transaction history

**DO** Dashboard → **Update Transactions** → **A downloaded file**

**⚠** The importer lives on the Dashboard, NOT the Tax page.

**SEE** Two questions: which account? · all available history? (Yes / No / I'm not sure)

**SEE** Dedupe note — the file is checked against earlier imports, overlaps don't duplicate

**⚠** The app never invents basis. A flagged lot is your reconstruction homework.

---

## □ 2 · Land on the lots

**DO** Strategy → Tax → Tax lots → **View all lots**

**SEE** Coverage banner: *"Tax-lot records reconcile"* = done · *"Cost-basis history is incomplete"* → read the counts (full / partial / missing)

**DO** Unresolved → **Import or reconcile history** → back to step 1

**⚠** The missing-basis count IS your homework list.

**SEE** Columns: Asset · Purchased · Qty · Cost basis · Avg price · Value · Gain/loss · Term (LT/ST) · Account

**DO** Fixing a wrong lot: Dashboard → holding row → **Lots** → dialog *"Purchase Lots — {asset}"* (add/edit/delete)

**SEE** Neighbors: **Add transaction** (single buy/sell/transfer) · **Transfer** (moves holding + basis, NOT a sale, no taxable event)

**⚠** Two guardrails, both protection, not bugs:
- A sold lot is LOCKED (*"Purchase lot locked by a sale"*). Unwind in order: delete the sale → fix the lot → re-enter.
- *"Remaining lot quantity exceeds this holding by X"* is almost always a double import. Delete the duplicate.

---

## □ 3 · Ground the three buckets

**DO** Plan → Retirement → click a year on the chart → drawer → **Account mix**

**SEE** Collapsed: *"N% tax-free"* + a 3-segment bar → expand: Taxable / Tax-deferred / Tax-free

**⚠** If it's 100% one bucket, this walkthrough is short. A mix is what makes the levers work at all.

---

## □ 4 · Model a Roth conversion — SLOW DOWN

**DO** Strategy → Tax → Moves this year → **Roth conversion**

**SEE** Right side: *"None modeled"* / *"~$X lifetime"*

**DO** **Compare strategies** — the table computes on open

**SEE** Strategy · After-tax NW @{age} · Saved · Cost

**SEE** Selected strategy tiles: Lifetime saved · NW impact · Window · Total tax cost

**DO** **Customize schedule** → Conversion schedule: timeline (Amount converted / Tax cost) · per-year rows · hover for *"Projected year-end traditional"*

**DO** Tax funding picker → **Plan cash flow (withdrawal order)**

**⚠** That's paying the tax from outside the Roth. NOT "Withheld from each conversion."

**DO** **Apply schedule** → watch *"Projected year-end traditional"* shrink across the years

**⚠** That shrinking line is the whole point: the future RMD getting smaller before it can spike a bracket.

---

## □ 5 · Where the conversion tax money comes from — THE #1 CONFUSION

**⚠ Say this slowly. Every client gets stuck here.**

**⚠** The conversion tax is **not** paid out of the account you converted. You do not "withdraw to pay it," and there's no penalty involved. It's an ordinary tax bill, due at tax time, paid like any other tax bill — from cash, or by selling from your taxable account.

**SEE** Point at the two pots on screen: the retirement account (moving) · the taxable account / checking (paying)

**⚠ Pay it from OUTSIDE.** Convert $30,000, owe $3,600. Pay from taxable or checking and the full $30,000 compounds tax-free. Pay it out of the conversion and only $26,400 lands.

**⚠ The line that makes it click:** "so we'd be selling from the taxable Bitcoin, not from the account we just converted."

**Then the question they actually ask — how do I come up with that money?**
- Save cash between now and the filing deadline
- Sell some taxable Bitcoin
- Split the conversion across two years so each bill is smaller

**⚠** Size the conversion to a bill you can actually pay. Decide to convert, then discover the bill, and a good move turns into stress.

**⚠** Filing deadlines and extension rules are law-set. Point at them, don't quote them, and say: confirm the dates and any interest with your CPA before you rely on them.

**The Bitcoiner's version — save that money in dollars or in Bitcoin?**

**⚠** Dollars means the bill is certain and the money is certain. Bitcoin means you might have more, you might have less, and the bill doesn't move. A tax bill is a fixed obligation with a date on it — and Module 2 already said fixed obligations don't get funded by volatile assets. Same rule here.

---

## □ 6 · Harvest room + Form 8949

**DO** Moves this year → **Harvest gains / Harvest losses**

**SEE** Eyebrow **Modeled, not advice**

**SEE** Headroom one section up: **Room this year → Long-term gains → "$X more at 0%"**

**DO** Lot-by-lot: lots table preset filters **Review filtered gains / losses**

**DO** **Export 8949** (top right) → `Form8949_{year}.csv`

**⚠** That file is the artifact you hand your CPA. Not a screenshot.

**⚠** Toast *"No lots to review"* = no eligible lots, or step 1 wasn't finished.

---

## □ 7 · Run the state scenario

**DO** Scenarios → What if... → **See more scenarios** → **Move to no-tax state**

**⚠** It's NOT in the first four cards. You have to expand.

**SEE** *"What if you moved from {your state} to a state with no income tax?"* · one click creates + selects it, plan re-runs

**⚠** Say it once: residency is a legal standard, not a change of address.

---

## □ 8 · AI review

**DO** Strategy → Tax → **Review Tax Strategy** (header, near Download Tax Summary)

**SEE** It reads tax context + future projection + the conversion comparison

**SEE** Asks: *"Is there a tax event this year that Orange Plan does not yet include?"*

**DO** Answer honestly — a big sale, an inheritance, a business exit

**DO** Read one thing it surfaced, agree or disagree

**⚠** Run it AFTER the lots are clean and BEFORE committing a conversion or harvest.

**⚠** It reviews and explains. It does not decide.

---

## □ 9 · Capture the decisions (paper is fine)

1. This year's moves — harvests you're doing, conversion you're applying
2. Next low-income-year moves — the bridge window
3. Exact CPA questions with dollar amounts and dates, in order

**⚠** Write on top of the page: **"Am I leaving low brackets empty?"**

---

## □ WRAP — spot check off the screen

- [ ] Banner reads reconcile, no missing-basis count
- [ ] Account mix is a real mix
- [ ] Conversion fills the bracket, doesn't spill
- [ ] Near-zero lifetime saved = the window isn't there this year (that's a finding, not a failure)
- [ ] "Projected year-end traditional" visibly shrinks
- [ ] Harvest room read out loud ("$X more at 0%")
- [ ] 8949 file on disk
- [ ] State swing framed against the life trade-off

**⚠** Hand-off: your CPA doesn't need the app. They need the 8949, the one-page conversion schedule, and your question list.

**END**
