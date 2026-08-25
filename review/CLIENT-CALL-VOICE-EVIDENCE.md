# Client-call voice evidence

**Status:** source pack for the Academy voice pass  
**Private source material:** six unique client calls, approximately 10.2 hours total  
**Use:** rewrite and review teaching scripts; do not publish client details or raw transcripts

## Source set

The uploaded files contain six unique calls with two client households. A second upload of the July 9 call was byte-for-byte identical and is not counted twice.

| Source ID | Transcript | Primary planning areas |
|---|---|---|
| C1-01 | `GMT20260601-130045_Recording.transcript (1)(1).vtt` | Baseline, accounts, assumptions, life events, confidence |
| C1-02 | `GMT20260611-160002_Recording.transcript(1).vtt` | Spending, reserve, retirement spending, contributions, cost basis |
| C2-01 | `GMT20260619-130808_Recording.transcript(1).vtt` | Baseline, assumptions, life events, retirement timing |
| C2-02 | `CallRecording(1).vtt` | Cash flow, retirement spending, reserve, tax, allocation |
| C2-03 | `GMT20260709-130048_Recording.transcript (1)(3).vtt` | Custody, risk, tax, app questions |
| C2-04 | `GMT20260803-145921_Recording.transcript (1)(1).vtt` | Custody, estate, retirement income, app and AI review |

The corpus contains roughly 51,000 Austin-spoken words. It is large enough to calibrate the course without asking Austin to re-dictate every lesson from zero.

## What the calls are for

The calls are not the only voice target.

- **Dictated Lesson 2.2** remains the best reference for a prepared teaching lesson.
- **Client calls** show how Austin explains a number when someone is confused, how he qualifies a recommendation, how he works through trade-offs, and how he navigates the app.
- **Dictated portions of 0.1 and 1.1** show course framing and instruction.
- **Slides** provide the teaching sequence and worked visuals.
- **The current app** is the authority for labels, calculations, routes, and save behavior.

The final script should sound like Austin teaching on a prepared first take, not a raw transcript with every filler word preserved.

## The core explanation pattern

Across the calls, Austin repeatedly uses the same useful sequence:

1. **Start with the client's actual number or decision.**
2. **Say what is included and excluded.**
3. **Explain why the app separates or calculates it that way.**
4. **Connect the number to what changes later in the plan.**
5. **Ask whether it matches the client's real life.**
6. **Give a qualified recommendation.**
7. **Make the next change or name the next decision.**

A representative example is the explanation of living spending versus debt payments:

> Living expenses and debt payments are separate so the app can remove the mortgage payment automatically when the mortgage is paid off. The living-spending field should contain what the household needs outside debt payments.

That is the pattern the walkthroughs need: number → source → reason → downstream effect.

## Austin's natural teaching behaviors

### 1. He explains the mechanism before giving the judgment

Austin rarely gives a bare recommendation. He explains what is causing the result first.

Typical structure:

> “The reason why this is laid out this way is…”  
> “What this calculates is…”  
> “The biggest part of this is going to be…”  
> “That makes it so we can…”

**Course rule:** every recommendation should have a visible cause. If the script says what to do without explaining why the number moves, it is incomplete.

### 2. He marks judgment as judgment

Across the six calls, `I think` appears more than 250 times. It is not filler when it distinguishes a planning opinion from app mechanics or a factual rule.

Common forms:

- “I think this makes more sense for you because…”
- “I don't see a huge problem with that as long as…”
- “I think 80% is a good place to start…”
- “From a financial perspective, I think…”
- “If being debt-free matters more to you…”

**Course rule:** mechanics are stated directly. Personal planning judgments are qualified.

### 3. He invites the client's reaction

Austin does not only deliver an answer. He asks whether the number or trade-off fits the person.

Recurring forms:

- “How do you feel about that?”
- “Does that make sense?”
- “Is that something you'd want to look at?”
- “Do you feel good about the number here?”
- “What would you want to do?”

**Course rule:** a concept lesson can end with a decision question. A walkthrough should pause at the decision rather than narrating past it.

### 4. He works from the source row, not the headline

When a result looks wrong, Austin opens the underlying account, expense, debt, assumption, or life event. He does not “fix” the result itself.

Examples from the calls:

