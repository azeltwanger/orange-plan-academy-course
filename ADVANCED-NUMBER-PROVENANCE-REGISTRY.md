# Orange Plan Academy — Advanced number and status provenance registry

**Purpose:** prevent a calculated Advanced result, agreement term, quote, or checklist status from appearing without a source and limitation.

For each important output, teach:

> **What it means · Calculated from · Edit source · This affects · Proof/qualification**

The app owns calculations it actually performs. An agreement, quote, device test, provider record, tax file, or legal document owns everything outside that calculation.

## A1 · Modeling and assumptions

| Output | What it means | Calculated from | Edit source | This affects | Proof / qualification |
|---|---|---|---|---|---|
| Confidence change between assumptions | Difference in successful test runs after one assumption changes | Same saved plan and comparable path set, with one changed return/inflation input | Scenario or Plan assumption | Confidence, earliest date, spending references, ending balances | Meaningful only when the comparison changes one primary input and uses the current model receipt |
| Holding return model | Rule used to change one holding's value through time | Saved holding return type and periods/rate | Holding editor advanced projection settings | Account value, allocation, tax, confidence, withdrawals | Override must correct a real mismatch; economic reasonableness remains judgment |
| Holding income/yield | Cash the holding is modeled to produce separately from value return | Saved yield and qualification fields | Holding editor | Cash flow, tax, total draw, reinvestment | Confirm the holding actually produces the modeled income and that it is not double-counted in total return |

## A2 · Bitcoin-backed borrowing

| Output | What it means | Calculated from | Edit source | This affects | Proof / qualification |
|---|---|---|---|---|---|
| Current LTV | Current loan balance relative to current pledged Bitcoin value | Balance ÷ (collateral BTC × current price) | Loan record and live balance/collateral | Action status, top-up, liquidation, release, capacity | Lender ledger and agreement own the contractual figure |
| Threshold Bitcoin price | BTC price where a chosen agreement LTV is reached | Balance ÷ collateral BTC ÷ threshold LTV | Agreement threshold, balance, collateral | Drawdown cushion and action ladder | Use the agreement's price source, timing, fees and balance definition |
| Drawdown cushion | Percent decline from current/reference BTC price to a threshold price | 1 − threshold price ÷ starting price | Scenario price and agreement terms | Survivability and starting LTV decision | Not a probability and not proof the lender gives time to act |
| BTC top-up required | Additional collateral needed to restore a target LTV at a given price | Balance ÷ (target LTV × BTC price) − current collateral | Target policy, price, balance, current collateral | Remaining self-custody, lender exposure, future runway | Top-up transfer must be possible before the agreement deadline |
| Cash paydown required | Principal reduction needed to restore a target LTV using current collateral | Balance − target LTV × collateral value | Target policy, balance, collateral price | Cash reserve, tax, debt and runway | Cash cannot also be counted for emergency, tax, and spending needs |
| Top-up/paydown runway | Number of planned actions finite reserves can fund | Available eligible BTC/cash ÷ requirement by action | Reserve designation and action policy | Hard exit and liquidation risk | Not reliable when price moves while transfers are pending |
| Loan interest | Financing cost accrued or paid | Agreement rate, compounding/payment method, balance and time | Loan terms and payment policy | Cash flow, LTV, net benefit, estate | Agreement/ledger owns the actual amount; variable/reset terms matter |
| Collateral at lender | BTC economically or legally under the lender/custodian structure | Pledged units plus top-ups minus released/liquidated units | Loan/custody record | Counterparty, custody, recovery and estate risk | Legal title, segregation and reuse require agreement review |
| Bitcoin retained versus sell-only | Additional ending BTC units under the borrowing path | Borrow-path ending BTC − sell-path ending BTC | Funding strategies and loan policy | Net worth, custody, debt and estate | Retained exposure is not unencumbered custody while pledged |
| Loan balance later / at death | Outstanding liability before the modeled repayment event | Principal, interest, repayments, liquidations and timing | Loan policy and repayment source | Estate value, heirs, collateral release and taxes | Agreement and estate process own actual death/incapacity handling |
| Net advantage versus sell-only | Difference in ending result after tax, interest, debt and retained BTC | Full borrow projection − full sell projection | Both strategy inputs | Decision ranking | Provisional when loan tax/legal treatment is unconfirmed; one modeled path is not proof of safety |

