<artifact
  data-placement-id="outcomes-6a64f0b191c739d3da789cb0"
  data-artifact-id="6a6754643a9be21a8d113311"
  data-params='{"items":["Complete an annual review in the app in one sitting"]}'
></artifact>

# Walkthrough: run the annual review in Orange Plan

Companion walkthrough for Module 9. This is the ~8-minute lap that runs both rhythms on camera: **one timed monthly pass** (under five minutes, honestly), then **the six-area annual lap** (~40 seconds per screen). By the end, you have this year's report saved, a fresh encrypted backup, and 1–3 actions on the calendar.

Set aside about 20 minutes to run it slowly the first time. Have a couple of transactions ready to enter, at least one linked account with something flagged (so the AI beat has something to explain), and last year's report open in another tab if you have one. This year's read is the *after* picture and next year's *before.*

## Pre-flight

⚠ **The 18-month / $120,000 reserve target from Module 6 is not settable from the UI.** "Target months" offers None / 1 / 3 / 6 / 12 only; an 18 renders only if it's already saved in the data. Seed it in your plan file; don't click for it on camera.

⚠ **The AI beat in Step 3 only renders when the Accounts page has flagged review items.** Have at least one linked account with something in review before you start, or the button simply won't be there.

The viewer brings any transactions since the last entry. If a month has no transactions, it doesn't need this pass at all.

## Step 1: The monthly pass. Timed, live

**Start a visible timer → Cash Flow.**

Section **"This month"**. Surplus verdict:

- Surplus: **"You have $X/mo left to put to work."**
- Deficit: **"Spending runs $X/mo ahead of income."**

Flow rows: **"Income" · "Taxes" · "Living" · "Debt payments."**

Card **"Verify spending" → "Review" →** drawer **"Verify spending" → tab "By month."**

Section **"Routing · waterfall order"**. Leave it alone unless something real changed.

⚠ **Four inputs, only actual changes get entered.** The monthly pass isn't a re-planning session. If income, spending, and routing all held steady, the pass is 60 seconds and you're out.

⚠ **Deficit mode:** if the month ran negative, the routing block is replaced by *"This month has no surplus to allocate. Reserve settings stay editable and apply when surplus returns."* That's an honest read. Routing pauses, reserve settings stay editable, and the pass still happened.

## Step 2: Enter transactions (Dashboard, not Cash Flow)

**Dashboard → header button "Update Transactions" → dialog "Update transactions."**

⚠ **Transactions import is on Dashboard, not Cash Flow.** Hop over, do it, hop back. Budget the click in your timer.

Source step **"Start here"**, heading *"How would you like to update transactions?"* Four choices:

| Choice | Sub-copy |
|---|---|
| **A linked account** | *"Check supported purchases from a brokerage, retirement, or Bitcoin account you connected."* |
| **A downloaded file** | *"Upload a CSV or Excel file from the account or service."* |
| **Describe one transaction to AI** | *"Tell Orange Plan AI about one purchase or sale. Review every field before saving."* |
| **I'll enter them myself** | *"Add a purchase, sale, or transfer manually."* |

**File path** → account step *"Which account are these transactions for?"* → **a review step before anything saves.**

Footnote: *"Downloaded files are checked against earlier imports before saving."*

⚠ **Nothing imported enters the plan silently.** Everything waits in a review step until you approve it, which enforces the honest-transactions discipline from Lesson 2.

## Step 3: AI · "Explain review items"

**Account menu (hamburger, aria "Account menu") → "Accounts" → button "Explain review items."**

Page eyebrow **"Accounts"** → h1 **"Linked Accounts."** Sub-line: *"{n} institutions · {n} accounts · {n} needs review · last sync {date}."*

**It reads:** the active tab, what's visible on the page, your synced-spending coverage, and the count awaiting review.

**It asks:** *"Which synced item looks missing or wrong if these review counts do not match the page?"*

Click, then **stop talking** until the answer arrives. Read one flagged item back and say whether you agree.

**When to run it:** during the monthly pass, when something's flagged and the count doesn't match what you expect to see.

**What it isn't:** it explains the queue. It does not approve anything.

⚠ **The button only renders when there's something to explain.** With no linked accounts and no flagged items, the button doesn't appear.

## Step 4: The annual lap. One screen per module

Six screens, ~40 seconds each. You're reading these screens, not editing them. If a screen looks off, note it and keep moving. The fix belongs to a separate session.

### Spending & Reserve · Plan → Income

**"Retirement operating plan" → "What you can spend"** → **"Review annual update"** → panel **"Annual update ready"** → tiles:

- **Prior**
- **After inflation**
- **{80}% target**
- **Saved target**

→ **"Apply annual update."**

The reserve read is the **"Reserve buffer"** strip: **"{N} yrs · without selling investments."**

Refill the reserve by hand on the Lesson 3 rule:
- **Good year** → refill to $120,000 (the 18-month target).
- **Cut year** → stop at roughly 12 of 18 months (~$80,000).
- **Target months never moves.**

⛔ **Don't invent status words on camera.** Nothing on screen names a refill state. Strings like "Refilling," "Paused," "Critical," or "Portfolio declined…" don't exist in the app. Read the tiles and the strip as they are.

