#!/usr/bin/env python3
"""Apply the reviewed course-wide direct-affirmative prose pass.

The first pass replaced the most visible “not A, but B” lines. This pass removes
the remaining copywriting-style setup sentences while preserving negatives that
carry a safety, legal, tax, custody, or model boundary.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = ROOT / "DIRECT-VOICE-PASS-2.md"

REPLACEMENTS: dict[str, list[tuple[str, str]]] = {
    "scripts/00-1_how-to-use-this-course.md": [
        (
            "And a quick disclaimer: this is not designed to replace your tax advisor, estate planning attorney, or financial advisor. It's not financial advice. This is education as far as how I think about these concepts and how I would go about building a financial plan. It is on you to make your own financial decisions and then act on those, using the information that you've learned and what you feel like is best for your specific situation.",
            "And a quick disclaimer: this course is education about how I think through building a financial plan. You are responsible for your own financial decisions. Use a tax advisor, estate planning attorney, insurance professional, or financial advisor when your specific facts require licensed or current professional judgment.",
        ),
    ],
    "scripts/00-2_how-to-use-orange-plan-ai.md": [
        (
            "The file removes personal information that the outside AI does not need and gives it a structured summary of the plan.",
            "The file removes personal identifiers and gives the outside AI a structured summary of the plan.",
        ),
    ],
    "scripts/01-1_what-to-gather-before-you-build-the-plan.md": [
        (
            "There are not necessarily any documents that you need for this one. I think it's just important to start thinking about what might be coming up in the future.",
            "For future life events, start with a list of the income and expenses you reasonably expect. A statement usually is not required yet.",
        ),
        (
            "Sometimes exchanges do not keep all of your history forever. If you cannot access all of it, that's okay.",
            "Download every history file that is still available and make a note of any missing years or accounts. We will handle the gaps honestly in the Tax module.",
        ),
    ],
    "scripts/01-2_the-three-layers-of-a-plan-and-setting-your-assumptions.md": [
        (
            "Don't feel like you need to constantly make changes to your baseline information just to test an idea. We want to get the information in the first layer right so we can make accurate comparisons with hypothetical futures in the third layer.",
            "Keep the baseline stable and accurate. Use Scenarios to compare hypothetical futures without changing the saved plan.",
        ),
        (
            "It isn't a guarantee. Moderate is a step down if you want to be more conservative, and Conservative is there if you want to use a much lower growth path.",
            "Treat every model as a planning tool. Moderate uses a lower growth path than Power Law, and Conservative steps down further.",
        ),
    ],
    "scripts/02-1_find-the-surplus-your-plan-can-actually-use.md": [
        (
            "Your spending is not your gross income. It is not the amount hitting the bank before taxes. And in Orange Plan, minimum debt payments are entered separately, so you do not want to count the same payment again inside living expenses.",
            "Enter after-tax living expenses as spending. Gross income and minimum debt payments have their own rows, which keeps the same dollars from being counted twice.",
        ),
    ],
    "scripts/02-2_size-your-cash-reserve-in-months-of-spending.md": [
        (
            "In our example, we have a couple that's holding 1.75 Bitcoin. Back in 2022, during the bear market, Bitcoin dropped 77% from its peak. If they were to have something like a job loss during this window and they're not holding enough cash, but they still have bills like their mortgage that they have to pay, they're now stuck in a situation where they're selling Bitcoin at a 77% loss just to cover all of their bills and their mortgage.",
            "In our example, a couple holds 1.75 Bitcoin. During the 2022 bear market, Bitcoin fell 77% from its peak. A job loss during that drawdown, combined with too little cash and a mortgage that still has to be paid, can force the household to sell Bitcoin near the bottom to cover the bills.",
        ),
        (
            "If you have, for example, two stable incomes and you don't have any kids or people relying on you, you can start at about 3 months, and that's going to be the minimum. For most households, I would say 6 months is the baseline.",
            "Two stable incomes with no dependents may support a starting target around three months. Six months is a more common baseline for a household with normal uncertainty.",
        ),
        (
            "If you don't like holding a lot of cash, then I think a floor for a cash reserve in retirement is going to be 12 months. These can go up to around 3 years if you're risk-averse and just feel better having a large cash position.",
            "For a Bitcoin-heavy retirement plan, I use roughly 12 months as the aggressive end of the Reserve range. A more risk-averse household may choose up to around three years of the spending gap.",
        ),
    ],
    "scripts/02-3_add-the-future-changes-your-plan-should-expect.md": [
        (
            "Real life is not going to stay flat for the next thirty or forty years. A child may start college, you may replace a car, sell a house, change jobs, help a parent, receive an inheritance, or spend more in the first few years of retirement than you do later.",
            "Over the next thirty or forty years, college, cars, homes, jobs, family support, inheritances, and retirement spending will change the cash flow.",
        ),
        (
            "You do not need perfect information to add one. Use the best amount and date you can reasonably defend today, then update it as the event gets closer.",
            "Use the best amount and date you can reasonably defend today, then update the life event as it gets closer.",
        ),
    ],
    "scripts/03-3_build-the-contribution-waterfall-for-every-new-dollar.md": [
        (
            "Most people do not need another list of possible accounts. They need to know what happens to the next five hundred dollars after it hits the plan.",
            "The useful answer is where the next five hundred dollars goes after it enters the plan.",
        ),
        (
            "The reason it comes first is not that cash is the best long-term investment. It is that an empty reserve can turn the next emergency into credit-card debt or a forced Bitcoin sale.",
            "The Reserve comes first because an empty Reserve can turn the next emergency into credit-card debt or a forced Bitcoin sale.",
        ),
        (
            "A stock-only 401(k), a plan with high fees, and an account that cannot hold the Bitcoin exposure you want may not deserve every additional dollar. Capture the match first, then compare the rest honestly.",
            "Capture the match first. Then compare additional 401(k) contributions with the other destinations using the fees, investment menu, access rules, and Bitcoin exposure available inside the plan.",
        ),
        (
            "We are not inserting a generic \"pay debt first\" rule. For now, this rung uses the Extra Debt amount currently saved in the plan, which may be zero. Module 4 decides the final amount and then returns it to this waterfall.",
            "This rung uses the current Extra Debt amount as a placeholder, which may be zero. Module 4 decides the final amount and returns it to this waterfall.",
        ),
        (
            "If two jobs are both underfunded, splitting the dollar is not indecision. It can be the correct answer.",
            "Splitting the dollar can fund two underfunded jobs at the same time.",
        ),
        (
            "And Orange Plan cannot change the outside world for you. Saving a contribution plan in the app updates the projection. You still need to change the payroll election, automatic bank transfer, exchange purchase, or brokerage instruction that actually moves the money.",
            "Saving the contribution plan updates the projection. Then change the payroll election, automatic bank transfer, exchange purchase, or brokerage instruction that actually moves the money.",
        ),
    ],
    "scripts/03-4_put-the-right-holdings-inside-the-right-accounts.md": [
        (
            "But saving a specific holding in the plan does not purchase it at the custodian. It tells the projection what you intend the new dollars to buy.",
            "Saving a specific holding tells the projection what the new dollars are intended to buy. Complete the actual purchase with the custodian.",
        ),
    ],
    "scripts/03-5_WALKTHROUGH_route-the-investable-surplus.md": [
        (
            "**SAY** Saving the target does not order a taxable sale. New contributions can move the plan toward it.",
            "**SAY** Saving the target updates the plan. Use new contributions to move toward it unless a separate one-time shift is intentionally previewed and completed.",
        ),
        (
            "**⚠** A bucket estimate is not a global guarantee that one contribution amount solves the entire retirement plan. Read the scope shown in the app.",
            "**⚠** Read the scope shown in the app. A bucket estimate applies to that funding job and timeframe.",
        ),
    ],
    "scripts/04-1_decide-what-every-debt-should-do.md": [
        (
            "The interest rate matters, but it is not the only thing that matters. I would look at:",
            "Read the interest rate alongside:",
        ),
    ],
    "scripts/05-1_cost-basis-know-what-you-paid-before-you-plan-a-sale.md": [
        (
            "Moving Bitcoin from an exchange to a hardware wallet usually does not create a new purchase price. The original lot history still follows the Bitcoin.",
            "The original acquisition date and basis follow Bitcoin when it moves between your own accounts. A transfer from an exchange to a hardware wallet generally keeps the same lot history.",
        ),
        (
            "If the full history does not exist, do not make up a precise number because it makes the report look complete. Gather everything you can document, narrow the missing purchase period as honestly as possible, keep notes on how the reconstruction was performed, and review uncertain treatment with a tax professional.",
            "When the full history is missing, gather everything you can document, narrow the purchase period as honestly as possible, keep notes on the reconstruction, and review uncertain treatment with a tax professional. Leave unsupported precision out of the record.",
        ),
    ],
    "scripts/05-2_use-the-tax-buckets-and-low-income-window-on-purpose.md": [
        (
            "The decision is not whether conversions are always good. It is whether paying a known rate now is likely to reduce lifetime tax or create useful flexibility later.",
            "Compare the known tax rate now with the expected lifetime tax and flexibility of leaving the money in the Traditional account.",
        ),
        (
            "A conversion is not the only way to use a low-income year. In some plans, spending from the Traditional account while the rate is low is simpler and still shrinks the future required-distribution problem.",
            "A low-income year can support a Roth conversion or an intentional Traditional withdrawal. Both use lower brackets now and can reduce future required-distribution pressure.",
        ),
        (
            "But changing the state on a tax form is not the same thing as changing domicile. A real move involves where you live, work, vote, hold property, spend time, and intend to remain.",
            "Domicile depends on the full pattern of where you live, work, vote, hold property, spend time, and intend to remain. A state entry on a tax form is only one piece of that record.",
        ),
        (
            "The goal of this module is not to complete every tax move today. It is to leave with three things:",
            "Leave this module with three things:",
        ),
    ],
    "scripts/05-3_WALKTHROUGH_tax.md": [
        (
            "**SAY** The app does not invent basis. Missing is a work item, not zero and not a supported estimate.",
            "**SAY** A missing basis field stays missing and becomes a reconstruction work item. Zero means an actual supported zero basis.",
        ),
    ],
    "scripts/06-1_build-spending-income-floor-gap-and-bridge.md": [
        (
            "The core course does not assume one solution. It may be COBRA for a short period, an ACA marketplace plan, a spouse's employer plan, a health-sharing arrangement, or another option.",
            "The healthcare bridge may use COBRA for a short period, an ACA marketplace plan, a spouse's employer plan, a health-sharing arrangement, or another option.",
        ),
    ],
    "scripts/06-2_choose-withdrawal-order-and-refill-rule.md": [
        (
            "The household did not eliminate the tax. It left lower brackets unused and pushed more income into later years when the rate and other interactions may be worse.",
            "The household left lower brackets unused and pushed more taxable income into later years, where rates and other interactions may be worse.",
        ),
    ],
    "scripts/07-1_self-custody-professional-custody-and-when-a-split-makes-sense.md": [
        (
            "The first decision is not the product. It is which risk you are trying to reduce.",
            "Start by naming the risk you are trying to reduce.",
        ),
        (
            "For another person, direct control matters, but it is not absolute. They may want some Bitcoin they control directly and some professionally supported.",
            "Another person may want both directly controlled Bitcoin and a professionally supported portion.",
        ),
        (
            "Notice what this does not say. A large balance can use direct self-custody, collaborative multisig, institutional custody, or an intentional combination.",
            "A large balance can use direct self-custody, collaborative multisig, institutional custody, or an intentional combination.",
        ),
    ],
    "scripts/07-2_set-up-a-hardware-wallet-and-prove-recovery.md": [
        (
            "Redundancy is not simply making as many copies as possible. It is making sure one event cannot destroy every recovery path.",
            "Redundancy makes sure one event cannot destroy every recovery path. Each additional copy or location should solve a specific failure.",
        ),
    ],
    "scripts/07-3_fix-single-points-of-failure-and-harden-accounts.md": [
        (
            "You do not have to fix everything this week. Rank the top one to three by the damage they could cause, then fix the first one.",
            "Rank the top one to three weaknesses by the damage they could cause, then fix the first one this week.",
        ),
        (
            "A few years ago, somebody called my bank pretending to be me and tried to move about ten thousand dollars. They did not get it, but it made the weakness very real. That is when I moved my email and important exchange logins to physical security keys.",
            "A few years ago, somebody called my bank pretending to be me and tried to move about ten thousand dollars. The bank stopped the transfer, and the attempt made the weakness very real. That is when I moved my email and important exchange logins to physical security keys.",
        ),
        (
            "The app checklist is not the security itself. It is the honest record of what has and has not actually been done.",
            "The app checklist is the honest record of which security work has actually been completed and which action comes next.",
        ),
    ],
    "scripts/07-5_WALKTHROUGH_document-the-custody-decision-and-status.md": [
        (
            "**SAY** More hardware is not the goal. Every extra method, provider, or device has to solve the failure we just named.",
            "**SAY** Add a method, provider, or device only when it solves the failure we just named.",
        ),
        (
            "**⚠** An institutional account is not \"secure\" merely because it exists. Email security, authentication, withdrawal protections, beneficiary or estate process, and provider concentration still matter.",
            "**⚠** Review the email security, authentication, withdrawal protections, beneficiary or estate process, and provider concentration for every institutional account.",
        ),
    ],
    "scripts/08-1_choose-who-is-in-charge-and-put-the-legal-baseline-in-place.md": [
        (
            "They do not have to know how to recover a wallet personally. They need a clear process, the right legal authority, and a named technical or custody contact when the setup requires one.",
            "Give the executor a clear process, the right legal authority, and a named technical or custody contact when the setup requires one. The executor can coordinate the recovery without personally being the wallet expert.",
        ),
        (
            "A will cannot move Bitcoin if nobody can recover the wallet. A seed phrase does not give somebody lawful authority to take the asset. Legal authority and technical capability are two separate layers, and the plan needs both.",
            "The plan needs both legal authority and technical capability. The will identifies who may act; the tested custody process makes the Bitcoin recoverable by the authorized people.",
        ),
        (
            "I would start with the baseline even if the estate is not large. A simple plan that exists and is properly executed is more useful than an advanced trust design that never gets finished.",
            "Start with the legal baseline at every asset level. A simple plan that exists and is properly executed is more useful than an advanced trust design that never gets finished.",
        ),
        (
            "That last question is not solved by copying one waiver sentence from the internet. Trustee duties and the ability to hold a concentrated asset depend on the governing law, the trust language, and the facts.",
            "Trustee duties and the authority to hold a concentrated asset depend on the governing law, the complete trust language, and the facts. Have the attorney draft the full authority instead of copying one waiver sentence from the internet.",
        ),
    ],
    "scripts/08-2_align-legal-authority-with-technical-recovery.md": [
        (
            "The passphrase is not a second signer and it does not create legal dual control. It is another secret that must be recovered exactly.",
            "A passphrase is another secret that must be recovered exactly. It does not create a second signer or legal dual control.",
        ),
        (
            "One key alone cannot spend. That can create real operational separation, but the keys are not the entire recovery plan.",
            "A two-of-three wallet can create operational separation because one key alone cannot spend. The descriptor or wallet configuration, identity process, legal authority, and people remain part of the recovery plan.",
        ),
        (
            "The value is not only the third key. It is also the support, identity-verification, continuity, and documented procedure.",
            "A collaborative provider can add support, identity verification, continuity, a documented procedure, and a third key.",
        ),
        (
            "The deliverable is not a diagram that looks sophisticated. It is a tested path where the legally authorized people can recover the asset, one ordinary failure does not destroy the plan, and no secret is stored in the app or legal documents.",
            "The deliverable is a tested path where the legally authorized people can recover the asset, one ordinary failure does not destroy the plan, and no secret is stored in the app or legal documents.",
        ),
    ],
    "scripts/08-3_write-the-heir-letter-and-create-the-backstop.md": [
        (
            "A dead-man switch is not a substitute for the will, power of attorney, beneficiary forms, custody recovery, or a real conversation with the family. It is a backup communication layer.",
            "A dead-man switch is a backup communication layer. The will, power of attorney, beneficiary forms, tested custody recovery, and family conversation still carry their own jobs.",
        ),
    ],
    "scripts/08-4_use-insurance-for-risks-the-stack-cannot-carry.md": [
        (
            "It does not cover every loss and it does not replace the underlying policies. Review the exclusions and required base limits rather than assuming the word umbrella means everything is covered.",
            "Umbrella coverage sits above the underlying policies and follows its own exclusions and required base limits. Read those terms before deciding which liability gaps it covers.",
        ),
        (
            "Do not cancel coverage only because Bitcoin rose during one market cycle. Reassess it using the full plan, the debts, the dependents, and the amount the household could reliably spend from the assets after taxes and market risk.",
            "Reassess coverage using the full plan, debts, dependents, and the amount the household could reliably spend from the assets after taxes and market risk. One Bitcoin market cycle is too narrow to establish that the family can self-insure the risk.",
        ),
        (
            "Orange Plan does not currently replace a policy inventory or quote comparison. Use the coverage-audit worksheet as the system of record and bring the gaps to a licensed insurance professional.",
            "Use the coverage-audit worksheet as the current system of record for policies and quote comparisons, then bring the gaps to a licensed insurance professional.",
        ),
        (
            "The finish line is not buying more insurance. It is knowing which risks the reserve and stack can carry, which risks still need a policy, and when each coverage will be reviewed again.",
            "Finish with a clear list of which risks the Reserve and stack can carry, which risks still need a policy, and when each coverage will be reviewed again.",
        ),
    ],
    "scripts/08-5_WALKTHROUGH_family-handoff.md": [
        (
            "**SAY** This planning screen does not update the legal beneficiary forms at the custodian or insurer. Those forms are checked separately and coordinated with the attorney.",
            "**SAY** Use this screen to coordinate the plan, then verify the legal beneficiary forms directly with the custodian or insurer and the attorney.",
        ),
    ],
    "scripts/advanced/A1-1_how-orange-plan-models-bitcoin.md": [
        (
            "Historical data cannot reveal the exact future distribution. Use the simulation count to compare decisions, find fragility, and understand the plan's dependence on sequence.",
            "Use historical data to build a documented range of market paths, then use the simulation count to compare decisions, find fragility, and understand the plan's dependence on sequence. The exact future distribution remains unknown.",
        ),
    ],
    "scripts/advanced/A3-1_price-context-before-a-large-bitcoin-move.md": [
        (
            "Price context does not tell you whether to buy or sell. It tells you what emotion is most likely influencing the decision.",
            "Price context identifies the emotion most likely influencing the decision. The full plan still decides whether a buy, sale, or borrowing move is supportable.",
        ),
    ],
    "scripts/advanced/A4-1_borrow-against-bitcoin-without-liquidation.md": [
        (
            "The useful question is not only today's LTV. It is how far Bitcoin can fall before each trigger.",
            "Translate today's LTV into the Bitcoin price and percentage decline that reaches each trigger.",
        ),
        (
            "The relationship is not linear. Starting twice as high can remove most of the crash cushion.",
            "The crash cushion shrinks nonlinearly as the starting LTV rises. Starting twice as high can remove most of the room before liquidation.",
        ),
        (
            "Bitcoin held for an automatic top-up is not the same thing as cash available to pay living expenses. And collateral held by a lender is not the same thing as Bitcoin in your own custody.",
            "Separate the resources by job: automatic top-up Bitcoin protects the loan, cash pays living expenses, and collateral at the lender carries different access and counterparty risk from Bitcoin in your own custody.",
        ),
        (
            "Loan proceeds generally are not income when a bona fide loan is created. A later liquidation is a sale of collateral and may create a taxable gain or loss.",
            "A bona fide loan generally provides proceeds without income at origination. A later liquidation sells collateral and may create a taxable gain or loss.",
        ),
    ],
    "scripts/advanced/A4-2_four-ways-debt-can-strengthen-a-plan.md": [
        (
            "The planning question is not whether debt can build wealth. It can.",
            "Debt can build wealth. The planning question is whether the specific debt makes this household stronger or more fragile.",
        ),
    ],
    "scripts/advanced/A5-1_rmd-pressure-and-roth-conversions.md": [
        (
            "The required beginning age depends on current law and the owner's birth year, so do not build the strategy around one age from an old article. The planning issue is the same: money may be forced out later, on top of Social Security, pensions, and other income.",
            "Verify the required beginning age under current law for the owner's birth year. The planning issue is that required distributions may later stack on top of Social Security, pensions, and other income.",
        ),
        (
            "An RMD itself generally cannot be converted. The required amount must first be distributed under the applicable rules, and any additional eligible amount can be considered separately.",
            "Distribute the required amount under the applicable rules first. Then consider a conversion of any additional eligible amount separately; the RMD itself generally is not convertible.",
        ),
    ],
    "scripts/advanced/A5-2_harvest-bitcoin-losses-and-gains.md": [
        (
            "For gain harvesting, remember that the zero-percent capital-gains bracket is not a separate empty bucket floating above the return. Long-term gains stack on top of ordinary taxable income.",
            "For gain harvesting, long-term gains stack on top of ordinary taxable income. That full stack determines how much room remains in the zero-percent capital-gains bracket.",
        ),
        (
            "Do not harvest simply because the dashboard shows a candidate. Ask what the realized amount does to the entire year's tax picture and whether the new basis is likely to matter for future spending or estate plans.",
            "Use the dashboard candidate as a starting point. Then calculate what the realized amount does to the entire year's tax picture and whether the new basis matters for future spending or estate plans.",
        ),
    ],
    "scripts/advanced/A6-1_health-coverage-before-medicare.md": [
        (
            "It is not health insurance. It is a membership and crowdfunding arrangement with its own eligibility, member-responsibility, bill-negotiation, and funding rules.",
            "CrowdHealth is a membership and crowdfunding arrangement with its own eligibility, member-responsibility, bill-negotiation, and funding rules. It is not health insurance.",
        ),
    ],
    "scripts/advanced/A6-2_sell-borrow-or-hold.md": [
        (
            "Borrowing keeps the collateral exposure at the beginning and generally does not create income merely because bona fide loan proceeds were received. The cost is interest, lender risk, LTV risk, collateral outside self-custody, and a repayment problem that still has to be solved.",
            "Borrowing keeps the collateral exposure and generally provides bona fide loan proceeds without income at origination. The trade-off is interest, lender risk, LTV risk, collateral outside self-custody, and a repayment problem that still has to be solved.",
        ),
        (
            "Holding means deciding that a core Bitcoin position is not a normal spending source. The Reserve, Bridge, income floor, and other accounts fund life while the core compounds or remains part of the estate.",
            "Holding assigns the core Bitcoin position a long-term or estate job. The Reserve, Bridge, income floor, and other accounts fund life while that core compounds.",
        ),
    ],
    "scripts/advanced/A7-1_compare-passphrase-multisig-institutional-custody-and-an-intentional-split.md": [
        (
            "One lost key does not necessarily destroy access, and one stolen key does not spend alone. That removes a single-key failure.",
            "A two-of-three wallet can survive one lost key, and one stolen key cannot spend alone. That removes a single-key failure.",
        ),
        (
            "The safest architecture is not the one with the most hardware or the strongest ideological label. It is the simplest combination that removes the household's actual failure points, preserves the amount of direct control the household values, and can still be recovered by the people who inherit the responsibility.",
            "The strongest architecture is the simplest combination that removes the household's actual failure points, preserves the amount of direct control the household values, and can still be recovered by the people who inherit the responsibility.",
        ),
    ],
    "scripts/advanced/A7-2_what-self-custody-asks-of-you.md": [
        (
            "Schedule a yearly recovery exercise using a test wallet or another procedure that does not expose live secrets. Review the locations, people, devices, software, and provider contacts.",
            "Schedule a yearly recovery exercise using a test wallet or another safe procedure, then review the locations, people, devices, software, and provider contacts. Keep live secrets out of the exercise.",
        ),
        (
            "The question is not whether self-custody is morally better. The question is which risks you want to own directly and whether the household can keep owning them for decades.",
            "Decide which risks you want to own directly and whether the household can keep owning them for decades. That is the useful self-custody question.",
        ),
    ],
    "scripts/advanced/A7-3_run-the-one-failure-test-across-methods-and-providers.md": [
        (
            "A setup does not become safer merely because the diagram has more boxes. It becomes safer when a real failure can happen and the family plan still survives.",
            "A setup becomes safer when a real failure can happen and the family plan still survives. Extra boxes help only when they remove a named failure.",
        ),
    ],
    "scripts/advanced/A8-1_do-you-need-a-trust.md": [
        (
            "The relevant number is not only today's net worth. It is what the estate may become under assumptions the household actually believes.",
            "Use both today's net worth and the projected estate under assumptions the household actually believes.",
        ),
        (
            "Do not assume one sentence waiving the prudent-investor rule solves every concentrated-Bitcoin trust. The attorney needs to draft the investment authority, concentration language, risk disclosures, delegation, custody powers, valuation process, and successor-trustee instructions for the governing state.",
            "A concentrated-Bitcoin trust needs complete investment authority, concentration language, risk disclosures, delegation, custody powers, valuation process, and successor-trustee instructions drafted for the governing state. One waiver sentence cannot carry all of those jobs.",
        ),
        (
            "Compare the projected estate with current federal and state exposure, but do not hard-code one exemption into a video. Then bring the report, custody map, family goals, and current ownership structure to an attorney and tax professional.",
            "Compare the projected estate with current federal and state exposure using the current exemption figures, then bring the report, custody map, family goals, and ownership structure to an attorney and tax professional. Keep the changing exemption figure out of the recorded video.",
        ),
        (
            "If the answers are vague, the plan is not ready to fund. A trust should make the transfer, control, or tax outcome clearer.",
            "Fund the trust after the transfer, control, tax outcome, and custody process are clear enough to execute.",
        ),
    ],
}


def main() -> None:
    if MARKER.exists():
        print("direct-voice pass 2 already applied")
        return

    changed_files = 0
    changed_lines = 0
    missing: list[str] = []
    for rel, pairs in REPLACEMENTS.items():
        path = ROOT / rel
        if not path.exists():
            missing.append(f"missing file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        before = text
        for old, new in pairs:
            if old in text:
                text = text.replace(old, new)
                changed_lines += 1
            elif new not in text:
                missing.append(f"text not found in {rel}: {old[:110]}")
        if text != before:
            path.write_text(text, encoding="utf-8")
            changed_files += 1

    if missing:
        raise RuntimeError("Direct-voice pass could not prove every replacement:\n- " + "\n- ".join(missing))

    MARKER.write_text(
        "# Direct-voice pass 2\n\n"
        f"Applied {changed_lines} reviewed affirmative rewrites across {changed_files} script files.\n\n"
        "The remaining negative statements are reserved for safety, legal, tax, custody, model interpretation, or explicit UI warnings.\n",
        encoding="utf-8",
    )
    print(f"applied {changed_lines} direct-voice rewrites across {changed_files} files")


if __name__ == "__main__":
    main()