## A3 · Tax optimization

| Output | What it means | Calculated from | Edit source | This affects | Proof / qualification |
|---|---|---|---|---|---|
| Quantity reconciled | Current units explained by acquisition, transfer and disposition history | Lot/transaction history compared with current holdings | Transactions and lots | Basis confidence and sale readiness | Unexplained units remain unresolved rather than forced into a lot |
| Known basis | Supported tax investment in documented units | Acquisition cost/allowed adjustments for supported lots | Lot records | Gain, tax and net proceeds | Tax records and CPA conclusion own filing basis |
| Unresolved basis quantity | Units owned without a complete supported basis chain | Current quantity minus supported lots | Reconstruction work queue | Tax-estimate reliability and sale selection | Keep visibly unresolved; zero basis is only a labeled planning test when used |
| Planned lot | Lot Orange Plan assumes will leave in a modeled disposition | Selected method/lot and modeled sale | Tax strategy/lot selection | Gain, tax and remaining basis | Real provider/wallet identification must match by required time with adequate records |
| First-pass conversion room | Selected ordinary-income ceiling minus expected ordinary income before conversion | Tax-roadmap inputs and chosen ceiling | Conversion Scenario | Proposed conversion range | Not the final recommendation; other income, state, healthcare, cash and five-year rules apply |
| Full conversion cost | Current tax plus healthcare/program changes and implementation cash | Conversion amount, tax projection, current quote/program inputs | Scenario and professional worksheet | Cash reserve, Bridge, future Roth/traditional balances | CPA and healthcare reviewer own current result |
| Harvestable loss/gain | Supported unrealized result in a specific lot | Current value − supported basis | Lot and market records | Current tax, carryforwards and future basis | Opportunity is not a recommendation; compare no action and smaller action |
| State-move plan delta | Full-plan difference after tax and life-cost changes | Scenario state, housing, insurance, travel, work, events and tax | Relocation Scenario | Confidence, spending, estate and tax | Domicile, sourcing and residency remain professional conclusions |

## A4 · Access and healthcare

| Output | What it means | Calculated from | Edit source | This affects | Proof / qualification |
|---|---|---|---|---|---|
| Early-year account draw | Amount each account supplies before the ordinary access age | Total draw and saved phase/order/blend | Income funding phase | Tax, penalties, Bridge and balances | Use only accounts/amounts whose access is documented |
| Eligible employer-plan amount | Amount available under the actual plan after separation | Plan balance, distribution options and relevant exception facts | Plan document / administrator confirmation | Taxable Bridge use and rollover decision | App cannot infer plan-specific distribution options; additional-tax exception does not make pre-tax distribution tax-free |
| Remaining Roth contribution basis | Supported regular contributions not previously distributed | Forms/account history and Roth ordering | CPA-maintained basis schedule | Early Bridge and future Roth balance | Full Roth balance is not the accessible amount |
| SEPP stream | Professionally designed payment under current rules | Account balance, approved method, rates/life expectancy and start date | CPA/plan document | Cash flow, tax and flexibility | Modification rules can create retroactive consequences; professional-only implementation |
| Qualified HSA source | Supported reimbursement for qualified expenses | Eligible expenses, account balance and records | HSA/expense record | Healthcare draw and tax | Not unrestricted spending; premium eligibility is limited and fact-specific |
| Healthcare full cost | Annual cost of the selected pre-Medicare path | Net premium/membership + expected OOP + known non-covered items + reserve | Current quote and dated Plan expense | Spending, draw, confidence and earliest date | Quote and plan agreement own the current amount |
| Expected Marketplace income | Income measure used in the current application/estimate | Current tax facts and applicable MAGI rules | Quote/tax worksheet | Premium/credit and conversion/withdrawal range | Spendable cash is not the same number; update when income changes |
| Net healthcare premium | Premium after current employer/Marketplace/other contribution or credit | Current quote/application and expected income | Current quote | Total draw and strategy comparison | Never use illustrative amounts as a current promise |
| Integrated funding result | Same spendable-cash need funded from different tax pools | Account sources, gains, ordinary income, tax, premium and Bridge balances | Income/Tax Scenarios | Tax, healthcare, Bridge survival and future balances | Current quote and CPA review required |

