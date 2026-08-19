# Orange Plan Academy — walkthrough run-sheet template

**Use:** copy this file only after Austin has completed the relevant Build Your Plan step in a working preview. A mockup, spec, or guessed route is not enough.

Walkthroughs are short, replaceable implementation videos. They are not teleprompter scripts and do not reteach the full concept lesson.

---

# Metadata

```yaml
walkthrough_id:
module:
lesson_support:
planning_area:
app_step_id:
app_step_label:
primary_route:
starting_demo_checkpoint:
ending_demo_checkpoint:
demo_fixture_version: demo-v1-inputs
last_verified_app_commit:
last_verified_date:
concept_video_status:
walkthrough_status: draft
save_behavior: autosave | save_action | apply_action | scenario_only | mixed
app_completion_rule:
human_completion_rule:
professional_gate: none | cpa | custody | estate | insurance | other
```

## Recording title

Use the learner's task, not the page name alone.

> Example: **Set your confidence target and read the earliest date**

## One-sentence purpose

> We already decided ____. This walkthrough puts that decision into Orange Plan and verifies ____.

## Do not record yet when

- The exact route or label is still changing.
- Save/apply behavior has not been verified.
- The demo checkpoint does not reconcile.
- The required professional correction has not been applied.
- The concept lesson and app now ask for different decisions.
- The page produces an app-owned output that has not been captured in the current receipt.

---

# Before recording

- [ ] Use the isolated synthetic demo account.
- [ ] Confirm the starting checkpoint and fixture version.
- [ ] Confirm the current app commit.
- [ ] Confirm the current Build Your Plan step ID and label.
- [ ] Confirm the save, preview, Apply, or Scenario state.
- [ ] Confirm the app completion rule.
- [ ] Confirm the human planning finish line.
- [ ] Confirm required checkpoint outputs and reconciliations pass.
- [ ] Remove notifications, personal browser profiles, credentials, and customer data.
- [ ] Keep every Bitcoin secret outside the app and recording.

# Demo state

State only the facts needed for this decision.

| Input | Current demo value | Source |
|---|---:|---|
|  |  | `DEMO-HOUSEHOLD.md` / checkpoint receipt |

Do not repeat the entire household balance sheet.

# Decision recall

Open with one sentence:

> In the concept lesson, we decided ____ because ____.

Ask the learner to predict one result before changing the app:

> When this changes, which number should move and in which direction?

# Recording steps

Use the smallest number of steps required to implement the decision.

## Step 1 · Enter through Build Your Plan

**DO**

- Open the current Build Your Plan entry point.
- Select the verified step.

**SHOW**

- Step label
- Current completion state
- What the step is asking the learner to finish

**SAY**

- One sentence connecting this step to the concept decision

**DO NOT RETEACH**

- The full financial-planning explanation

## Step 2 · Verify the source inputs

**DO**

- Open the page or row that owns the input.
- Confirm the canonical demo value.

**SHOW**

- Which value is saved
- Whether it is verified, estimated, or missing

**NUMBER PROVENANCE**

- **WHAT IT MEANS:**
- **CALCULATED FROM:**
- **EDIT SOURCE:**
- **THIS AFFECTS:**

Use all four lines the first time the module's important output appears. Later screens can point back to the named source.

## Step 3 · Implement the decision

**DO**

- Enter, select, save, Apply, or create the Scenario using the verified behavior.

**SHOW**

- Current versus Previewing when the page supports a preview
- The exact action that changes the saved plan

**SAY**

- Whether the learner is viewing a saved input, unsaved preview, applied strategy, read-only result, or separate Scenario

**DO NOT SAY**

- “If you didn't click Apply, it didn't happen” as an app-wide rule

## Step 4 · Read what changed

**DO**

- Let the current app calculation complete.
- Point to the checkpoint-controlled result.

**SHOW**

- The output that should have moved
- Any important downstream result
- Current source/receipt reconciliation when useful

**ASK**

> Did the number move the way you predicted? Why?

If the result is surprising, trace it. Do not change another input merely to produce the expected answer.

## Step 5 · Return to Build Your Plan

**DO**

- Return to the current step list.
- Show the completion state.

**EXPLAIN**

- What the app checkmark proves
- What it does not prove
- What human decision completes the planning area

# What changed

End with a small before/after table from the checkpoint receipt.

| Item | Before | After | Why it moved |
|---|---:|---:|---|
|  |  |  |  |

Do not fill the table from memory or a mockup.

# Finish line

## App complete when

> [Exact app completion rule]

## Human complete when

> [The learner can explain the decision and has completed any required real-world action]

## Next Build Your Plan step

> [Current verified label]

# Number checklist

For every app-owned output shown:

- [ ] Value matches the current checkpoint receipt.
- [ ] Source input is identifiable.
- [ ] The same number agrees across cards, tables, report, and tooltip where applicable.
- [ ] Taxes, debt, life events, and reserve refill are not hidden inside a vague spending label.
- [ ] Bitcoin sold or retained agrees with the funding-source calculation.
- [ ] Preview and saved states are not confused.

# Retake triggers

Replace or patch this walkthrough when any of these change:

- Build Your Plan step ID or label
- route or page hierarchy
- control label
- input contract
- save/apply behavior
- completion rule
- important output
- checkpoint fixture or result
- report field
- product security or privacy boundary

A cosmetic change that does not affect understanding may not require a full retake. Record the review decision in the crosswalk.

# After recording

- [ ] Confirm recording matches the app commit in metadata.
- [ ] Create or update the ending checkpoint receipt.
- [ ] Update `BUILD-YOUR-PLAN-CROSSWALK.md`.
- [ ] Update the lesson's filming-readiness row.
- [ ] Verify caption and lesson text use current terms.
- [ ] Archive the replaced walkthrough under its app commit/version.

The walkthrough is successful when the learner can complete the current app work without needing the video to reteach the concept.