#!/usr/bin/env python3
"""Apply the Orange Plan V1 conceptual alignment and direct-voice pass.

This is intentionally deterministic. It rewrites the lessons materially affected
by the V1 product contracts, removes the reviewed copywriting-style negation
reversals from the remaining spoken scripts, updates the course authority files,
and leaves exact UI capture verification to the final Preview recording gate.
"""
from __future__ import annotations

import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIVIDER = "=" * 60


def dedent(text: str) -> str:
    return textwrap.dedent(text).strip() + "\n"


def render_script(num: str, title: str, body: str, *, advanced: bool = False,
                  source: str, gate: str | None = None) -> str:
    body = dedent(body)
    words = len(body.split())
    prefix = "ADVANCED TELEPROMPTER SCRIPT" if advanced else "TELEPROMPTER SCRIPT"
    lines = [
        f"{prefix} — segment {num}",
        f"{num} {title}",
        f"{words:,} words · ~{words / 155:.1f} min at 155 wpm · PRE-DICTATION FILMING DRAFT — Orange Plan V1 aligned and direct-voice reviewed",
        f"SOURCE: {source}",
    ]
    if gate:
        lines.append(f"PUBLICATION GATE: {gate}")
    return "\n".join(lines) + f"\n{DIVIDER}\n\n" + body


