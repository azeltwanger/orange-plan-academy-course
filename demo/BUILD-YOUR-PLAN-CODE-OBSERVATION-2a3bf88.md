# Build Your Plan — code observation at `2a3bf88`

**Status:** source-code observation, not deployed end-to-end acceptance  
**App branch:** `codex/build-plan-focus-exact`  
**Observed commit:** `2a3bf8872b35e782c6fb098d1a65ffcdf9a85666`  
**Course fixture:** `demo-v1-inputs`  
**Purpose:** remove speculation about the preview's current mission structure before Austin uses the deployed flow and the Academy writes exact clicks.

The source defines **seven planning missions**. This file records the IDs, labels, routes, completion logic, manual keys, and current course implications. The deployed UI can still differ because the available preview was built from a dirty working tree. Final walkthrough authority remains the accepted deployed flow Austin uses end to end.

## Panel behavior observed in code

- The top band contains seven mission nodes.
- Opening a mission reveals its tasks and progress.
- Tasks can be completed automatically from saved app data or manually through a checkbox, depending on the task contract below.
- Tax and Retirement Income can be skipped at the product level.
- Skipped missions are hidden from the focused strip and can be restored from the expanded list.
- A focused task uses query parameters:
  - `buildArea`
  - `buildTask`
  - `buildReturn`
- The focus key is `areaId:taskId`.
- The default return label is **Return to Your Plan**.
- Focus mode opens the requested mission/task and suppresses unrelated work until the learner returns.
- Mission ordering can use recommended IDs, then incomplete before complete, then remaining task count, then source order.

These are implementation details for walkthroughs. They do not change the concept syllabus by themselves.

---

# Mission 1 · Get organized

**ID:** `organized`  
**Label:** `Get organized`  
**Summary:** `Add the core facts once so every later decision is usable.`  
**Area route:** `/Dashboard`

| Task ID | Customer-facing title | Route | Completion type | Current completion rule / key | Academy teaching |
|---|---|---|---|---|---|
| `add_accounts` | Add every account | `/Dashboard` | Automatic | At least one account exists | 1.1 gathers the full account list; walkthrough enters the account records |
| `add_holdings` | Add the holdings inside them | `/Dashboard` | Automatic | At least one holding exists | 1.1 and 4.2 distinguish an account wrapper from its holdings |
| `split_household` | Separate mine, yours, and joint | `/Household?focus=ownership` | Manual | `build_organized_people_split` | Baseline household/ownership setup |
| `life_events` | Put the big future costs and changes on the calendar | `/Plan?focus=life-events` | Automatic | At least one life event exists | 1.2 sorts expected changes from Scenarios; 2.3–2.4 fund dated costs |

**No mission skip key observed.**

## Course alignment

Strong alignment:

- accounts and holdings are separate,
- household ownership is explicit,
- and life events are part of the foundational plan rather than hidden in a later calculator.

## Product issue to resolve

The automatic life-event rule requires at least one saved event. A household with no meaningful future event may be unable to complete the mission honestly. The product should support a deliberate **No major life events to add right now** state rather than forcing a fictional event.

The Academy must not tell a learner to invent a life event to obtain a checkmark.

---

# Mission 2 · Find financial capacity

**ID:** `capacity`  
**Label:** `Find financial capacity`  
**Summary:** `Turn household cash flow into a reliable monthly amount you can direct.`  
**Area route:** `/CashFlow`

| Task ID | Customer-facing title | Route | Completion type | Current completion rule / key | Academy teaching |
|---|---|---|---|---|---|
| `cash_flow` | Confirm income, taxes, living spending, and Debt | `/CashFlow?focus=summary` | Automatic | Gross income > 0 and current annual spending > 0 | 2.1 explains source rows and post-debt capacity |
| `reserve` | Choose the working reserve | `/CashFlow?focus=reserve` | Automatic | Reserve months > 0 and reserve basis is saved | 2.2 chooses basis and months |
| `debt` | Choose the Debt treatment | `/Debt?focus=strategy` | Mixed automatic/manual data | Complete when there are no active debts, or every active debt has a reviewed flag in `build_plan_debt_reviewed[liability.id]` | 3.1 decides the treatment and household ceiling |
| `contributions` | Route the next dollar | `/CashFlow?focus=routing` | Manual | `build_capacity_contributions` | 4.3 routes the post-debt account amount |

