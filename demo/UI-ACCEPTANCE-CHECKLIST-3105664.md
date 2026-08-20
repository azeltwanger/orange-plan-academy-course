# Academy demo — deployed UI acceptance checklist

**Engine candidate:** app commit `3105664da5dd77c57bf6d489e28b8f3a5e3d3eb5`  
**Fixture:** `demo-v1-inputs`  
**Purpose:** convert the reconciled engine candidate into eight final app receipts without rediscovering what to verify.

This is a synthetic-account procedure. Never use a client account, Austin's personal plan, real account numbers, credentials, wallet addresses, custody locations, or Bitcoin secrets.

## Before the run

Record:

- deployed URL,
- displayed app version/commit when available,
- browser and viewport,
- fixture version,
- synthetic-account identifier,
- date and time,
- whether the page is showing Saved, Previewing, Scenario, or read-only output,
- and whether Build Your Plan is open.

Use the same account for the whole run. Do not reset one page between checkpoints unless the reset is part of the recorded procedure.

---

# 1 · Baseline receipt

**Primary route:** `/plan` or the current Plan → Retirement surface  
**Receipt ID:** `demo-v1-baseline`

Confirm visible inputs:

- household retirement age: Alex 55
- Baseline retirement spending: $100,000 in today's dollars
- planning age: 95
- confidence target: 80%
- 3% inflation baseline
- built-in Power Law Bitcoin view

Confirm visible outputs:

- confidence at planned date: **94.6%**
- earliest target-qualified date: **May 2032 / Alex age 51**
- the page does not display a second deterministic result beside Monte Carlo
- the retirement age is one household date anchored to the primary person's age

Capture:

- full result card,
- confidence target control,
- earliest-date label,
- saved/preview state,
- and source path for changing retirement age and spending.

Block the receipt when the visible value or label differs from the candidate without an explained app change.

---

# 2 · Cash Flow receipt

**Primary route:** `/cash-flow`  
**Receipt ID:** `demo-v1-cashflow`

Confirm visible source rows:

- gross household income: $190,000/year
- modeled tax: approximately **$36,862/year**
- living spending: $80,000/year, debt excluded
- required debt: approximately $1,833/month
- saved extra auto principal: $500/month
- planned debt total: approximately $2,333/month

Confirm output and route:

- displayed surplus after planned debt: approximately **$3,761/month**
- account contributions after debt: **$3,500/month**
- operating cushion: approximately **$261/month**
- full decision route: $500 extra debt + $3,500 contributions = $4,000/month
- bare-bones spending: $5,000/month
- reserve: $30,000 target, $30,000 current, 6 months funded

Capture:

- the source equation,
- the Debt row showing extra principal,
- the route after debt,
- reserve basis and target,
- and the edit source for each line.

The receipt fails if the $500 extra principal is counted both inside Debt and again as an additional use of the displayed post-debt surplus.

---

# 3 · Debt receipt

**Primary route:** `/debt`  
**Receipt ID:** `demo-v1-debt`

Confirm:

- mortgage: $280,000 at 3.25%, $1,450 required payment, required payment only
- auto: $18,000 at 7%, approximately $383 required plus $500 extra
- total debt: $298,000
- DTI: **11.6%**
- DTA at reference valuation: **40.0%**
- projected auto payoff: **2027 / Alex age 46**
- household policy recorded separately: 25% DTI ceiling; no new debt at 40%+ DTA

Capture the ratio labels, denominator help, treatment state, and payoff result.

---

# 4 · Allocation receipt

**Primary route:** `/allocation`  
**Receipt ID:** `demo-v1-allocation`

Confirm inclusion/exclusion:

- primary residence excluded
- 529 excluded as beneficiary-restricted
- allocatable portfolio: **$270,000**
- broader financial balances including the 529: $295,000
- Bitcoin: $175,000

Confirm decision state:

- current Bitcoin allocation: **64.8%**
- target: 50%
- review band: 40–60%
- page indicates above-band review rather than an automatic sell instruction
- taxable Bridge contributions follow target and drift rather than automatically buying Bitcoin

Confirm drawdown:

- 75% Bitcoin loss: $131,250
- allocatable portfolio after that Bitcoin loss, other holdings flat: $138,750

Capture the denominator or included holdings, target controls, review state, and contribution action.

---

# 5 · Tax receipt