FULL_SCRIPTS: dict[str, str] = {
    "scripts/00-2_how-to-use-orange-plan-ai.md": render_script(
        "0.2",
        "How to use Orange Plan AI",
        """
        So in this lesson, we're going to cover how I would use Ask while building and maintaining a financial plan.

        Ask is available from the header throughout Orange Plan. It uses the page you are already viewing as context, so you can ask about the number or decision directly in front of you.

        On Home, I would use it to check whether the current accounts, holdings, activity, and debts look complete. On Cash Flow, I would ask whether the income, spending, taxes, debt payments, and amount left to save look believable. On Plan, I would ask what is driving the simulation result, the retirement dates, or a Current-versus-Preview comparison. On Protect, I would ask which unfinished item creates the largest family risk.

        Orange Plan still performs the calculations. Ask helps you understand the result, find missing information, compare trade-offs, and open the workspace where the real change gets modeled.

        Here are a few prompts I would use throughout the course:

        - Explain why this result changed.
        - Which three inputs are affecting this result the most?
        - What information looks missing, stale, or inconsistent?
        - Show me up to three realistic ways to improve this plan.
        - Compare Current and Preview in plain language.
        - What should I model before I take this question to my CPA, attorney, or insurance professional?
        - Take me to the page where I can review or change this.

        When Ask identifies a possible plan change, the decision moves into Current versus Preview. Read the exact before-and-after result, review the other outcomes that changed, and save it to the plan only when you actually want that decision in the baseline.

        Ask can also help you find unfinished work. It may point out an account with no holdings, an old debt rate, missing cost basis, a life event that has not been entered, a stale simulation result, or an unresolved item in Needs Attention.

        Linked activity follows the same rule. Orange Plan records the facts it can prove and keeps the receipt. Anything ambiguous becomes one focused question in Needs Attention. Ask can explain the question and take you to it; the accounting and reconciliation still happen in the account or activity workflow.

        The Daily Bitcoin Market Report gives you a quick read on the market without checking several sites. It can include the current price and recent change, distance from the prior high, ETF and public-company activity when it matters, leverage and futures conditions, the most useful on-chain change, and the larger macro or industry news.

        I use the report for context. The final question is whether anything changed a rule in the plan. Most market days update the value of the assets without changing the strategy.

        Orange Plan also has an AI Strategy Review Export for people who prefer ChatGPT, Claude, or another AI. The file removes personal information that the outside AI does not need and gives it a structured summary of the plan. Review the export before uploading it, then use the same prompts from this lesson.

        Keep seed phrases, private keys, wallet backups, passphrases, PINs, passwords, Social Security numbers, full account numbers, and backup-file passwords out of every AI tool. Treat the encrypted Orange Plan backup as a restoration file and keep that out of AI tools too.

        Before moving on, open Ask from the page you are currently reviewing and use one prompt tied to your own numbers. Then open the Daily Bitcoin Market Report and locate the AI Strategy Review Export. That is enough to know where these tools fit while you build the rest of the plan.
        """,
        source="PR #227 product direction for Ask, Current versus Preview, Needs Attention, and the V1 shell; Austin's 0.2 direction",
    ),
    "scripts/01-3_what-the-onboarding-retirement-age-actually-means.md": render_script(
        "1.3",
        "What the onboarding retirement age actually means",
        """
        So in this lesson, we're going to cover the retirement age from onboarding, the first simulation result, and how both change as the plan becomes more complete.

        Onboarding asks for a small amount of information so you can get a useful starting point quickly. It uses your age, income, spending, rough account values, Bitcoin holdings, and the growth model you selected.

        The onboarding age is a deterministic estimate. Orange Plan takes that one set of assumptions, projects it forward at different retirement ages, and finds the earliest age where that version of the plan lasts through the planning age.

        That estimate gives you direction before every account, debt, life event, tax record, and retirement-income decision has been entered. Treat it as the first answer from rough information.

        The Plan result adds a different question. Orange Plan runs the plan through 1,000 market paths and counts how many of them fund the plan as written through the planning age.

        A result of 790 of 1,000 means the money lasted through the planning age in 790 modeled paths. The normal Orange Plan standard is 800 of 1,000. Orange Plan uses that standard to calculate the earliest modeled retirement date for a normal user.

        The planned retirement date and the earliest modeled retirement date have different jobs. The planned date is the date you currently intend to use. The earliest modeled date is the first date that reaches the Orange Plan standard under the saved assumptions.

        The first result may be preliminary. Orange Plan uses four plain states:

        - Preliminary means important facts or accuracy details are still missing.
        - Current means the relevant facts and the calculation are up to date.
        - Stale means a modeled fact changed after the last calculation.
        - Unavailable means the calculation or required source data failed.

        Foundation replaces the rough account values with your real accounts and current holdings. Cash Flow verifies income, spending, taxes, debt payments, the Reserve, and expected life events. Allocation decides what the money is for and how new dollars get invested. Debt adds the real loan terms and the job assigned to each debt. Tax adds basis and the planning window. Retirement Income adds the spending, income floor, Bridge, withdrawal order, and guardrail policy. Protect completes the family side of the plan.

        Each completed area improves the information underneath the result. The age can move earlier or later as those inputs change. Better information produced a different answer.

        The first useful Plan result belongs in Foundation because it gives you something to read while the plan is still being built. Module 9 confirms the completed-plan baseline after the major facts and decisions are current.

        The Orange Plan standard stays fixed at 800 of 1,000 for normal users. A power user can change that standard under Advanced model settings, but the core course uses the same standard so the result stays easy to understand and compare.

        The main takeaway is simple: onboarding gives you a deterministic starting estimate. The simulation count shows how the fuller plan holds up across 1,000 market paths. Both become more useful as the information underneath them becomes accurate.

        In the Foundation walkthrough, I'll show you how to replace the rough account estimates with real accounts and holdings, review the assumptions, run or read the first preliminary Plan result, and see exactly which details could still change it.
        """,
        source="current deterministic onboarding behavior plus PR #227 fixed-standard, count-first, freshness, and retirement-date contracts",
    ),
    "scripts/03-1_set-the-bitcoin-allocation-you-can-actually-hold.md": render_script(
        "3.1",
        "Set the Bitcoin allocation you can actually hold",
        """
        So in this lesson, we're going to set a Bitcoin target the household can actually hold through a major drawdown.

        Your target comes from four things: how well you understand Bitcoin, the job it has in the plan, the volatility you have already lived through, and whether the rest of the financial plan can support the position.

        Conviction means you understand what you own well enough to keep following the plan when the price falls. A rising price can increase the position quickly, so the target still has to work when the market moves in the other direction.

        🎬 VISUAL — Week 3 allocation deck, Bitcoin path: Foundation, Integration, Optimization, Sovereign.

        The four paths describe where you are today. Use the description that matches your current understanding, experience, and support systems.

        Foundation is a smaller position while you are still learning. Bitcoin may be a hedge or an experiment, and the current account may be an exchange, brokerage, or ETF.

        Integration means Bitcoin has a defined role in the financial plan. You understand why you own it, it may replace some traditional growth exposure, and you are building the custody and tax knowledge around it.

        Optimization means Bitcoin is the main growth driver. You have already lived through real volatility, the position is intentional, and the Reserve, debt, taxes, account access, and custody are designed around it.

        Sovereign means Bitcoin is the primary long-term money in the plan. That position needs strong cash flow, enough accessible liquidity, a custody process the family can recover, and a retirement plan that can operate through a deep drawdown.

        Pick the description that is true today. The target should reflect the plan you can maintain now.

        Then translate the drawdown into dollars.

        🎬 VISUAL — Week 3 deck page 7: net-worth hit if Bitcoin falls 75%.

        If Bitcoin is 10% of the portfolio and falls 75% while everything else stays flat, the total portfolio falls about 7.5%.

        At 25% Bitcoin, the hit is about 19%.

        At 50% Bitcoin, the hit is about 37.5%.

        At 75% Bitcoin, more than half of the total portfolio value disappears on the statement.

        Use those numbers as a stress test. Put your own balance into it and calculate the dollar loss. Then ask what the household would actually do. Would you keep buying, hold, cut spending, add collateral to a loan, or feel pressure to sell?

        The household also has to keep operating while the asset is down. Check the Reserve, required debt payments, Bitcoin held with a lender, large purchases coming up, accessible Bridge money, and whether your spouse understands the expected volatility.

        The largest responsible position is the one the household can keep through a full drawdown without a forced sale or panic decision.

        A concentrated Bitcoin allocation can be intentional. It also gives the rest of the plan more work. The Reserve may need to be larger. Bridge money needs to stay accessible. Debt needs more room. Custody and family recovery need to handle a larger share of the family's wealth.

        Separate the target from an immediate trade. New contributions can move the portfolio toward the target over time. A one-time sale or shift has its own tax, timing, and risk decision.

        Price context helps identify the emotion around a large move. A sharp run-up usually adds urgency and overconfidence. A sharp drop usually adds fear and may also create a stronger expected entry. Cash flow, Reserve, debt, taxes, custody, and time horizon still decide whether the move fits the plan. The Advanced Library has the full price-context check.

        By the end of this lesson, you should have a target or range you can defend with three things: your understanding of Bitcoin, the dollar loss in a major drawdown, and the support systems around the position.

        In the Allocation walkthrough, we'll compare the current mix with that target, run the drawdown against the actual plan, and preview how contributions or a one-time shift would move the portfolio before anything is saved.
        """,
        source="Austin's allocation deck pages 4–7, Bitcoin-first planning philosophy, and V1 Current-versus-Preview language",
    ),
    "scripts/06-3_use-plan-confidence-and-guardrails-to-adjust-spending.md": render_script(
        "6.3",
        "Read the simulation result and use spending guardrails",
        """
        So in this lesson, we're going to read the 1,000-simulation result and use the spending guardrails that turn it into an annual operating rule.

        Orange Plan runs the completed plan through 1,000 market paths. Every path still includes the income, taxes, debts, life events, contributions, retirement spending, withdrawal order, and other decisions in the saved plan. The market sequence changes from one path to the next.

        If the result is 790 of 1,000, the money lasted through the planning age in 790 modeled paths. In the other 210, the exact plan as written did not last through that age.

        The simulation count measures the saved plan under the selected assumptions. It is a stress test for comparing decisions, rather than a personal probability of ruin.

        🎬 VISUAL — 1,000 plan paths ending in a large “790 of 1,000” count, with the through-age shown underneath.

        The normal Orange Plan standard is 800 successful simulations out of 1,000. Orange Plan uses that fixed standard to calculate the earliest modeled retirement date. Normal users see one clear standard instead of another percentage control to manage.

        The planned retirement date remains separate. That is the date the household currently intends to use. The earliest modeled date is the first date that reaches the Orange Plan standard.

        Read the freshness state beside the result too. Preliminary means important facts remain. Current means the facts and calculation are up to date. Stale means a modeled fact changed after the last calculation. Unavailable means the calculation or required source data failed.

        The goal is a plan the household actually wants that reaches the Orange Plan standard. Pushing the count toward 1,000 can require working longer or spending less than the household values.

        Current versus Preview shows what a proposed decision changes. A later retirement date, lower spending, higher savings, a different allocation, a tax strategy, debt payoff, or borrowing strategy should show the exact count before and after, along with the other outcomes that materially moved.

        Save a change only after the comparison makes sense. The saved plan remains Current until the preview is intentionally accepted.

        The spending guardrails handle the annual operating decision after retirement.

        🎬 VISUAL — Lower guardrail · Current portfolio · Upper guardrail on one horizontal line, followed by the annual review action.

        Orange Plan shows three portfolio values for the current year:

        - the lower guardrail;
        - the current retirement-portfolio value;
        - the upper guardrail.

        When the current portfolio is between the two guardrails, the spending plan stays in place and the normal inflation policy applies.

        Falling below the lower guardrail opens a spending review. The review calculates a lower spending amount that moves the plan back toward the policy's risk standard.

        Rising above the upper guardrail opens the same review in the other direction. The household can preview a higher spending amount instead of under-spending indefinitely.

        Each guardrail level is year-specific. It uses the same remaining cash flows, taxes, income, debts, assumptions, and planning age as the saved plan. The annual spending adjustment remains capped at 10%, so a large change can take more than one annual review.

        The core screen should answer one question in plain language: are you within the guardrails, below the lower guardrail, or above the upper guardrail? The Advanced methodology can explain the internal probability boundaries and inverse calculation behind those portfolio levels.

        The annual review also checks the Reserve. A weak market and a lower spending review may call for pausing a discretionary refill instead of selling assets into weakness. A healthy plan can refill toward the target. A Reserve near its hard floor still needs attention because the household has bills regardless of the market.

        By the end of this lesson, you should be able to explain four things: how many of 1,000 simulations worked, the planning age used, whether the result is current, and whether the portfolio is inside its spending guardrails.

        In the Retirement Income walkthrough, we'll read the current result, compare one strategy in Preview, save the withdrawal decision, and show where the portfolio guardrails and annual spending review live. Module 9 confirms the completed current baseline after every area is finished.
        """,
        source="PR #227 central simulation-result direction, accepted 800-of-1,000 standard, freshness states, and portfolio-guardrail decision",
    ),
    "scripts/09-1_keep-the-plan-current-without-rebuilding-it.md": render_script(
        "9.1",
        "Keep the plan current without rebuilding it every month",
        """
        So in this lesson, we're going to build the monthly and annual review rhythm that keeps the plan current.

        Maintenance updates the facts as life changes and revisits strategy on a schedule. The decisions from the course stay in place until a material fact or a planned review gives you a reason to change them.

        I use two rhythms: a short monthly pass and a full annual review.

        The monthly pass should take around five minutes in a quiet month.

        Start on Home. Review Needs Attention, recent activity, account balances, holdings, and debt monitoring. Orange Plan records exact purchases, sales, and uniquely proven internal transfers when the source and account mapping support them. Ambiguous withdrawals, deposits, transfers, corrections, or unsupported activity become one focused question in Needs Attention.

        Balance and holdings, recorded activity, and tax details are three separate truths. A linked account can have a fresh balance while some activity or cost basis still needs work. Read each status for the job it actually covers.

        Then open Cash Flow. Check income, living spending, taxes, required debt payments, the amount available to save, and the Reserve. One unusual month usually stays in the activity history. A repeated difference or permanent change updates the baseline.

        Open Plan when a modeled fact changed. Recalculate the result and read the freshness state. A price update can move current values and real risks such as LTV or taxes. A strategy change still needs a reason tied to the plan.

        Choose no more than one to three actions. A short list that gets completed is the useful output of the review.

        A quiet month is a successful review. Update the few facts that changed and stop.

        🎬 VISUAL — Monthly loop: Home → Cash Flow → Plan only when a modeled fact changed → one to three actions.

        The annual review is a four-destination lap.

        Home answers whether the current financial picture is true. Review the accounts, holdings, activity, debts, source coverage, and unresolved attention items.

        Cash Flow answers whether the monthly system is working. Review income, living spending, taxes, debt payments, the Reserve, and contribution routing.

        Plan answers whether the future still works. Read the simulation count and freshness, planned retirement date, earliest modeled date, allocation, tax strategy, retirement income, debt strategy, Bitcoin borrowing, and one important scenario. Any proposed strategy change stays in Preview until you save it.

        Protect answers whether the family can carry out the plan. Review beneficiaries, custody and access, recovery, heir instructions, trusted people, the dead-man switch, legal readiness, and the plan packet.

        🎬 VISUAL — Four-stop annual lap: Home → Cash Flow → Plan → Protect, ending with one to three actions and a fresh copy of Your Plan.

        Run the tax portion before year-end while there is still time to act. Prove one custody recovery, re-run the One-Failure Test, and confirm that the executor, beneficiaries, heir letter, and trusted contacts still fit.

        Recalculate the plan after the facts are current. Save a new copy of Your Plan and a fresh encrypted backup. Then put the next monthly and annual review dates on the calendar.

        Before moving on, choose the day of the month for the short review and the month for the annual review. The app stores the plan. The calendar protects the habit.
        """,
        source="V1 Home, Cash Flow, Plan, Protect ownership; Slice 1 account/activity continuity; Austin's five-minute review rule",
    ),
    "scripts/09-2_test-decisions-and-read-the-finished-plan.md": render_script(
        "9.2",
        "Test decisions separately and read Your Plan like a planner",
        """
        So in this lesson, we're going to test one decision without disturbing the saved plan and then read Your Plan in the order a planner would.

        The saved plan is Current. Scenarios test a focused question against that baseline.

        Ask one question at a time:

        What happens if I retire three years earlier?

        What happens if Bitcoin returns are lower than the saved assumption?

        What happens if we move to another state?

        What happens if we pay off this debt instead of investing the extra amount?

        What happens if Social Security starts at 62 instead of 70?

        Change only the inputs needed to answer the question. Orange Plan shows the differences between the saved plan and the scenario by default.

        A useful comparison includes the simulation count, planned and earliest modeled retirement dates, spending, taxes, accessible Bridge money, debt and LTV risk, Bitcoin remaining, and estate value when those outputs materially change.

        A scenario that wins becomes a Preview of the plan change. Read the exact before-and-after result, confirm which inputs changed, and save it to the plan only when the decision belongs in the baseline. Otherwise keep the scenario as evidence or delete it.

        🎬 VISUAL — Saved plan on the left, one scenario in the middle, Current versus Preview on the right with changed outputs highlighted.

        After every Build & improve area is intentionally complete, recalculate the completed plan. Read how many of 1,000 simulations worked, the through-age, the planned retirement date, the earliest modeled date at the 800-of-1,000 Orange Plan standard, and the freshness state.

        Then open Your Plan.

        Your Plan is a read-only document generated from the saved plan. It supports PDF, printing, and sharing. Fix any wrong information in the owning workspace, recalculate, and generate the document again.

        I would read it in four passes: position, trajectory, risk, and actions.

        Position asks where you stand today. Check the accounts, Bitcoin amount, ownership, cash, and debts. A wrong position stops the review because every downstream result depends on it.

        Trajectory asks where the plan is headed. Read the simulation count, planning age, planned retirement date, earliest modeled date, spending plan, and retirement funding together. The freshness label tells you whether those results can be trusted today.

        Risk asks what could break the plan. Review alternate Bitcoin paths, sequence risk, Reserve and Bridge funding, debt and LTV, taxes, custody, and family protection. The useful question is whether the household has a workable response.

        Actions are the one to three next steps. Each action should have an owner and a realistic time to completion.

        🎬 VISUAL — Your Plan reading order: Position → Trajectory → Risk → Actions.

        The assumptions and methodology explain what the outputs rest on. You should be able to defend the major return, inflation, spending, longevity, and tax inputs in plain language.

        Save one copy of Your Plan after each annual review with the year in the filename. The second copy creates the comparison that matters. Review net worth and Bitcoin share, simulation count and retirement dates, spending and guardrail status, and whether last year's actions were completed.

        Use Your Plan as the agenda for the family conversation. Give the relevant tax pages and lot export to the CPA. Give the no-secrets protection and custody summary to the estate attorney. These people can review a coherent plan without needing the household's app login.

        You started the course with scattered accounts and a rough estimate. The final walkthrough makes every area current, recalculates the plan, tests one decision, reads Your Plan in this order, and saves the first yearly PDF.
        """,
        source="PR #227 Scenarios, Current versus Preview, Your Plan, count-first result, and freshness contracts",
    ),
    "scripts/advanced/A1-1_how-orange-plan-models-bitcoin.md": render_script(
        "A1.1",
        "How Orange Plan models Bitcoin inside the simulation test",
        """
        So in this lesson, we're going to cover how Orange Plan creates the Bitcoin market paths behind the 1,000-simulation result.

        A useful simulation needs difficult market paths and a return process that matches the type of asset being modeled.

        Orange Plan gives Bitcoin its own return process because Bitcoin's historical return shape differs from a generic stock.

        The first difference is the tails. Extreme positive and negative years have occurred more often than a normal bell curve would suggest. A polite normal distribution can understate the outcomes a Bitcoin holder most needs to test.

        The second difference is asymmetry. Bitcoin has had very large upside years along with deep drawdowns. The model preserves room for both sides instead of forcing them into a perfectly symmetrical shape.

        The third difference is maturity. The volatility schedule can decline as Bitcoin grows, while difficult sequences remain possible. A larger asset requires more capital to move by the same percentage.

        The fourth difference is correlation. Bitcoin, stocks, inflation, and interest-rate conditions can become difficult at the same time. The simulation links major assets and economic variables so a stress path can contain several problems together.

        The straight-line growth assumption still controls the long-run premise. An unrealistic return assumption produces an unrealistic plan. Calibration keeps the random paths from adding another hidden layer of optimism: the median modeled result is checked against the deterministic projection under the same settings.

        Strategy comparisons use matched paths. Retiring at 60 and retiring at 65 face the same 1,000 market sequences. Selling and borrowing face the same sequences too. The comparison changes the decision while holding the weather constant.

        The result is repeatable. The same inputs and saved settings produce the same simulation count. A changed result points to a changed market value, plan fact, assumption, or strategy.

        The normal product uses the Orange Plan standard of 800 successful simulations out of 1,000. A custom standard belongs under Advanced model settings. Changing that standard changes which retirement date qualifies; it does not change the market paths or make the plan itself safer.

        Historical data cannot reveal the exact future distribution. Use the simulation count to compare decisions, find fragility, and understand the plan's dependence on sequence. Treat it as a model with documented assumptions.

        The current distributions, volatility schedule, correlations, caps, calibration tests, and through-age definition belong in Help & Methodology. Before recording, verify that the explanation and production engine still match the same app commit.
        """,
        advanced=True,
        source="PR #227 fixed-standard and count-first product contract plus existing Monte Carlo methodology",
        gate="Research complete. Record after Help & Methodology, production settings, and the exact simulation engine are checked against the same app commit used on camera.",
    ),
}


