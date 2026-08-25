# Orange Plan Academy — Advanced app contract

**App source reviewed:** `azeltwanger/orange-plan` at `34f42d94f4e236e6b82bad07e2b7bff0a578835e`  
**Course source:** `scripts/advanced/current/`  
**Status:** concept/app ownership mapped; exact deployed labels, routes, rounding, and screenshots remain receipt holds

## Contract rule

Advanced teaches a conditional decision. Orange Plan supplies the current plan inputs, projection, comparison, or checklist where supported. A provider, agreement, device, tax record, quote, or legal document supplies the proof Orange Plan cannot create.

For every Advanced lesson, distinguish:

- **Saved Plan input** — part of the Baseline
- **Preview** — changes displayed results but not the saved Plan until applied
- **Scenario** — a separate question beside the Baseline
- **External evidence** — agreement, quote, record, device test, provider confirmation, or professional conclusion

Do not narrate an exact click path until the deployed screen has been used end to end.

## Lesson contract

| Lesson | Current Orange Plan owner | App can support | Save / preview contract | App cannot prove | Final receipt needed |
|---|---|---|---|---|---|
| A1.1 | Plan assumptions · Scenarios · confidence engine | Current return/inflation assumptions, comparable Scenario result, confidence and earliest target-qualified date | Baseline remains saved; alternate assumption remains a Scenario unless deliberately adopted | That one assumption is economically correct | Model/version receipt; visible assumption labels; same-path comparison |
| A1.2 | Account/holding editor · advanced projection settings | Bitcoin assumptions, fixed, declining, custom periods, and supported income/yield fields; spot Bitcoin ETF default to Bitcoin assumptions | Holding override becomes saved only after the holding is saved | Economic reasonableness of the custom rate or yield | Exact labels, help copy, save confirmation, and downstream result |
| A2.1 | Plan → Income borrowing comparison · collateralized-loan records | Loan balance, collateral quantity, modeled LTV choices, custody split, capacity/runway, drawdown risk | Comparison is a preview until the borrowing strategy is applied; Core Baseline remains sell/no-loan by default | Signed threshold, legal ownership, collateral reuse, lender behavior, tax classification | Synthetic loan preview with current labels and source math; agreement review |
| A2.2 | Income borrowing risk/detail · Debt · Cash Flow · Protect | Modeled capacity, top-up/paydown needs, runway, interest, later balance, collateral at lender | Survival ladder is a household policy; only chosen settings are saved | Availability/timing of top-up assets, lender notices, actual repayment, family action | LTV path, finite-resource calculation, saved/preview state, agreement terms |
| A2.3 | Income sell-versus-borrow comparison · Scenarios | Same-need comparison, tax difference, interest, BTC retained, custody exposure, modeled drawdown, net result versus sell-only | Preview both; Apply only the chosen strategy; unchosen path remains a Scenario | Tax/legal classification of collateral transfer, stress tolerance, future refinance | Same cash need; source reconciliation; provisional-tax marker; applied-state proof |
| A2.4 | Debt record · Income risk detail · Protect | Provider name/structure notes, rate, thresholds, modeled exit effect, professional contact/action | Provider choice and exit rules are household decisions, not engine outputs | Contract interpretation, insolvency claim, notice/cure, liquidation, provider-independent recovery | Redacted agreement receipt and completed clause matrix |
| A3.1 | Tax Center · holdings/lots · transaction history | Quantity reconciliation, known/unresolved basis, planning lot comparison, projected gain/tax | Imported/entered records become saved; unresolved units stay unresolved | That the real provider/wallet executed and documented the selected lot | Quantity and basis receipt; unresolved state; provider/CPA sale packet |
| A3.2 | Tax Center roadmap · conversion comparison · Scenarios | Projected traditional/Roth balances, modeled tax by year, no/smaller/proposed conversion comparison | Conversion remains a preview/Scenario until deliberately saved and implemented | Final taxable amount, five-year/access conclusion, estimated payments, filing | Three-option comparison; tax-payment source; CPA-approved range |
| A3.3 | Tax Center lots/opportunities · Scenarios | Current supported gain/loss, planned lot, estimated tax effect, future balances | Harvest remains a proposed action until the actual disposition and records exist | Current repurchase rule, lot execution, filing result | No-action/smaller/proposed comparison; post-action exposure plan; CPA receipt |
| A3.4 | Scenarios · household state · life events · Tax Center | A move Scenario changing state, housing, spending, work, property and tax assumptions | Possible move stays a Scenario; committed move becomes life event then Baseline | Domicile, sourcing, residency, state legal/tax result | Full-life Scenario inputs and state-professional conclusion |
| A4.1 | Plan → Income phases · accounts · Tax Center | Year-by-year draw, account order/blend, access phases, projected tax | Baseline uses only verified sources; special access remains Scenario/phase until documented | Employer-plan options, Roth basis, SEPP design, HSA records | Access map by year; plan document; CPA-approved eligible amount |
| A4.2 | Life events/spending · Income · Tax Center · Scenarios | Dated healthcare expense, funding source, modeled draw, tax/MAGI-sensitive Scenario inputs | Current accepted cost becomes a dated Plan expense; alternate coverage remains Scenario | Premium quote, network, prescriptions, subsidy, enrollment, claim/payment protection | Current quote worksheet; all-in cost; MAGI estimate; Medicare transition |
| A4.3 | Income phases · Tax Center · Scenarios | Same spendable-cash need under alternate taxable/traditional/Roth/HSA mixes | Save one annual phase/range; keep alternates as Scenarios | Marketplace/Medicare program result and filing interaction | Same-cash comparison; current quote and tax result; Bridge survival |
| A5.1 | Protect · custody records · Family Custody Map | Custody type, people, component roles at a process level, review/test dates | App records status only after the real practice/recovery test | Exact passphrase, correct wallet, recovery success, family capability | Device-specific practice test with no secrets; custody review |
| A5.2 | Protect · custody map · estate people/provider records | Threshold description, provider, key-holder roles at process level, configuration-record location, test date | App status follows the chosen and tested design | Keys, descriptor correctness, provider-independent recovery, legal authority | Practice 2-of-3 recovery; provider agreement; estate/custody review |
| A5.3 | Holdings/accounts · Protect · custody map | Old/new custody location, migration status, participants, test date, next review | Old record stays active until the staged migration is proven; then update holding/custody | Address correctness, signatures, change/UTXO privacy, backup validity | Practice wallet, small tranche, destination spend, alternate recovery, staged transfer |
| A6.1 | Protect · estate roles/documents · professional actions | Trust gate, problem, attorney question, status, review date | “Not indicated” is a valid saved review result; recommended trust remains pending until counsel | Correct trust type, tax result, creditor/probate effect, document validity | Attorney/CPA claim response and accepted design memo |
| A6.2 | Protect · people · beneficiaries · custody map · account records | Ownership/authority checklist, provider confirmations, unresolved implementation actions | Mark complete only after legal, provider, tax and custody proof agree | Ownership transfer, completed gift, provider acceptance, fiduciary authority, key recovery | Asset-by-asset ownership/authority matrix and evidence packet |

## Current code anchors

The current app code confirms:

- holding-level return models and income/yield settings in `src/components/forms/AddAssetWithTransaction.jsx` and `src/lib/holdingReturnModels`,
- sell-versus-borrow and loan-risk analysis in `src/pages/WithdrawalStrategy.jsx` and `src/components/shared/sellVsBorrowAnalysis`,
- tax planning and lot records in `src/pages/TaxCenter.jsx`,
- account and asset funding phases in `src/pages/WithdrawalStrategy.jsx`,
- Scenario comparison in `src/pages/Scenarios.jsx`,
- and process/checklist ownership in `src/pages/EstateSecurity.jsx` and Protect-related components.

## Change-control rule

An app change requires an Advanced course impact classification when it changes:

- a holding return model or label,
- a borrowing input, comparison, risk output, or apply state,
- a Tax Center lot/strategy result,
- an account-access or funding phase,
- a Protect completion rule,
- or the source/meaning of a number used in an Advanced example.

Update this contract, the applicable run sheet, and the last-verified app commit before recording.
