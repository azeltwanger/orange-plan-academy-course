# Unit 9 · Module 8 — Estate & Inheritance

*Turn 'you can access it' into 'they can inherit it': executor and legal documents, the access split, the heir letter, the backstop switch, insurance, trusts if needed, and the Bitcoin-specific questions for the attorney.*

> **US-specific module.** The executor role, the four documents, probate, trusts, and the federal exemption are all US law. Said ONCE, at the top of 8.1, and never repeated per lesson.

## 8.1 The executor, the four legal documents, and choosing an estate attorney
*`TEACH + APP` · ~1,011 words · ~7 min*

**By the end of this lesson, you can:**

- Choose an executor using the capable/available/trustworthy test
- Name the four core estate documents and each one's job
- Understand why a valid beneficiary/POD/TOD form generally controls instead of the will, and why each one still gets verified with the provider
- Screen an estate attorney with Bitcoin-specific questions
- Recognize the Prudent Investor waiver that lets a trust hold concentrated Bitcoin

---

In today's lesson, we're going to build the legal and human layer around the custody process.

This module is US-specific and state-specific. The course can teach the jobs the documents perform. An attorney licensed in the governing state has to draft and supervise the actual plan.

### Nomination is not appointment

A will usually nominates the person you want to serve as executor and directs the probate assets.

The executor generally receives legal authority through the court process after death. Before appointment, the nominee may have very limited power to act.

If there is no valid will, the court can appoint an administrator under the state's intestacy rules.

So the problem with no will is not that nobody can ever receive authority. The problem is that state default rules and a court process choose the path instead of the plan you wrote.

### Document one: the will

The will directs probate assets, nominates the executor, and can nominate a guardian for minor children.

A guardian nomination is not an automatic appointment. The court makes the final decision under state law.

The will does not control every asset. A valid beneficiary, payable-on-death, transfer-on-death, trust, joint-ownership, or retirement-plan arrangement may transfer outside the will.

That is why the estate plan is a coordinated system rather than one document.

### Document two: financial power of attorney

A financial power of attorney authorizes an agent to act during life under the terms of the document.

It is an incapacity and lifetime-management tool. It generally ends at death.

The document should address digital assets and the accounts the agent may need to manage, subject to the state's law and provider terms.

### Document three: healthcare directive

A healthcare directive and healthcare power name who makes medical decisions and record the owner's wishes when the owner cannot communicate.

This is not an inheritance document. Its job ends where the executor and post-death plan begin.

### Document four: transfer and access records

Beneficiary, POD, TOD, and retirement-plan designations can transfer the covered asset outside the will.

A valid provider-held designation generally controls that account, but "generally" matters.

Plan terms, ERISA, spousal consent, QDROs, community-property rules, state law, and an invalid or outdated designation can change the result.

Orange Plan records intent. The provider holds the binding account record.

The fourth category also includes the digital-asset authority language the legal documents need.

Many states follow a version of the Revised Uniform Fiduciary Access to Digital Assets Act. Access to an account and access to the content of electronic communications can be treated differently, and explicit consent may be required.

Ask the attorney to address digital assets and electronic communications directly rather than relying on a generic property clause.

### The executor is a person, not a name in a field

Ask the person before naming them.

They should understand:

- that the role exists;
- who the attorney and tax professional are;
- where the legal documents and no-secrets process map are kept;
- what not to do with Bitcoin;
- that they may need court appointment before acting;
- that they never need the wallet backup merely to begin the legal process.

The executor does not need every signing secret. They need authority, process, and the right people.

### Legal authority and technical control are different

A person can be legally authorized and unable to sign.

A person can hold enough signing material and have no legal authority to use it.

A good estate plan aligns those two systems.

The will, trust, or court order governs authority. The custody design governs what can technically authorize a transaction. The heir letter and custody map explain how to start. None replaces the others.

### Beneficiary review

For each retirement account, insurance policy, brokerage account, bank account, and provider that supports a designation:

1. read the current provider record;
2. confirm the primary and contingent beneficiaries;
3. confirm percentages and per-stirpes or similar choices when available;
4. check spouse-consent and plan-document rules;
5. save evidence of the review without storing account secrets in the course tools;
6. coordinate the designation with the will and trust plan.

Do not assume an entry in Orange Plan changed the provider's record.

### Choosing the attorney

The attorney does not have to be a Bitcoin engineer.

They do have to be willing to coordinate legal ownership and fiduciary authority with a custody process they may not have seen before.

Ask:

1. How does this state treat probate, elective-share or community-property rights, and guardian nominations?
2. Which assets in this household pass by will, beneficiary form, joint ownership, or trust?
3. Does the power of attorney include the digital-asset powers needed during incapacity?
4. Does the estate plan include explicit consent for digital assets and electronic communications under this state's law?
5. How should an executor, trustee, heir, and custody provider coordinate without placing all signing power with one person?
6. Which document authorizes retention of a concentrated Bitcoin position, and what fiduciary protections are available under this state's trust law?
7. What signing and witnessing process makes these documents valid here?

### The executor packet

The Executor Packet is an operational briefing, not a legal instrument.

It can explain the first week, contact list, account inventory, tax order, and Bitcoin safety rules.

It cannot appoint the executor, change a beneficiary, authorize access to an account, or override a court order.

Use it to brief the person the legal documents nominate.

### Your decision

Who will be nominated, whether they have accepted, and which state-licensed attorney will draft and coordinate the documents.

### Put it in orange plan

Protect records the completion status, beneficiaries as intent, emergency contacts, and the family process.

Do not store seeds, private keys, passphrases, PINs, account passwords, full account numbers, or exact recovery locations.

### You are done when

The executor has accepted, the provider-held beneficiary records were reviewed, the attorney has the digital-asset questions, and every operational document is clearly labeled as process rather than legal authority.


## 8.2 Split access: dual control and redundancy
*`TEACH` · ~767 words · ~5 min*

> ✅ **SAFETY REWRITE (2026-08-08).** The old lesson claimed a seed + passphrase
> split gave "no single point of failure" and that half of it left the plan
> "intact." Seed + passphrase is 2-of-2; half of a 2-of-2 is zero access.
>
> ✅ **OPTIONALITY FIXED (2026-08-08).** 7.3 tells students the advanced setups
> are optional and their custody plan is complete without them. This lesson
> then required a passphrase or multisig to build the family access plan. Now
> it teaches the two tests and an honest design **at whatever custody level the
> student already has** — including Level 1 and Level 2, which previously had
> no answer here at all. The passphrase and multisig implementations moved to
> Advanced Custody, where the custody decision lives.

**By the end of this lesson, you can:**

- Apply the two tests: dual control, and redundancy
- Design an access split that fits the custody level you actually have
- Say out loud which test your design does not pass
- Back up each piece on its own side without collapsing the split
- Prove the design with a small amount before it matters

---

In today's lesson, we're going to test whether one person can spend alone and whether one loss can permanently block recovery.

These are two different questions. Dual control tells you whether one person can spend alone. Redundancy tells you whether one loss can stop recovery.

### Test one: can one person spend alone?

If one person, one backup, or one account credential can authorize the whole balance, the setup fails the dual-control test.

That may be an accepted trade in a simple single-signature wallet. It should not be described as if two people are required when they are not.

### Test two: can one loss stop recovery?

If one missing device, backup, passphrase, person, provider, or wallet policy can permanently stop recovery, the setup fails the redundancy test.

A system can pass one test and fail the other.

One seed copied into three locations is redundant against one location loss, but every copy is still sufficient to spend.

A mnemonic and passphrase stored apart can prevent either item alone from deriving the intended passphrase wallet, but losing either can block recovery. That is operational two-part access, not on-chain multisig.

A 2-of-3 multisig can pass both tests when any two keys work, one cannot spend, one can be lost, and the policy/descriptor is recoverable.

