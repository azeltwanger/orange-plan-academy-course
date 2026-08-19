# Orange Plan Academy — learner comprehension pilot

**Purpose:** test whether the repaired course produces understanding and plan completion before the entire course is filmed.

This is not a satisfaction survey. The pilot measures whether a learner can make the intended decision, explain the important number, find its source, and complete the matching plan work without Austin rescuing them.

## Pilot scope

Run the pilot on the highest-risk sequence first:

1. Module 0 framing and AI safety
2. Module 1 Baseline and Confidence
3. Module 2 Cash Flow and Reserve
4. Module 6 Retirement Income

These lessons contain the largest app changes and establish the language used everywhere else. Do not wait until all 28 videos are filmed to learn that confidence, spending, debt payments, or total draw is still being misunderstood.

Use concept-video rough cuts or live teaching from the approved run sheet plus the current demo walkthrough. The pilot does not require final animation, lighting, music, or course-platform production.

## Participants

Recruit 6–9 people across three perspectives:

- 2–3 Bitcoin holders newer to financial planning
- 2–3 people comfortable with financial planning but not the Orange Plan app
- 2–3 spouses or family members who are not the household's primary money person

At least two participants should have never seen the existing Academy or client decks.

Do not use only highly engaged existing clients who already know Austin's terminology. Familiarity can hide a course problem.

## Test environment

- Use a clean Orange Plan account or a disposable copy of the canonical demo.
- Use the current app version recorded in the walkthrough metadata.
- Give the participant the same lesson text and app access a paying learner receives.
- Do not provide the answer in the task wording.
- Ask the participant to think aloud.
- Record screen, voice, time, and the exact point of confusion with consent.

## Core task loop

After each concept lesson, ask the participant to complete five actions without coaching:

1. State the decision in one sentence.
2. Identify the number or source input needed for the decision.
3. Predict which app result should change.
4. Complete the matching app work.
5. Explain the result and whether the decision still fits.

Austin or the observer may answer a genuine technical failure. Do not explain the financial concept until the participant has finished the attempt; otherwise the test measures the observer rather than the course.

---

# Module-specific tests

## Start Here and AI

Ask:

- What does Orange Plan calculate?
- What does the AI do?
- What information must never be entered into the app, a document, or AI?
- Does an app checkmark prove the human decision is complete?

**Pass:** participant separates engine from explanation and states the no-secrets rule without prompting.

## Baseline and assumptions

Give five items and ask the participant to sort each into Baseline, Life event, or Scenario.

Include:

- a current salary,
- a vehicle replacement expected in 5 years,
- a possible move,
- a current Bitcoin holding,
- and an earlier-retirement question.

Then ask:

- Which source number is verified, estimated, or missing?
- When is a holding-level override appropriate?
- Does changing a Scenario alter the saved Baseline?

**Pass:** at least 4 of 5 items are sorted correctly, and the participant does not customize every holding merely because the control exists.

## Confidence

Ask the participant to explain:

- planned retirement age,
- confidence target,
- confidence result,
- and earliest target-qualified date.

Then change one input and ask them to predict the direction of the result.

**Pass:** participant does not call confidence a grade, guarantee, or literal bankruptcy probability; does not describe a second deterministic result; and can identify the source input rather than editing the output.

## Cash Flow

Show the demo's income, tax, living-spending, and debt rows.

Ask the participant to rebuild surplus and explain why debt payments are separate from living spending.

Then show one unusual month and ask whether it changes the normal-spending Baseline.

**Pass:** participant does not duplicate the mortgage or other debt, and can distinguish recurring spending from a one-time event.

## Reserve

Ask the participant to choose a spending basis and target months for a short household profile.

Then ask:

- What created the target amount?
- Which cash counts?
- Why does a known future bill not belong in the emergency reserve?

**Pass:** participant can explain basis × months, exclude committed cash, and state the risk trade-off without repeating only a generic six-month rule.

## Retirement Income

Ask the participant to explain:

- retirement living spending,
- recurring income floor,
- portfolio-funded living gap,
- total draw,
- source split,
- and Bitcoin sold or retained.

Then ask them to distinguish:

- Plan confidence target,
- starting-spending comparison,
- and annual spending guardrails.

**Pass:** participant can explain why total draw may exceed living spending, and does not treat the three confidence controls as one shared setting.

---

# Number-provenance test

For every important output, ask the participant:

1. What does this number mean?
2. What is it calculated from?
3. Where do you edit the source?
4. What else should move when it changes?

Score each answer:

- `0` — cannot answer or gives a wrong source
- `1` — directionally understands but needs help
- `2` — explains accurately and finds the source unaided

A number passes the pilot when at least 80% of participants score 2 on meaning and source, and no more than one participant gives a dangerous interpretation.

## Numbers in the first pilot

- Net worth / current position
- Surplus
- Reserve target and months funded
- Plan confidence
- Earliest target-qualified date
- Retirement living-spending gap
- Total draw
- Bitcoin sold or retained
- Starting spending amount and annual policy update

## Dangerous interpretations requiring a stop

One occurrence is investigated; repeated occurrence blocks filming.

- Confidence is treated as a guarantee or grade.
- Learner thinks debt payments belong inside living spending and the debt rows.
- Learner changes assumptions until the result becomes acceptable.
- Learner thinks `Hold Bitcoin` is a funding source without another asset or loan.
- Learner interprets a preview as already applied.
- Learner enters a seed phrase, key, passphrase, credential, or full recovery path.
- Learner thinks the app checkmark proves a backup, legal document, provider record, or family recovery actually works.

---

# Observation log

Use one row for every meaningful problem.

| Participant | Lesson / timestamp | What the learner tried | What they believed | Error type | Consequence | Proposed fix | Retest result |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## Error types

- `CONCEPT` — explanation did not create the mental model
- `DECISION` — learner understood the concept but did not know what to choose
- `NUMBER` — meaning or calculation source was unclear
- `APP` — route, control, state, or save behavior was unclear
- `DEMO` — example introduced a contradiction or unnecessary complexity
- `COPY` — label or sentence caused the wrong interpretation
- `VISUAL` — slide emphasized the wrong thing or hid the hierarchy
- `REFERENCE` — learner needed changing detail that belongs in lesson text
- `PROFESSIONAL` — learner tried to execute a tax/legal/custody/insurance action that should be gated

## Fix the smallest layer that owns the problem

- Fix the **concept script** when the mental model is wrong.
- Fix the **demo** when the concept is clear but the example conflicts.
- Fix the **walkthrough** when the learner cannot implement the decision.
- Fix the **app copy or UX** when multiple learners make the same product-state mistake.
- Fix the **lesson text** when the missing detail is a maintained reference.
- Add an **Advanced gate** when Core invites unnecessary implementation complexity.

Do not rewrite the spoken lesson to compensate for a product bug or add app copy to compensate for a missing concept.

---

# Pilot pass thresholds

The pilot sequence clears when:

- At least 80% can state each lesson's decision without prompting.
- At least 80% can explain the important number and find its source.
- At least 80% complete the app task without an observer taking over.
- No repeated dangerous interpretation remains.
- Median concept-video runtime remains within the intended range.
- Participants can tell the difference between an app checkmark and human completion.
- Participants leave each module with no more than one to three clear actions.
- Spouse/family participants can explain the finished decision even when they would choose a different option.

## Pilot failure rule

Do not solve a failed pilot by adding more paragraphs everywhere.

First identify whether the failure belongs to the concept, demo, walkthrough, app, visual, or reference layer. Remove, reorder, or clarify before expanding.

## Production decision

After the pilot:

1. Apply the smallest fixes.
2. Reconcile scripts and lesson texts.
3. Update the canonical demo or crosswalk only when the source changed.
4. Retest the failed task with at least two fresh participants.
5. Proceed with filming the remaining modules only after the repaired sequence passes.

The course is successful when a learner can explain and use the plan—not when every sentence survives the first draft.