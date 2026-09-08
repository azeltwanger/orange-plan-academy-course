# Session 8 — Build the family handoff

Four steps: choose the people and legal baseline; coordinate authority with actual custody; write and test the non-secret handoff; identify risks to discuss with an insurance professional. W08 documents and rehearses. Legal instruments and product execution stay outside the app and behind the relevant professional review.

## 8.1 — Choose the people and put the legal baseline in place
Kind: teach
Gate: ESTATE_REVIEW
Sources: ESTATE, ESTATE_DECK, OWNER, PRIMARY

### Read aloud

A family plan needs people who know their roles and documents that give the appropriate authority. Start with incapacity and death as two different situations.

During incapacity, someone may need authority to handle financial decisions while you are alive. A properly prepared financial power of attorney can address that role under the applicable law. Healthcare decisions may require a healthcare agent and advance directive. After death, authority follows the estate, trust, beneficiary, and account processes that apply.

An executor is commonly nominated in a will, but nomination and legal appointment are different steps. The relevant court process and local law determine who can act for the estate. An administrator may be appointed when there is no effective nomination or another circumstance requires it. A power of attorney generally does not continue as authority to act for the person after death.

Choose for trust, capability, availability, and willingness. The person best at technology may not be the best person to coordinate the legal and financial work. You can identify a separate technical helper without giving that person unrestricted legal authority.

Ask the primary person and a backup to accept the role. Explain the scope at a high level. Someone who has never heard about the assignment is not yet part of a practical handoff. Confirm how they would contact the attorney or other professional when needed.

For Alex and Morgan, the first task is reviewing who would make decisions if one spouse were unavailable and who would coordinate after a death. They also need to consider guardianship nominations for the children where appropriate. Those decisions belong with an attorney who understands their jurisdiction and family circumstances.

The baseline documents may include a will, financial power of attorney, healthcare directive, and the account-specific beneficiary designations. A trust may be useful when it solves a defined job, but it is not a prerequisite for every Bitcoin household. The advanced trust lesson explains how to prepare that question.

Beneficiary forms need separate attention. Retirement accounts, life insurance, payable-on-death arrangements, jointly owned property, and trust-owned assets may pass under rules that differ from the will. Do not assume changing the will updates every account. Check primary and contingent beneficiaries directly with each institution.

Also check names, percentages, and the consequences of naming a minor, estate, or trust. Retirement-account beneficiary choices can have tax and distribution consequences. An attorney and tax professional should coordinate complex cases rather than treating a form as a simple address book.

Keep the location of the legal documents understandable to the person who will need them. The course worksheet can record which documents exist, when they were reviewed, the professional contact, and the next action. It should not pretend to create a valid legal instrument or provide the entire confidential file.

Life changes create review triggers: marriage, divorce, a child, a move, a death, a new business, or a significant change in assets. A technically correct old document can become a poor fit for the household that exists today.

In the working session, we will list the roles, confirm the status of the documents and beneficiary forms, and identify the missing professional action. We will not fill a legal gap with a guessed clause or an app checkbox.

Finish knowing who is supposed to act, whether they have agreed, what document or account process supports their role, and which review remains. The next step connects that legal authority to the actual custody methods you chose.

### Production notes

State-licensed attorney review required for jurisdiction-specific claims or instruments. Do not promise a template creates legal authority. Distinguish nomination/court appointment, incapacity/death, probate/non-probate, and beneficiary designation/will. No detailed client estate fact pattern published.

### Member checkpoint

- Choose primary and backup people and ask them to accept.
- Review the status of legal documents and account beneficiary forms.
- Record the specific attorney or tax question needed to close each gap.

## 8.2 — Connect legal authority with the actual recovery process
Kind: teach
Gate: ESTATE_CUSTODY_REVIEW
Sources: ESTATE, CUSTODY, DICTATION, PRIMARY

### Read aloud

A legal document and a technically recoverable wallet solve different parts of the same problem. The person entitled to act must have a usable process, and the person helping with the technology must understand the limits of that role.

Start with each asset's actual arrangement. Personally held Bitcoin, Bitcoin in a retirement account, a brokerage fund, an institutional custody account, and a trust-owned wallet can have different ownership and recovery paths. One set of instructions should not assume all of them work like a hardware wallet.

For direct single-signature custody, whoever has the required signing information may be able to move the Bitcoin. That practical ability is separate from legal entitlement. The handoff needs to manage access without leaving the legitimate process incomplete.

