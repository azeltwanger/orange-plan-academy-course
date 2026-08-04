TELEPROMPTER SCRIPT — segment 8.2
8.2 The hardware wallet and the recovery test
624 words · ~4.0 min at 155 wpm
============================================================

A seed backup is only as good as your ability to actually restore from it. This lesson walks through the setup, then the recovery test that proves the backup works before serious money depends on it.

== WHERE YOUR BITCOIN ACTUALLY LIVES ==

Your Bitcoin isn't on the device. When you set up a hardware wallet, it generates a seed phrase (12 or 24 words), and every key to your Bitcoin is derived from those words. The device is a safe place to use them.

- The device is replaceable.
- The seed is not.

If the device breaks, you rebuild the wallet on a new device from the seed. If the seed is wrong, a broken device is the end of the stack.

Most hardware wallets wipe themselves after a set number of wrong PIN entries. Right feature (stops a thief guessing their way in). Also means your entire stack lives on the paper backup. The device can erase itself on a Tuesday afternoon, and that paper becomes the only copy.

== THE SIX-STEP SETUP ==

1. Buy the device directly from the manufacturer. Never used, never third-party. A device someone else touched can arrive with a seed they already know.
2. Generate a brand-new wallet on the device itself. The seed is created by the device and has never existed anywhere else.
3. Write the seed down offline. Set a PIN.
4. Send a small test transaction to the wallet. About 0.01 BTC (~$1,000). Small enough that losing it is survivable, big enough that you take it seriously.
5. Wipe the device. Factory reset, on purpose, with that $1,000 sitting on it. This is where most people stop short.
6. Restore from your written seed and confirm the test transaction reappears.

The wipe proves three things at once: the seed was written correctly, you know the procedure under calm conditions, and the backup works.

- If the restore works, the $150,000 stays where it is and you've proven the backup.
- If it fails, you find out with $1,000 at risk instead of $150,000.

== THE NEVER LIST ==

The seed exists on paper or steel, offline, and nowhere else. Anything with a screen and a network connection can be read.

Paper degrades and burns. For a meaningful stack, seed goes on steel, and backups live in separate locations.

== MOVING COIN WELL: UTXOS AND SWEEP THRESHOLDS ==

Every transfer into your wallet creates a UTXO (unspent transaction output). Think of it as a separate bill in your wallet. Your balance is the sum of the bills, and you spend whole bills, not slices.

Send 10 small buys in, and you're holding 10 small bills. Really small ones are called dust because the fee to move them can approach or exceed what they're worth. Either way, holding many small UTXOs raises what it costs to move your Bitcoin later.

Network fees depend on how many bills you're spending, not how much they're worth. A fee that's trivial against a large bill can eat a meaningful slice of a small one.

Sweep on a threshold, not a schedule. Rule of thumb: ~0.01 to 0.02 BTC as a minimum per transfer. Smaller monthly buys accumulate on the exchange to the threshold, then move in one transaction.

If you already have a pocketful of small bills, consolidation is the fix. Combine many small pieces into one in a single transaction, best done when network fees are low. Annual custody review item. Maintenance, not an emergency.

== HOMEWORK ==

If you've never done the wipe-and-restore, watch the demo lesson and do it, with a small test amount, before serious money is on the line.

The next lesson covers closing single points of failure and common scams.
