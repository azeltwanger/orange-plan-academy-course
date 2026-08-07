TELEPROMPTER SCRIPT — segment A7.4
A7.4 Wallet operations: UTXOs, dust, consolidation, and addresses
~5 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
============================================================

In today's lesson, we're going to cover two operational things about moving Bitcoin that almost nobody explains, and both of them came from clients asking me directly.

== YOUR WALLET IS A STACK OF BILLS ==

A client asked me what happens to all the small buys he'd made over the years. His worry was that a bunch of tiny purchases might end up stranded, and that's actually a real thing.

Your wallet isn't a bucket with a balance in it. It's more like a wallet full of bills. Every time Bitcoin lands in your wallet, that deposit is its own separate chunk, and the technical name for one of those chunks is a UTXO, an unspent transaction output. Your balance is the sum of the bills, and when you spend, your wallet grabs one or more whole bills to cover the amount. You spend whole bills, not slices of them.

Now the part that costs money. Every chunk you spend adds to the fee, and that fee doesn't care how big the chunk is. So a very small deposit can become uneconomical to move, because the fee to spend it approaches or exceeds what it's worth. That's what people mean by dust.

If you've been buying small amounts regularly, you can end up with a wallet made of a hundred tiny chunks. Nothing is lost. But the day you go to move it all, you're paying to spend every one of those chunks at once, and if fees are high that day, it gets expensive.

== THE TWO FIXES ==

There are two fixes, one for going forward and one for what you already have.

Going forward, transfer on a threshold rather than on a schedule. Instead of moving every small buy to cold storage the day it happens, let them accumulate on the exchange and move them in one transaction.

Now, I'm deliberately not going to give you a fixed number of Bitcoin here, because the right threshold moves with the price and with what fees are doing. The test that doesn't go stale is this: look at what it would cost in fees to spend that chunk later, and ask whether that's a rounding error against the chunk or a real bite out of it. If a transfer's fee is a meaningful percentage of what you're transferring, it's too small. Check fees on the day, because they swing enormously.

The trade-off is real, though, and worth saying out loud. Everything waiting for the threshold is sitting on an exchange, which is exactly the counterparty risk the custody module is about. So the threshold is a fee decision bounded by a custody decision. If the accumulating balance gets big enough to worry you, move it and pay the fee.

For what you already hold, the fix is consolidation. You send those small chunks to yourself in one transaction, which combines them into one bigger chunk. Do it deliberately on a day when fees are low, not on the day you urgently need to move money. It's a chore for a quiet Sunday and an annual custody review item, not an emergency.

== ADDRESSES ARE PUBLIC ==

The second thing is addresses. Another client was surprised to learn that if somebody knows one of your receiving addresses, they can look up the entire history of that address on the blockchain. Bitcoin's ledger is public. That's the whole design.

So if you use the same receiving address over and over, you've handed anyone who has it a running total of everything you've ever received there. That's not a theft risk directly. It's a privacy risk that becomes a personal safety question once somebody can tie an address to your name.

The fix is easy. Use a fresh receiving address every time you receive. Modern wallets generate a new one automatically and it's usually the default, so mostly this is about not overriding it. And don't post an address publicly and then keep using it.

This is also another reason to check the address on the device screen every single time. It should be a new one, and if it isn't, something is worth understanding before you send.

== YOUR DECISION ==

Your decision here is your transfer threshold, stated as a fee test rather than a fixed amount, and whether you have a consolidation chore waiting.

== HOMEWORK ==

Your homework for this lesson is to:

1. Open your wallet and look at how many separate chunks your balance is actually made of. Most wallets will show you this; some call it coin control.
2. Check what fees are doing today, and write down your transfer threshold as a fee test: the smallest transfer where the fee to spend it later is still a rounding error.
3. If you're holding a pile of small chunks, put consolidation on your annual review as a low-fee-day chore.
4. Confirm your wallet is generating a fresh receiving address each time, and that you haven't published one you keep reusing.
