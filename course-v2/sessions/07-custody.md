# Session 7 — Choose and prove the custody plan

Keep Austin's trade-off framework. The older exchange→hardware→passphrase→multisig wealth ladder is historical, not a recommendation. W07 documents non-secret decisions in Protect; D07 is the separate exact-device demonstration.

## 7.1 — Choose who controls each part of the Bitcoin
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

## 7.2 — Prove recovery before meaningful money depends on it
Kind: teach
Gate: DEVICE_CAPTURE
Sources: CUSTODY, DICTATION, PRIMARY

### Read aloud

A backup becomes useful when you know what it restores and have proved the process. The first recovery attempt should happen under calm conditions, using a small test arrangement rather than the family's only funded wallet.

A hardware wallet is a signing device. Your Bitcoin is recorded on the network; the device protects the information used to authorize transactions. Losing the device can be recoverable when the correct backup and required wallet information remain available. Losing the only usable recovery material can be a very different problem.

Obtain the device through the manufacturer's verified channel or an explicitly authorized source, and follow the current authenticity and setup instructions for that model. Generate your own new wallet through the supported process. Treat a device supplied with prewritten recovery words as compromised.

Identify the backup standard being used. Different devices and wallet configurations can require different information. A word count alone does not establish universal compatibility. A passphrase, a special recovery scheme, an account derivation, or a multisig policy can add requirements beyond the words someone wrote down.

Protect the backup offline using an appropriate physical method. Paper and durable metal have different resistance to fire, water, and deterioration. More copies may improve availability while increasing exposure to theft. Placement should be chosen around the failures you are trying to survive, and sensitive locations belong in a separate protected recovery process.

Use a small test transaction and verify the receiving address through the device's trusted display where the supported process provides it. A computer screen can be misleading if the computer or interface is compromised. Transaction details need independent attention before approval.

Then validate the backup through the device's supported backup-check function or a recovery on a compatible spare device. Confirm the expected wallet and test balance. Where a reset-and-restore demonstration is appropriate, perform it only after backup validation and only in a controlled test setup. Never wipe the only working device protecting meaningful funds simply because a generic course checklist says reset next.

A passphrase requires special care. It is an additional exact input that can create a different wallet. A mistyped passphrase may open a valid but empty wallet rather than produce an obvious error. The device PIN protects access to the device; it is not a substitute for the recovery backup or passphrase.

For multisig, test the intended signing threshold and retain the wallet policy or configuration information needed for recovery. Having enough seed backups is not automatically proof that heirs can reconstruct the correct wallet. The recovery plan must include compatible tools and the information required by that particular setup.

For Alex and Morgan, the direct-custody pool remains a documented open action until the test succeeds. The account can be listed in Orange Plan without pretending recovery is proven. Once the test is complete, they record that it was tested and the next review date, while the secret material stays outside the financial-planning app.

The separate device demonstration shows this process on the exact hardware, firmware, and backup method used for filming. Follow the official instructions for your own setup. Stop when a step differs materially from what is shown rather than improvising with funded assets.

You are finished when you have verified what information is required, proved recovery using the safe test procedure, and made the process maintainable. Buying a device and writing down words are preparation. The evidence that matters is a successful recovery of the intended wallet.

### Production notes

D07 exact-device gate: official instructions, authenticity, backup standard, firmware, spare-device/backup check, test-only funds, address verification, reset safety, and recovery proof. Never display usable real or demo seed phrases in distributable course footage; mask/cut secrets rather than teaching from a reusable public funded wallet. Vendor procedures must be freshly checked.

### Member checkpoint

- Identify the complete recovery information for the actual setup.
- Validate the backup before any destructive test.
- Record a successful small-value recovery and the next review date.

## 7.3 — Harden accounts and remove the largest shared failure
Kind: teach
Gate: CUSTODY_REVIEW
Sources: CUSTODY, DICTATION, PRIMARY, CLIENT_THEMES

### Read aloud

A strong wallet can still sit inside a weak household process. Email access, exchange logins, recovery channels, physical storage, and the way you respond to a suspicious message all deserve attention.

Start with the email account used to recover financial accounts. Use a unique strong password and the strongest supported authentication you can maintain. A phishing-resistant security key or passkey can reduce attacks that rely on a convincing fake sign-in page. An authenticator code is useful where that stronger option is unavailable, but a code can still be entered into the wrong site.

Secure the recovery path too. An excellent primary login can be undermined by a weak recovery email, easily abused phone reset, or lost backup authentication method. Keep the recovery information private and make sure a lost phone or key does not leave you unable to access the account.

For exchanges and custodians, review withdrawal controls, address allowlisting where supported, delays, alerts, and the provider's recovery process. These controls have different limitations. An allowlist does not protect a seed stored in the wrong place, and a delayed withdrawal does not eliminate provider or account-takeover risk.

Use trusted bookmarks or enter the known address when logging in. A message that says the account is in danger should lead you to independently contact the provider, not to follow the message's link or call the number it supplied. Urgency is often used to make someone skip verification.

