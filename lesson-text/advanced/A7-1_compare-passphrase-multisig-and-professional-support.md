# A7.1 — Compare passphrase, multisig, and professional support

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: DEVICE_CUSTODY_REVIEW
Sources: CUSTODY, DICTATION, PRIMARY, OWNER
Use when: the basic custody arrangement leaves a named failure that another architecture may address.

### Read aloud

Begin with the failure you want to address. A passphrase, multisig, and professional custody solve different problems and create different responsibilities.

A passphrase changes the wallet derived from the recovery material. It adds another exact secret to preserve. A wrong passphrase can produce a different valid wallet, which makes testing and documentation important. It does not create a second cryptographic signer or a legal approval process.

Multisig requires a defined combination of keys. A two-of-three policy can survive one unavailable key if the other required resources remain usable. It also requires configuration information and compatible recovery tools. Test which combinations work, including a provider-independent path when the arrangement claims to provide one.

Collaborative support can help a household maintain that process. Read which key the provider holds, what it can and cannot do, the approval process, recovery fees, identity requirements, and what happens if it disappears. Provider involvement is not automatically equivalent to provider control of the entire asset.

Institutional custody may simplify key management and family administration, but it creates a contractual and counterparty dependence. Review ownership, segregation, withdrawal restrictions, legal process, and the exact services offered. A retirement or brokerage structure adds its own wrapper and beneficiary rules.

An intentional split can preserve direct control over one portion and professional support for another. Define the purpose and maximum exposure of each portion. More methods are useful only when they remove meaningful dependence without creating an unmaintainable process.

Use a non-secret comparison table: protection gained, new failure introduced, recovery requirements, family usability, cost, and review cadence. Keep the signing material and sensitive configuration outside the ordinary course workbook.

Before moving meaningful funds, conduct a small-value test using current vendor instructions. Verify the complete recovery path, not merely the ability to sign one transaction today. Involve the professional needed for the actual arrangement.

Return to the core custody map with the simplest architecture that meets the household's requirements and can be maintained over time. A complex setup that only one person understands has not solved the family problem.

### Production notes

Exact BIP39/passphrase and multisig configuration claims need current primary vendor/spec verification. No funded seed demonstration. Attorney/custody coordination for actual family design. Return to 7.1–7.2 and 8.2.

### Member checkpoint

- Name the failure each proposed architecture addresses.
- Test the complete recovery path and dependencies.
- Document the non-secret choice and retained risks.
