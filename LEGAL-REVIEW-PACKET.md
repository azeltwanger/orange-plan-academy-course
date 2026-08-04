# Legal review packet — Orange Plan Academy course

**Status: DRAFT FOR ATTORNEY REVIEW. Not legal advice. Nothing here should be published until a licensed attorney in Austin's state has reviewed it.**

Prepared 2026-08-04 by Claude Code as a language and coverage audit, plus draft copy for counsel to work from. Two separate questions are in scope:

1. Does the course content stay on the education side of the line? (Audit below.)
2. Do the course's own legal documents exist and cover it? (They do not yet. Drafts below.)

---

## Part 1 — Coverage gap (the finding that matters most)

**The existing `Terms of Service` and `Disclaimer` pages cover the software only. Neither mentions a course, training, or curriculum anywhere.** A paid course is a different product with different exposure: purchase terms, refunds, license to the material, testimonials/results claims, and the education-not-advice line all need to be addressed for the course specifically.

| Document | Exists | Covers the app | Covers the course |
|---|---|---|---|
| Terms of Service (`src/pages/TermsOfService.jsx`) | Yes | Yes | **No** |
| Disclaimer (`src/pages/Disclaimer.jsx`) | Yes | Yes | **No** |
| Privacy Policy (`src/pages/PrivacyPolicy.jsx`) | Yes | Yes | Partially (data handling likely carries over) |
| Course terms / refund policy | **No** | — | **No** |
| Course disclaimer | **No** | — | **No** |

The app disclaimer is well-structured and its section list is a good model to extend: Financial Projections and Calculations · Bitcoin and Cryptocurrency Risks · Not Professional Advice · Orange Plan AI · Linked Accounts · Tax Calculations · Estate, Custody, and Security Information · No Warranties and Limitation of Liability · Your Responsibility.

---

## Part 2 — Content audit results

A pattern scan was run across all 53 scripts and all 53 lesson-text files for advisory language.

**Result: the content is in good shape.** The house rule ("educational, not advisory: use projection/scenario/explore, never recommend/should/optimal") is being followed closely.

| Pattern | Hits | Assessment |
|---|---|---|
| "I recommend" / "recommendation" | 2 | Both are **disclaimers** ("none of this is a product recommendation"). Good. |
| "you should" | 4 | All hedged and situational ("the months you should hold depends on your specific situation"). Low risk. |
| "optimal" / "the best option" | 2 | Both hedged with "I think" and about personal comfort, not products. Low risk. |
| "you must" / "you need to" | 12 | Nearly all factual, not directive ("documents you need to gather", "a loan you have to pay back"). Low risk. |
| "guarantee" | 24 | **None are performance promises.** Uses are: arithmetic facts ("paying a 20% card is a guaranteed 20% return"), describing Social Security as guaranteed income, scam warnings ("guaranteed returns are a scam"), and disclaimers ("not a guarantee"). Worth confirming counsel is comfortable with the debt-paydown phrasing. |

**Structural strengths already present:** no law-set figures (brackets, limits, exemptions, RMD ages) are spoken as fact on camera; the course routes to a CPA, licensed insurance professional, and estate attorney in the relevant modules; the trust lesson opens by telling most students they don't need one; the insurance lesson explicitly says "none of this is a product recommendation"; international content was removed rather than guessed at.

**Gaps found and fixed in this pass:**

- **The 1.1 script had no spoken disclaimer at all.** The lesson *text* carried one, but the video (which is what most students actually consume) never said it. A spoken "what this is and isn't" section was added.
- Four high-risk lessons had no verification line: **5.2** (LTV cushion), **5.3** (the four debt plays), **7.6** (guardrails), **9.2** (access split). Each now names the limit of what's being taught and points to the right professional.

**Still to consider with counsel:** whether the Bitcoin-backed borrowing material (5.2, 5.3, 7.5) needs a stronger standing warning than the lesson-level lines now carry, given it is the highest-stakes content in the course.

---

## Part 3 — Draft copy for counsel

### 3a. Course Disclaimer (draft)

> **Educational content only.** Orange Plan Academy is an educational course. It does not provide financial, investment, tax, legal, insurance, or accounting advice. Purchasing or completing this course does not create an advisory, fiduciary, or client relationship of any kind between you and Orange Plan, Austin Zeltwanger, or any affiliate.
>
> **General, not personalized.** All content is general in nature and identical for every student. It is not tailored to your financial situation, needs, or objectives, and it does not take into account your particular circumstances. No part of this course should be interpreted as a recommendation to buy, sell, or hold any security, asset, or product, including Bitcoin.
>
> **Projections are hypothetical.** The course uses Orange Plan, a modeling tool that produces hypothetical projections based on the figures and assumptions you enter. Projections are assumption-dependent, are not predictions, and are not guarantees of any outcome. Actual results will differ.
>
> **Bitcoin risk.** Bitcoin is highly volatile and has historically experienced drawdowns exceeding 70%. You can lose money, including all of it. Past performance does not indicate future results. Any price, return, or growth figure used in this course is illustrative only.
>
> **Borrowing risk.** Content addressing Bitcoin-backed lending is educational. Borrowing against volatile collateral can result in margin calls and forced liquidation of your collateral, potentially at unfavorable prices. Lending terms, collateral handling, and liquidation rules vary materially by lender. Review any agreement in full and consult your own advisors before borrowing.
>
> **Tax, legal, and insurance content.** Tax, estate, and insurance material is general educational information based on rules in effect when the course was recorded. Rules change, and their application depends on your specific facts and jurisdiction. Consult a qualified CPA, licensed insurance professional, and estate attorney licensed in your jurisdiction before acting.
>
> **US focus.** The course is written around United States rules and account types. Concepts may translate to other jurisdictions, but specific rules do not. Non-US students should work with a qualified local professional.
>
> **No results promised.** Individual results vary. Nothing in this course guarantees any financial outcome, retirement date, rate of return, or level of savings.
>
> **Your responsibility.** You are solely responsible for your own financial decisions and for verifying any information before acting on it.