No legitimate support process needs your seed phrase or private key. A request to move funds to a supposed safe wallet, send money to unlock a withdrawal, or accept an unsolicited recovery expert deserves an immediate stop. Verify through a known official channel before doing anything with the assets.

Now look for shared failures. Two backup envelopes in the same building can be lost in the same disaster. Two devices may depend on the same software or vendor. Two providers may rely on one custodian. A family process can depend entirely on one technically capable person.

Rank the few weaknesses by consequence and likelihood, then fix one at a time. An additional method should solve the failure you named. Adding hardware or accounts without improving independence can make the household harder to maintain without making recovery more robust.

For the Reed household, one task might be hardening the email and custodial logins. Another might be proving the direct-custody backup. A third might be making sure Morgan knows the safe starting instructions and which professional to call. They do not need to distribute all the secrets to complete that orientation.

Review physical risk as well. Publicly sharing exact holdings or locations can create exposure. The financial plan needs enough information to explain the assets and their custody, not a complete map for finding and moving them. Keep sensitive recovery instructions separate and appropriately protected.

A calm routine helps with transactions too. Verify the destination, amount, network, fee, and purpose before authorizing a move. Use the current official procedure and a small test when appropriate. Stop when a screen, address, or instruction differs from what you expected.

This working-session chapter records the top unfinished action, the responsible person, and the deadline. The external security work happens with the provider or device. Mark it complete only when the control was actually enabled or the process tested.

Finish with fewer ways for a single mistake to affect the entire plan. The improvement should be something the household can explain: a stronger login, a verified recovery route, less concentration in one dependency, or a family process that works when you are unavailable.

### Production notes

CISA phishing-resistant MFA guidance supports the authentication distinction. Avoid statistical claims such as most Bitcoin losses occur by one specific cause unless sourced. Do not claim passkeys prevent every takeover or every provider supports all controls. No personal bank-fraud story invented for Austin.

### Member checkpoint

- Secure primary and recovery channels for critical accounts.
- Identify shared provider, device, location, and person dependencies.
- Complete and verify one material security improvement.

## 7.4 — Record a usable custody plan without exposing secrets
Kind: teach
Gate: APP_CAPTURE
Sources: CUSTODY, OWNER, APP, MAINTENANCE

### Read aloud

The custody record should help the household understand what exists and how to start the right process. Keep it useful without turning the financial plan into a source of signing authority.

For each meaningful pool, record the type of asset, the account or custody method, its intended job, the owner, and the relevant provider or professional contact. A rough scale may be enough in a separate family instruction document. The financial account record can retain its balance without duplicating that sensitive detail everywhere.

Then record the recovery status. Was the process tested? On what kind of setup? When is the next review? What remains unfinished? A statement that recovery has been proved should refer to an actual test of the relevant method, not confidence that it would probably work.

The family needs a starting point if you are unavailable. That might be contacting a named provider, attorney, executor, or technical helper. It should explain how to verify that contact and where the protected process is managed. Exact secret locations, passwords, passphrases, seed words, and complete recovery sequences stay out of Orange Plan and ordinary heir letters.

Operational ability and legal authority are separate. Someone may know how to sign without being entitled to move the assets. Another person may have legal authority but need technical help. The next session coordinates those roles. For now, identify which people and services the custody process depends on.

For Alex and Morgan, the direct-custody record says which method they use and whether recovery was tested. The institutional account record identifies the provider and the family-administration process that needs to be verified. The Bitcoin fund follows the brokerage account's legal and operational process. Each pool gets instructions appropriate to what it actually is.

Set the next review date and event-based triggers. A new device, changed firmware or backup method, a provider change, a new custodian, a larger balance, or a change in family roles can justify a fresh test. Years can pass while a setup quietly becomes harder to use because the people or software changed.

An encrypted Orange Plan export has a separate job. It may help restore financial-plan data when the supported restore process is available and verified. It is not a Bitcoin wallet backup. Keep the export password and restoration instructions protected, and never assume the existence of an export proves that every restoration feature in a changing release works.

In the working session, we will document the non-secret plan in Protect using only the fields the release supports. External tasks remain in the action list. If a recovery test or provider process is unfinished, the record should say so. A complete course step can include a clear pending action; it cannot label the underlying security work completed prematurely.

The finished custody plan answers four practical questions. How is each important pool held? What failure does that method protect against? What dependency remains? Who starts the process if you are unavailable?

Once those answers are clear, the family-handoff session can connect them to beneficiaries, legal documents, and the people authorized to act. The technical plan and the legal plan should support one another without putting the secrets into the course workbook.

### Production notes

W07 follows current Protect ownership and relevance states. No old estate-size tier dictates custody architecture. Backup/restore capability must be actually verified before promising recovery of app data. Do not store descriptors, xpubs, secret locations, or a complete signing route in the course worksheet.

### Member checkpoint

- Complete the non-secret custody map and honest recovery status.
- Name a first contact and review triggers.
- Keep financial-plan restoration separate from wallet recovery.