**No mission skip key observed.**

## Course alignment

- A debt-free household can complete the Debt task honestly.
- The product separates the saved debt treatment from routing the remaining money.
- The Academy's reconciled demo matches this: $500 extra principal is already in Debt, leaving $3,500 of account contributions.

## Completion boundary

The automatic Cash Flow rule proves that income and spending exist. It does not prove the amounts are accurate, that debt is not duplicated in spending, or that the monthly route is repeatable. The Academy finish line remains the learner's ability to rebuild the source equation and explain the route.

---

# Mission 3 · Aim the portfolio

**ID:** `portfolio`  
**Label:** `Aim the portfolio`  
**Summary:** `Choose the mix, timeframe, and account placement that fit the plan.`  
**Area route:** `/Allocation`

| Task ID | Customer-facing title | Route | Completion type | Current completion rule / key | Academy teaching |
|---|---|---|---|---|---|
| `allocation_range` | Choose the Bitcoin range you will review against | `/Allocation?focus=mix` | Automatic | Holdings exist and the saved target-allocation percentages total exactly 100 after rounding | 4.1 chooses target, band, denominator, and drawdown |
| `timeframes` | Give Reserve, Bridge, and Legacy a job | `/Allocation?focus=timeframes` | Automatic | Every in-scope holding is assigned a timeframe; primary residence and 529 holdings are excluded | 4.2 assigns holding and time-horizon jobs |
| `contribution_allocation` | Decide what future dollars buy | `/Allocation?focus=contributions` | Manual | `build_portfolio_contribution_allocation` | 4.3 applies target/drift to future contributions |
| `account_location` | Choose which holdings belong in which accounts | `/Allocation?focus=accounts` | Manual | `build_portfolio_account_location` | 4.4 teaches wrapper, access, tax, and custody trade-offs |

**No mission skip key observed.**

## Course alignment

The preview confirms the same Allocation scope discovered by the demo generator:

- primary residence excluded,
- beneficiary-restricted 529 excluded,
- the learner must assign Reserve, Bridge, and Legacy to every remaining holding.

## Completion boundary

A target totaling 100 proves a complete input, not a tolerable allocation. The Academy finish line remains the learner's ability to state the denominator, current percentage, target/band, and dollar loss in a major Bitcoin drawdown.

---

# Mission 4 · Plan the tax path

**ID:** `tax`  
**Label:** `Plan the tax path`  
**Summary:** `Make current records usable and surface the tax decisions worth reviewing.`  
**Area route:** `/Tax`  
**Mission skip key:** `build_plan_skip_tax`

| Task ID | Customer-facing title | Route | Completion type | Current completion rule / key | Academy teaching |
|---|---|---|---|---|---|
| `cost_basis` | Get cost basis usable before the next sale | `/Tax?focus=cost-basis` | Manual | `build_tax_cost_basis` | 5.1 reconciles quantity and keeps unresolved lots visible |
| `tax_report` | Read the year-by-year tax roadmap | `/Tax?focus=overview` | Manual | `build_tax_report` | 5.2 reads tax as a timeline |
| `tax_opportunities` | Flag conversion, harvesting, or repayment windows | `/Tax?focus=harvesting` | Manual | `build_tax_opportunities` | 5.2 identifies opportunities without executing them |
| `tax_follow_through` | Record what happens now, later, or never | `/Tax?focus=roth-conversion` | Manual | `build_tax_follow_through` | 5.2 ends with one action, CPA question, or deliberate pass |

## Important correction