- A negative cash-flow result was traced to the wrong income input.
- A spending number was explained by separating living expenses from the mortgage.
- FBTC was corrected from stock returns to Bitcoin assumptions at the holding level.
- Confidence was traced back to Bitcoin return assumptions because Bitcoin was the largest driver of the plan.

**Course rule:** every major output gets the four-part provenance block:

- WHAT IT MEANS
- CALCULATED FROM
- EDIT SOURCE
- THIS AFFECTS

### 5. He uses real numbers and walks the change

Austin is clearest when he points to the current number, changes one input, and shows the result move.

He does not normally stack four hypothetical levers at once. He changes one thing, reruns the plan, and compares.

**Course rule:** the demo household should change one meaningful input at a time. The viewer should be able to name what caused the result to move.

### 6. He is comfortable saying what he does not know

When a current product, provider, legal, or technical fact is uncertain, Austin says so and offers to verify it.

Common forms:

- “I'll have to double-check that.”
- “I'm pretty sure, but I want to verify it.”
- “I haven't watched the full thing, so I don't have the complete context.”
- “That would be a good question to research.”

**Course rule:** never manufacture certainty to make a script sound authoritative. Flag the research point or remove the claim.

### 7. He restates when the client is still confused

Austin often explains the same mechanism a second time using different words. This is useful repetition, not filler, when it answers a live misunderstanding.

**Course rule:** preserve one restatement after a difficult concept such as confidence, cost basis, withdrawal order, or multisig. Remove repetition that merely says the same idea in adjacent lessons.

## Measured language patterns

The calls support the existing voice guide but refine it.

- `I think`: about 259 occurrences
- `we can`: about 197 occurrences
- `as far as`: about 62 occurrences
- `if you want`: about 54 occurrences
- `let's see`: about 59 occurrences
- `how do you feel`: about 12 occurrences
- `do you feel`: about 25 occurrences

The most common sentence-like openers in the calls are `So`, `And`, `Yeah`, `I`, and `But`. This is the conversational register. A prepared lesson should not inject those at the start of every sentence; Lesson 2.2 remains the guide for the cleaner teaching register.

## What not to copy from raw calls

Voice matching does not mean reproducing transcription noise.

Do not intentionally add:

- repeated filler such as “like” in every clause,
- abandoned sentence starts,
- excessive “so” and “yeah,”
- live screen-searching language when the script already knows the route,
- client-specific facts or personally identifying details,
- incorrect or superseded app behavior from the date of the call.

The target is **Austin's reasoning and cadence after a clean first edit**, not a literal VTT transcript.

## Authentic script shapes

### Explaining a number

> “This number is showing [plain-language meaning]. It is taking [inputs] and calculating [output]. If it looks wrong, the place to fix it is [source], because changing [input] is also going to move [downstream result].”

### Giving a recommendation

> “For your situation, I think [recommendation] makes sense because [reason]. On the flip side, if [different preference or risk], then [alternative] can still be reasonable.”

### Explaining a trade-off

> “If you move this higher, you're getting [benefit], but you're also accepting [cost]. If you move it lower, the trade-off goes the other way. The app can show you the numbers, but you still have to decide which side fits you.”

### Handling uncertainty

> “I don't want to state that as a fact without checking it. The planning mechanism is [what is known]. The current rule or provider detail needs to be verified before you act.”

### Closing a lesson

> “Your decision out of this lesson is [one decision]. In the walkthrough below this module, we're going to put that into the demo account and show exactly which number changes.”

## Script acceptance test

A voice-matched draft is ready for Austin review when:

- the first minute teaches rather than resells the lesson,
- every recommendation includes the reason,
- facts and Austin's judgment are distinguishable,
- the example uses the continuous demo household,
- app terminology matches current `main`,
- the script shows where the number came from,
- there is no slogan written only to sound quotable,
- the close asks for one decision,
- Austin can read it aloud without translating it back into his own words.

## Provenance label

Use:

- `AUSTIN DICTATION` — direct transcript of Austin's recorded lesson
- `VOICE-MATCHED DRAFT` — rewritten from Austin's dictation, client calls, slides, and current app; Austin review pending
- `AUSTIN APPROVED` — Austin reviewed the final wording and cleared it for filming

Do not use `SPOKEN-PROSE VERSION (calibrated)`. It obscures whether Austin actually said the words.
