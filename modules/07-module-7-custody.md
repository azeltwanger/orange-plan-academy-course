# Unit 8 · Module 7 — Custody

*Custody as operational protection: choose your level on the four-tier ladder, set up hardware with a proven recovery test, close single points of failure, and — when it fits — go advanced with passphrase, multisig, or collaborative custody.*

## 8.1 Choose the custody setup that matches your stack and family
*`TEACH` · 2,041 words · ~13 min*

**By the end of this lesson, you can:**

- Score your household against the five custody questions
- Name the job each pile of Bitcoin is doing
- Match a custody level to your stack, your skill, and your family
- Decide whether custodial Bitcoin should sit at more than one institution
- Name what your whole stack is trusting, and whether to spread that out

---

Custody is more than where your Bitcoin sits. It covers whether you can reach it, whether anyone else can, and whether there's a process that still works when you're not around.

It's different from inheritance. Inheritance is the legal transfer (wills, executor, who gets what). Module 8 covers that. This module secures access while you're alive and makes it recoverable if you're not.

In 2022, Celsius customers watched a balance sit on a screen while withdrawals were frozen. Same at BlockFi and FTX. The number was theirs. The Bitcoin was not. A Bitcoin balance in someone else's system is a claim on their Bitcoin, not ownership of yours.

### The five questions

Custody comes down to five:

- Where is the Bitcoin held?
- What type of custody are you using?
- Who knows what to do?
- What happens if you're unavailable?
- Where are the single points of failure?

A typical Bitcoin household: he's 45, she's 43, two kids ages 10 and 12. They hold 1.5 BTC on a hardware wallet in a desk drawer, and 0.25 BTC on an exchange.

- **Where:** they can answer cold. ✓
- **What type:** one hardware wallet, one exchange account, no passphrase. ✓
- **Who knows what to do:** he does. She's never touched the device. ✗
- **What happens if he's unavailable:** nothing. ✗
- **Single points of failure:** they've never asked. ✗

Two out of five. That's a normal Bitcoin household, not a careless one. The score turns a vague worry into three specific jobs.

### Name the job before you pick the setup

Different jobs can call for different custody.

For the couple, the 1.5 BTC is long-term cold storage. It's the retirement stack and shouldn't move in a hurry. The 0.25 BTC on the exchange is the buying account — but it's also quietly doing a second job nobody assigned: it's what they'd reach for in an emergency. Different job, different custody answer, because an exchange can freeze an account in exactly the week they need it.

Name the job, so one setup doesn't cover two jobs that need different things.

### The one rule this module runs on

**You document the process, never the secrets.**

By "secrets" I mean the things that actually move Bitcoin: seed phrase (the words your whole wallet rebuilds from), private keys, passphrase, PIN. Anyone with one of those has your Bitcoin.

> ⚠ No seed phrases, no private keys, no passphrases, no PINs. In any app, document, photo, cloud note, or AI tool. Ever.

What you write down: who holds what, what type of setup it is, and what someone should do. Never the words that unlock it. You can share the document with your executor and store it safely, because nothing in it is worth stealing.

### Choosing your level

A custody level is how much protection a setup gives you and what it asks back: skill, maintenance, and what your family has to be able to do. The right level matches how much is at stake and who depends on it.

The mistake is a mismatch, in either direction. Celsius customers had too little custody for the amount at stake. Others move a life-changing stack onto a hardware wallet they've never tested, which is more custody than their skill supports. Both cases: the setup doesn't match what's at stake.

### The four levels

**Level 1: Hardened exchange or broker.** Small stack, or still learning.

- Setup: strong password, app-based 2FA, secured email, withdrawal delays on.
- The word is hardened, not neglected. A small stack on a locked-down exchange is legitimate.

**Level 2: Hardware wallet.** The default destination once a stack becomes meaningful.

- Setup: seed stays offline, test transaction first, wipe-and-restore proven, and a backup medium matched to what's being protected.
- **Backup medium is a tradeoff, not a rule.** Paper is cheap and burns. Steel survives fire and flood and costs more. Weigh it against the size of the stack and the hazards where the household actually lives — do not hand students "steel is required."
- Removes freeze risk. Hands you maintenance instead.

**Level 3: The stack matters to more than just you.** The defining feature is that someone other than you has to be able to recover it, not any one technique.

- Setup: a hardened wallet, a documented process your spouse or executor can actually follow, backups that survive one loss, and an annual review.
- **Split access is one way to get here, not the requirement.** A passphrase split, a sealed executor packet, or a well-documented single-signature setup with redundant backups can all clear this bar. Split access buys dual control; it does not by itself buy redundancy, and it adds a failure mode of its own when the family is confused or a holder is unreachable.
- Pick the design your household can actually operate. Complexity nobody can execute is not a higher level.

