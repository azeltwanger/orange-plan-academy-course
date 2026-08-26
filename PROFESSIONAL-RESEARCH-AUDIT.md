# Professional research audit — tax, custody, insurance, and estate

**Audit date:** 2026-08-25  
**Primary sources:** `research/PRIMARY-SOURCE-REGISTER.md`  
**Purpose:** separate factual research from Austin’s planning philosophy and from the state-, policy-, provider-, or taxpayer-specific judgment that still needs a credentialed signer.

## Bottom line

The old gate was too broad. It treated every sentence in a sensitive module as if only a professional could verify it. Most of the work is instead a primary-source and calculation audit. That audit is now complete.

The scripts are being corrected to this standard:

- durable federal or protocol mechanics may be taught after primary-source verification;
- current-year figures stay in the app or student text with a verification date;
- state law, policy language, provider behavior, and personal tax outcomes are never generalized;
- a professional signs only the narrow claims their credential actually covers;
- no reviewer gets to replace Austin’s planning position merely because they prefer another default.

## Tax findings

| Claim area | Research finding | Course treatment |
|---|---|---|
| Missing basis | The IRS requires substantiation. There is no general IRS safe harbor saying a self-created estimate is accepted merely because it is “reasonable and documented.” | Remove that sentence. Reconstruct from contemporaneous evidence; mark uncertainty in the plan; do not invent return basis. A zero-basis planning stress test is not a legal conclusion. |
| Specific identification | For self-custody, the units must be identified in books and records no later than the transaction, and records must establish that those units left the wallet. Broker-held units after 2025 must be identified using identifiers the broker accepts. | Teach specific identification as a documented instruction, not a retrospective choice. If identification fails, the IRS default is earliest-acquired units within that wallet or account. |
| HIFO | HIFO is not a universal exchange default or a magic toggle. It is one possible standing or transaction instruction when the identification and record requirements are met. | Replace “the exchange picks FIFO; choose HIFO” with the current wallet/account-specific rule. |
| Capital losses | Net capital losses offset gains first; an individual may then deduct the current annual limit against income and carry the remainder forward. | Keep the framework. Do not value every loss at the ordinary marginal rate; its value depends on what it offsets and when. |
| Wash sales | Section 1091 applies to stock or securities. Spot Bitcoin is generally outside that rule under current treatment; tokenized stock/security and future legislation can change the result. | State the current scope narrowly and require year-of-action verification. |
| Roth withdrawals | Qualified Roth distributions are tax-free. Nonqualified earnings and early distributions can have tax or penalty consequences. | Remove “never taxed again” as an unconditional statement. |
| RMD age | Current law uses age 73 for the intermediate cohort and age 75 for people attaining age 74 after 2032. Roth IRAs and, since 2024, designated Roth plan accounts do not have lifetime owner RMDs. | Name the couple’s applicable age as 75; tell every viewer to read their own applicable age in the current app/source. |
| Roth conversion | The taxable conversion amount is ordinary income. An RMD due for a year cannot itself be converted. Conversions also affect capital-gain stacking, ACA credits, Medicare premiums, NIIT, state tax, and other thresholds. | Replace “fill the bracket and stop” with an all-in marginal-cost comparison. The bracket top is a starting line, not the answer. |
| Inherited retirement accounts | Many nonspouse designated beneficiaries face a 10-year outside deadline, but eligible-designated-beneficiary exceptions and annual-distribution rules can change the schedule. | Remove “the kids have 10 years” as a universal rule. |
| Inherited Bitcoin basis | Inherited property generally receives date-of-death fair-market-value basis, subject to exceptions, estate inclusion, and consistent-basis rules. Gifts and some trust transfers follow different rules. | Replace “the gain disappears at death” with the general rule and its conditions. |
| Loan proceeds | Borrowed cash is generally not income because there is an obligation to repay. Collateral liquidation, sale, or debt cancellation may create income or gain. | Replace “borrowing creates no taxable event” with the narrower rule. |
| ACA planning | Marketplace credits depend on household income and benchmark-plan rules. Enhanced pandemic-era subsidies ended after 2025, and current eligibility must be checked annually. | Preserve MAGI coordination but remove assumptions that every household receives a subsidy or that old thresholds persist. |
| State relocation | Domicile, statutory residency, part-year rules, source income, entity/trust rules, and transaction timing differ by state. | Keep the lifestyle-first frame; remove the universal claim that only residence on the sale date controls. |

