# W03 — Set debt jobs and test one financing decision

Status: CONVERSATIONAL_CAPTURE_REVIEW — revised demonstration narration; actual app/device capture remains pending.
Kind: capture
Gate: APP_CAPTURE
Sources: DEBT, OWNER, APP

### Production basis — not spoken

Use PR #227 accepted direction at reference head `21fedfbb1290bfdd637f3b0879bf7e7d6bfdbbc2`; the [latest directive](https://github.com/azeltwanger/orange-plan/pull/227#issuecomment-5618008737) governs future behavior. This is a capture manuscript, not proof that the planned screens or writers ship. The unchanged Reed fixture and a separately reviewed synthetic extension supply all household facts. Use separate takes after the paired lessons. Only Narration blocks are spoken; overlays are added in editing. All amounts inside an app recording must come from its actual inputs and result. Common rules: [stepwise script standard](../../production/STEPWISE-SCRIPT-STANDARD.md).

#### Chapter 1 — Verify payments and changing terms · after 3.1

**Show:** Use Home → Your Money → Debt and open one existing debt detail at a time. Review the card, mortgage and interest-only HELOC against authorized fictional records. Read current balance, rate, required payment, rate-reset/maturity and security terms; use contextual Add or update only for a verified change.

**Narration:**

We're going to look at what the existing debts require before deciding about extra payments. Here I'll match the balance, rate and required payment to the lender record. The card's $405 minimum isn't all principal: the rough first-month illustration has about $235 of interest and $170 of principal before purchases or fees. The actual statement has its own billing rules.

The home-equity line has a different issue. Its interest-only payment leaves principal to repay later, so the payment-change date and exit matter. Let's keep those beside the cash-flow picture.

The teaching payments are about 17% of gross income, but the original example has only $500 after other costs and Alex's contribution. The ratio doesn't give us extra payment money. That $500 and any proposed spending change are the starting point for choosing what each debt does next.

**Overlay:** Required payment → interest + principal; DTI does not equal surplus

**Verify:** Correct debt record, source and terms survive readback. Required/extra payments remain separate. HELOC date or guarantee omissions remain missing facts rather than inferred defaults.

**Capture dependency:** PR #227 Debt detail owner/contextual writer, payment schedule and source freshness. Exact card billing/minimum rules and HELOC maturity require the reviewed extension. No debt is duplicated or newly adopted by this review.

#### Chapter 2 — Separate household leverage from loan collateral · after 3.6

**Show:** Read included household assets and debt, with net worth separately. Use the unchanged balance-sheet and partial-stress graphics unless the exact app scenario is verified. Then show fixed-debt 50%/25% initial LTV to an assumed 80% liquidation threshold in a separate generic comparison.

**Narration:**

Here we're separating the household's overall debt from one loan's collateral requirements. The Reeds' included assets are $1,996,000 before subtracting debt. Against $444,500 owed, that's about 22% debt-to-assets. The home and restricted or dedicated accounts aren't all cash available for repayment.

In the partial stress illustration, included assets fall to $1,217,200 while debt stays the same. The ratio moves to about 37%. That shows what a fall in asset values does to the household measure.

Now consider the separate lender test. With fixed debt and an assumed 80% liquidation line, 50% initial LTV reaches it after a 37.5% price fall. Posting enough for 25% initial LTV gives a 68.75% decline to that same line. Those numbers compare upfront collateral. The actual agreement's call, cure and liquidation terms are what go into the response rules, alongside the household's ability to fund them.

**Overlay:** Household DTA: 22.27% → 36.52% · One loan’s LTV uses pledged collateral

**Verify:** Assets/debt/net-worth denominators remain distinct. Stress assumptions/exclusions are visible. No Reed Bitcoin loan or integrated worst-case result is fabricated.

**Capture dependency:** Exact supported asset denominator and scenario fields. Source partial stress: BTC exposure −70%, selected stocks −30%, home −20%; education/health unchanged; vehicle/business values omitted while debts included. Fixed-debt threshold graphics are hypothetical, not lender offers.

#### Chapter 3 — Choose and save affordable debt actions · after 3.1

**Show:** In Plan → Scenarios, compare extra card payments against the same current inputs and Reserve claim. Inspect payoff/interest and Cash Flow effect. Use Debt detail’s approved save path only after choosing the action, then read it back. Contrast the low fixed mortgage and review the other debts without fabricating finalized choices.

