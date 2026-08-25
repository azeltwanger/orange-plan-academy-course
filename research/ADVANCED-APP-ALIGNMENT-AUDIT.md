# Orange Plan Academy — Advanced app-alignment audit

**Status:** complete for current concept architecture  
**Scope:** 18 Advanced lessons  
**App evidence:** current projection engine and known planning areas; final customer-facing labels, save/preview states, and screenshots remain receipt holds

## Alignment rule

Every Advanced lesson must identify four owners:

1. **Orange Plan input owner** — where the learner records or changes the planning fact
2. **Orange Plan output owner** — which engine or page calculates the comparison
3. **External evidence owner** — agreement, tax return, plan document, quote, device/provider process, attorney, or real-world test
4. **Core return path** — where the accepted decision changes the saved plan

The app can calculate and organize a decision. It cannot convert missing external evidence into a verified implementation.

## Classification

- **App-primary:** the main result is calculated by Orange Plan; external review verifies interpretation or execution.
- **Hybrid:** Orange Plan models the plan effect while an external source owns a material input or rule.
- **External-primary:** the app records status and plan effect, but the agreement, provider, device, document, or professional owns completion.

---

# Lesson map

| Lesson | Classification | App input owner | App output / comparison owner | External evidence | Return to Core | Receipt hold |
|---|---|---|---|---|---|---|
| **A1.1** | App-primary | Plan → Retirement assumptions and saved Scenario overrides | Monte Carlo paths, confidence at planned date, earliest target-qualified date, Scenario delta | Current model/version documentation | Baseline assumptions and Scenarios | Exact assumption labels, path/version receipt, save state |
| **A1.2** | Hybrid | Holding editor → advanced projection assumptions | Projection after holding-level return/yield override | Holding's actual economic exposure and source documentation | Baseline and Allocation | Final override labels, return versus income fields, save behavior, affected outputs |
| **A2.1** | Hybrid | Debt / Bitcoin-loan record and Plan → Income borrowing comparison | LTV, projected debt, collateral, Bitcoin retained, taxes and plan result | Signed lender agreement and current collateral ledger | Debt and Retirement Income | Current loan-field labels, price source, preview versus saved state |
| **A2.2** | Hybrid | Loan terms, collateral, top-up/paydown resources, repayment assumptions | LTV path, debt balance, liquidation/top-up comparison where supported | Agreement, lender notices, real reserve/collateral availability | Debt, Reserve, Protect, estate handoff | Current top-up/liquidation modeling and source reconciliation |
| **A2.3** | App-primary with agreement hold | One cash need plus sell/borrow strategy preview | Tax, Bitcoin sold/retained, interest, loan balance, confidence, ending assets after debt | CPA and lender terms | Retirement Income or life-event funding source | Same cash need, current sell/borrow cards, source split, saved versus preview |
| **A2.4** | External-primary | Provider and loan record; notes/actions in Debt and Protect | App can carry fees, rate, balance, and collateral assumptions | Signed agreement, legal structure, custody, insolvency, release, death/incapacity process | Debt ceiling, Reserve, Protect | Redacted agreement version and exact provider fields |
| **A3.1** | Hybrid | Tax lots, transactions, holdings, unresolved-basis status | Quantity reconciliation, planning gain/loss, lot comparison, projected tax | Broker/wallet identification process and CPA-reviewed records | Tax roadmap and Retirement Income sales | Current Tax labels, unresolved basis display, selected-lot preview versus executed lot |
| **A3.2** | App-primary with CPA hold | Conversion Scenario or saved tax strategy; income and account records | Current-year tax, future traditional/Roth balances, confidence and withdrawal effects | Current tax return, CPA sizing, healthcare/Medicare effects | Tax strategy and withdrawal phase | Current conversion controls, tax ceiling, save/apply behavior, source of tax payment |
| **A3.3** | App-primary with CPA hold | Taxable lots and harvesting Scenario | Gain/loss, projected tax, remaining basis, holdings and allocation effect | Current repurchase/identification rules and actual transactions | One current Tax action or deliberate pass | Harvesting controls, lot eligibility, exposure after action |
| **A3.4** | Hybrid | State, housing, income, spending, property and life-event Scenario | Full-plan tax, spending, net worth, confidence and timing difference | State residency/domicile, sourcing, move records and professional review | Baseline after commitment | State-tax model scope, Scenario inputs, before/after delta |
| **A4.1** | Hybrid | Accounts, tax wrappers, Retirement Income phases and Bridge assignments | Year-by-year draw and account/holding sources | Employer-plan document, Roth basis, HSA records, current access rules | Bridge and Retirement Income | Account-source labels, phase behavior, special-source amount and evidence status |
| **A4.2** | Hybrid | Dated healthcare expense/life event; retirement income and tax assumptions | Spending need, total draw, confidence and retirement date | Current household quote, Marketplace/COBRA/Medicare facts, HSA eligibility | Retirement spending, Bridge and Tax question | Expense dates, quote source, income sensitivity and what the app does not calculate |
| **A4.3** | App-primary with quote/CPA hold | Same spending need under separate withdrawal/Scenario mixes | Taxable sales, ordinary income, Bridge use, future balances, confidence | Current quote and applicable income calculation | First Retirement Income phase plus alternate Scenario | Same-cash-need reconciliation, app tax result, external premium result |
| **A5.1** | External-primary | Protect custody type, people, process status and review date | App checklist only | Device support, exact passphrase process and successful practice recovery | Family Custody Map and failure review | No secrets; device/version/test date and evidence reference |
| **A5.2** | External-primary | Protect threshold, provider, people, configuration-process locations | App checklist only | Provider agreement, key distribution, descriptor/configuration and recovery test | Custody level, people and estate handoff | Threshold, provider-independent recovery evidence, successful combinations |
| **A5.3** | External-primary | Holding/custody location, migration status, people and test dates | App checklist and updated holdings | Device/coordinator instructions, transaction evidence and recovery tests | Protect and estate handoff | Practice wallet, tranche transaction IDs, verified spend, family test and old-wallet retirement |
| **A6.1** | External-primary | Protect trust status, problem, attorney question and review date | App readiness/checklist only | Colorado attorney and CPA design | Estate roles, documents and beneficiaries | Trust job, document/version, funding status, professional response |
| **A6.2** | External-primary with app plan effect | Protect ownership/authority matrix; account/holding owner and beneficiary records | App reflects changed owner/account/estate assumptions where supported | Signed documents, accepted provider records, tax records, custody threshold and practice proof | Estate readiness, custody map and heir letter | Legal owner, binding provider record, tax evidence, access test and unresolved mismatch |

