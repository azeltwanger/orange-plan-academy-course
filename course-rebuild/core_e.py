CORE = {
    "8.1": {
        "title": "Choose who is in charge and put the legal baseline in place",
        "source": "Estate deck, detailed Module 8 outline, and the state-law research audit",
        "body": r"""
The custody module made sure the Bitcoin can be reached. Estate planning makes sure the right person has the legal authority to act and the family knows where to start.

The first decision is who will be in charge.

The executor is the person who carries out the instructions after death. Depending on the documents and the state, other roles may handle assets held in a trust or act during incapacity. The title matters less than choosing people who can actually do the job and making sure the documents give them the authority they need.

I would judge an executor on three things: capability, availability, and trust.

Capability means they can follow a legal and financial process, keep records, work with professionals, and avoid making rushed decisions.

Availability means they have the time and willingness. Somebody can be trustworthy and still be the wrong choice because the role would be too much for them.

Trust means they will act in good faith when the family is under pressure.

Pick for the job, not for who would be flattered to be asked. Then ask the person. An executor who has never heard about the role is not part of a working plan yet.

A nontechnical executor can still be a good executor. They do not have to know how to recover a wallet personally. They need a clear process, the right legal authority, and a named technical or custody contact when the setup requires one.

🎬 VISUAL — Estate deck: Capable / Available / Trustworthy, with professional executor as the alternative.

The baseline legal work usually includes four areas.

A will directs how probate assets should be handled and names important roles. It does not control every asset automatically.

A financial power of attorney can give somebody authority to handle financial matters while you are alive but unable to act. That authority generally ends at death, which is why it is not a replacement for the executor or trustee role.

A healthcare directive covers medical decisions and wishes.

Beneficiary designations direct certain accounts or policies outside the will. Retirement accounts and life-insurance policies are common examples. The exact legal effect depends on the account and state, but the practical rule is simple: beneficiary forms need to agree with the overall estate plan and be reviewed after major life changes.

Digital-asset authority matters too. A document can name an executor without necessarily giving the person every permission needed to access online accounts or digital records. Ask the attorney how the state's digital-asset law and the account agreements affect the plan.

The documents and the custody process have to match.

A will cannot move Bitcoin if nobody can recover the wallet. A seed phrase does not give somebody lawful authority to take the asset. Legal authority and technical capability are two separate layers, and the plan needs both.

I would start with the baseline even if the estate is not large. A simple plan that exists and is properly executed is more useful than an advanced trust design that never gets finished.

Trusts are an advanced decision. They may be useful for probate avoidance, incapacity planning, family control, asset protection, tax planning, or a complicated family situation. They are not automatically required because somebody owns Bitcoin, and a revocable trust is not automatically an estate-tax solution.

If the baseline is straightforward, a local estate-planning attorney who is willing to coordinate with the custody process may be enough.

When interviewing the attorney, I would ask:

- Have you planned for clients who hold direct Bitcoin or multisig, not only an exchange account?
- How will the documents give the right people authority without putting secrets into the legal file?
- How should the executor, trustee, custody provider, and technical helper work together?
- What beneficiary forms or account titles need to change?
- What state-specific signing, witnessing, or probate rules apply?
- If a trust may hold concentrated Bitcoin, how will the trustee's duties and the investment language be handled under this state's law?

That last question is not solved by copying one waiver sentence from the internet. Trustee duties and the ability to hold a concentrated asset depend on the governing law, the trust language, and the facts. That is an attorney drafting issue.

Before moving on, choose the primary person and backup you would trust to run the process. Confirm whether they are willing. Then list which of the baseline documents and beneficiary reviews are already complete and which still need an appointment.

The next lesson connects that legal layer to the technical custody setup without pretending there is one universal way to split seeds, passphrases, or keys.
""",
    },
    "8.2": {
        "title": "Align legal authority with the technical recovery path",
        "source": "Estate access-split deck, corrected by the custody and legal research audit",
        "body": r"""
This lesson is about making sure the legal plan and the custody plan lead to the same outcome.

I do not want to give you one universal formula such as "the heirs hold the seed and the executor holds the passphrase." That can work in a carefully designed and tested plan, but it can also create new failure points or give the wrong person practical control.

The right structure depends on the custody method, the people involved, the legal roles, and what each component can actually do.

Start with the principle: no unnecessary person should hold enough information or authority to act alone, but the family must still have a complete, tested recovery path when the proper conditions are met.

With ordinary single-signature custody, anyone who obtains the seed can usually recover that wallet. If a BIP39 passphrase is also used, the seed without the exact passphrase opens a different wallet. The passphrase is not a second signer and it does not create legal dual control. It is another secret that must be recovered exactly.

Splitting those two objects between people can reduce one-person access in some designs, but it can also mean one lost memory, one unavailable person, or one family dispute locks everybody out. It should only be used when the full recovery has been tested and the attorney understands who has legal authority to combine the components.

Do not split a recovery phrase itself into arbitrary word groups and hand the pieces to different people. That creates fragile backups, can reduce security in ways people do not expect, and is not a substitute for a designed secret-sharing or multisig system.

With multisig, the structure is different.

A two-of-three wallet requires two valid signatures from the defined keys. One key alone cannot spend. That can create real operational separation, but the keys are not the entire recovery plan.

The wallet descriptor or configuration records how the keys are combined, including the threshold and derivation information. Without the correct configuration, heirs may struggle to reconstruct the intended wallet even if they have key material.

🎬 VISUAL — Two separate diagrams: passphrase single-sig and 2-of-3 multisig. Show what each component can and cannot do. Do not label a passphrase as a second signer.

A collaborative custody provider may hold one key, a copy of the public wallet configuration, and an established recovery process. The value is not only the third key. It is also the support, identity-verification, continuity, and documented procedure. The trade-off is vendor dependence, fees, privacy considerations, and the need to understand what happens if the company changes or disappears.

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

The system should be tested at the process level while you are alive. You do not need to expose a real seed to the family. You can use a trivial-value test wallet or a documented tabletop exercise to confirm everybody knows the first call, the role they have, and the components that exist.

The plan should also account for change. Hardware wallets fail. Providers merge or close. Executors age. Families move. A custody design that works today can become unusable if it is never reviewed.

The deliverable is not a diagram that looks sophisticated. It is a tested path where the legally authorized people can recover the asset, one ordinary failure does not destroy the plan, and no secret is stored in the app or legal documents.

The heir letter in the next lesson tells the family how to start without disclosing the components themselves.
""",
    },
    "8.3": {
        "title": "Write the heir letter and create the communication backstop",
        "source": "Estate deck heir-letter and dead-man-switch flow, updated for the no-secrets rule",
        "body": r"""
The heir letter is the calm starting point your family receives when they are least prepared to solve a technical and financial problem.

It is not the will. It is not the wallet backup. And it is not a list of passwords.

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

🎬 VISUAL — Estate deck heir-letter slide: include list on one side, never-include list on the other.

The letter should never contain seed phrases, private keys, passphrases, PINs, passwords, backup-file passwords, exact storage coordinates, or the complete recovery path.

It can say that a hardware-wallet process exists, that a collaborative provider should be contacted, or that the executor packet identifies the professionals and document locations. It should point to the process without containing the power to move the asset.

I would keep a separate executor packet too. That is the no-secrets working folder for the person in charge. It may include professional contacts, copies or locations of legal documents, account and provider lists, insurance contacts, funeral or household instructions, and the order in which people should be called.

The heir letter orients the family. The executor packet helps the person running the process.

Both need to be available outside the app. A letter that only exists behind your login may never be found. Download it, print it when appropriate, store it with the estate documents, and make sure the executor knows the packet exists.

Then add a communication backstop.

A dead-man switch or another scheduled delivery process can send the no-secrets letter if you fail to check in for a defined period. The purpose is not to release keys. It is to make sure somebody starts the process.

🎬 VISUAL — Four-step communication flow: check in → missed window → waiting period → heir letter delivered.

The cadence has to balance false alarms with delay. Orange Plan uses a ninety-day check-in as the current default. Whatever system you use, test the recipients, the waiting period, and the message.

A dead-man switch is not a substitute for the will, power of attorney, beneficiary forms, custody recovery, or a real conversation with the family. It is a backup communication layer.

I would also have the family conversation while you can answer questions.

Show them the process at a high level. Tell them who is in charge, which provider or professional to call, why they should not rush, and where the legal documents are kept. Do not reveal secrets just to prove the plan exists.

Then test delivery. Send a sample no-secrets message. Confirm the recipient recognizes it, understands the first action, and knows how to verify that it actually came from your system.

The finish line for this lesson is a letter that tells the family the first call and the first mistake to avoid, an executor packet that exists outside the app, and a tested communication method that can deliver the letter without releasing any secret.

The walkthrough will start the letter in Protect, confirm beneficiaries, enable the switch when Cloud mode is being used, download the document, and record the remaining outside-the-app actions.
""",
    },
    "8.4": {
        "title": "Use insurance for the risks the current stack cannot carry",
        "source": "Module 8 insurance outline and targeted insurance research; policy-specific decisions remain externally reviewed",
        "body": r"""
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

Umbrella coverage is excess liability protection above the required underlying home and auto limits. It can help protect the balance sheet from a large liability claim and defense costs. It does not cover every loss and it does not replace the underlying policies. Review the exclusions and required base limits rather than assuming the word umbrella means everything is covered.

Long-term care belongs on the later-life review. The cost is real, the products and pricing are imperfect, and a sufficiently large plan may choose to self-insure. The decision depends on health, family support, desired care, state rules, and the size of the assets available later. It is worth revisiting in the years when coverage is still available, not waiting until care is already needed.

Health coverage before Medicare is part of the Retirement Income bridge rather than this insurance audit. The same principle applies: price the actual options and the risk retained by the household.

🎬 VISUAL — Insurance coverage audit: Risk / current coverage / what the stack can absorb / remaining gap / next review date.

For each category, I would write down:

- the risk being transferred;
- the current policy and benefit;
- the deductible or waiting period the reserve must cover;
- the amount the current assets could absorb;
- the remaining gap;
- and the event or balance-sheet milestone that would justify changing the coverage.

Beneficiary forms are part of the review. A policy can be perfectly sized and still pay the wrong person if the designation is stale.

Do not cancel coverage only because Bitcoin rose during one market cycle. Reassess it using the full plan, the debts, the dependents, and the amount the household could reliably spend from the assets after taxes and market risk.

Orange Plan does not currently replace a policy inventory or quote comparison. Use the coverage-audit worksheet as the system of record and bring the gaps to a licensed insurance professional. The professional review should confirm policy mechanics, exclusions, and whether the proposed amount and term match the actual household.

The finish line is not buying more insurance. It is knowing which risks the reserve and stack can carry, which risks still need a policy, and when each coverage will be reviewed again.
""",
    },
    "9.1": {
        "title": "Keep the plan current without rebuilding it every month",
        "source": "Maintenance deck, current transaction and Build Your Plan flows, and Austin's five-minute review rule",
        "body": r"""
A financial plan usually dies from neglect or from being changed so often that nobody trusts it anymore.

Maintenance is the middle ground.

You are not rebuilding the strategy every month. You are keeping the facts current so the decisions you already made are still being tested against reality.

I use two rhythms: a short monthly pass and a more complete annual review.

The monthly pass should take around five minutes in a quiet month.

I would check four categories.

First, money movement: purchases, sales, contributions, withdrawals, transfers, and loan changes that are not already reflected in linked accounts.

Second, income and spending: a raise, a business change, a new recurring expense, or a spending level that has actually moved enough to change the plan.

Third, life events: something expected happened, changed date, changed amount, or is no longer likely.

Fourth, assumptions and targets: only when the facts or your honest long-term view changed. The Bitcoin price moving this week is not, by itself, a reason to rewrite the return assumptions.

The current app separates updating holdings from reconstructing old purchase history.

A new purchase, sale, or transfer updates what an account owns today. Cost basis and older transaction history can be added or corrected in the Tax workflow without changing the current balance twice.

That distinction matters. The monthly pass keeps the current portfolio accurate. The tax module maintains the evidence behind taxable lots.

🎬 VISUAL — Monthly loop: This month → update activity → verify spending → review open Build Your Plan tasks → choose 1–3 actions.

After entering the changes, verify the spending against the plan. One unusual month does not always justify a new baseline. Look for a repeated difference or a permanent change.

Then choose no more than one to three actions.

A long review list feels productive but usually creates unfinished work. A short list that gets completed every month compounds.

A quiet month is a successful review. If nothing material changed, update what needs updating and stop.

The annual review is where the whole strategy gets reconsidered.

I would walk the plan in the same order it was built:

- Cash Flow and Reserve: Is spending still realistic? Is the reserve target right? For retirees, run the guardrail and refill review.
- Allocation: Is the current mix near the target? Can the household still tolerate the dollar loss in a major Bitcoin drawdown? Are the account timeframes still correct?
- Debt: Does every debt still have the same job? Are the rates current? Is any Bitcoin-backed loan too close to a forced-sale level?
- Tax: Is basis current? Is there a harvesting, conversion, or state decision that must happen before year-end?
- Retirement Income: Did spending, Social Security timing, healthcare, or the withdrawal plan change?
- Custody: Prove one recovery, inspect the backups, and fix the largest new single point of failure.
- Estate and Insurance: Are the executor, beneficiaries, heir letter, switch recipients, and coverage gaps still current?

This is also where Build Your Plan is useful after the initial course. An open or incomplete area tells you which source data or decision needs attention. The checklist should be derived from the real data where possible, not used as a substitute for entering it.

The app should not train you to react to every red candle. Market prices update the values and may affect real risks such as LTV or taxes, but the strategy changes when a rule or life input changes.

A large drawdown may create a real action if a loan reaches a trigger, the retirement guardrail is breached, or the Reserve is near its floor. In those cases you are following a rule that was set beforehand, not redesigning the plan because the news is loud.

Before the next lesson, choose the day of the month for the short review and the month for the annual review. Put both on the calendar. The app stores the plan; the calendar protects the habit.
""",
    },
    "9.2": {
        "title": "Test decisions separately and read the finished plan like a planner",
        "source": "Old Module 10 plan-review deck, Maintenance capstone, and current Scenarios and Report flows",
        "body": r"""
The completed baseline is the plan you are currently using. Scenarios are where you ask questions without corrupting that baseline.

That separation is important.

If you change the retirement age, return assumptions, home purchase, or withdrawal strategy directly in the baseline every time you are curious, you lose the answer to what the actual plan is.

A scenario should have one clear question.

What happens if I retire three years earlier?

What happens if Bitcoin returns are lower than the baseline?

What happens if we move to another state?

What happens if we pay off this debt instead of investing the extra amount?

What happens if Social Security starts at sixty-two instead of seventy?

Change only the inputs needed to answer the question, compare the result with the baseline, and decide whether the evidence is strong enough to change the real plan.

🎬 VISUAL — Baseline on the left, one named scenario on the right, with changed inputs highlighted.

A useful comparison looks at more than the headline retirement date.

Read the change in confidence, taxes, accessible Bridge money, spending flexibility, debt risk, estate value, and any new failure point. A scenario that improves one number may weaken the rest of the plan.

When a scenario wins, apply the decision deliberately and document what changed. When it does not, keep it as evidence or delete it. Do not leave several unnamed versions and forget which one is real.

After every Build Your Plan area is intentionally complete, run the first full 1,000-path confidence check. This is the point where the confidence result is testing the full plan rather than a rough onboarding estimate or an unfinished strategy.

Choose the confidence target the retirement date has to clear, read the earliest date, and save the run. Then test the most important assumption or decision in Scenarios.

The final report assembles the whole plan into something the household and professionals can read.

I would read it in four passes: position, trajectory, risk, and actions.

Position asks where you stand today. Does the net worth, Bitcoin amount, account ownership, and debt match reality? If the position is wrong, stop and fix the source before trusting anything later.

Trajectory asks where the plan is headed. Read the retirement date and confidence result together. Then read the spending plan and how retirement gets funded. A date without the confidence and cash-flow story is incomplete.

Risk asks what could break the plan. Look at alternate Bitcoin paths, sequence risk, the Reserve and Bridge, debt and LTV, taxes, and the protection work. The question is not which chart looks best. It is whether the household would still have a workable response.

Actions are the one to three next steps. A plan review that ends with thirty vague tasks is not finished.

🎬 VISUAL — Report reading order: Position → Trajectory → Risk → Actions.

The assumptions and methodology belong at the end because they explain what every output rests on. You should be able to defend the major return, inflation, spending, longevity, and tax inputs in plain language. If you cannot, change the source and regenerate the report.

Save one report PDF each year after the annual review, with the year in the filename.

The second report is where the artifact becomes powerful. Compare four things with the prior year:

- net worth and the Bitcoin share;
- the retirement date and confidence target;
- the spending range or operating target;
- and whether last year's one to three actions were completed.

Use the report as the agenda for the family conversation. Give the tax pages and lot export to the CPA. Give the protection and custody summary to the estate attorney without including secrets. The point is that these people can review a coherent plan without needing your app login.

You started the course with scattered accounts and a rough estimate. The final walkthrough closes every open area, runs the full confidence check, tests one decision, reads the report in this order, and saves the first yearly PDF.
""",
    },
}
