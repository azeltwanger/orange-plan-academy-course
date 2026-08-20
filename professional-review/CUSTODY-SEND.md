# Orange Plan Academy — send-ready custody review

**Reviewer:** experienced Bitcoin custody practitioner  
**Source pass:** completed 2026-08-20  
**External status:** not reviewed

No spending secret will be requested or shared.

## Response codes

`OK` · `QUALIFY` · `DEVICE/PROVIDER SPECIFIC` · `UNSAFE` · `ADVANCED ONLY` · `REMOVE`

## Claims to review

| ID | Current course position | Specific question |
|---|---|---|
| C-01 | Custody is a trade-off, not a purity test; setup depends on amount, job, skill, family capability, and consequence of failure. | Is the framing balanced across third-party and direct custody? |
| C-02 | Four educational levels: hardened third-party account; tested single-signature wallet; family-ready self-custody; multi-key/professionally supported design. | Define minimum evidence for each without implying an industry standard or dollar threshold. |
| C-03 | Orange Plan, maps, letters, documents, photos, email, cloud notes, and AI never receive seed phrases, private keys, passphrases, PINs, passwords, xprvs, or wallet backups. | Which non-secret identifiers/configuration data may safely be documented and at what granularity? |
| C-04 | Buy and verify a device through current manufacturer guidance; never use supplied backup words or an already-created wallet. | Separate durable principle from device-specific walkthrough. |
| C-05 | The device is replaceable; the supported wallet backup and any required passphrase recreate access. A PIN protects the device, not the backup. | Supply backup-standard-neutral wording. |
| C-06 | Verify receive address and transaction details on the trusted display and complete a small receive and send test. | Add only the privacy/change-output/UTXO cautions essential to Core. |
| C-07 | Use a manufacturer backup check, compatible spare device, or supported recovery drill. Do not wipe the only meaningful device without a previously checked backup, understood process, and safe fallback. | Confirm the safest generic standard and successful-recovery evidence. |
| C-08 | Device and backup in one fire/theft/coercion domain are one failure domain; more complete backups also create more theft paths. | Confirm practical Core examples. |
| C-09 | FIDO security keys or properly implemented passkeys are preferred when supported; authenticator apps are generally stronger than SMS-only, but manually entered OTPs remain phishable. | Confirm terminology and backup/sync qualifications. |
| C-10 | Secure email and carrier recovery, preserve backup authenticators, and use provider withdrawal/session/API controls when understood. | Which controls are evergreen versus provider-specific? |
| C-11 | Unexpected support contact, urgency, remote-access software, and screen sharing are stop signs. Independently contact the provider. | Add any essential emergency or compromised-device sequence. |
| C-12 | Passphrases are Advanced unless the household understands that an exact passphrase may produce another wallet and has tested backup-plus-passphrase recovery. | Confirm device and compatibility qualifications. |
| C-13 | Dual control and redundancy are separate tests. | Confirm terminology. |
| C-14 | Do not hand-split ordinary backup words and call it multisig or threshold custody. | Should Shamir/SLIP39 remain Advanced only? |
| C-15 | A 2-of-3 wallet has three keys and any two sign; survivability also depends on recoverable configuration information. | Confirm exact generic wording. |
| C-16 | Descriptors/configuration records are not private keys but may reveal addresses and balances; keep protected redundant copies. | Supply coordinator-neutral language and estate-map guidance. |
| C-17 | Collaborative custody can reduce some one-key risks while adding provider, software, privacy, fee, succession, and recovery dependencies. | List minimum provider-independent recovery questions. |
| C-18 | Another family member practices on a small wallet rather than using the main backup as the first lesson. | Define a practical family-ready test. |
| C-19 | Protect can record type, people, documents, and dates but cannot prove recovery. | What real-world evidence should complete the custody area? |

## Current files in scope

- `scripts/07-1...`, `07-2...`, `07-3...`
- technical portions of `scripts/08-2...` and `08-3...`
- matching lesson text

## Return format

| ID | Code | Corrected wording / qualification | Technical source | Evergreen, maintained reference, or Advanced |
|---|---|---|---|---|
|  |  |  |  |  |

Finish with any unsafe sequence or missing failure mode that could cause permanent loss.
