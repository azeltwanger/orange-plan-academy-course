# Orange Plan Academy — Bitcoin custody review packet

**Status:** pre-dictation technical review  
**Reviewer needed:** experienced Bitcoin custody practitioner who can distinguish device-specific instructions from durable custody principles  
**Scope:** hardware wallets, backups, recovery, authentication, single points of failure, family readiness, passphrases, multisig, providers, descriptors, and privacy.

## Reviewer instructions

For every claim below, mark one:

- **ACCURATE AS WRITTEN**
- **ACCURATE — ADD QUALIFICATION**
- **DEVICE / PROVIDER SPECIFIC — MOVE OUT OF EVERGREEN VIDEO**
- **UNSAFE — REPLACE**
- **ADVANCED ONLY**

Please provide corrected language and the primary technical documentation or standard you would rely on.

The course never asks a reviewer, learner, or app to receive a seed phrase, private key, passphrase, PIN, password, xprv, wallet backup, or other spending secret.

---

# A. Custody levels and risk framing

## C-01 · Custody is a trade-off, not a purity test

**File:** `scripts/07-1...`

**Current course position:** More direct control reduces some third-party risks while increasing operational responsibility. More convenience can increase provider or access risk. The appropriate setup depends on amount, job, skill, family, and consequence of failure.

**Review:** Confirm balanced wording and identify any hidden assumption that exchange custody is always temporary or self-custody is always superior.

## C-02 · Different balances can have different jobs

**Current course position:** A household may use a small operating balance at a provider, long-term cold storage, a practice wallet, and retirement-account Bitcoin under different custody arrangements.

**Review:** Confirm the teaching structure and whether “operating balance” needs a clearer limit/review rule.

## C-03 · Four practical levels

**Current course position:**

1. Hardened third-party account
2. Tested single-signature hardware wallet
3. Family-ready self-custody
4. Multi-key or professionally supported design

**Review:** These are educational levels, not an industry standard. Confirm the distinctions and identify language that could imply one universal dollar threshold.

## C-04 · Family-ready does not require one specific technology

**Current course position:** A carefully designed single-signature setup can be family-ready when backups, people, locations, and tests are adequate. Passphrase or multisig is not automatically safer when the family cannot operate it.

**Review:** Confirm and define the minimum evidence that justifies the phrase “family-ready.”

---

# B. No-secrets documentation

## C-05 · Process, never secrets

**Files:** Modules 0, 7, and 8

**Current course position:** Orange Plan, the Family Custody Map, heir letter, executor packet, email, cloud storage, photos, and AI never receive seed phrases, private keys, passphrases, PINs, passwords, or wallet backups.

**Review:** Confirm and identify whether any normal process document should ever include an xpub, descriptor, wallet name, fingerprint, derivation information, or address.

## C-06 · General locations and people

**Current course position:** A map can state that a backup exists in a protected off-site location and identify who understands the process without revealing the access combination or secret.

**Review:** Confirm privacy and coercion concerns and recommend safe granularity.

## C-07 · Compromised backup

**Current course position:** A seed phrase or private key entered into a website, AI, photo, cloud note, or unsolicited support process should be treated as exposed and funds should be moved to a newly generated secure wallet using a verified process.

**Review:** Confirm and add the safest emergency sequence without creating a panic-driven mistake.

---

# C. Hardware-wallet setup and operation

## C-08 · Buy and verify the device

**File:** `scripts/07-2...`

**Current course position:** Buy from the manufacturer or a verified authorized seller when supported; inspect the device/package and use the official authenticity/firmware process. Never use a prewritten seed or already-created wallet.

**Review:** Confirm what is durable versus manufacturer-specific and whether third-party retail wording is too broad.

## C-09 · Device versus backup

**Current course position:** The device is replaceable; the wallet backup and any required passphrase recreate the wallet. A PIN protects the physical device but is not a substitute for the backup.

**Review:** Confirm wording across BIP39, SLIP39, SeedQR, device-specific secure elements, and non-BIP39 backup systems. Recommend a generic term if “seed phrase” is too narrow.

## C-10 · Backup compatibility

**Current course position:** Different wallets use different backup standards; the learner should not assume a backup works on every other device or software.

**Review:** Confirm and identify the minimum compatibility information a family should record without exposing secrets.

## C-11 · Passphrase behavior

**Current course position:** An exact passphrase can produce a separate wallet; a wrong passphrase may open another empty wallet rather than an obvious error. A forgotten passphrase can permanently lose access. Passphrases belong in Advanced unless fully understood and tested.

**Review:** Confirm wording and identify device-specific exceptions.

## C-12 · Trusted-display address verification

**Current course position:** Before receiving or signing, verify the address, amount, and fee on the hardware-wallet display. Do not trust only the connected computer or a copied recent address.

**Review:** Confirm full-address versus sampled-character guidance and address-poisoning/clipboard-attack language.

## C-13 · Small receive and send test

**Current course position:** A complete operating test includes receiving a small amount and sending a small amount back out while verifying the transaction on the device.

**Review:** Confirm and identify any privacy, fee, change-output, UTXO, or account-discovery issue that belongs in the core or Advanced.

## C-14 · Safe recovery test

**Current course position:** Use the manufacturer's backup-check feature, a compatible spare device, or another supported recovery drill. Do not tell a learner to wipe the only working device holding meaningful funds unless the backup has already been checked, the process is understood, and a safe fallback exists.

**Review:** High priority. Confirm this is a safe generic standard and recommend exact wording for devices whose backup-check procedure differs.

## C-15 · Successful recovery evidence

**Current course position:** A restored app opening is not enough. The recovered wallet should reproduce the expected account/address structure or another manufacturer-supported verification.

**Review:** Confirm and explain how to avoid address reuse, privacy leaks, or mistaken empty-account paths.

