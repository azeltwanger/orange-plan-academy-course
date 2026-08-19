# Orange Plan Academy — Bitcoin custody review packet

**Purpose:** verify the custody and recovery guidance in the core course without asking the reviewer to evaluate the entire Academy.  
**Reviewer output:** mark each item **accurate**, **qualify**, or **remove / replace**, with product-neutral replacement wording where needed.

The course should teach durable security principles. Exact device screens, backup formats, firmware procedures, provider processes, and compatibility details belong in maintained lesson text or versioned demos.

## Files in scope

### Primary

- `scripts/07-1_choose-the-custody-setup-that-matches-you.md`
- `lesson-text/07-1_choose-the-custody-setup-that-matches-you.md`
- `scripts/07-2_set-up-a-hardware-wallet-and-test-recove.md`
- `lesson-text/07-2_set-up-a-hardware-wallet-and-test-recove.md`
- `scripts/07-3_single-points-of-failure-account-hardeni.md`
- `lesson-text/07-3_single-points-of-failure-account-hardeni.md`
- `scripts/08-2_split-access-dual-control-and-redundancy.md`
- `lesson-text/08-2_split-access-dual-control-and-redundancy.md`

### Secondary

- `scripts/00-2_how-the-ai-works-what-it-reads-what-it-n.md`
- `scripts/08-1_the-executor-the-four-legal-documents-an.md`
- `scripts/08-3_the-heir-letter-and-the-dead-mans-switch.md`
- Custody sections of `DEMO-HOUSEHOLD.md`

## Review standard

For each claim, tell us:

1. Is it technically accurate across common modern wallets and providers?
2. What device- or provider-specific exception requires qualification?
3. Is the instruction safe for a novice following it literally?
4. Does it accidentally create a new single point of loss or theft?
5. Does it belong in evergreen video, maintained lesson text, a versioned demo, or Advanced?

## A. Custody-level framework

Review the four educational levels:

1. Hardened third-party account for a small operating, learning, or temporary balance.
2. Tested single-signature hardware wallet.
3. Family-ready self-custody that no longer depends on one person or one failure domain.
4. Multi-key or professionally supported design for a high-stakes or complex situation.

The course explicitly says the levels are not a universal dollar threshold or ideological ranking. Confirm that the framework:

- Does not imply an exchange is safe merely because the balance is small.
- Does not imply self-custody is complete merely because a device was purchased.
- Does not imply multisig is safer when the household cannot operate it.
- Appropriately considers amount, job, skill, family dependence, liquidity needs, and provider risk.

## B. Hardware-wallet purchase and verification

Please review the product-neutral guidance to:

- Buy from the manufacturer or a verified authorized seller when supported.
- Inspect packaging and use the manufacturer’s authenticity / firmware-verification process.
- Reject a device that arrives with a prewritten backup or already-created wallet.
- Obtain software, firmware, and support links through independently verified official channels.
- Stop when the setup differs from the manufacturer’s current documentation.

Flag any wording that overstates the value of packaging seals or implies one verification method works for every manufacturer.

## C. Wallet generation, backup, PIN, and passphrase

Review the distinctions among:

- Device-generated wallet.
- Wallet backup / recovery words or other backup format.
- Device PIN or local unlock method.
- Optional passphrase creating or selecting a different wallet.
- Private keys and signing.

Confirm the course should say:

- The PIN protects the device and does not replace the wallet backup.
- The exact backup and any passphrase may both be required.
- A wrong passphrase can open a different valid wallet rather than displaying an obvious error.
- Backup standards and compatibility vary; students should not assume every backup restores on every wallet or application.
- No backup, private key, passphrase, PIN, or password goes into Orange Plan, a document, photo, cloud note, support chat, or AI tool.

Identify nuances around SLIP-39, BIP39, seedless or server-assisted recovery, wallet-specific backup formats, and when those belong only in a device-specific demo.

## D. Receive and send verification

Review the instruction to:

- Display a receiving address on the hardware wallet’s trusted display.
- Compare the device-displayed address with the sending application.
- Verify destination, amount, and fee on the trusted display before signing a send.
- Reject any mismatch.
- Avoid trusting a copied address based only on a few characters or transaction-history lookalikes.

Please qualify what “check the full address” should mean in a realistic novice process and how address poisoning, clipboard malware, and change addresses should be explained without creating false confidence.

## E. Small test transaction

The course recommends a small receive and send before moving the meaningful balance.

Please review:

- Whether the amount should remain non-prescriptive.
- Confirmation / fee considerations.
- Whether a test send back to a controlled destination is appropriate.
- UTXO and privacy effects.
- Avoiding many tiny withdrawals from an exchange.

The Core should teach the purpose of the test, while UTXO management and coin control can remain Advanced.

## F. Backup and recovery testing

The repaired course deliberately removed a universal instruction to wipe the only device holding meaningful funds.

It now recommends one of:

- Manufacturer-supported backup check.
- Compatible spare-device restore.
- A small practice wallet.
- Another documented recovery drill supported by the wallet.