---

# Current engine and product anchors

Advanced lessons reuse the same app-owned calculation layer as Core, including:

- `buildProjectionParams.jsx` and projection-parameter helpers
- `runProjection.jsx` / unified year-by-year projection
- `monteCarloSimulation.jsx`
- `monteCarloEarliestMonth.js`
- Allocation portfolio and retirement-funding builders
- Tax-lot and tax-roadmap data
- Debt and retirement-income source strategies
- Build Your Plan completion logic where the product exposes the related task

The Academy never creates a second result when the app already owns the calculation.

## Save-state rule

Every Advanced app demonstration must name whether the learner is viewing:

- a saved Baseline input,
- an unsaved field,
- a strategy preview,
- an applied strategy,
- a separate Scenario,
- or a read-only result.

A preview is not described as the current plan. A manually completed task is not described as proof that the external implementation worked.

## Missing-data rule

When an external input is missing—basis, plan access, quote, lender term, provider process, legal ownership, or recovery proof—the app and lesson must preserve that uncertainty.

The learner may complete a review by recording the missing item, owner, and due date. They may not fabricate the value to make the task or projection look complete.

## App acceptance still required

Before any Advanced app screen-share is recorded, capture:

- current route and label,
- exact input and output names,
- denominator and units,
- rounding,
- save/apply/preview/Scenario state,
- source reconciliation,
- current app commit,
- and a synthetic screenshot or recording reference.

Those receipts are defined in `demo/ADVANCED-DEMO-RECEIPTS.md`.
