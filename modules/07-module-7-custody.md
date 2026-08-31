# Unit 8 · Module 7 — Custody

*Choose which custody risks to keep or transfer, prove every recovery path, and make sure one device, method, provider, or person cannot materially damage the family's plan.*

**You will build:** A custody direction, a no-secrets map of the meaningful Bitcoin pools, a proven recovery path, and one major failure point fixed.

## 7.1 Self-custody, professional custody, and when a split makes sense

*`TEACH` · ~7.6 min · PRE-DICTATION FILMING DRAFT*

Most custody advice starts by asking, "What is the safest setup?"

I think that is the wrong question, because every setup can fail.

Self-custody protects you from a company freezing withdrawals, failing, or deciding when you can access your Bitcoin. But it makes you responsible for recovery, physical security, and leaving a process your family can follow.

Professional custody takes some of that burden off you and may give the family support, administration, and a legal or contractual process when something goes wrong. But you give up direct control and accept that an institution can delay or restrict access.

Multisig can make one lost key survivable. It also gives you more keys, more documentation, and more ways to build something the family does not understand.

There is no setup with no trade-offs.

The goal is to decide which risks you are willing to own and make sure one mistake, one provider, one device, or one bad day cannot destroy the family's plan.

Before we go farther, I want to separate custody from inheritance.

Custody is the operational side: where the Bitcoin is held, who can move it, how recovery works, and what can fail.

Estate planning is the legal side: who has authority and who receives the asset.

They have to fit together, but they are not the same job.

And there is one rule for the entire module: document the process, never the secrets.

No seed phrase, private key, passphrase, PIN, password, descriptor contents, or exact recovery location goes into Orange Plan, an heir letter, a cloud note, a photo, an email, or an AI tool. The plan can tell somebody what exists, who to call, and where the process starts. It should never become a treasure map.

> 🎬 **VISUAL — Four methods compared side by side: direct self-custody, collaborative multisig, institutional custody, intentional split. Each gets two rows: what it protects against and what you accept.**

Start by naming the risk you are trying to reduce.

Direct self-custody protects against provider failure, frozen withdrawals, and loss of direct control. The trade-off is that recovery mistakes, physical security, and family continuity become your responsibility.

Collaborative multisig can make one lost key survivable and give the family a provider that understands the setup. The trade-off is more setup, more maintenance, fees, provider involvement, and a recovery process that still has to be understood.

Institutional custody protects against personal key loss and some technical mistakes. It can also make administration simpler for a spouse, executor, or trustee. The trade-off is counterparty risk, withdrawal restrictions, identity checks, and less direct control.

An intentional split protects against one method or one provider taking out the entire plan. The trade-off is that the household now has more than one system to maintain and document.

Use a split when each additional setup solves a named risk the family can maintain.

The next question is how much direct control matters to you.

> 🎬 **VISUAL — Three-position control preference: Non-negotiable · Important, not absolute · Support and simplicity matter more.**

For one person, direct control is non-negotiable. They want a meaningful amount that no institution can freeze.

Another person may want both directly controlled Bitcoin and a professionally supported portion.

For another household, support, recourse, and family simplicity matter more than controlling every key personally.

None of those answers automatically tells you which product to use. It tells you which trade-off you are not willing to give up.

Then name the job of each meaningful Bitcoin pool.

Bitcoin used for near-term liquidity has a different job from a long-term sovereign reserve. Bitcoin in a retirement account has a different recovery and legal path from direct Bitcoin. Bitcoin posted to a lender has a different failure path again.

One household can reasonably use more than one custody method because the Bitcoin is doing more than one job.

I would classify each pool by rough scale instead of writing exact balances on a sensitive document:

- replaceable;
- meaningful;
- life-changing.

The decision changes when the amount becomes life-changing. A hardware wallet that felt reasonable when it held a smaller amount can eventually represent the family's entire financial future. Nothing about the device changed. What was at stake did.

That is when concentration in one method becomes a risk of its own.

> 🎬 **VISUAL — The One-Failure Test: lost recovery material · frozen account · provider failure · home disaster · coercion · incapacity · family unable to execute.**

For every meaningful pool, run the One-Failure Test:

Could one lost seed, one frozen account, one provider failure, one home disaster, one coercion event, or my incapacity materially damage the family's plan?

If the answer is yes, the setup may be too concentrated.

A large balance can use direct self-custody, collaborative multisig, institutional custody, or an intentional combination. The right architecture depends on the failures the household needs to survive.

It says the architecture has to match the actual failure that matters.

A single, well-run method can be enough when the amount is replaceable or not plan-critical, the recovery has been proven, the family dependency is limited, and simplicity is worth more than diversification.