A full wipe-and-restore is presented only when the backup is already verified, the process is understood, and a safe fallback exists.

Please review:

- Whether this is safe enough for a novice.
- What evidence proves the correct wallet was recovered.
- Whether matching expected accounts and addresses is an appropriate check.
- How passphrases, derivation paths, account indexes, descriptors, multisig configuration, and wallet software can create a false “empty wallet” result.
- Whether the course should recommend professional assistance before testing a life-changing balance.

## G. Physical backups and failure domains

Review the guidance that:

- Device and backup in one location can be lost together.
- Two copies in the same failure domain are not meaningful redundancy.
- Metal can reduce fire / water risk but does not solve theft, discovery, or family access.
- Backup locations should be selected against realistic physical, legal, privacy, and access risks.
- Multi-key components should not all share one location or one person’s control.

Avoid giving burglars or coercers a blueprint. The course should teach the design questions without prescribing a public storage layout.

## H. Single signature, passphrase, and multisig

Please verify these core statements:

- A complete single-signature backup can control the wallet; family or legal procedures around it do not create cryptographic dual control.
- An improvised split of ordinary seed words is not a threshold scheme and can create fragile two-part loss risk.
- A passphrase split can require two components but does not automatically create redundancy.
- A 2-of-3 multisig contains three keys and any two can sign.
- A multisig recovery may also need a non-secret descriptor or wallet configuration.
- A descriptor is not a private key but can reveal addresses, transaction history, and balances, so protected redundant copies are appropriate.
- Collaborative custody reduces some risks while adding provider, software, policy, privacy, and inheritance dependencies.

Detailed construction belongs in Advanced. Core should help the household identify whether the current design passes the dual-control and redundancy tests.

## I. Practice wallet and family training

Review the recommendation to use a small practice wallet so a spouse, executor, or trusted helper can learn:

- Device versus backup.
- Provider versus self-custody.
- Receive, restore, and sign sequence.
- What never to share.
- Where the real process begins.

The practice should not expose the primary wallet backup or train someone on a fake process that does not resemble the real custody design.

## J. Account hardening

Review the current order:

1. Secure primary email and recovery channels.
2. Use unique passwords and a reputable password manager when appropriate.
3. Prefer phishing-resistant FIDO security keys or properly implemented passkeys when supported.
4. Maintain a separate backup authenticator / recovery method.
5. Prefer authenticator apps over SMS-only authentication when stronger methods are unavailable.
6. Add carrier PIN, port-out protection, or transfer lock.
7. Enable provider withdrawal allowlists, address locks, delays, alerts, freezes, or session review when supported.
8. Review API keys, authorized devices, linked accounts, and recovery contacts.

Please identify any wording that overpromises that hardware security keys “remove phishing entirely,” ignores account-recovery bypasses, or mishandles synced passkeys and authenticator backups.

## K. Scam and support rules

Verify the course’s stop signs:

- No legitimate support person needs the wallet backup, seed phrase, private key, passphrase, PIN, password, or one-time authentication code.
- Treat unsolicited contact as hostile until independently verified.
- Do not move funds to a “safe wallet” supplied by a caller or message.
- Verify transactions on the trusted display.
- Guaranteed returns and “send Bitcoin to receive more” are scams.
- Urgency is a reason to stop and verify rather than act faster.

Add any high-frequency failure mode the core lesson is missing without turning the course into an exhaustive scam catalog.

## L. App and documentation boundary

Review the rule that Orange Plan may track:

- Custody type.
- Provider or general process location.
- People and roles.
- Recovery-test date.
- Readiness checklist.
- Family Custody Map and process-document locations.

It never receives:

- Wallet backups.
- Seed phrases.
- Private keys.
- Passphrases.
- PINs.
- Passwords.
- Safe combinations.
- Full recovery instructions that assemble a spending path.

Please identify whether xpubs, descriptors, wallet fingerprints, addresses, or transaction IDs need an explicit privacy note in Core or a maintained help article.

## M. Demo-household review

The demo begins with:

- 1.50 BTC on one hardware-wallet setup.
- 0.25 BTC at one exchange.
- Device and only backup exposed to one home.
- Only one spouse having operated the wallet.
- No completed recovery test or current family map.

By the end of Core, the household should have:

- A verified hardware-wallet process.
- Safe backup or recovery proof.
- Separate failure domains.
- A spouse who completed a practice process.
- Hardened email and exchange accounts with backup authentication.
- A no-secrets map.
- A deliberate decision whether the current single-signature design remains appropriate or whether professional multi-key support is warranted.

Confirm that this is a safe and realistic core completion standard.

## Requested deliverable

Return a table:

| ID | File / section | Status | Technical risk or exception | Replacement wording | Evergreen / maintained / demo / Advanced |
|---|---|---|---|---|---|

Also provide:

- Product-neutral claims safe for evergreen video.
- Device- or provider-specific claims that require maintained text.
- Claims that should move to Advanced.
- A one-page pre-flight checklist for filming the hardware-wallet demo.

Do not request, inspect, or receive any real wallet backup, private key, passphrase, PIN, password, address map, or signing material.
