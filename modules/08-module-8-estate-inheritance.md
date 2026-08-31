# Unit 9 · Module 8 — Estate + Inheritance

*Give the right people legal authority, align it with the custody process, create the family handoff, and transfer the risks the current stack cannot absorb.*

**You will build:** An executor path, legal-document plan, no-secrets heir letter and packet, communication backstop, and insurance gap audit.

## 8.1 Choose who is in charge and put the legal baseline in place

*`TEACH` · ~4.9 min · PRE-DICTATION FILMING DRAFT*

The custody module made sure the Bitcoin can be reached. Estate planning makes sure the right person has the legal authority to act and the family knows where to start.

The first decision is who will be in charge.

The executor is the person who carries out the instructions after death. Depending on the documents and the state, other roles may handle assets held in a trust or act during incapacity. The title matters less than choosing people who can actually do the job and making sure the documents give them the authority they need.

I would judge an executor on three things: capability, availability, and trust.

Capability means they can follow a legal and financial process, keep records, work with professionals, and avoid making rushed decisions.

Availability means they have the time and willingness. Somebody can be trustworthy and still be the wrong choice because the role would be too much for them.

Trust means they will act in good faith when the family is under pressure.

Pick for the job, not for who would be flattered to be asked. Then ask the person. An executor who has never heard about the role is not part of a working plan yet.

A nontechnical executor can still be a good executor. Give the executor a clear process, the right legal authority, and a named technical or custody contact when the setup requires one. The executor can coordinate the recovery without personally being the wallet expert.

> 🎬 **VISUAL — Estate deck: Capable / Available / Trustworthy, with professional executor as the alternative.**

The baseline legal work usually includes four areas.

A will directs how probate assets should be handled and names important roles. It does not control every asset automatically.

A financial power of attorney can give somebody authority to handle financial matters while you are alive but unable to act. That authority generally ends at death, which is why it is not a replacement for the executor or trustee role.

A healthcare directive covers medical decisions and wishes.

Beneficiary designations direct certain accounts or policies outside the will. Retirement accounts and life-insurance policies are common examples. The exact legal effect depends on the account and state, but the practical rule is simple: beneficiary forms need to agree with the overall estate plan and be reviewed after major life changes.

Digital-asset authority matters too. A document can name an executor without necessarily giving the person every permission needed to access online accounts or digital records. Ask the attorney how the state's digital-asset law and the account agreements affect the plan.

The documents and the custody process have to match.

The plan needs both legal authority and technical capability. The will identifies who may act; the tested custody process makes the Bitcoin recoverable by the authorized people.

Start with the legal baseline at every asset level. A simple plan that exists and is properly executed is more useful than an advanced trust design that never gets finished.

Trusts are an advanced decision used for jobs such as probate avoidance, incapacity planning, family control, asset protection, tax planning, or a complicated family situation. Bitcoin ownership by itself does not establish the need, and a revocable trust generally serves different jobs from estate-tax planning.

If the baseline is straightforward, a local estate-planning attorney who is willing to coordinate with the custody process may be enough.

When interviewing the attorney, I would ask:

- Have you planned for clients who hold direct Bitcoin or multisig, not only an exchange account?
- How will the documents give the right people authority without putting secrets into the legal file?
- How should the executor, trustee, custody provider, and technical helper work together?
- What beneficiary forms or account titles need to change?
- What state-specific signing, witnessing, or probate rules apply?
- If a trust may hold concentrated Bitcoin, how will the trustee's duties and the investment language be handled under this state's law?

Trustee duties and the authority to hold a concentrated asset depend on the governing law, the complete trust language, and the facts. Have the attorney draft the full authority instead of copying one waiver sentence from the internet. That is an attorney drafting issue.

Before moving on, choose the primary person and backup you would trust to run the process. Confirm whether they are willing. Then list which of the baseline documents and beneficiary reviews are already complete and which still need an appointment.

The next lesson connects that legal layer to the technical custody setup without pretending there is one universal way to split seeds, passphrases, or keys.