An intentional split starts to make more sense when the amount is life-changing, one method protects almost everything, the household values both direct control and support, and the family can maintain the additional complexity.

I would use five steps to make the decision:

1. Name the job of the Bitcoin.
2. Name the failure you are protecting against.
3. Decide how much direct control matters.
4. Run the One-Failure Test.
5. Choose the simplest architecture that passes.

Choose the simplest setup that removes the household's real failure points and can still be maintained ten or twenty years from now.

I would measure readiness with four outcomes instead of a wealth ladder:

1. The accounts and recovery channels are secured.
2. Any direct custody has been proven through a real recovery test.
3. Family continuity exists: somebody besides you understands the process and knows who to call.
4. Catastrophic concentration is removed: no single device, person, provider, method, or location can materially destroy the plan.

A household can reach the fourth outcome with one strong method or a thoughtful combination that removes catastrophic concentration.

Before the next lesson, make one decision and one action.

Choose the current custody direction: one method or an intentional split.

Then name the first unfinished protection step for that direction.

If direct self-custody is the direction, that may be proving recovery with a small test wallet.

If an institutional bucket is part of the direction, that may be hardening the email account, adding phishing-resistant authentication, and reviewing the withdrawal and beneficiary process.

If collaborative multisig is the direction, that may be understanding the provider-independent recovery path before moving meaningful funds.

If an intentional split is the direction, write the job and maximum exposure for each bucket before moving anything.

The next two lessons handle the operational work: proving a hardware-wallet recovery and fixing the largest remaining single point of failure. The Advanced Library goes deeper on passphrases, multisig, institutional custody, and concentration across providers.

---
## 7.2 Set up a hardware wallet and prove the recovery

*`TEACH` · ~4.2 min · PRE-DICTATION FILMING DRAFT*

The important test for a hardware wallet is not whether you wrote the recovery words down.

It is whether you can restore the wallet from the backup before a meaningful amount of Bitcoin depends on it.

Most people skip that step. They generate a wallet, write the words down, send the Bitcoin, and hope the backup works. The first real recovery test then happens on the worst possible day.

I want the first test to happen while the wallet contains only a small amount and you are calm.

> 🎬 **VISUAL — Hardware-wallet six-step sequence. Never display real seed words.**

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

Separate locations protect against one fire or disaster. They can also create a theft or privacy problem if the locations are chosen poorly. Redundancy makes sure one event cannot destroy every recovery path. Each additional copy or location should solve a specific failure.

A passphrase changes the recovery process. The seed alone restores a different wallet from the seed plus passphrase. A forgotten or mistyped passphrase can make the intended funds unreachable even when the seed is perfect. That setup needs its own small-value test and its own recovery documentation.

Multisig adds another dependency: the wallet descriptor or configuration that explains how the keys form the wallet. The keys alone may not be enough to reconstruct the intended wallet safely. That is covered in the Advanced custody lesson.

There is also a practical issue with moving Bitcoin into cold storage: transaction size and UTXOs.

Every withdrawal can create a separate spendable output. A large number of tiny withdrawals can become expensive or awkward to spend later when network fees are high. I would not turn this into one permanent Bitcoin threshold because the dollar value and fee market change. The useful rule is to avoid creating a pile of uneconomic outputs and review consolidation when fees are low. The Advanced wallet-operations lesson covers the details.

For this core lesson, the finish line is straightforward: you have a device-specific recovery process you personally tested with a trivial amount, the backup is stored offline, and the address and transaction checks were performed on the trusted device.

The external demo will show the actual process using a throwaway wallet with no meaningful funds. Do not film or display a real seed, real PIN, or real family recovery setup.

---
## 7.3 Fix the single points of failure and harden the accounts

*`TEACH` · ~6.1 min · PRE-DICTATION FILMING DRAFT*

Most Bitcoin losses are not somebody breaking the cryptography.

They are one weak login, one backup, one location, one person who knows the process, one provider, or one rushed decision with no second check.

I call these the "only one" problems.

> 🎬 **VISUAL — The expanded only-one list: device · recovery backup · location · person · email or login · custody method · institutional provider · family process · wallet configuration.**

Go through every meaningful Bitcoin pool and look for the word one.

Only one hardware device.

Only one recovery backup.

Only one physical location.

Only one person who understands what exists.

Only one email account protecting every custodial login.

Only one custody method protecting all of the life-changing Bitcoin.

Only one institution holding all of the professionally custodied Bitcoin.

Only one copy of the wallet policy or descriptor needed to reconstruct a multisig wallet.

Only one family member who knows who to call.

A legal document naming one person while the technical recovery process points to somebody else.

The important addition is method and provider concentration.

A person can have several devices and backups and still have the entire plan depend on one method. They can also spread Bitcoin across two account names that rely on the same underlying custodian or recovery system.

