TELEPROMPTER SCRIPT — segment 9.2
9.2 The access split
~7 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
============================================================

In today's lesson, we're going to cover the access split, which divides the ability to reach your Bitcoin into two pieces, held by two different people.

Either piece on its own is useless. Only the two together can move the Bitcoin. The heirs hold one piece, and your executor holds the other.

== WHY BOTH SIMPLE OPTIONS FAIL ==

Let me show you why the two simple options both fail. The couple's stack is $175,000.

Option one is that one person gets everything. He writes the seed on a card and hands it to her brother, the executor. Now a man who isn't an heir has unilateral control of $175,000 of his sister's inheritance, and the only thing protecting it is his own good faith. Even if he's a great guy, the plan is now built on one person never having a bad year.

Option two is that nobody gets enough. He tells nobody, to be safe. Then he dies. And $175,000 sits on a device his wife can't open, forever.

The split sits between those two extremes. It's an access setup that requires two people to move any Bitcoin.

== WHAT THE SPLIT DOES ==

The split does two jobs at once.

First, no unilateral access. Nobody can help themselves to the funds, and just as important, nobody can be pressured or tricked into moving them alone.

Second, no single point of failure. One person losing their piece doesn't lose the Bitcoin.

Notice how the two failures map: handing one person everything fails both tests. Telling nobody passes the first test and fails the second one completely.

== POOR MAN'S MULTISIG ==

The way you carry the split on a single hardware wallet is the passphrase. Anthony Park calls this poor man's multisig, and it works because of how a passphrase behaves.

Quick review: a seed phrase is the 12 or 24 words that rebuild your wallet. A passphrase is an extra word or phrase added on top, and it's built to the standard we covered in the custody module: 7 random words off a wordlist, picked by dice or an offline generator, never words you thought of yourself. And here's the key property: seed plus passphrase produces a completely different wallet than the seed alone. Same words, different passphrase, different set of coins.

So the seed alone opens a real wallet that's empty. And the passphrase alone is just a word that opens nothing. Two objects, each worthless on its own. That's exactly what lets you hand each one to a different person.

Here's the couple's 1.5 Bitcoin on a hardware wallet with a passphrase. His wife holds the seed phrase. That's the wallet itself, but it's empty on its own, because the funds sit behind the passphrase. Her brother, the executor, holds the passphrase, which doesn't unlock anything without the seed. Together, they have full access. Apart, they have nothing.

Play out the bad days. If her brother turns out to be the wrong guy, he gets nothing. If she loses her card, the passphrase holder still has half of the plan intact. No single bad day, and no single bad person, costs them $175,000.

And this is why the rule from the executor lesson matters: keep the executor and the heirs as different people wherever you can, because they're the two halves of this split.

== MULTISIG: WHERE THE MODEL CHANGES ==

If you're running multisig instead, the split works a little differently.

In a two-of-three vault, there are three keys, and any two can spend. You hold two of them, so nothing about your day changes. You spend on your own, just like today. Your executor holds the third as a sealed seed card, and since one key alone can't spend, they can't touch anything while you're alive. The provider holds the remaining key, and never your seed phrase.

After you're gone, your executor and the provider hold two keys between them, which meets the threshold. The provider verifies who the executor is and walks them through the recovery. So your heirs get a guided recovery instead of a technical exam.

One thing carries over from the custody module: the config file. The keys hold the money, and the config is the map that tells the network how to rebuild the wallet from those keys. Without the map, holding every key still locks you out.

Now, the config has no spending power on its own, so it lives in a password manager, never printed, and never stored with any physical key. Here's why that last part matters: an executor's key sitting next to the config file is one step from control, and that would quietly turn your two-of-three into a single-key setup.

So with a passphrase, you're splitting two different objects between two people. With multisig, the keys are already separate, and the job becomes keeping the config file away from whoever holds a key. Same principle, different setup.

== TEST THE SPLIT WHILE YOU'RE ALIVE ==

Just like the hardware backup, the split gets proven, not hoped for. Because a passphrase mistake can make funds permanently unrecoverable.

Here's the couple's Saturday afternoon. He moves about $1,000 into the passphrase wallet. She restores the seed on a spare device. Her brother reads him the passphrase over the phone. And they watch the $1,000 appear on her screen.

That one afternoon converts a hoped-for split into a proven one, for $1,000 they never actually spent, on a day when nobody was grieving.

One rule after the test: the pieces stay distributed. Writing them down together in one place undoes the entire split.

== THE MISCONCEPTION THAT GETS PEOPLE HURT ==

Last thing, and it's the misconception I hear the most: "I'll just split the seed words between two people." Someone actually did this. 24 words, 12 to each of two people.

Think about what that setup actually does. If the two people trust each other, then together they have the whole thing, so there's no protection. And if either one gets the other half through a leak or a guess, they have unilateral access. And 12 words is a much shorter guess than 24.

So splitting a seed makes the wallet weaker. Splitting the seed from a passphrase makes it stronger. The difference between those two sentences is this entire lesson.

== HOMEWORK ==

Your homework for this lesson is to:

1. Decide who holds each half of your split. Heirs on one side, executor on the other.
2. Schedule the Saturday-afternoon test with a small amount, and actually run it.
3. Confirm the pieces stay in separate places afterward, and that nothing anywhere has both halves written together.