FULL_WALKTHROUGHS: dict[str, str] = {
    "scripts/01-4_WALKTHROUGH_foundation.md": dedent("""
        # 1.4 · WALKTHROUGH — Replace the onboarding estimate with real Foundation data

        **Screen capture · about 20 minutes**

        > **V1 capture gate:** The product route below follows the approved Home / Plan / Cash Flow / Protect architecture. Verify every final label and click path against the same Preview commit used for recording.
        > **DO** = action on screen · **SEE** = point at this result · **⚠** = avoid this mistake
        > Narrate naturally. This sheet is not a teleprompter.

        ## Before recording

        - Complete the short onboarding with rough values.
        - Use a demo account with no real accounts or holdings entered yet.
        - Have a statement list ready: account names, owners, current quantities, and cash balances.
        - Start with the onboarding estimate and no completed current Plan receipt.

        ## 1 · Orient the learner

        **DO** Land on Home after onboarding.

        **SEE** The current financial summary and the starting retirement estimate.

        **SAY** The onboarding age is the deterministic starting estimate from Lesson 1.3. The Plan result becomes more useful as real facts replace the rough inputs.

        **DO** Plan → **Build & improve**.

        **SEE** One next task by default and quiet **View all** access.

        **SAY** Build & improve is the implementation roadmap. The course teaches the decisions; each walkthrough opens the workspace that owns the data.

        ## 2 · Verify household details

        **DO** Build & improve → Household basics / Plan details.

        **CHECK** date of birth or age · state or country · filing status · spouse details where applicable.

        **⚠** Fix the source field. Calculated tax and retirement totals update from that source.

        ## 3 · Add the real accounts

        **DO** Home → Accounts → **Add account**.

        **ENTER** account type · recognizable name · owner.

        **SHOW** at least one cash account, one retirement or brokerage account, and the actual Bitcoin custody location: exchange, hardware wallet, collaborative custody, IRA, or ETF account.

        **SAY** The account is the container. Bitcoin, cash, funds, property, and other assets are holdings inside it.

        **DO** Point at **Link account** without waiting on a live connection.

        **SAY** Linking is optional. Manual entry and supported imports can produce the same honest current position.

        ## 4 · Add current holdings

        **DO** Open an account → Holdings → **Add holding**.

        **ENTER** Bitcoin as quantity · stocks or funds as ticker and shares where supported · cash as the current balance · property or other assets with current value.

        **SEE** Home and account totals update.

        **⚠** Enter basis when it is already known. Module 5 reconstructs missing purchase history.

        ## 5 · Explain activity, balance, and tax-detail coverage

        **DO** Open Account → Activity and Home → Activity.

        **SEE** recorded activity, source receipts, coverage or status language, and Needs Attention.

        **SAY** Orange Plan keeps three questions separate: what the account owns now, which activity has been recorded, and how much tax history or basis is supported.

        **SHOW** one exact purchase or sale receipt when the demo data supports it.

        **SHOW** one focused Needs Attention question for an ambiguous withdrawal, deposit, transfer, or correction.

        **SAY** Facts Orange Plan can prove are recorded with provenance. Anything it cannot prove waits for one plain answer.

        **⚠** An internal transfer preserves total quantity, acquisition date, and basis. Never represent it as a sale followed by a purchase.

        **⚠** Keep full historical tax reconstruction for Module 5.

        ## 6 · Verify the current position

        **DO** Expand each account on Home and open the account detail when needed.

        **CHECK** owner · account type · quantity · current value · custody location.

        **SEE** net worth and Bitcoin share.

        **SAY** Fix any wrong total at the row or source that created it.

        ## 7 · Review the baseline assumptions

        **DO** Plan → Build & improve → Advanced → Return assumptions.

        **CHECK** Bitcoin model · inflation · planning age · other asset assumptions.

        **OPTIONAL** Show custom return windows without building one.

        **SAY** Choose assumptions you can defend. Then use Scenarios for a different future instead of repeatedly changing the saved baseline.

        ## 8 · Run or read the first Plan result

        **DO** Plan → Overview → calculate or refresh the result.

        **SEE** simulations worked out of 1,000 · through-age · planned retirement date · earliest modeled date · Preliminary / Current / Stale / Unavailable state.

        **SAY** The Orange Plan standard is 800 of 1,000. This first result may remain Preliminary while other Build & improve areas are unfinished.

        **POINT OUT** the concise provenance: accounts included, recalculation time, and details that could still change the result.

        ## 9 · Close Foundation

        **DO** Return to Plan → Build & improve → Foundation / Get your first plan.

        **SEE** household basics, accounts, current holdings, assumptions review, and first result complete from real data.

        **SAY** Cash Flow owns income, living spending, taxes, debt payments, the Reserve, and expected life events. The later modules improve allocation, debt, tax, retirement income, and protection.

        ## Foundation checkpoint

        - Household details are accurate.
        - Every real account and custody location is listed.
        - Current holdings match the source statements.
        - Balance, activity, and tax-detail coverage are understood separately.
        - Transfers cannot duplicate quantity or basis.
        - Assumptions were reviewed deliberately.
        - The first Plan result is visible with a truthful freshness state.
        - Build & improve shows Foundation complete.
        """),
    "scripts/06-4_WALKTHROUGH_retirement-paycheck.md": dedent("""
        # 6.4 · WALKTHROUGH — Build the retirement paycheck

        **Screen capture · about 18 minutes**

        > **V1 capture gate:** Verify final Retirement Income, Bitcoin Borrowing, guardrail, and Save-to-plan labels against the same Preview commit used for recording.

        ## Before recording

        - Retirement spending decision from Lesson 6.1.
        - Current Social Security estimates and start ages.
        - Pension or other durable-income details.
        - Healthcare bridge estimate when retirement begins before Medicare.
        - Account timeframes and contribution plan from Module 3.
        - Tax-window work from Module 5.

        ## 1 · Confirm retirement spending

        **DO** Plan → Build & improve → Retirement income.

        **ENTER / VERIFY** planned retirement date · baseline annual spending · healthcare · irregular costs.

        **SAY** Required debt payments remain modeled separately from living spending.

        **DO** Add large irregular costs as life events.

        ## 2 · Add the healthcare bridge when needed

        **DO** Build & improve → Life events → Expense change.

        **ENTER** start at retirement · current annual premium or retained cost · duration until Medicare or the chosen transition date.

        **⚠** Use current quotes.

        ## 3 · Build the income floor

        **DO** Retirement income → Social Security, pensions, and other durable income.

        **ENTER** each amount in the unit the field requests.

        **SEE** the income floor and year-by-year funding update.

        ## 4 · Read the gap and Bridge years

        **DO** Open early retirement years in the year-by-year view.

        **SEE** spending need · durable income · portfolio-funded gap.

        **COUNT** the years before retirement-account access, Social Security, pension, or other income begins.

        **COMPARE** the gap with accounts assigned to Bridge.

        **SAY** The Bridge has to exist in money the household can actually access.

        ## 5 · Compare Social Security timing when material

        **DO** Plan → Scenarios → compare an earlier and later claiming age.

        **READ** benefit size · Bridge withdrawals · taxes · Bitcoin or portfolio remaining.

        **SAY** Waiting produces a larger check and uses more portfolio money during the Bridge. Compare both sides on the same plan.

        ## 6 · Preview the withdrawal strategy

        **DO** Retirement income → Withdrawal order / income strategy.

        **SHOW** account order and what is sold inside accounts as separate choices.

        **COMPARE** Current with a tax-aware, sequential, proportional, or custom Preview supported by the build.

        **SEE** simulation count · retirement dates · lifetime taxes · Bitcoin remaining · after-tax result.

        **DO** **Save to plan** only after the comparison is understood.

        **SAY** Current remains the saved strategy. Preview shows the proposed change until it is saved.

        ## 7 · Read the Reserve / Bridge / Legacy draw-and-refill system

        **SEE** the Reserve, account timeframes, and annual refill status.

        **SAY** Spending comes from the Reserve. Bridge refills it. Legacy refills Bridge when the plan and market conditions support the move.

        **⚠** The annual rule supports the decision; it does not predict a good sale day.

        ## 8 · Preview sell, borrow, or hold

        **DO** Plan → Build & improve → Bitcoin borrowing.

        **COMPARE** sell-only, bracket-aware, borrow-first, or custom strategies supported by the current build.

        **SEE** interest · debt · LTV · runway · Bitcoin at lender versus custody · taxes · simulation result · projected estate.

        **DO** **Save borrowing strategy to plan** only when the decision belongs in Current.

        **SAY** Orange Plan models the strategy. The actual sale, loan, collateral move, or repayment happens with the provider and gets recorded after completion.

        ## 9 · Read the simulation result and spending guardrails

        **DO** Return to Retirement income / annual spending review.

        **SEE** simulations worked out of 1,000 · through-age · freshness state.

        **SEE** lower guardrail · current retirement portfolio · upper guardrail · status.

        **SAY** The Orange Plan standard is 800 of 1,000. The guardrail summary says whether an annual spending review is needed.

        **IF REVIEW NEEDED** Open the separate review, read Current versus Preview spending and the simulation result, then stop before saving unless the demo state is meant to show an actual annual decision.

        **SEE** the 10% annual adjustment cap and Reserve refill status where the final V1 build displays them.

        ## 10 · Close Retirement income

        **DO** Plan → Build & improve → Retirement income.

        **SEE** planned date and spending · income floor · Bridge · Social Security · withdrawal strategy · simulation result · guardrail status complete.

        ## Module 6 checkpoint

        - Retirement spending, healthcare, and irregular costs are honest.
        - The income floor and gap can be stated from memory.
        - Bridge years and accessible funding are verified.
        - Social Security timing was compared when material.
        - A withdrawal strategy was previewed and intentionally saved.
        - Sell, borrow, or hold remains Preview until intentionally saved.
        - The simulation result is read as a count with a truthful freshness state.
        - The portfolio guardrail status is understood.
        """),
    "scripts/09-3_WALKTHROUGH_finish-test-review-and-save.md": dedent("""
        # 9.3 · WALKTHROUGH — Finish, test, review, and save the plan

        **Screen capture · about 22 minutes**

        > **V1 capture gate:** Verify the final Home, Plan, Cash Flow, Protect, Ask, Your Plan, Current-versus-Preview, and Settings labels against the same Preview commit used for recording.

        ## Before recording

        - Every prior module completed on the demo plan.
        - Current accounts, activity, cash flow, debts, allocation, tax history, retirement income, beneficiaries, custody map, and heir letter entered.
        - One meaningful scenario question prepared.
        - Calendar open for monthly and annual review dates.

        ## 1 · Close every Build & improve area intentionally

        **DO** Plan → Build & improve → View all.

        **WALK** Get your first plan · Improve accuracy · Improve strategy · Advanced where used.

        **SEE** complete, truthfully not applicable, or one precise missing-data line.

        **FIX** open source facts before recalculating.

        **SAY** The plan is complete when the real data and saved decisions exist.

        ## 2 · Recalculate the completed plan

        **DO** Plan → Overview → calculate / refresh.

        **SEE** the full 1,000 simulations complete.

        **READ** simulations worked out of 1,000 · through-age · Current freshness state · provenance.

        **SAY** This is the completed-plan baseline. Earlier results were useful while the plan was being built; this one uses the finished core data and saved strategy.

        ## 3 · Read both retirement dates

        **SEE** planned retirement date and earliest modeled retirement date.

        **SAY** The earliest modeled date is the first date that reaches the Orange Plan standard of 800 successful simulations out of 1,000. The planned date is the household's saved intention.

        **⚠** Normal users do not choose another standard here. Custom standards live under Advanced model settings.

        ## 4 · Read the spending guardrails

        **DO** Plan → Retirement income / annual spending review.

        **SEE** lower guardrail · current retirement portfolio · upper guardrail · status.

        **IF INSIDE** Confirm that no spending review is needed.

        **IF OUTSIDE** Open the separate review and read Current versus Preview spending, simulation count, and the 10% annual cap before saving.

        **SEE** Reserve refill status.

        ## 5 · Run one focused scenario

        **DO** Plan → Scenarios → answer **What do you want to test?**

        **CHANGE** only the inputs needed.

        **COMPARE** saved plan with no more than two scenarios at once.

        **READ** simulation count · retirement dates · spending · taxes · accessible money · debt / LTV · Bitcoin or estate value when material.

        **MOVE** the winning decision into Current versus Preview.

        **DECIDE** Save to plan, keep the scenario as evidence, or delete it.

        ## 6 · Run the five-minute monthly pass

        Start a visible timer.

        **DO** Home → Needs Attention and recent Activity.

        **REVIEW** one exact receipt and one focused unresolved question when available.

        **DO** Cash Flow → This month → verify spending and the Reserve.

        **CHOOSE** one to three actions and stop the timer.

        **SAY** A quiet month is a successful review.

        ## 7 · Walk the annual four-destination review

        **HOME** Accounts, holdings, activity, debts, source coverage, Needs Attention.

        **CASH FLOW** Income, living spending, taxes, debt payments, Reserve, saving and routing.

        **PLAN** Simulation result, retirement dates, allocation, tax, retirement income, debt strategy, borrowing, one scenario.

        **PROTECT** Beneficiaries, custody and access, recovery, heir instructions, trusted people, dead-man switch, legal and estate readiness.

        **APPLY** an annual spending or strategy update only when the demo state makes it due and the comparison is understood.

        ## 8 · Read Your Plan in planner order

        **DO** Plan → **View full plan** or Profile → **Your plan**.

        **READ**:

        1. Position — does today's account and debt picture match reality?
        2. Trajectory — simulation count, planning age, retirement dates, spending, and funding.
        3. Risk — alternate paths, taxes, debt, custody, and protection.
        4. Actions — one to three next steps.

        **CHECK** result freshness, assumptions, and methodology.

        ## 9 · Save the yearly artifacts

        **DO** Print / Save Your Plan as PDF with the year in the filename.

        **DO** Profile → Settings → Data and privacy → Backup & Restore → create a fresh encrypted plan export.

        **SAY** Your Plan is the readable annual document. The encrypted export restores the app data. A Bitcoin wallet backup is a separate object.

        ## 10 · Schedule the rhythm

        **DO** Calendar → recurring monthly review and annual review.

        **RECORD** the tax review before year-end and custody / estate check inside the annual session.

        ## Final checkpoint

        - Every Build & improve area is intentionally complete.
        - The completed 1,000-simulation result is Current.
        - Planned and earliest modeled retirement dates are understood separately.
        - Portfolio guardrail status and annual-review rule are understood.
        - One scenario was tested and any winning decision moved through Current versus Preview.
        - Monthly and annual review dates are on the calendar.
        - Your Plan PDF and encrypted backup are saved.
        - One to three next actions are clear.
        """),
}


