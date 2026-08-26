from __future__ import annotations

from textwrap import dedent


def b(text: str) -> str:
    return dedent(text).strip() + "\n"


FILES = {
"scripts/08-1_the-executor-the-four-legal-documents-an.md": b(r'''
TELEPROMPTER SCRIPT — segment 8.1
8.1 The executor, the four legal documents, and choosing an estate attorney
~10 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to build the legal and human layer around the custody process.

This module is US-specific and state-specific. The course can teach the jobs the documents perform. An attorney licensed in the governing state has to draft and supervise the actual plan.

== NOMINATION IS NOT APPOINTMENT ==

A will usually nominates the person you want to serve as executor and directs the probate assets.

The executor generally receives legal authority through the court process after death. Before appointment, the nominee may have very limited power to act.

If there is no valid will, the court can appoint an administrator under the state's intestacy rules.

So the problem with no will is not that nobody can ever receive authority. The problem is that state default rules and a court process choose the path instead of the plan you wrote.

== DOCUMENT ONE: THE WILL ==

The will directs probate assets, nominates the executor, and can nominate a guardian for minor children.

A guardian nomination is not an automatic appointment. The court makes the final decision under state law.

The will does not control every asset. A valid beneficiary, payable-on-death, transfer-on-death, trust, joint-ownership, or retirement-plan arrangement may transfer outside the will.

That is why the estate plan is a coordinated system rather than one document.

== DOCUMENT TWO: FINANCIAL POWER OF ATTORNEY ==

A financial power of attorney authorizes an agent to act during life under the terms of the document.

It is an incapacity and lifetime-management tool. It generally ends at death.

The document should address digital assets and the accounts the agent may need to manage, subject to the state's law and provider terms.

== DOCUMENT THREE: HEALTHCARE DIRECTIVE ==

A healthcare directive and healthcare power name who makes medical decisions and record the owner's wishes when the owner cannot communicate.

This is not an inheritance document. Its job ends where the executor and post-death plan begin.

== DOCUMENT FOUR: TRANSFER AND ACCESS RECORDS ==

Beneficiary, POD, TOD, and retirement-plan designations can transfer the covered asset outside the will.

A valid provider-held designation generally controls that account, but "generally" matters.

Plan terms, ERISA, spousal consent, QDROs, community-property rules, state law, and an invalid or outdated designation can change the result.

Orange Plan records intent. The provider holds the binding account record.

The fourth category also includes the digital-asset authority language the legal documents need.

Many states follow a version of the Revised Uniform Fiduciary Access to Digital Assets Act. Access to an account and access to the content of electronic communications can be treated differently, and explicit consent may be required.

Ask the attorney to address digital assets and electronic communications directly rather than relying on a generic property clause.

== THE EXECUTOR IS A PERSON, NOT A NAME IN A FIELD ==

Ask the person before naming them.

They should understand:

- that the role exists;
- who the attorney and tax professional are;
- where the legal documents and no-secrets process map are kept;
- what not to do with Bitcoin;
- that they may need court appointment before acting;
- that they never need the wallet backup merely to begin the legal process.

The executor does not need every signing secret. They need authority, process, and the right people.

== LEGAL AUTHORITY AND TECHNICAL CONTROL ARE DIFFERENT ==

A person can be legally authorized and unable to sign.

A person can hold enough signing material and have no legal authority to use it.

A good estate plan aligns those two systems.

The will, trust, or court order governs authority. The custody design governs what can technically authorize a transaction. The heir letter and custody map explain how to start. None replaces the others.

== BENEFICIARY REVIEW ==

For each retirement account, insurance policy, brokerage account, bank account, and provider that supports a designation:

1. read the current provider record;
2. confirm the primary and contingent beneficiaries;
3. confirm percentages and per-stirpes or similar choices when available;
4. check spouse-consent and plan-document rules;
5. save evidence of the review without storing account secrets in the course tools;
6. coordinate the designation with the will and trust plan.

Do not assume an entry in Orange Plan changed the provider's record.

== CHOOSING THE ATTORNEY ==

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

== THE EXECUTOR PACKET ==

The Executor Packet is an operational briefing, not a legal instrument.

It can explain the first week, contact list, account inventory, tax order, and Bitcoin safety rules.

It cannot appoint the executor, change a beneficiary, authorize access to an account, or override a court order.

Use it to brief the person the legal documents nominate.

== YOUR DECISION ==

Who will be nominated, whether they have accepted, and which state-licensed attorney will draft and coordinate the documents.

== PUT IT IN ORANGE PLAN ==

Protect records the completion status, beneficiaries as intent, emergency contacts, and the family process.

Do not store seeds, private keys, passphrases, PINs, account passwords, full account numbers, or exact recovery locations.

== YOU ARE DONE WHEN ==

The executor has accepted, the provider-held beneficiary records were reviewed, the attorney has the digital-asset questions, and every operational document is clearly labeled as process rather than legal authority.
'''),

"scripts/08-2_split-access-dual-control-and-redundancy.md": b(r'''
TELEPROMPTER SCRIPT — segment 8.2
8.2 Split access: dual control and redundancy
~10 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to test whether one person can spend alone and whether one loss can permanently block recovery.

Those are different failures.

Dual control answers the first. Redundancy answers the second.

== TEST ONE: CAN ONE PERSON SPEND ALONE? ==

If one person, one backup, or one account credential can authorize the whole balance, the setup fails the dual-control test.

That may be an accepted trade in a simple single-signature wallet. It should not be described as if two people are required when they are not.

== TEST TWO: CAN ONE LOSS STOP RECOVERY? ==

If one missing device, backup, passphrase, person, provider, or wallet policy can permanently stop recovery, the setup fails the redundancy test.

A system can pass one test and fail the other.

One seed copied into three locations is redundant against one location loss, but every copy is still sufficient to spend.

A mnemonic and passphrase stored apart can prevent either item alone from deriving the intended passphrase wallet, but losing either can block recovery. That is operational two-part access, not on-chain multisig.

A 2-of-3 multisig can pass both tests when any two keys work, one cannot spend, one can be lost, and the policy/descriptor is recoverable.

== LEVEL 1: INSTITUTIONAL CONTROL ==

At Level 1, the institution controls signing.

The household's dual-control and redundancy questions are delegated to the provider's controls, beneficiary record, account recovery, and death-claim process.

Verify what the provider actually requires. Do not assume an institution's legal process works like a wallet recovery.

== LEVEL 2: SINGLE-SIGNATURE CONTROL ==

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

== LEVEL 3: PASSPHRASE SEPARATION ==

A passphrase wallet can separate the mnemonic and exact passphrase.

Each element needs its own backup and recovery path.

The standard no-passphrase wallet still exists. Whether it is empty, a decoy, or used for another purpose is deliberate.

This design can reduce the risk of one found backup revealing the intended wallet. It also creates an all-parts-required recovery unless the household adds redundancy on both sides.

Test the exact intended wallet. Every passphrase typo derives another valid wallet.

== LEVEL 4: MULTISIG ==

A 2-of-3 wallet requires two signing keys.

To recover it, the family also needs the wallet policy or descriptor and compatible software.

The descriptor cannot spend. Storing it with a key does not change the 2-of-3 threshold.

It is still privacy-sensitive and should be backed up in places the intended recovery team can reach.

Distribute keys across independent failure domains and test the combinations the family plan depends on.

== LEGAL ROLE VERSUS KEY ROLE ==

Executor, trustee, heir, guardian, provider, and signing-key holder are not interchangeable roles.

The legal documents decide who is authorized to act. The signing policy decides who can technically authorize a Bitcoin transaction.

A key holder may need to sign under an executor's or trustee's legal instruction. A legally authorized person may need help from the threshold key holders.

Write both maps and make sure they agree.

== THE FAMILY MEETING ==

The meeting teaches:

- who calls the attorney first;
- where the legal documents and no-secrets map live;
- which people hold roles;
- which action requires another person;
- what nobody should ever reveal or improvise.

It does not reveal the backup, passphrase, PIN, or exact key locations to everyone in the room.

== YOUR DECISION ==

Which of the two tests the setup passes, which one it fails, and whether the accepted failure is still appropriate for the current amount and family.

== PUT IT IN ORANGE PLAN ==

Protect records the level, recovery-test status, and process completion.

The secret distribution stays off-app.

== YOU ARE DONE WHEN ==

Both tests are answered honestly, the legal and technical roles align, and the intended recovery team has completed the process without giving one unintended person enough to spend.
'''),

"scripts/08-3_the-heir-letter-and-the-dead-mans-switch.md": b(r'''
TELEPROMPTER SCRIPT — segment 8.3
8.3 The heir letter and the dead man's switch
~8 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to write the first page your family reads and build a delivery process that does not contain the secrets.

The heir letter and dead man's switch are operational tools.

They do not appoint an executor, create legal authority, change a beneficiary, transfer ownership, or override a will, trust, provider form, plan document, or court order.

Their job is to help the right person start the right legal and recovery process without improvising.

== THE FIRST TWO LINES ==

The first line says who to call first.

The second line says what not to do.

For example:

"Call the executor and estate attorney before moving any Bitcoin. Do not enter recovery words into a phone, computer, website, chat, or support form."

Those two lines can prevent the most expensive mistake in the entire estate plan.

== WHAT THE LETTER SHOULD CONTAIN ==

The letter can state:

- that Bitcoin and other digital assets exist;
- which legal and professional contacts should be called;
- where the legal documents and no-secrets process map are kept;
- which institution or custody provider has an official claim process;
- which role each person has;
- the order of operations;
- what must never be done;
- how to verify a helper through a known channel.

== WHAT THE LETTER MUST NOT CONTAIN ==

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

== THE CUSTODY MAP ==

The Family Custody Map names the setup, roles, provider contacts, document locations, and recovery dependencies without recording the secret material.

The heir letter points the family to that map.

The executor packet explains the legal and tax order.

The wallet-specific recovery instructions live in the controlled recovery package appropriate to the setup.

Three documents, three jobs.

== THE DEAD MAN'S SWITCH ==

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

== DIGITAL-ACCOUNT AUTHORITY ==

The message can tell the family which accounts exist. It does not create the legal right to access them.

The estate attorney should include the digital-asset and electronic-communications authority required under the governing state's law, and the executor should use provider claim procedures rather than impersonating the owner.

== THE FAMILY HANDOFF ==

The handoff meeting covers:

1. why the plan exists;
2. who to contact first;
3. where the legal documents live;
4. where the no-secrets map lives;
5. what not to do;
6. what is still confusing;
7. who owns each follow-up.

No secrets are revealed in the meeting.

== YOUR DECISION ==

The first contact, the first prohibited action, the recipients, and the backup delivery method if automation fails.

== PUT IT IN ORANGE PLAN ==

Protect → Heir letter. Write it in your own words, export it, and store it with the legal documents away from signing material.

In Cloud mode, arm and test the switch. In Local Only mode, document and test the manual delivery process.

== YOU ARE DONE WHEN ==

The family has received a test message, knows it is legitimate, can find the legal and process documents, and still does not possess any secret merely because the letter exists.
'''),

"scripts/08-4_insurance-term-life-disability-umbrella-.md": b(r'''
TELEPROMPTER SCRIPT — segment 8.4
8.4 Insurance: term life, disability, umbrella, and when to stop
~9 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · see research/PRIMARY-SOURCE-REGISTER.md
============================================================

In today's lesson, we're going to identify the financial risks the balance sheet cannot absorb yet and build a first-pass insurance review.

This is education, not a quote or policy recommendation. Coverage, underwriting, exclusions, definitions, riders, guarantees, and state rules live in the actual contract.

== THE QUESTION INSURANCE ANSWERS ==

Insurance transfers a risk that would damage the plan more than the household is willing or able to absorb.

The useful question is not whether a category is good or bad.

It is:

- what event are we transferring;
- how large is the financial loss;
- how long does the exposure last;
- what resources already cover it;
- what does the contract actually promise;
- when can the household absorb the risk itself?

== LIFE INSURANCE ==

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

== TERM AND PERMANENT ARE CATEGORIES, NOT ONE PRODUCT ==

Term insurance provides death-benefit coverage for a stated period. Many policies have a level premium for a stated guarantee period, but terms differ.

Permanent insurance can combine lifelong death-benefit coverage with cash value and guarantees, subject to charges, surrender terms, policy assumptions, and product design.

Austin can prefer term for the household example because the need is temporary and the family wants a simple death-benefit tool.

The course should not claim that every permanent policy is merely low-yield savings or that Bitcoin replaces every insurance purpose. Estate liquidity, lifelong dependents, business planning, and guarantees can create a different job.

Life-insurance death proceeds are generally excluded from federal income tax, but interest, transfer-for-value, ownership, and estate-tax rules can change the result.

== DISABILITY INSURANCE ==

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

The gap—not the salary—is the planning result.

== UMBRELLA LIABILITY ==

Umbrella insurance generally provides excess personal liability above required underlying auto or homeowners limits and may add defense coverage, subject to exclusions and the policy language.

It does not insure every loss, does not repair the household's own property merely because it is an umbrella, and can exclude business, intentional, professional, or other risks.

Do not quote a universal price per million. Price the actual policy after confirming the required underlying limits, covered properties, drivers, rentals, watercraft, business activity, and exclusions.

== LONG-TERM CARE ==

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

== HEALTH-SHARING IS NOT INSURANCE ==

A health-sharing membership does not belong in this lesson as a substitute for an insurance contract.

It can be part of the healthcare bridge comparison, but it generally has no legal obligation to pay claims and its member terms control.

Austin's experience can be described as his experience, not as a guarantee about the category.

== WHEN COVERAGE CAN FALL ==

Coverage can be reviewed downward when the exposure shrinks.

Examples:

- children become independent;
- debts or education commitments are gone;
- the surviving spouse has enough income and liquid assets;
- the household can absorb the liability or long-term-care risk;
- earned income is no longer part of the plan.

Do not cancel or replace an existing policy until any replacement is effective and the consequences of surrender, conversion, taxes, contestability, and new underwriting have been reviewed.

== THE COVERAGE AUDIT ==

For each category, record:

1. the event being transferred;
2. the dollar loss and duration;
3. current coverage;
4. actual contract limits and exclusions;
5. the remaining gap;
6. the next review trigger;
7. who will verify the final recommendation.

== YOUR DECISION ==

Which gaps need a current quote or contract review and which risks the household has deliberately chosen to retain.

== PUT IT IN ORANGE PLAN ==

Protect records the review status and unresolved gaps. Do not store policy secrets or pretend the app entry changed the carrier contract.

== YOU ARE DONE WHEN ==

The rough math is labeled as rough, every policy statement came from the actual contract, and a licensed reviewer can see the exact question instead of being asked to design the whole plan from scratch.
'''),

"scripts/advanced/A8-1_advanced-do-you-need-a-trust-and-which-o.md": b(r'''
TELEPROMPTER SCRIPT — segment A8.1
A8.1 Advanced: do you need a trust, and which one?
~11 min at 155 wpm · SPOKEN-PROSE VERSION (calibrated)
RESEARCH AUDIT: 2026-08-25 · general research complete; state-specific attorney signoff required before publication
============================================================

In today's lesson, we're going to decide whether the estate plan has a problem that deserves a trust conversation.

We are not going to diagnose a trust from net worth, Bitcoin conviction, or one checkbox.

A trust is a fiduciary relationship governed by a legal instrument. The trustee holds or administers property for beneficiaries under those terms.

Calling it a container can be useful shorthand, but ownership, control, tax treatment, creditor rights, and fiduciary duties depend on the actual document and state law.

== THE GATE IS A CONVERSATION TRIGGER ==

The core module names complexity triggers:

- minor or vulnerable beneficiaries;
- blended family or conflicting beneficiary groups;
- business ownership;
- property in more than one state;
- privacy or probate concerns;
- incapacity planning;
- a custody setup another person must operate;
- a potentially taxable estate;
- a concentrated asset a fiduciary may be asked to retain.

One trigger does not mechanically mean a trust is required.

It means the attorney conversation has a real question to solve.

== REVOCABLE LIVING TRUST ==

A revocable living trust can support incapacity management and can avoid probate for assets properly titled or assigned to it.

Signing a trust does not move every asset into it. An unfunded trust does not avoid probate for property that still passes through the probate estate.

A revocable trust generally remains within the grantor's control and estate. It usually does not create federal estate-tax savings merely because the title includes the word trust.

Privacy can improve because a trust instrument is not automatically filed like a probated will, but administration, litigation, beneficiary rights, and state law can still expose information.

== IRREVOCABLE TRUST ==

An irrevocable trust can change ownership, control, estate inclusion, income taxation, creditor exposure, and basis.

None of those results happens automatically.

The effect depends on:

- whether the transfer was completed;
- which powers the grantor retained;
- who can benefit;
- whether the trust is a grantor trust for income tax;
- withdrawal or substitution powers;
- creditor-access rules;
- the governing state;
- gift and generation-skipping consequences;
- whether the property remains in the taxable estate for basis purposes.

Do not use "irrevocable" as a synonym for "outside the estate" or "protected from creditors."

== TAXABLE ESTATE VERSUS SUCCESSION PROBLEM ==

The first attorney question is what problem the household has.

A succession problem can exist at modest wealth: minor children, a special-needs beneficiary, a blended family, a business, or a complicated custody process.

An estate-tax problem depends on current federal and state law, ownership, deductions, prior gifts, and future values.

A fast-growing asset can make future estate exposure worth modeling. It does not by itself tell you to give up control today.

Model at least two defensible growth cases, then ask the attorney and CPA which ownership structures preserve the plan's tax and basis goals.

== BITCOIN OWNERSHIP AND THE KEY PLAN ==

The legal owner and the signing policy have to match.

If a trust owns Bitcoin but the trustee has no practical way to carry out authorized transactions, the document and custody plan are misaligned.

If one trustee holds enough signing material to act alone, the household may have recreated the single-person risk the custody module tried to remove.

Multisig can distribute technical signing power, but one key does not automatically define legal control.

The trust instrument should state the trustee's authority and duties. The wallet policy should state the technical threshold. The recovery map should show how the authorized team can act. Those three layers must agree.

== THE PRUDENT-INVESTOR ISSUE ==

Most states follow some form of prudent-investor law.

The general framework evaluates the portfolio as a whole and ordinarily favors diversification unless the governing instrument, purposes, circumstances, or state law support another approach.

A trustee asked to hold a concentrated Bitcoin position needs explicit, state-specific planning.

There is not one universal sentence called "the Bitcoin waiver" that solves every state and every trust.

The attorney should consider the tools available in that jurisdiction, which may include:

- express authority to retain or concentrate in a named asset;
- modification of the diversification duty;
- a directed-trust structure;
- a special trustee, trust protector, or investment adviser;
- trustee selection based on willingness and competence;
- consent, release, accounting, or exculpation procedures allowed by law;
- a process for liquidity, taxes, distributions, and rebalancing.

The correct question is:

"How will this trust authorize and protect a fiduciary who is expected to retain concentrated Bitcoin, and what limits still cannot be waived under this state's law?"

== THE BASIS TRADE-OFF ==

Inherited property generally receives a date-of-death basis under current federal law.

Property transferred during life, property excluded from the estate, and property in different trust structures can have different basis consequences.

A strategy that reduces estate tax can create more capital-gain exposure, and the reverse can also be true.

That is why the estate attorney and CPA model the ownership and basis result together.

== THE COUPLE'S RESULT ==

The couple has minor children and concentrated Bitcoin, so the conversation is real.

The course cannot conclude from those facts alone that a revocable trust, irrevocable trust, or attorney-supervised will is definitely the right answer.

The output is a scoped attorney question:

- how should assets be held for the children;
- who has authority during incapacity and after death;
- which assets avoid probate already;
- whether a funded revocable trust improves administration;
- whether future estate exposure justifies advanced planning;
- how the custody threshold and fiduciary roles should align.

"Trust not currently indicated" can still be a finished answer after that review.

== WHAT TO REMOVE FROM THE DECISION ==

Do not choose a trust because:

- someone said every homeowner needs one;
- Bitcoin might go up;
- a trust sounds more private;
- an online form says the estate is complex;
- one generic irrevocable-trust benefit sounds attractive;
- a provider wants the structure to fit its custody product.

Choose only after the legal, tax, custody, and family jobs are named.

== READ IT IN ORANGE PLAN ==

Protect → Projected legacy shows a planning estimate under the saved baseline.

Use it to identify whether the estate may cross a current federal or state planning line under assumptions you would defend.

The app does not establish legal domicile, determine a filing-status-specific exemption, draft a trust, transfer title, or prove that a fiduciary duty has been modified.

Change an assumption only as a scenario or temporary read, then return it to the saved baseline.

== HOMEWORK ==

1. Run the core complexity triggers and write the actual problem, not a trust type.
2. Read the projected after-tax estate under at least two defensible growth paths.
3. Inventory which assets pass by beneficiary form, joint ownership, will, or current trust.
4. Take the digital-asset, basis, fiduciary-retention, and custody-policy questions to a state-licensed estate attorney and the tax questions to the CPA.
5. Record the dated result, including "no trust currently indicated."

You are done when the household knows the problem the trust would solve, the ownership and key plan agree, and no one has treated a generic trust label as the answer.
'''),

"lesson-text/08-1_executor-documents-attorney.md": b(r'''
# The executor, the legal documents, and choosing an estate attorney

A will nominates an executor and directs probate assets. Authority generally begins after court appointment. Without a valid will, a court may appoint an administrator under intestacy law.

## Jobs

- **Will:** probate assets, executor nomination, guardian nomination; the court makes appointments.
- **Financial power of attorney:** lifetime/incapacity authority; generally ends at death.
- **Healthcare directive:** medical decisions, not inheritance.
- **Beneficiary/POD/TOD and plan records:** generally transfer the covered asset outside the will, subject to plan terms, ERISA, spousal consent, QDROs, state law, and validity.
- **Digital-asset authority:** state law may require explicit consent for digital assets and electronic-communications content.

The executor packet is operational, not legal authority. Orange Plan records intent; provider forms and valid legal documents control.

**Complete when:** the executor has accepted, provider-held beneficiary records were reviewed, and a state-licensed attorney has the digital-asset and custody questions.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/08-2_split-access-dual-control-and-redundancy.md": b(r'''
# Split access: dual control and redundancy

- **Dual control:** one person or item cannot authorize the whole spend.
- **Redundancy:** one loss cannot permanently block recovery.

A single-signature backup copied three times is redundant by location but every copy can still spend. A passphrase creates two required recovery elements but is not on-chain multisig. A tested 2-of-3 policy can pass both tests when the policy/descriptor is recoverable.

The course no longer prescribes one universal Level 2 holder arrangement. For a single-signature wallet, record who can technically recover, who is legally authorized, how copies are protected, whether one-person spending is accepted, and the trigger for moving to a different design.

Legal roles and key roles must agree. The descriptor cannot sign and does not change the multisig threshold.

**Complete when:** both tests are answered honestly and the intended recovery team has tested the process without giving one unintended person enough to spend.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/08-3_heir-letter-and-dead-mans-switch.md": b(r'''
# The heir letter and the dead man's switch

The heir letter, custody map, executor packet, and dead man's switch are operational tools. They do not appoint anyone, create legal authority, change a beneficiary, or override a will, trust, provider form, plan document, or court order.

## Letter content

Include who to call, where the legal and no-secrets process documents live, role names, order of operations, and what not to do.

Never include wallet backups, private keys, passphrases, PINs, passwords, full account numbers, exact secret locations, or enough recovery detail for any reader to bypass the intended control structure.

## Switch

Deliver the letter or document-location instructions only. Tell recipients in advance, test the message, and keep a manual backup process. The message does not create account access; provider and legal procedures still apply.

**Complete when:** the family recognizes the test message, can find the process documents, and still possesses no secret merely because the letter exists.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/08-4_insurance-term-life-disability-umbrella-.md": b(r'''
# Insurance: term life, disability, umbrella, and when to stop

Insurance transfers a loss the household cannot or does not want to absorb.

## Life

Shortfall × years minus available resources is a first-pass range, not a complete needs analysis. Also include final expenses, debt payoff, childcare/education, survivor benefits and income, taxes, inflation, asset liquidity, business/estate needs, and existing coverage.

Term and permanent are broad categories with different guarantees, charges, and jobs. Death proceeds are generally excluded from federal income tax, subject to exceptions.

## Disability

Read the actual policy for benefit percentage and cap, tax treatment, elimination and benefit periods, own/any occupation, partial/residual benefits, offsets, and exclusions. Compare the after-tax benefit with bare-bones spending.

## Umbrella

Excess personal liability subject to required underlying limits and exclusions. Price the actual policy; there is no universal price per million.

## Long-term care

Review from health, insurability, assets, caregiving exposure, benefit triggers, elimination period, inflation protection, rate history, and alternatives—not one universal age.

Never cancel or replace coverage before the new arrangement is effective and reviewed.

**Complete when:** the rough math is labeled, contract terms came from the policy, and exact gaps go to a licensed reviewer.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),

"lesson-text/advanced/A8-1_trusts.md": b(r'''
# Advanced: do you need a trust, and which one?

A trust is a fiduciary relationship governed by its instrument. It is not a generic container that automatically changes tax, creditor, probate, or basis results.

## Revocable

Can support incapacity and avoid probate for assets properly titled or assigned to it. It generally remains in the grantor's estate and does not create estate-tax savings merely by existing.

## Irrevocable

Estate inclusion, control, income tax, creditor rights, basis, and gift consequences depend on the completed transfer, retained powers, beneficiaries, terms, and state law. “Irrevocable” does not automatically mean outside the estate or protected.

## Gate

Minor/vulnerable beneficiaries, blended family, business, multi-state property, incapacity, probate/privacy concerns, a complicated custody setup, potential estate tax, or concentrated assets can justify an attorney conversation. They do not mechanically diagnose a trust type.

## Concentrated Bitcoin

Prudent-investor law generally favors portfolio-level prudence and diversification, subject to the instrument and state law. Ask which state-specific tools authorize and protect concentrated retention: express retention authority, diversification modification, directed trust, special trustee/protector, trustee selection, consent/release, or another available structure.

One multisig key does not automatically solve legal control. Trust authority, wallet threshold, and recovery process must agree.

## Complete when

The household can name the problem a trust would solve, model estate and basis consequences with the CPA, and record the state attorney's dated answer—including “no trust currently indicated.”

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
'''),
}