**Primary route:** `/tax`  
**Receipt ID:** `demo-v1-tax`

Confirm basis status:

- total Bitcoin quantity: 1.75 BTC
- complete lots: 1.25 BTC with $48,000 known basis
- reconstruction pending: 0.40 BTC
- unknown: 0.10 BTC
- unresolved basis remains visible

Confirm the app does not imply:

- that unknown basis is complete,
- that an app HIFO/FIFO preview executed a real sale,
- or that the tax roadmap is a filed return.

Capture the current-year tax value, roadmap label, basis warning, lot status, and any saved versus preview state.

This receipt remains professionally qualified until the CPA packet is returned.

---

# 6 · Retirement Income receipt

**Primary route:** `/income`  
**Receipt ID:** `demo-v1-income`

## Spending choices

Confirm:

- Conservative / 95%: approximately **$99,317/year**
- Current Plan: **$100,000/year at 94.6%**
- Balanced / 80%: approximately **$170,216/year**
- Aggressive / 60%: approximately **$249,904/year**
- saved starting paycheck remains $100,000/year
- Plan confidence, starting-spending choice, and annual guardrails appear as separate controls

## First retirement calendar year

Confirm visible components or drill-down:

- base living spending: $129,912
- college event: $13,439
- living need: $143,351
- debt: $17,400
- tax: $10,632
- total need: **$171,383**
- partial-year household wages: $42,557
- inflation-adjusted part-time income: $26,878
- recurring income: **$69,435**
- total draw: **$101,948**

## Sources

Confirm:

- taxable accounts are the account source
- cash: approximately $2,200
- stocks: approximately $1,800
- Bitcoin: approximately $97,900
- account source total: approximately $101,946
- Bitcoin sale proceeds: $97,948
- projected Bitcoin price: $1,235,921
- Bitcoin sold: approximately **0.079251 BTC**

The dollars, projected price, and units must come from the same year. Do not accept a quantity derived from today's $100,000 reference price.

Capture the total-need side, recurring-income side, source side, Bitcoin dollars/units, spending cards, and saved policy state.

---

# 7 · Protect receipt

**Primary route:** `/protect`  
**Receipt ID:** `demo-v1-protect`

Capture the app's visible status for:

- custody type,
- recovery test,
- top single point of failure,
- Family Custody Map,
- beneficiaries and roles,
- heir letter and delivery,
- policies and coverage gaps,
- and overall readiness.

Real-world boundary:

- recovery remains incomplete until a supported device/practice test works,
- legal status remains incomplete until counsel/provider/court evidence exists,
- beneficiary status remains incomplete until the provider accepts the record,
- insurance status remains incomplete until the actual contract is verified.

Never enter or capture a seed phrase, key, passphrase, PIN, password, wallet backup, full account number, or exact custody location.

---

# 8 · Final / Scenario / Report receipt

**Primary routes:** `/scenarios`, `/your-plan`, and the current report/export controls  
**Receipt ID:** `demo-v1-final`

Confirm the inflation Scenario:

- baseline inflation: 3%
- baseline confidence: 94.6%
- Scenario inflation: 4%
- Scenario confidence: **91.6%**
- delta: **−3.0 percentage points**
- baseline remains unchanged

Confirm report and record behavior:

- the report agrees with the saved Plan, Cash Flow, Debt, Allocation, Tax, Income, and Protect state
- one to three next actions have owners and dates
- PDF is the readable annual snapshot
- encrypted export is the passphrase-protected data copy
- in-app restore is not described as currently available while restore remains disabled

Do not use the $428,365,615 modeled ending value as a Core promise or primary visual.

---

# Build Your Plan metadata pass

After Austin uses the deployed Build Your Plan flow end to end, record for every step:

- stable step ID,
- current label,
- primary route,
- save/apply/autosave behavior,
- app completion rule,
- human planning finish line,
- Academy lesson IDs,
- important number keys,
- and last verified app commit.

Do not write an exact click path from a mockup or code branch that Austin has not used.

# Final acceptance rule

A candidate becomes a final receipt only when:

- synthetic identity is confirmed,
- visible output agrees or the difference is explained,
- source lines reconcile,
- saved/preview/Scenario state is recorded,
- screenshot or recording evidence is safe,
- app commit and fixture version are stored,
- and no unresolved failure is hidden by rounding or a checkmark.
