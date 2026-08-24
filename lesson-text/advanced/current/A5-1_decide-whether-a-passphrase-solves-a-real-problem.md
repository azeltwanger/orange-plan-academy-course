# Decide whether a passphrase solves a real problem

> **Watch this only when a tested single-signature wallet still has a specific problem a passphrase may solve.**

## What it does

Backup words plus an exact passphrase derive a wallet. A different passphrase can derive another valid wallet rather than produce an obvious error.

The passphrase can protect against discovery of the backup words and can also permanently lock out the family when it is missing.

## Worked example

- Backup words are discovered: a passphrase may keep the main wallet hidden.
- Owner dies and passphrase is missing: the family can restore an empty wallet and have no recovery path.

The control changes one required secret into at least two required components.

## Rules

- Do not use memory as the only backup.
- Use a supported sufficiently random method.
- Preserve the exact value offline.
- Separate the components without creating one fragile copy of each.
- Coordinate legal authority separately from key possession.

## Practice first

A small practice wallet should prove:

1. backup-only wallet,
2. exact passphrase wallet,
3. receive and send,
4. clean-device recovery,
5. family process without secrets in the instructions.

## Done when

The household can name the risk solved, the new failure created, and has recovered the practice wallet through the full process.
