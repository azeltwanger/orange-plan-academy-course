TELEPROMPTER SCRIPT — segment 9.2
9.2 The access split
841 words · ~5.4 min at 155 wpm
============================================================

The access split divides the ability to reach your Bitcoin into two pieces, held by two different people. Either piece on its own is useless. Only the two together can move the Bitcoin. Heirs hold one piece; your executor holds the other.

== WHY BOTH SIMPLE OPTIONS FAIL ==

The couple's stack is $175,000.

Option 1: One person gets everything. He writes the seed on a card and hands it to her brother. Now a man who isn't an heir has unilateral control of $175,000 of his sister's inheritance, and the only thing protecting it is his own good faith.

Option 2: Nobody gets enough. He tells nobody, to be safe. He dies. $175,000 sits on a device his wife can't open.

The split sits between those two extremes: an access setup that requires two people to move any Bitcoin.

== WHAT THE SPLIT DOES ==

Two jobs at once:

1. No unilateral access. Nobody can help themselves, and nobody can be pressured or tricked into moving it alone.
2. No single point of failure. One person losing their piece doesn't lose the Bitcoin.

Handing one person everything fails both tests. Telling nobody passes the first and fails the second completely.

== POOR MAN'S MULTISIG: HOW A PASSPHRASE CARRIES THE SPLIT ==

Anthony Park calls this "poor man's multisig." It works because of how a passphrase behaves.

A seed phrase is the 12 or 24 words that rebuild your wallet. A passphrase is an extra word or phrase added on top. Seed plus passphrase produces a completely different wallet than the seed alone. Same words, different passphrase, different set of coins.

- Seed alone. Opens a real wallet that's empty.
- Passphrase alone. A word that opens nothing.

Two objects that are worthless on their own. That's what lets you hand each to a different person.

Here's the couple's 1.5 BTC on a hardware wallet with a passphrase:

- His wife holds the seed phrase. The wallet itself. Empty on its own. The funds sit behind the passphrase.
- Her brother, the executor, holds the passphrase. The extra word. Doesn't unlock anything without the seed.
- Together, they have full access. Apart, they have nothing.

If her brother turns out wrong, he gets nothing. If she loses her card, the passphrase holder still has half of the plan. No single bad day or bad person costs them $175,000.

Keep the executor and the heirs as different people wherever you can.

== MULTISIG: ONE PLACE THE PASSPHRASE MODEL DOESN'T CARRY OVER ==

A 2-of-3 vault has three keys, any two can spend.

- You hold two. Nothing about your day changes. You spend on your own like today.
- Your executor holds the third as a sealed seed card. One key alone can't spend, so they can't touch it while you're alive.
- The provider holds the remaining key, never your seed phrase.

After you're gone, your executor and the provider hold two keys between them (the threshold). The provider verifies who the executor is and walks them through recovery. Your heirs get a guided recovery, not a technical exam.

== THE CONFIG FILE, REVISITED ==

The keys hold the money. The config is the map that tells the network how to rebuild the wallet from those keys. Without the map, holding every key still locks you out.

The config has no spending power on its own, so it lives in a password manager, never printed, and never stored with any physical key. An executor's key sitting next to the config file is one step from control, and that would turn your 2-of-3 into a single-key setup.

With a passphrase, you're splitting two different objects. With multisig, the keys are already separate, and the job becomes keeping the config file away from whoever holds a key. Same principle, different setup.

== TEST THE SPLIT WHILE YOU'RE ALIVE ==

A passphrase mistake can make funds unrecoverable, so this gets proven the same way the hardware backup did.

The couple's Saturday afternoon:

1. He moves ~$1,000 into the passphrase wallet.
2. She restores the seed on a spare device.
3. Her brother reads him the passphrase over the phone.
4. They watch the $1,000 appear on her screen.

That converts a hoped-for split into a proven one, for $1,000 they never actually spent and one afternoon nobody was grieving.

The pieces stay distributed after the test. Writing them together in one place undoes the entire split.

== THE MISCONCEPTION THAT GETS PEOPLE KILLED ==

"I'll just split the seed words between two people." A client did exactly this: 24 words, 12 to each of two people.

- If they trust each other, together they have the whole thing (no protection).
- If either one figures out the other half through a leak or a guess, unilateral access. 12 words is a much shorter guess than 24.

Splitting a seed makes the wallet weaker. Splitting the seed from a passphrase makes it stronger.

The next lesson covers the heir letter, which sits alongside the split.