**Level 4: Collaborative or DIY multisig.** For stacks where a single mistake is unacceptable.

- Setup: professional support (collaborative) or full-DIY, coordination with trust and estate plan, family process actually tested.
- Buys you a setup where one mistake no longer ends it.

### Every level is a trade

There is no custody setup without a trade-off. Each level buys one protection by handing you a different risk to manage:

| Level | What it buys | What it costs |
|---|---|---|
| 1 · Hardened exchange/ETF | Convenience, easy inheritance, no self-responsibility | Counterparty risk. The account can be frozen exactly when you need it |
| 2 · Hardware wallet | Removes freeze risk. True ownership | Maintenance and self-responsibility. One seed is one point of failure |
| 3 · Passphrase + split | Theft protection, survivable without you | More complexity. A lost passphrase is a permanent loss |
| 4 · Multisig | No single mistake can end it | Highest complexity. Config-file dependence, a fee (collaborative) or heirs' complexity (DIY) |

The pattern: more sovereignty always means more responsibility, and more convenience always means more counterparty risk. You never eliminate risk, you choose which risks you hold and which you hand to someone else. That's why the level is matched to stakes and skill instead of picked on ideology.

### One more question, if it applies to you

Everything above is about *what type* of custody you use. A separate question asks how **concentrated** it is, and it only matters for some people, so name it rather than teach it.

> **Advanced Library → A7.3 "Concentration: one institution, one vendor, one
> firmware"** if either is true: the custodial balance is big enough that
> losing access for a few months would change your life, or every satoshi you
> own sits behind one model of one device running one manufacturer's firmware.
> If neither is true, the custody plan is complete without it.

### Sizing it on a real household

The couple holds 1.5 BTC on a hardware wallet and 0.25 BTC on an exchange. At an illustrative $100,000/coin, the hardware wallet is $150,000 and the exchange is $25,000.

The $25,000 is Level 1 money on a Level 1 setup. Honest match, as long as it's hardened.

The $150,000 is Level 3 money. His wife and two kids depend on it. Neither kid is a teenager yet.

Compare against where it's sitting: Level 2, and Level 2 isn't finished (no proven wipe-and-restore, seed still on paper).

Homework: finish Level 2 honestly, then add whatever makes it recoverable without him — that is what moves it to Level 3. Two jobs, in that order, and the second one has more than one right answer.

### The app's tier

Orange Plan runs three tiers keyed to estate size:

| Tier | Net worth |
|---|---|
| **Foundation** | Under $500k |
| **Substantial** | $500k to $2M |
| **High Net Worth** | Above $2M |

The tier filters the security checklist so a Foundation household isn't held to the hardware items a high-net-worth household is.

**Two separate scales, with two separate inputs. Do not let one answer the other.**

| | **Custody level** (1–4) | **App tier** (Foundation / Substantial / HNW) |
|---|---|---|
| Driven by | What the Bitcoin is for · how much is actually at risk · your technical ability · whether your family could recover it · estate complexity · liquidity needs | Estate net worth, and nothing else |
| Decides | How you hold and hand off the coins | Which checklist items the app shows you |
| Who sets it | You | The app |

These do not move together, and the gap is where people get hurt. **A household with $400,000 of net worth and $350,000 of it in direct self-custodied Bitcoin lands in Foundation and never sees the hardware items.** They need a proven recovery process anyway. The Bitcoin does not care what tier the estate is in.

⚠ **The tier-filtered checklist is a convenience, not a custody recommendation.** If your Bitcoin position is heavier than your estate tier implies, hold yourself to the standard the app isn't asking for.

### Custody is not a purity test

The right setup is one you can maintain, explain, and recover from. If your family can't actually use it, the advanced version isn't protecting anything.

You'll hear people say real Bitcoiners self-custody everything, immediately. That claim is wrong. You move up a level by earning it, with skill and with need, not with ideology.

### Your decision

Two decisions. Your honest score with the job each pile is doing. And which level you're going to run, including whether your custodial Bitcoin should sit at more than one institution.

Match the level to what's at stake and what you can genuinely maintain, and remember a mismatch in either direction is the failure. Too little custody for the amount is the Celsius problem. Too much custody for your skill is the lost-seed problem.

### Put it in Orange Plan

Nothing in the app yet. This decision goes on your Family Custody Map, which the module walkthrough fills in.

### You are done when

You have an honest score on the five questions, a named job for each pile of Bitcoin, and the level you're going to run. A note is on your annual review to re-ask all of it at that year's balance, because the price moves and your setup doesn't.


## 8.2 Set up a hardware wallet and test recovery
*`TEACH` · ~1,149 words · ~7 min*

**By the end of this lesson, you can:**