### Level 1: institutional control

At Level 1, the institution controls signing.

The household's dual-control and redundancy questions are delegated to the provider's controls, beneficiary record, account recovery, and death-claim process.

Verify what the provider actually requires. Do not assume an institution's legal process works like a wallet recovery.

### Level 2: single-signature control

A Level 2 single-signature wallet usually has one sufficient recovery path.

That means someone holding the complete wallet backup can generally control the wallet, unless another required element such as a passphrase exists.

Multiple backup copies create location redundancy but also create multiple sufficient spending copies.

The old course prescribed one universal Level 2 family arrangement even though Austin had not dictated one. That recommendation has been removed.

For Level 2, write the accepted trade plainly:

- who can technically recover;
- who is legally authorized;
- how redundant copies are protected;
- whether one-person spending is accepted;
- what event would justify moving to a passphrase or multisig design.

The estate attorney coordinates authority. The custody lesson coordinates technical recovery. The course does not choose the backup holder for every family.

### Level 3: passphrase separation

A passphrase wallet can separate the mnemonic and exact passphrase.

Each element needs its own backup and recovery path.

The standard no-passphrase wallet still exists. Whether it is empty, a decoy, or used for another purpose is deliberate.

This design can reduce the risk of one found backup revealing the intended wallet. It also creates an all-parts-required recovery unless the household adds redundancy on both sides.

Test the exact intended wallet. Every passphrase typo derives another valid wallet.

### Level 4: multisig

A 2-of-3 wallet requires two signing keys.

To recover it, the family also needs the wallet policy or descriptor and compatible software.

The descriptor cannot spend. Storing it with a key does not change the 2-of-3 threshold.

It is still privacy-sensitive and should be backed up in places the intended recovery team can reach.

Distribute keys across independent failure domains and test the combinations the family plan depends on.

### Legal role versus key role

Executor, trustee, heir, guardian, provider, and signing-key holder are not interchangeable roles.

The legal documents decide who is authorized to act. The signing policy decides who can technically authorize a Bitcoin transaction.

A key holder may need to sign under an executor's or trustee's legal instruction. A legally authorized person may need help from the threshold key holders.

Write both maps and make sure they agree.

### The family meeting

The meeting teaches:

- who calls the attorney first;
- where the legal documents and no-secrets map live;
- which people hold roles;
- which action requires another person;
- what nobody should ever reveal or improvise.

It does not reveal the backup, passphrase, PIN, or exact key locations to everyone in the room.

### Your decision

Which of the two tests the setup passes, which one it fails, and whether the accepted failure is still appropriate for the current amount and family.

### Put it in orange plan

Protect records the level, recovery-test status, and process completion. Keep the seed, passphrase, key distribution, and exact storage locations out of the app.

### You are done when

Both tests are answered honestly, the legal and technical roles align, and the intended recovery team has completed the process without giving one unintended person enough to spend.


## 8.3 The heir letter and the dead man's switch
*`TEACH + APP` · ~694 words · ~4 min*

**By the end of this lesson, you can:**

- Understand what the heir letter is and who reads it
- Write the first two lines that carry the whole letter
- Follow the never-list of what must never go in the letter
- Prepare the companion executor packet

---

In today's lesson, we're going to write the first page your family reads and build a delivery process that does not contain the secrets.

The heir letter and dead man's switch are operational tools.

They do not appoint an executor, create legal authority, change a beneficiary, transfer ownership, or override a will, trust, provider form, plan document, or court order.

Their job is to help the right person start the right legal and recovery process without improvising.

### The first two lines

The first line says who to call first.

The second line says what not to do.

For example:

"Call the executor and estate attorney before moving any Bitcoin. Do not enter recovery words into a phone, computer, website, chat, or support form."

Those two lines can prevent the most expensive mistake in the entire estate plan.

### What the letter should contain

The letter can state:

- that Bitcoin and other digital assets exist;
- which legal and professional contacts should be called;
- where the legal documents and no-secrets process map are kept;
- which institution or custody provider has an official claim process;
- which role each person has;
- the order of operations;
- what must never be done;
- how to verify a helper through a known channel.

### What the letter must not contain

Do not include:

- wallet backup words or shares;
- private keys;
- passphrases;
- PINs or passwords;
- full account numbers;
- exact secret storage locations;
- an unencrypted descriptor or extended public key when the document may circulate broadly;
- detailed instructions that let any reader bypass the intended control structure.

The letter points to the process. It is not the process and not the secret.

### The custody map

The Family Custody Map names the setup, roles, provider contacts, document locations, and recovery dependencies without recording the secret material.

The heir letter points the family to that map.

The executor packet explains the legal and tax order.

The wallet-specific recovery instructions live in the controlled recovery package appropriate to the setup.

### The dead man's switch

A dead man's switch can send a message after missed check-ins.

It can deliver the heir letter or tell the family where the process documents are.

It should never deliver a wallet backup, private key, passphrase, PIN, or enough information for an unintended recipient to authorize a transaction.

The switch also creates its own failure modes:

- email goes to spam;
- the recipient assumes it is a scam;
- the contact address changed;
- the service fails;
- a false trigger causes the message to arrive while the owner is alive;
- a local-only plan cannot use a cloud delivery feature.

Tell recipients in advance, test the message, and keep a non-automated backup process.

### Digital-account authority

The message can tell the family which accounts exist. It does not create the legal right to access them.

The estate attorney should include the digital-asset and electronic-communications authority required under the governing state's law, and the executor should use provider claim procedures rather than impersonating the owner.

### The family handoff

The handoff meeting covers:

1. why the plan exists;
2. who to contact first;
3. where the legal documents live;
4. where the no-secrets map lives;
5. what not to do;
6. what is still confusing;
7. who owns each follow-up.

No secrets are revealed in the meeting.

### Your decision

Write down who gets contacted first, what they should not do, who receives the message, and how the letter gets delivered if the automatic process fails.

### Put it in orange plan

Protect → Heir letter. Write it in your own words, export it, and store it with the legal documents away from signing material.

In Cloud mode, arm and test the switch. In Local Only mode, document and test the manual delivery process.

### You are done when

The family has received a test message, knows it is legitimate, can find the legal and process documents, and still does not possess any secret merely because the letter exists.


## 8.4 Insurance: term life, disability, umbrella, and when to stop
*`TEACH` · ~976 words · ~6 min*

**By the end of this lesson, you can:**

- Understand insurance as protection you rent until the stack can carry the weight
- Calculate the term-life gap using annual hole × years to cover minus stack
- Identify the four coverage lines that still matter
- Run the graduation review each year

---

In today's lesson, we're going to identify the financial risks the balance sheet cannot absorb yet and build a first-pass insurance review.

This is education, not a quote or policy recommendation. Coverage, underwriting, exclusions, definitions, riders, guarantees, and state rules live in the actual contract.

### The question insurance answers

Insurance transfers a risk that would damage the plan more than the household is willing or able to absorb.

The useful question is not whether a category is good or bad.

It is:

- what event are we transferring;
- how large is the financial loss;
- how long does the exposure last;
- what resources already cover it;
- what does the contract actually promise;
- when can the household absorb the risk itself?

### Life insurance

Life insurance protects the people whose plan depends on the insured person.

A first-pass need can begin with the survivor's annual shortfall multiplied by the years of dependence, then subtract resources that are truly available.

That is not a complete needs analysis.

Also include:

- final expenses;
- debt the survivor intends to eliminate;
- childcare and education commitments;
- survivor Social Security and pensions;
- the survivor's earnings and benefits;
- taxes and asset liquidity;
- inflation and timing;
- investment risk;
- business or estate liquidity;
- existing coverage and its expiration.

The result is a range to review, not the amount the course tells every household to buy.

### Term and permanent are categories, not one product