# Exact reviewed rewrites for the remaining course. Each old phrase was surfaced
# by the direct-voice audit and is replaced with the affirmative fact that does
# the teaching. Necessary safety and legal negatives are intentionally retained.
REPLACEMENTS: dict[str, list[tuple[str, str]]] = {
    "scripts/00-1_how-to-use-this-course.md": [
        (
            "Your date is also going to move with that confidence level. This is a living financial plan that you can check in with regularly. This is not a spreadsheet you're going to build and use once and not open again. This is built and designed for you to be able to constantly make updates and changes and know exactly where you are at any given time.",
            "Your planned retirement date and simulation result are going to move as the information changes. This is a living financial plan you can update regularly so you know where you stand at any given time.",
        ),
        ("3. What level of confidence you can have in that plan.\n4. How many future scenarios your plan's going to hold up in.",
         "3. How many of 1,000 simulations fund the plan as written.\n4. Which market and life scenarios the plan can handle."),
        ("You'll learn how to read the retirement date and confidence number, but the first full confidence run happens after the plan is built in Module 9.",
         "You'll learn how to read the first preliminary simulation result. Module 9 saves the completed current baseline after the facts and major strategy decisions are in place."),
        ("ways to optimize this to reduce your tax liability", "ways to improve this and reduce your tax liability"),
        ("Build Your Plan is the checklist underneath both of them.", "Build & improve is the roadmap underneath both of them."),
        ("one annual review, scenarios, and a yearly report.", "one annual review, focused scenarios, and a yearly copy of Your Plan."),
    ],
    "scripts/01-1_what-to-gather-before-you-build-the-plan.md": [
        ("Onboarding only asked for enough information to give you a starting estimate. It did not add every real account, debt, life event, or tax record. The Build Your Plan guide is going to take you through those pieces in the right order, and each module walkthrough is going to enter the information that belongs to that part of the plan.",
         "Onboarding asked for enough information to give you a starting estimate. Build & improve takes you through the real accounts, debts, life events, and tax records in the order each module uses them."),
        ("Gathering everything now does not mean entering everything in this module.",
         "We will enter each item in the module that owns it."),
        ("Run Your Plan performs the first full 1,000-run confidence check after the plan is built.",
         "Module 9 confirms and saves the completed current simulation result after the core plan is built."),
        ("You do not need to enter any of this yet. Put the statements, exports, employer information, and rough future-event list in one place.",
         "For now, put the statements, exports, employer information, and rough future-event list in one place."),
    ],
    "scripts/01-2_the-three-layers-of-a-plan-and-setting-your-assumptions.md": [
        ("They might not be happening now, but you have a high level of confidence that they're going to happen. Some examples are future college payments, how your spending might change in retirement, a new car you're planning to purchase, a house you're planning to purchase or sell, a future change in your job or income, or long-term care expenses later in retirement.",
         "These are future expenses or income changes you expect with a high level of confidence. Examples include college payments, retirement spending changes, a car or home purchase, a future job or income change, or long-term care expenses later in retirement."),
    ],
    "scripts/02-1_find-the-surplus-your-plan_can_actually_use.md": [],
    "scripts/02-1_find-the-surplus-your-plan-can-actually-use.md": [
        ("Keep is anything essential or clearly worth what it costs. The goal is not to make your life miserable just to make a projection prettier.",
         "Keep anything essential or clearly worth what it costs. Look for spending that adds little value before touching the life you want to keep."),
        ("Cut means it is not worth paying for at all. Unused subscriptions, recurring charges you forgot, or spending that is not buying much happiness or utility.",
         "Cut removes unused subscriptions, forgotten recurring charges, and spending that adds little happiness or utility."),
        ("That is not the amount you want to live on. It is the minimum amount the household could run on during a job loss, a business slowdown, or a major Bitcoin drawdown.",
         "Bare-bones spending is the minimum amount the household could run on during a job loss, a business slowdown, or a major Bitcoin drawdown."),
        ("The goal is not a perfect refund. It is making sure the monthly number is honest.",
         "Set withholding so the monthly surplus reflects the taxes you actually expect to owe."),
    ],
    "scripts/02-2_size-your-cash-reserve-in-months-of-spending.md": [
        ("By bare bones, this is not going to be what you normally spend in any given month. This is going to be the absolute minimum amount that you can spend and still get by.",
         "Bare-bones spending is the absolute minimum amount you can spend in a month and still get by."),
        ("I don't think there's a wrong answer here. A lot of this, like I said, comes down to your risk tolerance.",
         "Your risk tolerance sets the final number."),
    ],
    "scripts/02-3_add-the-future-changes-your-plan-should-expect.md": [
        ("That fourth question does not mean we are deciding the debt strategy in this lesson. It simply keeps us from acting as if every future purchase must be fully saved in cash today. The Debt module decides whether financing improves or weakens the plan. The Allocation module decides how new dollars are invested and which money needs to stay accessible.",
         "Keep the financing question open here. The Debt module decides whether financing improves or weakens the plan. The Allocation module decides how new dollars are invested and which money needs to stay accessible."),
        ("If the event is more than five years away, Bitcoin can remain part of the funding plan. I would not automatically move the entire future expense into cash at year five. The part you have firmly promised should become less dependent on Bitcoin as the date gets closer. The flexible portion can stay invested longer.",
         "If the event is more than five years away, Bitcoin can remain part of the funding plan. Start protecting the firmly promised portion as the date gets closer. The flexible portion can stay invested longer."),
    ],
    "scripts/02-4_optional-decide-how-much-college-help-you-are-funding.md": [
        ("A lot of conventional college planning starts with the 529. I do not think that should be automatic for a Bitcoiner.",
         "For a Bitcoiner, start with the family commitment and funding sources, then decide whether a 529 improves that plan."),
        ("For my own planning, if college is still more than five years away, I am comfortable using Bitcoin as a meaningful part of the savings plan instead of assuming every dollar has to go into a 529. That does not mean I would wait until freshman year and hope the price cooperates.",
         "For my own planning, if college is still more than five years away, I am comfortable using Bitcoin as a meaningful part of the savings plan. As the date gets closer, I would protect the first committed tuition payments so the family is not depending on the market at enrollment."),
    ],
    "scripts/02-5_WALKTHROUGH_cash-flow-reserve-life-events.md": [
        ("**SAY** One unusual month does not automatically change the baseline. Look for a repeated difference or a permanent change.",
         "**SAY** Update the baseline after a repeated difference or a permanent change. Keep a genuine one-time month in the activity history."),
    ],
    "scripts/03-2_give-each-dollar-a-job-before-choosing-the-investment.md": [
        ("This does not mean every Bridge account needs a conventional stock-and-bond portfolio. A high-conviction Bitcoiner may keep more Bitcoin involved, especially when the need is still more than five years away. It means the portion that is firmly committed has to become less dependent on Bitcoin as the date gets close.",
         "A high-conviction Bitcoiner may keep more Bitcoin in the Bridge while the need is still more than five years away. Protect the firmly committed portion as the date gets close."),
        ("A savings account is not automatically Reserve unless you have actually designated that cash for the reserve.",
         "A savings account becomes Reserve when you designate that cash for the reserve job."),
        ("The goal is not to classify every holding perfectly. It is to make sure the major accounts have jobs and that the investment inside each one is compatible with that job.",
         "Give the major accounts a job and make the holdings inside each one compatible with that job."),
    ],
    "scripts/03-4_put-the-right-holdings-inside-the-right-accounts.md": [
        ("That makes Roth space valuable, but it does not mean Roth is always the correct contribution choice.",
         "Roth space is valuable, and the contribution choice still depends on the current bracket, expected future bracket, access needs, and investment menu."),
        ("Your overall target may be seventy percent Bitcoin and thirty percent other assets. That does not mean every account has to hold the same seventy-thirty mix. One account may hold the Bitcoin exposure, another may hold cash for the Reserve, and another may hold the assets that are available inside the employer plan.",
         "Your overall target may be 70% Bitcoin and 30% other assets while the account-level mixes differ. One account may hold the Bitcoin exposure, another may hold Reserve cash, and another may use the assets available inside the employer plan."),
    ],
    "scripts/04-1_decide-what-every-debt-should-do.md": [
        ("You may reasonably keep a low-rate mortgage and continue accumulating Bitcoin. That does not automatically mean taking a new Bitcoin-backed loan to buy more is also reasonable. New leverage needs a much higher standard because it adds a new payment, a lender, and potentially forced-sale risk.",
         "Keeping existing low-rate debt and adding new leverage are separate decisions. A new Bitcoin-backed loan needs a higher standard because it adds a payment, a lender, and forced-sale risk."),
        ("I do not mean one universal percentage that everybody copies. I mean the point where you would stop adding debt because either the monthly payments, the drawdown stress, or the amount tied to a lender has become more than your household can comfortably carry.",
         "Your debt ceiling is the point where monthly payments, drawdown stress, or the amount tied to a lender becomes more than the household can comfortably carry."),
    ],
    "scripts/05-1_cost-basis-know-what-you-paid-before-you-plan-a-sale.md": [
        ("The blockchain can show that the coins moved. It does not automatically tell a tax program what you originally paid or why the transfer happened.",
         "The blockchain can prove that the coins moved. The tax record still needs the original basis and the reason for the movement."),
        ("Specific identification also requires discipline. It is not enough to decide after the fact that the most favorable lot was sold. The records and the transaction process need to support which units were disposed of. When that is not possible, the applicable default ordering rules may control.",
         "Specific identification requires records and a transaction process that support which units were disposed of at the time of the sale. Applicable default ordering rules may control when those records are missing."),
        ("The goal is not a beautiful dashboard. The goal is being able to answer a real question before money moves: if I sell this amount, which lot is being sold, what is the gain, and what tax range should I expect?",
         "The useful output is an answer before money moves: which lot is being sold, what is the gain, and what tax range should I expect?"),
    ],
    "scripts/05-2_use-the-tax-buckets-and-low-income-window-on-purpose.md": [
        ("The important detail is that gains stack on top of the rest of your taxable income, so a low salary does not automatically mean an unlimited amount of gains will be taxed at zero.",
         "Gains stack on top of the rest of taxable income, so the available 0% long-term capital-gains space is limited by the whole return."),
        ("That makes Roth space valuable for long-term growth, but it does not mean every dollar should automatically go there.",
         "Roth space is valuable for long-term growth. The right contribution mix still depends on the tax rate now, the expected rate later, and access needs."),
        ("That does not make the strategy unusable. It means the app can model a range, and the exact current-year amount gets verified with a tax professional before execution.",
         "Use the app to model a range, then verify the exact current-year amount with a tax professional before execution."),
    ],
    "scripts/06-1_build-spending-income-floor-gap-and-bridge.md": [
        ("This is not only the average of what you spend today. Retirement spending needs to include the life you actually expect to live in the early years, healthcare, and the irregular expenses that do not show up every month.",
         "Retirement spending includes the life you expect in the early years, healthcare, and irregular expenses along with the normal annual spending."),
        ("I would be careful with income that is not truly durable. A dividend is not guaranteed in the same way as Social Security or a pension. Rental income can be reliable but still has vacancies and repairs. The floor should be something you can defend.",
         "Use durable income for the floor. Social Security and pensions have different reliability than dividends or rental income, which can change with distributions, vacancies, and repairs."),
        ("The lowest-tax conversion is not automatically the lowest total cost after healthcare. That comparison is covered in more detail in the Advanced health-insurance lesson.",
         "Compare conversion tax and healthcare subsidy effects together. The Advanced health-coverage lesson walks through that combined cost."),
    ],
    "scripts/06-2_choose-withdrawal-order-and-refill-rule.md": [
        ("Borrowing can provide liquidity without an immediate sale, but it adds interest, counterparty risk, LTV risk, and the possibility of a forced liquidation. Loan proceeds are generally not income when the loan is created, but a later liquidation, forgiveness, or other event can have tax consequences. Borrowing works best when it is planned from strength, not used because the household is trapped.",
         "Borrowing can provide liquidity while adding interest, counterparty risk, LTV risk, and forced-liquidation risk. Loan proceeds are generally outside income at origination; liquidation, forgiveness, or restructuring can create tax consequences. Plan the purpose, repayment source, and drawdown response while the household has room."),
    ],
    "scripts/07-1_self-custody-professional-custody-and-when-a-split-makes-sense.md": [
        ("A split is not automatically better. Every additional setup needs to solve a named risk. Otherwise it is just extra complexity.",
         "Use a split when each additional setup solves a named risk the family can maintain."),
        ("It does not say every large balance belongs in multisig. It does not say institutional custody is only for beginners. It does not say every household needs three different setups.",
         "A large balance can use direct self-custody, collaborative multisig, institutional custody, or an intentional combination. The right architecture depends on the failures the household needs to survive."),
        ("That last line matters. The goal is not the most advanced setup. It is the simplest setup that removes the household's real failure points and can still be maintained ten or twenty years from now.",
         "Choose the simplest setup that removes the household's real failure points and can still be maintained ten or twenty years from now."),
        ("A household can reach the fourth outcome with one strong method or a thoughtful combination. It does not mean graduating every coin into one increasingly complicated wallet.",
         "A household can reach the fourth outcome with one strong method or a thoughtful combination that removes catastrophic concentration."),
    ],
    "scripts/07-3_fix-single-points-of-failure-and-harden-accounts.md": [
        ("Redundancy means one event does not erase every recovery path. It does not mean buying more hardware until the diagram looks complicated.",
         "Redundancy gives the family another recovery path for the failure being addressed. Add equipment only when it solves that specific failure."),
    ],
    "scripts/08-1_choose-who-is-in-charge-and-put-the-legal-baseline-in-place.md": [
        ("Trusts are an advanced decision. They may be useful for probate avoidance, incapacity planning, family control, asset protection, tax planning, or a complicated family situation. They are not automatically required because somebody owns Bitcoin, and a revocable trust is not automatically an estate-tax solution.",
         "Trusts are an advanced decision used for jobs such as probate avoidance, incapacity planning, family control, asset protection, tax planning, or a complicated family situation. Bitcoin ownership by itself does not establish the need, and a revocable trust generally serves different jobs from estate-tax planning."),
    ],
    "scripts/08-2_align-legal-authority-with-the-technical-recovery-path.md": [],
    "scripts/08-2_align-legal-authority-with-technical-recovery.md": [
        ("You do not need to expose a real seed to the family. You can use a trivial-value test wallet or a documented tabletop exercise to confirm everybody knows the first call, the role they have, and the components that exist.",
         "Use a trivial-value test wallet or a documented tabletop exercise to confirm that everybody knows the first call, the role they have, and the components that exist. Keep real recovery secrets out of the exercise."),
    ],
    "scripts/08-3_write-the-heir-letter-and-create-the-backstop.md": [
        ("It is not the will. It is not the wallet backup.",
         "The heir letter is a no-secrets orientation document for the family."),
        ("The purpose is not to release keys. It is to make sure somebody starts the process.",
         "The scheduled delivery makes sure somebody starts the documented process. It carries the no-secrets letter and never releases keys."),
    ],
    "scripts/advanced/A5-1_rmd-pressure-and-roth-conversions.md": [
        ("The goal is not automatically to convert as much as possible. It is to compare the rate paid now with the expected lifetime cost of leaving the money in the Traditional account.",
         "Compare the rate paid now with the expected lifetime cost of leaving the money in the Traditional account, then choose the conversion range that uses the window well."),
    ],
    "scripts/advanced/A5-3_state-taxes-and-relocation.md": [
        ("A move that saves tax but makes life worse is not automatically an optimization.",
         "Include the lifestyle cost beside the tax savings. The move needs to improve the full plan and the life attached to it."),
    ],
    "scripts/advanced/A7-1_compare-passphrase-multisig-institutional-custody-and-an-intentional-split.md": [
        ("Three different devices are not automatically safer if nobody can remember which software, cable, firmware, or signing order works ten years later.",
         "Device diversity helps only when the family can maintain the software, firmware, cables, and signing process over time."),
        ("The point is not equal thirds or maximum fragmentation. Each pool needs a job and each additional method needs to remove a named failure.",
         "Give each pool a job and use each additional method to remove a named failure."),
        ("A life-changing amount deserves a harder One-Failure Test. That does not automatically mean multisig. It means the household should be able to explain why no single failure can destroy too much of the plan.",
         "A life-changing amount deserves a harder One-Failure Test. The household should be able to explain why no single failure can destroy too much of the plan before choosing direct custody, multisig, institutional custody, or a split."),
    ],
    "scripts/advanced/A7-2_what-self-custody-asks-of-you.md": [
        ("It does not remove trust or responsibility. It moves more of both onto you.",
         "Self-custody moves more trust and responsibility onto you."),
        ("That does not mean everybody should leave Bitcoin with an institution. It means moving into self-custody should follow skill and a real need for direct control rather than identity or pressure from somebody online.",
         "Move into self-custody when the skill and need for direct control justify owning the operational risk. Identity and online pressure are poor reasons to take that responsibility."),
    ],
    "scripts/advanced/A7-3_run-the-one-failure-test-across-methods-and-providers.md": [
        ("The answer does not have to be that every pool is perfectly replaceable. The goal is to know which loss would be catastrophic and whether that exposure is intentional.",
         "Identify which loss would be catastrophic and decide whether that exposure is intentional."),
        ("The goal is not maximum fragmentation.",
         "Use the fewest independent systems that remove the catastrophic failures."),
    ],
    "scripts/advanced/A7-4_utxos-dust-consolidation-and-addresses.md": [
        ("A transaction can combine UTXOs from several tax lots, and moving Bitcoin does not automatically establish which tax lot was sold.",
         "A transaction can combine UTXOs from several tax lots. The tax records still need to identify which lot was disposed of."),
    ],
    "scripts/advanced/A8-1_do-you-need-a-trust.md": [
        ("A trustee holding one key in a two-of-three wallet does not automatically have control, but the other key holders, descriptor, provider, and legal authority determine what the arrangement actually does. A trustee holding a seed and passphrase may have full technical control even if the paperwork describes a different intention.",
         "One trustee key in a two-of-three wallet lacks unilateral technical control. The other key holders, descriptor, provider, and legal authority determine the full arrangement. A trustee holding both a seed and passphrase may have full technical control even when the paperwork describes a different intention."),
    ],
}


