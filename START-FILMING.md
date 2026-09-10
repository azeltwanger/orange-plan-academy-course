# Start filming

Film the teaching and walkthroughs separately. The lesson page pairs them so a member learns the decision, then implements it.

## Teaching session

1. Open [the recording order](DICTATION-ORDER.md).
2. Open a lesson's source script to see its task and overlay cues. Read only **Read aloud**, or use its linked clean teleprompter file.
3. Record the explanation as written. The task comes first, followed by the decisions and worked example needed to complete it.
4. Give the editor [the overlay list](TEACHING-OVERLAYS.md). Each cue matches words in the recording; the overlays are not extra narration.

The scripts include an editorial slop-removal and voice pass using Austin's source dictation. Austin's spoken read-through is the final check of phrasing. Any wording change belongs in the canonical script before regenerating its teleprompter copy.

## Walkthrough session

1. Use [the pairing map](FILM-ORDER.md) to select the chapters for that teaching lesson.
2. Open [the walkthrough script](WALKTHROUGH-SCRIPTS.md). Each chapter has the screen action, complete narration, overlay, finish check and exact capture dependency.
3. Verify the relevant redesigned flow before filming. These scripts target the future app described by PR #227; they do not claim that every control has shipped.
4. Record each chapter as its own take. Use `teleprompter/walkthrough/W01-01.txt` and the equivalent files for speech without production notes. The `W01.txt` files combine the chapter speech for a longer recording session.
5. Check the actual result and saved state before accepting a take. When an app result differs from illustrative teaching arithmetic, explain the real convention or correct the example; do not stage a result.

Use [capture dependencies](WALKTHROUGH-CAPTURE-DEPENDENCIES.md) as the shot checklist. A missing app control holds that take, not the rest of the teaching. Device footage needs the exact safe procedure and test setup described in D07.

## Files for the editor

- [Teaching master with production notes](MASTER-COURSE.md)
- [Conditional teaching master](MASTER-ADVANCED.md)
- [Teaching overlay cues](TEACHING-OVERLAYS.md)
- [Walkthrough scripts and overlays](WALKTHROUGH-SCRIPTS.md)
- [Pairing map](FILM-ORDER.md)

The completion check at each lesson is private confirmation that the member has the intended decision or action. It is not another filmed lecture, worksheet assignment or public submission.
