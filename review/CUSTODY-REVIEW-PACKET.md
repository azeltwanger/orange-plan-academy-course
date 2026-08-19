# Orange Plan Academy — custody and security review packet

**Reviewer:** experienced Bitcoin custody practitioner, wallet educator, or security professional  
**Status:** pre-filming technical and safety review

## What we need from you

Review the operational safety and accuracy of the core guidance. Do not rewrite Austin's voice or turn Core into a full wallet course.

For each item, mark:

- **ACCURATE AS WRITTEN**
- **ACCURATE WITH QUALIFICATION**
- **UNSAFE / REMOVE**
- **DEVICE- OR PROVIDER-SPECIFIC** — move exact procedure to maintained text

## Files in scope

- `scripts/07-1_choose-the-custody-setup-that-matches-you.md`
- `scripts/07-2_set-up-a-hardware-wallet-and-test-recove.md`
- `scripts/07-3_single-points-of-failure-account-hardeni.md`
- `scripts/08-2_split-access-dual-control-and-redundancy.md`
- `scripts/08-3_the-heir-letter-and-the-dead-mans-switch.md`

Matching `lesson-text/` files are the written reference.

## A · Custody-level framework

The course uses four practical levels as a teaching tool:

1. Hardened third-party account for an operating or learning balance
2. Tested single-signature hardware wallet
3. Family-ready self-custody that is not dependent on one person or location
4. Multi-key or professionally supported high-stakes design

It explicitly says the levels are not universal dollar thresholds and more complexity is not automatically safer.

Status: ______  Notes: ______

Confirm that Level 3 is correctly defined by family readiness rather than requiring a passphrase.

Status: ______  Notes: ______

## B · Hardware-wallet acquisition and authenticity

Review the guidance to:

- buy from the manufacturer or a verified authorized seller,
- reject a device supplied with prewritten recovery words,
- use official software and authenticity checks,
- independently navigate to provider support rather than follow unsolicited links.

Identify any claim that is too absolute across devices.

Status: ______  Notes: ______

## C · Backup and recovery proof

The draft no longer tells every user to wipe the only working device holding meaningful funds.

It offers:

- manufacturer-supported backup check,
- compatible spare-device restore,
- small practice wallet,
- full wipe-and-restore only when the backup has been checked, the exact process is understood, and a safe fallback exists.

Confirm this hierarchy and provide any stronger safety language.

Status: ______  Notes: ______

Confirm the standard for proving recovery: expected wallet/accounts/addresses reproduced, not merely seeing an app open.

Status: ______  Notes: ______

## D · Receive and send verification

Review the guidance to:

- verify the receiving address on the hardware-wallet display,
- verify destination, amount, and fee before signing,
- avoid trusting copied address fragments or transaction-history lookalikes,
- run a small receive and send before a meaningful transfer.

Status: ______  Notes: ______

## E · Backup compatibility

The course says different wallets and backup formats can differ and should not be assumed compatible across every device or application.

Give the minimum accurate evergreen wording without teaching one standard as universal.

Status: ______  Notes: ______

## F · Passphrase framing

Review these claims:

- exact passphrase may create a separate wallet,
- a wrong passphrase can open a different empty wallet rather than produce an obvious error,
- losing it can create permanent loss,
- backup plus passphrase behaves like a two-part recovery requirement unless redundancy is separately designed,
- a passphrase is Advanced rather than a mandatory family-ready step.

Status: ______  Notes: ______

## G · Multi-key and descriptor/configuration records

The course now states:

- a 2-of-3 wallet has three keys and any two sign,
- one key cannot spend,
- losing one key can be survivable only when the remaining keys and required wallet information are recoverable,
- a descriptor or configuration record is not a private key but can reveal addresses/balances and may be necessary to reconstruct the wallet,
- redundant protected copies are appropriate,
- provider-assisted and DIY arrangements have different recovery dependencies.

Please correct any oversimplification, especially the phrase “keys alone cannot restore” across different implementations.

Status: ______  Notes: ______

## H · Dual control and redundancy

Confirm the two-test framework:

1. Can one unauthorized person or component spend alone?
2. Can one realistic loss or unavailable person permanently stop recovery?

Confirm the warning against manually dividing an ordinary seed phrase into word fragments as an improvised threshold system.

Status: ______  Notes: ______

## I · Failure-domain review

Review the physical, human, and provider failure categories and the examples:

- device and backup in one location,
- all keys or security keys in one event domain,
- one person holding all process knowledge,
- exchange/provider access or recovery failure.

Status: ______  Notes: ______

## J · Account hardening

Review the recommended order and terminology:

- secure primary email,
- unique passwords,
- FIDO security key or properly implemented passkey when available,
- separate backup authenticator/recovery method,
- authenticator app when stronger phishing-resistant methods are unavailable,
- avoid SMS-only authentication when stronger options exist,
- carrier PIN / port-out protection,
- withdrawal allowlist, delay, address lock, session/API review where supported.

Identify provider-specific controls that should remain written reference only.

Status: ______  Notes: ______

## K · Scam guidance

Confirm the no-secrets, independently verified support, urgency, transaction-display, guaranteed-return, and “send one, receive more” warnings.

Status: ______  Notes: ______

## L · Family practice

The course recommends a small practice wallet for a spouse, executor, or trusted helper so the first recovery attempt is not the main balance after a crisis.

Confirm the benefits and any privacy or operational cautions.

Status: ______  Notes: ______

## M · Orange Plan data boundary

Standing rule:

> Orange Plan may record custody type, provider, people, process status, test date, and general document location. It never receives seed phrases, private keys, passphrases, PINs, passwords, wallet backups, or a complete spending path.

Status: ______  Notes: ______

## Reviewer sign-off

Reviewer: ____________________  
Background / organization: ____________________  
Review date: ____________________  
Wallets / custody types considered: ____________________  
Claims moved to device-specific reference: ____________________  
Unsafe claims removed: ____________________