Term insurance provides death-benefit coverage for a stated period. Many policies have a level premium for a stated guarantee period, but terms differ.

Permanent insurance can combine lifelong death-benefit coverage with cash value and guarantees, subject to charges, surrender terms, policy assumptions, and product design.

Austin can prefer term for the household example because the need is temporary and the family wants a simple death-benefit tool.

The course should not claim that every permanent policy is merely low-yield savings or that Bitcoin replaces every insurance purpose. Estate liquidity, lifelong dependents, business planning, and guarantees can create a different job.

Life-insurance death proceeds are generally excluded from federal income tax, but interest, transfer-for-value, ownership, and estate-tax rules can change the result.

### Disability insurance

Disability insurance protects earned income while the insured is alive.

Do not estimate the benefit from salary alone.

Read the actual certificate or policy for:

- benefit percentage and monthly cap;
- whether benefits are taxable based on who paid premiums and how;
- elimination period;
- benefit period;
- own-occupation, any-occupation, and specialty definitions;
- partial or residual disability;
- offsets for Social Security, workers' compensation, or employer benefits;
- exclusions, limitations, and pre-existing-condition language;
- inflation or future-purchase options.

Compare the expected after-tax benefit with the household's bare-bones spending number and reserve.

The number we are trying to cover is the gap between what the family would need and what the assets and other income could already provide.

### Umbrella liability

Umbrella insurance generally provides excess personal liability above required underlying auto or homeowners limits and may add defense coverage, subject to exclusions and the policy language.

It does not insure every loss, does not repair the household's own property merely because it is an umbrella, and can exclude business, intentional, professional, or other risks.

Do not quote a universal price per million. Price the actual policy after confirming the required underlying limits, covered properties, drivers, rentals, watercraft, business activity, and exclusions.

### Long-term care

Long-term-care risk is the cost of extended help with activities of daily living or cognitive impairment.

The review is not automatically postponed until one age.

Insurability and price can change before the 50s or 60s. The right review trigger includes:

- family caregiving history;
- current health and insurability;
- assets available to self-fund;
- spouse or family support;
- benefit triggers and elimination period;
- home-care and facility preferences;
- inflation protection;
- premium and rate-increase history;
- state partnership rules;
- hybrid and non-insurance alternatives.

The first decision can still be "not now." It should be a dated decision with a reason and a next review trigger.

### Health-sharing is not insurance

A health-sharing membership does not belong in this lesson as a substitute for an insurance contract.

It can be part of the healthcare bridge comparison, but it generally has no legal obligation to pay claims and its member terms control.

Austin's experience can be described as his experience, not as a guarantee about the category.

### When coverage can fall

Coverage can be reviewed downward when the exposure shrinks.

Examples:

- children become independent;
- debts or education commitments are gone;
- the surviving spouse has enough income and liquid assets;
- the household can absorb the liability or long-term-care risk;
- earned income is no longer part of the plan.

Do not cancel or replace an existing policy until any replacement is effective and the consequences of surrender, conversion, taxes, contestability, and new underwriting have been reviewed.

### The coverage audit

For each category, record:

1. the event being transferred;
2. the dollar loss and duration;
3. current coverage;
4. actual contract limits and exclusions;
5. the remaining gap;
6. the next review trigger;
7. who will verify the final recommendation.

### Your decision

Which gaps need a current quote or contract review and which risks the household has deliberately chosen to retain.

### Put it in orange plan

Protect records the review status and unresolved gaps. Do not store policy secrets or pretend the app entry changed the carrier contract.

### You are done when

The rough math is labeled as rough, every policy statement came from the actual contract, and a licensed reviewer can see the exact question instead of being asked to design the whole plan from scratch.


## 8.5 Walkthrough: Protect, the heir letter, and the switch

*`DEMO` · ~2,000 words · ~22 min raw, cut into seven*

