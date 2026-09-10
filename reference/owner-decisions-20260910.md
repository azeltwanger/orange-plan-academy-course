# Owner decisions and bounded-review reconciliation — September 10, 2026

## Source and scope

These are first-party excerpts from Austin's messages in this course conversation, copied on September 10, 2026. They are written/chat dictation, not newly verified on-camera lines. Spelling is preserved inside quotations. The interpretation below is editorial and is kept separate from the quoted words. No private account information or client material is included.

The current course remains 25 main and 8 situation-specific scripts. This record does not change app code, insurer contracts, loan agreements, licensed-review status or recording/capture approval.

## Borrowing

Austin's initial statement:

> starting LTV is 50% but this is higher risk, and we need to teach that people need to be aware of what their liquidation level is, and make sure they have BTC avaialble to top up loans if BTC drops 80% like it has in the past.

Austin's custody reasoning:

> My reasoning for the 50% starting LTV, or the maximum that an exchange allows you to take to start with, is that if Bitcoin price goes up from there, you're putting the least amount possible on the exchange. If you have the ability to just closely watch the loan, you're committing less collateral to the loan.

Austin's sizing requirement:

> It's extremely important to have that collateral available and to make sure that you're checking how much you actually need before you take out a loan. How much you're comfortable with taking depends on risk tolerance.

Austin's correction of the proposed stressed target:

> not 50% even at that lower price, but to avoid getting liquidated at 80% or whatever liquidation is.

Current course interpretation: choose the debt first using all Bitcoin genuinely dedicated to it, a severe drawdown, the projected full debt balance and actual contract requirements. Then consider opening that pre-sized loan at 50% posted-collateral LTV to leave more BTC under personal control. The stress calculation aims below the actual liquidation threshold with chosen room and any stricter cure/maturity requirement; it does not impose 50% LTV at the stressed price. This is a conditional, actively managed choice, not permission to borrow the maximum or a guarantee against liquidation. Cold-storage reserves are capacity to top up; they count toward lender LTV only when credited. Availability, response timing, counterparty exposure, funded payments and repayment remain separate conditions.

The current example uses $100,000/BTC, 3.5 supporting BTC, $50,000 debt and an assumed 80% liquidation threshold. Its $50,000 opening amount assumes separately funded interest and fees. An 80% decline leaves $70,000 collateral, with $56,000 of debt at the exact boundary. The $6,000 margin is fully used by one hypothetical year of 12% interest capitalized at year-end. Resize principal or dedicated BTC before borrowing when costs will accrue. Posting all 3.5 BTC initially gives about 14.3% LTV; posting 1 BTC gives 50%. These are calculations, not a lender offer or a claim that this reserve satisfies a stricter 65% cure.

## Insurance

Austin's stated preference:

> I don't have a deeply nuanced view on insurance. I think it depends on risk tolerance, but once something can be safely self funded to the point where it will not affect the persons quality of life, then it starts to make more sense. for example someone doesn't need disability insruance if they can live off of assets comfortably. If their family can thrive with assets, they wont need as much life insruance. but hten with more assets, liability and umbrella coverage make more sense because you have more to lose.

Austin separately asked for research to support the application:

> might need your help finding mathematical thresholds or researching best practices here. Higher confident returns on bitcoin like most holders have can change some of tehse tradtinaol dynamics as well.

Current course interpretation: transfer losses that could materially change the family's quality of life; consider self-funding once accessible, spendable resources and continuing income can cover the changed needs. Income-replacement protection may shrink as financial independence grows. Liability/umbrella exposure is a different review. Do not convert this preference into a fixed net-worth cutoff, a promise based on assumed Bitcoin growth, or an instruction to cancel a policy. The existing insurance lesson includes care costs, ongoing obligations, simultaneous market/income stress, replacement eligibility and actual policy terms. The needs calculation is editorial; [the dated research record](script-finishing-sources.md#insurance-needs-and-resources-not-one-threshold) identifies its external support. Austin's preference is established by his words above, not invented by either model.

## Reviewer routing

Austin's explicit clarification:

> where does alfred come from? we are using claude to cross check.

For this course, Claude is the cross-checker. This instruction comes from Austin. It is not a checker unilaterally waiving an owner's review process. Model review is not licensed tax, legal, insurance or investment advice. Keep the categorical will-drafting instruction out. Do not label any lesson professionally cleared based on an AI check.

## Older quote and upstream-source status

The supplied `Pasted markdown(9).md`, section 10.4, reproduces this earlier on-camera line:

> My default conservative level here is using a loan to value of around 10 to 20% of the value of the Bitcoin that I'm putting up.

Retain that line and its original provenance as a historical quote. It is superseded as the current course's posted-LTV default by Austin's later dictation above. Do not change what was said, call it a newly recorded quote, or silently reinterpret its denominator as all available BTC. Also do not replace an unrelated limit on the percentage of total holdings placed with a lender: that measures custody exposure, not posted LTV.

The audit says the old line and Alfred routing also appear in a voice-and-philosophy file, a research file and Claude project instructions. Searches of this Project's available files and connected GitHub sources did not identify those exact three original documents or an editable Claude settings surface. This pass therefore updates the course authority and research notes, preserves historical source bytes, and supplies the addendum below. It does **not** claim those external originals or project settings were edited. App-repository historical coding logs that mention Alfred are unrelated and are unchanged.

## Addendum for the three upstream Claude sources

Apply this beside any older posted-LTV default and in the current project instructions; preserve quoted historical text and its provenance:

> **Current course authority — September 10, 2026.** Austin's latest course dictation supersedes the earlier 10–20% posted-LTV teaching default. Size debt first against all dedicated supporting BTC under a severe decline, projected debt growth and the actual liquidation/cure/maturity requirements, leaving chosen room. Then consider 50% initial posted-collateral LTV to keep more BTC under personal control, only with a workable top-up, payment and repayment plan. There is no 50% stressed-LTV target. The $50,000 / 3.5 BTC example assumes separately funded interest/fees; capitalized costs require resizing before borrowing. Historical on-camera quotes remain historical, not current default recommendations.
>
> Austin also supplied the insurance position: consider self-funding once the event can be absorbed without an unacceptable quality-of-life change; assets can reduce income-replacement needs while increasing the importance of liability review. This is not an automatic policy-cancellation rule. Claude is the course cross-checker, per Austin's explicit clarification; no Alfred approval role should be invented, and AI checking is not licensed sign-off. The categorical will wording remains excluded.

The upstream work is complete only when the actual three documents/settings are updated and verified. This addendum and a GitHub merge alone do not close that separate step.
