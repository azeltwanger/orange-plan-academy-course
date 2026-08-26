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

What recovers the wallet depends on the setup. That can include the wallet backup, a passphrase, the address or script type, derivation information, and the wallet policy or descriptor if you use multisig.

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

I would test it in this order.

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

Do not record any seed words, passphrases, PINs, private keys, or backup contents in the app.

== YOU ARE DONE WHEN ==

The backup standard is known, the intended wallet was independently recovered or checked, the address/policy matched, and the test did not rely on the only working copy of a meaningful balance.