---
## 8.2 Align legal authority with the technical recovery path

*`TEACH` · ~4.7 min · PRE-DICTATION FILMING DRAFT*

This lesson is about making sure the legal plan and the custody plan lead to the same outcome.

I do not want to give you one universal formula such as "the heirs hold the seed and the executor holds the passphrase." That can work in a carefully designed and tested plan, but it can also create new failure points or give the wrong person practical control.

The right structure depends on the custody method, the people involved, the legal roles, and what each component can actually do.

Start with the principle: no unnecessary person should hold enough information or authority to act alone, but the family must still have a complete, tested recovery path when the proper conditions are met.

With ordinary single-signature custody, anyone who obtains the seed can usually recover that wallet. If a BIP39 passphrase is also used, the seed without the exact passphrase opens a different wallet. A passphrase is another secret that must be recovered exactly. It does not create a second signer or legal dual control.

Splitting those two objects between people can reduce one-person access in some designs, but it can also mean one lost memory, one unavailable person, or one family dispute locks everybody out. It should only be used when the full recovery has been tested and the attorney understands who has legal authority to combine the components.

Do not split a recovery phrase itself into arbitrary word groups and hand the pieces to different people. That creates fragile backups, can reduce security in ways people do not expect, and is not a substitute for a designed secret-sharing or multisig system.

With multisig, the structure is different.

A two-of-three wallet requires two valid signatures from the defined keys. A two-of-three wallet can create operational separation because one key alone cannot spend. The descriptor or wallet configuration, identity process, legal authority, and people remain part of the recovery plan.

The wallet descriptor or configuration records how the keys are combined, including the threshold and derivation information. Without the correct configuration, heirs may struggle to reconstruct the intended wallet even if they have key material.

> 🎬 **VISUAL — Two separate diagrams: passphrase single-sig and 2-of-3 multisig. Show what each component can and cannot do. Do not label a passphrase as a second signer.**

A collaborative custody provider may hold one key, a copy of the public wallet configuration, and an established recovery process. A collaborative provider can add support, identity verification, continuity, a documented procedure, and a third key. The trade-off is vendor dependence, fees, privacy considerations, and the need to understand what happens if the company changes or disappears.

A DIY multisig arrangement removes the provider but moves every operational duty to the household. Key distribution, descriptors, device compatibility, replacement, inheritance, and recovery documentation all become your responsibility.

The legal role also needs to be clear.

An executor, trustee, spouse, beneficiary, and technical helper may all be different people. The person with a key may not be the person legally entitled to direct a transaction. The person with legal authority may not be technically capable of signing one.

That is why I like separating roles on paper:

- Who has legal authority while you are alive but incapacitated?
- Who has authority after death?
- Who can locate each recovery component?
- Who can provide technical help without receiving every secret?
- Which provider or professional verifies the event and the identity?
- What stops one person from acting prematurely?
- What happens if one person or provider is unavailable?

The system should be tested at the process level while you are alive. Use a trivial-value test wallet or a documented tabletop exercise to confirm that everybody knows the first call, the role they have, and the components that exist. Keep real recovery secrets out of the exercise.

The plan should also account for change. Hardware wallets fail. Providers merge or close. Executors age. Families move. A custody design that works today can become unusable if it is never reviewed.

The deliverable is a tested path where the legally authorized people can recover the asset, one ordinary failure does not destroy the plan, and no secret is stored in the app or legal documents.

The heir letter in the next lesson tells the family how to start without disclosing the components themselves.

---
## 8.3 Write the heir letter and create the communication backstop

*`TEACH` · ~4.0 min · PRE-DICTATION FILMING DRAFT*

The heir letter is the calm starting point your family receives when they are least prepared to solve a technical and financial problem.

The heir letter is a no-secrets orientation document for the family. And it is not a list of passwords.

Its job is to answer the first practical questions:

- Who should I call first?
- What types of accounts and assets exist?
- Where are the legal documents and no-secrets instructions?
- Which custody or financial providers are involved?
- What should I absolutely not do?