A passphrase is an additional secret used to derive a wallet. It does not turn a single-signature wallet into two legal signers. Dividing recovery words and a passphrase between people can introduce dependence on both components, but the suitability of that arrangement depends on the full design, secure storage, exact recovery, and legal roles. It is one possible design to review, not a universal inheritance rule.

Multisig uses a defined signing threshold. A two-of-three wallet can require two valid keys, together with the configuration needed to identify and use the intended wallet. Decide who controls each signing capability, which combinations can act, how backups are held, and what happens when a person or provider is unavailable.

A provider can help with recovery or administration, but its exact role must be verified. Can the household recover without it? Which documents does it require after incapacity or death? Does it provide technical support only, or does it control assets under an institutional arrangement? What changes if the provider stops operating?

For brokerage and retirement accounts, the institution's beneficiary and estate process governs the account access. Possessing a password is not a substitute for completing that process. Give the family the correct contact and documents rather than instructions to impersonate the owner.

For Alex and Morgan, we will make a non-secret table. Each row names the asset type, legal owner, person or role entitled to direct the process, operational helper or provider, whether the process has been tested, and the next verification. It never includes the signing material itself.

Then test the table under a simple scenario. Alex is unavailable for six months. Can Morgan identify the assets, contact the right professionals, and arrange ordinary household cash flow without improvising access to every Bitcoin holding? Next test a death scenario, where different legal steps apply.

Look for a circular dependency. The instructions may be behind a login controlled by the unavailable person. The password manager may depend on the same lost device as the email. The only technical helper may have moved or lost contact. These are practical failures you can identify before anyone is under stress.

Digital-account authority also deserves legal review. Providers may have online legacy settings and terms governing disclosure of information. Applicable state law and consent documents can affect what a fiduciary may receive. Technical possession of credentials and lawful access are not interchangeable.

The working session records what is known and the exact unanswered questions for the attorney and custody professional. It does not distribute secrets or settle legal title. Finish with an executable starting path for each meaningful pool and a clear plan to test the unresolved parts safely.

### Production notes

Retire the old universal heirs-hold-seed/executor-holds-passphrase instruction. No universal trustee concentration waiver. Explain descriptor/policy as sensitive recovery metadata without claiming it signs. Review digital-account consent against applicable law and provider terms; no instruction to bypass access controls.

### Member checkpoint

- Match each asset's legal owner and authorized role to its real recovery method.
- Identify incomplete or circular dependencies.
- Prepare specific legal and technical questions without storing secrets.

## 8.3 — Write and test the first instructions your family will receive
Kind: teach
Gate: ESTATE_REVIEW
Sources: ESTATE, ESTATE_DECK, DICTATION, OWNER, APP

### Read aloud

The first instructions should help the family slow down, find the right people, and start the documented process. They should be useful to someone who understands less about Bitcoin and the financial plan than you do.

Write the first call clearly. Name the person or professional, their role, and a safe way to verify the contact. Then identify the account and asset categories that exist, the location of the legal documents at an appropriate level, and the process for finding the protected instructions.

Use ordinary language. “There is Bitcoin held through two different arrangements, and this provider can help with one of them” is more useful than assuming the reader understands seed standards, descriptors, or retirement account administration. Technical recovery details belong in the separate protected process reviewed for the actual setup.

Include the mistakes the family should avoid. Never provide recovery words to a website or unsolicited helper. Do not transfer funds because someone creates urgency. Verify contacts independently. Coordinate sales and distributions with the legally authorized person and tax professional. These warnings address real decisions the family may face while distracted or grieving.

Keep seeds, private keys, passphrases, PINs, passwords, exact storage locations, and a complete recovery route out of the ordinary heir letter. A document that is meant to be shared for orientation should not also contain everything required to move the assets.

A separate non-secret executor packet can hold the working inventory: professional contacts, account categories, insurance information, legal-document status, household obligations, the order of first calls, and the current financial-plan summary. That packet supports coordination. It does not replace the will, beneficiary forms, court process, or custody recovery plan.

Make the information available through a path that does not depend entirely on your login. The appropriate paper, encrypted, professional-held, or other arrangement depends on the household. Tell the responsible people that the packet exists and how the starting process works.

A scheduled-delivery or missed-check-in system can provide a communication backstop. Verify the recipients, waiting periods, delivery conditions, and what happens during a false alarm. It should deliver non-secret direction rather than release signing keys. Availability and features depend on the actual service or app release.

For Alex and Morgan, the test is simple. Give Morgan a sample letter and ask, “What would you do first? How would you confirm this contact is genuine? What would you avoid doing?” If the answer is unclear, improve the instructions before adding more pages.

