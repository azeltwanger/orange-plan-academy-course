# A7.1 · Compare passphrase, multisig, institutional custody, and an intentional split

**Publication gate:** Research complete. Verify exact devices, wallet software, descriptors, provider roles, institutional terms, and recovery procedures before any setup-specific footage.

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
