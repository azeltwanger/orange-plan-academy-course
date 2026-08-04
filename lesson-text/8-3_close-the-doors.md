# Close the doors: single points of failure, hardening, scams

## Three shapes of a single point of failure

1. The thing gets destroyed (device, backup).
2. The thing is fine but the person is unavailable (only one head holds the process).
3. You and your coin are fine and the custodian won't move it (exchange freeze).

Three ordinary Tuesdays lose Bitcoin without a single hacker: a flood takes the device *and* the only backup in the same house; a six-week hospitalization freezes everything because nobody else knows anything; an exchange review locks the account.

## The nine-question hunt

Is there only one… device? seed backup? location? person who knows everything? weak exchange login? heir with no idea what exists? document contradicting your beneficiary forms? passphrase nobody can recover? place all multisig keys sit?

## The fix method

List your top three **by cost of loss** (not ease of fix) → fix the top one only → re-check → repeat. Every only-one becomes a backup, a second location, or a second person who knows the *process*, never the secrets.

## Account hardening (in this order)

1. **Secure the email first**: it's the master key; every reset routes through it.
2. Strong unique password everywhere.
3. **App-based 2FA, not SMS** (SIM swap takes exchange + email in an afternoon); authenticator cloud backup off.
4. Withdrawal delays + allowlists on; never click login links.

One better: a **hardware security key**: bound to the real site's address, so phishing sites get no response. Cheapest upgrade in the lesson.

## The scam rules

"Your account is hacked" call → hang up, contact the provider yourself. Guaranteed returns are a scam. **Urgency is the common thread**: every scam needs you to act before you think. When something feels urgent, close the app and slow down.

## UTXOs and addresses

**UTXOs.** Your wallet isn't a bucket with a balance; it's a wallet full of bills. Every deposit is its own chunk (a UTXO), and spending grabs one or more chunks.

Every chunk costs a fee to spend, and the fee doesn't care how big the chunk is. So a very small deposit can become uneconomical to move (that's "dust"). Buy small amounts regularly and you can end up with a hundred tiny chunks: nothing is lost, but moving it all means paying fees on every chunk at once.

**Fix: consolidation.** Send the small chunks to yourself in one transaction to combine them, deliberately on a low-fee day, not the day you urgently need to move money.

**Addresses.** Bitcoin's ledger is public, so anyone with one of your receiving addresses can see that address's entire history. Reuse the same address and you've handed them a running total.

**Fix:** use a fresh receiving address every time. Modern wallets do this by default, so don't override it and don't publish an address you keep using. Another reason to check the address on the device screen each time: it should be a new one.

## Homework

1. Write your only-one list (all nine).
2. Fix just the top one this week.
3. Watch the demo below for the on-screen setup + hardening.