- Set up a hardware wallet safely from scratch
- Never leak the seed phrase, ever
- Perform a wipe-and-restore recovery test
- Know the one transfer rule that matters before you start sending coin

---

In today's lesson, we're going to cover the hardware wallet setup, and the recovery test that proves your backup actually works before serious money depends on it.

Because a seed backup is only as good as your ability to actually restore from it. And most people have never tested that.

### Where your bitcoin actually lives

First: your Bitcoin isn't on the device.

When you set up a hardware wallet, it generates a seed phrase, 12 or 24 words, and every key to your Bitcoin is derived from those words. The device is just a safe place to use them. The device is replaceable. The seed is not.

So if the device breaks, you rebuild the wallet on a new device from the seed, and nothing is lost. But if the seed is wrong, a broken device is the end of the stack.

And there's a detail that makes this sharper: most hardware wallets wipe themselves after a set number of wrong PIN entries. That's the right feature, because it stops a thief from guessing their way in. But it also means your entire stack effectively lives on the paper backup. The device can erase itself on a Tuesday afternoon, and that piece of paper becomes the only copy in existence.

### The six-step setup

The setup is 6 steps, and the order matters.

Step one: buy the device directly from the manufacturer. Never used, never from a third-party seller. A device someone else touched can arrive with a seed they already know, and then every coin you send it is already theirs.

Step two: generate a brand-new wallet on the device itself. The seed gets created by the device, and it has never existed anywhere else in the world.

Step three: write the seed down offline, and set a PIN.

Step four: send a small test transaction to the wallet. Something like 0.01 Bitcoin, around $1,000. Small enough that losing it is survivable, big enough that you take it seriously.

Step five, and this is where most people stop short: wipe the device. Factory reset it, on purpose, with that $1,000 sitting on it. I know that feels wrong. That's exactly why you do it.

Step six: restore from your written seed, and confirm the test transaction reappears.

That wipe-and-restore proves three things at once. The seed was written down correctly. You know the procedure, and you learned it under calm conditions. And the backup actually works.

If the restore works, your real stack moves over and you've proven the backup. And if it fails, you found out with $1,000 at risk instead of $150,000. I think that's a pretty good trade for an afternoon of work.

### The never list

The rules for the seed itself are short. The seed exists on paper or steel, offline, and nowhere else. Not in a photo, not in a password manager, not in a note app, because anything with a screen and a network connection can be read.

And paper degrades and burns. For a meaningful stack, the seed goes on steel, and the backups live in separate locations. We'll cover the locations in the single-points-of-failure lesson.

### One pointer before you start moving coin

One thing to know before you start sending Bitcoin to this wallet, and then I'll point you at where it's taught properly.

Every deposit into your wallet is its own separate chunk, and every chunk costs a fee to spend later. So a lot of very small transfers quietly raises what it costs to move your own Bitcoin down the road. If you're buying small amounts regularly, let them accumulate and transfer in fewer, larger chunks rather than moving every buy the day it happens.

That's the whole rule you need today. The advanced library has the full lesson on it, along with why you use a fresh receiving address every time. Worth watching once, before you've made a hundred small transfers rather than after.

### If you're afraid to touch it

I want to talk to a specific person for a minute, because I run into them a lot. You bought the hardware wallet, you moved your Bitcoin onto it, and now you don't touch it. You don't plug it in, you don't update it, you don't check it, because you're scared that plugging it in is how you get robbed. A client told me almost exactly that: she doesn't plug it into anything, because she doesn't know how to keep it safe.

If that's you, a hardware wallet is built for exactly this. The whole design is that your keys never leave the device. It doesn't hand them to your computer or your phone when you plug it in. That's the entire reason the thing exists. So plugging it into your normal computer is not the risk you think it is.

There is one real threat to know about, and it's worth knowing precisely. There's malware that watches your clipboard and swaps the Bitcoin address you're sending to. You paste in your address, and what actually gets sent is somebody else's.

The defense takes 10 seconds and it never fails: **read the address on the hardware wallet's own screen and confirm it matches what's on your computer.** The whole address, not just the first few characters. The device screen is the thing malware can't touch. That's why it has a screen.

On firmware updates, I don't rush them, and I do eventually install them, because they often carry real security fixes. Being a little paranoid here isn't a bad instinct. Just don't let it turn into never.

### PIN versus seed phrase

And there's a distinction that resolves a fear I hear constantly: what if I die and nobody knows my PIN?

Your PIN protects the device. That's all it does. If someone gets the physical device, the PIN is what stops them.

Your seed phrase IS your Bitcoin. It works in any hardware wallet from any manufacturer.

So if something happens to you and your family doesn't know your PIN, that's fine. They don't need it. They buy a new hardware wallet, restore from the seed phrase, and the Bitcoin is there. The PIN dies with the device and it doesn't matter.

