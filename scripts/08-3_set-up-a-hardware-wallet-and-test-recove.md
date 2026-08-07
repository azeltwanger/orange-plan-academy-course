TELEPROMPTER SCRIPT — segment 8.3
8.3 Set up a hardware wallet and test recovery
~8 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
============================================================

In today's lesson, we're going to cover the hardware wallet setup, and the recovery test that proves your backup actually works before serious money depends on it.

Because a seed backup is only as good as your ability to actually restore from it. And most people have never tested that.

== WHERE YOUR BITCOIN ACTUALLY LIVES ==

First: your Bitcoin isn't on the device.

When you set up a hardware wallet, it generates a seed phrase, 12 or 24 words, and every key to your Bitcoin is derived from those words. The device is just a safe place to use them. The device is replaceable. The seed is not.

So if the device breaks, you rebuild the wallet on a new device from the seed, and nothing is lost. But if the seed is wrong, a broken device is the end of the stack.

And there's a detail that makes this sharper: most hardware wallets wipe themselves after a set number of wrong PIN entries. That's the right feature, because it stops a thief from guessing their way in. But it also means your entire stack effectively lives on the paper backup. The device can erase itself on a Tuesday afternoon, and that piece of paper becomes the only copy in existence.

== THE SIX-STEP SETUP ==

The setup is 6 steps, and the order matters.

Step one: buy the device directly from the manufacturer. Never used, never from a third-party seller. A device someone else touched can arrive with a seed they already know, and then every coin you send it is already theirs.

Step two: generate a brand-new wallet on the device itself. The seed gets created by the device, and it has never existed anywhere else in the world.

Step three: write the seed down offline, and set a PIN.

Step four: send a small test transaction to the wallet. Something like 0.01 Bitcoin, around $1,000. Small enough that losing it is survivable, big enough that you take it seriously.

Step five, and this is where most people stop short: wipe the device. Factory reset it, on purpose, with that $1,000 sitting on it. I know that feels wrong. That's exactly why you do it.

Step six: restore from your written seed, and confirm the test transaction reappears.

That wipe-and-restore proves three things at once. The seed was written down correctly. You know the procedure, and you learned it under calm conditions. And the backup actually works.

If the restore works, your real stack moves over and you've proven the backup. And if it fails, you found out with $1,000 at risk instead of $150,000. I think that's a pretty good trade for an afternoon of work.

== THE NEVER LIST ==

The rules for the seed itself are short. The seed exists on paper or steel, offline, and nowhere else. Not in a photo, not in a password manager, not in a note app, because anything with a screen and a network connection can be read.

And paper degrades and burns. For a meaningful stack, the seed goes on steel, and the backups live in separate locations. We'll cover the locations in the single-points-of-failure lesson.

== MOVING COIN WELL: UTXOS AND SWEEP THRESHOLDS ==

The last piece of this lesson is about moving coins well, and it starts with a word: UTXO.

Every transfer into your wallet creates a UTXO, an unspent transaction output. The way I think about it is that each one is a separate bill in your wallet. Your balance is the sum of the bills, and you spend whole bills, not slices of them.

So if you send 10 small buys into your wallet, you're now holding 10 small bills. And the really small ones are called dust, because the fee to move them can approach or even exceed what they're worth.

That matters because network fees depend on how many bills you're spending, not how much they're worth. A fee that's trivial against one large bill can eat a meaningful slice of a small one. So holding a pile of small UTXOs quietly raises what it costs to move your own Bitcoin later.

The fix is to sweep on a threshold, not on a schedule. My rule of thumb is about 0.01 to 0.02 Bitcoin as a minimum per transfer. Your smaller monthly buys accumulate on the exchange until they hit the threshold, and then they move in one transaction.

And if you already have a pocketful of small bills, the fix is consolidation: you combine many small pieces into one, in a single transaction, best done when network fees are low. That's an annual custody review item. It's maintenance, not an emergency.

== IF YOU'RE AFRAID TO TOUCH IT ==

I want to talk to a specific person for a minute, because I run into them a lot.

You bought the hardware wallet. You moved your Bitcoin onto it. And now you don't touch it. You don't plug it in, you don't update it, you don't check it, because you're scared that plugging it in is how you get robbed.

I had a client tell me almost exactly that. She said she doesn't plug it into anything, and that outside of receiving and sending she doesn't really use it, because she doesn't know how to keep it safe.

If that's you, a hardware wallet is built for exactly this. The whole design is that your keys never leave the device. It doesn't hand them to your computer or your phone when you plug it in. That's the entire reason the thing exists. So plugging it into your normal computer is not the risk you think it is.

There is one real threat to know about, and it's worth knowing precisely. There's malware that watches your clipboard and swaps the Bitcoin address you're sending to. You paste in your address, and what actually gets sent is somebody else's.

The defense takes 10 seconds and it never fails: **read the address on the hardware wallet's own screen and confirm it matches what's on your computer.** The whole address, not just the first few characters. The device screen is the thing malware can't touch. That's why it has a screen.

On firmware updates, I'll tell you what I do. I don't rush them. When an update comes out, I usually wait a few months and let other people find the problems first. But I do eventually install them, because they often contain real security fixes. Being a little paranoid here isn't a bad instinct at all. Just don't let it turn into never.

== PIN VERSUS SEED PHRASE ==

And there's a distinction that resolves a fear I hear constantly: what if I die and nobody knows my PIN?

Your PIN protects the device. That's all it does. If someone gets the physical device, the PIN is what stops them.

Your seed phrase IS your Bitcoin. It works in any hardware wallet from any manufacturer.

So if something happens to you and your family doesn't know your PIN, that's fine. They don't need it. They buy a new hardware wallet, restore from the seed phrase, and the Bitcoin is there. The PIN dies with the device and it doesn't matter.

That also means the reverse is true, and it's the part to take seriously: **protecting the PIN is not protecting your Bitcoin.** The seed phrase is the thing that needs the real protection.

== HOMEWORK ==

Your homework for this lesson is to:

1. If you've never done the wipe-and-restore, watch the demo lesson in this module and then actually do it, with a small test amount, before serious money is on the line.
2. Check your own wallet for dust. If your buys have been trickling in small, set your sweep threshold now.
