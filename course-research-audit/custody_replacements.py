from __future__ import annotations

from textwrap import dedent


def b(text: str) -> str:
    return dedent(text).strip() + "\n"


FILES = {
"scripts/07-1_choose-the-custody-setup-that-matches-you.md": b(r'''
TELEPROMPTER SCRIPT — segment 7.1
7.1 Choose the custody setup that matches your stack and family
~10 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to choose the custody setup you can actually maintain and your family can actually recover.

The four levels in this course are an Orange Plan framework. They are not a Bitcoin protocol standard and they are not a score.

The right level is the simplest setup that protects the amount at stake, survives the failures you care about, and still works when somebody besides you has to use it.

== THE JOB OF CUSTODY ==

Bitcoin exists on the network. Custody is control of the signing material that can authorize a spend.

Depending on the setup, that can involve:

- an institution's account and legal claim process;
- one hardware wallet and its recovery material;
- a wallet backup plus a passphrase;
- multiple signing keys and a wallet policy or descriptor;
- a collaborative provider and a documented provider-independent recovery path.

Do not call every one of those things a seed. The backup standard matters.

== FIVE QUESTIONS BEFORE THE LEVEL ==

First: how much is at stake today, and what could it become under assumptions you would defend?

Second: who depends on it?

Third: which loss worries you most—online account takeover, physical theft, backup loss, coercion, provider failure, incapacity, or death?

Fourth: how much operational complexity will you actually maintain?

Fifth: can somebody else follow the recovery process without improvising or learning Bitcoin during a crisis?

The answer is not the most impressive setup. It is the one you can prove.

== LEVEL 1: HARDENED INSTITUTION ==

Level 1 delegates signing control to a regulated or otherwise chosen institution.

Your job is account security, beneficiary and death-claim paperwork, withdrawal controls, and diversification of whatever counterparty exposure you keep.

The family recovery test is not a device restore. It is the institution's login-recovery and death-claim process.

Verify what documents the institution requires, who can make the claim, whether a beneficiary designation exists, how long the process can take, and what happens if the institution fails.

This level trades self-custody risk for counterparty and legal-claim risk. That can be a legitimate trade when it is deliberate.

== LEVEL 2: SINGLE-SIGNATURE HARDWARE WALLET ==

Level 2 moves signing control into a hardware wallet and a compatible wallet setup.

The recovery material may be a BIP39 mnemonic, another single backup, or a supported multi-share standard. Record the actual standard rather than assuming every device uses 12 or 24 words.

The hardware wallet is replaceable. The recovery material and any required passphrase or wallet information are the durable pieces.

This is simple enough for many households to maintain well. The trade-off is concentration: one sufficient backup can authorize the wallet, and one missing required element can block recovery.

== LEVEL 3: ADDED SEPARATION ==

Level 3 adds another independent element, often a passphrase or another deliberately separated custody arrangement.

A BIP39 passphrase derives a different wallet. Every passphrase, including a typo, derives a valid wallet. That gives separation, but it also creates another thing that must be entered exactly and recovered.

A passphrase is not multisig. The mnemonic and passphrase are both required to derive that wallet, but the protocol does not enforce two independent signers.

This level only improves the plan when the new element has its own backup, its own location, and a tested family process.

== LEVEL 4: THRESHOLD SIGNING ==

Level 4 uses a threshold policy such as 2-of-3 multisig, either independently or with a collaborative provider.

Two signing keys can authorize a spend and one cannot. Losing one key can be survivable.

The keys are not the whole recovery package. The family also needs the wallet policy or descriptor, script and derivation information, and compatible software or a provider-independent recovery process.

A descriptor cannot sign, but losing the policy can make reconstruction slow, uncertain, or dependent on a provider.

Collaborative custody is only provider-independent when the client truly holds enough keys to meet the threshold, has exported the policy data, and has tested recovery in compatible software without the provider.

== COMPLEXITY CAN BECOME THE BIGGEST RISK ==

A second device, passphrase, multisig, or provider can reduce one failure and create three new ones.

More pieces mean more backups, more updates, more inheritance instructions, and more ways for the written plan to drift from reality.

A single-signature setup maintained and tested well can be safer than a multisig nobody can reconstruct.

== THE DECISION ==

Choose the level from the failure you are trying to remove and the process your household can operate.

Then write the reason in one sentence.

"We use Level 2 because we can maintain one hardware-wallet recovery process and accept the single-backup control risk."

Or:

"We use Level 4 because the amount justifies threshold signing and we have tested recovery without the provider."

== PUT IT IN ORANGE PLAN ==

Protect → Protection tier. Save the level, why it fits, and the next review trigger.

Do not put a backup, seed, passphrase, PIN, private key, descriptor, or exact storage location into Orange Plan.

== YOU ARE DONE WHEN ==

The level matches today's amount and family, the trade-off is stated honestly, and the exact setup has a recovery test appropriate to it—not merely a belief that it works.
'''),

"scripts/07-2_set-up-a-hardware-wallet-and-test-recove.md": b(r'''
TELEPROMPTER SCRIPT — segment 7.2
7.2 Set up a hardware wallet and test recovery
~9 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to set up a hardware wallet and prove the recovery path without turning the test itself into the failure.

This is the operational lesson. Use the exact manufacturer's current instructions for the device and firmware on the table.

== WHAT THE DEVICE DOES ==

A hardware wallet stores signing keys and signs transactions in an environment designed to keep those keys away from the everyday computer or phone.

The Bitcoin is not inside the device. The device is replaceable.

What recovers the wallet depends on the setup: the wallet backup, any passphrase, the address or script type, derivation information, and—for multisig—the wallet policy or descriptor.

Do not assume one mnemonic restores every wallet in every device from every manufacturer.

== START WITH A CLEAN DEVICE ==

Buy from the manufacturer or an authorized source you can verify.

Follow the official authenticity and firmware checks. Never use recovery words or a PIN supplied in the box, on a card, or by another person.

The device should generate the backup during setup. Nobody legitimate asks you to type that backup into a website, chat, support form, or ordinary computer.

== RECORD THE ACTUAL BACKUP STANDARD ==

A common BIP39 backup can contain 12, 15, 18, 21, or 24 words. Other devices can use a different or multi-share standard.

Write down what this device actually produced and which wallet it belongs to.

If a passphrase is enabled, the backup without the exact passphrase derives a different wallet. Record that fact in the no-secrets process map without putting the passphrase there.

== VERIFY THE BACKUP BEFORE MOVING A MEANINGFUL AMOUNT ==

Use this order.

First, use the manufacturer's backup-check feature when one exists. That checks the recorded backup without destroying the working setup.

Second, when practical, restore on a spare compatible device or approved recovery environment with only a small test amount at risk.

Third, use a destructive wipe-and-restore only after the backup has already been checked, the exact vendor procedure is open, and another working path or low-value test protects you from one typo becoming a loss.

The old course made wiping the only device the default first proof. That was too aggressive.

A recovery test should reduce risk, not temporarily create one live copy of everything you own.

== VERIFY THE WALLET, NOT ONLY THE WORDS ==

A successful recovery means more than the device accepting the backup.

Confirm that the recovered wallet produces the expected receive address or wallet fingerprint and can see the expected small test transaction.

For a passphrase wallet, test the exact passphrase and verify the intended wallet, because every different passphrase opens a valid but different wallet.

For multisig, confirm the wallet policy or descriptor loads and that the intended threshold combinations can sign.

== RECEIVE WITH THE TRUSTED DISPLAY ==

When receiving Bitcoin, generate the address in the wallet software and confirm the destination on the hardware device's trusted display.

Do not approve an address that appears only on the computer or phone.

This reduces common malware risk. It is not a guarantee against every device, firmware, supply-chain, or human failure, which is why the setup source and recovery process still matter.

== BACKUP STORAGE ==

Keep recovery material offline under the policy you chose.

Paper can be damaged. Metal can survive more physical hazards. Either can be copied by anyone who finds it.

Separate redundant copies so one fire, flood, theft, or household conflict does not reach all of them.

Do not photograph the backup, email it, upload it, store it in a generic note, or enter it into an AI.

A supported encrypted digital backup is a different design decision and must follow the exact wallet standard; the course default remains offline recovery material.

== PIN, PASSPHRASE, AND BACKUP ARE DIFFERENT ==

The PIN protects access to the device.

The wallet backup recreates the signing material under a compatible recovery path.

The passphrase, when used, selects a different derived wallet and must be recovered exactly.

None of those should be treated as interchangeable.

== UPDATES ==

Install firmware and wallet-software updates only from official sources and only when the recovery path is already verified.

Read the release and migration notes. Do not rush an update because an email or social post creates urgency.

== YOUR DECISION ==

Which recovery proof this setup will use: manufacturer backup check, spare-device recovery, or a carefully staged destructive restore.

== PUT IT IN ORANGE PLAN ==

Protect → Security checklist. Mark the recovery test complete only after the intended wallet was recovered and verified.

Record no secrets in the app.

== YOU ARE DONE WHEN ==

The backup standard is known, the intended wallet was independently recovered or checked, the address/policy matched, and the test did not rely on the only working copy of a meaningful balance.
'''),

"scripts/07-3_single-points-of-failure-account-hardeni.md": b(r'''
TELEPROMPTER SCRIPT — segment 7.3
7.3 Single points of failure, account hardening, and scams
~8 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to find the one failure that can still take the whole setup and harden the online accounts around it.

== FIND ONE FAILURE AT A TIME ==

A single point of failure is one person, device, backup, provider, email account, or location whose loss or compromise can stop recovery or authorize an unwanted spend.

Do not create a list of 20 theoretical risks and fix none of them.

Ask:

- What one thing can authorize everything?
- What one thing can permanently block recovery?
- What one provider can freeze or impair every custodial holding?
- What one email or phone number can reset every financial account?

Fix the largest one, test the new process, then repeat at the annual review.

== HARDEN THE EMAIL FIRST ==

The primary email is often the reset path for exchanges, brokerages, banks, cloud accounts, and the plan itself.

Use a unique password and a phishing-resistant authenticator where the provider supports one.

Passkeys and hardware security keys can be phishing-resistant when correctly deployed. Keep a backup key or recovery method in a separate location.

A time-based authenticator code is generally stronger than SMS, but a code you type into a phishing site can still be stolen in real time.

SMS is the last choice, not the standard.

== HARDEN EVERY CUSTODIAL ACCOUNT ==

For each exchange, brokerage, lender, and custodian:

- use a unique password;
- use passkey or security key when supported, otherwise a strong authenticator method;
- store recovery codes offline and separately;
- turn on withdrawal allowlists, delays, or secondary approval when available;
- review active sessions and trusted devices;
- remove old phone numbers and unused recovery methods;
- test the real account-recovery path without locking yourself out.

Provider features change. The course names the control, not a button every provider promises to have.

== RECOVERY CAN BE THE BACK DOOR ==

A strong security key does not help if support will reset the account after a weak identity check.

Ask what happens after the phone is lost, the email is inaccessible, or the owner dies.

The recovery path should not be easier to attack than the login path.

== SCAMS USE URGENCY AND AUTHORITY ==

The common scam asks you to act before you verify.

"Your wallet is compromised."

"Move the Bitcoin now."

"Enter the backup to synchronize."

"Support needs remote access."

The response is always the same.

Stop. Close the message. Navigate to the provider through a known bookmark or official channel. Verify on another device or with another person. Never reveal recovery material.

No legitimate support person needs the wallet backup, private key, passphrase, or PIN.

== PHYSICAL AND SOCIAL EXPOSURE ==

Privacy is part of custody.

The more people who know the amount, location, or exact setup, the larger the coercion and social-engineering surface.

The family needs the process. They do not all need every secret.

Public content should discuss principles and test setups, never the real household's balance, locations, device identifiers, or recovery distribution.

== YOUR DECISION ==

The largest remaining single point of failure and the one hardening action with a date.

== PUT IT IN ORANGE PLAN ==

Protect → Security checklist. Record completion status only. Keep names, secrets, backup contents, and exact storage locations off the page.

== YOU ARE DONE WHEN ==

The email and custodial accounts use the strongest practical authentication available, recovery paths are documented, and the largest remaining failure has a specific fix instead of a vague plan to be more secure.
'''),

"scripts/advanced/A7-1_advanced-custody-passphrase-multisig-collaborative.md": b(r'''
TELEPROMPTER SCRIPT — segment A7.1
A7.1 Advanced custody: passphrase, multisig, and collaborative
~15 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to compare three ways to add separation beyond a single-signature wallet: a passphrase, independent multisig, and collaborative multisig.

The goal is not maximum complexity. It is removing a specific failure without creating a recovery process your family cannot operate.

== START WITH THE TWO TESTS ==

Test one: can one person or one stolen item authorize a spend?

Test two: can one lost item or one unavailable person permanently block recovery?

A passphrase and multisig answer those tests in different ways.

== A BIP39 PASSPHRASE ==

A BIP39 passphrase is an optional string used with a compatible mnemonic backup to derive a different wallet.

It is not simply an extra recovery word appended to the list.

Every possible passphrase derives a valid wallet. A typo does not produce an error. It produces a different wallet, often one with a zero balance.

That means the exact passphrase is part of the recovery material for the intended wallet.

The mnemonic without the passphrase can still derive the standard wallet. Whether that standard wallet is empty, a decoy, or used for a small balance is a deliberate design choice—not something the protocol does automatically.

== WHAT THE PASSPHRASE BUYS ==

If the mnemonic and passphrase are stored separately, finding one does not reveal the intended passphrase wallet.

Operationally, the household can place the two elements with different people or locations.

But this is not cryptographic multisig. There are not two independent signers and there is no threshold policy enforced on-chain.

Anyone who obtains both elements can derive the wallet. Losing either can make the intended wallet unrecoverable.

== AUSTIN'S PASSPHRASE RULE ==

Austin's course rule is a long randomly generated passphrase, often seven random words, written and backed up offline.

That is an operational recommendation, not a BIP39 minimum and not a universal password rule.

Whatever method you choose, the passphrase must be generated without a human pattern, recorded exactly, kept separate from the mnemonic, backed up on its own side, and tested on the intended wallet.

Do not enter it into a password manager, AI, generic cloud note, or everyday computer merely because it is called a passphrase.

== INDEPENDENT MULTISIG ==

In a 2-of-3 multisig wallet, any two signing keys can authorize a spend and one key cannot.

That threshold can pass both tests: no single key spends, and one key can be lost.

The signing keys are only part of the recovery package.

The household also needs the wallet policy or descriptor and enough script, derivation, and key-origin information for compatible software to reconstruct the wallet.

A descriptor can reveal wallet structure, public keys, and addresses. Protect it for privacy and back it up for availability.

It cannot sign by itself.

One signing key stored with the descriptor is still one signing key in a 2-of-3 wallet. The old course incorrectly said that combination quietly created single-key control. It does not.

== WHERE THE POLICY LIVES ==

The policy or descriptor can be copied more freely than a signing secret because it cannot spend, but do not publish it.

Keep redundant copies in places the recovery team can reach. Avoid storing the only policy copy inside one hardware wallet or only with one provider.

The goal is that any intended two-key recovery team can reconstruct the wallet without guessing derivation paths or depending on one company.

== KEY DISTRIBUTION ==

A common 2-of-3 design places keys in separate failure domains.

For example:

- one key with the owner;
- one key in a separate secure location or with a trusted participant;
- one key with a collaborative provider or another independent location.

The exact people and locations are estate and threat-model decisions.

Do not put two keys, or their sufficient backups, in the same safe, household, office, or provider if the purpose is to survive that failure.

== COLLABORATIVE MULTISIG ==

Collaborative custody uses a provider for setup, policy coordination, recovery assistance, transaction review, or one signing key.

Do not assume the label guarantees provider independence.

Verify:

1. What is the actual threshold?
2. Which signing keys does the client control?
3. Can the client meet the threshold without the provider?
4. Has the client exported the wallet policy or descriptor?
5. Which compatible software can reconstruct and spend without the provider?
6. What happens if the provider disappears, is enjoined, or changes terms?
7. Can the provider delay or veto a transaction under the contract or software workflow even when it cannot sign alone?

A provider cannot move a true 2-of-3 wallet with only one key. But the practical recovery claim is only proven after the client restores the policy and signs with the client-controlled threshold outside the provider's normal interface.

== PASSphrase VERSUS MULTISIG ==

Choose a passphrase when the household wants a smaller increase in hardware and software complexity and can protect two exact recovery elements.

Choose multisig when on-chain threshold signing, loss tolerance, and distributed control justify the operational work.

Choose collaborative multisig when the household values assistance and has verified that provider independence is real rather than promised.

== TESTING ==

For a passphrase wallet:

- recover on a spare compatible setup;
- enter the exact passphrase;
- verify the intended wallet fingerprint or address;
- confirm the standard no-passphrase wallet is understood;
- test the family process without revealing both elements to one unintended person.

For multisig:

- export and restore the policy or descriptor;
- verify the intended receive address on each signing device;
- create a small test transaction;
- sign with each intended two-key combination, or at least every combination the recovery plan depends on;
- prove one key cannot complete the transaction;
- for collaborative custody, complete a provider-independent recovery test.

== THE FAMILY AND ESTATE LAYER ==

The access map names roles and process, not secrets.

The legal plan names who has authority. The key plan names who can technically sign. Those two systems must agree, but one does not replace the other.

A trustee, executor, heir, or provider holding one key does not automatically have legal control or unilateral technical control. The governing documents and full signing policy decide the result together.

== YOUR DECISION ==

Which failure you are removing and why the added complexity is worth maintaining.

== HOMEWORK ==

1. Write the two access-test answers for the proposed setup.
2. Inventory every required recovery element, including the policy or descriptor.
3. Run the exact spare-device or provider-independent recovery test.
4. Update the no-secrets custody map and legal plan so roles match the signing policy.

You are done when the setup survives the failure it was built for and the family can recover it without the vendor, without guessing, and without one unintended person holding enough to spend.
'''),

"scripts/advanced/A7-3_concentration-one-institution-one-vendor.md": b(r'''
TELEPROMPTER SCRIPT — segment A7.3
A7.3 Concentration: one institution, one vendor, one firmware
~6 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to find concentration that remains after choosing a custody level.

Custody type and concentration are different questions.

A household can use a strong institution and still have every custodial asset behind one login. It can self-custody and still have every satoshi behind one device model, one firmware family, one wallet implementation, and one recovery process.

== INSTITUTION CONCENTRATION ==

The 2022 failures showed what happens when customers become unsecured creditors, lose access, or wait through a bankruptcy process.

The lesson is not that every institution fails or that splitting money makes it self-custody.

The lesson is that one institution should not be able to freeze every asset the family needs next month.

Consider a second independent institution when:

- the custodial amount is large enough that months without access would change the plan;
- the account is part of the emergency or spending bridge;
- one provider holds every taxable, retirement, or lending relationship;
- the second institution genuinely fails in a different way.

Two accounts using the same email, phone, identity provider, bank, or underlying custodian may not be as independent as they look.

== THE COST OF ANOTHER ACCOUNT ==

Every extra account adds another password, authenticator, recovery process, tax record, beneficiary form, and executor row.

Three weak accounts can be worse than one hardened account.

Add an institution only when the reduced concentration is worth the maintenance and the family map is updated immediately.

== VENDOR CONCENTRATION IN SELF-CUSTODY ==

Self-custody removes the chosen custodian's control. It does not remove every dependency.

A hardware wallet still depends on device hardware, firmware, backup standards, wallet software, supply chain, and the user's recovery process.

Using a second vendor or implementation can reduce a correlated vendor or firmware failure.

It does not guarantee safety. A second setup that nobody understands adds human and recovery risk.

== DIFFERENT FAILURE DOMAINS ==

Diversification only helps when the second path is actually independent.

Examples:

- a hardware wallet from another manufacturer with a compatible but independently implemented recovery path;
- multisig keys from different device vendors;
- part self-custody and part institution;
- separate email, authentication, and recovery paths for custodial accounts.

The goal is not to collect devices. It is to prevent one flaw, provider, credential, household event, or process error from reaching everything.

== YOUR DECISION ==

Whether the current amount justifies a second institution or independent signing path—and whether the household can maintain it well.

== HOMEWORK ==

1. Draw every custodial and self-custody dependency.
2. Circle any one provider, credential, vendor, firmware family, or location that reaches the entire stack.
3. Decide whether to reduce that concentration or accept it deliberately.
4. Add every new account or setup to the family map the same day.

You are done when the remaining concentration is visible, deliberate, and small enough that one failure does not destroy the household plan.
'''),

"scripts/advanced/A7-4_wallet-operations-utxos-dust-and-address.md": b(r'''
TELEPROMPTER SCRIPT — segment A7.4
A7.4 Wallet operations: UTXOs, dust, consolidation, and addresses
~6 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to cover the wallet operations that matter after the hardware and recovery process are working.

== YOUR BALANCE IS A SET OF OUTPUTS ==

Bitcoin does not maintain one account balance inside the protocol.

A wallet tracks unspent transaction outputs, or UTXOs. Each incoming transaction can create one or more outputs the wallet may later spend as inputs.

When you spend, the wallet selects enough inputs to fund the payment and usually creates change back to a new wallet-controlled output.

== WHY SMALL OUTPUTS MATTER ==

Fees depend partly on how much transaction data has to be included.

Spending many small inputs can require more data than spending one larger input.

That does not mean every small UTXO is protocol dust.

Dust has a technical policy meaning tied to the cost of spending an output. Separately, an output can be economically unattractive to spend at a high fee rate even when it is not protocol dust.

The planning question is whether the fee to spend the output later would be material relative to the output.

== AUSTIN'S TRANSFER RULE ==

Austin's rule of thumb is to accumulate small exchange purchases and transfer around 0.01 to 0.02 Bitcoin at a time rather than moving every small buy immediately.

That is not a Bitcoin rule and it is not a permanent threshold.

Before using it, check:

- the current fee environment;
- the amount exposed to the exchange while waiting;
- withdrawal fees and minimums;
- whether the future spend fee would still be a rounding error;
- the household's counterparty-risk limit.

If the exchange balance becomes larger than the household is willing to expose, move it even when the threshold has not been reached.

== CONSOLIDATION ==

Consolidation spends several UTXOs to a new output controlled by the same wallet.

It can reduce the number of inputs a later transaction needs, especially when performed during a low-fee period.

It also has costs.

Combining outputs can link activity that was previously less obviously related, reducing privacy. It creates an on-chain transaction and fee now. It can also produce a larger output that becomes a more obvious target for future coin selection.

So consolidation is not automatic cleanup. It is a fee-versus-privacy decision.

Do not consolidate in an emergency, during a high-fee spike, or merely because the wallet shows many rows.

== ADDRESS USE ==

Use a fresh receive address when the wallet provides one.

Address reuse can make payments easier to link and can expose more of the wallet's activity to counterparties or observers.

The wallet should verify the receive address on the trusted hardware display before a meaningful transfer.

A descriptor or extended public key can reveal many addresses and wallet history. It cannot sign by itself, but it is privacy-sensitive and belongs in the recovery plan rather than in public notes.

== LABELS AND COIN CONTROL ==

Labeling acquisition source and purpose can help with tax records, privacy decisions, and future coin selection.

Coin control is an advanced tool. Selecting the wrong output can break the intended tax identification, combine private clusters, or create inefficient change.

Use it only when you understand the wallet's behavior and the tax record is made no later than the transaction.

== YOUR DECISION ==

The transfer threshold, whether consolidation is currently justified, and which privacy trade-off you accept.

== HOMEWORK ==

1. Open coin control or the wallet's UTXO view without changing anything.
2. Identify very small outputs, labels, and repeated addresses.
3. Estimate the fee to spend them at a normal and high fee rate.
4. Decide whether to leave them, consolidate during a low-fee period, or change the future transfer threshold.
5. Update the annual custody review with the decision.

You are done when the threshold is tied to current fees and counterparty exposure, and consolidation is treated as a privacy decision rather than housekeeping.
'''),

"lesson-text/07-1_choose-the-custody-setup-that-matches-you.md": b(r'''
# Choose the custody setup that matches your stack and family

The four custody levels are an Orange Plan framework, not a protocol or industry standard.

1. **Hardened institution:** provider account, beneficiary/death-claim path, and counterparty risk.
2. **Single-signature hardware wallet:** device plus the actual backup standard and any required wallet data.
3. **Added separation:** often a passphrase or deliberately separated setup; more recovery complexity.
4. **Threshold signing:** multisig or collaborative multisig with signing keys plus the wallet policy/descriptor and a tested provider-independent path.

Choose from the amount, dependents, failure you are removing, maintenance capacity, and family recovery ability. Complexity is a risk too.

**Complete when:** the level and trade-off are written in plain language and the exact setup has a matching recovery test.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/07-2_set-up-a-hardware-wallet-and-test-recove.md": b(r'''
# Set up a hardware wallet and test recovery

Use the exact current manufacturer instructions.

## Safe order

1. Verify source, authenticity, and official software.
2. Generate the backup on the clean device; never use supplied words or enter the backup online.
3. Record the actual backup standard. BIP39 permits 12, 15, 18, 21, or 24 words; other standards exist.
4. Use a vendor-supported backup check first when available.
5. Restore on a spare compatible device or approved environment with a small test amount.
6. Use a destructive reset only after the backup is already validated and the official procedure is open.
7. Verify the intended wallet fingerprint/address; for passphrase or multisig, verify the exact passphrase or wallet policy.
8. Confirm receive addresses on the trusted hardware display.

A backup is not universally portable to every device. Recovery may also require passphrase, script/address type, derivation information, or a multisig policy/descriptor.

**Complete when:** the intended wallet—not only a list of words—was recovered without risking the only working copy of a meaningful balance.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/07-3_single-points-of-failure-account-hardeni.md": b(r'''
# Single points of failure, account hardening, and scams

Find the one person, provider, credential, device, backup, or location that can authorize everything or permanently stop recovery.

## Authentication order

1. Passkey or hardware security key where supported, with a separate backup path.
2. Authenticator app / TOTP when a phishing-resistant option is unavailable.
3. SMS only when stronger options are not supported.

TOTP is stronger than SMS but is not phishing-resistant merely because it is an app. Review recovery codes, active sessions, withdrawal controls, and support reset procedures.

Never reveal wallet backup, private key, passphrase, or PIN. Verify urgent messages through a known official channel.

**Complete when:** the primary email and custodial accounts use the strongest practical authentication and the largest remaining failure has a dated fix.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/advanced/A7-1_advanced-custody.md": b(r'''
# Advanced custody: passphrase, multisig, and collaborative

## Passphrase

A BIP39 passphrase is an optional string that derives a different wallet. Every passphrase, including a typo, derives a valid wallet. It is not an extra mnemonic word and it is not multisig.

Austin's seven-random-word rule is an operational standard, not a protocol minimum. Store and back up the exact passphrase separately from the mnemonic and test the intended wallet.

## 2-of-3 multisig

Any two signing keys can authorize a spend; one cannot. Recovery also needs the wallet policy/descriptor or enough script, derivation, and key-origin data to reconstruct it.

A descriptor is privacy-sensitive but cannot sign. One key plus a descriptor remains one key in a 2-of-3 wallet.

## Collaborative custody

Verify the actual threshold, which keys the client controls, whether the client can meet the threshold without the provider, whether the policy is exported, compatible recovery software, and the contractual delay/veto powers.

## Complete when

The exact passphrase or intended key combinations were tested on a spare setup, the policy/descriptor was restored, provider-independent recovery was proven when claimed, and the legal roles match the signing policy.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/advanced/A7-3_concentration.md": b(r'''
# Concentration: one institution, one vendor, one firmware

Custody type and concentration are different.

- One institution can freeze every custodial asset.
- One email or phone can reset every account.
- One device vendor, firmware family, wallet implementation, or recovery process can reach an entire self-custody stack.

A second institution or vendor helps only when it fails independently and the household can maintain it. Every extra account adds authentication, tax records, beneficiaries, and executor work.

**Complete when:** the remaining concentration is mapped and either reduced or accepted deliberately.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/advanced/A7-4_wallet-operations.md": b(r'''
# Wallet operations: UTXOs, dust, consolidation, and addresses

A wallet tracks unspent transaction outputs. Spending many small inputs can require more transaction data and higher fees.

Protocol dust and an output that is merely uneconomic to spend at current fees are not the same thing.

Austin's 0.01–0.02 BTC transfer threshold is a rule of thumb, not a Bitcoin rule. Check current fees, exchange exposure, withdrawal costs, and the future spend fee.

Consolidation can reduce future input count but creates a transaction now and can link coins, reducing privacy. Use fresh receive addresses and verify the destination on the hardware display.

Coin control can affect privacy, change, fees, and tax identification. Use it only with matching records made no later than the transaction.

**Complete when:** the transfer threshold and any consolidation decision are tied to current fees, counterparty exposure, and a stated privacy trade-off.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),
}