## A5 · Advanced custody

These are primarily **status and proof** fields, not projection outputs.

| Status | What it means | Source | Edit source | This affects | Proof / qualification |
|---|---|---|---|---|---|
| Passphrase design present | Exact passphrase is required with the mnemonic under the selected wallet | Real wallet design | Protect process record only | Theft/loss/family recovery | Orange Plan never receives the passphrase; practice recovery proves it |
| Passphrase recovery proven | Intended wallet recreated and verified with backup + exact passphrase | Supported clean-device/practice test | Test record/date | Family readiness | Opening an app is not enough; expected wallet/accounts/addresses must match |
| Multisig threshold | Number of keys required out of total keys | Wallet configuration | Protect process-level record | Dual control and redundancy | Descriptor/configuration and compatible software may also be required |
| Failure survived | One specified key/person/device/provider loss did not block authorized recovery | Practice test | Test record | Readiness claim | Name the exact failure tested; do not generalize beyond it |
| Provider-independent recovery | Household can reconstruct and sign without provider availability when claimed | Family-controlled keys/configuration/software and test | Provider/custody record | Counterparty and succession risk | Provider agreement and successful test own the result |
| Migration complete | Destination received/spent, recovered and main balance moved in verified stages | Transaction IDs, device verification and test log | Holding location + Protect | Custody, basis records and estate handoff | Old record remains active until every dependent wallet/account is retired safely |

## A6 · Trusts and complex estate planning

These are evidence-backed statuses, not calculated legal conclusions.

| Status | What it means | Source | Edit source | This affects | Proof / qualification |
|---|---|---|---|---|---|
| Trust indicated / not indicated | Counsel's decision whether a trust solves a named problem better than baseline documents | Attorney design review | Protect review status | Documents, ownership and estate actions | “Not indicated; review after trigger” is valid completion |
| Legal owner | Person/entity legally owning a material asset after implementation | Executed documents, title/assignment, provider record | Real legal/provider record | Tax, fiduciary authority and transfer | Orange Plan checklist is not proof of ownership |
| Life/incapacity authority | Person legally permitted to manage during life/incapacity | POA/trust/provider acceptance | Attorney/provider records | Account/custody access | Key possession alone is not authority |
| Post-death authority | Executor/personal representative/trustee authority after death | Will/trust/court/provider process | Attorney/court/provider records | Claims and transfer | Naming a person does not itself complete every appointment/claim step |
| Technical access path | Authorized combination capable of using direct Bitcoin | Custody design and test | Protect process map | Recovery and distributions | Legal authority cannot sign without a key path; a key does not establish authority |
| Provider acceptance | Provider has accepted current owner/beneficiary/authorized-party record | Provider confirmation | Provider account | Transfer and claim process | A trust or will does not update the provider automatically |
| Tax implementation status | CPA/attorney conclusion for gift, income tax, estate inclusion and basis | Executed transaction and tax/legal analysis | Professional record | Projected tax/estate and filings | Grantor status, gift completion, gross-estate inclusion and basis are separate questions |
| Ownership-authority matrix complete | Every material asset's legal, provider, tax and technical records agree | Evidence packet | Protect checklist after proof | Estate readiness | Complete only after all mismatches are resolved or assigned |

## Registry rule

When an Advanced number appears in a script, slide, AI answer, report or demonstration:

1. identify the registry key,
2. show the denominator or scope,
3. identify whether it is app-calculated, illustrative, agreement-derived, quote-derived or professionally concluded,
4. point to the edit source,
5. and state the limitation preventing false certainty.
