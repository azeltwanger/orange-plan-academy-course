# Demo-number reconciliation audit

**Status:** active pre-dictation QA  
**Authority:** `DEMO-HOUSEHOLD.md`  
**Goal:** remove numeric contradictions before Austin reviews or dictates scripts so he does not have to approve wording twice.

This audit separates three problems:

1. **True conflict** — two files claim different facts about the continuous demo household.
2. **Unlabelled separate example** — the math may be valid, but the learner cannot tell that it is not the demo household.
3. **Unsupported app output** — the course presents a calculated result that has not been reproduced from a versioned demo account.

## Highest-priority corrections

| Area | Current conflict | Required correction | Status |
|---|---|---|---|
| Module 1 confidence | The current draft uses a precise planned age, confidence, and earliest qualifying age before a versioned demo run exists. | Keep the mechanism; label any precise result hypothetical until the checkpoint export supplies the real values. | OPEN |
| Current vs retirement spending | Cash Flow uses $80,000 living spending while Income drafts use $100,000 without consistently explaining whether this is a different stage or a different lifestyle. | Lock both current and planned retirement living spending at $80,000 for the continuous demo. Keep taxes and debt outside living spending. | OPEN |
| Retirement first-year funding | Current Income draft uses $100,000 spending + $18,000 costs − $20,000 income = $98,000. | Use $80,000 spending + $18,000 taxes/debt − $0 recurring income = $98,000. This preserves the total while making every component match the demo. | OPEN |
| Social Security bridge | One draft implies a 5-year bridge; the older teaching example and locked profile imply retirement at 60 and full Social Security at 67. | Use a 7-year income bridge for the demo. Explain account-access rules separately and avoid one universal age shortcut. | OPEN |
| Starting-spending bands | Draft amounts of $86k / $100k / $119k are presented as though the demo account produced them. | Replace with placeholders or clearly hypothetical round examples until the Income page produces the actual 95/80/60 amounts. | OPEN |
| Annual guardrail dollars | A 10% change is explained from a $100,000 target. | Use $80,000 for the demo: maximum 10% correction is up to $8,000/year or about $667/month before the exact policy calculation. | OPEN |
| Retirement reserve | Dictated 2.2 uses $80,000 and $51,600, while later Income drafts use different spending and income values. | Keep the dictated $120,000 early target and approximately $43,000 later target as the continuous demo arithmetic. | OPEN |
| Insurance need | Insurance draft begins from $100,000 living spending even though current household spending is $80,000, then derives a $55,000 survivor gap without a visible survivor budget. | Show the survivor all-in need as $95,000, less $40,000 survivor income = $55,000. State that $175,000 is existing coverage plus usable assets, not the entire Bitcoin stack. | OPEN |
| College commitment | The household has two children, while the lesson can read as though $80,000 is for one child or each child. | State that $80,000 is the household's total family commitment across the education goal unless Austin deliberately changes it. | OPEN |
| Contribution route | The $4,000 surplus route includes a $750 workplace contribution, but the interaction with payroll deductions and the tax estimate is not explicit. | Define $4,000 as available before new savings routing and verify the app does not count the employee deferral twice. | OPEN |

## Module-by-module pass

### Module 0

| File | Check | Status |
|---|---|---|
| `scripts/00-1_how-to-use-this-course.md` | Course map matches current 28-lesson core structure. | VERIFY AFTER OTHER MODULES |
| `lesson-text/00-1_how-to-use-this-course.md` | Same module names and outcomes as `CURRENT-COURSE.md`. | VERIFY AFTER OTHER MODULES |
| 0.2 script and text | No demo arithmetic; AI versus engine distinction is stable. | LOW RISK |

### Module 1

| File | Check | Status |
|---|---|---|
| 1.1 script and text | Source-document list supports every locked demo input. | REVIEW |
| 1.2 script and text | Broad assumptions versus holding overrides; spot Bitcoin ETF example remains generic. | REVIEW |
| 1.3 script and text | Replace unsupported exact confidence/age result or mark it hypothetical. | OPEN |
| 1.3 script and text | Planned retirement age must be 60 when referring to the demo. | OPEN |
| 1.3 script and text | Current living spending and retirement spending must not be conflated. | OPEN |

### Module 2

| File | Check | Status |
|---|---|---|
| 2.1 script and text | $190k − $40k − $80k − $22k = $48k/year = $4k/month. | RECONCILES |
| 2.1 script and text | Living excludes mortgage and car payments. | RECONCILES |
| 2.2 script | $5k × 6 = $30k working reserve. | RECONCILES |
| 2.2 script | $80k early-retirement spending → $120k at 18 months. | RECONCILES |
| 2.2 script | $80k − $51.6k = $28.4k gap → approximately $43k at 18 months. | RECONCILES |
| 2.3 script and text | $35k vehicle − $10k proceeds − $5k purchase-year flow = $20k pre-fund. | RECONCILES |
| 2.4 script and text | $80k commitment − $25k 529 − $20k cash flow − $10k other = $25k gap. | RECONCILES; CLARIFY TWO-CHILD TOTAL |

### Module 3

| File | Check | Status |
|---|---|---|
| 3.1 script and text | Debt $280k + $18k = $298k. | RECONCILES |
| 3.1 script and text | DTI $22k / $190k = 11.6%. | RECONCILES |
| 3.1 script and text | DTA $298k / $745k = 40.0%. | RECONCILES |
| 3.1 script and text | Household ceiling is Austin judgment, not an app-derived fact. | REVIEW JUDGMENT |

