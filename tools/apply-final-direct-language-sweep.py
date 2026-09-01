#!/usr/bin/env python3
"""Apply the final human-reviewed direct-language corrections to Academy scripts.

Every replacement was selected after the exhaustive 52-lesson inventory. This is
not a blind deletion of negative words: safety, legal, tax, custody, and model
boundaries stay direct. The changes below remove ordinary copywriting setup and
state the useful fact first.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS: dict[str, list[tuple[str, str]]] = {
    "scripts/01-2_the-three-layers-of-a-plan-and-setting-your-assumptions.md": [
        (
            "It isn't mainly a current-day budgeting app.",
            "Orange Plan is a forward-looking retirement planning tool.",
        ),
        (
            "I would not choose the model just because it gives you the earliest retirement date.",
            "Choose the model you could defend even when another preset gives you an earlier retirement date.",
        ),
        (
            "Think through what you believe is realistic instead of leaving the default simply because it was already loaded.",
            "Think through what you believe is realistic, then choose the preset or custom model that matches it.",
        ),
        (
            "I think the numbers should be realistic and not emotion-driven.",
            "Use numbers that are realistic and grounded in how you actually expect the future to unfold.",
        ),
        (
            "A flat CAGR isn't realistic across a 30- or 40-year retirement plan.",
            "Use a declining growth model across a 30- or 40-year retirement plan.",
        ),
        (
            "Before the walkthrough, choose the growth model and inflation assumption you would actually defend, not the pair that produces the earliest date.",
            "Before the walkthrough, choose the growth model and inflation assumption you would actually defend if you were explaining the plan to your family.",
        ),
    ],
    "scripts/01-3_what-the-onboarding-retirement-age-actually-means.md": [
        (
            "The main takeaway is simple: onboarding gives you a deterministic starting estimate.",
            "Onboarding gives you a deterministic starting estimate.",
        ),
    ],
    "scripts/02-1_find-the-surplus-your-plan-can-actually-use.md": [
        (
            "I think this is where a financial plan becomes real.",
            "Cash flow is where a financial plan becomes usable.",
        ),
        (
            "You can have a strong opinion about Bitcoin, taxes, retirement accounts, or borrowing, but none of those decisions can use more money than your cash flow produces.",
            "Every decision about Bitcoin, taxes, retirement accounts, or borrowing is limited by the amount your cash flow produces.",
        ),
        (
            "There is one more number you need besides normal spending: your bare-bones spending.\n\nBare-bones spending is the minimum amount the household could run on during a job loss, a business slowdown, or a major Bitcoin drawdown. Housing, food, utilities, insurance, healthcare, minimum debt payments, and the other expenses that do not disappear just because the month is bad.\n\nNormal spending tells the plan what your life costs. Bare-bones spending tells you how much cash it takes to buy time in an emergency. The next lesson uses that second number to size the reserve.",
            "There is one more number you need besides normal spending: your bare-bones spending.\n\nThis is the monthly amount your household could run on during a stressful or unexpected situation, like:\n\n- losing a job;\n- your business slowing down;\n- Bitcoin going through a major drawdown at the same time a car repair, medical bill, or another large one-time expense comes up.\n\nInclude the essential bills that would still need to be paid: housing, food, utilities, insurance, healthcare, and minimum debt payments.\n\nNormal spending tells the plan what your life costs. Bare-bones spending tells you how much cash it takes to buy time when something goes wrong. The next lesson uses that number to size the reserve.",
        ),
        (
            "I would not count a retirement contribution as an expense in this calculation.\n\nA contribution is a decision about where the surplus goes. We are going to make that decision in the Allocation and Next-Dollar module.",
            "Treat retirement contributions as a use of the surplus.\n\nThe Allocation and Next-Dollar module decides where that money goes.",
        ),
    ],
    "scripts/02-2_size-your-cash-reserve-in-months-of-spending.md": [
        (
            "For retirement, I use 18 months as a planning default, because the first few years after you stop working are when sequence risk is most dangerous. It's not a prediction of how long the next Bitcoin recovery takes.",
            "For retirement, I use 18 months as a planning default because the first few years after you stop working are when sequence risk is most dangerous. That reserve gives the household time to cover spending during a bad market.",
        ),
        (
            "The reason why we use this is that, for the floor, or your bare-bones spending, in a real emergency, this is the amount that you could cut back and still get by. If we were to size your emergency fund based off normal spending, you're oversizing your emergency fund and losing money to inflation. A smaller amount of cash is going to buy you more time in a worst-case scenario.",
            "Bare-bones spending is the monthly amount the household could run on during an emergency. Using that number keeps the reserve focused on the essential bills and lets each dollar of cash buy more time.",
        ),
        (
            "Now, your reserve is going to change as you move into retirement. While you're working, the purpose of the reserve is to replace a lost paycheck and protect you against losing your income and having large unexpected expenses come up. When we shift into retirement, there's not a paycheck to replace.\n\nInstead, this is going to cover the gap between what you spend and what's coming in from other income sources, like Social Security or, if you have one, a pension. The purpose of your reserve in retirement is there so that a bear market doesn't force you to sell Bitcoin to cover your expenses at the wrong time.",
            "Your reserve changes jobs as you move into retirement. While you're working, it replaces a lost paycheck and covers large unexpected expenses.\n\nIn retirement, it covers the gap between what you spend and what comes in from Social Security, a pension, or other reliable income. That cash lets you keep paying the bills through a bear market and wait for the plan to support the next sale or refill.",
        ),
        (
            "Before you pick and decide what your cash reserve is going to be, I think it's important to go through a scenario or situation.",
            "Before you choose the reserve, run this scenario.",
        ),
        (
            "Orange Plan calculates the target from those inputs and shows the gap; you do not type the target multiplication manually.",
            "Orange Plan calculates the target and gap automatically from the monthly amount and number of months.",
        ),
    ],
    "scripts/02-3_add-the-future-changes-your-plan-should-expect.md": [
        (
            "The timing still matters, but I do not want to turn it into a rigid rule that says every expense at a certain year must use a certain asset.",
            "Use the timing as a guide, then choose the funding source based on the amount, flexibility, and risk the household can carry.",
        ),
        (
            "If the bill is coming in the next year or two and the amount is non-negotiable, it should not depend on Bitcoin being at a favorable price when the bill arrives.",
            "For a bill due in the next year or two, protect the committed amount in cash or another reliable source before the due date.",
        ),
    ],
    "scripts/02-4_optional-decide-how-much-college-help-you-are-funding.md": [
        (
            "The first college-planning question is not which account to open.\n\nIt is how much you are actually committing to help with.",
            "Start by deciding how much you are actually committing to help with.",
        ),
        (
            "This is an estimate that gets updated, not a contract with a school that has not been chosen yet.",
            "Update this estimate as the school choice, aid package, and actual costs become clearer.",
        ),
        (
            "It also limits the investment menu, has rules around how the money is used, and may not give you the Bitcoin exposure you actually want.",
            "The trade-off is a limited investment menu, qualified-use rules, and often no direct Bitcoin exposure.",
        ),
        (
            "As the date gets closer, I would protect the first committed tuition payments so the family is not depending on the market at enrollment.",
            "As the date gets closer, protect the first committed tuition payments in reliable funding before enrollment.",
        ),
        (
            "I think that can be a useful starting framework because it reminds you there are several funding sources. I would not treat it as a rule.",
            "That can be a useful starting framework because it reminds you there are several funding sources. Adapt it to the family's actual commitment and resources.",
        ),
        (
            "The plan should reflect the decision you actually made, not a generic percentage.",
            "Build the plan around the family's actual commitment and funding sources.",
        ),
        (
            "It does not decide the family commitment for you, and education contributions stay separate from the broader Reserve, Bridge, and Legacy savings target.",
            "The family chooses the commitment. Orange Plan quantifies it, while education contributions stay separate from the broader Reserve, Bridge, and Legacy savings target.",
        ),
    ],
    "scripts/03-3_build-the-contribution-waterfall-for-every-new-dollar.md": [
        (
            "I would treat that as a comparison order, not a law.",
            "Use that order as a starting comparison and adjust it when the household's Bridge, taxes, or debt priorities change.",
        ),
        (
            "A plan that says \"invest two thousand dollars a month\" but does not say when that starts or which account gets it is not implemented yet.",
            "An implemented contribution plan names the monthly amount, the start date, and the account that receives it.",
        ),
    ],
    "scripts/03-4_put-the-right-holdings-inside-the-right-accounts.md": [
        (
            "A perfect tax account is not useful for a Bitcoin dollar if the plan only offers a limited stock and bond menu and no Bitcoin ETF or brokerage window.",
            "The account has to hold the asset the plan actually calls for. A limited stock-and-bond menu may send the Bitcoin dollars to a different account.",
        ),
        (
            "These accounts are usually long-term money rather than near-term Bridge funding.",
            "Use these accounts for long-term retirement money and keep near-term Bridge funding accessible.",
        ),
    ],
    "scripts/03-5_WALKTHROUGH_route-the-investable-surplus.md": [
        (
            "It is not a second surplus.",
            "It is the same surplus after the earlier claims.",
        ),
        (
            "It does not open the outside account.",
            "The outside account still has to be opened with the provider.",
        ),
    ],
    "scripts/04-1_decide-what-every-debt-should-do.md": [
        (
            "In today's lesson, we're going to build a debt strategy instead of just making a list of what you owe.",
            "In today's lesson, we're going to decide what each debt should do inside the plan.",
        ),
        (
            "That is why I would not look at today's debt-to-assets ratio and assume it is permanent. I want to know what it looks like after a major drawdown too.",
            "Recalculate debt-to-assets after a major Bitcoin drawdown before deciding how much leverage the household can carry.",
        ),
        (
            "A strong answer on one does not cancel a weak answer on the other.",
            "Use both answers together; payment capacity and balance-sheet leverage can point in different directions.",
        ),
        (
            "I treat the bands in the app as context, not commands.",
            "Use the bands in the app as context for setting the household's range.",
        ),
        (
            "The correct range is the one that still works in the bad version of your life, not only the current one.",
            "Choose the range that still works after income falls, fixed costs rise, or Bitcoin goes through a major drawdown.",
        ),
        (
            "The rate may be a drag, but the payment may or may not be the thing holding the plan back.",
            "The rate may be a drag, while the payment pressure determines whether it is the current bottleneck.",
        ),
        (
            "Those are not the same risk.",
            "Evaluate each decision separately.",
        ),
        (
            "- Pay it off because the guaranteed cost and stress are not worth carrying.",
            "- Pay it off because removing the guaranteed cost and stress improves the plan.",
        ),
    ],
    "scripts/05-2_use-the-tax-buckets-and-low-income-window-on-purpose.md": [
        (
            "The starting age has changed more than once, so the current rule should be verified instead of frozen into a video.",
            "Verify the current starting age before recording or acting because the rule has changed more than once.",
        ),
        (
            "I would not simply \"fill the bracket\" based on one tax rate line.",
            "Model the entire tax stack before choosing a conversion amount.",
        ),
        (
            "I would treat relocation as a life decision that can have a tax benefit, not a tax trick that happens to require a moving truck.",
            "Treat relocation as a real life decision and measure the tax benefit inside the full plan.",
        ),
    ],
    "scripts/06-1_build-spending-income-floor-gap-and-bridge.md": [
        (
            "The correct answer comes from comparing the full plan, not repeating \"always wait\" or \"always claim early.\"",
            "Compare the full plan at several claiming ages and choose the trade-off that fits the Bridge, taxes, and household priorities.",
        ),
    ],
    "scripts/06-2_choose-withdrawal-order-and-refill-rule.md": [
        (
            "The better strategy is often tax-aware rather than strictly sequential.",
            "A tax-aware strategy can use low ordinary-income brackets on purpose while taxable lots fund the rest of the spending.",
        ),
        (
            "The ratio is an output from the plan, not a universal number somebody should copy.",
            "Let the plan produce the blend from spending, basis, account balances, Social Security, healthcare, and current tax rules.",
        ),
        (
            "If the Reserve approaches its hard floor, the household may still have to refill, reduce spending, use another account, or make a different funding decision. The rule is not \"never sell down.\" The rule is that the plan responds before a cash shortage forces a bad decision.",
            "If the Reserve approaches its hard floor, respond before a cash shortage forces a bad decision. The response may be a refill, lower spending, another account, or a controlled sale.",
        ),
        (
            "It should not decide which trade-off your family prefers.",
            "The family chooses the trade-off after seeing the taxes, interest, risk, and estate impact.",
        ),
    ],
    "scripts/06-3_use-plan-confidence-and-guardrails-to-adjust-spending.md": [
        (
            "It is a stress test for comparing decisions, rather than a personal probability of ruin.",
            "Use it as a stress test for comparing decisions. It describes modeled paths under the selected assumptions, not your personal chance of ruin.",
        ),
        (
            "Normal users see one clear standard instead of another percentage control to manage.",
            "That fixed standard keeps the core result consistent across every plan.",
        ),
        (
            "The goal is a plan the household actually wants that reaches the Orange Plan standard.",
            "Build the spending level the household actually wants, then confirm it reaches the Orange Plan standard.",
        ),
        (
            "Rising above the upper guardrail opens the same review in the other direction. The household can preview a higher spending amount instead of under-spending indefinitely.",
            "Rising above the upper guardrail opens a review of a higher spending amount, giving the household permission to use more of the plan when the math supports it.",
        ),
        (
            "A weak market and a lower spending review may call for pausing a discretionary refill instead of selling assets into weakness.",
            "During a weak market, the annual review may pause a discretionary refill and use the cash already set aside.",
        ),
    ],
    "scripts/07-1_self-custody-professional-custody-and-when-a-split-makes-sense.md": [
        (
            "There is no setup with no trade-offs.",
            "Every setup comes with trade-offs.",
        ),
        (
            "The goal is to decide which risks you are willing to own and make sure one mistake, one provider, one device, or one bad day cannot destroy the family's plan.",
            "Choose the risks you are willing to own, then make sure one mistake, one provider, one device, or one bad day cannot destroy the family's plan.",
        ),
        (
            "They have to fit together, but they are not the same job.",
            "Custody handles operational access. Estate planning handles legal authority and transfer.",
        ),
        (
            "None of those answers automatically tells you which product to use. It tells you which trade-off you are not willing to give up.",
            "Those answers narrow the trade-offs and show which protection the household insists on preserving.",
        ),
        (
            "Nothing about the device changed. What was at stake did.",
            "The device stayed the same while the amount at stake became life-changing.",
        ),
        (
            "I would measure readiness with four outcomes instead of a wealth ladder:",
            "I would measure readiness with four outcomes:",
        ),
    ],
    "scripts/07-2_set-up-a-hardware-wallet-and-prove-recovery.md": [
        (
            "The important test for a hardware wallet is not whether you wrote the recovery words down.\n\nIt is whether you can restore the wallet from the backup before a meaningful amount of Bitcoin depends on it.",
            "The important hardware-wallet test is whether you can restore the wallet from the backup before a meaningful amount of Bitcoin depends on it.",
        ),
        (
            "The exact button sequence depends on the device and firmware. That is why the filmed demo has to use the actual hardware and current instructions rather than a generic script pretending every wallet works the same way.",
            "The exact button sequence depends on the device and firmware, so the filmed demo uses the actual hardware and current vendor instructions.",
        ),
        (
            "There are a few rules that do not change.",
            "The safety rules stay the same across devices.",
        ),
        (
            "I would not turn this into one permanent Bitcoin threshold because the dollar value and fee market change.",
            "Set the withdrawal threshold from the current dollar value, fee market, and the size of the outputs you are creating.",
        ),
    ],
    "scripts/07-3_fix-single-points-of-failure_and_harden_accounts.md": [],
    "scripts/07-3_fix-single-points-of-failure-and-harden-accounts.md": [
        (
            "Most Bitcoin losses are not somebody breaking the cryptography.\n\nThey are one weak login, one backup, one location, one person who knows the process, one provider, or one rushed decision with no second check.",
            "Most Bitcoin losses come from one weak login, one backup, one location, one person who knows the process, one provider, or one rushed decision with no second check.",
        ),
        (
            "That is why I want you to test failure domains, not count objects.",
            "Test whether the backups are independent across failure domains.",
        ),
        (
            "Urgency is the biggest warning sign. Somebody says the account is being drained, the wallet is compromised, or the offer expires in ten minutes. The goal is to make you skip the verification process.",
            "Urgency is the biggest warning sign. Somebody says the account is being drained, the wallet is compromised, or the offer expires in ten minutes. The pressure is designed to make you skip the verification process.",
        ),
    ],
    "scripts/07-5_WALKTHROUGH_document-the-custody-decision-and-status.md": [
        (
            "It does not decide that every larger balance should move into a more complicated self-custody setup.",
            "The decision map records the household's chosen architecture and the risk it is meant to reduce.",
        ),
        (
            "Buying a hardware wallet does not complete it.",
            "Mark recovery complete only after a real recovery test.",
        ),
        (
            "**SAY** The goal is one meaningful reduction in risk, not checking every box for appearance.",
            "**SAY** Use the checklist to make one meaningful reduction in risk at a time.",
        ),
    ],
    "scripts/08-1_choose-who-is-in-charge-and-put-the-legal-baseline-in-place.md": [
        (
            "Pick for the job, not for who would be flattered to be asked. Then ask the person. An executor who has never heard about the role is not part of a working plan yet.",
            "Pick for capability, availability, and trust. Then ask the primary person and backup to accept the role before you rely on them in the plan.",
        ),
        (
            "A will directs how probate assets should be handled and names important roles. It does not control every asset automatically.",
            "A will directs how probate assets should be handled and names important roles. Beneficiary forms, jointly owned assets, and trust-owned assets follow their own legal paths.",
        ),
        (
            "The next lesson connects that legal layer to the technical custody setup without pretending there is one universal way to split seeds, passphrases, or keys.",
            "The next lesson connects that legal layer to the technical custody setup and shows how the design changes with single-sig, passphrase, multisig, or institutional custody.",
        ),
    ],
    "scripts/08-2_align-legal-authority-with-technical-recovery.md": [
        (
            "I do not want to give you one universal formula such as \"the heirs hold the seed and the executor holds the passphrase.\" That can work in a carefully designed and tested plan, but it can also create new failure points or give the wrong person practical control.\n\nThe right structure depends on the custody method, the people involved, the legal roles, and what each component can actually do.\n\nStart with the principle: no unnecessary person should hold enough information or authority to act alone, but the family must still have a complete, tested recovery path when the proper conditions are met.",
            "Use one governing principle for every custody design: the legally authorized people need a complete, tested recovery path while no unnecessary person can act alone. The exact structure changes with the custody method, the people involved, the legal roles, and what each component can actually do.",
        ),
        (
            "A passphrase is another secret that must be recovered exactly. It does not create a second signer or legal dual control.",
            "A passphrase is another secret that must be recovered exactly. Multisig is what creates multiple signers and operational separation.",
        ),
        (
            "Without the correct configuration, heirs may struggle to reconstruct the intended wallet even if they have key material.",
            "Heirs need the correct wallet configuration as well as the key material to reconstruct the intended wallet.",
        ),
        (
            "The person with a key may not be the person legally entitled to direct a transaction. The person with legal authority may not be technically capable of signing one.",
            "Legal authority and signing capability can belong to different people.",
        ),
        (
            "A custody design that works today can become unusable if it is never reviewed.",
            "Review the custody design as devices, providers, and people change.",
        ),
        (
            "The heir letter in the next lesson tells the family how to start without disclosing the components themselves.",
            "The heir letter in the next lesson gives the family the safe starting instructions while the recovery components remain separate.",
        ),
    ],
    "scripts/08-4_use-insurance-for-risks-the-stack-cannot-carry.md": [
        (
            "The reserve already self-insures smaller problems. A repair, a deductible, or a short income interruption should not require a complicated policy if the cash buffer can handle it.",
            "Use the reserve for repairs, deductibles, and short income interruptions that the cash buffer can absorb.",
        ),
        (
            "The contract language matters: own-occupation versus any-occupation definitions, waiting periods, benefit periods, exclusions, and how bonuses or self-employment income are treated. This is where the actual policy and a licensed professional matter more than a generic rule.",
            "The contract language matters: own-occupation versus any-occupation definitions, waiting periods, benefit periods, exclusions, and how bonuses or self-employment income are treated. Review the actual policy with a licensed professional because those terms drive the result.",
        ),
        (
            "It is worth revisiting in the years when coverage is still available, not waiting until care is already needed.",
            "Revisit long-term-care coverage while the household still has practical options, usually during the later working years.",
        ),
        (
            "Health coverage before Medicare is part of the Retirement Income bridge rather than this insurance audit.",
            "Handle health coverage before Medicare inside the Retirement Income bridge.",
        ),
    ],
    "scripts/advanced/A3-1_price-context-before-a-large-bitcoin-move.md": [
        (
            "The context check is a pause, not a signal.",
            "Use the context check as a pause before making the decision.",
        ),
        (
            "A sale needs a reason tied to spending, taxes, or risk rather than relief from the current emotion.",
            "Tie a sale to spending, taxes, or risk and state that reason before acting.",
        ),
        (
            "The price context never replaces those decisions.",
            "Cash flow, the Reserve, debt, taxes, custody, and time horizon still make the decision.",
        ),
    ],
    "scripts/advanced/A4-1_borrow-against-bitcoin-without-liquidation.md": [
        (
            "Read the actual agreement rather than assuming one lender works like another.",
            "Read the actual agreement and record that lender's specific thresholds, fees, and remedies.",
        ),
        (
            "The phrase \"borrow and never pay tax\" is not a complete plan.",
            "A complete borrow-versus-sell plan includes interest, liquidation risk, repayment, counterparty risk, and the tax consequences of every exit path.",
        ),
        (
            "It cannot make the contract safer than the actual lender terms.",
            "The model is only as safe as the actual lender terms entered into it.",
        ),
    ],
    "scripts/advanced/A5-1_rmd-pressure-and-roth-conversions.md": [
        (
            "Start with the ordinary-income brackets, but do not stop there.",
            "Start with the ordinary-income brackets, then include capital gains, Social Security, Medicare, healthcare subsidies, state tax, deductions, and credits.",
        ),
        (
            "The question to ask is not simply, \"How much can I convert?\" It is, \"How much ordinary-income room is actually worth using this year after every interaction is included?\"",
            "Ask, \"How much ordinary-income room is actually worth using this year after every interaction is included?\"",
        ),
    ],
    "scripts/advanced/A5-2_harvest-bitcoin-losses-and-gains.md": [
        (
            "Without the date, amount, basis, and supported identification method, the app cannot tell you which loss or gain is actually being realized.",
            "The app needs the date, amount, basis, and supported identification method to determine which loss or gain is being realized.",
        ),
        (
            "The Form 8949 export is a handoff, not a substitute for reviewing whether the transaction and identification were reported correctly.",
            "Use the Form 8949 export as the CPA handoff, then verify that the transaction and identification were reported correctly.",
        ),
    ],
    "scripts/advanced/A5-3_state-taxes-and-relocation.md": [
        (
            "Residency is not created by editing the state field in the app or changing a mailing address.",
            "Residency depends on the full pattern of where you live, work, own property, vote, spend time, and intend to remain.",
        ),
        (
            "Treat relocation as a real life decision that may create a large tax benefit, not a tax trick with a moving truck.",
            "Treat relocation as a real life decision and measure the potential tax benefit inside the full plan.",
        ),
    ],
    "scripts/advanced/A6-1_health-coverage-before-medicare.md": [
        (
            "The number is large enough to move the retirement date, so it needs to be priced rather than left as a fear.",
            "Price the healthcare bridge because the annual cost can move the retirement date.",
        ),
        (
            "ACA marketplace coverage uses metal tiers to describe cost sharing, not medical quality.",
            "ACA metal tiers describe how costs are shared between the plan and the member; provider networks and plan terms determine access and quality.",
        ),
        (
            "Compare the total cost, not only the income-tax line.",
            "Compare premiums, subsidies, deductibles, out-of-pocket risk, HSA eligibility, and tax effects together.",
        ),
    ],
    "scripts/advanced/A6-2_sell-borrow-or-hold.md": [
        (
            "These are tools, not moral positions.",
            "Treat selling, borrowing, and holding as tools with different costs and risks.",
        ),
        (
            "Do not build the entire plan around one sentence about a step-up without legal and tax review.",
            "Build the estate assumption from current law and professional review, then test how sensitive the plan is to a different outcome.",
        ),
        (
            "Nothing should change in the baseline until the strategy has been previewed, the lender terms are verified, and the household can explain how the debt gets repaid if Bitcoin does not cooperate.",
            "Keep the strategy in Preview until the lender terms are verified and the household can explain repayment under a bad Bitcoin path.",
        ),
    ],
    "scripts/advanced/A7-2_what-self-custody-asks-of-you.md": [
        (
            "Self-custody should create confidence, not constant fear.",
            "A sustainable self-custody setup should leave the household confident in the recovery process.",
        ),
        (
            "And keeping some professionally supported Bitcoin is not a failure of conviction when it solves a real family or operational risk.",
            "Professionally supported custody can be a deliberate way to solve family or operational risk while preserving direct control over another portion.",
        ),
    ],
    "scripts/advanced/A7-3_run-the-one-failure-test-across-methods-and-providers.md": [
        (
            "Concentration risk is not only holding too much Bitcoin.",
            "Concentration risk also comes from depending on one device, one vendor, one custodian, one recovery method, one location, or one person.",
        ),
        (
            "Three keys in three envelopes are not independent if all three are in the same house.",
            "Three keys in three envelopes are still exposed to the same house fire when all three are stored in one house.",
        ),
        (
            "Two hardware devices are not full vendor diversity if they rely on the same secure element, firmware path, and companion software.",
            "Two hardware devices share a vendor failure domain when they rely on the same secure element, firmware path, and companion software.",
        ),
        (
            "Two exchanges are not independent if both rely on the same custodian.",
            "Two exchanges share a custody failure domain when both rely on the same custodian.",
        ),
        (
            "A meaningful amount can become life-changing without the custody process changing.",
            "As the balance grows from meaningful to life-changing, rerun the One-Failure Test even if the custody process has stayed the same.",
        ),
    ],
    "scripts/advanced/A8-1_do-you-need-a-trust.md": [
        (
            "Bitcoin ownership by itself does not establish the need.",
            "The need for a trust comes from the legal, tax, control, probate, creditor, and family jobs it must solve.",
        ),
        (
            "That is a successful answer, not a failure to use an advanced tool.",
            "Stopping at the legal baseline is a successful answer when no additional trust job exists.",
        ),
        (
            "Because the owner retains broad control, it usually does not remove the assets from the taxable estate or create broad creditor protection by itself.",
            "A revocable trust usually keeps the assets in the taxable estate and offers limited creditor protection because the owner retains broad control.",
        ),
        (
            "One waiver sentence cannot carry all of those jobs.",
            "The full trust language has to address investment authority, trustee duties, custody, fees, taxes, and distributions together.",
        ),
        (
            "It should not create a legal document that depends on a custody process nobody can execute.",
            "The legal document and custody process must be executable by the named people under stress.",
        ),
    ],
}

# Remove an accidental empty alias if present in the mapping above.
REPLACEMENTS.pop("scripts/07-3_fix-single-points-of-failure_and_harden_accounts.md", None)


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path.relative_to(ROOT)} expected one match, found {count}: {old[:90]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def update_header(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith(("TELEPROMPTER SCRIPT", "ADVANCED TELEPROMPTER SCRIPT")):
        return
    divider = "=" * 60
    head, sep, body = text.partition(divider)
    if not sep:
        raise RuntimeError(f"missing script divider: {path.relative_to(ROOT)}")
    words = len(body.strip().split())
    minutes = words / 155
    lines = head.splitlines()
    if len(lines) < 3 or " words · ~" not in lines[2]:
        raise RuntimeError(f"unexpected metadata header: {path.relative_to(ROOT)}")
    status = lines[2].split(" · ", 2)[2]
    lines[2] = f"{words:,} words · ~{minutes:.1f} min at 155 wpm · {status}"
    path.write_text("\n".join(lines) + "\n" + divider + body, encoding="utf-8")


def main() -> None:
    changed: list[Path] = []
    for relative, pairs in REPLACEMENTS.items():
        path = ROOT / relative
        for old, new in pairs:
            replace_once(path, old, new)
        update_header(path)
        changed.append(path)
    print(f"updated {len(changed)} canonical lesson files with {sum(len(v) for v in REPLACEMENTS.values())} reviewed replacements")


if __name__ == "__main__":
    main()