The warnings are as valuable as the account list.

Do not respond to unsolicited recovery help.

Do not move Bitcoin because somebody creates urgency.

Do not enter a seed phrase into a website or send it to support.

Do not start liquidating accounts before the executor and tax professionals understand the plan.

Do not assume the person who knows technology is the person with legal authority.

> 🎬 **VISUAL — Estate deck heir-letter slide: include list on one side, never-include list on the other.**

The letter should never contain seed phrases, private keys, passphrases, PINs, passwords, backup-file passwords, exact storage coordinates, or the complete recovery path.

It can say that a hardware-wallet process exists, that a collaborative provider should be contacted, or that the executor packet identifies the professionals and document locations. It should point to the process without containing the power to move the asset.

I would keep a separate executor packet too. That is the no-secrets working folder for the person in charge. It may include professional contacts, copies or locations of legal documents, account and provider lists, insurance contacts, funeral or household instructions, and the order in which people should be called.

The heir letter orients the family. The executor packet helps the person running the process.

Both need to be available outside the app. A letter that only exists behind your login may never be found. Download it, print it when appropriate, store it with the estate documents, and make sure the executor knows the packet exists.

Then add a communication backstop.

A dead-man switch or another scheduled delivery process can send the no-secrets letter if you fail to check in for a defined period. The scheduled delivery makes sure somebody starts the documented process. It carries the no-secrets letter and never releases keys.

> 🎬 **VISUAL — Four-step communication flow: check in → missed window → waiting period → heir letter delivered.**

The cadence has to balance false alarms with delay. Orange Plan uses a ninety-day check-in as the current default. Whatever system you use, test the recipients, the waiting period, and the message.

A dead-man switch is a backup communication layer. The will, power of attorney, beneficiary forms, tested custody recovery, and family conversation still carry their own jobs.

I would also have the family conversation while you can answer questions.

Show them the process at a high level. Tell them who is in charge, which provider or professional to call, why they should not rush, and where the legal documents are kept. Do not reveal secrets just to prove the plan exists.

Then test delivery. Send a sample no-secrets message. Confirm the recipient recognizes it, understands the first action, and knows how to verify that it actually came from your system.

The finish line for this lesson is a letter that tells the family the first call and the first mistake to avoid, an executor packet that exists outside the app, and a tested communication method that can deliver the letter without releasing any secret.

The walkthrough will start the letter in Protect, confirm beneficiaries, enable the switch when Cloud mode is being used, download the document, and record the remaining outside-the-app actions.

---
## 8.4 Use insurance for the risks the current stack cannot carry

*`TEACH` · ~4.7 min · PRE-DICTATION FILMING DRAFT*

Insurance exists for the risks that would break the plan before the assets are large enough to absorb them.

The reserve already self-insures smaller problems. A repair, a deductible, or a short income interruption should not require a complicated policy if the cash buffer can handle it.

Insurance is for the larger gap between what the family would need and what the current assets could provide.

That gap changes over time. Early in the plan, a young family may depend heavily on one or two incomes and have decades of spending ahead. As the assets grow, debts decline, and the retirement date gets closer, the amount that needs to be transferred to an insurer may shrink.

I think of insurance as renting protection until the balance sheet can carry more of the risk itself.

Term life is the clearest example.

If somebody depends on your income and the current assets could not fund the family's remaining needs, term coverage can fill that gap during the working years. A multiple of income can be a rough starting point, but the actual planning question is what the family would need after considering existing assets, debts, Social Security survivor benefits, childcare, education commitments, and the surviving spouse's income.

Permanent life insurance combines lifelong coverage with a cash-value component and can have legitimate uses in certain estate, business, or lifelong-dependency situations. It is also more expensive and more complex. A sales illustration should be compared with the simpler alternative of buying the needed insurance and keeping the investment strategy separate.

Disability coverage protects the income while you are alive.