That is why I want you to test failure domains, not count objects.

Three keys in the same house are still exposed to one house fire.

Two devices using the same vendor, firmware path, and companion software may not be as independent as they look.

Two custodial accounts may still depend on the same underlying company.

Redundancy gives the family another recovery path for the failure being addressed. Add equipment only when it solves that specific failure.

Use the rough scale from the first lesson: replaceable, meaningful, or life-changing.

Then ask one question for each row in the custody map:

If this entire row became inaccessible, would the financial plan still survive?

A temporary problem with a replaceable amount is different from a failure that destroys the retirement plan or leaves the family unable to act.

> 🎬 **VISUAL — One-Failure Test card with seven events and one final question: “Would the plan survive?”**

Run the test against:

- lost or damaged recovery material;
- a frozen institutional account;
- a provider or vendor disappearing;
- physical theft or coercion;
- a home disaster;
- your incapacity or death;
- and the family being unable to execute the process.

If one event materially damages the plan, that is the failure point to work on.

Rank the top one to three weaknesses by the damage they could cause, then fix the first one this week.

The fix may be a second location, a proven backup device, another person who understands the process, a provider-independent recovery path, a second custody method, or a lower maximum exposure to one institution.

The answer depends on the setup. The rule is that every added component must solve the failure you named.

Account hardening is part of custody too, especially for institutional custody, exchanges, retirement accounts, and the email account that can reset them.

Use a strong, unique password for the email account and every financial institution.

Secure the email account first because it is often the master reset path.

Use phishing-resistant hardware security keys or passkeys when the provider supports them. App-based two-factor authentication is still better than relying only on SMS.

Turn on withdrawal delays, allowlists, additional approvals, or account-lock features when they fit the way the account is used.

Review who the provider recognizes after death or incapacity. A hardened login is not a family recovery plan if nobody else can complete the legal process.

Save the institution's official support path before you need it. Do not use the phone number, login link, or support account supplied in an urgent message.

A few years ago, somebody called my bank pretending to be me and tried to move about ten thousand dollars. The bank stopped the transfer, and the attempt made the weakness very real. That is when I moved my email and important exchange logins to physical security keys.

An authenticator app is good. A hardware security key can add phishing resistance because it is bound to the real website instead of giving you a code that can be typed into a convincing fake page.

Then there are the scam rules.

Urgency is the biggest warning sign. Somebody says the account is being drained, the wallet is compromised, or the offer expires in ten minutes. The goal is to make you skip the verification process.

No legitimate provider needs your seed phrase or private key.

No support agent needs you to move Bitcoin into a "safe" wallet they supplied.

Guaranteed returns, send-one-get-two offers, and unsolicited recovery help are scams.

If somebody claims an account is compromised, end the communication. Open the official app or type the known website yourself. Contact the provider through the method you already verified.

The same pause applies to real security changes. Moving a life-changing balance, changing a multisig setup, adding a passphrase, replacing a device, or changing institutional providers should not happen because you feel rushed.

Before the walkthrough, complete the custody map at a no-secrets level:

- the job of each meaningful Bitcoin pool;
- its rough share or scale;
- how it is held;
- what that method protects against;
- the biggest remaining failure;
- and the family recovery path.

Then circle the one failure that could do the most damage. That becomes the next action. The app checklist is the honest record of which security work has actually been completed and which action comes next.

---
## 7.4 DEMO — Hardware-wallet recovery and exchange hardening

*`DEMO` · ~3 min · IMPLEMENTATION SHEET*

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
## 7.5 WALKTHROUGH — Document the custody decision and current status without storing secrets

*`WALKTHROUGH` · ~10 min · IMPLEMENTATION SHEET*

**Screen capture · about 10 minutes**

> **V1 capture gate:** Verify the final label and click path against the same approved Preview commit used for recording.

## Before recording

- The custody-direction decision from Lesson 7.1: one method or intentional split.
- Direct-control preference stated: non-negotiable · important but not absolute · support and simplicity matter more.
- Hardware-wallet recovery completed or clearly marked as still outstanding.
- One real single point of failure to fix.
- The no-secrets Custody Decision Map open beside the app.
- No secret material anywhere near the demo account, worksheet, or recording notes.

## 1 · State the custody direction before opening the checklist

**DO** Show the no-secrets Custody Decision Map.

**RECORD**:

- one primary method or an intentional split;
- how much direct control the household needs to retain;
- the risk the architecture is meant to reduce;
- and the first unfinished action.

**SAY** The app checklist records implementation status. It does not decide that every larger balance should move into a more complicated self-custody setup.

## 2 · Map the meaningful Bitcoin pools

For each meaningful pool, record only:

- the job of the Bitcoin;
- rough share or scale: replaceable · meaningful · life-changing;
- how it is held;
- what that method protects against;
- the biggest remaining failure;
- and the family recovery path.

**SHOW** at least two different jobs when the demo household uses them, such as directly controlled long-term Bitcoin and professionally custodied retirement-account exposure.

**⚠** Do not record an exact balance when a rough share or scale is enough.

**⚠** Do not record a seed, key, passphrase, PIN, descriptor contents, password, backup location, or exact recovery sequence.

## 3 · Run the One-Failure Test

For every life-changing row, ask:

- What if the provider freezes or disappears?
- What if the device and backup fail?
- What if the home or storage location is compromised?
- What if the owner is unavailable for six months?
- What if the spouse or executor has to handle this without the owner?
- Could one event materially damage the financial plan?

**CIRCLE** the largest current failure.

**SAY** Add a method, provider, or device only when it solves the failure we just named.

## 4 · Open Protect

**DO** Protect → readiness / security checklist.

**SEE** current tier, checklist sections, and attention queue.

**SAY** The app's tier determines which implementation items it asks about. The household's custody direction and risk trade-offs came from the decision map, not from a wealth ladder.

## 5 · Complete the checklist honestly

**DO** Review Hardware · Distribution · Legal · Access-after-death or the current sections.

**CHECK** only items that are true today.

**⚠** A recovery-test item stays open until the recovery was actually proven. Buying a hardware wallet does not complete it.

**⚠** Review the email security, authentication, withdrawal protections, beneficiary or estate process, and provider concentration for every institutional account.

**SAY** what is not being entered: no seed, passphrase, PIN, key, descriptor contents, password, or storage coordinates.

## 6 · Use the attention queue

**SEE** the top incomplete essential.

**COMPARE** it with the failure circled on the map.

**CHOOSE** the next action, owner, and deadline.

Examples:

- Direct self-custody → prove recovery with a trivial test wallet.
- Institutional custody → harden email, add phishing-resistant authentication, and document the provider's family process.
- Collaborative multisig → verify provider-independent recovery and the wallet policy backup.
- Intentional split → define the job and maximum exposure for each bucket before moving funds.

**SAY** The goal is one meaningful reduction in risk, not checking every box for appearance.

## 7 · Confirm process contacts without secrets

**DO** Review the relevant contact / provider fields that store names or roles, not recovery material.

**SAY** Who the household calls first and which provider, technical helper, attorney, or executor is part of the process.

**⚠** Estate authority and heir instructions are completed in Module 8. This walkthrough only confirms that the operational path has a starting point.

## 8 · Back up the plan itself

**DO** Settings → Data & Privacy → Backup & Restore.

**CREATE** an encrypted export.

**SAY** This file protects the financial-plan data. It is not a Bitcoin wallet backup and should never contain seed material.

**⚠** In Local Only mode, the export may be the only recovery path for the plan data.

## 9 · Schedule the annual custody check

Record:

- prove one recovery;
- inspect backups and locations;
- review device, software, institution, and provider support;
- re-run the One-Failure Test across methods and providers;
- refresh account and email security;
- confirm the family knows the first call;
- update the encrypted plan backup.

## 10 · Close Custody

**DO** Return to Build & improve / Protect status.

**SEE** the custody work represented honestly even when outside-device work remains.

## Module 7 checkpoint

- Custody direction is one method or an intentional split, chosen on purpose.
- Direct-control preference and the risk being reduced are stated.
- Every meaningful Bitcoin pool has a no-secrets job, scale, method, remaining failure, and family path.
- Hardware recovery is proven or clearly outstanding.
- The One-Failure Test identified the largest current weakness.
- Important accounts and email are hardened.
- No secret is stored in Orange Plan, the worksheet, or the course notes.
- Encrypted plan backup is saved.

---

<!-- ADVANCED-GATE:START -->

## Related advanced lessons

**Your core plan is complete.** These are optional, and each one is
worth watching only when its condition is true for you. Continue only if
one of these describes your situation:

- **A7.1 Compare passphrase, multisig, institutional custody, and an intentional split**
  → *(no gate condition set — add one to MASTER-ADVANCED.md)*
- **A7.2 What self-custody actually asks of you**
  → *(no gate condition set — add one to MASTER-ADVANCED.md)*
- **A7.3 Run the One-Failure Test across methods and providers**
  → *(no gate condition set — add one to MASTER-ADVANCED.md)*
- **A7.4 UTXOs, dust, consolidation, and address use**
  → *(no gate condition set — add one to MASTER-ADVANCED.md)*

*Generated by `tools/build-module-gates.py` from the Gate line on each
advanced lesson. Edit the condition there, not here.*

<!-- ADVANCED-GATE:END -->