MODULE_CHECKPOINTS = dedent("""
    # Module checkpoints

    ## Module 0 — Start Here

    **You will build:** Know the course sequence, the US-versus-non-US boundary, the Ask tools, and the no-secrets rule.

    - [ ] You know the course is taught in order and implemented through the owning Build & improve area.
    - [ ] You know teach lessons make decisions and walkthroughs perform the clicks.
    - [ ] You have used one helpful Ask prompt and know the Daily Bitcoin Market Report and AI export.
    - [ ] You can state what stays out of every AI tool.

    ## Module 1 — Foundation

    **You will build:** An honest current position, reviewed assumptions, and a first preliminary Plan result.

    - [ ] Household details are accurate.
    - [ ] Every real account and custody location is listed.
    - [ ] Current holdings match the source statements.
    - [ ] Balance, activity, and tax-detail coverage are understood separately.
    - [ ] The growth and inflation assumptions were reviewed deliberately.
    - [ ] The simulation result is visible with a truthful freshness state.
    - [ ] Planned and earliest modeled retirement dates are understood separately.
    - [ ] Build & improve shows Foundation complete.

    ## Module 2 — Cash Flow + Reserve

    **You will build:** A believable monthly surplus, a funded-or-funding Reserve, and expected life events in the baseline.

    - [ ] Normal spending and bare-bones spending are separate.
    - [ ] The surplus is believable and sustainable.
    - [ ] Orange Plan calculated the Reserve target from the selected basis and months.
    - [ ] The monthly Reserve build amount is saved.
    - [ ] Expected life events are in the baseline and hypotheticals are in Plan → Scenarios.
    - [ ] College funding has a commitment and source plan when it applies.

    ## Module 3 — Allocation + Next-Dollar

    **You will build:** A target allocation, account timeframes, and a contribution plan for what changes now and after the Reserve is full.

    - [ ] The Bitcoin target survives the dollar drawdown test.
    - [ ] Major accounts have Reserve, Bridge, or Legacy jobs.
    - [ ] The target mix and drift band are saved.
    - [ ] The employer match and contribution destinations are modeled correctly.
    - [ ] Each contribution row says what the money buys.
    - [ ] External payroll, transfer, and purchase changes are listed.
    - [ ] The extra-debt claim is clearly provisional until Module 4.

    ## Module 4 — Debt Strategy

    **You will build:** Current debt terms, a job for every debt, and a final extra-payment amount reflected in Cash Flow Routing.

    - [ ] Every active debt has a current balance, rate, payment, and loan-specific terms.
    - [ ] You understand payment capacity and balance-sheet leverage as separate lenses.
    - [ ] Every debt has a job and a reason.
    - [ ] Any Bitcoin-backed loan has written operating triggers.
    - [ ] Extra debt is reflected in Cash Flow Routing.
    - [ ] The contribution plan was rechecked after the debt decision.

    ## Module 5 — Tax Strategy

    **You will build:** Usable lot history, a tax-window roadmap, and a professional handoff packet.

    - [ ] Missing basis is visible and never silently invented.
    - [ ] Transfers and duplicate imports are reconciled.
    - [ ] The taxable, tax-deferred, and Roth mix is understood.
    - [ ] A conversion or withdrawal range is modeled when relevant.
    - [ ] Harvesting candidates and the 8949 export are saved.
    - [ ] Current-year questions are ready before the calendar deadline.

    ## Module 6 — Retirement Income

    **You will build:** A retirement paycheck strategy with accessible Bridge funding, a saved withdrawal order, and understood spending guardrails.

    - [ ] Retirement spending, healthcare, and irregular costs are honest.
    - [ ] The income floor and portfolio-funded gap can be stated from memory.
    - [ ] Bridge years and accessible funding are verified.
    - [ ] Social Security timing was compared when material.
    - [ ] A withdrawal strategy was previewed and intentionally saved.
    - [ ] Sell, borrow, or hold remains Preview until intentionally saved.
    - [ ] The simulation result is read as a count with a truthful freshness state.
    - [ ] Lower, current, and upper portfolio guardrails are understood.

    ## Module 7 — Custody

    **You will build:** A custody direction, a no-secrets map of the meaningful Bitcoin pools, a proven recovery path, and one major failure point fixed.

    - [ ] Custody direction is one method or an intentional split, chosen on purpose.
    - [ ] Direct-control preference and the risk being reduced are stated.
    - [ ] Every meaningful Bitcoin pool has a no-secrets job, scale, method, remaining failure, and family path.
    - [ ] Hardware recovery is proven or clearly outstanding.
    - [ ] The One-Failure Test identified the largest current weakness.
    - [ ] Important accounts and email are hardened.
    - [ ] No seed, key, passphrase, PIN, password, descriptor contents, or exact recovery location is stored in the app, map, or course notes.
    - [ ] An encrypted backup of the plan data exists.

    ## Module 8 — Estate + Inheritance

    **You will build:** An executor path, legal-document plan, no-secrets heir letter and packet, communication backstop, and insurance gap audit.

    - [ ] Executor and backup are chosen and contacted.
    - [ ] Baseline legal documents and beneficiary forms have a clear status.
    - [ ] Legal authority and technical recovery are mapped together.
    - [ ] Heir letter and executor packet contain no secrets.
    - [ ] The communication backstop is armed and tested when applicable.
    - [ ] Insurance gaps are documented for licensed review.

    ## Module 9 — Finish, Test + Maintain

    **You will build:** A completed current baseline, one tested scenario, yearly copy of Your Plan, encrypted backup, and review calendar.

    - [ ] Every Build & improve area is intentionally complete.
    - [ ] The completed 1,000-simulation result is Current.
    - [ ] The result states how many simulations worked and the through-age.
    - [ ] Planned and earliest modeled retirement dates are understood separately.
    - [ ] The Orange Plan standard of 800 of 1,000 is understood.
    - [ ] Portfolio guardrail status and the annual spending-review rule are understood.
    - [ ] One scenario was tested and any winning decision moved through Current versus Preview.
    - [ ] Monthly and annual review dates are on the calendar.
    - [ ] Your Plan PDF and encrypted backup are saved.
    - [ ] Only one to three next actions remain.
    """)