A long disability can stop the paycheck and the monthly surplus at the same time, while healthcare and other costs continue. Employer coverage may replace only part of the income, may have a dollar cap, may be taxable depending on who paid the premium, and may use a definition of disability that becomes harder to qualify for over time.

The contract language matters: own-occupation versus any-occupation definitions, waiting periods, benefit periods, exclusions, and how bonuses or self-employment income are treated. This is where the actual policy and a licensed professional matter more than a generic rule.

Umbrella coverage is excess liability protection above the required underlying home and auto limits. It can help protect the balance sheet from a large liability claim and defense costs. Umbrella coverage sits above the underlying policies and follows its own exclusions and required base limits. Read those terms before deciding which liability gaps it covers.

Long-term care belongs on the later-life review. The cost is real, the products and pricing are imperfect, and a sufficiently large plan may choose to self-insure. The decision depends on health, family support, desired care, state rules, and the size of the assets available later. It is worth revisiting in the years when coverage is still available, not waiting until care is already needed.

Health coverage before Medicare is part of the Retirement Income bridge rather than this insurance audit. The same principle applies: price the actual options and the risk retained by the household.

> 🎬 **VISUAL — Insurance coverage audit: Risk / current coverage / what the stack can absorb / remaining gap / next review date.**

For each category, I would write down:

- the risk being transferred;
- the current policy and benefit;
- the deductible or waiting period the reserve must cover;
- the amount the current assets could absorb;
- the remaining gap;
- and the event or balance-sheet milestone that would justify changing the coverage.

Beneficiary forms are part of the review. A policy can be perfectly sized and still pay the wrong person if the designation is stale.

Reassess coverage using the full plan, debts, dependents, and the amount the household could reliably spend from the assets after taxes and market risk. One Bitcoin market cycle is too narrow to establish that the family can self-insure the risk.

Use the coverage-audit worksheet as the current system of record for policies and quote comparisons, then bring the gaps to a licensed insurance professional. The professional review should confirm policy mechanics, exclusions, and whether the proposed amount and term match the actual household.

Finish with a clear list of which risks the Reserve and stack can carry, which risks still need a policy, and when each coverage will be reviewed again.

---
## 8.5 WALKTHROUGH — Build the family handoff in Protect

*`WALKTHROUGH` · ~12 min · IMPLEMENTATION SHEET*

**Screen capture · about 12 minutes**

> **V1 capture gate:** Verify the final label and click path against the same approved Preview commit used for recording.

## Before recording

- Primary executor and backup chosen; willingness confirmed when possible.
- Baseline legal-document status known.
- Custody method and technical helper / provider identified.
- Insurance coverage-audit worksheet started.
- No secrets in the demo material.

## 1 · Confirm beneficiaries

**DO** Protect → Beneficiaries.

**ENTER / REVIEW** the people and projected shares used by Orange Plan.

**SAY** Use this screen to coordinate the plan, then verify the legal beneficiary forms directly with the custodian or insurer and the attorney.

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

**DO** Build & improve → Protect.

**SEE** beneficiaries · heir letter · downloaded copy complete; outside legal, custody, and insurance actions remain visible in the production checklist.

## Module 8 checkpoint

- Executor and backup are chosen and contacted.
- Baseline legal documents have a clear status and attorney action.
- Beneficiary forms are scheduled for verification.
- Heir letter and executor packet contain no secrets.
- Communication backstop is armed and tested when applicable.
- Legal authority and technical recovery are mapped together.
- Insurance gaps are documented for licensed review.

---

<!-- ADVANCED-GATE:START -->

## Related advanced lessons

**Your core plan is complete.** These are optional, and each one is
worth watching only when its condition is true for you. Continue only if
one of these describes your situation:

- **A8.1 Do you need a trust, and what job would it do?**
  → *(no gate condition set — add one to MASTER-ADVANCED.md)*

*Generated by `tools/build-module-gates.py` from the Gate line on each
advanced lesson. Edit the condition there, not here.*

<!-- ADVANCED-GATE:END -->
