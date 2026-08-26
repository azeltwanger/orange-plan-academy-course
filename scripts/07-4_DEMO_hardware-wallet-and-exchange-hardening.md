# 7.4 · DEMO — Hardware-wallet recovery and exchange hardening

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