CLAIM_REGISTRY = dedent("""
    # Claim registry — current filming policies

    This registry records the positions that must stay consistent across scripts, master files, student text, walkthroughs, visuals, and production documents.

    ## MUST remain true

    | Area | Current course policy |
    |---|---|
    | Course order | Module 2 is Cash Flow + Reserve. Module 3 is Allocation + Next-Dollar. Module 4 is Debt, followed by a return to Cash Flow Routing. |
    | Permanent app model | Home owns current truth. Plan owns building, testing, and improving. Cash Flow owns current income, spending, taxes, debt payments, and saving. Protect owns family execution and estate readiness. |
    | Plan model | Plan uses Overview, Build & improve, and Scenarios. Build & improve shows one next task by default and opens the full analytical workspaces. |
    | Lesson roles | Teach lessons explain the concept and decision. Walkthroughs own click paths, data entry, calculations, saves, and verification. |
    | Authorship | Only retained Austin dictation is labeled AUSTIN DICTATION. All other teach scripts are PRE-DICTATION FILMING DRAFT. |
    | Onboarding | The onboarding age is a deterministic starting estimate. The first Plan simulation result may be Preliminary and becomes more trustworthy as real data replaces estimates. |
    | Simulation result | Customer-facing results lead with successful simulations out of 1,000 and the through-age. The normal Orange Plan standard is 800 of 1,000. Normal users do not choose another standard. |
    | Retirement dates | Planned retirement date and earliest modeled retirement date remain distinct. The earliest modeled date is the first date that reaches the Orange Plan standard. |
    | Freshness | Every displayed result is truthfully Preliminary, Current, Stale, or Unavailable. |
    | Current versus Preview | Material plan choices show exact before-and-after results and remain Preview until intentionally saved to the plan. |
    | Guardrails | The core view shows lower portfolio guardrail, current retirement portfolio, upper guardrail, and whether an annual spending review is needed. Internal probability boundaries belong in Advanced methodology. |
    | Activity | Balance and holdings, recorded activity, and tax details are separate continuity dimensions. Provable activity is recorded with provenance; ambiguity becomes one focused Needs Attention question. |
    | Transfers | An internal transfer preserves total quantity, lot identity, acquisition date, and known or unknown basis. It never becomes a sale plus purchase. |
    | Execution | Orange Plan previews and saves planning choices. Trades, conversions, harvesting, loans, and provider actions execute outside the app and are recorded after completion. |
    | Reserve | Orange Plan calculates the Reserve target from the selected monthly spending basis and target months. |
    | Life events | Expected changes belong in Life events. Hypothetical questions belong in Plan → Scenarios. |
    | Future funding | Bitcoin can remain part of a funding plan more than five years out. The firmly committed amount becomes less dependent on Bitcoin as the date approaches. |
    | College | Start with the parent's commitment and funding sources. A 529 is one tool; the one-third framework is an option. |
    | Contributions | Reserve, match, provisional Extra Debt, Bridge versus Legacy, then the target inside the account. Module 4 finalizes the debt claim. |
    | Custody | Document the process, never the secrets. Custody methods are trade-offs, and the One-Failure Test includes one method and one provider. |
    | Professional scope | General research supports education. Taxpayer-, state-, contract-, provider-, and device-specific execution keeps a targeted external gate. |

    ## MUST NOT return

    - A normal-user confidence-target control or teaching that asks the student to choose the standard.
    - Percentage-first customer language when a count such as 790 of 1,000 is available.
    - A core guardrail graphic framed as a visible 60 / 80 / 95 confidence scale.
    - A claim that the first useful simulation result must wait until Module 9.
    - A stale result presented as current.
    - Strategy, Scenarios, Ask, Transactions, Debt, Tax, Report, Settings, or Tools as permanent navigation.
    - Apply-to-plan or execution language when the correct action is Preview change, Save to plan, or Record completed action.
    - Manual Reserve-target multiplication presented as a user input.
    - A 529 or full sticker price presented as the universal college target.
    - A rigid rule that Bitcoin must leave every future funding plan at year five.
    - Debt-before-Allocation presented as the course teaching order.
    - The Extra Debt rung described as final before Module 4.
    - A generated draft presented as Austin's original words.
    - The repeated `YOUR DECISION / PUT IT IN ORANGE PLAN / YOU ARE DONE WHEN` architecture forced onto every teach lesson.
    - One universal Bitcoin allocation, loan amount, LTV, UTXO threshold, insurance amount, trust clause, or inheritance key split.
    - A custody wealth ladder or a claim that multisig removes every single point of failure.
    - Any seed phrase, key, passphrase, PIN, password, or exact recovery location in an app, worksheet, screenshot, course note, or AI tool.

    ## Direct-voice rule

    State the useful affirmative fact first. Keep a negative statement only when the exclusion itself prevents a materially unsafe or incorrect decision. The course does not use copywriting reversals such as “not A, but B” merely to make a sentence land.

    ## Verification

    `V1-COURSE-ALIGNMENT.md`, `DIRECT-VOICE-AUDIT.md`, `FINALIZATION-STATUS.md`, and the branch verification workflow record the active checks.
    """)