Test the delivery method with a harmless sample. Confirm the message arrives, can be opened, and is recognized. An untested system is still an assumption. Record when it was tested and what needs to be reviewed after a change of address, email, provider, or family role.

In the working session, we will prepare a non-secret letter, export or place it through the supported process, and identify the outside document and delivery tasks. We will not mark a legal or recovery process complete merely because the letter was generated.

Finish with instructions a family member can follow, a packet that can be found, and a tested way to start the right process. Keep it short enough to be usable in a difficult moment, with deeper detail available to the people who actually need it.

### Production notes

Use the safe worksheet letter skeleton; no false claim that generic instructions are attorney-approved. APP capture checks actual heir-letter/export/dead-man-switch availability and mode restrictions; no unverified 90-day default promise. Test-only recipients and messages. Exporting the letter is distinct from delivery proof.

### Member checkpoint

- State the first contact and first actions in plain language.
- Keep secrets separate and make the packet findable.
- Test a harmless delivery and the recipient's understanding.

## 8.4 — Identify the risks you will transfer or carry
Kind: teach
Gate: INSURANCE_REVIEW
Sources: ESTATE, ESTATE_DECK, RETIREMENT, PRIMARY

### Read aloud

Insurance planning starts with the financial loss the household would struggle to carry. The Reserve handles some smaller shocks. Larger losses can require a different combination of coverage, assets, and contingency planning.

Start with life insurance. If one person dies, what income disappears and what costs remain? Include debt, childcare, education commitments, final expenses, taxes, and the surviving household's spending. Also account for survivor benefits, the spouse's income, existing coverage, and assets that are actually available.

A first-pass example might identify forty thousand dollars a year of temporary survivor funding for ten years. That is four hundred thousand before inflation, investment returns, timing, and other needs. It is a scale estimate, not a policy recommendation. The actual amount needs a fuller review, including how much risk the family can retain.

Term coverage and permanent coverage have different purposes, costs, and contract features. Compare the job the policy is meant to solve, the period coverage is needed, premiums, guarantees, exclusions, and flexibility. A product should not be selected solely because of a slogan about investing the difference or borrowing against cash value.

Disability coverage addresses the loss of earning ability while living. Read the definition of disability, benefit amount and cap, waiting period, duration, exclusions, offsets, and whether benefits are taxable under the arrangement. A quoted percentage of salary may be reduced by a monthly cap or other terms. Variable and self-employed income can need particular attention.

Liability risk deserves a separate look. Home and auto policies have liability limits and exclusions. An umbrella policy may provide additional coverage above required underlying limits, subject to its terms. Review the actual risks, underlying policies, business activities, and coverage gaps with a licensed professional.

Later-life care can place a substantial burden on family and assets. Options may include retaining the risk, traditional coverage, hybrid products, or other arrangements. Eligibility, underwriting, benefit triggers, inflation features, premium history, and contract guarantees matter. The household should review the decision while there are practical choices rather than assume a future policy will always be available.

Healthcare before Medicare was addressed in the retirement-paycheck session. Keep that coverage choice connected to this broader risk review without duplicating the same costs. Non-insurance alternatives need their own clear treatment of the financial risk the household retains.

For Alex and Morgan, the worksheet begins with existing policies and employer benefits. They identify what would happen if either income stopped, one spouse died, a large liability claim occurred, or long-term care became necessary. They then list the gaps and questions for the appropriate professional. They do not buy one of every policy just to fill a checklist.

Be careful when replacing coverage. The new arrangement must be reviewed and effective before an existing policy is canceled when continuous protection is needed. Health, age, underwriting, exclusions, and waiting periods can make an apparently simple replacement difficult or irreversible.

The app may record parts of the protection plan, but the policy contract governs the coverage. Store the necessary non-secret summary and contact information where the family can start the process. Keep original policy documents privately available.

Finish with a short risk decision for each material category: covered and verified, intentionally retained, or requiring a specific review. That gives the household a practical protection plan rather than a list of products it feels pressured to buy.

### Production notes

Licensed insurance review required for contract mechanics and the worksheet. No universal coverage multiple, premium estimate, or medical underwriting promise. Term/permanent and disability definitions are educational comparisons, not recommendations. The first-pass survivor arithmetic is illustrative and explicitly incomplete as a full needs analysis.

### Member checkpoint

- Inventory current coverage and the risks the household retains.
- Identify material gaps and contract questions.
- Verify replacement coverage before canceling an arrangement needed for continuity.