## Custody findings

| Claim area | Research finding | Course treatment |
|---|---|---|
| Custody levels | The four levels are Orange Plan’s educational framework, not an industry or protocol standard. | Label them as the course framework. |
| “Seed phrase” | BIP39 permits 12, 15, 18, 21, or 24 words; other wallets use other backup standards or multi-share backups. | Use “wallet backup or recovery material” first; use “seed phrase” only when the setup actually uses one. |
| Cross-device recovery | A BIP39 mnemonic is common but not universally portable. Recovery can also require the passphrase, script/address type, derivation information, and—for multisig—the wallet policy or descriptor. | Remove “the seed works in any hardware wallet from any manufacturer.” |
| Recovery test | Destroying the only working device is not the safest first validation. Many vendors support a backup check; a spare-device recovery avoids creating a single live failure during testing. | Teach vendor-supported backup check first, spare-device restore second, destructive reset only after validation and under the exact vendor procedure. |
| Passphrase | A BIP39 passphrase is an optional string; every passphrase derives a valid, different wallet. It is not literally “one extra word,” and it is not cryptographic multisig. | Teach Austin’s seven-random-word rule as his operational standard, not a protocol minimum. State that exact entry matters and every typo opens another wallet. |
| Seed splitting | Cutting a mnemonic into halves is not threshold secret sharing and creates a fragile all-parts-required backup. | Keep the warning. Point to a supported threshold-backup scheme or multisig when threshold recovery is wanted. |
| Multisig | A 2-of-3 wallet needs any two signing keys. Recovery also needs the wallet policy/descriptor or enough data to reconstruct it. | Keep the threshold arithmetic; add policy/descriptor recovery. |
| Descriptor/config file | A descriptor can reveal wallet structure and addresses, but it cannot sign by itself. One key plus a descriptor is still one key in a 2-of-3 wallet. | Remove the claim that storing a descriptor with one key quietly creates single-key control. Back it up for availability and protect it for privacy. |
| Collaborative custody | Provider power depends on the exact threshold, which keys the client holds, whether the client exports the descriptor/policy, and whether recovery works in compatible software without the provider. | Make every “provider can never…” statement conditional on those verified facts. |
| Device screen | Confirm the destination on the trusted display, but do not claim that malware or supply-chain compromise can never affect it. | Replace absolutes with a verified-address and official-software procedure. |
| Authentication | SMS is weak. TOTP is stronger but manually entered OTPs are not phishing-resistant. Security keys and passkeys can be phishing-resistant when correctly deployed. | Teach passkey/security-key first where supported, TOTP second, SMS last; keep backup keys and recovery codes separate. |
| UTXOs and dust | A UTXO is an output. “Dust” has a protocol/policy meaning; a larger UTXO can also be economically unattractive to spend when fees are high. Consolidation can reduce future input fees but link coins and reduce privacy. | Teach “economically uneconomic” separately from protocol dust and add the privacy cost of consolidation. |
| Transfer threshold | 0.01–0.02 BTC is Austin’s rule of thumb, not a Bitcoin rule. | Preserve it with an explicit fee/counterparty check. |

## Insurance findings

| Claim area | Research finding | Course treatment |
|---|---|---|
| Coverage-gap math | Annual shortfall × years minus liquid resources is a useful first pass, not a full needs analysis. It ignores timing, inflation, Social Security/survivor benefits, taxes, education, childcare, final expenses, debt payoff, asset liquidity, investment return, and the survivor’s choices. | Relabel the output as a rough first-pass range and route the final number to a licensed producer or fee-only insurance analyst. |
| Term life | Term provides death-benefit coverage for a stated period. Premiums may be level for a stated guarantee period, but product terms differ. | Remove the implication that all term policies are fixed-premium for the entire term. |
| Death-benefit taxation | Life-insurance death proceeds are generally excluded from federal income, but interest, transfer-for-value, ownership, and estate-tax issues can change the result. | Use “generally income-tax-free” and name the exceptions as professional-review items. |
| Permanent insurance | Permanent products combine lifelong coverage with cash-value and guarantee structures; charges, surrender terms, dividends, and assumptions vary. | Austin may state his preference for term in the example, but the course cannot reduce every permanent policy to “low-yield savings” or imply Bitcoin replaces every insurance purpose. |
| Disability | Benefit percentage, monthly cap, tax treatment, elimination period, benefit period, offsets, residual/partial benefits, and disability definition vary by policy. | Replace the invented net benefit with a worksheet that reads the actual certificate and compares after-tax benefits with the spending floor. |
| Umbrella | Umbrella is excess personal liability coverage and may add defense coverage, subject to required underlying limits and exclusions. | Remove the price-per-million claim; price actual policies. |
| Long-term care | Need, insurability, premiums, rate history, benefit triggers, elimination periods, inflation protection, state partnership rules, and alternatives vary. | Replace the universal “park it until your 50s or 60s” rule with an annual trigger based on health, caregiving exposure, assets, and insurability. |
| Health-sharing | A health-sharing arrangement is not insurance and generally has no legal obligation to pay. Terms differ materially by organization. | Austin’s CrowdHealth experience stays personal and dated; no provider mechanics are generalized. |
| Replacing or reducing coverage | A policy should not be canceled or allowed to lapse until any replacement is in force and the consequences are reviewed. | Add this to the graduation review. |

