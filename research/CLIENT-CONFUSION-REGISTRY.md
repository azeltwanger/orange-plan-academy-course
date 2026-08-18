# Client confusion registry

**Status:** active curriculum input  
**Private source:** six unique client calls, approximately 10.2 hours  
**Rule:** use the confusion, not the client's identity or private facts

This file records the questions real clients asked while Austin taught the plan. It is not a list of every feature in Orange Plan. It is the list of places where a user could see a number or control and still not understand what it means, where it came from, or what to do next.

## How to use this registry

For each item:

1. The concept lesson teaches the decision and the mechanism.
2. The walkthrough shows the exact current app behavior on the demo household.
3. The first important output gets the four-part provenance block:
   - **WHAT IT MEANS**
   - **CALCULATED FROM**
   - **EDIT SOURCE**
   - **THIS AFFECTS**
4. The module checkpoint tests the decision, not whether the learner watched the video.

## Priority 1 — Foundation and confidence

### C-01 · What is the retirement-spending number?

**Observed confusion**

A client thought the retirement-spending input might be pre-tax income, an amount of cash arriving after retirement, or a number tied to current household income. Once Austin clarified that it was the household's living-spending need, separate from debt payments, the client realized the amount entered was too high.

**Why the confusion happens**

- The number sits near retirement timing and confidence, so it can look like an output rather than an input.
- People anchor it to current income instead of what life actually costs.
- Debt payments are modeled separately and can drop off over time.

**Course answer**

> Baseline spending is the annual living-spending need the plan is being asked to fund. It excludes debt payments that already have their own rows. The app keeps them separate so a mortgage or other debt can disappear from future cash flow when it is paid off.

**Insert into**

- Module 1 lesson on confidence and retirement inputs
- Module 1 baseline walkthrough
- Module 2 spending lesson
- Module 6 retirement-spending confirmation

**Demo proof**

Show the same household first with a mistakenly income-anchored spending number, then correct it to actual living spending. Point to the mortgage row separately and show that it ends on its payoff date.

---

### C-02 · Why are living expenses and debt payments separate?

**Observed confusion**

Clients repeatedly needed Austin to explain why the spending total did not include the mortgage or why the displayed monthly spending looked lower than their all-in outflow.

**Course answer**

> Living spending continues until the plan says it changes. Debt payments follow the terms of the debt and stop when the debt is paid. Combining them would make the plan fund a mortgage forever.

**Insert into**

- Module 1 baseline walkthrough
- Module 2 surplus lesson
- Module 3 debt walkthrough

**Number provenance**

- **WHAT IT MEANS:** recurring living costs outside debt payments
- **CALCULATED FROM:** the saved living-spending input or calibrated spending data
- **EDIT SOURCE:** Cash Flow / Plan spending source
- **THIS AFFECTS:** surplus, reserve sizing, retirement spending, earliest date, confidence

---

### C-03 · What confidence percentage is “good enough”?

**Observed confusion**

A client directly asked whether 75% was enough and whether there was a standard number. Austin naturally answered that 80% and above was a strong starting point, that 70% could still be workable with adjustments, and that lower results call for reviewing spending, saving, timing, or allocation.

**Course answer**

> Orange Plan starts at an 80% target. That is a planning starting point, not a universal pass line. A higher target generally costs time or spending. A lower target accepts a greater chance that the plan needs to adjust later.

**Insert into**

- Module 1 confidence lesson
- Module 1 walkthrough
- Module 6 guardrails lesson, with a clear distinction between Plan confidence and annual spending guardrails

**Do not teach**

- Confidence as a school grade
- 80% as a literal probability of personal success or bankruptcy
- 100% as automatically better

---

### C-04 · Does 80% confidence mean a 20% chance of going broke?

**Observed confusion**

Austin repeatedly had to say that the result is not a literal chance of bankruptcy. His practical explanation was that the unsuccessful runs are the runs where the plan, unchanged, would need an adjustment.

**Course answer**

> The percentage is the share of test runs where the saved plan lasted through the planning age without changing the plan. A lower result means more runs needed some change. It does not tell you that you have a matching probability of ending with nothing.

**Accuracy note**

Do not promise that one small adjustment rescues every unsuccessful run. The app only reports what happened under the saved inputs and policy.

**Insert into**

- Module 1 confidence lesson
- Module 1 walkthrough, immediately after the ring appears
- Module 6 annual-review lesson

---

### C-05 · Why are two retirement ages or dates visible?

**Observed confusion**

A client saw one retirement age in the input and another result in the hero and asked whether the earlier number meant the plan could begin immediately even though the entered age was later.

**Current mental model**

