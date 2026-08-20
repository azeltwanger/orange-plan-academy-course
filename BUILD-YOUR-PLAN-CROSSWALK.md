# Build Your Plan ↔ Orange Plan Academy walkthrough crosswalk

**Status:** exact preview-code mapping complete; deployed end-to-end acceptance still pending  
**Customer-facing concept review:** `azeltwanger/orange-plan` `main` at `8019bfcf14387f2e15746b18707534bfcb7eb4e5`  
**Reproducible demo engine:** app commit `3105664da5dd77c57bf6d489e28b8f3a5e3d3eb5`  
**Build Your Plan code observation:** `demo/BUILD-YOUR-PLAN-CODE-OBSERVATION-2a3bf88.md`  
**Observed preview commit:** `2a3bf8872b35e782c6fb098d1a65ffcdf9a85666`  
**Exact walkthroughs:** hold until Austin completes the deployed Build Your Plan flow end to end

## Standing rule

**Build Your Plan is the navigation spine for walkthroughs. It is not required to be the exact syllabus for every concept lesson.**

The Academy groups concepts in the order that makes the decisions easiest to understand. The product groups implementation into seven missions.

A source-code observation is useful enough to prepare the crosswalk and identify completion risks. It is not sufficient to record final clicks, labels, screenshots, or save behavior when the deployed working tree may differ.

## What is already complete

The continuous demo already has reconciled engine candidates for:

- confidence and earliest target-qualified date,
- Cash Flow and reserve,
- debt ratios and payoff,
- Allocation scope, current mix, target, band, and drawdown,
- basis/tax status,
- retirement-spending choices, total draw, sources, and Bitcoin units,
- and the 4% inflation Scenario.

Build Your Plan does not need to rediscover those numbers. The final walkthrough verifies how the customer enters, saves, completes, and returns from each mission.

## Walkthrough learner loop

1. Recall the decision from the concept lesson.
2. Enter through the matching Build Your Plan mission.
3. Continue from the accepted demo checkpoint.
4. Name Saved / Previewing / Scenario / read-only state.
5. Implement only the decision already taught.
6. Explain the material result using number provenance.
7. Return to Build Your Plan.
8. State both finish lines:
   - `app_completion_rule`
   - `human_completion_rule`

An app checkmark certifies the current product rule. The Academy finish line certifies that the learner understands the trade-off and made the decision honestly.

---

# Seven observed missions

## 1 · Get organized

**App ID:** `organized`  
**Starting state:** approved source documents  
**Ending checkpoint:** `demo-v1-baseline`

| Task | Route | Product completion | Core teaching |
|---|---|---|---|
| `add_accounts` · Add every account | `/Dashboard` | At least one account | 1.1 |
| `add_holdings` · Add the holdings inside them | `/Dashboard` | At least one holding | 1.1 and 4.2 |
| `split_household` · Separate mine, yours, and joint | `/Household?focus=ownership` | Manual key `build_organized_people_split` | 1.1–1.2 |
| `life_events` · Put the big future costs and changes on the calendar | `/Plan?focus=life-events` | At least one life event | 1.2, 2.3, 2.4 |

**Human finish line:** the plan is honest about verified, estimated, missing, expected, and Scenario information.

**Open product gap:** a household with no meaningful future event needs a deliberate “none right now” completion state rather than being forced to invent one.

## 2 · Find financial capacity

**App ID:** `capacity`  
**Starting checkpoint:** `demo-v1-baseline`  
**Ending checkpoint:** `demo-v1-cashflow` plus `demo-v1-debt`

| Task | Route | Product completion | Core teaching |
|---|---|---|---|
| `cash_flow` · Confirm income, taxes, living spending, and Debt | `/CashFlow?focus=summary` | Gross income and current spending exist | 2.1 |
| `reserve` · Choose the working reserve | `/CashFlow?focus=reserve` | Reserve months and basis saved | 2.2 |
| `debt` · Choose the Debt treatment | `/Debt?focus=strategy` | No active debts, or each active debt reviewed | 3.1 |
| `contributions` · Route the next dollar | `/CashFlow?focus=routing` | Manual key `build_capacity_contributions` | 4.3 |

**Human finish line:** learner can rebuild post-debt capacity, explain the reserve and debt treatment, and route the remaining amount without counting the extra debt twice.

Canonical demo:

> $4,261 capacity before extra debt − $500 extra auto principal = $3,761 post-debt surplus  
> $3,500 account route + $261 operating cushion

