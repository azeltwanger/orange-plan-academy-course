WALKTHROUGHS = {
    "7.4": {
        "title": "DEMO — Hardware-wallet recovery and exchange hardening",
        "body": r"""
# 7.4 · DEMO — Hardware-wallet recovery and exchange hardening

**External screen / device recording · about 12 minutes**

## Production safety

- Use a throwaway wallet with trivial funds.
- Use the exact device and firmware named in the take.
- Follow current official device instructions.
- Never show a real seed, passphrase, PIN pattern, backup QR, live family address, or meaningful account balance.
- Record the act of writing recovery material, not the words.
- Have a second person review the raw footage for accidental secrets before editing.

## Part 1 · Verify the device and create a test wallet

**DO** Unbox or reset the demo device according to the current official process.

**SHOW** authenticity / firmware verification steps the vendor currently requires.

**DO** Generate a new wallet on the device.

**SAY** A seed supplied in the package or by another person is not a new wallet.

**DO** Record the recovery material off camera and set the PIN.

## Part 2 · Receive and verify a small transaction

**DO** Generate a receive address.

**VERIFY** the address on the trusted device screen.

**SEND** a trivial test amount.

**SEE** the transaction appear.

## Part 3 · Prove recovery

**DO** Use the exact vendor-supported backup-check or wipe-and-restore process chosen for this device.

**RESTORE** the test wallet from the offline recovery material.

**VERIFY** the same wallet and test transaction reappear.

**SAY** This is the point where the backup becomes proven instead of assumed.

**⚠** Do not teach one device's button sequence as universal.

## Part 4 · Show the offline backup standard

**SHOW** paper versus steel without displaying recovery data.

**EXPLAIN** separate locations, theft trade-offs, and the annual inspection.

**DO NOT** show actual storage locations.

## Part 5 · Harden an exchange and the email account

Using demo accounts:

- change to a strong unique password;
- enable app-based 2FA or hardware-key authentication when supported;
- secure the email account first;
- enable withdrawal allowlists, delays, or approval controls that exist;
- save the official support path;
- remove SMS-only recovery where practical and supported.

**SAY** Never follow a login or recovery link from an urgent email, text, call, or direct message.

## Part 6 · Close with the repeatable standard

The setup earns meaningful Bitcoin only after:

- the device is verified;
- a small receive is confirmed on-device;
- recovery is proven;
- the offline backup is protected;
- the account and email are hardened;
- and the process is documented without secrets.

## Device verification receipt

Record in `DEVICE-DEMO-VERIFICATION.md`:

- device model;
- firmware version;
- official instructions checked date;
- recovery method used;
- test-wallet amount;
- reviewer who checked raw footage for secrets.
""",
    },
    "7.5": {
        "title": "WALKTHROUGH — Document the custody status without storing secrets",
        "body": r"""
# 7.5 · WALKTHROUGH — Document the custody status without storing secrets

**Screen capture · about 7 minutes**

## Before recording

- Hardware-wallet demo completed or clearly marked as still outstanding.
- A chosen custody level.
- One real single point of failure to fix.
- No secret material anywhere near the demo account or recording notes.

## 1 · Open Protect

**DO** Protect → readiness / security checklist.

**SEE** current tier, checklist sections, and attention queue.

**SAY** The app's tier is an implementation checklist. The household's custody level is the actual design decision from Lesson 7.1.

## 2 · Complete the checklist honestly

**DO** Review Hardware · Distribution · Legal · Access-after-death or the current sections.

**CHECK** only items that are true today.

**⚠** A recovery-test item stays open until recovery was actually proven. Buying a hardware wallet does not complete it.

**SAY** what is not being entered: no seed, passphrase, PIN, key, descriptor contents, or storage coordinates.

## 3 · Use the attention queue

**SEE** the top incomplete essential.

**CHOOSE** the largest current "only one" and state the fix and deadline.

**SAY** The goal is one meaningful reduction in risk, not checking every box for appearance.

## 4 · Confirm the process contacts without secrets

**DO** Review the relevant contact / provider fields that store names or roles, not recovery material.

**SAY** Who the household calls first and which provider or technical helper is part of the process.

**⚠** Estate authority and heir instructions are completed in Module 8.

## 5 · Back up the plan itself

**DO** Settings → Data & Privacy → Backup & Restore.

**CREATE** an encrypted export.

**SAY** This file protects the financial-plan data. It is not a Bitcoin wallet backup and should never contain seed material.

**⚠** In Local Only mode, the export may be the only recovery path for the plan data.

## 6 · Schedule the annual custody check

Record:

- prove one recovery;
- inspect backups and locations;
- review device / software support;
- re-scan shared dependencies;
- refresh account security;
- update the encrypted plan backup.

## 7 · Close Custody

**DO** Return to Build Your Plan / Protect status.

**SEE** the custody work represented honestly even when outside-device work remains.

## Module 7 checkpoint

- Custody level is chosen.
- Hardware recovery is proven or clearly outstanding.
- Top single point of failure has an owner and deadline.
- Important accounts and email are hardened.
- No secret is stored in Orange Plan or the course notes.
- Encrypted plan backup is saved.
""",
    },
    "8.5": {
        "title": "WALKTHROUGH — Build the family handoff in Protect",
        "body": r"""
# 8.5 · WALKTHROUGH — Build the family handoff in Protect

**Screen capture · about 12 minutes**

## Before recording

- Primary executor and backup chosen; willingness confirmed when possible.
- Baseline legal-document status known.
- Custody method and technical helper / provider identified.
- Insurance coverage-audit worksheet started.
- No secrets in the demo material.

## 1 · Confirm beneficiaries

**DO** Protect → Beneficiaries.

**ENTER / REVIEW** the people and projected shares used by Orange Plan.

**SAY** This planning screen does not update the legal beneficiary forms at the custodian or insurer. Those forms are checked separately and coordinated with the attorney.

## 2 · Start the heir letter

**DO** Protect → Heir letter.

**ENTER** first contact · account and provider categories · document locations at a safe level · first warnings · professional contacts.

**SAY** the first call and first mistake to avoid.

**⚠** Never enter seeds, keys, passphrases, PINs, passwords, exact recovery steps, or storage coordinates.

**OPTIONAL** Show Draft with AI only after restating the no-secrets rule. Review every generated line.

## 3 · Download and place the document

**DO** Export / Download the heir letter.

**RECORD** where the printed or encrypted no-secrets copy will be stored and who knows it exists.

**SAY** A letter that exists only behind the creator's login may never be found.

## 4 · Build the executor packet outside the app

List on screen:

- executor and backup;
- attorney, CPA, custody provider, and technical helper;
- legal-document locations;
- account / policy inventory;
- order of first calls;
- no-secrets custody map;
- insurance contacts;
- annual review date.

**⚠** The packet points to the recovery process; it does not contain the recovery secrets.

## 5 · Enable the communication backstop

**DO** Protect → Dead-man switch.

**ENABLE** the current cadence and recipients when Cloud mode is used.

**SEE** next check-in / delivery status.

**SAY** The switch delivers direction, not keys. It does not replace legal documents or tested custody recovery.

**TEST** a safe sample delivery when the product supports it.

## 6 · Record legal and custody alignment

Using a no-secrets table, state:

- who has authority during incapacity;
- who acts after death;
- who knows each component exists;
- which provider or helper supports recovery;
- whether the process was tested;
- the attorney question still open.

**⚠** Do not present one seed/passphrase or multisig split as universal.

## 7 · Record insurance gaps

**DO** Use the worksheet, not an invented app feature.

**REVIEW** life · disability · umbrella · long-term care / later-life review.

**RECORD** current coverage, risk retained by the Reserve / stack, remaining gap, and next professional action.

## 8 · Close Protect

**DO** Build Your Plan → Protect.

**SEE** beneficiaries · heir letter · downloaded copy complete; outside legal, custody, and insurance actions remain visible in the production checklist.

## Module 8 checkpoint

- Executor and backup are chosen and contacted.
- Baseline legal documents have a clear status and attorney action.
- Beneficiary forms are scheduled for verification.
- Heir letter and executor packet contain no secrets.
- Communication backstop is armed and tested when applicable.
- Legal authority and technical recovery are mapped together.
- Insurance gaps are documented for licensed review.
""",
    },
    "9.3": {
        "title": "WALKTHROUGH — Finish, test, review, and save the plan",
        "body": r"""
# 9.3 · WALKTHROUGH — Finish, test, review, and save the plan

**Screen capture · about 20 minutes**

## Before recording

- Every prior module completed on the demo plan.
- Current holdings, cash flow, debts, allocation, tax history, retirement income, beneficiaries, and heir letter entered.
- No existing full confidence receipt, or a clean way to show the first completed run.
- One meaningful scenario question prepared.
- Calendar open for monthly and annual review dates.

## 1 · Close every Build Your Plan area intentionally

**DO** Open Build Your Plan.

**WALK** Foundation · Cash flow · Allocation · Debt · Tax · Retirement income · Protect.

**SEE** complete, truthfully not applicable, or a precise missing-data line.

**FIX** any open source input before running confidence.

**SAY** Watching the course did not complete the plan. The real data and applied decisions did.

## 2 · Run the first full confidence check

**DO** Build Your Plan → Run your plan / Plan page → **Run confidence**.

**SEE** 1,000 test runs complete against the full baseline.

**SAY** This is the first confidence result we treat as the finished-plan baseline. Onboarding used one deterministic estimate; this run includes the completed plan across many market paths.

## 3 · Choose the confidence target and read the earliest date

**DO** Set the target confidence using the current control.

**SEE** earliest retirement date at that target.

**READ** date and confidence together.

**SAY** A lower target can produce an earlier but more adjustable plan. A higher target usually asks for more time, savings, or lower spending. One hundred percent is not automatically the objective.

**SAVE / CONFIRM** the target and receipt.

## 4 · Set the retirement operating target

**DO** Income → Retirement operating plan / What you can spend.

**CHOOSE** the starting spending target at the selected confidence policy.

**SEE** the annual 60 / 80 / 95 guardrail logic and ten-percent cap.

**SAVE** the starting target.

**SAY** The confidence target sets the plan. The guardrails adjust it in later annual reviews.

## 5 · Run one clean scenario

**DO** Scenarios → create or select one question.

**CHANGE** only the inputs needed.

**COMPARE** retirement date · confidence · taxes · accessible money · debt / LTV · estate or Bitcoin remaining.

**DECIDE** apply to baseline, keep as evidence, or delete.

**⚠** Do not leave the learner with unnamed scenario copies and no clear baseline.

## 6 · Run the five-minute monthly pass

Start a visible timer.

**DO** Cash Flow → This month · enter one recent purchase or transfer · verify spending · review open attention items · choose one to three actions.

**STOP** the timer.

**SAY** Most months are quieter. No material change is a successful review.

## 7 · Walk the annual review

Visit one screen per area:

- Cash Flow / Income: spending, guardrail, Reserve refill.
- Allocation: current versus target and drawdown tolerance.
- Debt: jobs, rates, and LTV triggers.
- Tax: basis, harvest room, conversion window before year-end.
- Custody: prove one recovery and fix the largest shared dependency.
- Estate / Insurance: beneficiaries, letter, executor, switch, coverage gaps.

**APPLY** the annual retirement update only when the demo state makes it due and the result is understood.

## 8 · Read the report in planner order

**DO** Open Report.

**READ**:

1. Position — does today's account and debt picture match reality?
2. Trajectory — retirement date, confidence, spending, and funding.
3. Risk — alternate paths, taxes, debt, custody, and protection.
4. Actions — one to three next steps.

**CHECK** assumptions and methodology at the end.

## 9 · Save the yearly artifacts

**DO** Print / Save report as PDF with the year in the filename.

**DO** Settings → Backup & Restore → create a fresh encrypted plan export.

**SAY** Report = readable annual snapshot. Encrypted export = recovery file for the app data. Neither is a Bitcoin wallet backup.

## 10 · Schedule the rhythm

**DO** Calendar → recurring monthly review and annual review.

**RECORD** tax review before year-end and custody / estate check within the annual session.

## Final checkpoint

- Every Build Your Plan area is intentionally complete.
- First full 1,000-path confidence result is saved.
- Confidence target and earliest date are understood together.
- Retirement operating target and guardrail policy are saved.
- One scenario was tested without corrupting the baseline.
- Monthly and annual review dates are on the calendar.
- Report PDF and encrypted backup are saved.
- One to three next actions are clear.
""",
    },
}