- **Planned retirement age:** the age the user chose to test
- **Confidence result:** how the plan performed at that planned age
- **Earliest date at target:** the first date that reaches the user's selected confidence target

**Course answer**

> The planned age is your input. The confidence result evaluates that input. The earliest date is a separate answer the app finds using your target. Changing the target can change the earliest date without silently changing the age you entered.

**Insert into**

- Module 1 confidence lesson
- Module 1 walkthrough
- Foundation slides replacing the retired three-scenario / working-freedom-date sequence

**Demo proof**

Set planned age 55 and target 80%. Show a result below target at 55 and an earliest target-qualified date later than 55. Then change only the target and show the earliest date move.

---

### C-06 · Where did the confidence result come from?

**Observed confusion**

Clients tended to read the ring as an isolated software score. Austin's strongest live explanation traced it back to the inputs—especially the Bitcoin return assumption when Bitcoin represented most of the plan.

**Course answer**

> Confidence is not typed in. It is calculated from the entire saved plan: balances, spending, income, debts, life events, tax rules, assumptions, retirement timing, and saved strategies. The biggest driver depends on the household.

**Insert into**

- Module 1 confidence lesson
- Every walkthrough that materially changes confidence

**Walkthrough rule**

When confidence changes, name the input that changed and why it affected the result. Do not say only “the plan improved.”

---

### C-07 · Which return assumption applies to a Bitcoin ETF or unusual holding?

**Observed confusion**

A client's FBTC holding was being treated as stock exposure. The fix was to apply the Bitcoin return assumptions to that holding. Another client needed to separate spot Bitcoin and Bitcoin ETFs from treasury companies and individual stocks.

**Course answer**

> Broad Plan assumptions are defaults by asset class. A specific holding gets an advanced override only when it would otherwise be modeled incorrectly. Spot Bitcoin ETFs should follow the Plan's Bitcoin assumptions. A treasury company, preferred security, rental property, concentrated stock, or income-producing holding may need its own return or yield assumption.

**Insert into**

- Module 1 assumptions lesson
- Module 1 walkthrough
- Advanced assumptions reference

**App route**

Dashboard → holding → Edit → Advanced settings → Projection overrides

**Completion rule**

Every holding either deliberately uses the broad Plan assumption or has a deliberate override. The existence of an advanced control is not a reason to customize every position.

---

### C-08 · Is an assumption a prediction, and how often should it change?

**Observed confusion**

Clients wanted to know whether assumptions should be updated as a model “holds or breaks,” and whether using a conservative model meant abandoning their Bitcoin conviction.

**Course answer**

> An assumption is the starting rule for the saved plan. It is not a promise about the future. Use a base assumption you can defend, test weaker and stronger versions in Scenarios, and update the saved assumption when your actual planning view changes—not every time price moves.

**Insert into**

- Module 1 assumptions lesson
- Module 9 maintenance lesson

**Keep from the slides**

The Foundation deck's “living model” idea is useful. Replace the retired three-scenario workflow, but keep the principle that the plan stays useful by staying current.

---

### C-09 · Is this a baseline fact, expected life event, or scenario?

**Observed confusion**

Clients mixed desired retirement spending, possible gifts, healthcare, college, and speculative changes together. Austin's live process was to ask whether the event was actually expected and whether it materially changed income, expenses, or assets.

**Course answer**

- Baseline = true today
- Life event = expected change the saved plan should include
- Scenario = a question to test without changing the saved plan

**Insert into**

- Module 1 assumptions lesson
- Module 1 walkthrough
- Module 9 scenarios lesson

**Decision question**

> Would you be surprised if this never happened? If yes, it probably belongs in the plan. If no, it probably belongs in Scenarios.

---

## Priority 2 — Cash Flow and Reserve

### C-10 · Why does cash flow look negative when income is strong?

**Observed confusion**

A large negative result was traced to an incorrect income entry. The client read the output first and assumed the plan itself was broken.

**Course answer**

> Surplus is an output. Do not edit it. Open income, taxes, living spending, and debt payments until the rows match reality.

**Insert into**

- Module 2 surplus lesson
- Cash Flow walkthrough

---

### C-11 · Which spending number should drive the plan?

**Observed confusion**

Clients had unusual travel, family support, gifts, and one-time years mixed into the average. They were unsure whether to use the highest year, a rough average, or a lower “normal” number.

**Course answer**

> Separate normal recurring spending, bare-bones spending, and known irregular costs. Do not bury a known future cost inside a permanently inflated baseline.

**Insert into**

- Module 2 spending lesson
- Cash Flow walkthrough
- Module 6 retirement-spending confirmation

---

### C-12 · How does the reserve change between working and retirement?

**Observed confusion**

