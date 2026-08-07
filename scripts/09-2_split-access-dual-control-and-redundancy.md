TELEPROMPTER SCRIPT — segment 9.2
9.2 Split access: dual control and redundancy
~10 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
============================================================

In today's lesson, we're going to design who can reach your Bitcoin after you're gone, and prove it works while you're still here.

Before we design anything, I need to give you two tests, because most people design for one of them and just assume they got the other one for free. They didn't, and that assumption is how people lose Bitcoin.

== WHY BOTH SIMPLE OPTIONS FAIL ==

The two obvious answers both fail, and the couple's $175,000 shows why.

One person gets everything: he writes the seed on a card and hands it to her brother, the executor. Now a man who isn't even an heir has unilateral control of $175,000 of his sister's inheritance, and the only thing protecting it is his own good faith. Even if he's a great guy, the plan is built on one person never having a bad year.

Or nobody gets enough: he tells nobody, to be safe, and then he dies, and $175,000 sits on a device his wife can't open, forever.

Everything in this lesson lives between those two.

== THE TWO TESTS ==

🎬 GRAPHIC: two checkboxes, held on screen for the whole lesson. TEST 1 — can one person spend alone? TEST 2 — can one lost copy, or one person you can't reach, permanently stop recovery?

Test one is dual control. Can one person spend alone? If the answer is yes, then that person is a single point of theft, and they're also a single point of pressure, because somebody can lean on them.

Test two is redundancy. Can one lost copy, or one person you can't reach, permanently stop recovery? If the answer is yes, then you've built a way to lose the Bitcoin that has nothing to do with anybody being dishonest.

Two completely different tests. Handing one person everything fails test one. Telling nobody fails test two.

The part that gets missed, and it's really the reason this lesson exists, is that passing one of these does not give you the other. Most setups that pass test one fail test two by default, and test two is a separate job you have to go do on purpose.

== YOUR DESIGN FOLLOWS YOUR CUSTODY LEVEL ==

Now, what you can actually build depends on the custody level you picked back in the custody module. You don't need a more advanced setup to do this lesson. You need an honest design for the setup you already have.

At Level 1, on a hardened exchange or broker, you haven't built household dual control at all. You've delegated custody to an institution, and their process is what stands between any one person and the money. That's a different thing, and worth naming honestly, because it means the two tests get answered by somebody else's procedures rather than by a design you control.

So at Level 1 you're designing a path rather than a secret. Your heirs get the beneficiary designation on the account. Your executor gets the process: which institution, what they'll ask for, who to call. And what you should actually verify is that institution's death-claim procedure, because that procedure is your plan. If it turns out to be slow, or it requires something your family won't have, that's the gap to fix, and no amount of household design fixes it for you.

At Level 2, one hardware wallet and one seed, be honest about what you can and can't do. You cannot split a single seed between two people, and I'll come back to why that idea is actively dangerous. So the honest design is: the seed goes to your heir, backed up in more than one place, and your executor holds the process rather than the secret. Where the device is, where the backups are, what to do, who to call.

That design passes test two, because a lost copy doesn't end you, and it fails test one, because your heir can spend alone. For a lot of households that's an acceptable trade, and it's far better than either failure we opened with. Choose it knowing what it is, and don't describe it to your family as a no-single-point-of-failure plan.

At Level 3 or 4, the passphrase or the multisig, you can pass both tests, but only if the setup and its backups are designed for it.

A passphrase lets you hand two different objects to two different people, where neither does anything alone. That passes test one immediately. It does not pass test two, because seed plus passphrase is a two-of-two, and both are required every single time. Half of a two-of-two is zero. So a passphrase split gets you redundancy only when each half has its own separate backup, which is a second job you have to go do.

A two-of-three multisig is the one that gets both from the arithmetic itself, because any two keys can spend and no single key can, so losing one key entirely is survivable.

Building either one is in the advanced custody lesson, and that's the right place for it, because it's a custody decision, not an estate decision.

The estate job is the same at every level: name who holds what, answer both tests out loud, and be honest about the one you didn't pass.

== EVERY BACKUP IS ALSO A PATH IN ==

Whatever level you're at, there's one tension you have to resolve deliberately, because it's the actual design problem underneath all of this.

Every backup you add to protect against loss is also another potential path to somebody getting unilateral access.

It resolves the same way every time: each piece gets its own backup, and that backup stays on its own side. Never in the same house, never in the same safe, never with the person holding the other piece. Do it that way and each side can lose a copy and still recover, while neither side gains anything it shouldn't have. Do it carelessly and a backup in a shared safe quietly collapses your whole design into one person holding everything.

And this is where the executor question from the last lesson comes back. If the design you chose puts the executor on one side and the heirs on the other, then they have to be different people, or you've handed one person both sides on day one. If your design doesn't split them that way, and plenty don't, then a spouse serving as both is fine. It's a consequence of your design, not a rule about executors.

== TEST IT WHILE YOU'RE ALIVE ==

Just like the hardware backup, this gets proven, not hoped for.

The couple's Saturday afternoon: he moves about $1,000 into the setup, whoever is supposed to be able to recover it does the recovery on a spare device following only what's written down, and they watch the $1,000 appear. If two people are supposed to be needed, run it twice, once with both and once with only one, to confirm the one alone can't.

That converts a hoped-for plan into a proven one, for $1,000 they never spent, on a day when nobody was grieving. One rule afterwards: the pieces stay distributed. Writing everything down together in one place undoes the entire design.

== THE MISCONCEPTION THAT GETS PEOPLE HURT ==

Last thing, and I hear it most from people at Level 2 who want to pass test one without changing their setup. "I'll just split the seed words between two people." Someone actually did this. 24 words, 12 to each of two people.

Look at what that actually builds. If the two people trust each other, together they have the whole thing, so there's no protection at all. And you've just created a two-of-two, which means either half going missing loses everything permanently. You've taken on the redundancy problem without buying any dual control.

That's the difference. Splitting a seed from a passphrase gives you two objects that were designed to be separate. Chopping one seed in half gives you two fragments of one object, and a wallet that now fails if either fragment does. Those sound almost identical and they do opposite things. If you want to pass test one, you change your custody setup. You do not chop up your seed.

== YOUR DECISION ==

Your decision out of this lesson is who holds what, and which of the two tests your design passes.

Design for the custody level you actually have, not the one you'd like to have, because an access plan built on a setup you haven't finished isn't a plan. Pick people who don't share a household, a safe, or a bad week. Choose for reliability over technical skill, since the process is written down and the person mainly has to follow it and be findable. And assume neither person goes rogue, while planning as if one might.

== PUT IT IN ORANGE PLAN ==

Nothing to type. This design goes on your Family Custody Map, and the module walkthrough confirms it against both tests on camera.

== YOU ARE DONE WHEN ==

You can name who holds each piece and where it lives, you have answered both tests in writing including the one your design fails, and you have run the whole thing with a small amount on a spare device. If you failed test two, you fixed it first: a loss you caused yourself is far more likely than a betrayal.