The current preview does **not** require all basis to be complete before the task can be marked reviewed. The cost-basis task is manually completed.

That is compatible with the Academy demo:

- current quantity reconciles,
- 1.25 BTC has known basis,
- 0.40 BTC is being reconstructed,
- 0.10 BTC remains unknown,
- and the learner can finish the review by recording the unresolved work and professional question rather than fabricating basis.

## Skip-state boundary

Tax is optional at the product-mission level, but it remains a Core Academy concept because every usable Bitcoin plan needs to understand basis readiness and tax consequences.

A product skip means **hide this mission for now**. It is not educational completion and should not be presented as proof that tax does not apply.

---

# Mission 5 · Build the retirement paycheck

**ID:** `retirement_income`  
**Label:** `Build the retirement paycheck`  
**Summary:** `Turn the long-range plan into an actual future paycheck.`  
**Area route:** `/Income`  
**Mission skip key:** `build_plan_skip_retirement_income`

| Task ID | Customer-facing title | Route | Completion type | Current completion rule / key | Academy teaching |
|---|---|---|---|---|---|
| `retirement_timing` | Set retirement timing and spending | `/Plan?focus=retirement-age` | Automatic | Retirement age > 0 and retirement spending > 0 | 1.3 and 6.1 define household retirement timing and lifestyle |
| `income_floor` | Add Social Security, pensions, and other recurring income | `/Plan?focus=social-security` | Automatic | Custom Social Security is off, or required primary/spouse benefit amounts exist under current household rules | 6.1 builds the phased income floor |
| `withdrawal_strategy` | Choose the withdrawal and refill policy | `/Income?focus=withdrawal-order` | Manual | `build_retirement_withdrawal_strategy` | 6.2 chooses accounts, holdings, phases, and refill |
| `sell_borrow_hold` | Decide when you sell, borrow, or keep holding | `/Income?focus=overview` | Manual | `build_retirement_sell_borrow_hold` | 6.2 compares tools and allows borrowing to remain excluded |

## Course alignment

The final task does not require the household to borrow. The Core demo completes it with a deliberate decision:

> Sell under the saved funding policy, keep borrowing excluded from the baseline, and compare borrowing only when the plan actually triggers the Advanced gate.

## Skip-state boundary

A product skip may be useful for someone not ready to design retirement income. It is not proof that the concept is irrelevant to the full Core outcome.

---

# Mission 6 · Protect the plan

**ID:** `protect`  
**Label:** `Protect the plan`  
**Summary:** `Make the plan recoverable, transferable, and covered.`  
**Area route:** `/Protect`

| Task ID | Customer-facing title | Route | Completion type | Current completion rule / key | Academy teaching |
|---|---|---|---|---|---|
| `custody_recovery` | Document custody and prove recovery | `/Protect?focus=recovery` | Manual | `build_protect_custody_recovery` | 7.1–7.3 custody and recovery |
| `beneficiaries` | Check beneficiaries everywhere | `/Protect?focus=beneficiaries` | Manual | `build_protect_beneficiaries` | 8.1 provider records and intent |
| `estate_roles` | Name the people and documents that let others act | `/Protect?focus=estate` | Manual | `build_protect_estate_roles` | 8.1 legal roles/documents |
| `heir_letter` | Write the heir letter and add the backup delivery path | `/Protect?focus=heir-letter` | Manual | `build_protect_heir_letter` | 8.3 no-secrets instructions and discovery |
| `coverage` | Fill the insurance gaps the family cannot absorb | `/Protect?focus=coverage` | Manual | `build_protect_coverage` | 8.4 protection-gap review |

**No mission skip key observed.**

## Critical real-world boundary

Every task is manually checked, but the checkbox cannot prove:

- a wallet backup works,
- another family member can recover,
- a legal document is valid,
- a provider accepted a beneficiary record,
- or an insurance contract provides the stated benefit.

The Academy walkthrough must state both:

1. the app/manual completion action,
2. the real-world evidence still required.