**Narration:**

We're continuing the reduced-spending test. Your actual surplus stays unchanged until the spending changes happen. Here we're comparing the card with $500 going to the Reserve and $1,200 of extra card principal. The required $405 was already counted, so the total card payment is $1,605.

Let's read the payoff date and interest under that comparison, then see whether required payments and the Reserve still fit. With the mortgage, we're weighing interest avoided against cash becoming home equity. Extra principal may shorten the term without reducing next month's payment, and property costs continue after payoff.

Once you've chosen an affordable action, we'll save it in Debt and reopen it to check the terms. Changing the lender payment is a separate outside step. The saved choice is what we carry back into Cash Flow, so it only uses the money once.

**Overlay:** Reduced example: $405 required + $1,200 extra = $1,605 card total

**Verify:** Comparison does not silently change Current; selected save is counted once in Debt and Cash Flow. Mortgage escrow/property costs remain correctly funded. Each other debt has a choice or precise unresolved term.

**Capture dependency:** Approved future Scenario-to-owner decision flow, extra-payment capacity semantics, debt strategy save/preview behavior, payoff calculation and save/reload. Preserve separate source $500 Reserve and $1,200 extra. No predetermined app payoff date or automatic lender payment.

#### Chapter 4 — Compare one financing purpose through its exit · after 3.4; A3.2 when relevant

**Show:** Use Plan → Scenarios for one hypothetical $30,000 project at the reviewed date. Compare cash, a supported taxable sale and one eligible financing arrangement, plus smaller/delay. Read cash retained, payments, fees, collateral and ending principal. Use a separate graphic for $20,000/8%/60-month amortizing-versus-interest-only arithmetic.

**Narration:**

Let's compare one purchase using the same amount and date in each version. Paying $30,000 from the $32,000 Reserve leaves $2,000 for that job. A taxable sale needs enough proceeds after its actual tax cost. Financing keeps cash initially, but the payment has to fit beside the Reserve and card.

The final balance is part of that comparison. In our separate $20,000 example, about $406 a month pays the loan down over five years; about $133 interest-only leaves the $20,000 owed. A refinance needs the full replacement mortgage priced, while unusual terms need their actual settlement formula, guarantees and use restrictions.

We'll keep any contract term the app doesn't represent beside the comparison and resolve it before choosing. A smaller or delayed project may be the affordable answer. Whichever direction you choose, the payment and principal exit go into the debt rules next.

**Overlay:** Same need/date → cash left → payment → final balance → repayment source

**Verify:** Equal need and dates, actual source tax, complete repayment shape and constraints. Proposal remains separate; no application or approval. Unsupported settlement terms prevent a model-complete conclusion.

**Capture dependency:** Reviewed fictional offer/date, taxes/basis, permitted uses and guarantee terms; approved Scenario expressiveness. Generic arithmetic: $405.5279 amortizing, $4,331.6735 total interest; $133.3333 interest-only, $8,000 interest plus principal. HEI/shared appreciation requires its actual formula; do not approximate it as an ordinary loan.

#### Chapter 5 — Write funded repayment and response rules · after 3.6; A3.1 when relevant

**Show:** Use the existing debt instructions/worksheet alongside Debt for actual loans or Plan → Scenarios for proposals. Record purpose, amount, payment source, principal exit, dates, fallback, operator and backup. For A3.1 only, use a separate generic $50,000/3.5 BTC sizing graphic and an authorized non-broadcast procedure diagram; do not create a Reed Bitcoin loan or initiate a real top-up.

**Narration:**

This is where the borrowing decision becomes something the household can follow. We're writing where the regular payments come from and how the principal gets repaid. If that uses a sale, the amount, date and response to smaller or late proceeds matter. If it uses refinancing, we need an answer for approval not being available.

Then we can connect a review trigger to the resource and person who will respond. Someone trusted needs a way to recognize a time-sensitive problem and find the safe instructions while you're unavailable. Wallet secrets stay out of this record.

If you're using the Bitcoin-loan lesson, there's a separate sizing example to work through here. We start with the full obligation before deciding how much collateral to post. This example dedicates 3.5 BTC to $50,000 of debt when Bitcoin is $100,000. After an 80% decline, those coins are worth $70,000. If posted in time, that's about 71.4% LTV. At the assumed 80% liquidation line, 3.125 BTC only reaches the boundary. The 3.5 BTC provides some room, but any stricter call-cure or maturity term still has to be met.

