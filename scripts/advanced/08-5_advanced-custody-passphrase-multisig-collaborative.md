TELEPROMPTER SCRIPT — segment 8.5
8.5 Advanced custody: passphrase, multisig, and collaborative
~16 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
============================================================

In today's lesson, we're going to cover the advanced custody setups: the passphrase, multisig, and collaborative custody.

You just went hunting for your single points of failure. Advanced custody is how you actually split them.


Now the advanced setups, for when you're at Level 3 or 4.

What "advanced" actually means here is removing the single points of failure that a single-device, single-seed setup has. Every advanced setup takes one of those only-ones and splits it into two. And you pay for that in complexity, and in what your family has to be able to do.

Two definitions first. A passphrase is an extra word you choose, layered on top of your seed. The wallet doesn't open without both. And multisig, short for multi-signature, means the wallet is secured by several separate keys, and more than one has to sign before Bitcoin moves. The common setup is two-of-three: 3 keys, any two can spend, and losing any single one costs you nothing.

There are 3 paths.

Path one is passphrase single-sig. One seed plus a hidden extra word. It's best for a modest stack, and what it buys you is the simplest advanced plan a family can follow. The watch-out is serious, though: a forgotten passphrase locks the funds permanently. There is no reset mechanism, no support line. So the passphrase gets its own backup, stored separately from the seed, and you practice with a small amount first.

Now, since the passphrase is doing so much work in this path, let me talk about how to actually make one that's strong, because this is where people get it wrong.

Before the how, let me give you the clearest example I've got for why a passphrase is worth it at all. Say someone comes to clean your house, and they find your seed phrase in a drawer. Without a passphrase, they now have your Bitcoin. With a passphrase, they have 12 or 24 words that open an empty wallet, and they can't do anything with them. That's what you're buying.

Now, how to actually make one.

A passphrase that you make up yourself is the weak point of the whole setup. Humans pick quotes, song lyrics, kids' names, dates. And the people trying to crack wallets run exactly those lists first. So the fix is randomness that you didn't choose.

Use 7 random words, picked from a wordlist by rolling dice or by a generator running offline. This is called the diceware method, and a good password manager can do it for you too, with the device offline. The key word is random. The tool picks the words, not you.

🎬 GRAPHIC: 7 dice-drawn words appearing one at a time, with the combination count multiplying beside them (7,776 → 60M → 470B → …). End on "~90 bits of entropy" and "millions of years at a trillion guesses per second."

Every word that gets drawn at random from the standard wordlist multiplies the number of guesses an attacker needs by about 7,776, because that's how many words are on the list. By the time you're at 7 words, you're at roughly 90 bits of entropy, which works out to more combinations than a machine guessing a trillion times per second could get through in millions of years. 4 or 5 words is where "pretty good" lives. I think 7 is the floor for money that has to stay safe forever.

A few nevers while we're here. Never personal facts, never quotes or lyrics, never an address or a pet's name, and never a password that you already use somewhere else. The test is simple: if it means something to you, it's guessable.

And two practical things. First, a wallet passphrase is case-sensitive and completely unforgiving, so you record it exactly, letter for letter, on paper or on steel, and it never gets typed into anything that's online. Second, this same 7-word standard covers three different things in this course: your wallet passphrase, your password manager's master password, and the passphrase on the encrypted plan backup that we make in the walkthroughs. One method, three uses.

Now, I know the temptation here, because I've felt it and clients ask me about it every time. The temptation is to pick something short and memorable instead, so you're sure you won't forget it. And I understand the logic. But memorable means guessable, and a passphrase is guarding money that has to stay safe for decades. So the answer isn't a passphrase you can remember. The answer is 7 random words that you back up properly in two places, so you never have to remember them at all.

People also ask whether they can just keep it in a password manager. My answer is that a password manager is fine as one copy, but not as your only copy, and only if somebody else can actually get into that password manager if you're gone. If your passphrase lives in a manager that dies with you, you've built a very secure way to lose your Bitcoin. Keep a physical copy.

The trade-off is built right in. A passphrase that's strong enough to be unguessable is also unrecoverable if you lose it. That's exactly why it gets its own backup, stored separately from the seed, and why you practice with a small amount first.

Path two is collaborative multisig. You hold 2 keys, a provider holds one, plus the configuration. This is best for a meaningful balance, or for heirs who aren't technical, because what you're buying is a professional on call to guide them. The costs are an annual fee and some vendor dependence. One important note: the provider's single key can't spend on its own, so they never actually custody your Bitcoin.

Let me go a level deeper on collaborative, because I think it's the right answer for more households than pick it, and the key count is the part people miss.

It's a two-of-three. 3 keys exist, and any two of them can move Bitcoin. You hold two. The provider holds one.

That split gives you two properties. The first one is that they can never take your Bitcoin, because one key out of a required two spends nothing. They're a co-signer, not a custodian, and that is the entire difference between this and leaving it on an exchange. The second one is that they can never lock you out, because you're already holding 2 keys, which is a spending quorum all by itself. You don't need their permission or their participation to move your own money.

So what are you actually paying for? Three things. A key you didn't have to store yourself. A copy of the configuration file, held by somebody whose actual job is not losing it. And a human being who is going to pick up the phone and walk your family through a recovery on the worst week of their lives. That third one, honestly, is the whole reason this path exists.

