# 8.2 — Connect legal authority with the actual recovery process

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/sessions/08-family-handoff.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: teach
Gate: ESTATE_CUSTODY_REVIEW
Sources: ESTATE, CUSTODY, DICTATION, PRIMARY

### Read aloud

A legal document and a technically recoverable wallet solve different parts of the same problem. The person entitled to act must have a usable process, and the person helping with the technology must understand the limits of that role.

Start with each asset's actual arrangement. Personally held Bitcoin, Bitcoin in a retirement account, a brokerage fund, an institutional custody account, and a trust-owned wallet can have different ownership and recovery paths. One set of instructions should not assume all of them work like a hardware wallet.

For direct single-signature custody, whoever has the required signing information may be able to move the Bitcoin. That practical ability is separate from legal entitlement. The handoff needs to manage access without leaving the legitimate process incomplete.

A passphrase is an additional secret used to derive a wallet. It does not turn a single-signature wallet into two legal signers. Dividing recovery words and a passphrase between people can introduce dependence on both components, but the suitability of that arrangement depends on the full design, secure storage, exact recovery, and legal roles. It is one possible design to review, not a universal inheritance rule.

Multisig uses a defined signing threshold. A two-of-three wallet can require two valid keys, together with the configuration needed to identify and use the intended wallet. Decide who controls each signing capability, which combinations can act, how backups are held, and what happens when a person or provider is unavailable.

A provider can help with recovery or administration, but its exact role must be verified. Can the household recover without it? Which documents does it require after incapacity or death? Does it provide technical support only, or does it control assets under an institutional arrangement? What changes if the provider stops operating?

For brokerage and retirement accounts, the institution's beneficiary and estate process governs the account access. Possessing a password is not a substitute for completing that process. Give the family the correct contact and documents rather than instructions to impersonate the owner.

For Alex and Morgan, we will make a non-secret table. Each row names the asset type, legal owner, person or role entitled to direct the process, operational helper or provider, whether the process has been tested, and the next verification. It never includes the signing material itself.

Then test the table under a simple scenario. Alex is unavailable for six months. Can Morgan identify the assets, contact the right professionals, and arrange ordinary household cash flow without improvising access to every Bitcoin holding? Next test a death scenario, where different legal steps apply.

Look for a circular dependency. The instructions may be behind a login controlled by the unavailable person. The password manager may depend on the same lost device as the email. The only technical helper may have moved or lost contact. These are practical failures you can identify before anyone is under stress.

Digital-account authority also deserves legal review. Providers may have online legacy settings and terms governing disclosure of information. Applicable state law and consent documents can affect what a fiduciary may receive. Technical possession of credentials and lawful access are not interchangeable.

The working session records what is known and the exact unanswered questions for the attorney and custody professional. It does not distribute secrets or settle legal title. Finish with an executable starting path for each meaningful pool and a clear plan to test the unresolved parts safely.

### Production notes

Retire the old universal heirs-hold-seed/executor-holds-passphrase instruction. No universal trustee concentration waiver. Explain descriptor/policy as sensitive recovery metadata without claiming it signs. Review digital-account consent against applicable law and provider terms; no instruction to bypass access controls.

### Member checkpoint

- Match each asset's legal owner and authorized role to its real recovery method.
- Identify incomplete or circular dependencies.
- Prepare specific legal and technical questions without storing secrets.