## C-16 · Firmware and software updates

**Current course position:** Use official software, verify the source, keep the backup current, and avoid urgent unsolicited update prompts. The course does not tell learners to install every update immediately or never update.

**Review:** Recommend durable wording and what belongs only in current device walkthroughs.

---

# D. Backup storage and failure domains

## C-17 · Device and backup in one location

**File:** `scripts/07-3...`

**Current course position:** Two components exposed to the same fire, flood, theft, move, or coercion are one failure domain even when there are two physical objects.

**Review:** Confirm and identify the most useful core examples.

## C-18 · Paper and metal

**Current course position:** Paper can be valid in some situations but is vulnerable to water, fire, fading, and handling. Metal reduces some physical risks but does not solve theft, discovery, or family process.

**Review:** Confirm neutral wording and avoid implying one commercial product is required.

## C-19 · More backups create more access paths

**Current course position:** Redundancy and theft risk must be balanced. Scattering complete backups is not automatically safer.

**Review:** Confirm and identify coercion/privacy considerations.

## C-20 · Backup of authenticators

**Current course position:** Security keys, passkeys, authenticator apps, backup codes, and account-recovery methods also need a separate failure-domain plan so hardening does not create lockout.

**Review:** Confirm operational standard.

---

# E. Account hardening and phishing resistance

## C-21 · Secure email first

**Current course position:** Email is often part of the reset/recovery chain for exchanges, brokers, banks, and other accounts, so primary email is hardened before downstream accounts.

**Review:** Confirm and identify any provider-specific exception.

## C-22 · Security keys and passkeys

**Current course position:** FIDO security keys and properly implemented passkeys can provide phishing-resistant authentication because the credential is bound to the legitimate service.

**Review:** Confirm terminology and recommend wording that does not imply all passkeys, sync models, or recovery designs are identical.

## C-23 · Authenticator apps versus SMS

**Current course position:** When phishing-resistant authentication is unavailable, an authenticator app is generally stronger than SMS-only authentication. Manually entered one-time codes can still be phished.

**Review:** Confirm and identify the place for backup/sync guidance.

## C-24 · SIM-swap protections

**Current course position:** Protect the carrier account with available account PIN, port-out lock, or transfer protection; do not rely on SMS as the only factor when stronger methods exist.

**Review:** Confirm.

## C-25 · Exchange controls

**Current course position:** Use withdrawal allowlists, delays, address locks, alerts, session/device review, API-key review, and account freezes when the provider offers them and the household understands recovery.

**Review:** Identify which controls are durable core concepts and which should stay in provider-specific reference material.

## C-26 · Unsolicited support and urgency

**Current course position:** Legitimate support does not need a wallet backup or one-time authentication code. Stop unsolicited contact and reach the provider through an independently found channel. Urgency is a major attack signal.

**Review:** Confirm and add any essential remote-access or screen-sharing warning.

---

# F. Dual control, redundancy, passphrases, and multisig

## C-27 · Dual control and redundancy are separate

**File:** `scripts/08-2...`

**Current course position:** Dual control asks whether one person/component can spend alone. Redundancy asks whether one loss permanently stops recovery. A design can pass one and fail the other.

**Review:** Confirm.

## C-28 · Do not hand-split ordinary backup words

**Current course position:** Dividing an ordinary wallet backup into fragments is not a designed threshold system and can create a fragile two-part requirement. Use a supported scheme or multi-key design.

**Review:** Confirm and identify whether Shamir/SLIP39 should be named only in Advanced.

## C-29 · 2-of-3 arithmetic

**Current course position:** A 2-of-3 wallet has three keys and any two can sign; losing one key is survivable only when the remaining keys and required wallet configuration are recoverable.

**Review:** Confirm.

## C-30 · Configuration, descriptors, and xpub privacy

**Current course position:** Non-secret wallet configuration may be required to reconstruct/monitor a multisig wallet. It is not a private key but can reveal addresses and balances. Keep redundant protected copies.

**Review:** Supply precise generic wording across wallet coordinators and identify what the estate map should record.

## C-31 · Provider-assisted multisig

**Current course position:** Collaborative custody can reduce some one-key risks while adding provider, software, fee, privacy, succession, and recovery dependencies. The household must know whether it can recover without the provider.

**Review:** Confirm and list the questions the Advanced lesson must ask.

## C-32 · DIY multisig

**Current course position:** DIY multisig is Advanced. Core does not teach setup. It requires tested key replacement, configuration recovery, geographic distribution, software compatibility, inheritance coordination, and ongoing maintenance.

**Review:** Confirm the gate and any missing failure mode.

---

# G. Family and estate readiness

## C-33 · Practice wallet

**Current course position:** Another required person learns the process with a small practice wallet rather than the main backup. The person should be able to explain the first steps and complete the intended test under supervision.

**Review:** Confirm and recommend a practical test scope.

## C-34 · Key possession versus legal authority

**Current course position:** A person may technically possess a spending path without legal authority, or hold legal authority without a key. Custody and estate design must align.

**Review:** Confirm the technical side and flag legal wording for attorney review.

## C-35 · Protect readiness versus proof

**Current course position:** Orange Plan can record custody type, people, documents, and test dates. It cannot prove that a backup works or the family can recover. The real-world test is separate evidence.

**Review:** Confirm the minimum completion evidence the app/course should require.

---

# Reviewer summary

Please return:

1. Claim ID → status → replacement wording.
2. Claims safe for evergreen video.
3. Claims that must remain device/provider-specific lesson text or walkthrough.
4. Claims that should move entirely to Advanced.
5. A minimum family-ready custody checklist.
6. Any dangerous omission or unsafe sequence in the current core lessons.

Austin will perform his final voice review only after accepted custody changes are applied to both script and lesson text.
