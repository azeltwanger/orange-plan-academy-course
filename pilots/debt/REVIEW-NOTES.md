# Debt video pilot — editorial and recording notes

**September 10, 2026. Owner review, not approval.**

## What to read

[DEBT-VIDEO.md](DEBT-VIDEO.md) is the single video script. It has six chapter headings, not six recordings. The Bitcoin-backed-loan segment is an optional chapter within the same video. There is one introduction and one closing application sequence.

The active course remains untouched while Austin reviews this pilot. This file is a candidate replacement for the three current debt recordings (08/3.1, 09/3.4 and 10/3.6) and incorporates the core collateral-sizing teaching from A3.1. It does not silently delete the existing unusual-financing or repeat-borrowing detail. After pilot approval, reconcile the active recording map and retained conditional material deliberately; do not market this draft as a fully consolidated course.

## Source basis and visible editorial choices

1. **Original Debt Strategy deck:** `OrangePlan-Week4-Debt-Strategy.pptx`, 12 pages; Library file `file_00000000815881fb90257c2529627688`, read in this turn. Pages 3–10 provide current-debt review, the CFO/debt-as-tool framing, tolerance, ratio guideposts, volatility drift, structure comparison, collateral math and the final decision. Their teaching is incorporated into the narration. No deck production or slide assignment is required.
2. **Austin's debt video transcript:** `Pasted text(3).txt`, “How I Use Debt To Buy Bitcoin (Without Getting Wiped Out),” user-provided transcript. Its business framing, liquidity/spread/tax reasoning, income-stability comparison, price-cycle restraint, preference for payment flexibility and investigation order supply the spoken explanation. It is a historical source, not today's lender-rate sheet.
3. **Current first-party direction:** [owner decisions](../../reference/owner-decisions-20260910.md) plus Austin's subsequent approval in this course conversation of the six-step sequence and one chaptered video per section. Size debt from the downside first; a possible 50% initial posting is a custody/management decision. There is no 50% stressed-LTV requirement.
4. **Preserved running example:** [Reed fixture](../../fixtures/reed-household.json) and existing scripts at base `c3e08387c03e6c7236ec5ea798931ace81d4c1f5`. No live client, personal account or transaction data is included. All prices, rates and calculated schedules in the narration are teaching assumptions.
5. **Prior voice audit:** `Pasted markdown(9).md` informs conversational phrasing and concrete decision guidance only. Its superseded recommendations are not treated as owner authority. The user has since authorized substantive restructuring, so the audit's earlier “no rewrites” scope is not this pilot's instruction.

### The ratio choice is explicit, not silently reconciled

The video uses a broad 10–40% “optimal” household range for both debt-to-assets and payment-to-income. The deck instead has **debt-to-assets below 30%, 30–60%, above 60%**, and **DTI below 36%, 36–43%, above 43%**. Those are different presentations, and the sources do not establish either as a scientifically optimal Bitcoin-household borrowing level.

**This review draft uses the deck's separate bands**, because they make the two measures easier to interpret distinctly. It changes “healthy/acceptable” into “lower leverage/lower pressure/caution” and explains that these are review guideposts, not safe maximums, loan approvals, or minimum borrowing targets. The suggested starting check below the first review points is editorial application of that framework and needs Austin's spoken approval with the rest of the pilot. No claim that Austin has already ratified these exact final words is made. The historical 10–40% quote remains unchanged in its source; it is not blended into a second set of narration thresholds.

The $8,000-income household's 25% ceiling is explicitly an example of a personally chosen limit. The $400 ratio headroom / $250 cash-flow headroom comparison is a new teaching illustration, not a fact about the Reeds. It demonstrates how the tighter constraint controls the decision.

### What changed from historical wording