### 3b. Course Terms — points for counsel to draft

Items a course (as distinct from the software) typically needs, flagged for counsel rather than drafted here:

1. **What is being sold** — access to course materials; whether app access is bundled, and what happens to course access if an app subscription lapses.
2. **License and restrictions** — personal, non-transferable license; no redistribution, resale, or sharing of logins; treatment of downloadable toolkit PDFs.
3. **Refund policy** — the actual terms, stated plainly. (Also an FTC-facing issue: whatever is advertised must match what is honored.)
4. **Renewal and cancellation** — if the course is sold as an annual subscription, auto-renewal disclosure and cancellation mechanics carry specific federal and state requirements.
5. **Group / live-call component** — if live Q&A is added at the $2K price point, this is the highest-risk element in the whole product. Answering "should *I* do a Roth conversion this year?" live is materially different from a recorded lesson. Counsel should advise on the format, the standing script for redirecting personal questions, and whether recordings change the analysis.
6. **Testimonials and results claims** — see FTC note below.
7. **Limitation of liability, disclaimer of warranties, indemnification, governing law, dispute resolution.**
8. **Content changes** — the right to update lessons as rules change, and what students are entitled to.

### 3c. Marketing-side note (FTC)

This sits outside the course content but is the same body of risk:

- Testimonials must be **real** and must reflect **typical** results, or carry a clear disclosure that results are not typical. The FTC's Consumer Reviews and Testimonials Rule (effective late 2024) and the 2023 Endorsement Guides update both bear on this.
- **Material connections** (payment, free access, affiliate relationships) must be disclosed clearly and conspicuously, near the claim.
- Avoid income, retirement-date, or return claims in course marketing. "Retire at 55" as a *lesson title* is fine; "retire at 55" as a *promise in an ad* is a different thing.

---

## Part 4 — Why the education framing matters (background for the conversation)

The relevant federal line is the Investment Advisers Act. Section 202(a)(11)(D) excludes "the publisher of any bona fide newspaper, news magazine or business or financial publication of general and regular circulation" from the definition of investment adviser. Commentary on that exclusion generally describes three conditions: the content is **impersonal**, it is **bona fide** (genuine and disinterested commentary rather than a vehicle for touting), and it is of **general and regular circulation** rather than issued in response to episodic market events.

The boundary that matters for this product is personalization. General education — how compounding works, how bracket-fill works, comparing categories of approach — is ordinarily not regulated advice. The exclusion stops applying when content becomes personalized to a specific person's situation.

**Practical implication for the course:** the recorded lessons are general and identical for every student, which is the right side of that line and matches how the course is written. The risk concentrates in anything that becomes one-to-one: live group calls, DMs, community replies, and any "here's what *you* should do" moment. That is a question for counsel before the group component launches, not after.

State-level rules can differ from the federal analysis, so this needs review by an attorney licensed where Austin is.

**Sources consulted for this background:**

- [Navigating the Publisher's Exclusion Under the Advisers Act — National Law Review](https://natlawreview.com/article/navigating-publishers-exclusion-under-advisers-act)
- [Navigating the Publisher's Exclusion Under the Advisers Act — Winstead](https://www.winsteadinvestmentmanagement.com/2025/12/navigating-the-publishers-exclusion-under-the-advisers-act/)
- [Spotlight on the Publisher Exclusion — Interactive Brokers](https://www.interactivebrokers.com/webinars/spotlight-publisher-exclusion.pdf)
- [SEC Regulation of "Information Providers" — Wilson Sonsini](https://www.wsgr.com/en/insights/informationor-advice-sec-regulation-of-information-providers-may-expand-to-include-providers-of-innovative-investment-analytics.html)
- [Endorsements, Influencers, and Reviews — FTC](https://www.ftc.gov/business-guidance/advertising-marketing/endorsements-influencers-reviews)
- [16 CFR Part 255 — Guides Concerning Use of Endorsements and Testimonials](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255)

---

## Part 5 — Questions to put to the attorney

1. Does the course, as written and disclaimed, sit within the publisher's exclusion?
2. Does a live group-call component change that answer, and what format keeps it safe?
3. Is a separate course Terms of Service needed, or can the app Terms be extended?
4. Is the annual-subscription structure subject to auto-renewal disclosure rules in our state?
5. Is the Bitcoin-backed borrowing content adequately disclaimed, or does it need a standing warning?
6. Does Austin's professional background or any current or former licensure create additional obligations here?
7. What review, if any, does course marketing copy need before launch?
