ADVANCED = {
    "A6.2": {
        "title": "Sell, borrow, or hold when the plan needs a year of spending",
        "gate": "Research complete. Targeted CPA or EA review before publication; verify lender terms and current basis-at-death law before relying on them.",
        "body": r"""
A Bitcoin-heavy retirement plan can fund a year of spending by selling, borrowing, using other assets, or leaving a core position untouched while the Reserve and Bridge do the work.

These are tools, not moral positions.

Selling is the simplest. The household receives cash, the gain or loss is reported using the lot basis, and there is no lender or repayment obligation. Selling can be especially attractive in a low-income year where part of the long-term gain may fall into a lower federal bracket.

The cost is the tax, the loss of future upside on the Bitcoin sold, and any emotional difficulty with reducing the position.

Borrowing keeps the collateral exposure at the beginning and generally does not create income merely because bona fide loan proceeds were received. The cost is interest, lender risk, LTV risk, collateral outside self-custody, and a repayment problem that still has to be solved.

A later forced liquidation is a sale and can create tax. A long bear market can also make refinancing or collateral top-ups harder exactly when the household has less flexibility.

Holding means deciding that a core Bitcoin position is not a normal spending source. The Reserve, Bridge, income floor, and other accounts fund life while the core compounds or remains part of the estate.

Under current federal rules, inherited property may receive a basis adjustment at death, but exceptions, ownership structure, estate inclusion, and future law matter. Do not build the entire plan around one sentence about a step-up without legal and tax review.

Compare the tools on the same year of spending.

For a sale, calculate the gross sale required, the basis of the selected lots, federal and state tax, and Bitcoin remaining.

For a loan, calculate the proceeds, interest, starting LTV, margin and liquidation prices, collateral posted, repayment source, and Bitcoin still in custody versus with the lender.

For holding, identify exactly which Reserve, Bridge, income, or non-Bitcoin asset pays the bill and whether that source can keep doing the job through a long drawdown.

The best plan may mix the tools. A household can sell high-basis lots in a low-tax year, use a conservative loan for a temporary need during a strong market, and preserve a separate core position.

The weak version is choosing "never sell" first and forcing every future need into a loan. The decision should come after the tax, risk, cash-flow, and family-comfort comparison.

Use the Loans workbench as a sandbox. Nothing should change in the baseline until the strategy has been previewed, the lender terms are verified, and the household can explain how the debt gets repaid if Bitcoin does not cooperate.
""",
    },
    "A7.1": {
        "title": "Passphrase, collaborative custody, and DIY multisig",
        "gate": "Research complete. Verify exact devices, wallet software, descriptors, provider roles, and recovery procedures before any setup-specific footage.",
        "body": r"""
Advanced custody is only safer when the added complexity removes a real risk that the household understands.

A passphrase wallet uses a normal seed plus an additional passphrase to derive a different wallet. The passphrase is sometimes called a twenty-fifth word, but it does not have to be one word and it is not a second signature.

Anyone with the seed and exact passphrase can control the wallet. A wrong passphrase can still produce a valid but different wallet, which makes recovery mistakes especially dangerous.

The benefit is that possession of the seed alone may not reveal the intended wallet. The risk is losing, mistyping, or failing to communicate the passphrase. Test the exact recovery with a trivial amount and store the recovery components according to a deliberate plan.

A two-of-three multisig wallet uses three keys and requires two valid signatures. One lost key does not necessarily destroy access, and one stolen key does not spend alone.

The wallet also depends on public configuration information: the keys or xpubs, threshold, script type, derivation paths, and related descriptor data. This configuration has no private spending key by itself, but it is essential to reconstructing the wallet correctly and can reveal privacy information.

Collaborative custody shares the operational burden with a provider. The customer may hold two keys while the provider holds one, or use another arrangement defined by the service. The provider may also retain the wallet configuration, help verify an executor, and guide recovery.

The trade-off is dependence on the provider's continued operation, policies, identity checks, jurisdiction, security, fees, and privacy. Understand how to recover without the provider when the product claims that is possible.

DIY multisig removes the provider but leaves every task with the household: device diversity, key generation, backups, descriptor storage, software compatibility, transaction signing, inheritance, and periodic testing.

Device diversity can reduce one-vendor risk, but too many device types can also make the process harder to maintain. Each component should have a reason.

Compare the three setups on:

- what one stolen component can do;
- what one lost component does;
- how many people and locations are required;
- how recovery works after ten years;
- how the family gets help;
- what happens when a vendor or provider disappears;
- ongoing cost and maintenance;
- and whether the legal plan matches the technical control.

Do not move a life-changing stack directly into a new advanced setup. Build a small test wallet, send and receive, replace or lose one component on purpose, recover it, and document the process without writing secrets into the documentation.

The safest setup is not the one with the most hardware. It is the simplest design that removes the household's actual failure points and can still be recovered by the people who will inherit the responsibility.
""",
    },
    "A7.2": {
        "title": "What self-custody actually asks of you",
        "gate": "Research complete. Record as an operational-responsibility lesson; verify any named device or vendor behavior before mentioning it.",
        "body": r"""
Self-custody removes a financial institution from the spending decision. It does not remove responsibility. It moves the responsibility to you.

You have to generate the keys safely, verify addresses, protect backups, maintain devices and software, understand fees, avoid scams, and leave a recovery process somebody else can use.

That does not mean everybody should leave Bitcoin on an exchange. It means moving to self-custody should follow skill rather than identity.

Start with a small amount. Receive it, send part of it, verify the address on the device, wipe or check recovery using the correct vendor procedure, and prove the backup.

Then ask whether the setup can survive ordinary life: a lost phone, a failed device, a house fire, travel, incapacity, death, or simply forgetting a process after five years.

Maintenance is part of the job. Firmware and wallet software change. Devices may become unsupported. A backup can be moved by somebody else. A passphrase can be forgotten. Multisig configuration can be lost.

Schedule a yearly recovery exercise using a test wallet or a procedure that does not expose the live secrets. Review the locations, people, devices, and provider contacts.

Self-custody should create confidence, not constant fear. A smaller amount in a simple, tested setup is better than a large amount in a complex setup copied from somebody online.
""",
    },
    "A7.3": {
        "title": "Avoid custody concentration in one institution, vendor, or failure path",
        "gate": "Research complete. Verify provider and device facts before naming them; no vendor-specific recommendation is implied.",
        "body": r"""
Concentration risk is not only holding too much Bitcoin. It can also mean every recovery path depends on the same company, device family, software, location, or person.

An institution can fail operationally, freeze withdrawals, change jurisdiction, or enter bankruptcy. A hardware-wallet vendor can ship a flawed update or disappear. A single wallet application can stop supporting an old format. A physical location can be destroyed. One family member can become unavailable.

List the dependencies for each meaningful Bitcoin pool:

- who controls withdrawals;
- which devices and software are required;
- where the backups are;
- where the public wallet configuration is;
- which provider or institution must cooperate;
- and who knows the process.

Then look for correlated failure.

Three keys in three envelopes are not independent if all three are in the same house. Two hardware devices are not full vendor diversity if they use the same secure element, firmware path, and companion software. Two exchanges are not independent if both rely on the same custodian.

Diversification also has a cost. More vendors and devices create more maintenance, more interfaces, and more ways for the family to get confused. The goal is not maximum fragmentation.

Use separate custody pools when they have separate jobs or when one failure would otherwise threaten the entire stack. Keep the recovery plan simple enough that every pool can be identified and maintained.

At the annual review, ask what one event could still affect everything. Fix the largest remaining shared dependency rather than adding complexity without a specific threat.
""",
    },
    "A7.4": {
        "title": "UTXOs, dust, consolidation, and address use",
        "gate": "Research complete. Verify current wallet behavior and network fees before demonstrating; use a test wallet and never expose live addresses unnecessarily.",
        "body": r"""
A Bitcoin wallet balance is made of individual unspent transaction outputs, or UTXOs. They are closer to separate bills in a wallet than one bank-account balance.

When you spend, the wallet selects one or more UTXOs as inputs. The transaction fee is driven more by the data size and number of inputs and outputs than by the dollar amount being sent.

That is why many tiny withdrawals can become expensive later. Spending a small UTXO can cost a meaningful percentage of its value when fees are high.

There is no permanent minimum withdrawal threshold that works in every year. Bitcoin's dollar price and the fee market change. The useful practice is to avoid automatically creating a large pile of tiny outputs and to consider batching withdrawals when the custody and counterparty trade-off is acceptable.

Consolidation spends several UTXOs into a smaller number of new outputs. Doing it during a low-fee period can reduce the number of inputs needed later.

Consolidation also has privacy costs. Inputs combined in one transaction become linked on-chain, and the resulting larger output may reveal more about the wallet's history or future spending. Do not consolidate every output automatically merely because fees are temporarily low.

Coin control lets an experienced user choose which UTXOs are spent. It can help with privacy, accounting, and avoiding uneconomic outputs, but it adds room for mistakes. Learn it on a test wallet before using it with meaningful funds.

Address reuse reduces privacy because multiple receipts become easy to associate. A modern wallet normally generates a new receive address from the same wallet for each payment. Verify the address on the trusted signing device before sharing it.

Keep tax lots and UTXOs conceptually separate. One is an on-chain spendable output; the other is a tax-accounting record. A transaction can combine UTXOs from several tax lots, and moving Bitcoin does not automatically establish which tax lot was sold.

Review UTXO health at the annual custody check: too many tiny outputs, any consolidation worth planning, current fees, privacy implications, and whether the wallet and backup still reconstruct the same addresses.
""",
    },
}
