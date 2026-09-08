# A7.1 — Compare passphrase, multisig, and professional support

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: DEVICE_CUSTODY_REVIEW
Sources: CUSTODY, DICTATION, PRIMARY, OWNER
Use when: the basic custody arrangement leaves a named failure that another architecture may address.

### Read aloud

Choose a more advanced custody arrangement only after naming the failure it needs to address. A passphrase, multisig, professional custody and collaborative support solve different problems and require different recovery information.

A passphrase changes the wallet derived from the recovery material. It adds another exact secret to preserve. A wrong passphrase can produce a different valid wallet, which makes testing and documentation important. It does not create a second cryptographic signer or a legal approval process.

Multisig requires a defined combination of keys. A two-of-three policy can survive one unavailable key if the other required resources remain usable. It also requires configuration information and compatible recovery tools. Test which combinations work, including a provider-independent path when the arrangement claims to provide one.

Collaborative support can help a household maintain that process. Read which key the provider holds, what it can and cannot do, the approval process, recovery fees, identity requirements, and what happens if it disappears. Provider involvement is not automatically equivalent to provider control of the entire asset.

Institutional custody may simplify key management and family administration, but it creates a contractual and counterparty dependence. Review ownership, segregation, withdrawal restrictions, legal process, and the exact services offered. A retirement or brokerage structure adds its own wrapper and beneficiary rules.

An intentional split can preserve direct control over one portion and professional support for another. Define the purpose and maximum exposure of each portion. More methods are useful only when they remove meaningful dependence without creating an unmaintainable process.

Use a non-secret comparison table: protection gained, new failure introduced, recovery requirements, family usability, cost, and review cadence. Keep the signing material and sensitive configuration outside the ordinary course workbook.

Before moving meaningful funds, conduct a small-value test using current vendor instructions. Verify the complete recovery path, not merely the ability to sign one transaction today. Involve the professional needed for the actual arrangement.

Test the proposed improvement under the failure you named. If a component or provider is unavailable, can the remaining resources recover the intended wallet under that actual setup? A second device is not automatically a second signer, and a passphrase is not a substitute for a tested threshold policy. Adding complexity helps only when the household can still maintain and recover the arrangement.

Return with the simplest method that meets the household's control and continuity needs, the risk it still retains, and the exact safe test required. Keep configuration and secrets in the protected recovery process, not the ordinary family worksheet.

### Production notes

Exact BIP39/passphrase and multisig configuration claims need current primary vendor/spec verification. No funded seed demonstration. Attorney/custody coordination for actual family design. Return to 7.1–7.2 and 8.2.

### Member checkpoint

- Name the failure each proposed architecture addresses.
- Test the complete recovery path and dependencies.
- Document the non-secret choice and retained risks.

### Source-led visual and teaching notes — not spoken

Protection gained / new responsibility / failure retained / recovery requirements / family starting path. No secret strings, descriptor contents or universal passphrase-split design.

Editorial reason: Evaluate advanced custody against a specific unavailable-component case rather than complexity or wealth level.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.

### Advanced demonstration plan — not spoken

Compare the actual methods using public specifications and the relevant provider agreement. Rehearse the non-secret absence path and separately verify the claimed signing/recovery combinations on a safe test setup. A practice test does not certify a different funded wallet. Return to 7.1–7.2 and 8.2.

Use this with the linked core working chapters; it does not create another required lesson or claim an app/device test was performed. Record precise controls and actual outcomes only after the relevant gate is met.