| Historical wording or number | Treatment in this pilot |
|---|---|
| Businesses “do the opposite” of paying off debt; 30–60% is typical business leverage | Preserve the CFO questions as an analogy; do not assert a universal corporate leverage rule. |
| Expected 18% project return vs 5% loan | Preserve the arithmetic and explicitly keep the 18% as an expectation, not proof the project is worth funding. |
| 10–40% “optimal” for two household ratios | Source difference disclosed above; deck bands selected for owner review, with limited meaning. |
| Borrowing “avoids the capital-gains hit” / a percentage applied to the whole sale | Explain postponement of a gain realization and compare tax on the actual gain, financing costs and repayment. No current tax bracket is asserted. |
| Lower debt can itself cause financial distress | Explain the specific liquidity problem from using accessible money to prepay the home; do not claim being debt-free is inherently dangerous. |
| Interest-only “beats” amortizing | Keep Austin's preference for flexibility when principal repayment is planned, then compare the ending balance and interest cost. |
| Unsecured means nobody can force a sale | Distinguish no price-based collateral call from default/collection/legal consequences. No immunity claim. |
| $50,000 at 7% interest-only costs $209 monthly in the transcript | Do not copy the incorrect number. Use the already-checked $20,000/8%/five-year comparison from the course. $50,000 × 7% / 12 would be $291.67. |
| Bitcoin loans always have no monthly payments / quoted 10–11% or 11.49% rates | No universal payment structure or current rate claim. Follow the actual agreement. |
| 10–20% default posted LTV | Preserve as a historical quote; current downside-first sizing and possible 50% initial posting replace it in the narration. |
| 37% or 69% drop to a “margin call” | Use 37.5% to the assumed 80% liquidation line from 50% starting LTV, not a generic warning or cure level. |
| Repeated warnings and qualifications | State the relevant limit at the decision it changes; omit repeated descriptions of the same stress-test omissions. |
| Homework / extra slides / each step as a separate video | None. Six chapters in a course video; members apply the teaching inside Orange Plan. |

## The cure and interest hole is closed in the narration

The original $50,000 / 3.5 BTC case now explicitly assumes **80% liquidation-only terms with no stricter cure/maturity limit and separately funded interest/fees** before its result is presented. It is not said to fit all lenders.

The same spoken segment then changes the assumed contract and resizes the example:

| Case at $20,000/BTC | Calculation | Result |
|---|---|---:|
| $50,000 at an 80% liquidation boundary | 50,000 / 0.80 / 20,000 | 3.125 BTC exactly at the boundary |
| $50,000 at a 65% cure requirement | 50,000 / 0.65 / 20,000 | 3.846154 BTC, spoken as about 3.85 |
| $56,000 after the hypothetical interest, at 65% | 56,000 / 0.65 / 20,000 | 4.307692 BTC, spoken as about 4.31 |
| Capacity of 3.5 BTC at 65% | 3.5 × 20,000 × 0.65 | $45,500 outstanding |
| Opening boundary allowing 12% added once at year-end | 45,500 / 1.12 | $40,625 |
| Deliberately smaller illustrative loan | 35,000 × 1.12 | $39,200 outstanding |
| Resized loan under the price stress | 39,200 / 70,000 | 56% LTV |
| Initial deposit for $35,000 at 50% | 35,000 / 0.50 / 100,000 | 0.7 BTC posted, 2.8 BTC reserved |
| Alternative: post all 3.5 BTC initially | 35,000 / 350,000 | 10% posted LTV |

These are *hypothetical contract comparisons*. An 80% liquidation line plus a 65% cure is not attributed to a particular lender. Equality at a liquidation boundary is not safety; equality at the example's “65% or below” cure is mathematical compliance at that moment, not operating cushion. Interest is deliberately added once at year-end to make the example auditable; real accrual/compounding, fees, prices, deadlines and repayment rules must replace the assumptions. The 56% stressed result is a consequence of the chosen $35,000 balance, not a prescribed stressed target.

The supported-BTC reserve is dedicated to this one loan, must be eligible and accessible, and counts in lender LTV only when credited. Timing, counterparty risk, cash flow, maturity, refinancing and repeated borrowing remain distinct checks. No 80% maximum drawdown or guaranteed liquidation avoidance is asserted.

## Primary-source verification — September 10, 2026

These checks supplement, rather than overwrite, the supplied source material. They are technical fact checks, not professional approval or an actuarial validation of debt bands.

