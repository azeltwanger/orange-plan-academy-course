# Orange Plan Academy — filming scripts

**[Open the current course: all filming scripts in one file](ALL-FILMING-SCRIPTS.md)**

The complete manuscript contains 25 main lessons, eight situational lessons, and 72 separately filmed app/device walkthrough takes, with spoken text, overlays, and production cues.

The teaching is conversational, uses examples where they help, and hands each decision off to its walkthrough. Members build and maintain their own Orange Plan as they go.

[Start filming](START-FILMING.md) explains the two recording sessions. [Filming aids](filming/README.md) has the editor's overlays, pairing map, clean-take links, and capture checklist. Teaching can be filmed while the redesign finishes; walkthrough footage depends on verifying the relevant PR #227 flow.

<details>
<summary>For contributors: source files and checks</summary>

Edit teaching and walkthrough content in `scripts/`. The filming master, recording aids, and individual `teleprompter/` files are generated from those canonical scripts.

```sh
python tools/guided_course.py build
python tools/guided_course.py check
python tools/guided_course.py test
python -m unittest discover -s tests -p 'test_*.py' -v
python tools/guided_course.py history
```

Checks cover script completeness, generated-copy parity, arithmetic, cue matching, and source preservation. Use a full-history checkout for the history check. Actual filming, Austin's delivery review, and learner testing are separate.

The [current owner direction](reference/owner-stepwise-direction-20260910.md), [focused-script pass](production/FOCUSED-SCRIPT-PASS.md), and [future-app alignment](V1-COURSE-ALIGNMENT.md) guide later edits. Original dictation, reviewed source material, fixture data, capture evidence, and member toolkit remain preserved.

</details>
