# Orange Plan Academy — learner-question audit

**Status:** complete before Austin's voice review  
**Scope:** 28 Core concept lessons  
**Purpose:** ensure Austin reviews the final teaching question rather than dictating polished prose around the wrong problem

## Decision

Yes, this pass belongs **before** dictation.

Voice can improve a sentence. It should not be used to discover that the lesson answers the wrong question. The learner question, worked example, Austin judgment, decision, and finish line must be stable first.

## Course rule

Every lesson follows:

> **Real learner question → minimum concept → worked example → honest trade-off → Austin's judgment → one decision → done-when test**

The title may remain short and outcome-focused. Every title does not need to become a question, and no script needs a new generic introduction.

The opening passes when the learner understands within roughly 30 seconds why the lesson matters, which question it answers, and what decision will be made.

## Audit result

- 28 current Core lessons are mapped to a real learner question.
- 28 lessons end with a specific decision and checkable finish line.
- 27 lessons use a financial, comparative, causal, or process example.
- 0.1 is an orientation lesson and uses Austin's own planning gap rather than a financial calculation.
- No new spoken question block was added to every script; the question map is a review contract, not extra runtime.
- Two intentionally compound lessons remain acceptable because the questions are inseparable in the decision: 1.2 and 9.2.

## Questions that anchor the course

The learner is not buying topics such as Monte Carlo, asset location, or RMDs. The learner is trying to answer questions such as:

- Can I retire when I want?
- What do I actually spend?
- How much cash should I hold?
- Should I pay this debt faster?
- How much Bitcoin can I responsibly own?
- Where should the next dollar go?
- Which account should hold each asset?
- What did I pay for my Bitcoin?
- When is my tax plan most flexible?
- How will retirement actually pay me?
- Will my Bitcoin backup work?
- Can my family legally and operationally recover it?
- What could financially break the family plan?
- How do I test a decision without corrupting the real plan?

The course may teach technical concepts, but the technical concept serves the question rather than becoming the lesson's identity.

## Shorter-is-better rule

Question framing is not permission to add more words.

- Do not add “In this lesson we will answer...” to every script.
- Do not repeat the title, question, and outcome in three forms.
- Do not turn the first minute into a motivational introduction.
- State the problem, move into the example, and let the example teach the concept.
- Keep changing product instructions in the walkthrough or lesson text when they are not necessary to understand the decision.

## Relationship to the worked-example audit

`research/CORE-WORKED-EXAMPLE-AUDIT.md` answers: **Did the lesson work the concept?**

This audit answers: **Was it the concept the learner actually needed to solve?**

Both must pass before Austin approves the spoken lesson.

## Permanent source

The machine-readable contract is `curriculum/core-learner-questions.json`.

The review-facing version is `review/LEARNER-QUESTION-MAP.md`.

The automated check is `tools/learner_question_audit.py`.
