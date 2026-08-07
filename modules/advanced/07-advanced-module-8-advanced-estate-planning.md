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
