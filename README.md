# Orange Plan Academy — filming scripts

[All scripts in one file](ALL-FILMING-SCRIPTS.md) · [Start filming](START-FILMING.md)

The course follows the steps in Austin's slide decks. Each lesson tells the member what to do, explains how to think about the decision, then implements it in a separately recorded walkthrough.

There are 25 main teaching recordings and eight **For your situation** recordings. The ten app walkthroughs and one device walkthrough are separate filming work. Their chapters are individual takes paired with the relevant teaching, not another course to watch from beginning to end.

| For this job | Open |
|---|---|
| Read or film everything from one file | [All teaching and walkthrough scripts, with overlays](ALL-FILMING-SCRIPTS.md) |
| Record the teaching | [Recording order](DICTATION-ORDER.md) or [all clean teaching text](ALL-SCRIPTS.md) |
| Add text and graphics | [Teaching overlay cues](TEACHING-OVERLAYS.md); each source script has its own cue table |
| Record app/device footage | [Walkthrough scripts](WALKTHROUGH-SCRIPTS.md) and clean takes in `teleprompter/walkthrough/` |
| Pair the recordings | [Film order](FILM-ORDER.md) |
| See the tasks and slide sources | [Course step map](COURSE-STEP-MAP.md) |
| Check what still needs the redesigned app | [Capture dependencies](WALKTHROUGH-CAPTURE-DEPENDENCIES.md) |
| Check lengths and editorial status | [Metrics](COURSE-METRICS.md) · [Finalization status](FINALIZATION-STATUS.md) |

Teaching scripts include `Do this`, complete `Read aloud` text, overlay cues, a walkthrough handoff and a completion check. Walkthrough chapters contain **Show / Narration / Overlay / Verify / Capture dependency**. Only the teaching Read aloud section and walkthrough Narration blocks are spoken. Individual teleprompter files contain speech only.

Members apply the course to their own Orange Plan. A fictional household demonstrates the process, with [Client] and [Partner] as generic display labels. No extra homework, quiz, submission or required community post. Saving a plan does not execute a transfer, lender payment, legal document or custody procedure.

## Editing source and checks

Edit `scripts/` only for teaching and walkthrough content. Generated masters, overlays, film maps and teleprompter files flow outward from that source.

```sh
python tools/guided_course.py build
python tools/guided_course.py check
python tools/guided_course.py test
python -m unittest discover -s tests -p 'test_*.py' -v
python tools/guided_course.py history
```

Checks cover source preservation, the fixed household, arithmetic, generation, cue matching and separation of speech from production instructions. Editorial judgment, Austin's own delivery and real app/device proof are separate.

[Current owner direction](reference/owner-stepwise-direction-20260910.md) supersedes older narration-only restrictions. [PR #227 alignment](V1-COURSE-ALIGNMENT.md) records the future-app reference. Original accepted scripts, dictation, capture evidence and the member toolkit remain preserved. This repository change does not release the course to students or modify the app.
