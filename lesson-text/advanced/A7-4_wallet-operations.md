# Wallet operations: UTXOs, dust, consolidation, and addresses

**Gate:** watch this *before* you have made a hundred small transfers, not after. It applies if you buy regularly in small amounts, or if your wallet already shows a long list of separate chunks under coin control.

## Your wallet is a stack of bills

Your wallet is not a bucket with a balance. Every deposit is its own separate chunk, technically a **UTXO** (unspent transaction output). Your balance is the sum of the bills, and you spend whole bills, not slices.

Every chunk you spend adds to the fee, and **the fee does not care how big the chunk is.** So a very small deposit can become uneconomical to move, because the fee to spend it approaches or exceeds its value. That is **dust**.

Buy small amounts regularly and you end up with a wallet made of a hundred tiny chunks. Nothing is lost. But the day you move it all, you pay to spend every chunk at once, and if fees are high that day it gets expensive.

## The two fixes

**Going forward: transfer on a threshold, not a schedule.** Let small buys accumulate and move them in one transaction rather than moving each buy the day it happens.

**Austin's rule of thumb: about 0.01 to 0.02 Bitcoin as a minimum per transfer.** Smaller monthly buys accumulate on the exchange until they hit that threshold, then move in one transaction.

The reasoning behind the number, which is what to hold onto if fees or the price move a long way: you want the fee to spend that chunk later to be a rounding error against the chunk, not a real bite out of it.

**The trade-off, said out loud:** everything waiting for the threshold sits on an exchange, which is exactly the counterparty risk the custody module is about. The threshold is a fee decision bounded by a custody decision. If the accumulating balance gets big enough to worry you, move it and pay the fee.

**For what you already hold: consolidation.** Send the small chunks to yourself in one transaction, combining them into one. Do it on a low-fee day, deliberately. It is an annual custody review item and a quiet-Sunday chore, not an emergency.

## Addresses are public

If somebody knows one of your receiving addresses, they can look up its entire history on the blockchain. Bitcoin's ledger is public; that is the design.

Reuse the same receiving address and you have handed anyone who has it a running total of everything you ever received there. That is not a theft risk directly. It is a privacy risk that becomes a personal safety question once an address is tied to your name.

**The fix:** use a fresh receiving address every time. Modern wallets do this automatically and it is usually the default, so mostly this is about not overriding it. Do not publish an address and then keep using it.

This is another reason to check the address on the device screen every single time. It should be a new one.

## Your decision

**Your transfer threshold, stated as a fee test rather than a fixed amount, and whether you have a consolidation chore waiting.**

## Homework

1. Open your wallet and look at how many separate chunks your balance is made of. Some wallets call this coin control.
2. Check what fees are doing today and write your threshold as a fee test: the smallest transfer where the fee to spend it later is still a rounding error.
3. If you hold a pile of small chunks, put consolidation on your annual review as a low-fee-day chore.
4. Confirm your wallet generates a fresh receiving address each time, and that you have not published one you keep reusing.
