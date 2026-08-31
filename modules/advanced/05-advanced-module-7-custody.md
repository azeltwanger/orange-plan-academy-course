# Advanced Module 7 — Custody

## A7.1 Compare passphrase, multisig, institutional custody, and an intentional split

> **Gate.** Research complete. Verify exact devices, wallet software, descriptors, provider roles, institutional terms, and recovery procedures before any setup-specific footage.

Advanced custody is not a ladder where every serious Bitcoiner eventually puts everything into the most complicated self-custody setup.

It is a comparison of which failure you want each method to remove and which responsibilities you are willing to keep.

A passphrase wallet uses a normal seed plus an additional passphrase to derive a different wallet. The passphrase is sometimes called a twenty-fifth word, but it does not have to be one word and it is not a second signature.

Anyone with the seed and the exact passphrase can control the intended wallet. A wrong passphrase can still produce a valid but different wallet, which makes recovery mistakes especially dangerous.

What the passphrase changes is what possession of the seed alone can do. It does not remove seed loss, passphrase loss, coercion, physical security, or family-process risk.

Test the exact recovery with a trivial amount. The seed-only wallet, the intended passphrase wallet, and a mistyped passphrase can all look valid. The family process has to make the intended wallet unambiguous without placing the two secrets together.

A two-of-three multisig wallet uses three signing keys and requires two valid signatures.

One lost key does not necessarily destroy access, and one stolen key does not spend alone. That removes a single-key failure. It does not remove every single point of failure.

The wallet also depends on public configuration information: the keys or xpubs, threshold, script type, derivation paths, fingerprints, and related descriptor or wallet-policy data. That information cannot sign by itself, but it is important for reconstructing the intended wallet and can reveal privacy information.

Collaborative multisig shares part of the operational burden with a provider. The customer may hold two keys while the provider holds one, or use another arrangement defined by the service. The provider may retain the wallet configuration, help verify an executor, and guide recovery.

The trade-off is provider involvement, fees, identity checks, jurisdiction, privacy, and the risk that the service changes or disappears. Understand the provider-independent recovery path when the product claims one exists. Export the information and test it instead of relying on a marketing sentence.

DIY multisig removes the provider but leaves every task with the household: device diversity, key generation, backups, descriptor storage, software compatibility, transaction signing, inheritance, and periodic testing.

Device diversity can reduce one-vendor risk. It can also make the process harder to maintain. Device diversity helps only when the family can maintain the software, firmware, cables, and signing process over time.

Institutional custody is a different trade-off, not a beginner version of self-custody.

The institution controls the keys and the withdrawal process. That can protect the household from personal key loss, technical mistakes, and a family being asked to execute a complex wallet recovery during a crisis. It may also provide statements, administrative support, beneficiaries, trust or estate procedures, and a legal or contractual path when access is disputed.

The trade-off is counterparty risk, bankruptcy or operational risk, identity verification, withdrawal restrictions, jurisdiction, privacy, and less direct control. The account security and family process still matter. An institution does not remove risk; it transfers part of it.

An intentional split is an architecture rather than another custody product.

The household may keep a directly controlled sovereign reserve, use collaborative multisig for a family-accessible pool, and hold retirement-account exposure through a professional custodian. Give each pool a job and use each additional method to remove a named failure.

The split becomes useful when one method, provider, device family, or person would otherwise threaten too much of the plan.

It becomes harmful when the family now has several systems, vendors, passwords, devices, and recovery procedures that nobody can maintain.

Compare every setup on the same questions:

- What does one stolen component allow?
- What does one lost component destroy?
- Which provider, device, software, and location must still work?
- How much direct control remains?
- What support or legal process exists?
- How does recovery work after ten years?
- Can the family execute or get help?
- What happens when the owner, provider, device, or law changes?
- If the entire pool became inaccessible, would the financial plan survive?

Use rough scale instead of putting exact balances into a custody worksheet: replaceable, meaningful, or life-changing.

A single method can be appropriate for a replaceable or noncritical amount when recovery is proven and simplicity is valuable.

A life-changing amount deserves a harder One-Failure Test. The household should be able to explain why no single failure can destroy too much of the plan before choosing direct custody, multisig, institutional custody, or a split.

Do not move a life-changing stack directly into a new advanced setup.

Build a small test wallet or account. Send and receive. Lose or replace one component on purpose when the process allows it. Recover it. Export the public recovery information. Test the provider-independent path when one is promised. Walk the family through the first call and the role each person has.

Document the process without documenting the secrets.

The safest architecture is not the one with the most hardware or the strongest ideological label. It is the simplest combination that removes the household's actual failure points, preserves the amount of direct control the household values, and can still be recovered by the people who inherit the responsibility.

---

## A7.2 What self-custody actually asks of you

> **Gate.** Research complete. Record as an operational-responsibility lesson; verify any named device or vendor behavior before mentioning it.

Self-custody removes a financial institution from the spending decision. Self-custody moves more trust and responsibility onto you.

You still rely on the device manufacturer, firmware, wallet software, random-number generation, the computer or phone used to coordinate a transaction, and your own ability to verify what is happening.

Your job is to generate keys safely, verify addresses on the trusted device, protect recovery material, maintain devices and software, understand fees, avoid scams, and leave a recovery process somebody else can use.

Move into self-custody when the skill and need for direct control justify owning the operational risk. Identity and online pressure are poor reasons to take that responsibility.

Start with a trivial amount.

Receive it. Send part of it. Verify the address on the device. Use the correct vendor-supported backup check or recovery procedure. Prove that the backup restores the intended wallet.

Then ask whether the setup survives ordinary life:

- a lost phone;
- a failed device;
- a house fire;
- travel;
- coercion;
- incapacity;
- death;
- or simply forgetting the process after five years.

Maintenance is part of the job. Firmware and wallet software change. Devices become unsupported. A backup can be moved or damaged. A passphrase can be forgotten. A multisig descriptor can be lost. A family member who once understood the process may no longer be available.

Schedule a yearly recovery exercise using a test wallet or another procedure that does not expose live secrets. Review the locations, people, devices, software, and provider contacts.

Self-custody should create confidence, not constant fear.

A smaller amount in a simple, tested setup is better than a life-changing amount in a complex setup copied from somebody else. And keeping some professionally supported Bitcoin is not a failure of conviction when it solves a real family or operational risk.

The question is not whether self-custody is morally better. The question is which risks you want to own directly and whether the household can keep owning them for decades.

---

## A7.3 Run the One-Failure Test across methods and providers

> **Gate.** Research complete. Verify provider and device facts before naming them; no vendor-specific recommendation is implied.

Concentration risk is not only holding too much Bitcoin.

It can also mean every recovery path depends on the same company, custody method, device family, software, location, or person.

An institution can fail operationally, freeze withdrawals, change jurisdiction, or enter bankruptcy.

A hardware-wallet vendor can ship a flawed update or disappear.

A wallet application can stop supporting an old format.

A physical location can be destroyed.

One family member can become unavailable.

And one custody method can protect the entire life-changing stack even when there are several devices or accounts inside that method.

List the dependencies for each meaningful Bitcoin pool:

- the job of the Bitcoin;
- rough scale: replaceable, meaningful, or life-changing;
- who controls withdrawals;
- which devices and software are required;
- where the recovery components are distributed;
- where the public wallet policy or descriptor is retained;
- which provider or institution must cooperate;
- how the family gets help;
- and who knows the process.

Then look for correlated failure.

Three keys in three envelopes are not independent if all three are in the same house.

Two hardware devices are not full vendor diversity if they rely on the same secure element, firmware path, and companion software.

Two exchanges are not independent if both rely on the same custodian.

A self-custody wallet and a collaborative multisig can still share a single person, location, or undocumented family process.

The One-Failure Test is:

> Could one lost recovery component, one frozen account, one provider failure, one home disaster, one coercion event, or the owner's incapacity materially damage the family's plan?

Run that test against each life-changing pool and then against the architecture as a whole.

A useful second question is:

> If this entire pool became inaccessible, would the financial plan still survive?

Identify which loss would be catastrophic and decide whether that exposure is intentional.

Separate custody pools can make sense when they have separate jobs or when one failure would otherwise threaten too much of the plan.

For example, a household may keep a directly controlled sovereign reserve and use a professionally supported method for the family-accessible or retirement-account portion. That can preserve direct control without making the whole plan depend on one self-custody process.

The opposite can also be true. A household that values simplicity and has a well-tested setup may be safer with one method than with four systems nobody can maintain.

Diversification has a cost: more devices, more providers, more interfaces, more recovery documents, and more ways for the family to get confused.

Use the fewest independent systems that remove the catastrophic failures.

Every additional method has to solve a named risk. Set a maximum exposure to one provider or failure domain only when the household can explain what that limit protects against.

At the annual review:

1. Reclassify the pools by rough scale. A meaningful amount can become life-changing without the custody process changing.
2. Check whether two supposedly separate pools still share a hidden provider, device, software, person, or location.
3. Test one recovery path.
4. Ask what one event could still affect everything.
5. Fix the largest shared dependency before adding more complexity.

A setup does not become safer merely because the diagram has more boxes. It becomes safer when a real failure can happen and the family plan still survives.

---

## A7.4 UTXOs, dust, consolidation, and address use

> **Gate.** Research complete. Verify current wallet behavior and network fees before demonstrating; use a test wallet and never expose live addresses unnecessarily.

A Bitcoin wallet balance is made of individual unspent transaction outputs, or UTXOs. They are closer to separate bills in a wallet than one bank-account balance.

When you spend, the wallet selects one or more UTXOs as inputs. The transaction fee is driven more by the data size and number of inputs and outputs than by the dollar amount being sent.

That is why many tiny withdrawals can become expensive later. Spending a small UTXO can cost a meaningful percentage of its value when fees are high.

There is no permanent minimum withdrawal threshold that works in every year. Bitcoin's dollar price and the fee market change. The useful practice is to avoid automatically creating a large pile of tiny outputs and to consider batching withdrawals when the custody and counterparty trade-off is acceptable.

Consolidation spends several UTXOs into a smaller number of new outputs. Doing it during a low-fee period can reduce the number of inputs needed later.

Consolidation also has privacy costs. Inputs combined in one transaction become linked on-chain, and the resulting larger output may reveal more about the wallet's history or future spending. Do not consolidate every output automatically merely because fees are temporarily low.

Coin control lets an experienced user choose which UTXOs are spent. It can help with privacy, accounting, and avoiding uneconomic outputs, but it adds room for mistakes. Learn it on a test wallet before using it with meaningful funds.

Address reuse reduces privacy because multiple receipts become easy to associate. A modern wallet normally generates a new receive address from the same wallet for each payment. Verify the address on the trusted signing device before sharing it.

Keep tax lots and UTXOs conceptually separate. One is an on-chain spendable output; the other is a tax-accounting record. A transaction can combine UTXOs from several tax lots. The tax records still need to identify which lot was disposed of.

Review UTXO health at the annual custody check: too many tiny outputs, any consolidation worth planning, current fees, privacy implications, and whether the wallet and backup still reconstruct the same addresses.

---
