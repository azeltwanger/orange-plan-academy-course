TELEPROMPTER SCRIPT — segment 9.2
9.2 Split access: dual control and redundancy
~8 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
============================================================

In today's lesson, we're going to cover the access split, which divides the ability to reach your Bitcoin into two pieces, held by two different people.

Now, before we build it, I need to give you two tests, because most people design for one of them and just assume they got the other one for free. They didn't, and that assumption is how people lose Bitcoin.

🎬 GRAPHIC: two boxes side by side. LEFT: seed phrase, held by heirs, with a padlock still closed. RIGHT: passphrase, held by executor, also closed. Then slide them together and the padlock opens. Neither alone does anything.

Either piece on its own is useless. Only the two together can move the Bitcoin. The heirs hold one piece, and your executor holds the other.

== WHY BOTH SIMPLE OPTIONS FAIL ==

Let me show you why the two simple options both fail. The couple's stack is $175,000.

Option one is that one person gets everything. He writes the seed on a card and hands it to her brother, the executor. Now a man who isn't an heir has unilateral control of $175,000 of his sister's inheritance, and the only thing protecting it is his own good faith. Even if he's a great guy, the plan is now built on one person never having a bad year.

Option two is that nobody gets enough. He tells nobody, to be safe. Then he dies. And $175,000 sits on a device his wife can't open, forever.

The split sits between those two extremes. It's an access setup that requires two people to move any Bitcoin.

== THE TWO TESTS ==

Test one is dual control. Can one person spend alone? If the answer is yes, then that person is a single point of theft, and they're also a single point of pressure, because somebody can lean on them.

Test two is redundancy. Can one lost copy, or one person you can't reach, permanently stop recovery? If the answer is yes, then you've built a way to lose the Bitcoin that has nothing to do with anybody being dishonest.

Two different tests. Handing one person everything fails test one. Telling nobody fails test two completely.

The part that gets missed, and it's really the reason this lesson exists, is that the split I'm about to show you passes test one by design and fails test two by default. Test two is a separate job. You have to go do it on purpose.

== POOR MAN'S MULTISIG ==

The way you carry the split on a single hardware wallet is the passphrase. Anthony Park calls this poor man's multisig, and it works because of how a passphrase behaves.

Quick review: a seed phrase is the 12 or 24 words that rebuild your wallet. A passphrase is an extra word or phrase added on top, and it's built to the standard we covered in the custody module: 7 random words off a wordlist, picked by dice or an offline generator, never words you thought of yourself. And the key property is this: seed plus passphrase produces a completely different wallet than the seed alone. Same words, different passphrase, different set of coins.

So the seed alone opens a real wallet that's empty. And the passphrase alone is just a word that opens nothing. Two objects, each worthless on its own. That's exactly what lets you hand each one to a different person.

His wife holds the seed phrase. That's the wallet itself, but it's empty on its own, because the funds sit behind the passphrase. Her brother, the executor, holds the passphrase, which doesn't unlock anything without the seed. Together, they have full access. Apart, they have nothing.

So that's test one, passed. If her brother turns out to be the wrong guy, he gets nothing.

Now test two, and this is the trap I want you to see clearly. Seed plus passphrase is a two-of-two setup. Both pieces are required, every single time. So if her card is lost in a fire, her brother's passphrase opens nothing. And if her brother dies without passing that passphrase on, her seed opens an empty wallet. Either one of those is a total, permanent loss, and neither one involves anybody doing anything wrong.

Half the plan is worth nothing here. Half of a two-of-two is zero.

== MAKING THE SPLIT SURVIVE A LOSS ==

So there's a tension here, and it's the actual design problem. Every backup you add to protect against loss is also a potential path to somebody getting unilateral access. And it resolves one way: each piece gets its own backup, and that backup stays on its own side of the split.

The seed's backup belongs to the seed side. A second steel copy his wife controls, or one her own successor can get to. Never somewhere the passphrase holder can also reach.

The passphrase's backup belongs to the passphrase side. Written once, sealed, held by the executor or whoever he names after him. Never stored with the seed, never in the same house, never in the same safe.