A learner should never mark a task complete merely because they intend to do it later.

---

# Mission 7 · Use and review the plan

**ID:** `review`  
**Label:** `Use and review the plan`  
**Summary:** `Make decisions with the plan, save the record, and keep it current.`  
**Area route:** `/YourPlan`

| Task ID | Customer-facing title | Route | Completion type | Current completion rule / key | Academy teaching |
|---|---|---|---|---|---|
| `read_plan` | Run the plan and read the result | `/Plan?run=confidence` | Manual | `build_review_read_plan` | 1.3 and 9.2 read the current plan |
| `run_scenario` | Compare one real decision | `/Scenarios` | Manual | `build_review_scenario` | 9.2 changes one primary lever |
| `action_list` | Turn the result into one to three actions | `/YourPlan` | Manual | `build_review_actions` | 9.1–9.2 action ownership and capstone |
| `save_record` | Save the annual record and schedule the next review | `/YourPlan` | Manual | `build_review_record` | 9.1–9.2 PDF, encrypted export, and cadence |

**No mission skip key observed.**

## Completion boundary

The `read_plan` task is manual. It does not appear to require a current calculation timestamp or prove the learner understood the result.

The Academy finish line remains:

- explain the plan in six sentences,
- name one to three owned actions,
- distinguish the PDF and encrypted export,
- and understand that in-app restore is currently unavailable.

---

# Mission-to-Academy crosswalk

| Build Your Plan mission | Primary Core lessons | App completion | Academy human finish line |
|---|---|---|---|
| Get organized | 1.1, 1.2, 2.3, 2.4 | Source records and checkboxes meet mission rules | Plan is honest about what is verified, estimated, missing, expected, or only a Scenario |
| Find financial capacity | 2.1, 2.2, 3.1, 4.3 | Required source inputs and reviewed debt/routing tasks complete | Learner can rebuild post-debt capacity, reserve, debt treatment, and route without double-counting |
| Aim the portfolio | 4.1–4.4 | Target totals 100, timeframe sorting complete, manual decisions checked | Learner can state scope, current/target/band, dollar drawdown, jobs, route, and wrapper trade-offs |
| Plan the tax path | 5.1–5.2 | Manual tax-review tasks complete or mission skipped | Quantity/basis status is honest and review ends with action, professional question, or deliberate pass |
| Build the retirement paycheck | 1.3, 6.1–6.3 | Timing/income inputs plus manual strategy tasks complete or mission skipped | Need, income, draw, sources, paycheck, and annual policy reconcile and can be explained |
| Protect the plan | 7.1–8.4 | Manual Protect tasks checked | Real recovery, provider, legal, and policy evidence exists or remains visibly open |
| Use and review the plan | 9.1–9.2 | Manual review/Scenario/action/record tasks checked | Learner can explain the plan, owns the next actions, and schedules the next review |

# Gaps requiring product or deployed-flow resolution

1. **No-life-event state:** Mission 1 currently requires at least one life event. Add a deliberate “none right now” completion path.
2. **Manual completion evidence:** Protect and final-review checkboxes need help copy that distinguishes completion from intent and app status from real-world proof.
3. **Skip meaning:** Tax and Retirement Income skip actions should clearly mean “hide for now,” not “this planning area does not apply forever.”
4. **Review freshness:** consider tying `read_plan` completion to a current run or storing the run date, while still retaining the human comprehension finish line.
5. **Stable Academy metadata:** issue #196 already tracks exposing step IDs, routes, completion rules, save behavior, number keys, and course impact from one product registry.

# Final acceptance rule

Before the first walkthrough is recorded:

- Austin must use the deployed seven-mission flow end to end,
- labels and task order must match what the customer sees,
- completion/skip behavior must be tested,
- the synthetic household must continue from the accepted checkpoint,
- exact routes and focus behavior must be recorded,
- and every manual task must state what evidence makes it honestly complete.

Until then, this file is a source-code observation—not a recording script.
