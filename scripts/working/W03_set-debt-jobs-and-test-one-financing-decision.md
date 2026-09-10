# W03 — Set debt jobs and test one financing decision

Status: CONVERSATIONAL_CAPTURE_REVIEW — revised demonstration narration; actual app/device capture remains pending.
Kind: capture
Gate: APP_CAPTURE
Sources: DEBT, OWNER, APP

### Production basis — not spoken

Use PR #227 accepted direction at reference head `21fedfbb1290bfdd637f3b0879bf7e7d6bfdbbc2`; the [latest directive](https://github.com/azeltwanger/orange-plan/pull/227#issuecomment-5618008737) governs future behavior. This is a capture manuscript, not proof that the planned screens or writers ship. The unchanged example household data and a separately reviewed synthetic extension supply all household facts. Use separate takes after the paired lessons. Chapter 4 is used only for a proposed financing decision; chapter 5 is only for Bitcoin collateral after A3.1. Ordinary debt repayment instructions remain in chapter 6. Only Narration blocks are spoken; overlays are added in editing. All amounts inside an app recording must come from its actual inputs and result. Common rules: [stepwise script standard](../../production/STEPWISE-SCRIPT-STANDARD.md).

#### Chapter 1 — Verify payments and changing terms · after 3.1

**Show:** Use Home → Your Money → Debt and open one existing debt detail at a time. Review the card, mortgage and interest-only HELOC against authorized fictional records. Read current balance, rate, required payment, rate-reset/maturity and security terms; use contextual Add or update only for a verified change.

**Narration:**

Let's match each existing debt to the lender record before choosing extra payments. We're checking the balance, rate, required payment and any date when the terms change. I'll use the debts that apply to your household.

With the example card, the $405 minimum isn't all principal. The rough first-month illustration has about $235 of interest and $170 reducing the balance, before new purchases or fees. The real statement has its own billing rules.

For the interest-only home-equity line, $46,000 at the example's 8% rate costs about $307 a month without clearing principal. The payment-change date and repayment source belong beside that figure. With the other example debts, the 6.7% auto loan has a $600 payment and the 7.4% equipment loan has a $480 payment; removing those payments uses different amounts of cash, and the business still has operating needs.

The listed payments are about $3,342 against about $19,417 gross income, roughly 17%. That's payment pressure before tax and other deductions. We'll use the available cash verified earlier to decide about extra payments; the ratio doesn't provide another pool of money.

**Overlay:** Required payment → interest + principal; DTI does not equal surplus

**Verify:** Correct debt record, source and terms survive readback. Required/extra payments remain separate. HELOC date or guarantee omissions remain missing facts rather than inferred defaults.

**Capture dependency:** PR #227 Debt detail owner/contextual writer, payment schedule and source freshness. Exact card billing/minimum rules and HELOC maturity require the reviewed extension. No debt is duplicated or newly adopted by this review.

#### Chapter 2 — Separate household leverage from loan collateral · after 3.6

**Show:** Read included household assets and debt, with net worth separately. Use the unchanged balance-sheet and partial-stress graphics unless the exact app scenario is verified. Keep the household-resource comparison here; lender-specific LTV mechanics belong to A3.1 and conditional chapter 5.

**Narration:**

Here we're looking at the resources supporting the household's debt. The example includes $1,996,000 of assets before subtracting $444,500 owed. That's about 22% debt-to-assets; subtracting the debt leaves $1,551,500 net worth.

Notice what those totals include. The home and retirement, education and health accounts have different access rules and other jobs. We also omitted vehicle and business-equipment values while including their debts. This is a teaching balance sheet, not a complete appraisal or a pile of accessible repayment cash.

In the partial stress illustration, Bitcoin exposure falls 70%, selected stocks fall 30% and the home falls 20%. Education and health values are held unchanged. Included assets become $1,217,200, while debt is still $444,500. The ratio rises to about 37%.

That shows what lower values do to the household measure. It doesn't test every bad outcome or tell us what one lender can require. For a collateral-backed loan, the actual agreement and accessible response money need a separate check. If Bitcoin backs your loan, complete the Bitcoin-loan lesson before the collateral walkthrough. We'll record ordinary repayment and fallback when we bring the debt choices back to Cash Flow.

**Overlay:** Household DTA: 22.27% → 36.52% · One loan’s LTV uses pledged collateral

**Verify:** Assets/debt/net-worth denominators remain distinct. Stress assumptions/exclusions are visible. No example household Bitcoin loan or integrated worst-case result is fabricated.

**Capture dependency:** Exact supported asset denominator and scenario fields. Source partial stress: BTC exposure −70%, selected stocks −30%, home −20%; education/health unchanged; vehicle/business values omitted while debts included. Preserve partial scope; no fixed-debt collateral threshold demonstration in this chapter.

#### Chapter 3 — Choose and save affordable debt actions · after 3.1