- **DTI definition:** CFPB, “What is a debt-to-income ratio?” Required payments divided by gross monthly income; lender/product limits vary. https://www.consumerfinance.gov/ask-cfpb/what-is-a-debt-to-income-ratio-en-1791/
- **Lender-vs-household distinction:** Fannie Mae B3-6-02. Qualifying obligations include housing costs; manual and automated underwriting use different limits. This does not validate 43% as a universal threshold. https://selling-guide.fanniemae.com/sel/b3-6-02/debt-income-ratios
- **HELOC mechanics:** CFPB, “What is a home equity line of credit?” Collateral, draw/repayment periods, variable rates, fees and possible freezes need review. https://www.consumerfinance.gov/ask-cfpb/what-is-a-home-equity-line-of-credit-heloc-en-107/
- **Securities-backed lines:** FINRA, “Securities-Backed Lines of Credit Explained.” Non-purpose restrictions, collateral calls, possible sales and demand-loan risk. https://www.finra.org/investors/insights/securities-backed-lines-credit
- **Gain calculation:** IRS Topic 409. Tax depends on gain and basis, not an automatic rate on every dollar of proceeds. https://www.irs.gov/taxtopics/tc409
- **Cure can precede liquidation:** Strike's current non-volatility-proof lending FAQ describes a 70% call requiring 65% or below within 72 hours, separate from 85% immediate liquidation. Used to verify the distinction only; these current product settings are not substituted for the generic manuscript's assumed contract. https://strike.me/faq/how-do-ltv-margin-calls-and-liquidations-work/
- **Credit timing and 80% equality:** Ledn says deposits require blockchain confirmation before LTV changes and that 80% or above triggers automatic liquidation. https://help.ledn.io/hc/en-us/articles/28302717485079-What-Happens-If-the-value-of-your-collateral-significantly-decreases
- **Automatic top-up reserve location:** Ledn's feature uses its BTC Transaction Account, not an external cold wallet. Its live settings are not narrated as universal. https://help.ledn.io/hc/en-us/articles/28299695292439-What-is-Auto-Top-Up-and-How-Does-It-Work

No insurance-threshold research is claimed complete by this debt pilot. No upstream Claude project setting has been edited. No Alfred role is introduced.

## Filming and application: one video, separately recordable takes

The teaching before the screen share is fully written and can be judged without opening Orange Plan. The final chapter moves from a decision for the fictional household into proposed app narration. The application is part of this one video, not an added assignment or a second required lecture.

The screen-share segment is **not yet screen-verified**. The [existing W03 working session](../../scripts/working/W03_set-debt-jobs-and-test-one-financing-decision.md) itself requires verification of the redesigned screens. Avoid inventing controls, pretending model outputs have been produced, or reading references to unfinished UI aloud. Record the camera and screen portions separately; edit them together with chapter markers. Text/math graphics may be added afterward, without commissioning a slide deck.

### Capture sequence to verify, not extra spoken lessons

| Passage / task | Required visual evidence before capture |
|---|---|
| Current debts and income | Actual existing-record review flow, account ownership, balances and terms; no duplicate records. Identify any missing contract information without inventing it. |
| Household ratios | Reconcile the app's asset and payment denominators with the fixture. Use a clearly labeled calculation graphic if a ratio is not displayed. Do not imply the app supplies the draft bands or an automatic “healthy” verdict. |
| Original vs reduced spending | Show the actual comparison mechanism. The original $500 and reduced-spending $1,700 are different scenarios, not simultaneous cash sources. |
| Extra card payment | Verify whether the input is *extra* ($1,200) or *total* ($1,605), its frequency and start date. The spoken script states the distinction without claiming a particular field exists. |
| Reserve funding | Preserve $500 of that same $1,700 for the reserve. Required debt payments and the employee contribution were already counted. |
| Payoff schedule and cost | Capture actual output only after exact APR, payment schedule, fees and other required inputs are verified. The 51-/10-month payoff example is a separate amortization illustration, not an engine receipt. |
| Whole-plan effect | Read only the outcome the verified app actually returns. Do not promise an earlier retirement date, saved taxes or restored confidence. |
| Proposed borrowing and downside | Use an actual supported comparison flow; otherwise show the arithmetic as a separate clearly labeled graphic. Do not imply that the app monitors a lender or models every cure, default and maturity term. |
| Saved decision and outside action | Verify actual save behavior. Planning does not change lender autopay or bank transfers. |
| Maintenance | Demonstrate only available reminder/review features; lender alerts and time-sensitive collateral management are external unless genuinely integrated and verified. |

## What Austin is reviewing now

Does this single video teach the decision in a sequence you would use? Are the source-based guideposts and conditional preferences the ones you want to teach? Does the example reach a clear action instead of stopping at a calculation? Does the narration sound natural out loud?

The rest of the course is intentionally unchanged pending that review. This pilot is not evidence that the other sections have been rewritten.
