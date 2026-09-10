# Start filming

**[Open all filming scripts in one file](ALL-FILMING-SCRIPTS.md).** Teaching comes first, in member order; the walkthroughs follow for a separate recording session. Read only **Spoken script** and **Narration** aloud. All other sections are production directions.

Film teaching now, then capture each walkthrough when its redesigned app flow is ready. The lesson page pairs the explanation with the relevant implementation takes.

## Teaching session

1. Follow the contents in the master, or use the [recording order](filming/DICTATION-ORDER.md) to open individual scripts and clean teleprompter files.
2. Record the lesson introduction, explanation, transitions, and spoken handoff. Examples are selective; keep callbacks to earlier decisions brief.
3. Give the editor the master or [teaching overlay cues](filming/TEACHING-OVERLAYS.md). Each cue matches a line in the spoken script.

Use **[Client]** and **[Partner]** for names in screenshots, household cards, and account labels. Spoken examples use “our example household,” “the client,” and “their partner.” Keep the example amounts and account ownership consistent.

If a line sounds more natural when you say it differently, put that wording into its canonical `scripts/` file and regenerate the recording copies so the editor's cues still match. In a canonical script, the spoken section is called **Read aloud**.

## Walkthrough session

1. Use the [pairing map](filming/FILM-ORDER.md) to select the chapters for the teaching lesson. Their narration and production cues are in the master and the [separate walkthrough scripts](filming/WALKTHROUGH-SCRIPTS.md).
2. Verify the relevant screen and behavior using [capture dependencies](filming/WALKTHROUGH-CAPTURE-DEPENDENCIES.md). These scripts target the future app described by PR #227. Each take needs its actual flow checked before capture.
3. Record each chapter as its own take. Links in the separate walkthrough scripts open clean speech files, such as [W01-01](teleprompter/walkthrough/W01-01.txt). The [W01 session file](teleprompter/walkthrough/W01.txt) combines its chapter speech for a longer recording session.
4. Check the actual result and saved state before accepting a take. If an app result differs from the illustrative arithmetic, explain the real convention or correct the example. Follow D07's exact safe test setup for device footage.

Walkthroughs apply the teaching and carry earlier decisions forward. Detailed contract and collateral work follows the relevant conditional lesson. W07 prepares the family map; W08 performs the rehearsal once.

The lesson completion check confirms the member's decision or action. It is not additional narration. The [filming aids index](filming/README.md) collects the remaining editor and production references.
