# 7.2 · Set up a hardware wallet and prove the recovery

The important test for a hardware wallet is not whether you wrote the recovery words down.

It is whether you can restore the wallet from the backup before a meaningful amount of Bitcoin depends on it.

Most people skip that step. They generate a wallet, write the words down, send the Bitcoin, and hope the backup works. The first real recovery test then happens on the worst possible day.

I want the first test to happen while the wallet contains only a small amount and you are calm.


The general process is:

1. Buy the device from the manufacturer or another source the manufacturer explicitly supports. Inspect the packaging and follow the vendor's current verification instructions.
2. Generate a new wallet on the device. Do not use recovery words supplied in the box or by another person.
3. Record the recovery material offline and set the device PIN according to the current vendor process.
4. Receive a small test transaction and confirm it is visible.
5. Use the vendor's verified recovery-check procedure or, when appropriate for the exact device, wipe and restore the test wallet.
6. Confirm the same wallet and test funds reappear before sending a meaningful balance.

The exact button sequence depends on the device and firmware. That is why the filmed demo has to use the actual hardware and current instructions rather than a generic script pretending every wallet works the same way.

There are a few rules that do not change.

Never type recovery words into a computer, phone, ordinary website, photo, cloud document, or AI chat.

Never use a recovery tool because somebody contacted you and created urgency.

Never assume a device screen and a computer screen showing the same address is enough. Verify receive addresses on the trusted device itself.

And always send a small transaction before moving a life-changing amount.

The backup has to survive the risks that matter in your life. Paper can be damaged by fire, water, fading, or somebody throwing it away. A steel backup may make sense for meaningful long-term holdings. Multiple copies can reduce loss risk, but copies also increase the number of places that have to be secured.

Separate locations protect against one fire or disaster. They can also create a theft or privacy problem if the locations are chosen poorly. Redundancy is not simply making as many copies as possible. It is making sure one event cannot destroy every recovery path.

A passphrase changes the recovery process. The seed alone restores a different wallet from the seed plus passphrase. A forgotten or mistyped passphrase can make the intended funds unreachable even when the seed is perfect. That setup needs its own small-value test and its own recovery documentation.

Multisig adds another dependency: the wallet descriptor or configuration that explains how the keys form the wallet. The keys alone may not be enough to reconstruct the intended wallet safely. That is covered in the Advanced custody lesson.

There is also a practical issue with moving Bitcoin into cold storage: transaction size and UTXOs.

Every withdrawal can create a separate spendable output. A large number of tiny withdrawals can become expensive or awkward to spend later when network fees are high. I would not turn this into one permanent Bitcoin threshold because the dollar value and fee market change. The useful rule is to avoid creating a pile of uneconomic outputs and review consolidation when fees are low. The Advanced wallet-operations lesson covers the details.

For this core lesson, the finish line is straightforward: you have a device-specific recovery process you personally tested with a trivial amount, the backup is stored offline, and the address and transaction checks were performed on the trusted device.

The external demo will show the actual process using a throwaway wallet with no meaningful funds. Do not film or display a real seed, real PIN, or real family recovery setup.

## Apply it

Use walkthrough 7.4 to enter the decision and confirm what Orange Plan calculated.

## Module checkpoint

- [ ] Custody level is chosen for the amount and household.
- [ ] Hardware recovery is proven or clearly outstanding.
- [ ] The top single point of failure has an owner and deadline.
- [ ] Important accounts and email are hardened.
- [ ] No seed, key, passphrase, or PIN is stored in the app or course notes.
- [ ] An encrypted backup of the plan data exists.