The $50,000 opening amount assumes separately funded interest and fees. One hypothetical year of 12% capitalized interest makes it $56,000, exactly 80% of the stressed $70,000. So if costs accrue, the initial principal needs reducing or more Bitcoin needs dedicating before borrowing.

After sizing the debt, posting 1 BTC starts it at 50% LTV and leaves 2.5 BTC reserved in cold storage. Posting all 3.5 starts the same loan at about 14.3%. The smaller initial deposit reduces lender exposure but needs a faster response. Reserved coins only count for lender LTV after they arrive and are credited. That's why the top-up trigger, amount, access time and maximum collateral exposure belong here. An automatic feature can't reach into your cold wallet; the actual funding and confirmation requirements still apply.

Repeat borrowing uses the same supporting resources too. In the recurring illustration, $25,000 becomes $28,000 after 12% interest. The next $25,000 draw makes $53,000, and another 12% makes $59,360. We can't reuse the same spare collateral for each draw. If the payment, timed response or final repayment still lacks a resource, the proposal stays unchosen. Once the rules are supported, we can carry the chosen obligation back into the household cash flow.

**Overlay:** Debt first → collateral placement second · Posted BTC and dedicated BTC have different jobs

**Verify:** Ordinary exit and unavailable-operator fallback are usable. Conditional worksheet preserves costs, exact boundary, stricter cure, timely crediting and combined repeated debt. No double-used BTC, automated cold-wallet claim or signed/executed loan.

**Capture dependency:** Actual contract, advanced modeled terms, saved liquidation selection, cost-accrual rule, source identity and approved scenario receipt. D63 parity/fix-first gates remain app implementation work. Any provider procedure requires safe independently authorized capture with no broadcasting, credentials or secret exposure; illustration is not proof a lender accepts the arrangement.

#### Chapter 6 — Carry one debt decision into Cash Flow and Allocation · after 3.6

**Show:** Return to Cash Flow → Debt payments and Saving and investing. Read the saved extra claim from Debt without entering it twice. Show the reduced-state bridge and a distinctly future payoff condition, then hand current/future claims to W04.

**Narration:**

Let's bring the debt choice back to Cash Flow and see the same money one more time. In the reduced-spending illustration, $2,475 before Alex's $775 contribution becomes $1,700 afterward. The $500 Reserve and $1,200 extra-card plan use that amount once, so there isn't another amount to invest now.

When the card is actually paid off, we'll verify which payments ended and whether any charge remains. The example's $405 required plus $1,200 extra would release $1,605 if those were still being paid. That future money needs a new decision; payoff doesn't automatically send it into investments.

What we take into Allocation is today's chosen claims and that future review condition. Then we can decide where contributions go and what they buy, using the money actually available at the time.

**Overlay:** Today: $1,700 assigned once · After payoff: verify the released $1,605 before routing

**Verify:** Debt and Cash Flow read one saved state. Required payments, Reserve and payroll saving are not duplicated. Future payoff money does not appear in current surplus or an automatic transfer.

**Capture dependency:** D37 payoff/removal semantics and D32 saving owner; exact source state, schedule, future start/stop and readback. Preserve W04’s existing conditional allocation illustration. No bank or lender action is implied by the planning save.

### Member checkpoint

Each debt has verified payment terms and a chosen job or a precise missing contract answer. Required payments, Reserve funding and extra debt use the monthly money once. A financing comparison includes cash retained, affordable payments, ending principal and a funded repayment source; leaving the proposal unchosen is valid. Any chosen saved debt action reads back correctly, with lender or bank changes listed separately. If Bitcoin collateral applies, the separate operating sheet covers full debt growth, dedicated versus posted collateral, contract triggers, timely response and the principal exit before the loan is used.

### Source and continuity notes — not spoken

The paired teaching scripts retain their deck/source IDs and dated research boundaries. Original dictation, accepted Reserve reference and prior manuscripts remain preserved; this stepwise rewrite follows Austin’s September 10 authorization. It changes no household fixture, financial model, provider state, learner account or real-world financial instruction. Build-dependent proof, final voice review and any qualified review remain separate.
