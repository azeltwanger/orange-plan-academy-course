# Unit 8 · Module 7 — Custody

*Custody as operational protection: choose your level on the four-tier ladder, set up hardware with a proven recovery test, close single points of failure, and — when it fits — go advanced with passphrase, multisig, or collaborative custody.*

## 7.1 Choose the custody setup that matches your stack and family
*`TEACH` · ~871 words · ~6 min*

**By the end of this lesson, you can:**

- Score your household against the five custody questions
- Name the job each pile of Bitcoin is doing
- Match a custody level to your stack, your skill, and your family
- Decide whether custodial Bitcoin should sit at more than one institution
- Name what your whole stack is trusting, and whether to spread that out

---

In today's lesson, we're going to choose the custody setup you can actually maintain and your family can actually recover.

The four levels in this course are an Orange Plan framework. They are not a Bitcoin protocol standard and they are not a score.

The right level is the simplest setup that protects the amount at stake, survives the failures you care about, and still works when somebody besides you has to use it.

### The job of custody

Bitcoin exists on the network. Custody is control of the signing material that can authorize a spend.

Depending on the setup, that can involve:

- an institution's account and legal claim process;
- one hardware wallet and its recovery material;
- a wallet backup plus a passphrase;
- multiple signing keys and a wallet policy or descriptor;
- a collaborative provider and a documented provider-independent recovery path.

Do not call every one of those things a seed. The backup standard matters.

### Five questions before the level

First: how much is at stake today, and what could it become under assumptions you would defend?

Second: who depends on it?

Third: which loss worries you most—online account takeover, physical theft, backup loss, coercion, provider failure, incapacity, or death?

Fourth: how much operational complexity will you actually maintain?

Fifth: can somebody else follow the recovery process without improvising or learning Bitcoin during a crisis?

I would choose the simplest setup you can actually prove works.

### Level 1: hardened institution

Level 1 delegates signing control to a regulated or otherwise chosen institution.

Your job is account security, beneficiary and death-claim paperwork, withdrawal controls, and diversification of whatever counterparty exposure you keep.

The family recovery test is not a device restore. It is the institution's login-recovery and death-claim process.

Verify what documents the institution requires, who can make the claim, whether a beneficiary designation exists, how long the process can take, and what happens if the institution fails.

This level trades self-custody risk for counterparty and legal-claim risk. That can be a legitimate trade when it is deliberate.

### Level 2: single-signature hardware wallet

Level 2 moves signing control into a hardware wallet and a compatible wallet setup.

The recovery material may be a BIP39 mnemonic, another single backup, or a supported multi-share standard. Record the actual standard rather than assuming every device uses 12 or 24 words.

The hardware wallet is replaceable. The recovery material and any required passphrase or wallet information are the durable pieces.

I think this is simple enough for a lot of households to maintain well. The risk is that one complete backup can authorize the wallet, and one missing required piece can also block recovery.

### Level 3: added separation

Level 3 adds another independent element, often a passphrase or another deliberately separated custody arrangement.

A BIP39 passphrase derives a different wallet. Every passphrase, including a typo, derives a valid wallet. That gives separation, but it also creates another thing that must be entered exactly and recovered.

A passphrase is not multisig. The mnemonic and passphrase are both required to derive that wallet, but the protocol does not enforce two independent signers.

This level only improves the plan when the new element has its own backup, its own location, and a tested family process.

### Level 4: threshold signing

Level 4 uses a threshold policy such as 2-of-3 multisig, either independently or with a collaborative provider.

Two signing keys can authorize a spend and one cannot. Losing one key can be survivable.

The keys are not the whole recovery package. The family also needs the wallet policy or descriptor, script and derivation information, and compatible software or a provider-independent recovery process.

A descriptor cannot sign, but losing the policy can make reconstruction slow, uncertain, or dependent on a provider.

Collaborative custody is only provider-independent when the client truly holds enough keys to meet the threshold, has exported the policy data, and has tested recovery in compatible software without the provider.

### Complexity can become the biggest risk

A second device, passphrase, multisig, or provider can reduce one failure and create three new ones.

More pieces mean more backups, more updates, more inheritance instructions, and more ways for the written plan to drift from reality.

A single-signature setup maintained and tested well can be safer than a multisig nobody can reconstruct.

### Your decision

Choose the level from the failure you are trying to remove and the process your household can operate.

Then write down why that level fits your household.

