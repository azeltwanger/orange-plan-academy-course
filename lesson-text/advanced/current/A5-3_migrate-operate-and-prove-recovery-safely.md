# Migrate, operate, and prove recovery safely

> **Watch this only when changing custody or taking over an advanced wallet.**

## Define the destination

Record wallet type, threshold, devices, software, component holders, configuration records, locations, roles, and claimed failure tolerance—without secrets.

## Practice first

A small wallet should prove:

- receiving-address verification,
- intended signing combination,
- alternate authorized combination,
- no one-key spending when intended,
- reconstruction from backups/configuration,
- and family process.

## Staged migration

1. Practice wallet
2. Small live tranche
3. Verified spend from destination
4. Staged remaining transfer
5. Family recovery practice
6. Custody-map update

Do not move the entire 1.50 BTC first or destroy the old backup until every dependent wallet/account is confirmed empty and retired safely.

## Address and UTXO review

Verify destination and transaction details on trusted devices. Review output size, fees, privacy, future spending, and coin control before consolidating.

## Changes require retesting

A new device, key, passphrase, coordinator, provider, or threshold requires updated recovery and family tests.

## Done when

The destination receives and spends, survives its claimed failure, reconstructs from backups, completes the migration, and passes the family test.
