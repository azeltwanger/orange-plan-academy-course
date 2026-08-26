# Unit 8 · Module 7 — Custody

*Choose a custody level, prove recovery, harden the accounts, and remove the largest single point of failure without storing secrets in the plan.*

**You will build:** A tested custody process, one major failure point fixed, and a no-secrets checklist with an encrypted plan backup.

## 7.1 Choose a custody setup your household can recover

*`TEACH` · ~4.4 min · PRE-DICTATION FILMING DRAFT*

Everything in the financial plan assumes the Bitcoin is still there and the right people can reach it.

Custody is where that assumption becomes real.

I want to separate custody from inheritance before we start. Custody is the operational side: where the Bitcoin is held, how access works, how recovery works, and what can fail. Estate planning is the legal side: who has authority and who receives the assets. They have to fit together, but they are not the same job.

There is one rule for the entire module: document the process, never the secrets.

No seed phrases, private keys, passphrases, PINs, or exact recovery information go into Orange Plan, an heir letter, a cloud note, a photo, an email, or an AI tool. The plan can tell somebody who to contact and what process exists. It should not become a treasure map.

> **Visual:** Custody deck frame: where held, what type, who knows, what if unavailable, where are the single points of failure.

The first question is what job the Bitcoin has.

Bitcoin being held for near-term liquidity may sit in a different setup from the long-term family stack. Bitcoin inside an IRA or ETF has different access and counterparty risks from direct Bitcoin. Collateral posted to a lender has a completely different job again.

One person can reasonably use more than one custody method because the coins are doing more than one job.

Then choose the level of responsibility that fits the amount and the household.

> **Visual:** Custody levels 1 through 4.

Level one is a hardened exchange or broker for a smaller or learning-stage amount. That still means a unique password, a secured email account, strong two-factor authentication, withdrawal protections, and a clear understanding that the institution controls the withdrawal process.

Level two is direct ownership with a hardware wallet. The seed is created offline, the device is tested with a small amount, and recovery is proven before meaningful Bitcoin depends on it.

Level three is a larger family setup. This may use a passphrase, collaborative support, or another design that separates responsibilities and gives the household a realistic recovery path.

Level four is a higher-value or more complex setup, often using multisig or professional collaborative custody, coordinated with the legal plan and tested with the people who may eventually use it.

The levels are not a status ladder. More complicated is not automatically safer.

A simple hardware-wallet setup that is tested, backed up, and understood can be safer than a multisig arrangement where nobody knows the wallet configuration or where the keys are.

The right setup is the one you can maintain, explain, and recover from. It also has to be a setup your spouse, executor, or heirs can navigate with the help you planned for them.

I would evaluate any custody method against five risks.

First, loss. What happens if the device, seed, login, or one location is destroyed?

Second, theft. What can an attacker do with one compromised component?

Third, unavailability. What happens if you are alive but unable to act for a month or a year?

Fourth, death. Do the legal authority and technical recovery process lead to the same people?

Fifth, complexity. How many steps, vendors, files, and assumptions have to remain correct for the next twenty years?

The setup should have redundancy without accidentally giving one untrusted person everything needed to spend.

And it should avoid concentration where possible. One institution, one hardware-wallet vendor, one firmware path, one physical location, or one person can all become a single point of failure when too much depends on them.

You do not have to solve every advanced problem in this module. The core outcome is much simpler:

- choose the custody level that fits the stack today;
- make sure the current method is hardened;
- prove the recovery that method requires;
- identify the largest single point of failure;
- and document the process without documenting the secrets.

The advanced lesson compares passphrase, collaborative custody, and DIY multisig in more detail. The estate module coordinates the chosen setup with the executor and legal documents.

In the walkthrough, we'll use Protect as a no-secrets checklist. We will record which protections are actually complete, identify the next single point of failure to fix, and create an encrypted backup of the plan itself.

---

## 7.2 Set up a hardware wallet and prove the recovery

*`TEACH` · ~4.2 min · PRE-DICTATION FILMING DRAFT*

The important test for a hardware wallet is not whether you wrote the recovery words down.

It is whether you can restore the wallet from the backup before a meaningful amount of Bitcoin depends on it.

Most people skip that step. They generate a wallet, write the words down, send the Bitcoin, and hope the backup works. The first real recovery test then happens on the worst possible day.

I want the first test to happen while the wallet contains only a small amount and you are calm.

> **Visual:** Hardware-wallet six-step sequence. Never display real seed words.

The general process is:

1. Buy the device from the manufacturer or another source the manufacturer explicitly supports. Inspect the packaging and follow the vendor's current verification instructions.
2. Generate a new wallet on the device. Do not use recovery words supplied in the box or by another person.
3. Record the recovery material offline and set the device PIN according to the current vendor process.
4. Receive a small test transaction and confirm it is visible.
5. Use the vendor's verified recovery-check procedure or, when appropriate for the exact device, wipe and restore the test wallet.
6. Confirm the same wallet and test funds reappear before sending a meaningful balance.