"We use Level 2 because we can maintain one hardware-wallet recovery process and accept the single-backup control risk."

Or:

"We use Level 4 because the amount justifies threshold signing and we have tested recovery without the provider."

### Put it in orange plan

Protect → Protection tier. Save the level, why it fits, and the next review trigger.

Do not put a backup, seed, passphrase, PIN, private key, descriptor, or exact storage location into Orange Plan.

### You are done when

The level fits the amount and your family, you can explain the risk you accepted, and you have actually tested the recovery process instead of assuming it works.


## 7.2 Set up a hardware wallet and test recovery
*`TEACH` · ~811 words · ~5 min*

**By the end of this lesson, you can:**

- Set up a hardware wallet safely from scratch
- Never leak the seed phrase, ever
- Perform a wipe-and-restore recovery test
- Know the one transfer rule that matters before you start sending coin

---

In today's lesson, we're going to set up a hardware wallet and prove the recovery path without turning the test itself into the failure.

This is the operational lesson. Use the exact manufacturer's current instructions for the device and firmware on the table.

### What the device does

A hardware wallet stores signing keys and signs transactions in an environment designed to keep those keys away from the everyday computer or phone.

The Bitcoin is not inside the device. The device is replaceable.

What recovers the wallet depends on the setup. That can include the wallet backup, a passphrase, the address or script type, derivation information, and the wallet policy or descriptor if you use multisig.

Do not assume one mnemonic restores every wallet in every device from every manufacturer.

### Start with a clean device

Buy from the manufacturer or an authorized source you can verify.

Follow the official authenticity and firmware checks. Never use recovery words or a PIN supplied in the box, on a card, or by another person.

The device should generate the backup during setup. Nobody legitimate asks you to type that backup into a website, chat, support form, or ordinary computer.

### Record the actual backup standard

A common BIP39 backup can contain 12, 15, 18, 21, or 24 words. Other devices can use a different or multi-share standard.

Write down what this device actually produced and which wallet it belongs to.

If a passphrase is enabled, the backup without the exact passphrase derives a different wallet. Record that fact in the no-secrets process map without putting the passphrase there.

### Verify the backup before moving a meaningful amount

I would test it in this order.

First, use the manufacturer's backup-check feature when one exists. That checks the recorded backup without destroying the working setup.

Second, when practical, restore on a spare compatible device or approved recovery environment with only a small test amount at risk.

Third, use a destructive wipe-and-restore only after the backup has already been checked, the exact vendor procedure is open, and another working path or low-value test protects you from one typo becoming a loss.

The old course made wiping the only device the default first proof. That was too aggressive.

A recovery test should reduce risk, not temporarily create one live copy of everything you own.

### Verify the wallet, not only the words

A successful recovery means more than the device accepting the backup.

Confirm that the recovered wallet produces the expected receive address or wallet fingerprint and can see the expected small test transaction.

For a passphrase wallet, test the exact passphrase and verify the intended wallet, because every different passphrase opens a valid but different wallet.

For multisig, confirm the wallet policy or descriptor loads and that the intended threshold combinations can sign.

### Receive with the trusted display

When receiving Bitcoin, generate the address in the wallet software and confirm the destination on the hardware device's trusted display.

Do not approve an address that appears only on the computer or phone.

This reduces common malware risk. It is not a guarantee against every device, firmware, supply-chain, or human failure, which is why the setup source and recovery process still matter.

### Backup storage

Keep recovery material offline under the policy you chose.

Paper can be damaged. Metal can survive more physical hazards. Either can be copied by anyone who finds it.

Separate redundant copies so one fire, flood, theft, or household conflict does not reach all of them.

Do not photograph the backup, email it, upload it, store it in a generic note, or enter it into an AI.

A supported encrypted digital backup is a different design decision and must follow the exact wallet standard; the course default remains offline recovery material.

### PIN, passphrase, and backup are different

The PIN protects access to the device.

The wallet backup recreates the signing material under a compatible recovery path.

The passphrase, when used, selects a different derived wallet and must be recovered exactly.

None of those should be treated as interchangeable.

### Updates

Install firmware and wallet-software updates only from official sources and only when the recovery path is already verified.

Read the release and migration notes. Do not rush an update because an email or social post creates urgency.

### Your decision

Which recovery proof this setup will use: manufacturer backup check, spare-device recovery, or a carefully staged destructive restore.

### Put it in orange plan

Protect → Security checklist. Mark the recovery test complete only after the intended wallet was recovered and verified.