**Show:** In Plan → Scenarios, compare extra card payments against the same current inputs and Reserve claim. Inspect payoff/interest and Cash Flow effect. Use Debt detail’s approved save path only after choosing the action, then read it back. Contrast the low fixed mortgage and review the other debts without fabricating finalized choices.

**Narration:**

We're continuing the reduced-spending test. Your actual surplus stays unchanged until the spending changes happen. Here we're comparing the card with $500 going to the Reserve and $1,200 of extra card principal. The required $405 was already counted, so the total card payment is $1,605.

Let's read the payoff date and interest under that comparison, then see whether required payments and the Reserve still fit. With the mortgage, we're weighing interest avoided against cash becoming home equity. Extra principal may shorten the term without reducing next month's payment, and property costs continue after payoff.

Once you've chosen an affordable action, we'll save it in Debt and reopen it to check the terms. Changing the lender payment is a separate outside step. The saved choice is what we carry back into Cash Flow, so it only uses the money once.

**Overlay:** Reduced example: $405 required + $1,200 extra = $1,605 card total

**Verify:** Comparison does not silently change Current; selected save is counted once in Debt and Cash Flow. Mortgage escrow/property costs remain correctly funded. Each other debt has a choice or precise unresolved term.

**Capture dependency:** Approved future Scenario-to-owner decision flow, extra-payment capacity semantics, debt strategy save/preview behavior, payoff calculation and save/reload. Preserve separate source $500 Reserve and $1,200 extra. No predetermined app payoff date or automatic lender payment.

#### Chapter 4 — Compare one financing purpose through its exit · only for a proposal after 3.4 and relevant A3.2 sections

**Show:** Use Plan → Scenarios for one hypothetical $30,000 project at the reviewed date. Compare cash, a supported taxable sale and one eligible financing arrangement, plus smaller/delay. Read cash retained, payments, fees, collateral and ending principal. Use a separate graphic for $20,000/8%/60-month amortizing-versus-interest-only arithmetic.

**Narration:**

Use this take if you're comparing financing. Otherwise, continue to the repayment rules for your existing debts. We'll use the same purchase amount and date in each version. Paying $30,000 from the $32,000 Reserve leaves $2,000 for that job. A taxable sale needs enough proceeds after its actual tax cost. Financing keeps cash initially, but the payment has to fit beside the Reserve and card.

The final balance is part of that comparison. In our separate $20,000 example, about $406 a month pays the loan down over five years; about $133 interest-only leaves the $20,000 owed. A refinance needs the full replacement mortgage priced, while unusual terms need their actual settlement formula, guarantees and use restrictions.

We'll keep any contract term the app doesn't represent beside the comparison and resolve it before choosing. A smaller or delayed project may be the affordable answer. Whichever direction you choose, the payment and principal exit go into the debt rules next.

**Overlay:** Same need/date → cash left → payment → final balance → repayment source

**Verify:** Equal need and dates, actual source tax, complete repayment shape and constraints. Proposal remains separate; no application or approval. Unsupported settlement terms prevent a model-complete conclusion.

**Capture dependency:** Reviewed fictional offer/date, taxes/basis, permitted uses and guarantee terms; approved Scenario expressiveness. Generic arithmetic: $405.5279 amortizing, $4,331.6735 total interest; $133.3333 interest-only, $8,000 interest plus principal. HEI/shared appreciation requires its actual formula; do not approximate it as an ordinary loan.

#### Chapter 5 — Size and operate a Bitcoin-backed loan · only after A3.1 when Bitcoin collateral applies

**Show:** Conditional A3.1 capture only. Use the existing debt instructions/worksheet alongside Debt for an actual Bitcoin-backed loan or Plan → Scenarios for a proposal. Use a separate generic $50,000/3.5 BTC sizing graphic and authorized non-broadcast procedure diagram. Keep 50%/25% fixed-debt decline-to-threshold graphics here when explaining initial collateral; do not create an example household Bitcoin loan or initiate a real top-up. Ordinary debt instructions are in chapter 6.

**Narration:**

This take is for a Bitcoin-backed loan after you've completed its situation lesson. If that doesn't apply, go to chapter six. We'll use the actual contract and a separate sizing example here, with wallet secrets kept out of the record. We start with the full obligation before deciding how much collateral to post. This example dedicates 3.5 BTC to $50,000 of debt when Bitcoin is $100,000. After an 80% decline, those coins are worth $70,000. If posted in time, that's about 71.4% LTV. At the assumed 80% liquidation line, 3.125 BTC only reaches the boundary. The 3.5 BTC provides some room, but any stricter call-cure or maturity term still has to be met.

The $50,000 opening amount assumes separately funded interest and fees. One hypothetical year of 12% capitalized interest makes it $56,000, exactly 80% of the stressed $70,000. So if costs accrue, the initial principal needs reducing or more Bitcoin needs dedicating before borrowing.