The exact button sequence depends on the device and firmware. That is why the filmed demo has to use the actual hardware and current instructions rather than a generic script pretending every wallet works the same way.

There are a few rules that do not change.

Never type recovery words into a computer, phone, ordinary website, photo, cloud document, or AI chat.

Never use a recovery tool because somebody contacted you and created urgency.

Never assume a device screen and a computer screen showing the same address is enough. Verify receive addresses on the trusted device itself.

And always send a small transaction before moving a life-changing amount.

The backup has to survive the risks that matter in your life. Paper can be damaged by fire, water, fading, or somebody throwing it away. A steel backup may make sense for meaningful long-term holdings. Multiple copies can reduce loss risk, but copies also increase the number of places that have to be secured.

Separate locations protect against one fire or disaster. They can also create a theft or privacy problem if the locations are chosen poorly. Redundancy is not simply making as many copies as possible. It is making sure one event cannot destroy every recovery path.

A passphrase changes the recovery process. The seed alone restores a different wallet from the seed plus passphrase. A forgotten or mistyped passphrase can make the intended funds unreachable even when the seed is perfect. That setup needs its own small-value test and its own recovery documentation.

Multisig adds another dependency: the wallet descriptor or configuration that explains how the keys form the wallet. The keys alone may not be enough to reconstruct the intended wallet safely. That is covered in the Advanced custody lesson.

There is also a practical issue with moving Bitcoin into cold storage: transaction size and UTXOs.

Every withdrawal can create a separate spendable output. A large number of tiny withdrawals can become expensive or awkward to spend later when network fees are high. I would not turn this into one permanent Bitcoin threshold because the dollar value and fee market change. The useful rule is to avoid creating a pile of uneconomic outputs and review consolidation when fees are low. The Advanced wallet-operations lesson covers the details.

For this core lesson, the finish line is straightforward: you have a device-specific recovery process you personally tested with a trivial amount, the backup is stored offline, and the address and transaction checks were performed on the trusted device.

The external demo will show the actual process using a throwaway wallet with no meaningful funds. Do not film or display a real seed, real PIN, or real family recovery setup.

---

## 7.3 Fix the single points of failure and harden the accounts

*`TEACH` · ~3.6 min · PRE-DICTATION FILMING DRAFT*

The failures that lose Bitcoin are usually not somebody breaking the cryptography.

They are one weak login, one backup, one location, one person who knows the process, or one rushed decision with no second check.

I call these the "only one" problems.

> **Visual:** Custody deck list: one device, one seed copy, one location, one weak login, one heir with no idea, one lost passphrase, all multisig keys together.

Go through the setup and look for the word one.

Only one hardware device.

Only one seed backup.

Only one physical location.

Only one person who understands what exists.

Only one email account protecting every exchange login.

Only one passphrase record, or no one else who even knows a passphrase is part of the recovery.

All multisig components stored in the same building.

A legal document naming one person while the technical recovery process points to somebody else.

You do not have to fix every item this week. Rank the top one to three by the damage they could cause, then fix the first one.

The fix may be a second location, a tested backup device, a second person who understands the process, a provider contact, or updated legal and beneficiary information. The answer depends on the setup. The rule is that no ordinary failure should erase every recovery path.

Account hardening is part of custody too.

Use a strong, unique password for the email account and each exchange or financial institution. The email account comes first because it is often the reset path for everything else.

Use app-based two-factor authentication or a hardware security key rather than relying only on SMS when the provider supports it.

Turn on withdrawal delays, allowlists, or additional approval steps when they fit the way you use the account.

Save the institution's official contact method before you need it. Do not use the phone number, login link, or support account supplied in an urgent message.

A few years ago, somebody called my bank pretending to be me and tried to move about ten thousand dollars. They did not get it, but it made the weakness very real. That is when I moved my email and important exchange logins to physical security keys.

An authenticator app is good. A hardware key can add phishing resistance because it is bound to the real website instead of giving you a code that can be typed into a convincing fake page.

Then there are the scam rules.

Urgency is the biggest warning sign. Somebody says the account is being drained, the device is compromised, or the offer expires in ten minutes. The goal is to make you skip the normal verification process.

No legitimate provider needs your seed phrase or private key.

No support agent needs you to move Bitcoin into a "safe" wallet they supplied.

Guaranteed returns, send-one-get-two offers, and unsolicited recovery help are scams.

If somebody claims the account is compromised, end the communication. Open the official app or type the known website yourself. Contact the provider through the method you already verified.

The same pause applies to real security changes. Moving a large balance, changing a multisig setup, adding a passphrase, or replacing a device should not happen because you feel rushed.

Before the walkthrough, identify the single most dangerous "only one" in your current setup. That is the item you are going to record and fix first. The app checklist is not the security itself. It is the map of what has and has not actually been done.

---

## 7.4 DEMO — Hardware-wallet recovery and exchange hardening

*`WALKTHROUGH / DEMO` · narrate from the DO / SEE / ⚠ sheet*

**External screen / device recording · about 12 minutes**

## Production safety