Clients understood an emergency fund while working but needed help seeing why a retirement reserve is based on the spending gap after reliable income rather than the old paycheck-replacement job.

**Course answer**

> While working, the reserve protects against lost income and unexpected costs. In retirement, it protects the portfolio from forced sales by covering the gap between spending and reliable income.

**Insert into**

- Module 2 reserve lesson
- Module 6 reserve-refill lesson

---

## Priority 3 — Debt, Allocation, and Tax

### C-13 · Is debt automatically bad, or is the goal zero?

**Observed confusion**

Clients needed the trade-off separated into rate, cash-flow pressure, collateral risk, taxes, and personal comfort. Austin did not force a leverage-maximizing answer when a client preferred being debt-free.

**Course answer**

> The app can show the cost and pressure. The student still decides whether the flexibility or expected spread is worth carrying the debt. A debt strategy the household will abandon in a drawdown is not useful.

**Insert into**

- Module 3 concept lesson
- Debt walkthrough

---

### C-14 · What is the difference between target allocation, account holdings, and today's action?

**Observed confusion**

Clients blurred the desired portfolio mix, what each account should hold, and what to buy, sell, or contribute right now.

**Course answer**

1. Target allocation = where the household wants the portfolio to land
2. Account holdings = what belongs inside each wrapper
3. Current action = contribution routing, a one-time shift, or no change

**Insert into**

- Module 4 concept lessons
- Allocation walkthrough

---

### C-15 · How do taxes flow from a sale or conversion into the rest of the plan?

**Observed confusion**

Clients needed tax outputs connected to basis, account type, state, timing, and the amount actually sold or converted.

**Course answer**

> A tax number is calculated from a transaction or planned strategy. The learner should be able to open the underlying lot, sale, conversion, or tax setting and explain the result before acting.

**Insert into**

- Module 5
- Tax walkthrough
- Module 6 when sales fund retirement

---

## Priority 4 — Custody and Estate

### C-16 · What does “single point of failure” actually mean?

**Observed confusion**

A client stopped on the phrase “look for the only one” and asked what it meant. The abstract wording was not self-explanatory.

**Course answer**

> A single point of failure is one device, backup, location, login, person, or document whose loss or compromise can block recovery or expose the funds. Name the specific “only one,” then add a backup, another location, or another person in the process.

**Insert into**

- Module 7 custody lesson and slide copy

---

### C-17 · What is collaborative custody, and who can move the money?

**Observed confusion**

Clients repeatedly needed the key threshold and recovery path explained. “Multisig,” “collaborative,” and “provider holds a key” were not enough by themselves.

**Course answer**

> In a 2-of-3 setup, two valid keys are required. The provider holding one key cannot move funds alone. The exact ownership and inheritance design must be stated correctly for the specific setup; do not mix a four-key diagram into a 2-of-3 example.

**Insert into**

- Module 7 custody lesson
- Module 8 estate handoff
- Corrected slides

---

### C-18 · What belongs in the custody map or heir letter?

**Observed confusion**

Clients understood that family needed instructions but could easily turn the document into a treasure map.

**Course answer**

> Document the process, contacts, providers, locations at a safe level, and what not to do. Never include seed words, private keys, PINs, passwords, or a complete recovery path in one document.

**Insert into**

- Module 7 and 8
- Protect walkthrough

---

## Cross-course production rules created by these calls

1. **Every important number is introduced as either an input or an output.**
2. **Every output is traced to its source before a recommendation is made.**
3. **One input changes at a time in the demo household.**
4. **The learner is asked whether the result matches real life.**
5. **Austin's judgment is labeled as judgment.**
6. **A technical or current fact that is not verified is not upgraded into certainty.**
7. **The walkthrough ends by returning to Build Your Plan and showing the next step.**
8. **The app checkmark and the human planning decision are both stated.**

## Immediate Module 1 insertion map

| Confusion | Lesson | Walkthrough beat | Slide change |
|---|---|---|---|
| C-01 / C-02 | 1.3, with setup in 1.1 | Explain baseline spending and separate debt rows | Replace income-anchored “working freedom date” framing |
| C-03 / C-04 | 1.3 | Run test; define target and result | New confidence-target visual |
| C-05 | 1.3 | Planned age vs earliest date at target | Replace three-scenario date selection |
| C-06 | 1.3 | Show provenance block for confidence | Add “where this number came from” visual |
| C-07 | 1.2 | Review holdings; add override only when applicable | Add broad assumption vs holding override note |
| C-08 | 1.2 | Set base; use Scenario for alternate view | Keep living-model slide, remove retired scenario workflow |
| C-09 | 1.2 | Add one expected event and one scenario question | Clarify baseline / life event / scenario |