That also means the reverse is true, and it's the part to take seriously: **protecting the PIN is not protecting your Bitcoin.** The seed phrase is the thing that needs the real protection.

### Your decision

Whether your recovery actually works, which is not a thing you can decide by believing it.

### Put it in Orange Plan

Nothing to enter. This one happens on a device.

### You are done when

You have wiped and restored from your backup, on a device, and watched the balance come back. Until that has happened, you have a hardware wallet and a hope.


## 8.3 Single points of failure, account hardening, and scams
*`TEACH` · ~1,025 words · ~7 min*

> ✅ **Fixed in course:** stale hand-off promised "advanced custody" next — that
> material lives in 8.1; now points at the external demo.

**By the end of this lesson, you can:**

- Identify the three shapes of a single point of failure
- Run the nine-question hunt against your own setup
- Harden exchange and email accounts against real attacks
- Recognize the pattern behind Bitcoin scams

---

In today's lesson, we're going to cover single points of failure, account hardening, and the scam rules. This is the lesson about closing the doors you didn't know were open.

### Three shapes of a single point of failure

A single point of failure is anything that exists only once, where losing it means the Bitcoin is unreachable. And it comes in three shapes.

The first shape: the thing gets destroyed. A device, a backup.

The second shape: the thing is fine, but the person is unavailable, because only one person knows the process.

And the third shape: you're fine, your Bitcoin is fine, and the custodian won't let you move it. An exchange freezes an account.

Most people count the devices and completely forget the custodians.

### Two ordinary tuesdays

Let me make this concrete with the couple. Their setup: one hardware wallet in a desk drawer, one paper seed backup in the same house, a quarter Bitcoin on an exchange protected by SMS two-factor, and a wife who has never restored a wallet.

Now, two completely ordinary events.

The house floods. The device and the only seed backup are in the same building, so about $150,000 of Bitcoin goes out with the drywall. Two copies in one location were never really two copies.

Or he's hospitalized for 6 weeks. Nothing was stolen, nothing was lost, but nothing can move either. She can't sell a dollar of it, and she can't even tell anyone what exists.

No hackers involved in either one. The failure that actually loses Bitcoin is almost always just one thing without a backup.

### The nine-question hunt

So the hunt is 9 questions, and for each one you ask: is there only one?

Only one device? Only one seed backup? Only one location? Only one person who knows everything? One weak exchange login? One heir with no idea what exists? A document that contradicts your beneficiary forms, which are the forms your bank and retirement accounts keep on file naming who gets the money? A passphrase nobody else can recover? And multisig keys all sitting in one place?

The couple checks six of nine. And again, they're not careless. A normal setup collects only-ones on its own over the years, because nothing ever asked the question.

### The fix method

The fix method matters as much as the list, because trying to fix all nine at once is how nothing gets fixed.

Step one: list your top three, ranked by what the loss would cost. Not by how easy each one is to fix. Step two: pick the one at the top. Step three: fix that one, and only that one. Step four: re-check and repeat.

For the couple, the top item is the seed backup and the device sharing an address. The fix is a steel backup stored somewhere else. The in-laws' place, a safe deposit box, a second property. That's one afternoon of work.

The next one is the hospital scenario, which is a person problem. She needs to have restored a wallet once, with a small amount, so the procedure lives in two heads instead of one.

And notice the pattern: every only-one turns into one of three things. A backup, a second location, or a second person who knows the process. Never the secrets. The process.

### Account hardening

Now, account hardening, and I'll start with why I take this personally. A couple of years ago, someone called my bank pretending to be me and tried to move about $10,000. They didn't get it. But that's the day I moved my exchange and email logins onto physical security keys.

In most real-world losses, nobody breaks the encryption on your Bitcoin. They log in as you.

The hardening order matters, so do it in this order.

First, secure your email account, before anything else. Your email is the master key, because every other account will reset its password to that inbox on request. If they get the email, they get everything downstream.

Second, a strong, unique password on every account.

Third, app-based two-factor, not SMS, and turn the authenticator's cloud backup off.

Fourth, withdrawal delays and allowlists on at the exchange. And never click login links out of an email or a DM. Type the address yourself.

Why not SMS? Because of the SIM swap. Someone talks your carrier into moving your number onto their SIM, and from that moment, your texts arrive on their phone. A SIM swap takes the exchange and the email in one afternoon.

And one step better than the authenticator app: a hardware security key. A physical key is bound to the real site's address and checks it before signing. A lookalike phishing site simply doesn't get a response. That takes phishing off the table entirely, and it's the cheapest upgrade in this whole lesson.

### The scam rules

The scam rules are short.