### Allocation · Strategy → Allocation

**"Funding your timeframes"** → **Reserve / Bridge / Legacy** with badges **"Funded" / "Behind."**

**"What it takes to get to target"** → *"All assets are inside the {N}% drift band."*

Re-ask the stress question at today's balance, not last year's. If today's number changes your answer, allocation is the lever to pull.

### Debt & LTV · Strategy → Debt

H1 **"Debt Strategy."**

Ratios: **"Debt-to-assets"** (*"caution above {N}%"*) and **"Debt-to-income"** (*"high-risk above {N}%"*). Tooltip: **"Ratio bands."**

BTC loan (if any): severity chips **"near margin call" / "margin call" / "liquidation zone"** and the sentence *"A {N}% drop triggers a margin call at {price} BTC · liquidation at {price}."*

⚠ **There is no "loan cushion" label on this page.** Use the severity chips and the drop-to-margin-call sentence. The word "cushion" appears in one place: the report's BTC-loan gauge in Module 10.

### Tax · Strategy → Tax

H1 **"Tax strategy."**

Card **"Moves this year"**. Eyebrow **"Modeled, not advice."** Rows:

- **Harvest gains**
- **Harvest losses**
- **Roth conversion**

⚠ **This one runs BEFORE year-end, while the calendar can still act.** Harvest and conversion moves close December 31. If you're running the annual lap in January, the tax card is a *plan next year* read, not a *do it now* action.

### Custody · Protect

**"Needs attention" → "Security checklist" → "{n} of {n} for your tier."**

Groups: **Hardware / Distribution / Legal / Access after death.**

One item to look at every year: **"Full recovery process tested end-to-end."** A checked box means you did the wipe-and-restore this year. An unchecked box is a candidate for one of your three actions.

### Estate · Protect

Five segments: **"Dead man's switch" / "Heir letter" / "Protection tier" / "Checklist" / "Beneficiaries"** → **"{n} of 5 essentials in place."**

The switch row (armed) reads **"warns at 90 days · {n} contacts"** + **"{n} days left,"** action **"Check in."**

The check-in itself is the annual proof of life. The switch only stays armed if you show up.

## Step 5: Close the year. Report + backup

**Account menu → "Report" → button "Download PDF."**

Save with the year in the filename. This is next year's *before* picture.

**Settings → "Data & Privacy" → "Data & backups" → "Backup & Restore" → "Export Plan."**

⚠ **"Export Plan" opens a plaintext browser passphrase prompt.** Type it off-camera, or use a visible throwaway you'll discard. Say on screen: *this is a backup passphrase, not a wallet passphrase.*

Toast: **"Plan exported."**

⚠ **The annual review isn't done until the after-picture is saved.** Report on disk, encrypted backup on disk, both dated with the year. Saving them is what turns the pass into an archived review rather than a glance.

## Step 6: Schedule both rhythms

There is **no native scheduler in Orange Plan.** Use your calendar app, on camera.

- **Monthly day** (e.g. the first Saturday). Recurring.
- **Annual month** (e.g. every January). Recurring.

Extra rhythm: the **90-day check-in email** from the dead man's switch is a built-in reminder. If the email arrives and you're alive, log in and check in.

Close on the discipline: the confidence status only flips to "Recheck needed" when plan inputs change. A moving price doesn't touch it, so the app won't panic on a red candle, and neither should you.

## What good looks like

- **The timer stops under five minutes on the monthly pass.** Say out loud that most months are quieter than this one.
- **Nothing got touched that shouldn't have.** Name what you never opened: assumptions, targets, the allocation itself. Price moved; the plan didn't.
- **Spending & Reserve**. Inside the guardrails, reserve at target or rebuilding toward it on the L3 rule. Bad: a reserve at half target two years running.
- **Allocation**. Near target, and the stress question still passes honestly at today's balance.
- **Debt**. Ratios in band, no loan a 50% drawdown would liquidate.
- **Tax**. This year's window used or deliberately passed, before year-end.
- **Custody**. One recovery proven, last year's top only-one fixed, no new ones.
- **Estate**. A letter the family could act on today; switch armed; forms match the will.
- **Output is 1 to 3 actions**, finishable before next month's pass. Longer lists are how reviews stop happening.

## What got built

| # | Item | Where it lives |
|---|---|---|
| 1 | Current transactions + a verified month | Dashboard → "Update Transactions"; Cash Flow → "Verify spending" |
| 2 | This year's annual update, applied | Plan → Income → "Review annual update" → "Apply annual update" |
| 3 | The reserve refilled by hand on the L3 rule | Cash Flow → "Reserve settings" → "Monthly build cap" |
| 4 | 1–3 actions | Recorded decision |
| 5 | The yearly report PDF + fresh encrypted backup | Account menu → Report → "Download PDF"; Settings → Data & backups → "Export Plan" |
| 6 | Both review dates on the calendar | Calendar app (no native scheduler) |

## Handing it off

Next lesson (the capstone) is the read of the report you just saved. The nine modules assembled into one document, walked in planner order: position, trajectory, risk, actions.