- Use a throwaway wallet with trivial funds.
- Use the exact device and firmware named in the take.
- Follow current official device instructions.
- Never show a real seed, passphrase, PIN pattern, backup QR, live family address, or meaningful account balance.
- Record the act of writing recovery material, not the words.
- Have a second person review the raw footage for accidental secrets before editing.

## Part 1 · Verify the device and create a test wallet

**DO** Unbox or reset the demo device according to the current official process.

**SHOW** authenticity / firmware verification steps the vendor currently requires.

**DO** Generate a new wallet on the device.

**SAY** A seed supplied in the package or by another person is not a new wallet.

**DO** Record the recovery material off camera and set the PIN.

## Part 2 · Receive and verify a small transaction

**DO** Generate a receive address.

**VERIFY** the address on the trusted device screen.

**SEND** a trivial test amount.

**SEE** the transaction appear.

## Part 3 · Prove recovery

**DO** Use the exact vendor-supported backup-check or wipe-and-restore process chosen for this device.

**RESTORE** the test wallet from the offline recovery material.

**VERIFY** the same wallet and test transaction reappear.

**SAY** This is the point where the backup becomes proven instead of assumed.

**⚠** Do not teach one device's button sequence as universal.

## Part 4 · Show the offline backup standard

**SHOW** paper versus steel without displaying recovery data.

**EXPLAIN** separate locations, theft trade-offs, and the annual inspection.

**DO NOT** show actual storage locations.

## Part 5 · Harden an exchange and the email account

Using demo accounts:

- change to a strong unique password;
- enable app-based 2FA or hardware-key authentication when supported;
- secure the email account first;
- enable withdrawal allowlists, delays, or approval controls that exist;
- save the official support path;
- remove SMS-only recovery where practical and supported.

**SAY** Never follow a login or recovery link from an urgent email, text, call, or direct message.

## Part 6 · Close with the repeatable standard

The setup earns meaningful Bitcoin only after:

- the device is verified;
- a small receive is confirmed on-device;
- recovery is proven;
- the offline backup is protected;
- the account and email are hardened;
- and the process is documented without secrets.

## Device verification receipt

Record in `DEVICE-DEMO-VERIFICATION.md`:

- device model;
- firmware version;
- official instructions checked date;
- recovery method used;
- test-wallet amount;
- reviewer who checked raw footage for secrets.
---

## 7.5 WALKTHROUGH — Document the custody status without storing secrets

*`WALKTHROUGH / DEMO` · narrate from the DO / SEE / ⚠ sheet*

**Screen capture · about 7 minutes**

## Before recording

- Hardware-wallet demo completed or clearly marked as still outstanding.
- A chosen custody level.
- One real single point of failure to fix.
- No secret material anywhere near the demo account or recording notes.

## 1 · Open Protect

**DO** Protect → readiness / security checklist.

**SEE** current tier, checklist sections, and attention queue.

**SAY** The app's tier is an implementation checklist. The household's custody level is the actual design decision from Lesson 7.1.

## 2 · Complete the checklist honestly

**DO** Review Hardware · Distribution · Legal · Access-after-death or the current sections.

**CHECK** only items that are true today.

**⚠** A recovery-test item stays open until recovery was actually proven. Buying a hardware wallet does not complete it.

**SAY** what is not being entered: no seed, passphrase, PIN, key, descriptor contents, or storage coordinates.

## 3 · Use the attention queue

**SEE** the top incomplete essential.

**CHOOSE** the largest current "only one" and state the fix and deadline.

**SAY** The goal is one meaningful reduction in risk, not checking every box for appearance.

## 4 · Confirm the process contacts without secrets

**DO** Review the relevant contact / provider fields that store names or roles, not recovery material.

**SAY** Who the household calls first and which provider or technical helper is part of the process.

**⚠** Estate authority and heir instructions are completed in Module 8.

## 5 · Back up the plan itself

**DO** Settings → Data & Privacy → Backup & Restore.

**CREATE** an encrypted export.

**SAY** This file protects the financial-plan data. It is not a Bitcoin wallet backup and should never contain seed material.

**⚠** In Local Only mode, the export may be the only recovery path for the plan data.

## 6 · Schedule the annual custody check

Record:

- prove one recovery;
- inspect backups and locations;
- review device / software support;
- re-scan shared dependencies;
- refresh account security;
- update the encrypted plan backup.

## 7 · Close Custody

**DO** Return to Build Your Plan / Protect status.

**SEE** the custody work represented honestly even when outside-device work remains.

## Module 7 checkpoint

- Custody level is chosen.
- Hardware recovery is proven or clearly outstanding.
- Top single point of failure has an owner and deadline.
- Important accounts and email are hardened.
- No secret is stored in Orange Plan or the course notes.
- Encrypted plan backup is saved.
---

## Module checkpoint

- [ ] Custody level is chosen for the amount and household.
- [ ] Hardware recovery is proven or clearly outstanding.
- [ ] The top single point of failure has an owner and deadline.
- [ ] Important accounts and email are hardened.
- [ ] No seed, key, passphrase, or PIN is stored in the app or course notes.
- [ ] An encrypted backup of the plan data exists.