If a call says your account is hacked, hang up and contact the provider yourself, through the app or the number on your card. And guaranteed returns are a scam. All of them. There's no exception waiting for you.

The common thread in every scam is urgency. Every scam needs you to act before you think. So when something feels urgent, close the app and slow down. That one habit catches scams you've never even seen before, because it doesn't need to recognize the scam. It just needs to notice the pressure.

### Your decision

Your one most expensive only-one, and the fix with a date on it.

### Put it in Orange Plan

Protect → Security checklist for the hardening items, and Needs attention for the next one.

### You are done when

Your only-one list exists, the top item by cost of loss has a specific fix this week, and your account hardening is done: secured email, unique passwords, non-SMS two-factor, withdrawal delays on. One fix, not nine.

Then watch the demo and the walkthrough below this video, where I set up a hardware wallet on screen and then we document your custody map in Orange Plan.


## 8.4 External demo: hardware wallet setup + exchange hardening
*`DEMO` · 877 words*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **8.7**. Beat sheet + required app state: SCREEN-SHOOT-LIST.md.

> ❓ **Decision needed (item 24):** this read text is a *shooting script* —
> "review your footage before publishing," "if it fails, retake," staging/blur
> instructions. Producer-facing, not learner-facing. Once the video exists,
> decide whether this text is replaced with a learner summary or kept as-is.

**By the end of this lesson, you can:**

- Follow a hardware wallet setup end-to-end, from box to first restore
- Harden an exchange account in the right order
- Understand what to record and what never to record

---

About a 9-minute screen-record demo. Not Orange Plan. Vendor tools only.

This is the one lesson where the app never opens. The procedure: hardware wallet from box to first restore, plus the exchange settings that stop most losses. The custody map walkthrough is where all of this becomes a checked box.

Set aside about 20 minutes to run through it. Have:

- A manufacturer-direct hardware wallet, still sealed.
- A throwaway demo wallet with trivial funds.
- A demo exchange account you're willing to burn. Separate from anything real.
- Something to stage or blur the seed display: tape, a physical shield, or a tested camera angle.

Production safety is the whole job. Never let a real seed, a QR of a seed, or a PIN entry pattern reach the frame. Review your footage before publishing for stray reflections, second monitors, or a phone screen in the shot.

Because nothing in this lesson touches the app, it doesn't age with the app. Record it once, keep it forever.

### Step 1: Hardware wallet, the six steps (~5:30)

Vendor device plus vendor app. Six ordered beats:

| # | Beat | What actually happens |
|---|---|---|
| 1 | Buy direct from the manufacturer. | Never used, never third-party. A used or third-party device may have already been compromised. |
| 2 | Generate a new wallet on the device. | The seed comes from the device's own randomness. You never type a seed you got from anywhere else. |
| 3 | Write the seed offline, set a PIN. | Show the act (hand on paper or steel) but never the words. Then the PIN entry, with no pattern on screen. |
| 4 | Send a small test transaction. | Trivial amount, in and out. Enough to have a real on-chain record. |
| 5 | Wipe the device. | The scary step. Factory reset the device you just set up. This is where most people back out, and it's the whole reason to do it on a throwaway. |
| 6 | Restore from seed and confirm the test transaction reappears. | Type the words back in from the offline copy. If the balance and history return, the seed is real. If they don't, the seed backup was theatre. The wipe surfaces the problem while only a trivial amount is at stake. |

When the balance reappears: only now has this device earned real money.

> ⚠ The seed word display, the PIN entry, and the restore input screens are the three moments the camera should never see directly. Stage them, blur them, or turn away. A single frame catching the seed is a lifetime of exposure.

### Step 2: Exchange hardening (~2:30)

Generic exchange settings. Name vendors as examples, not endorsements. Four ordered beats:

| # | Beat | Why it's on the list |
|---|---|---|
| 1 | Strong unique password. | Password reuse is how one leaked breach becomes every account. A password manager is fine here (it's not a wallet). |
| 2 | Two-factor auth off SMS, onto an authenticator app or physical security key. | SIM-swap is the boring attack that keeps working. |
| 3 | Secure the email account first. | The email account is the master key. Reset flows on every exchange route through it. Harden the email before the exchange. |
| 4 | Withdrawal delays and allow-listing on. | Delays give an attacker no fast path to move funds out. Allow-listing means even a session takeover can only send to your own destinations. |

Say the frame out loud: most losses are account takeovers, not broken cryptography. The math on Bitcoin isn't what gets attacked. The account you access it through is.

### Step 3: The never-list (~1:00)

Camera, no screen. Four sentences, said plainly:

- Never type seed words into a computer, phone, website, screenshot, or AI chat.
- Never buy a used or third-party device.
- Urgency is the red flag. Close the app and slow down.
- No real company ever asks for your seed.

Everything else in this space is a variation on those four.

### What good looks like

- The restore step actually completes on camera. Test transaction reappears in balance and history. If it fails, retake.
- Every seed frame is staged or blurred. Watch the footage.
- The hardening walk names the email account first. Order matters.
- The never-list gets said to the camera, not to a screen. No UI in that shot.

### Handing it off

The custody-map walkthrough is where this demo becomes a checked box. Three of the checklist items exist specifically to prove you did what this demo taught: recovery tested, backup verified, signing device tested recently. Check them only if you actually ran the demo. An unchecked item is honest. A checked item that never happened is dangerous, because the plan now believes something untrue.

## 8.5 Walkthrough: document your custody map in Orange Plan
*`DEMO` · 1,718 words · ~8 min*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **8.7**. Beat sheet + required app state: SCREEN-SHOOT-LIST.md.

**By the end of this lesson, you can:**

- Walk the custody checklist in the app honestly, tier by tier
- Fill out a Family Custody Map with zero secrets on it
- Export an encrypted backup of the plan itself
- Record your top single point of failure and this week's fix

---
This walkthrough turns your custody decisions into an on-screen map. Checklist honest, tier confirmed, top single point of failure named, and an encrypted backup of the plan itself.

Set aside about 15 minutes to run it slowly the first time. Have your custody level from the custody-level lesson in mind, and know whether your dead-man switch will need cloud sync.

Zero secrets on screen. The checklist doesn't ask for any. Every item is a checkbox. The only free-text moment in this whole walkthrough is a backup passphrase prompt in Step 3, and you'll know exactly what it is before you type.

### Pre-flight (before you open Protect)

Two things to check so the walkthrough doesn't stall:

⚠ Tier is keyed to estate net worth, not your custody choice. Protect renders only the current tier's checklist items:

- **Foundation** ($0 to $500,000).
- **Substantial** ($500,000 to $2 million).
- **High Net Worth** ($2 million or more).

The three **Hardware** items only exist at Substantial and above. If your net worth lands at Foundation, that group is simply absent.

⚠ Storage mode matters for Module 8's dead-man switch. In **Local Only**, the switch panel replaces itself with *"Automatic check-in emails require cloud sync."* Heir letter, beneficiaries, and the checklist still work locally. But if you plan to arm the switch next module, flip to Cloud at **Settings → Data & Privacy** now.

### Step 1: Orient on Protect

**Protect** (primary nav). Page heading: **Protect**.

Read the top strip:

- Eyebrow **Estate readiness → {n} of 5 essentials in place**.
- Five segments across the bar: **Dead man's switch, Heir letter, Protection tier, Checklist, Beneficiaries**.
- Below the bar: **Next: {action} · start →**. The app naming the next single fix.

Below that is the **Needs attention** queue. One row per incomplete essential, each with its own action. The queue enforces the fix-one-thing method: always the next essential, one action each.

⚠ Two different "checklist" strings live on Protect. The segment on the readiness bar says **Checklist**. The row inside Needs attention says **Security checklist**. Both are real. Use the right one for the surface you're pointing at.

### Step 2: Walk the checklist as the map

**Protect → Needs attention → Security checklist row → Open checklist**.

The panel opens with your tier label:

*"{n} of {n} for your tier. Substantial ($500K–$2M). Items name outcomes; any custody model can satisfy them."*

Four groups, each headed *"{group} · {n} of {n}"*:

| Group | Items | What it covers |
|---|---|---|
| Hardware | 3 | Recovery tested, backup verified, storage documented (Substantial and above only). |
| Distribution | 4 | No single point of failure. Locations, people, devices. |
| Legal | 6 | Will, powers, custody instructions. |
| Access after death | 4 | The Module 8 handoff. |

17 items total at Substantial. Each item has a **How** toggle for custody-model-neutral guidance. Checked items render struck through.

⚠ The top unchecked item is this week's fix, not the whole list. This checklist is a map you audit and repair one item at a time, not a to-do you run in an afternoon.

The recovery-test callback, verbatim from the app:

- *Full recovery process tested end-to-end*
- *Backup seed verified readable*

Those only get checked if you actually did the wipe-and-restore. A checked item that never happened is dangerous, because the plan now believes something untrue.

The single-point-of-failure callback:

- *Storage locations documented. Hints only, no exact details*
- *No single point of failure can destroy access (one device, one location, one person)*

⚠ There are no free-text fields anywhere in the checklist. It's checkboxes plus the "How" toggles. Never write secrets down in the app. The only free-text estate fields in the whole app live in Module 8's heir-letter dialog, and that dialog carries its own red warning banner.

### Step 3: Back up the plan itself

**Settings → Data & Privacy → Data & backups → Backup & Restore → Export Plan**.

Panel copy: *"Export your entire plan as an AES-encrypted restore backup file protected by a passphrase."*

⚠ Clicking **Export Plan** opens a browser passphrase prompt in plaintext. The prompt reads *"Enter a passphrase to encrypt your Orange Plan export."* This is a native browser prompt, visible on screen. It's a backup-file passphrase, not a wallet passphrase. Two different objects with two different jobs, both built to the 7-random-word standard from the advanced-custody lesson. Type it somewhere private, or use an obvious throwaway you can discard.

Success toast: **Plan exported**.

The sibling **Data Privacy** panel on this same page shows the mode: **Cloud** or **Local Only**.

The rest of the module was about protecting the coins. This one button protects the map. In Local Only mode, this file is your only backup, because there's no cloud copy to fall back on.

⚠ The click target is the row **Data & backups** (summary: "Storage mode, encrypted backups, AI review export"). **Backup & Restore** is the panel heading you see after the row expands. If you go looking for a top-level Backup & Restore tab, you won't find it.

### Step 4: Save the Family Custody Map

The app's checklist is the state of your custody map. 17 items, honest. The **Family Custody Map** PDF is the printable page of it: one sheet, one row per account, where everything is and who knows the process. The app can't hand that to a family in a filing cabinet. This is the artifact that can.

**Course toolkit: Family Custody Map** (PDF). Available under **Materials → 07 Family Custody Map**. Print it or fill it as a PDF, then store it with the will and your Heir Letter.

Fill it as you talk. It has five blocks:

| Block | What goes in |
|---|---|
| BITCOIN | Hardware wallet, exchange, ETF, collaborative custody. One row per instance, provider named. |
| WHERE THE BACKUPS ARE | **Coded references, not street addresses.** Never seed words, PIN, or passphrase — and on the family-facing sheet, not the exact physical location either. Write *"Seed backup: Location A · retrieval instructions held by: executor"*, not *"safe deposit box, First National, downtown branch."* |
| ACCOUNTS | Retirement, bank, brokerage. Retirement transfers by beneficiary form. Keep those current (Module 8 hooks into this). |
| INSURANCE & OTHER | Policies, property, anything else the family should find. |
| DOCUMENTS | Will, POA, healthcare directive, Executor packet, Heir letter. Where the original is, and who has a copy. |

⚠ This map never contains a secret. It says *that* things exist and how to start, never *how* to open them. The template's own footer says it: *"never the words, PIN, or passphrase."* If your instinct is to write the seed on this map, stop and go back to the no-secrets rule before continuing.

⚠ **Why coded, and not just secret-free.** A sheet listing where every backup, device and passphrase copy physically sits is a treasure map even with no secret written on it. Someone who steals the document learns exactly where to go. Coding the locations removes that.

⚠ **The condition on coding: the legend needs its own backup.** Coded references pass the dual-control test and can fail the redundancy test. If the executor packet holding the decode is lost, destroyed, or held by someone the family cannot reach, they have a map they cannot read, and the Bitcoin is recoverable in principle and gone in practice. Before coding anything, decide **where the second copy of the legend lives and who can reach it.** Skip that and you have rebuilt a 2-of-2 out of paperwork.

⚠ **Two documents, two jobs.** The **Owner Custody Audit** is your private working sheet: backup medium, recovery-test log, single points of failure, whether multiple locations exist, whether a passphrase is involved, config-file status, and the fix queue. The **Family Access Map** is the shared one, and it is narrower on purpose: what categories of assets exist, which provider or custody type, who knows the process, who to contact, and where the non-secret executor documents live. Neither holds a secret. **They are not stored together**, because the audit's detail is exactly what the family sheet is designed not to reveal.

⚠ The map is the companion to the Heir Letter in the estate module. The letter says who to call and in what order. The map says what exists and where. Both need to be findable by the executor, and neither can contain a secret.

Set the review date on the footer: *"Review yearly. Module 9."* That becomes an input to next module's annual walkthrough.

### Step 5: Record your decisions

There is no scheduler in Orange Plan. These decisions live in your calendar or a note.

- **Custody level chosen** (Level 1, 2, 3, or 4 from the custody ladder). Your call, based on the self-triage. **Not** the app's tier, which is named Foundation / Substantial / High Net Worth and keyed to estate size. Two different scales with two different inputs — do not let the app's badge answer this one.
- **Which of the two tests your design passes** — redundancy, dual control, or both — and why the one it misses is acceptable to you.
- **Top single point of failure and the one fix this week.**
- **Annual custody review** on the calendar, recurring — plus the change triggers below, because the calendar is not the only reason to reopen this.

**Review annually, and whenever one of these changes:** a new wallet or custodian · a material rise in the value of your Bitcoin · a new spouse, heir, executor, or trusted person · a move to another home or state · a device replacement · a backup location change · a new legal document · a health or family change · a new Bitcoin-backed loan or collateral setup.

Any one of these can quietly break a design that was correct the day you built it. No extra video needed here; the student text carries the list.

Optional on-screen anchor for the tier decision: **Protect → Protection tier → Mark as reviewed**.

Optional artifact: **Protect header → Download estate summary** produces a PDF of the readiness state.

The custody card you just built becomes the input to Module 9's annual review. That walkthrough re-reads this checklist honestly and asks: what changed since last year?

### Step 6: The "Draft with AI" button you'll scroll past

While you're on Protect, you'll pass a **Draft with AI** button in the Heir letter section. Walk past it in this lesson. It belongs to Module 8, where you're actually writing the letter.

If you want a line as you pass it: *"there's an assistant for the heir letter. That's next module."*

### What good looks like

- **The Needs attention list is shorter at the end than the start.** And the top remaining item gets named out loud as this week's fix.
- **Hardware items are honest.** *Full recovery process tested end-to-end* is checked only if you actually did the wipe-and-restore. Leave unchecked anything you haven't done; a checked item that never happened makes the plan believe something untrue.
- **Distribution items are the only-one hunt, itemized.** The two checkboxes measure **two different things**, and they are not both required of everybody:
  - *Key material stored in 2+ physical locations* is **redundancy** — can one lost copy permanently prevent recovery? Leaving this one unchecked is a real gap at any level.
  - *No single person can access funds alone* is **dual control** — can one person move the coins by themselves? This is a **design choice, not a requirement.** Plenty of sound single-signature households answer "yes, the owner can spend alone," and that is fine.

  The bar is not "both checked." The bar is that **you know which one your design gives you, which one it does not, and why you accepted that.** A student who checks dual control without redundancy has built two independent ways to lose everything, which is worse than the setup they started with.
- **Access after death** is the handoff to Module 8. Those four items are next module's homework list.
- **Nothing secret got typed.** Say the absence as the win. The one moment you'll touch a passphrase is the backup export in Step 3, and you'll have explained exactly what it is and is not.
- **The plan file exists on disk**, encrypted with a passphrase you control.

### What got built

| # | Item | Where it lives |
|---|---|---|
| 1 | Honest checklist state (the custody map) | Protect → Security checklist (17 items, tier-filtered) |
| 2 | Family Custody Map filled in on paper | Course toolkit → **07 Family Custody Map** (PDF). Stored with the will. |
| 3 | Tier confirmed | Protect → Protection tier → Mark as reviewed |
| 4 | Top SPOF and its fix | Needs attention top row plus a recorded decision |
| 5 | Encrypted plan backup on disk | Settings → Data & Privacy → Data & backups → Export Plan |
| 6 | Annual custody review on the calendar | Recorded decision (no in-app scheduler) |
| 7 | Optional artifact | Protect header → Download estate summary |

### Handing it off

The next module (Estate & Inheritance) turns "Access after death" from four checkbox promises into a working handoff. You'll pair the Custody Map you just saved with two more toolkit documents: the **Heir Letter** (who to call and in what order) and the **Executor Packet** (the operations manual for the person who runs the process). Everything on this custody map is the prerequisite for that walkthrough.

<!-- ADVANCED-GATE:START -->

## Related advanced lessons

**Your core plan is complete.** These are optional, and each one is
worth watching only when its condition is true for you. Continue only if
one of these describes your situation:

- **A7.2 What self-custody actually asks of you**
  → *Optional throughout. Watch it if you are weighing whether you want the whole job of self-custody, or if the weight of it is what has been stopping you. Your custody plan is complete without it.*
- **A7.3 Concentration: one institution, one vendor, one firmware**
  → *Watch this if either is true on your own screen: (1) your non-self-custodied Bitcoin sits at a single institution and losing access to it for a few months would change your life, or (2) every satoshi you own is behind one model of one device from one manufacturer. If neither is true, your custody plan is complete without this.*
- **A7.4 Wallet operations: UTXOs, dust, consolidation, and addresses**
  → *Watch this before you have made a hundred small transfers, not after. It applies if you buy Bitcoin regularly in small amounts, or if your wallet already shows a long list of separate chunks under coin control.*
- **8.5 Advanced custody: passphrase, multisig, and collaborative**
  → *Watch this if your custody setup fails one of the two access tests from the estate module: one person can spend alone, or one lost copy could permanently stop recovery. If your Level 2 design passes test two and you have accepted failing test one deliberately, your custody plan is complete.*

*Generated by `tools/build-module-gates.py` from the Gate line on each
advanced lesson. Edit the condition there, not here.*

<!-- ADVANCED-GATE:END -->
