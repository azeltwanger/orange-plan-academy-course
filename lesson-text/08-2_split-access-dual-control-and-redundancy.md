# Design dual control and redundancy without creating a new loss path

Use two separate tests:

1. **Dual control:** can one person or component spend alone when the design says it should not?
2. **Redundancy:** can one loss or unavailable person permanently stop recovery?

Passing one test does not automatically pass the other.

## Match the design to the custody type

- **Custodial account:** provider authentication, beneficiary, and death-claim procedures control
- **Single-signature wallet:** one complete device or backup can control; physical and family controls do not create cryptographic dual control
- **Passphrase wallet:** backup and exact passphrase may both be required; each needs a recovery plan
- **Multi-key wallet:** threshold rules determine how many keys are required

A 2-of-3 wallet has three keys and any two can sign. It may also require a non-secret wallet configuration or descriptor for recovery. Keep redundant protected copies of that record without treating it as a private key.

## Do not split ordinary seed words by hand

Dividing one wallet backup into fragments is not a designed threshold system. It can create a fragile two-part recovery where loss of either fragment stops recovery.

Use a supported custody method for the control you want.

## Separate failure domains

Do not store all required keys, backups, descriptors, or instructions in one place or under one person's control.

Review physical, human, and provider failures.

## Align legal and technical roles

A key does not create legal authority. An executor title does not provide a key.

The attorney and custody professional should coordinate component holders, heirs, executor, provider, and legal process.

## Test with a practice wallet

Confirm:

- The intended authorized combination works
- The design survives the loss it claims to survive
- One person cannot spend when dual control is intended
- Provider-assisted recovery has a known process and fallback

## Done when

The household can state which tests the design passes, the components are separated across failure domains, and a practice recovery proves the process.
