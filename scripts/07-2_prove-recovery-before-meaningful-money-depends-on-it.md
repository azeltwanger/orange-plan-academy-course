# 7.2 — Prove recovery before meaningful money depends on it

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/sessions/07-custody.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: teach
Gate: DEVICE_CAPTURE
Sources: CUSTODY, DICTATION, PRIMARY

### Read aloud

A backup becomes useful when you know what it restores and have proved the process. The first recovery attempt should happen under calm conditions, using a small test arrangement rather than the family's only funded wallet.

A hardware wallet is a signing device. Your Bitcoin is recorded on the network; the device protects the information used to authorize transactions. Losing the device can be recoverable when the correct backup and required wallet information remain available. Losing the only usable recovery material can be a very different problem.

Obtain the device through the manufacturer's verified channel or an explicitly authorized source, and follow the current authenticity and setup instructions for that model. Generate your own new wallet through the supported process. Treat a device supplied with prewritten recovery words as compromised.

Identify the backup standard being used. Different devices and wallet configurations can require different information. A word count alone does not establish universal compatibility. A passphrase, a special recovery scheme, an account derivation, or a multisig policy can add requirements beyond the words someone wrote down.

Protect the backup offline using an appropriate physical method. Paper and durable metal have different resistance to fire, water, and deterioration. More copies may improve availability while increasing exposure to theft. Placement should be chosen around the failures you are trying to survive, and sensitive locations belong in a separate protected recovery process.

Use a small test transaction and verify the receiving address through the device's trusted display where the supported process provides it. A computer screen can be misleading if the computer or interface is compromised. Transaction details need independent attention before approval.

Then validate the backup through the device's supported backup-check function or a recovery on a compatible spare device. Confirm the expected wallet and test balance. Where a reset-and-restore demonstration is appropriate, perform it only after backup validation and only in a controlled test setup. Never wipe the only working device protecting meaningful funds simply because a generic course checklist says reset next.

A passphrase requires special care. It is an additional exact input that can create a different wallet. A mistyped passphrase may open a valid but empty wallet rather than produce an obvious error. The device PIN protects access to the device; it is not a substitute for the recovery backup or passphrase.

For multisig, test the intended signing threshold and retain the wallet policy or configuration information needed for recovery. Having enough seed backups is not automatically proof that heirs can reconstruct the correct wallet. The recovery plan must include compatible tools and the information required by that particular setup.

For Alex and Morgan, the direct-custody pool remains a documented open action until the test succeeds. The account can be listed in Orange Plan without pretending recovery is proven. Once the test is complete, they record that it was tested and the next review date, while the secret material stays outside the financial-planning app.

The separate device demonstration shows this process on the exact hardware, firmware, and backup method used for filming. Follow the official instructions for your own setup. Stop when a step differs materially from what is shown rather than improvising with funded assets.

You are finished when you have verified what information is required, proved recovery using the safe test procedure, and made the process maintainable. Buying a device and writing down words are preparation. The evidence that matters is a successful recovery of the intended wallet.

### Production notes

D07 exact-device gate: official instructions, authenticity, backup standard, firmware, spare-device/backup check, test-only funds, address verification, reset safety, and recovery proof. Never display usable real or demo seed phrases in distributable course footage; mask/cut secrets rather than teaching from a reusable public funded wallet. Vendor procedures must be freshly checked.

### Member checkpoint

- Identify the complete recovery information for the actual setup.
- Validate the backup before any destructive test.
- Record a successful small-value recovery and the next review date.