After sizing the debt, posting 1 BTC starts it at 50% LTV and leaves 2.5 BTC reserved in cold storage. Posting all 3.5 starts the same loan at about 14.3%. The smaller initial deposit reduces lender exposure but needs a faster response. With fixed debt and our assumed 80% liquidation line, the 50% starting position reaches it after a 37.5% price fall. Posting enough for 25% initially allows a 68.75% decline to the same line; that comparison shows more upfront collateral, not a preferred starting level. Reserved coins only count for lender LTV after they arrive and are credited. That's why the top-up trigger, amount, access time and maximum collateral exposure belong here. An automatic feature can't reach into your cold wallet; the actual funding and confirmation requirements still apply.

Repeat borrowing uses the same supporting resources too. In the recurring illustration, $25,000 becomes $28,000 after 12% interest. The next $25,000 draw makes $53,000, and another 12% makes $59,360. We can't reuse the same spare collateral for each draw. If the payment, timed response or final repayment still lacks a resource, the proposal stays unchosen. Once the rules are supported, we can carry the chosen obligation back into the household cash flow.

**Overlay:** Debt first → collateral placement second · Posted BTC and dedicated BTC have different jobs

**Verify:** The Bitcoin loan's exit and unavailable-operator fallback are usable. Conditional worksheet preserves costs, exact boundary, stricter cure, timely crediting and combined repeated debt. No double-used BTC, automated cold-wallet claim or signed/executed loan.

**Capture dependency:** Actual contract, advanced modeled terms, saved liquidation selection, cost-accrual rule, source identity and approved scenario receipt. D63 parity/fix-first gates remain app implementation work. Any provider procedure requires safe independently authorized capture with no broadcasting, credentials or secret exposure; illustration is not proof a lender accepts the arrangement.

#### Chapter 6 — Carry one debt decision into Cash Flow and Allocation · after 3.6

**Show:** Return to Cash Flow → Debt payments and Saving and investing. Read the saved extra claim from Debt without entering it twice. Record ordinary debt payment source, principal exit, relevant dates, fallback and responsible/backup person in the instructions worksheet beside the debt record. Read the reduced-state assigned amount without replaying the gross-to-net bridge, then show the distinctly future payoff condition and hand current/future claims to W04.

**Narration:**

Let's record the ordinary repayment instructions for each debt you carry or choose. If no debt applies, continue to Allocation with your available cash.

For this obligation, we're naming what pays the regular bill and what repays principal. If a sale is the exit, record the amount, date and response to smaller or late proceeds. If refinancing is planned, include what you'd do if approval isn't available.

Now put any payment-change, review and maturity dates with the person responsible. A trusted backup needs to recognize a time-sensitive problem and find the safe instructions if you're unavailable. Keep secrets out of this record. Collateral borrowers bring in the funded response already worked through in their contract lesson.

Once the choice is saved, let's read it back in Cash Flow. The reduced-spending illustration assigns its $1,700 to $500 Reserve and $1,200 extra card; there's no additional investing amount in that split. Required payments and existing saving were already included.

When the card is actually paid off, verify the payments that ended and any remaining charge. If the $405 required and $1,200 extra were still being paid, that releases $1,605. That future money needs a new decision; it doesn't automatically become an investment transfer today.

We'll take the chosen commitments and that future review condition into Allocation. Then we can choose where contributions go using the money actually available.

**Overlay:** Today: $1,700 assigned once · After payoff: verify the released $1,605 before routing

**Verify:** Debt and Cash Flow read one saved state. Required payments, Reserve and payroll saving are not duplicated. Future payoff money does not appear in current surplus or an automatic transfer.

**Capture dependency:** D37 payoff/removal semantics and D32 saving owner; exact source state, schedule, future start/stop and readback. Preserve W04’s existing conditional allocation illustration. No bank or lender action is implied by the planning save.

### Member checkpoint

Each debt has verified payment terms and a chosen job or a precise missing contract answer. Required payments, Reserve funding and extra debt use the monthly money once. When new financing is being considered, its comparison includes cash retained, affordable payments, ending principal and a funded repayment source; leaving the proposal unchosen is valid. Any chosen saved debt action reads back correctly, with ordinary repayment instructions in chapter 6 and lender or bank changes listed separately. With no debt or proposal, continue to Allocation. If Bitcoin collateral applies, the separate operating sheet covers full debt growth, dedicated versus posted collateral, contract triggers, timely response and the principal exit before the loan is used.

### Source and continuity notes — not spoken

The paired teaching scripts retain their deck/source IDs and dated research boundaries. Original dictation, accepted Reserve reference and prior manuscripts remain preserved; this stepwise rewrite follows Austin’s September 10 authorization. It changes no household fixture, financial model, provider state, learner account or real-world financial instruction. Build-dependent proof, final voice review and any qualified review remain separate.
