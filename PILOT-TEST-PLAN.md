# Orange Plan Academy — learner comprehension pilot

**Purpose:** test whether the repaired course creates understanding and plan completion before all 28 lessons are filmed.

This is not a satisfaction survey. The pilot measures whether a learner can make the intended decision, explain the important number, find its source, and complete the matching app work without Austin rescuing them.

## Pilot scope

Run the first pilot on the highest-risk sequence:

1. Module 0 framing and AI safety
2. Module 1 Baseline and Confidence
3. Module 2 Cash Flow and Reserve
4. Module 4 Allocation and the Next Dollar
5. Module 6 Retirement Income
6. Module 9 Scenario and final-plan read

These lessons contain the largest product changes and the most easily confused numbers.

Use rough concept-video cuts or live teaching from the current scripts plus the verified synthetic walkthrough. The pilot does not require final animation, lighting, music, or course-platform production.

## Participants

Recruit 6–9 people across three perspectives:

- 2–3 Bitcoin holders newer to financial planning
- 2–3 people comfortable with financial planning but unfamiliar with Orange Plan
- 2–3 spouses or family members who are not the household's primary money person

At least two participants should have never seen the prior Academy or live-client decks.

Do not use only existing clients who already know Austin's terminology. Familiarity can hide a course problem.

## Test environment

- Use a clean synthetic Orange Plan account based on `demo-v1-inputs`.
- Record the deployed app commit and walkthrough metadata.
- Give the participant the same lesson text and app access a paying learner receives.
- Do not include the answer in the task wording.
- Ask the participant to think aloud.
- Record screen, voice, elapsed time, and exact confusion point with consent.
- Never use a real wallet, account credential, client data, or Bitcoin secret.

## Core task loop

After each concept lesson, ask the participant to complete five actions without coaching:

1. State the decision in one sentence.
2. Identify the number or source input needed for it.
3. Predict which app result should change.
4. Complete the matching app work.
5. Explain the result and whether the decision still fits.

The observer may resolve a genuine technical failure. Do not explain the planning concept until the participant finishes the attempt; otherwise the test measures the observer rather than the course.

---

# Module-specific tests

## Start Here and AI

Ask:

- What does Orange Plan calculate?
- What does the AI do?
- Who makes the final decision?
- What must never be entered into an app, document, screenshot, or AI tool?
- Does an app checkmark prove the human decision or real-world action is complete?

**Pass:** participant separates engine, explanation, and decision and states the no-secrets rule without prompting.

## Baseline and assumptions

Give five items and ask the participant to sort them into Baseline, life event, or Scenario:

- current salary,
- vehicle replacement expected in 5 years,
- possible move,
- current Bitcoin holding,
- earlier-retirement question.

Then ask:

- Which source number is verified, estimated, or missing?
- When is a holding-specific return/yield override appropriate?
- Does changing a Scenario alter the saved Baseline?

**Pass:** at least 4 of 5 items are sorted correctly and the participant does not customize every holding merely because the control exists.

## Confidence and household retirement date

Show the canonical result:

- household retirement date: Alex age 55,
- target: 80%,
- confidence at 55: 94.6%,
- earliest target-qualified date: May 2032 / Alex age 51.

Ask the participant to explain all four values and answer:

- Is there a second deterministic retirement result?
- Does Jordan keep W-2 income for two extra years merely because Jordan is younger?
- Why can the first retirement calendar year still contain wages?
- Does the age-51 result tell the household it must retire at 51?

**Pass:** participant identifies one household retirement date, partial-year wages, one test-run framework, and options rather than an automatic instruction.

## Cash Flow and Reserve

Show:

- $4,261 monthly capacity before extra debt,
- $500 saved extra auto principal,
- $3,761 post-debt surplus,
- $3,500 account contribution route,
- $261 operating cushion,
- $30,000 reserve based on $5,000 × 6 months.

Ask the participant to rebuild the flow and explain:

- why Debt is separate from living spending,
- why the $500 cannot be routed again,
- why the full household decision can still be called $4,000,
- and why a known future bill is not the emergency reserve.

Then show one unusually expensive month and ask whether it automatically changes normal spending.

**Pass:** participant does not duplicate debt, distinguishes the full decision from the post-debt amount, and explains reserve basis × months.

## Allocation and the next dollar

Show three denominators:

- $270,000 app allocatable portfolio → 64.8% Bitcoin,
- $295,000 financial balances including 529 → 59.3%,
- $745,000 gross assets including home → 23.5%.

Ask:

- Which denominator controls the target-allocation decision?
- Why is the 529 excluded?
- Does being above the 40–60% band force a sale?
- What happens to the $1,500 taxable Bridge route while Bitcoin is overweight?
- What is the dollar loss in a 75% Bitcoin drawdown?

**Pass:** participant names the denominator, says review rather than automatic trade, and states the $131,250 loss without confusing it with a different percentage scope.

## Retirement Income

Show the first retirement calendar-year result:

- total need $171,383,
- recurring income $69,435,
- total draw $101,948,
- cash $2,200,
- stocks $1,800,
- Bitcoin about $97,900,
- Bitcoin sale $97,948 / 0.079251 BTC at the projected 2036 price.

Ask the participant to explain why the draw is not simply $100,000 spending minus $20,000 part-time income.

They should identify:

- inflation-adjusted living spending,
- college,
- remaining debt,
- tax,
- partial-year household wages,
- and inflation-adjusted part-time income.

Then ask them to distinguish:

- Plan confidence target,
- Conservative / current / Balanced / Aggressive spending choices,
- annual spending guardrails.

Finally show:

- Conservative $99,317,
- current $100,000 at 94.6%,
- Balanced $170,216,
- Aggressive $249,904.

Ask whether the household must raise spending to $170,216.

**Pass:** participant traces need, income, draw, and sources; uses the projected Bitcoin price for units; and understands that capacity is not an instruction to maximize spending.

## Scenario and final-plan read

Show:

- 3% inflation Baseline at 94.6%,
- 4% inflation Scenario at 91.6%,
- delta −3.0 percentage points,
- target 80%.

Ask:

- What changed?
- Did the Baseline change?
- What does the result tell us?
- What does it not tell us?
- Where would a decided change be applied?

Then ask the learner to summarize the plan in six sentences using the capstone.

**Pass:** participant identifies one changed input, one measured effect, no automatic action, no invented earliest-date/estate delta, and can explain the main plan without reopening every page.

---

# Number-provenance test

For every important output, ask:

1. What does this number mean?
2. What is it calculated from?
3. Where do you edit the source?
4. What else should move when it changes?

Score each answer:

- `0` — cannot answer or gives a wrong source
- `1` — directionally understands but needs help
- `2` — explains accurately and finds the source unaided

A number passes when at least 80% of participants score 2 on meaning and source and no more than one participant gives a dangerous interpretation.

## Numbers in the first pilot

- Confidence and earliest target-qualified date
- Modeled tax and post-debt surplus
- Reserve target and months funded
- DTI and DTA
- Allocation denominator, current percentage, band, and drawdown dollars
- First-year total need, recurring income, and total draw
- Account and holding source split
- Bitcoin sale dollars, projected price, and units
- Starting-spending choices and annual policy
- Scenario delta

## Dangerous interpretations requiring a stop

One occurrence is investigated; a repeated occurrence blocks filming.

- Confidence is treated as a guarantee, grade, or literal bankruptcy probability.
- Learner describes a second deterministic retirement result.
- Learner assumes the younger spouse works longer even though the app uses one household retirement date.
- Learner duplicates debt inside living spending or routes the extra debt twice.
- Learner uses the 529 or home denominator as the app target-allocation scope.
- Learner treats an above-band allocation as an automatic sell instruction.
- Learner changes assumptions until the result becomes acceptable.
- Learner thinks `Hold Bitcoin` is a funding source without another asset or loan.
- Learner divides future Bitcoin sale dollars by today's price.
- Learner treats Balanced spending as a command to spend more.
- Learner interprets a preview as already applied.
- Learner enters a seed phrase, key, passphrase, credential, or full recovery path.
- Learner thinks an app checkmark proves recovery, legal validity, provider acceptance, insurance coverage, or family capability.

---

# Observation log

| Participant | Lesson / timestamp | What the learner tried | What they believed | Error type | Consequence | Proposed fix | Retest result |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## Error types

- `CONCEPT` — mental model is wrong
- `DECISION` — concept understood, choice unclear
- `NUMBER` — meaning, denominator, or source unclear
- `APP` — route, control, state, or save behavior unclear
- `DEMO` — example contradicts or overloads the decision
- `COPY` — wording creates the wrong interpretation
- `VISUAL` — hierarchy or comparison is unclear
- `REFERENCE` — changing detail belongs in lesson text
- `PROFESSIONAL` — learner tries to execute a gated tax/legal/custody/insurance action

## Fix the smallest layer that owns the problem

- Fix the **concept script** when the mental model is wrong.
- Fix the **demo** when the concept is clear but the example conflicts.
- Fix the **walkthrough** when the learner cannot implement the decision.
- Fix the **app copy or UX** when multiple learners make the same product-state mistake.
- Fix the **lesson text** when the missing detail is maintained reference.
- Fix the **visual** when the comparison is correct but hard to see.
- Add an **Advanced or professional gate** when Core invites unsafe implementation.

Do not rewrite the spoken lesson to compensate for a product bug or add permanent app text to compensate for a missing concept.

---

# Pilot pass thresholds

The pilot sequence clears when:

- At least 80% can state each lesson's decision without prompting.
- At least 80% can explain the important number and find its source.
- At least 80% complete the app task without an observer taking over.
- No repeated dangerous interpretation remains.
- Median concept-video runtime remains within the intended range.
- Participants distinguish an app checkmark from human and real-world completion.
- Participants leave each module with no more than one to three clear actions.
- Spouse/family participants can explain the decision even when they would choose differently.

## Pilot failure rule

Do not solve a failed pilot by adding paragraphs everywhere.

First identify whether the failure belongs to concept, demo, walkthrough, app, visual, reference, or professional gate. Remove, reorder, or clarify before expanding.

## Production decision

After the pilot:

1. Apply the smallest fix.
2. Reconcile script and lesson text.
3. Update the demo or crosswalk only when the source changed.
4. Retest the failed task with at least two fresh participants.
5. Proceed with the remaining filming only after the repaired sequence passes.

The course succeeds when a learner can explain and use the plan—not when every sentence survives the first draft.
