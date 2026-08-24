TELEPROMPTER SCRIPT — Advanced A5.3
A5.3 Migrate, operate, and prove recovery safely
~9 min at 155 wpm · VOICE-MATCHED DRAFT — Austin review + custody/device review pending
============================================================

> **Watch this only if you are changing wallets, adding a passphrase, moving into multisig, replacing keys, or taking over an existing advanced setup. Otherwise do not move the main balance.**

The most dangerous moment in a custody upgrade is often the migration.

The question is: **how do we prove the destination works, move the balance without one irreversible leap, and leave the family with a process it has actually tested?**

== DEFINE THE END STATE BEFORE MOVING A SATOSHI ==

Write down, at a process level:

- wallet type and threshold,
- device and software versions,
- key or component holders,
- configuration or descriptor records,
- backup locations,
- family and provider roles,
- and the failures the design claims to survive.

Do not write seed phrases, private keys, passphrases, xprvs, PINs, passwords, or complete spending secrets.

If the end state cannot be explained without opening every secret, the process is not ready.

== BUILD A PRACTICE WALLET WITH THE SAME DESIGN ==

A practice wallet should use the same type of devices, threshold, coordinator, and recovery method as the intended setup.

Fund it with a small amount.

Then prove:

1. Each receiving address is verified on the trusted device displays required by the design.
2. The intended signing combination can spend.
3. A different authorized combination can spend when redundancy is claimed.
4. One key or component alone cannot spend when dual control is intended.
5. The wallet can be reconstructed from the protected backups and configuration.
6. The family or successor can begin the process without the main owner improvising.

A green balance in one coordinator application does not prove recovery.

== WORK THE DEMO MIGRATION ==

The demo household plans to move 1.50 BTC from a tested single-signature hardware wallet into a supported 2-of-3 design.

Do not send 1.50 BTC in the first transaction.

### Stage 1 — practice

Create the small 2-of-3 practice wallet. Receive a small amount, complete a spend, remove one key from the test, and prove the two remaining authorized keys plus the configuration can reconstruct and spend.

### Stage 2 — small live tranche

Generate a fresh destination address and verify it using the devices and coordinator required by the new setup.

Send a small live tranche from the old wallet. Wait for confirmation. Verify the balance through more than one trusted view when the design supports it. Then spend a small portion from the destination using the intended signing process.

### Stage 3 — staged balance transfer

Move the remaining Bitcoin in more than one deliberate tranche when the fee and privacy trade-off support that choice.

After each tranche, verify the transaction ID, destination, confirmations, and new wallet balance.

Do not destroy the old backup or device merely because the sending balance appears near zero. Confirm no remaining accounts, change outputs, hidden passphrase wallet, or other assets still depend on it.

### Stage 4 — family recovery

Have Jordan or the named backup person use the process-level instructions and practice wallet to prove the family handoff. The main 1.50 BTC secrets remain protected.

Only then update the custody map and mark the migration complete.

== ADDRESS AND TRANSACTION VERIFICATION ==

Malware and bad interfaces can replace a copied address.

Verify the destination on the trusted device display or displays required by the setup, not only on the connected computer or phone.

Review the amount, fee, destination, change behavior, and signing devices before approval.

Use a new receiving address according to the wallet's supported process rather than copying one from old transaction history.

== UTXO AND PRIVACY TRADE-OFFS ==

The wallet may contain several separate outputs.

Consolidating them can reduce future transaction overhead and can also link them together on-chain, reveal ownership relationships, and create one larger output with its own risk.

Leaving many tiny outputs can create high fee friction or make them uneconomic to spend later.

This course does not prescribe one consolidation policy.

Review:

- current fees,
- number and size of outputs,
- privacy history,
- future spending pattern,
- and the coordinator's coin-control capability.

When the amount or privacy consequence matters, use a qualified custody/privacy practitioner rather than clicking “consolidate all.”

== KEY REPLACEMENT REQUIRES A NEW TEST ==

A failed or compromised key is not fixed by making another copy of the same potentially exposed secret.

The supported process may require replacing a key and migrating to a new wallet configuration.

After any device, key, passphrase, coordinator, threshold, or provider change, rerun the recovery and family test and update every non-secret process record.

== RECORD EVIDENCE, NOT SECRETS ==

Keep:

- wallet type and threshold,
- device and software names,
- configuration checksum or protected location when appropriate,
- transaction IDs for migration,
- test date and successful combinations,
- people who participated,
- and the next review date.

Do not store the secret material in Orange Plan or the test log.

== YOUR DECISION ==

Approve the destination design, migration stages, address-verification method, recovery combinations, and family test before moving the main balance.

== PUT IT IN ORANGE PLAN ==

Keep the old custody record active until the migration is verified. Then update the holding location, custody type, people, configuration process, test date, and single-point-of-failure review.

== YOU ARE DONE WHEN ==

The destination wallet has received and spent a small amount, survived the failure it claims to survive, reconstructed from backups, completed the staged migration, and passed a family practice without exposing the main secrets.

**Return to Core:** update Protect and the estate handoff, then schedule the next recovery review.
