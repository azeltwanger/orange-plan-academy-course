# Orange Plan Academy — Advanced professional-claim matrix

**Purpose:** make sure every high-stakes Advanced claim has one named reviewer, packet, claim ID, and correction path before final approval.

## Review order

1. **CPA / tax attorney** — affects A2, A3, A4 and A6 and can change examples used by other reviewers.
2. **Bitcoin lending attorney/practitioner** — A2 agreement, collateral and liquidation claims.
3. **Pre-Medicare healthcare reviewer** — A4 coverage, quote and enrollment claims; coordinates with CPA on income.
4. **Bitcoin custody practitioner** — A5 technical process and A6.2 custody coordination.
5. **Colorado estate attorney** — A6 and legal portions of A2/A5.

No reviewer clears another profession's scope.

---

# Claim map

| Lesson | Primary packet / claim IDs | Secondary review | What the reviewer owns | What remains Austin judgment |
|---|---|---|---|---|
| **A1.1** | App receipt only | — | Current model/version and UI representation | How much model detail belongs in the lesson |
| **A1.2** | App receipt only | Holding/source documentation | Current override fields and save behavior | Whether the override materially improves accuracy |
| **A2.1** | `LENDING-SEND.md` · L-01–L-05, L-16 | `CPA-ADVANCED-SEND.md` · AT-17 | LTV framing, collateral/liquidation risks, tax boundary | No universal safe LTV; whether borrowing belongs in the plan |
| **A2.2** | `LENDING-SEND.md` · L-05–L-09, L-12–L-14 | Estate AE-13 | Top-up, paydown, repayment, cure, exit and incapacity/death wording | Required action ladder and finite-resource philosophy |
| **A2.3** | `LENDING-SEND.md` · L-15–L-16 | Core CPA T-11–T-13; Advanced CPA AT-17 | Loan/sale tax and lender caveats | Same-cash-need comparison; Core plan should not require borrowing |
| **A2.4** | `LENDING-SEND.md` · L-09–L-14 | Estate AE-13 | Agreement, collateral control, insolvency, release and succession | Rate is not the first provider comparison; written exit required |
| **A3.1** | `CPA-ADVANCED-SEND.md` · AT-01–AT-03 | Core CPA T-01–T-05 | Reconstruction, identification, provider/wallet evidence, filing boundary | Unknown basis remains unresolved; quantity first |
| **A3.2** | `CPA-ADVANCED-SEND.md` · AT-04–AT-06 | Healthcare H-06–H-07 | Conversion tax, five-year, pro-rata, payment and income interactions | Compare none/smaller/ceiling; do not automatically fill a bracket |
| **A3.3** | `CPA-ADVANCED-SEND.md` · AT-07–AT-08 | App lot/Scenario receipt | Current gain/loss, repurchase and identification rules | A harvest needs a plan purpose and exposure decision |
| **A3.4** | `CPA-ADVANCED-SEND.md` · AT-09 | State CPA/attorney sourced for the actual states | Residency, sourcing and current state result | Move only when the life and full plan improve |
| **A4.1** | `CPA-ADVANCED-SEND.md` · AT-10–AT-12 | Actual plan administrator/document | Access, tax/additional-tax and record requirements | Simplest verified source; every year needs a backup |
| **A4.2** | `HEALTHCARE-SEND.md` · H-01–H-13 | CPA AT-13–AT-14 | Coverage terminology, quote fields, Marketplace/COBRA/Medicare and HSA boundary | Premium is not full cost; health sharing is not insurance |
| **A4.3** | `HEALTHCARE-SEND.md` · H-06–H-13 | CPA AT-04, AT-13–AT-14 | Income/quote and tax interaction | Same cash need; annual range; preserve the Bridge |
| **A5.1** | `CUSTODY-ADVANCED-SEND.md` · AC-01–AC-03 | Exact manufacturer/device docs | Passphrase and recovery procedure | Passphrase only for a named problem; family recovery over status |
| **A5.2** | `CUSTODY-ADVANCED-SEND.md` · AC-04–AC-07 | Estate AE-10 | Threshold, descriptor/configuration, provider independence, key distribution | Collaborative versus DIY based on family capability |
| **A5.3** | `CUSTODY-ADVANCED-SEND.md` · AC-08–AC-11 | Device/coordinator docs | Migration, address/signing, recovery and UTXO terminology | Never make the main balance the first test |
| **A6.1** | `ESTATE-ADVANCED-SEND.md` · AE-01–AE-06 | CPA AT-15–AT-16 | Colorado trust gate, revocable/irrevocable, trustee and tax qualification | Trust selected by problem; “not indicated” is valid |
| **A6.2** | `ESTATE-ADVANCED-SEND.md` · AE-07–AE-12 | CPA AT-15–AT-16; Custody AC-12 | Ownership, funding, provider record, authority, tax and custody coordination | Academy teaches matrix; professionals execute it |

---

# Core packets reused by Advanced

Advanced reviewers receive the existing Core packet when the same mechanism carries forward:

- `CPA-SEND.md` with `CPA-ADVANCED-SEND.md`
- `CUSTODY-SEND.md` with `CUSTODY-ADVANCED-SEND.md`
- `ESTATE-ATTORNEY-SEND.md` with `ESTATE-ADVANCED-SEND.md`

The Advanced supplement should not ask the professional to repeat claims already cleared in Core. It asks only for the added implementation detail.

# Application protocol

For every returned claim:

1. Record reviewer, credentials, conflicts, date and response code.
2. Log the correction by claim ID in the applicable tracker.
3. Apply the **minimum factual correction** to both spoken script and student lesson text.
4. Move changing thresholds, rates, limits, procedures and document lists to maintained reference.
5. Update the hold register and demonstration receipt.
6. Rerun the Advanced course, voice, provenance, stale-claim and full-course audits.
7. Clear only the reviewer's actual scope.
8. Give Austin the corrected lesson for one clean final read.

A generic “looks good” does not clear a claim. A provider explanation clears only that provider's process, not the generic course comparison.

# Current status

| Area | Packet prepared | Reviewer selected | Sent | Returned | Applied |
|---|---|---|---|---|---|
| CPA / tax | Yes | No | No | No | No |
| Bitcoin lending | Yes | No | No | No | No |
| Pre-Medicare healthcare | Yes | No | No | No | No |
| Advanced custody | Yes | No | No | No | No |
| Colorado estate / trust | Yes | No | No | No | No |

Primary-source verification is complete. **Actual outside professional sign-off remains incomplete.**
