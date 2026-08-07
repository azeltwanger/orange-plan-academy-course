# Walkthrough: document your custody map

Follow along (~15 minutes). If you'll arm the dead-man switch next module, flip to Cloud mode now.

> **The app's tier is not your custody level.** The checklist tier keys to **estate net worth** (Foundation <$500k / Substantial $500k–$2M / HNW $2M+), and Hardware items only appear at Substantial+. Your **custody level** keys to something else: what the Bitcoin is for, how much is actually at risk, your technical ability, whether your family could recover it, your estate complexity, and your liquidity needs.
>
> These do not move together. A household with $400,000 of net worth and $350,000 of it in direct self-custodied Bitcoin sits in Foundation and never sees the hardware items. They need a serious recovery process anyway.
>
> **The tier-filtered checklist is a convenience, not your custody recommendation.** If your Bitcoin position is heavier than your tier implies, hold yourself to the higher standard.

1. **Orient on Protect**: the readiness bar ({n} of 5 essentials) and the Needs attention queue: always the next single fix.
2. **Walk the checklist honestly**: 4 groups (Hardware / Distribution / Legal / Access after death). Check "recovery tested" and "backup verified" only if you actually did them. A checked box that never happened means the plan believes something untrue. The top unchecked item is this week's fix, not the whole list. No free-text anywhere: never write secrets in the app.

   **The two Distribution boxes measure two different things, and you do not have to satisfy both:**

   | Checkbox | What it tests | Required? |
   |---|---|---|
   | Key material in 2+ physical locations | **Redundancy.** Can one lost copy permanently prevent recovery? | Yes, at every level. Unchecked is a real gap |
   | No single person can access funds alone | **Dual control.** Can one person move the coins by themselves? | No. This is a design choice |

   A well-run single-signature household answers "yes, the owner can spend alone." That is a sound setup. **The finish line is knowing which test your design passes, which it does not, and why you accepted that.**

   ⚠ **Dual control without redundancy is worse than where you started**: you have built two independent ways to lose everything instead of one.
3. **Back up the plan itself**: Settings → Data & Privacy → Data & backups → Export Plan. The passphrase prompt is for the *backup file*, not a wallet, and it's the third use of the 7-random-word standard from the advanced-custody lesson. In Local Only mode this file is your only backup.
4. **Fill the two custody documents.** They have different jobs and different readers, and they should not be stored together.

   | | **Owner Custody Audit** (private) | **Family Access Map** (shared) |
   |---|---|---|
   | Who reads it | You | Spouse, heirs, executor |
   | Holds | Backup medium, recovery-test log, single points of failure, whether multiple locations exist, whether a passphrase is involved, config-file status, the security fixes queue | What categories of assets exist, which provider or custody type, who knows the process, who to contact, where the non-secret executor documents live |
   | Secrets | None | None |
   | Distribution | Not broadly distributed | Stored with the will and Heir Letter |

   **Do not write exact physical locations on the family-facing map.** A stolen document listing where every seed backup, device and passphrase copy sits is a treasure map even though it contains no secret. Use controlled references instead:

   ```
   Seed backup: Location A
   Retrieval instructions held by: executor / attorney / sealed packet
   ```

   ⚠ **The legend needs its own backup.** Coding the locations passes the dual-control test and can fail the redundancy test: if the executor packet holding the decode is lost, or the person holding it cannot be reached, your family has a map they cannot read. Before you code anything, write down where the **second copy of the legend** lives and who can reach it. Otherwise you have rebuilt a 2-of-2 out of paperwork.

   The Heir Letter says who to call. The Family Access Map says what exists and how to start.
5. **Record decisions**: custody level chosen, which of the two tests your design passes, top single point of failure + this week's fix, annual custody review on the calendar.
6. **Walk past "Draft with AI"**: that's the heir letter assistant, next module's job.

**Done when:** Needs attention is shorter than at the start, the hardware items are honest, you can say which of the two tests your design passes and why the other one is acceptable, no secret was typed anywhere, and the encrypted plan file is on disk.

## Review annually, and whenever one of these changes

The calendar is not the only trigger. Pull the custody review forward when:

- a new wallet or custodian enters the picture
- your Bitcoin rises materially in value
- there is a new spouse, heir, executor, or trusted person
- you move to another home or another state
- you replace a device
- a backup location changes
- a new legal document is signed
- there is a health or family change
- you open a Bitcoin-backed loan or set up collateral

Any one of these can quietly break a design that was correct when you built it.

## Ask the AI

Open **Plan Guide** and ask for *"can my family access what they need."* That's the **Review Protection Plan** workflow. It reads completion status only, never names, locations, or anything secret.
