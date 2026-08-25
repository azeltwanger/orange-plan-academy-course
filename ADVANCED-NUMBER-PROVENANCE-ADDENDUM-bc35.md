# Advanced number-provenance addendum — current app

**App commit:** `bc35d739878f3daf502735d203f2677ab6565ba8`  
**Extends:** `ADVANCED-NUMBER-PROVENANCE-REGISTRY.md`

| Key | What it means | Calculated / derived from | Edit source | This affects | Proof owner / qualification |
|---|---|---|---|---|---|
| `exact_fact_readiness` | Whether the owner/account facts needed for the selected projection are present | Required fact set compared with saved exact-fact records | Tax exact-fact editor and underlying account/history records | Warning state, access, tax, report confidence | Readiness is not a legal conclusion; provider records and CPA own the result |
| `remaining_roth_contribution_basis` | Supported regular Roth IRA contributions not previously distributed | Owner Roth history, contributions, prior distributions, and ordering | Roth IRA history / CPA basis schedule | Early access, Roth balance, tax and Bridge | Full Roth balance is not the basis amount |
| `workplace_roth_fact_state` | Account-specific designated Roth facts available to the projection | Account wrapper, owner, participation/rollover facts and records | Workplace-plan exact facts | Tax-free/ordinary treatment, access and report | Plan administrator and CPA own actual plan and tax conclusion |
| `hsa_fact_readiness` | Whether the modeled HSA source has supported balance/expense facts | HSA record, eligible expense, reimbursement history and saved fact state | HSA exact-fact editor and expense record | Healthcare source, tax and Bridge | App does not prove an expense or premium is qualified |
| `planned_conversion_amount` | Proposed or saved conversion being compared | Conversion Scenario or saved strategy | Tax Center conversion schedule | Current tax, future Roth/traditional, healthcare, Bridge | Planned is not executed |
| `executed_conversion_amount` | Amount and date actually completed by the custodian | Executed conversion record and account evidence | Executed-conversion entry | Account balances, tax record, report and future ordering | Custodian/tax record own the fact; actual overrides plan |
| `voluntary_target_mix` | Target account percentages for the household's voluntary withdrawal policy | Saved funding phase/blend | Income / Withdrawal Strategy | Account sources, tax funding, balances and future tax | Applies only to eligible voluntary sources |
| `voluntary_tax_funding_mix` | Final account sources used for taxes and penalties created by voluntary withdrawals | Active target mix, iterative tax feedback, eligible balances and safety rules | Same saved blend plus account availability | Source reconciliation, Bridge and balances | Must reconcile with voluntary target; spill requires an exhaustion/safety reason |
| `required_rmd_source` | Required distribution modeled separately from the voluntary target | Current account facts and applicable RMD rules | Account/tax facts and maintained rules | Tax, cash, voluntary need and balances | Current law and CPA own applicability and amount |
| `tax_readiness_report_state` | Whether the report result is fully supported or remains qualified by missing facts | Exact-fact warnings, basis state, planned/executed state and projection receipt | Underlying records | Student interpretation and professional handoff | A mathematically reconciled result can remain professionally qualified |

## Teaching rule

When one of these values appears:

1. name the owner and account scope,
2. distinguish saved input, exact fact, Preview, Scenario, planned action, and executed fact,
3. show which source can correct it,
4. state what Orange Plan calculated,
5. and name the external proof owner.