Do it that way, and each side can lose a copy and still recover, and neither side can ever act alone. Do it carelessly, and a backup sitting in a shared safe quietly turns your two-of-two into one person holding everything.

And if you decide to only ever make one copy of each half, that's fine, but say it out loud and accept it. For a small stack that's a legitimate call. It just isn't a no-single-point-of-failure setup, and you shouldn't describe it to your family as one.

And this is why the rule from the executor lesson matters: keep the executor and the heirs as different people wherever you can, because they're the two halves of this split.

== MULTISIG: WHERE THE MODEL CHANGES ==

If you're running multisig instead, the split works a little differently.

And this is where multisig earns its complexity, because a two-of-three vault passes both tests at once, structurally, without you having to engineer the backups yourself.

In a two-of-three vault, there are 3 keys, and any two can spend. Because any two of the three are enough, losing one key entirely is survivable, and no single key holder can spend on their own. Both tests, handled by the arithmetic. You hold two of them, so nothing about your day changes. You spend on your own, just like today. Your executor holds the third as a sealed seed card, and since one key alone can't spend, they can't touch anything while you're alive. The provider holds the remaining key, and never your seed phrase.

After you're gone, your executor and the provider hold 2 keys between them, which meets the threshold. The provider verifies who the executor is and walks them through the recovery. So your heirs get a guided recovery instead of a technical exam.

One thing carries over from the custody module: the config file. The keys hold the money, and the config is the map that tells the network how to rebuild the wallet from those keys. Without the map, holding every key still locks you out.

Now, the config has no spending power on its own, so it lives in a password manager, never printed, and never stored with any physical key. That last part matters because an executor's key sitting next to the config file is one step from control, and that would quietly turn your two-of-three into a single-key setup.

So with a passphrase, you're splitting two different objects between two people. With multisig, the keys are already separate, and the job becomes keeping the config file away from whoever holds a key. Same principle, different setup.

== TEST THE SPLIT WHILE YOU'RE ALIVE ==

Just like the hardware backup, the split gets proven, not hoped for. Because a passphrase mistake can make funds permanently unrecoverable.

So, the couple's Saturday afternoon. He moves about $1,000 into the passphrase wallet. She restores the seed on a spare device. Her brother reads him the passphrase over the phone. And they watch the $1,000 appear on her screen.

That one afternoon converts a hoped-for split into a proven one, for $1,000 they never actually spent, on a day when nobody was grieving.

One rule after the test: the pieces stay distributed. Writing them down together in one place undoes the entire split.

== THE MISCONCEPTION THAT GETS PEOPLE HURT ==

Last thing, and it's the misconception I hear the most: "I'll just split the seed words between two people." Someone actually did this. 24 words, 12 to each of two people.

Think about what that setup actually does. If the two people trust each other, then together they have the whole thing, so there's no protection. And if either one gets the other half through a leak or a guess, they have unilateral access. And 12 words is a much shorter guess than 24.

So splitting a seed makes the wallet weaker, and splitting the seed from a passphrase makes it stronger. Those two things sound similar and they do opposite things.

== YOUR DECISION ==

Your decision out of this lesson is who holds each half of your access.

You're splitting two different objects, never one object into two pieces, because half a seed makes the wallet weaker while a seed separated from a passphrase makes it stronger. Pick people who don't share a household, a safe, or a bad week, because two halves in one house is one location, not two. Choose for reliability over technical skill, since the process is written down and the person mainly has to follow it and be findable. And assume neither one goes rogue, but plan as if one might, which is exactly why neither half is worth anything on its own.

== HOMEWORK ==

Your homework for this lesson is to:

1. Name the person holding each half, and write down where each piece lives.
2. Answer both tests in writing. Can one person spend alone? And can one lost copy stop recovery? If that second answer is yes, go back up each half on its own side of the split before you do anything else.
3. Run the test with a small amount, start to finish, so you know it actually works.
4. Confirm afterwards that the two halves are still in separate places, and that they were never written down together.