## 3 · Aim the portfolio

**App ID:** `portfolio`  
**Starting checkpoint:** `demo-v1-debt`  
**Ending checkpoint:** `demo-v1-allocation`

| Task | Route | Product completion | Core teaching |
|---|---|---|---|
| `allocation_range` · Choose the Bitcoin range you will review against | `/Allocation?focus=mix` | Holdings exist and saved target totals 100 | 4.1 |
| `timeframes` · Give Reserve, Bridge, and Legacy a job | `/Allocation?focus=timeframes` | All in-scope holdings sorted; home and 529 excluded | 4.2 |
| `contribution_allocation` · Decide what future dollars buy | `/Allocation?focus=contributions` | Manual key `build_portfolio_contribution_allocation` | 4.3 |
| `account_location` · Choose which holdings belong in which accounts | `/Allocation?focus=accounts` | Manual key `build_portfolio_account_location` | 4.4 |

**Human finish line:** learner can state the $270,000 denominator, 64.8% current Bitcoin allocation, 50% target, 40–60% review band, $131,250 drawdown loss, holding jobs, and post-debt route.

A target totaling 100 proves a complete input. It does not prove the household can hold the allocation.

## 4 · Plan the tax path

**App ID:** `tax`  
**Starting checkpoint:** `demo-v1-allocation`  
**Ending checkpoint:** `demo-v1-tax`  
**Product skip key:** `build_plan_skip_tax`

| Task | Route | Product completion | Core teaching |
|---|---|---|---|
| `cost_basis` · Get cost basis usable before the next sale | `/Tax?focus=cost-basis` | Manual key `build_tax_cost_basis` | 5.1 |
| `tax_report` · Read the year-by-year tax roadmap | `/Tax?focus=overview` | Manual key `build_tax_report` | 5.2 |
| `tax_opportunities` · Flag conversion, harvesting, or repayment windows | `/Tax?focus=harvesting` | Manual key `build_tax_opportunities` | 5.2 / Advanced gates |
| `tax_follow_through` · Record what happens now, later, or never | `/Tax?focus=roth-conversion` | Manual key `build_tax_follow_through` | 5.2 |

**Human finish line:** current quantity and basis status are honest and the review ends with one action, one professional question, or a deliberate pass.

The manual cost-basis task allows reviewed-but-unresolved basis. The learner does not need to invent a value merely to complete the mission.

**Skip meaning:** hide for now—not proof that tax never applies and not Academy completion.

## 5 · Build the retirement paycheck

**App ID:** `retirement_income`  
**Starting checkpoint:** `demo-v1-tax`  
**Ending checkpoint:** `demo-v1-income`  
**Product skip key:** `build_plan_skip_retirement_income`

| Task | Route | Product completion | Core teaching |
|---|---|---|---|
| `retirement_timing` · Set retirement timing and spending | `/Plan?focus=retirement-age` | Retirement age and spending exist | 1.3 and 6.1 |
| `income_floor` · Add Social Security, pensions, and other recurring income | `/Plan?focus=social-security` | Required custom benefit inputs exist, or custom mode is off | 6.1 |
| `withdrawal_strategy` · Choose the withdrawal and refill policy | `/Income?focus=withdrawal-order` | Manual key `build_retirement_withdrawal_strategy` | 6.2 |
| `sell_borrow_hold` · Decide when you sell, borrow, or keep holding | `/Income?focus=overview` | Manual key `build_retirement_sell_borrow_hold` | 6.2 |

**Human finish line:** spending, phased income floor, total need, recurring income, total draw, account/holding sources, saved $100,000 paycheck, and annual policy reconcile.

The final task does not require borrowing. The Core demo completes it by deliberately keeping borrowing out of the saved baseline.

**Skip meaning:** hide for now—not proof that retirement-income planning is permanently irrelevant.

## 6 · Protect the plan

**App ID:** `protect`  
**Starting checkpoint:** `demo-v1-income`  
**Ending checkpoint:** `demo-v1-protect`