FINALIZATION_STATUS = dedent("""
    # Finalization status

    ## Editorial status

    - The full core course remains in the approved order: Foundation → Cash Flow + Reserve → Allocation + Next-Dollar → Debt → Tax → Retirement Income → Custody → Estate + Inheritance → Finish, Test + Maintain.
    - All 28 core teach lessons have Austin dictation or a pre-dictation filming draft.
    - All 10 core walkthroughs / demos have an implementation sheet.
    - All 14 Advanced lessons remain attached to the correct core module.
    - The course now matches the Orange Plan V1 product contracts for Home / Plan / Cash Flow / Protect, Build & improve, Scenarios, Ask, Current versus Preview, Your Plan, account activity, the fixed 800-of-1,000 standard, result freshness, and portfolio guardrails.
    - The direct-voice audit now catches same-sentence and cross-sentence “not A, but B” copywriting structures. Reviewed ordinary candidates were rewritten around the affirmative fact; necessary safety, legal, tax, and custody boundaries remain.
    - Module 7 continues to use the custody trade-off and One-Failure framework.
    - Slide concepts remain edit graphics and B-roll cues; Austin can record the camera-facing scripts without presenting a slide deck.

    ## App reference

    The conceptual course contract is aligned to Orange Plan PR #227 and the committed V1 product decisions. PR #227 is still a Preview-only rebuild, so exact on-screen labels and click paths remain a recording-time gate. Walkthroughs must be checked against the same approved Preview commit used on camera.

    ## What remains before recording and publication

    - Austin reads / dictates the prepared scripts in chronological order.
    - App walkthroughs wait for the owning V1 slices and final labels to stabilize.
    - Targeted professional signoffs remain for tax, custody, insurance, and estate material.
    - The hardware-wallet demo requires exact device and firmware verification.
    - Current-year figures, laws, limits, premiums, provider terms, and tax examples are checked at recording or publication time.

    ## Recording decision

    Camera-facing concept lessons can be dictated and filmed after this branch is approved. Graphics can be added in editing. App walkthroughs, screenshots, and exact navigation are recorded after the relevant V1 Preview surfaces pass their product and verification gates.

    ## Verification record

    - Direct-voice audit generated across core and Advanced scripts.
    - V1 terminology and product-contract check added.
    - Scripts, masters, modules, lesson text, visual briefs, checkpoints, film order, shoot list, Circle structure, and production checklist are regenerated from the aligned sources.
    - Cross-reference, visual, layer-parity, formatting, and course-metric checks run in the branch workflow.
    """)


V1_ALIGNMENT_REPORT = dedent("""
    # Orange Plan V1 course alignment

    ## Product authority

    The course now uses the accepted V1 customer model:

    - Home = current financial truth.
    - Plan = build, understand, test, and improve the plan.
    - Cash Flow = income, spending, taxes, debt payments, Reserve, and saving.
    - Protect = beneficiaries, custody and access, heir instructions, trusted people, legal readiness, and the plan packet.
    - Plan contains Overview, Build & improve, and Scenarios.
    - Ask is a global contextual utility.
    - Your Plan is a read-only document generated from the saved plan.

    ## Central planning result

    - Customer language leads with simulations worked out of 1,000 and the through-age.
    - The Orange Plan standard is 800 successful simulations out of 1,000 for normal users.
    - A custom standard is Advanced only.
    - Planned retirement date and earliest modeled retirement date remain separate.
    - Every result is Preliminary, Current, Stale, or Unavailable.
    - Current versus Preview shows exact before-and-after outcomes for material changes.

    ## Guardrails

    The core course teaches lower portfolio guardrail, current retirement portfolio, upper portfolio guardrail, and whether a separate annual spending review is needed. The visible core lesson no longer asks the user to manage a 60 / 80 / 95 confidence scale. Internal probability boundaries and inverse-threshold methodology remain Advanced and must match the validated production engine.

    ## Account and activity continuity

    - Exact provable purchases, sales, and eligible internal transfers can be recorded with provenance and an immutable receipt.
    - Ambiguous activity becomes one focused Needs Attention question.
    - Balance and holdings, recorded activity, and tax details are separate states.
    - Internal transfers preserve quantity and lot history and never become a sale plus purchase.

    ## Course production boundary

    Concept lessons are durable and can be recorded after Austin's dictation pass. Walkthroughs remain gated on the relevant V1 Preview slice because exact routes, labels, and screen hierarchy are still under implementation.

    ## Direct-voice editorial rule

    The useful fact leads. Contrastive negatives remain only when the exclusion itself carries safety, legal, tax, custody, or model-interpretation value.
    """)