## Estate findings

| Claim area | Research finding | Course treatment |
|---|---|---|
| Executor authority | A will nominates an executor and directs probate assets. Authority generally begins after court appointment. Without a valid will, a court can appoint an administrator under intestacy law. | Remove “no document, no authority.” Teach the difference between nomination and appointment. |
| POA and health directive | A financial power of attorney is an incapacity tool and generally ends at death. A healthcare directive governs medical decisions, not inheritance. | State each document’s real job. |
| Beneficiary/POD/TOD | A valid designation generally transfers the covered asset outside the will, but plan terms, ERISA, spousal consent, QDROs, state law, community-property rules, and validity matter. | Keep “generally controls,” never “always,” and require provider verification. |
| Digital-asset authority | State enactments of RUFADAA often distinguish access to a digital asset from access to the content of electronic communications and may require explicit consent. | Add digital-asset and electronic-communications powers to the attorney checklist. |
| Heir letter/switch | These are operational communication tools. They confer no legal authority and do not override a beneficiary designation, will, trust, or court order. | State this directly. |
| Trust definition | A trust is a fiduciary relationship in which a trustee holds or administers property under the governing instrument; “container” is only shorthand. | Correct the definition. |
| Revocable trust | It generally remains in the grantor’s estate and avoids probate only for assets properly titled or assigned to it. Privacy and incapacity benefits vary. | Remove blanket claims that merely signing one avoids probate for everything. |
| Irrevocable trust | Estate exclusion, income-tax treatment, creditor protection, basis, control, and gift consequences depend on retained powers, completed transfer, terms, and state law. | Remove “irrevocable means the assets leave the estate” as an automatic rule. |
| Trust gate | Family complexity may justify an attorney conversation; it does not mechanically decide trust type. A future-appreciation question alone does not point to an irrevocable trust. | The nine triggers become conversation triggers, not a diagnosis. |
| Trustee diversification | UPIA generally favors diversification at the portfolio level, but the governing instrument and state enactment can alter the duty. Concentrated-asset planning may use explicit retention authority, a directed-trust structure, trustee selection, consent/release procedures, or other state-specific drafting—not one universal waiver. | Replace the universal “waive the prudent-investor rule” claim with the correct attorney question. |
| Trustee key | Holding one multisig key may make the trustee operationally involved, but legal control and fiduciary responsibility depend on the trust terms and the full signing policy. | Remove the claim that one key automatically solves the ownership/control problem. |
| Guardian | A will can nominate a guardian; the court makes the appointment under state law. | Correct the couple example. |
| International paragraph | Four legal systems cannot be accurately mapped in three sentences. | Remove it. |

## What this audit does and does not clear

### Cleared by research

- Federal mechanics stated at the general educational level.
- Bitcoin protocol and wallet-policy mechanics stated without vendor assumptions.
- Insurance-category definitions stated without quotes or policy recommendations.
- General estate concepts stated without pretending one state’s law is universal.

### Still needs targeted signoff

- an individual tax return position where records are incomplete;
- integrated tax examples after current-year app outputs are seeded;
- state residency/domicile and state tax treatment;
- actual insurance policy language, quotes, replacement, or amount recommendations;
- actual device/provider recovery procedures and inheritance terms;
- state-specific estate documents, trust drafting, RUFADAA consent, and fiduciary-duty modifications;
- the course terms/disclaimer and the education-versus-personalized-advice boundary.

The targeted questions and signature blocks live in `TARGETED-PROFESSIONAL-SIGNOFF.md`.