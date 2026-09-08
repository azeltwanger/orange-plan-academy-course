# 7.1 — Choose who controls each part of the Bitcoin

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/sessions/07-custody.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: teach
Gate: CUSTODY_REVIEW
Sources: CUSTODY, DICTATION, BRAIN, OWNER, PRIMARY

### Read aloud

Start by naming the job of each meaningful Bitcoin holding. Long-term money you want to control directly, retirement-account exposure, near-term liquidity, and collateral for a loan have different requirements.

Then ask what you are trying to protect against. Losing a recovery backup, a provider freezing access, a home disaster, incapacity, a dishonest helper, and family members being unable to carry out the process are different failures. The custody choice should solve the failures that matter to this household.

Direct self-custody gives you control of the signing keys. That reduces dependence on a company to authorize access. You also take responsibility for backup, recovery, physical security, transaction verification, and a process that still works when you are unavailable.

An institutional custodian takes on some operational responsibilities and may provide support, administration, and a documented legal process for the family. In return, you depend on its security, financial condition, withdrawal rules, legal obligations, and ability to serve you. Read the actual ownership and custody agreement rather than assuming every provider holds assets in the same way.

Collaborative multisig can divide signing authority and provide professional support. In a two-of-three arrangement, two valid signers are required under the wallet's policy. One lost key may be survivable, but the household still needs the wallet configuration, accessible remaining keys, and a tested process. The provider's role depends on the actual key distribution and agreement.

An intentional split uses more than one method because different portions have different jobs or because one failure would otherwise affect too much of the plan. It adds maintenance. An extra account earns its place when it removes a meaningful dependence the household can actually manage.

How much direct control matters is a personal decision. Some households want a meaningful amount no institution can restrict. Others value support and family administration more. You can combine those preferences instead of asking one custody method to do every job.

For Alex and Morgan, direct Bitcoin and professionally custodied Bitcoin are separate pools. They also have a spot Bitcoin fund in retirement accounts. The fund gives market exposure through a security; it does not give them the same direct control of underlying Bitcoin as their own keys. The account wrapper, investment, and custody method each need to be understood.

Now run the One-Failure Test. Could one device, backup, person, provider, location, or account-recovery process materially damage the family's financial plan? If so, name the failure and compare the simplest way to reduce it.

Two providers are not independent merely because the apps have different names. They may share a custodian or another important dependency. Several backups in one house share a location risk. A complex setup also creates risk if only one person knows how it works.

The amount at stake changes the consequences. A setup that was adequate for a replaceable balance may need review when it represents the household's retirement. That does not automatically require multisig or another account. It requires a fresh look at what a single failure could do and whether the recovery process is adequate.

Choose the current direction before moving funds. State the job of each pool, the control preference, the main protection gained, and the risk retained. Then identify the first unfinished action. It may be proving a backup, reviewing the provider agreement, hardening access, or simplifying a process the family cannot follow.

The next lessons turn that decision into operational proof and a safe record. The goal is a setup the household can maintain, explain, and recover under the conditions that actually matter.

### Production notes

Use four-method comparison and the One-Failure Test. Do not present a provider or wallet brand as approved. Source comparison covers operational trade-offs, not a security certification. Preserve distinction between a signing key and a wallet descriptor; a descriptor alone does not sign. No real balances, seed words, passwords, or recovery locations on camera.

### Member checkpoint

- Assign a custody job and control preference to each meaningful pool.
- Name the remaining failure each method creates.
- Choose one architecture and one next protection action.
