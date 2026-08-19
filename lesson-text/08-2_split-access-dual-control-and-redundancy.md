# Design dual control and redundancy without creating a new loss path

## Two tests

1. Dual control: can one unauthorized person or component spend alone?
2. Redundancy: can one loss permanently stop recovery?

## Custody types

- Custodial account: provider process controls
- Single signature: one complete backup can control
- Passphrase: backup and exact passphrase may both be required
- Multi-key: threshold defines how many keys sign

A 2-of-3 wallet has three keys and any two sign. Protected wallet configuration records may also be required for recovery.

## Do not split ordinary words by hand

Dividing a normal seed phrase is not a designed threshold system and can create a fragile two-part recovery.

## Separate failure domains

Review physical, human, and provider events. Do not put all required components in one place or person's control.

## Align legal and technical roles

A key does not create legal authority. An executor title does not provide a key. Coordinate roles with counsel and the custody design.

## Practice test

Confirm the authorized combination works, the design survives its claimed loss, and one person cannot spend when dual control is intended.

## Done when

The household can state which tests the design passes and has proven the process on a practice wallet.