Before you pick a provider, verify four things. Number one, can you recover if the provider is gone? They should hand you the configuration file, and it should work in open-source wallet software that they don't control. If the answer is that you'd have to call them, then that's a custodian wearing a multisig costume. Number two, is there a documented inheritance process? Ask exactly what happens when your executor calls, and what proof they're going to require. Number three, what's the annual fee, and what happens to your wallet if you stop paying it? And number four, what do they require from you, in identity verification and in privacy terms, to open the account in the first place.

The honest downside here is that you're depending on a company to keep existing across a timeline measured in decades. That's a real risk and I'm not going to talk you out of it. But it's bounded by the key count. Your worst case is that the provider vanishes and you spend an afternoon recovering with your 2 keys and the config file. Compare that to the DIY worst case, where the person who understood the whole setup is the person who died.

Path three is DIY multisig. You hold every key and the configuration yourself. Best for technically proficient people. It buys you maximum privacy and full independence. But there's a trade nobody talks about: your heirs inherit the complexity with no professional to guide them. This path trades your family's recovery odds for your independence.

You can see them compared right here across 4 rows: single point of failure, maintenance load, heir-friendliness, and cost. Look at all 4 rows before picking. Technical people tend to stop at row one and end up with something their family can't use.

Run it on the same household. $175,000 of Bitcoin, he's 45 and healthy, his wife has never restored a wallet, and the kids are 10 and 12.

DIY multisig wins the single-point-of-failure row, but it hands a widow and two middle-schoolers a recovery job nobody in the house can do. Collaborative is a real option, and if the stack triples, I think it becomes the right one. But right now they'd be paying an annual fee for a problem they don't have yet. The passphrase path fits. One seed, one extra word, split between two people. It's the only path his wife could realistically be walked through in an afternoon.

Match the setup to your family and your stack, and only add complexity when it buys real risk reduction.

== THE CONFIG FILE ==

One last thing, and for multisig households it's what actually gets families locked out.

The keys hold the money. The config is the file that records how those keys connect into one wallet: which keys, the two-of-three rule, the technical addresses. That file is the map. With the config, your heirs have 3 seeds in separate locations plus the map, and the wallet reassembles. Without it, they can hold all 3 seeds in their hands and still be locked out.

And this is not hypothetical. A man dies with a two-of-three multisig holding about $300,000. He did everything right on the keys. 3 seeds, three separate locations, the executor holds one, and the family finds all three. They recover nothing. $300,000, lost to a missing file.

It has no spending power. Losing it to a thief costs you privacy, not coins. Which means you can back it up aggressively, in ways you would never back up a seed. And if you're with a collaborative provider, they hold the config for you. On top of the support, that annual fee is buying the one file your heirs can't reconstruct on their own.

== BUILDING THE ESTATE SPLIT ON EACH PATH ==

The estate module gives you the two tests: can one person spend alone, and can one lost copy permanently stop recovery. What it deliberately doesn't do is show you how to build a setup that passes both, because that's a custody decision. So here's how each path carries the split.

On the passphrase path, Anthony Park calls this poor man's multisig, and it works because of how a passphrase behaves. Seed plus passphrase produces a completely different wallet than the seed alone. Same words, different passphrase, different set of coins. So the seed by itself opens a real wallet that's empty, and the passphrase by itself is a word that opens nothing. Two objects, each worthless alone, which is exactly what lets you hand each one to a different person.

Your heir holds the seed. Your executor holds the passphrase. Together they have full access, apart they have nothing. That's test one, passed by design.

Now test two, and this is the trap. Seed plus passphrase is a two-of-two. Both pieces are required every single time. So if the seed card is lost in a fire, the passphrase opens nothing. And if the executor dies without passing the passphrase on, the seed opens an empty wallet. Either one is a total, permanent loss with nobody having done anything wrong. Half of a two-of-two is zero.

Which means each half needs its own backup, on its own side. A second steel copy your heir controls, or one their own successor can reach, never anywhere the passphrase holder can also get to. The passphrase written once, sealed, held by the executor or whoever he names after him, never in the same house or the same safe as the seed.

On the multisig path, a two-of-three vault passes both tests structurally, without you engineering the backups yourself. Any two of the three can spend, so losing one key entirely is survivable, and no single holder can spend alone. Both tests, handled by the arithmetic.

The distribution that makes it work as an estate plan: you hold two keys, so nothing about your day changes and you spend on your own just like today. Your executor holds the third as a sealed seed card, and since one key alone can't spend, they can't touch anything while you're alive. If you're with a collaborative provider, they hold the remaining key and never your seed phrase. After you're gone, your executor and the provider hold two keys between them, which meets the threshold, and the provider verifies who the executor is and walks them through it. Your heirs get a guided recovery instead of a technical exam.

The one thing to get right is where the config file sits. An executor's key stored next to the config file is one step from control, and that quietly turns your two-of-three into a single-key setup. So the config lives in a password manager, never printed, never stored with any physical key.

So with a passphrase you're splitting two different objects between two people. With multisig the keys are already separate, and the job becomes keeping the config away from whoever holds a key. Same principle, different setup.

== HOMEWORK ==

Your homework for this lesson is to:

1. Decide whether an advanced setup is warranted for you at all. Staying at a well-run Level 2 is a legitimate answer, and I don't want anybody adding complexity they don't need.
2. If you're adding a passphrase, generate it with 7 random words off a wordlist, using dice or an offline generator. Back it up separately from the seed, and practice with a small amount first.
3. If you're considering collaborative custody, ask a provider those 4 questions and get the answers in writing before you pay anybody anything.
4. If you're already running multisig, go find your config file, back it up, and tell one other person that it exists.
5. Then record whatever you decide on your custody map, back in the core custody module.