Do not record any seed words, passphrases, PINs, private keys, or backup contents in the app.

### You are done when

The backup standard is known, the intended wallet was independently recovered or checked, the address/policy matched, and the test did not rely on the only working copy of a meaningful balance.


## 7.3 Single points of failure, account hardening, and scams
*`TEACH` · ~589 words · ~4 min*

> ✅ **Fixed in course:** stale hand-off promised "advanced custody" next — that
> material lives in 7.1; now points at the external demo.

**By the end of this lesson, you can:**

- Identify the three shapes of a single point of failure
- Run the nine-question hunt against your own setup
- Harden exchange and email accounts against real attacks
- Recognize the pattern behind Bitcoin scams

---

In today's lesson, we're going to find the one failure that can still take the whole setup and harden the online accounts around it.

### Find one failure at a time

A single point of failure is one person, device, backup, provider, email account, or location whose loss or compromise can stop recovery or authorize an unwanted spend.

Do not create a list of 20 theoretical risks and fix none of them.

Ask:

- What one thing can authorize everything?
- What one thing can permanently block recovery?
- What one provider can freeze or impair every custodial holding?
- What one email or phone number can reset every financial account?

Fix the largest one, test the new process, then repeat at the annual review.

### Harden the email first

The primary email is often the reset path for exchanges, brokerages, banks, cloud accounts, and the plan itself.

Use a unique password and a phishing-resistant authenticator where the provider supports one.

Passkeys and hardware security keys can be phishing-resistant when correctly deployed. Keep a backup key or recovery method in a separate location.

A time-based authenticator code is generally stronger than SMS, but a code you type into a phishing site can still be stolen in real time.

SMS is the last choice, not the standard.

### Harden every custodial account

For each exchange, brokerage, lender, and custodian:

- use a unique password;
- use passkey or security key when supported, otherwise a strong authenticator method;
- store recovery codes offline and separately;
- turn on withdrawal allowlists, delays, or secondary approval when available;
- review active sessions and trusted devices;
- remove old phone numbers and unused recovery methods;
- test the real account-recovery path without locking yourself out.

Provider features change. The course names the control, not a button every provider promises to have.

### Recovery can be the back door

A strong security key does not help if support will reset the account after a weak identity check.

Ask what happens after the phone is lost, the email is inaccessible, or the owner dies.

The recovery path should not be easier to attack than the login path.

### Scams use urgency and authority

The common scam asks you to act before you verify.

"Your wallet is compromised."

"Move the Bitcoin now."

"Enter the backup to synchronize."

"Support needs remote access."

When you get one of these messages, stop before you do anything.

Stop. Close the message. Navigate to the provider through a known bookmark or official channel. Verify on another device or with another person. Never reveal recovery material.

No legitimate support person needs the wallet backup, private key, passphrase, or PIN.

### Physical and social exposure

Who knows the amount, location, or exact setup is also part of your custody risk.

The more people who know the amount, location, or exact setup, the larger the coercion and social-engineering surface.

The family needs the process. They do not all need every secret.

Public content should discuss principles and test setups, never the real household's balance, locations, device identifiers, or recovery distribution.

### Your decision

The largest remaining single point of failure and the one hardening action with a date.

### Put it in orange plan

Protect → Security checklist. Record completion status only. Keep names, secrets, backup contents, and exact storage locations off the page.

### You are done when

The email and custodial accounts use the strongest practical authentication available, recovery paths are documented, and the largest remaining failure has a specific fix instead of a vague plan to be more secure.


## 7.4 External demo: hardware wallet setup + exchange hardening
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

## 7.5 Walkthrough: document your custody map in Orange Plan
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

<!-- PLAN-LIFECYCLE:MODULE-7 -->
### Build Your Plan handoff

Custody work supports the Protect area, but it does not complete the heir-letter and beneficiary tasks by itself. Leave this module with the custody map and recovery process complete; Module 8 finishes **Build Your Plan → Protect**.

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
- **A7.1 Advanced custody: passphrase, multisig, and collaborative**
  → *Watch this if your custody setup fails one of the two access tests from the estate module: one person can spend alone, or one lost copy could permanently stop recovery. If your Level 2 design passes test two and you have accepted failing test one deliberately, your custody plan is complete.*

*Generated by `tools/build-module-gates.py` from the Gate line on each
advanced lesson. Edit the condition there, not here.*

<!-- ADVANCED-GATE:END -->
