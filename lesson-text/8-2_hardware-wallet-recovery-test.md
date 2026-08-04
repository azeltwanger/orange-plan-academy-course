# The hardware wallet and the recovery test

**Your Bitcoin isn't on the device.** The seed phrase (12/24 words) is what everything derives from; the device is just a safe place to use it. The device is replaceable, the seed is not, and most devices wipe themselves after wrong PIN attempts, so your whole stack effectively lives on the backup.

## The six-step setup

1. Buy direct from the manufacturer. Never used, never third-party.
2. Generate a brand-new wallet on the device itself.
3. Write the seed offline; set a PIN.
4. Send a small test transaction (~0.01 BTC).
5. **Wipe the device on purpose**: with the test money on it. This is where most people stop short.
6. Restore from your written seed; confirm the transaction reappears.

The wipe proves three things at once: the seed was written right, you know the procedure under calm conditions, and the backup works. If it fails, you found out with $1,000 at risk, not $150,000.

## The never list

The seed exists on paper or steel, offline, nowhere else. Nothing with a screen and a connection. For a meaningful stack: steel, in separate locations.

## Moving coin well: UTXOs

Each transfer in creates a **UTXO**: a separate bill in your wallet. You spend whole bills, and fees scale with *how many* bills, not their value, so many small UTXOs (dust) raise your future cost of moving your own coin.

- **Sweep on a threshold, not a schedule:** ~0.01–0.02 BTC minimum per transfer; accumulate on the exchange until then.
- Already dusty? **Consolidate** small pieces into one when fees are low. Annual maintenance, not an emergency.

## Homework

1. Never done the wipe-and-restore? Watch the demo lesson and do it with a small amount before serious money is on the line.
2. Set your sweep threshold if your buys trickle in small.
