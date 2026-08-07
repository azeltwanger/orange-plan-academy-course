# FAQ and AI-knowledge backlog

Built from the recurring questions in 24 client calls across six journeys.

**The rule this file exists to enforce:** a question that came up repeatedly is
not automatically a reason to add a video. Most of these are better answered by
the app, a tooltip, the AI, or an FAQ entry — and answering them in a recorded
lesson makes the lesson longer *and* wrong sooner.

| Where the answer belongs | Why |
|---|---|
| **In-app provenance** | "Where did this number come from?" is a UI question. Prose cannot fix it |
| **Tooltip / lesson text** | Definitions and product specifics change faster than video |
| **Module checkpoint** | "What do I do next?" is a completion-state question |
| **Advanced gate** | "Does this apply to me?" is a condition, checkable on screen |
| **AI knowledge** | Situation-specific interpretation, which is what the calls were actually for |
| **Course video** | Only when it changes a planning *decision* for most students |

---

## 1 · App work: the provenance pattern

The single highest-leverage item in the audit. Every major output gets the same
three lines, in the same order, in plain English:

```
CALCULATED FROM   the inputs, named
EDIT SOURCE       the page where you change them
THIS AFFECTS      what downstream numbers move
```

Worked examples the calls specifically asked for:

**Surplus**
- Calculated from: income · taxes · living spending · debt payments
- Edit source: Cash Flow
- This affects: surplus · reserve funding · retirement date

**Portfolio-funded gap** (the app currently says *deficit*)
- Calculated from: retirement spending minus durable income
- Edit source: Plan → Income
- This affects: which account funds the year, and the bridge's price tag
- ⚠ Consider renaming the label to match the course, or the two terms need
  reconciling on camera forever.

**Confidence number**
- Calculated from: your saved assumptions · spending · retirement age ·
  balances · simulated return sequences
- Edit source: Plan → Retirement → Edit assumptions
- This affects: the date it is read against, and whether it is stale

> A consistent "Why this number?" control would remove more confusion than any
> additional course content. **Do not solve this with longer videos.**

## 2 · App work: layer labelling

Clients could not tell what was baseline truth, an expected change, or a
hypothetical. Module 1 now teaches the distinction; the app should show it.

- Label life events and scenarios distinctly wherever a projected number is
  affected by one.
- On any screen showing a projection, make it visible whether a scenario is
  currently selected.

## 3 · Tooltips and lesson text, not video

| Question | Answer lives in |
|---|---|
| What is a tax lot? | Tooltip + core lesson text |
| What does the deficit row mean? | Tooltip using the course's term |
| What is a drawdown? | Tooltip |
| What does 82% confidence mean? | Tooltip + 2.3 |
| What is dust? | Advanced A7.4 lesson text |
| Which model runs the AI, and what are the limits? | 1.2 lesson text (already moved) |
| What is the current 0% capital-gains ceiling? | The Tax page. **Never spoken** |

## 4 · AI knowledge backlog

Feed these to the assistant's knowledge base rather than the curriculum. Each
one appeared in the calls as *"does this apply to my situation?"* — which is
interpretation work, not teaching work.

- Reading a specific unusual account type into the right bucket
- Whether a given household's numbers show a conversion window
- Whether a specific debt is worth retaining at its rate
- What a scenario comparison is actually saying
- Which module a stalled student should return to, given plan state
- Household-specific bridge arithmetic

**Course knowledge is not yet loaded into the assistant.** When it is, the AI
should be able to answer "which lesson covers this?" and link. That is the
single highest-value AI addition for course students.

## 5 · Explicitly OUT of required core

These appeared in the calls only because the sessions were personalised. They
demonstrate the value of coaching; they are not curriculum, and every one of
them ages badly:

- Specific healthcare-sharing companies and their current terms
- Bitcoin miner economics
- Specific home-equity providers
- Specific Bitcoin treasury companies and covered-call funds
- Current lender terms
- Changing tax thresholds
- Beta-era interface behaviour
- Product-specific troubleshooting

## 6 · What replaces one-on-one interpretation

The calls show clients did not need six hours of new teaching. They needed help
applying the framework to an unusual account, debt, family, tax, or custody
situation. A self-paced offer needs a replacement for that, not more lessons:

1. Course + app + page-specific AI as the default
2. An FAQ built from these transcripts
3. Optional group office hours for unresolved decisions
4. An optional paid final plan review for people who want personal validation
5. Professional handoff prompts for tax, legal, insurance, and custody

## 7 · Next evidence, not next rewrite

Before another curriculum revision: give **Modules 1–3** to two or three
intelligent people who are not financial planners. Track where they pause,
replay, mis-enter data, or fail to complete the module.

That evidence outranks any runtime target.