VISUALS: dict[str, str] = {
    "visuals/1-3a_thousand-paths.md": dedent("""
        # 1.3 · What the simulation count actually measures

        **Paste `00-STYLE.md` first, then this.**

        ## What it has to make obvious
        The result is a count of modeled paths and includes the planning age and freshness state.

        ## The visual
        1,000 thin translucent paths fan right from one starting point. A counter reads **790 of 1,000 simulations worked**. Beneath it: **Money lasted through age 95**. A small state label cycles through Preliminary → Current → Stale → Unavailable, ending on Current.

        ## Labels and data
        Use 790 / 1,000 as an illustration. Show the Orange Plan standard separately as **800 of 1,000**. Keep planned retirement date and earliest modeled date as two different labels.

        ## Motion
        Paths draw left to right, the count builds to 790, the through-age appears, then the freshness state settles on Current.
        """),
    "visuals/1-3b_number-flow.md": dedent("""
        # 1.3 · How the numbers flow

        **Paste `00-STYLE.md` first, then this.**

        > **This is the course's reusable reference frame.** Recall the same frame in later modules instead of redesigning it.

        ## What it has to make obvious
        Every result comes from an owning fact or choice, and a changed fact makes the saved result stale until recalculated.

        ## The visual
        A four-band horizontal flow:

            WHAT YOU CHANGE → WHAT ORANGE PLAN CALCULATES → WHAT MOVES → RESULT STATE

        Three example rows sit below it.

        ## Labels and data

        Row 1 — cash flow:

            Income − taxes − living − debt payments
            → amount available to save
            → Reserve and contribution routing
            → simulation result becomes stale when the modeled amount changes

        Row 2 — life event:

            Expected life event
            → future cash flow in that year
            → account withdrawals and retirement dates
            → recalculated result becomes Current

        Row 3 — strategy:

            Current choice → Preview choice
            → before-and-after simulation count, dates, taxes, or spending
            → Save to plan
            → Current updates

        ## Motion
        Build left to right. End by highlighting the state transition **Current → Stale → Recalculate → Current**.
        """),
    "visuals/6-3_guardrails.md": dedent("""
        # 6.3 · The simulation result and portfolio guardrails

        **Paste `00-STYLE.md` first, then this.**

        ## What it has to make obvious
        The central result is a count, and the annual spending decision comes from portfolio guardrail levels.

        ## The visual
        Top: **790 of 1,000 simulations worked** with **Money lasted through age 95** and a Current state label.

        Bottom: one horizontal guardrail line:

            Lower guardrail        Current portfolio        Upper guardrail
            $1.45M ---------------------●---------------------- $2.40M
                                      $1.82M

        Beneath the line: **Within your guardrails · No spending review needed**.

        Include two alternate state cards for editing use: **Below your lower guardrail · Review spending** and **Above your upper guardrail · Review spending**.

        ## Labels and data
        The dollar values are illustrative. Show a separate note: **Annual spending change capped at 10%**. Do not display 60 / 80 / 95 as the core customer visual.

        ## Motion
        Build the simulation count first. Then draw the lower/current/upper line. Move the current marker below and above the band briefly to reveal the separate review states.
        """),
    "visuals/9-1b_annual-lap.md": dedent("""
        # 9.1 · The four-destination annual lap

        **Paste `00-STYLE.md` first, then this.**

        ## What it has to make obvious
        The annual review follows the same four destinations the customer uses all year.

        ## The visual
        Four stations arranged as a circuit:

        - Home — Is the current financial picture true?
        - Cash Flow — Is the monthly system working?
        - Plan — Does the future still work?
        - Protect — Could the family carry it out?

        A finish card reads: **Recalculate · Save Your Plan · 1–3 actions**.

        ## Motion
        A marker moves Home → Cash Flow → Plan → Protect and finishes on the yearly artifacts and action card.
        """),
    "visuals/9-2b_reading-order.md": dedent("""
        # 9.2 · How a planner reads Your Plan

        **Paste `00-STYLE.md` first, then this.**

        ## What it has to make obvious
        Your Plan is read through four questions, with result freshness checked before conclusions are trusted.

        ## The visual
        Four numbered stages in a straight sequence: Position → Trajectory → Risk → Actions. A small Current / Preliminary / Stale / Unavailable stamp sits above Trajectory.

        Beside it, show a read-only Your Plan document with arrows from its sections into the four stages.

        ## Labels and data
        Position: current accounts and debts. Trajectory: simulation count, through-age, planned date, earliest modeled date, spending and funding. Risk: scenarios, taxes, debt, custody, protection. Actions: one to three steps.

        ## Motion
        The freshness stamp appears first, then the four-stage reading path draws across the document.
        """),
    "visuals/0-2_ask.md": dedent("""
        # 0.2 · Ask as a contextual guide

        **Paste `00-STYLE.md` first, then this.**

        ## What it has to make obvious
        Ask explains the current screen, finds missing work, compares trade-offs, and routes the user to the owning workspace.

        ## The visual
        Show the four destinations in a quiet row: Home · Plan · Cash Flow · Protect. A restrained **Ask** drawer opens over Plan. Three sample prompts appear:

        - Why did this result change?
        - What information is missing or stale?
        - Compare Current and Preview.

        The final arrow goes from Ask to the relevant workspace and then to Current versus Preview.

        ## Safety footer
        Process and plan data only. Never seeds, keys, passphrases, PINs, passwords, or wallet backups.
        """),
    "visuals/9-2c_current-vs-preview.md": dedent("""
        # 9.2 · Current versus Preview

        **Paste `00-STYLE.md` first, then this.**

        ## What it has to make obvious
        A proposed choice stays separate from the saved plan until the user intentionally saves it.

        ## The visual
        Two aligned columns:

            CURRENT                  PREVIEW
            790 of 1,000             824 of 1,000
            Planned: May 2032        Planned: May 2032
            Earliest: May 2030       Earliest: January 2030
            Spending: $120,000       Spending: $115,000

        Highlight only the values that changed. One quiet button below reads **Save to plan**.

        ## Motion
        Current appears first. Preview slides in, changed values highlight, then the Save-to-plan action appears without auto-firing.
        """),
}


GLOBAL_SCRIPT_REPLACEMENTS = [
    ("Build Your Plan", "Build & improve"),
    ("Strategy → Allocation", "Plan → Build & improve → Allocation"),
    ("Strategy → Debt", "Plan → Build & improve → Debt and leverage"),
    ("Strategy → Tax", "Plan → Build & improve → Tax strategy"),
    ("Scenarios →", "Plan → Scenarios →"),
    ("confidence ring", "simulation result"),
    ("confidence number", "simulation count"),
    ("confidence result", "simulation result"),
    ("confidence check", "simulation test"),
    ("confidence receipt", "simulation receipt"),
    ("Apply to plan", "Save to plan"),
    ("apply to plan", "save to plan"),
]


def active_script_paths() -> list[Path]:
    paths = sorted((ROOT / "scripts").glob("*.md"))
    paths += sorted((ROOT / "scripts" / "advanced").glob("*.md"))
    return [p for p in paths if p.name not in {"README.md", "VOICE-GUIDE.md"}]


def master_body(body: str) -> str:
    out: list[str] = []
    for line in body.splitlines():
        match = re.match(r"^== (.+) ==$", line.strip())
        if match:
            words = match.group(1).lower()
            out += ["", "### " + words[:1].upper() + words[1:], ""]
        elif line.startswith("🎬 VISUAL"):
            out.append("> 🎬 **" + line[len("🎬 "):].strip() + "**")
        else:
            out.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()


def sync_full_script_to_master(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    title_line = next(line for line in lines[:8] if re.match(r"^A?\d+\.\d+\s+\S", line))
    num, title = title_line.split(" ", 1)
    divider = next(i for i, line in enumerate(lines) if set(line.strip()) == {"="})
    body = "\n".join(lines[divider + 1:]).strip()
    master_path = ROOT / ("MASTER-ADVANCED.md" if num.startswith("A") else "MASTER-COURSE.md")
    master = master_path.read_text(encoding="utf-8")
    start_match = re.search(rf"^## {re.escape(num)} .+$", master, re.M)
    if not start_match:
        raise RuntimeError(f"{num} missing from {master_path.name}")
    next_match = re.search(r"\n#{1,2} (?:A?\d+\.\d+|Unit |Advanced Module )", master[start_match.end():])
    end = start_match.end() + next_match.start() + 1 if next_match else len(master)
    section = master[start_match.start():end]
    if "\n---\n" not in section:
        raise RuntimeError(f"{num} has no master header/body divider")
    header, _ = section.split("\n---\n", 1)
    header_lines = header.splitlines()
    header_lines[0] = f"## {num} {title}"
    words = len(body.split())
    header = "\n".join(header_lines)
    header = re.sub(r"· [\d,~]+ words · ~[\d.]+ min", f"· ~{words:,} words · ~{words / 155:.0f} min", header)
    replacement = header + "\n---\n\n" + master_body(body) + "\n\n"
    master = master[:start_match.start()] + replacement + master[end:]
    master_path.write_text(master, encoding="utf-8")


def apply_exact_replacements() -> list[str]:
    modified_nums: set[str] = set()
    errors: list[str] = []
    for rel, pairs in REPLACEMENTS.items():
        if not pairs:
            continue
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing replacement file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        changed = False
        for old, new in pairs:
            if old not in text:
                errors.append(f"old text not found in {rel}: {old[:90]}")
                continue
            text = text.replace(old, new)
            changed = True
        if changed:
            path.write_text(text, encoding="utf-8")
            match = re.search(r"(?:segment |# )(A?\d+\.\d+)", text[:300])
            if match:
                modified_nums.add(match.group(1))

    if errors:
        raise RuntimeError("\n".join(errors))
    return sorted(modified_nums)


def apply_global_terms() -> None:
    for path in active_script_paths():
        text = path.read_text(encoding="utf-8")
        for old, new in GLOBAL_SCRIPT_REPLACEMENTS:
            text = text.replace(old, new)
        if "WALKTHROUGH" in path.name and "V1 capture gate:" not in text:
            lines = text.splitlines()
            insert_at = 1
            while insert_at < len(lines) and not lines[insert_at].startswith("**Screen capture"):
                insert_at += 1
            insert_at = min(insert_at + 1, len(lines))
            lines[insert_at:insert_at] = [
                "",
                "> **V1 capture gate:** Verify the final label and click path against the same approved Preview commit used for recording.",
            ]
            text = "\n".join(lines).rstrip() + "\n"
        path.write_text(text, encoding="utf-8")


def update_voice_guide() -> None:
    path = ROOT / "scripts" / "VOICE-GUIDE.md"
    text = path.read_text(encoding="utf-8")
    marker = "## Direct affirmative rule — V1 filming pass"
    block = dedent("""
        ## Direct affirmative rule — V1 filming pass

        Austin's preferred edit is to say the useful fact immediately. Delete the
        setup sentence when a paragraph uses this shape:

        - “This is not A. It is B.”
        - “The goal is not A. The goal is B.”
        - “Not because A, but because B.”
        - “A does not automatically mean B. C is the real answer.”

        Direct version:

        - “The four paths describe where you are today.”
        - “Bare-bones spending is the minimum the household can run on.”
        - “Give the major accounts a job and match the holdings to that job.”

        Keep a negative statement when the exclusion itself prevents a materially
        unsafe or incorrect decision: no secrets in an AI tool, CrowdHealth is not
        insurance, a simulation count is not a personal probability of ruin, and
        Orange Plan does not execute a trade or loan. State the boundary once, then
        move directly to the useful action.
        """)
    if marker not in text:
        path.write_text(text.rstrip() + "\n\n" + block, encoding="utf-8")


def main() -> None:
    modified = apply_exact_replacements()
    apply_global_terms()

    for rel, content in FULL_SCRIPTS.items():
        (ROOT / rel).write_text(content, encoding="utf-8")
    for rel, content in FULL_WALKTHROUGHS.items():
        (ROOT / rel).write_text(content, encoding="utf-8")

    # Full rewrites replace their master bodies. Exact direct-voice replacements
    # are then applied to the master prose too, preserving master-only tables and
    # editorial headers in the other lessons.
    for rel in FULL_SCRIPTS:
        sync_full_script_to_master(ROOT / rel)
    for rel in FULL_WALKTHROUGHS:
        # Walkthroughs are represented in the master, but their richer capture
        # sheets remain canonical. Keep the master title aligned when present and
        # let the generated module point to the script sheet.
        pass

    for master_name in ("MASTER-COURSE.md", "MASTER-ADVANCED.md"):
        path = ROOT / master_name
        text = path.read_text(encoding="utf-8")
        for pairs in REPLACEMENTS.values():
            for old, new in pairs:
                text = text.replace(old, new)
        for old, new in GLOBAL_SCRIPT_REPLACEMENTS:
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")

    (ROOT / "MODULE-CHECKPOINTS.md").write_text(MODULE_CHECKPOINTS, encoding="utf-8")
    (ROOT / "CLAIM-REGISTRY.md").write_text(CLAIM_REGISTRY, encoding="utf-8")
    (ROOT / "FINALIZATION-STATUS.md").write_text(FINALIZATION_STATUS, encoding="utf-8")
    (ROOT / "V1-COURSE-ALIGNMENT.md").write_text(V1_ALIGNMENT_REPORT, encoding="utf-8")
    for rel, content in VISUALS.items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    update_voice_guide()
    print("V1 alignment and direct-voice source pass applied")
    print("minor lesson replacements:", ", ".join(modified))


if __name__ == "__main__":
    main()