> 🎥 **SCREEN SHARE — entire lesson.** Capture segment **8.5** in ONE continuous
> session. The Needs attention queue shortens as you go, and that shrinking list
> is the visual argument of the module. Six `✂ CUT POINT` markers let the edit
> ship it as one video or seven. Beat sheet + required app state:
> SCREEN-SHOOT-LIST.md.
>
> Replaces the retired hybrid captures 8.1-B and 8.3-B. The 8.5-B estate-tax
> beats moved to the Advanced Library with the trust lesson.

**By the end of this lesson, you can:**

- Complete the Protect readiness queue in one sitting
- Assign beneficiaries in the app and mirror them on the custodian's own form
- Confirm your access design against both tests, out loud
- Write and export the heir letter without a single secret in it
- Arm the switch, tell its recipients, and do one check-in
- Read your projected legacy and download the estate summary

---

Companion walkthrough for Module 8, and the module's hand-off target. Eight chapters, filmed as one session: **Protect overview → beneficiaries and executor → confirm the access design → heir letter → dead man's switch → projected legacy and estate summary → the estate-complexity gate → the family handoff review.**

The full DO / SEE / ⚠ sheet lives in `scripts/09-5_WALKTHROUGH_estate.md`.

### The estate-complexity gate replaces the net-worth trust gate

⚠ **Net worth is an input, not the gate.** A family with $400,000, two young kids, a business and a blended household can need more planning than a single person with $3 million and a simple life.

**Triggers:** blended family · minor children · multiple heirs · business ownership · heavy Bitcoin concentration · probate or privacy concerns · incapacity planning · assets or property in more than one state · an advanced custody setup somebody has to operate after you.

| Level | What it is | Typically |
|---|---|---|
| 1 · Basic cleanup | Beneficiary forms, executor asked out loud, a letter | No attorney strictly required |
| 2 · Local estate plan | Will, POA, healthcare directive | Attorney licensed in your state |
| 3 · Trust or coordinated plan | A trust, coordinated with the custody design | Attorney + CPA |
| 4 · Advanced estate, tax and custody planning | Multiple specialists working together | A coordinated team |

The question each level answers is **which one deserves a professional conversation.** Most households land at 1 or 2 and are finished.

✅ **"No" is a finished answer.** *"A basic estate plan is sufficient right now. A trust is not currently indicated."* Recorded with a date, that is a completed decision — next year checks whether a trigger changed rather than starting over.

### The family handoff review

Not in the app. The documents don't work if the family has never heard about them.

⚠ **This meeting is not where secrets get revealed.** No seed words, PINs, passphrases, or device handling. It's where the family learns what exists and how to start.

**Bitcoin Family Handoff Review:** 1. Why this plan exists · 2. Who to contact first · 3. Where the legal documents live · 4. Where the no-secrets access map lives · 5. What not to do · 6. What is still confusing · 7. Who owns each follow-up.

Item 6 earns the meeting — if nobody says anything is confusing, the question was asked wrong. Item 7 stops it being a conversation everyone forgets.

<!-- PLAN-LIFECYCLE:MODULE-8 -->
### Build Your Plan handoff

Return to **Build Your Plan → Protect**. Confirm the beneficiaries exist, the heir letter is drafted in your own words, and the printable or downloaded copy is stored where the family can find it. The app checkmark is not the legal work; provider forms and signed documents remain the record.

<!-- ADVANCED-GATE:START -->

## Related advanced lessons

**Your core plan is complete.** These are optional, and each one is
worth watching only when its condition is true for you. Continue only if
one of these describes your situation:

- **A8.1 Advanced: do you need a trust, and which one?**
  → *Watch this once the **core estate gate in 8.5** has lit up and put you at Level 3 or 4 — a trust or coordinated plan. This lesson does not re-run that gate; it explains the options after it fires. Most households run the gate in 8.5, get a no, and are finished.*

*Generated by `tools/build-module-gates.py` from the Gate line on each
advanced lesson. Edit the condition there, not here.*

<!-- ADVANCED-GATE:END -->