### Module 4

| File | Check | Status |
|---|---|---|
| 4.1 script and text | $175k BTC / $295k investable = 59.3%. | RECONCILES |
| 4.1 script and text | $175k BTC / $745k gross assets = 23.5%. | RECONCILES |
| 4.1 script and text | 75% BTC drawdown removes $131,250 and leaves $43,750 BTC. | RECONCILES |
| 4.2 script and text | Stocks $75k + bonds $15k + cash $30k + BTC $175k = $295k. | RECONCILES |
| 4.2 script and text | Account-level holdings must match the $25k 529 used in Module 2.4. | OPEN DETAIL CHECK |
| 4.3 script and text | $750 + $500 + $1,250 + $1,500 = $4,000. | RECONCILES |
| 4.3 script and text | Employee contribution and tax treatment are not counted twice. | APP VERIFICATION NEEDED |
| 4.4 script and text | Account-location example preserves the same household allocation. | REVIEW |

### Module 5

| File | Check | Status |
|---|---|---|
| 5.1 script and text | 1.25 + 0.40 + 0.10 = 1.75 BTC. | RECONCILES |
| 5.1 script and text | Only $48k basis is known; no complete sale-tax result is claimed for unresolved lots. | REVIEW |
| 5.2 script and text | No demo tax amount is stated without a state and current app calculation. | REVIEW |
| 5.2 script and text | RMD, Roth, capital-gain, and conversion language receives CPA review. | PROFESSIONAL REVIEW |

### Module 6

| File | Check | Status |
|---|---|---|
| 6.1 script and text | Retirement living spending should be $80k, not $100k. | OPEN |
| 6.1 script and text | Full recurring floor $51.6k at age 67. | OPEN ALIGNMENT |
| 6.1 script and text | Income bridge is 7 years from age 60 to 67. | OPEN |
| 6.1 script and text | Retirement cash buffer examples reconcile to 2.2. | OPEN |
| 6.2 script and text | First-year total draw remains $98k using $80k + $18k − $0. | OPEN |
| 6.2 script and text | Illustrative $60k taxable + $38k traditional source split adds to $98k. | RECONCILES; APP OUTPUT PENDING |
| 6.2 script and text | Borrowing remains optional and all loan costs/risk are shown. | REVIEW |
| 6.3 script and text | Replace $100k target and unsupported exact bands. | OPEN |
| 6.3 script and text | Keep Plan confidence, spending-band confidence, and annual policy separate. | RECONCILES CONCEPTUALLY |

### Module 7

| File | Check | Status |
|---|---|---|
| 7.1 script and text | 1.50 BTC self-custody + 0.25 BTC exchange = 1.75 BTC. | RECONCILES |
| 7.2 script and text | Recovery testing does not tell the learner to wipe the only meaningful device without safeguards. | RECONCILES |
| 7.3 script and text | Family map contains process, never secrets. | RECONCILES |
| Module 7 | Technical claims receive custody-professional review. | PROFESSIONAL REVIEW |

### Module 8

| File | Check | Status |
|---|---|---|
| 8.1 script and text | One stale workplace beneficiary record is the demo problem. | RECONCILES |
| 8.2 script and text | 2-of-3 is described as three keys where any two sign. | RECONCILES |
| 8.2 script and text | Descriptor/configuration is non-secret but privacy-sensitive. | REVIEW |
| 8.3 script and text | Dead-man switch is an additional notification path, not sole delivery or authority. | RECONCILES |
| 8.4 script and text | Replace $100k current living figure with visible $95k survivor need calculation. | OPEN |
| 8.4 script and text | $55k × 15 + $180k = $1.005M; minus $175k = $830k. | RECONCILES |
| Module 8 | Estate and insurance claims receive appropriate licensed review. | PROFESSIONAL REVIEW |

### Module 9

| File | Check | Status |
|---|---|---|
| 9.1 script and text | No universal 1-minute or 5-minute promise. | RECONCILES |
| 9.1 script and text | Annual review uses the same module sequence as the course. | REVIEW |
| 9.2 script and text | No precise Scenario result is presented as demo output before app run. | REVIEW |
| 9.2 script and text | PDF and encrypted backup have separate jobs. | RECONCILES |

## App checkpoint outputs still required

The following are not safe to lock from prose alone:

- Plan confidence at the planned age
- Earliest date reaching the selected confidence target
- Income spending-band amounts at 95%, 80%, and 60%
- Current and projected federal/state taxes
- Exact first-year funding source split
- Exact Bitcoin sold and retained
- Exact account balances after each module
- Exact reserve status under the selected current app basis
- Ending assets and estate values
- Scenario deltas
- Protect readiness counts

The demo account must produce these results after the locked inputs are entered. Save a versioned export or checkpoint receipt for every module before the values appear in slides or recorded walkthroughs.

## Completion definition

The demo-number pass is complete when:

1. Every true conflict above is patched in both script and lesson text.
2. Every separate example is labelled as separate.
3. Every simple arithmetic chain reconciles.
4. Every calculated app output is tied to a versioned demo checkpoint.
5. `DEMO-HOUSEHOLD.md` is the only place where approved demo inputs are changed.