| Task | Route | Product completion | Core teaching |
|---|---|---|---|
| `custody_recovery` · Document custody and prove recovery | `/Protect?focus=recovery` | Manual key `build_protect_custody_recovery` | 7.1–7.3 |
| `beneficiaries` · Check beneficiaries everywhere | `/Protect?focus=beneficiaries` | Manual key `build_protect_beneficiaries` | 8.1 |
| `estate_roles` · Name the people and documents that let others act | `/Protect?focus=estate` | Manual key `build_protect_estate_roles` | 8.1–8.2 |
| `heir_letter` · Write the heir letter and add the backup delivery path | `/Protect?focus=heir-letter` | Manual key `build_protect_heir_letter` | 8.3 |
| `coverage` · Fill the insurance gaps the family cannot absorb | `/Protect?focus=coverage` | Manual key `build_protect_coverage` | 8.4 |

**Human finish line:** real recovery, provider, legal, family, and insurance evidence exists or remains visibly open.

A manual checkbox cannot prove recovery, legal validity, provider acceptance, coverage, or another person's capability. Every walkthrough states what real-world evidence makes the task honestly complete.

## 7 · Use and review the plan

**App ID:** `review`  
**Starting checkpoint:** `demo-v1-protect`  
**Ending checkpoint:** `demo-v1-final`

| Task | Route | Product completion | Core teaching |
|---|---|---|---|
| `read_plan` · Run the plan and read the result | `/Plan?run=confidence` | Manual key `build_review_read_plan` | 1.3 and 9.2 |
| `run_scenario` · Compare one real decision | `/Scenarios` | Manual key `build_review_scenario` | 9.2 |
| `action_list` · Turn the result into one to three actions | `/YourPlan` | Manual key `build_review_actions` | 9.1–9.2 |
| `save_record` · Save the annual record and schedule the next review | `/YourPlan` | Manual key `build_review_record` | 9.1–9.2 |

**Human finish line:** learner can explain the plan in six sentences, owns one to three dated actions, distinguishes PDF from encrypted export, and understands that in-app restore is currently unavailable.

The manual `read_plan` checkbox does not prove the calculation is current or the result is understood. A dated run/receipt and learner explanation remain separate requirements.

---

# Code-observed focus/navigation contract

The preview uses:

- `buildArea`
- `buildTask`
- `buildReturn`

The focus key is `areaId:taskId`. The default return label is **Return to Your Plan**.

The final run sheet records:

- `app_step_id`
- `app_step_label`
- `primary_route`
- `accepted_app_commit`
- `verified_date`
- `demo_household_version`
- `starting_checkpoint`
- `ending_checkpoint`
- `planning_decisions_implemented`
- `saved_input_or_preview_or_scenario`
- `app_completion_rule`
- `human_completion_rule`
- `important_number_keys`
- `screenshot_or_recording_reference`
- `known_holds`

# Current product gaps

1. **No major life events:** Foundation currently requires at least one life event. The product needs an honest none-state.
2. **Manual proof boundaries:** Protect and final-review tasks need help text distinguishing a checked task from real-world evidence or comprehension.
3. **Skip semantics:** Tax and Retirement Income skips should clearly mean hide/defer, not permanently complete or irrelevant.
4. **Plan freshness:** consider storing or checking a current run date for `read_plan` while retaining the separate human comprehension finish line.
5. **Stable metadata:** app issue #196 tracks one canonical step registry with stable IDs, routes, completion rules, save behavior, number keys, and Academy impact.

# Candidate outputs the walkthroughs verify

- Plan: 94.6% at Alex 55; May 2032 / Alex 51 earliest 80% date
- Cash Flow: $36,862 tax; $3,761 post-debt surplus; $3,500 account route; $261 cushion
- Debt: 11.6% DTI; 40.0% DTA; 2027 auto payoff
- Allocation: $270,000 scope; 64.8% Bitcoin; 50% target; 40–60% band; $131,250 drawdown loss
- Tax: 1.25 BTC / $48,000 known basis; 0.50 BTC unresolved
- Income: $100,000 saved at 94.6%; $101,948 first-year draw; $97,948 / 0.079251 BTC sale
- Scenario: 4% inflation = 91.6%, down 3 points

Protect requires UI status plus real-world proof and has no engine-owned pass result.

# Final acceptance rule

Before recording a walkthrough:

1. Austin completes the deployed seven-mission flow end to end.
2. Customer-facing labels, order, routes, and focus behavior match the record.
3. Auto/manual/skip completion behavior is tested.
4. The same synthetic household continues from the accepted checkpoint.
5. Important output and source rows match the receipt.
6. Every manual task states the evidence required for honest completion.
7. The app checkmark and Academy finish line are both spoken.

Until then, `demo/BUILD-YOUR-PLAN-CODE-OBSERVATION-2a3bf88.md` is an engineering observation—not a recording script.
