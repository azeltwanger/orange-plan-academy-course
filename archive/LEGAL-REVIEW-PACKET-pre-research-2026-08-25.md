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

- **The 0.1 script had no spoken disclaimer at all.** The lesson *text* carried one, but the video (which is what most students actually consume) never said it. A spoken "what this is and isn't" section was added.
- Four high-risk lessons had no verification line: **4.2** (LTV cushion), **4.3** (the four debt plays), **6.4** (guardrails), **8.2** (access split). Each now names the limit of what's being taught and points to the right professional.

**Still to consider with counsel:** whether the Bitcoin-backed borrowing material (4.2, 4.3, 6.3) needs a stronger standing warning than the lesson-level lines now carry, given it is the highest-stakes content in the course.

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

## Part 4b — A8.1 trust lesson: blocking estate-attorney review (added 2026-08-08)

**`A8.1 Advanced: do you need a trust, and which one?` is held TEXT-ONLY and
UNPUBLISHED until an estate attorney signs off on the substance.** This is a
separate review from Parts 1–3: those concern the education-vs-advice line and
the course's own legal documents. This one is about whether the legal statements
in a single lesson are *correct*.

The lesson makes high-stakes claims in six areas. Each needs confirmation, and
each needs a note on how state-specific it is:

| # | Claim area | What the lesson currently asserts |
|---|---|---|
| 1 | **Revocable living trusts** | Avoid probate, preserve privacy, give a smooth incapacity handoff — and **do not** lower an estate tax bill, because the tax follows control |
| 2 | **Irrevocable trusts** | Removing assets from the taxable estate requires genuinely giving up control; future growth escapes the estate too |
| 3 | **Creditor protection** | An irrevocable trust "can shield assets from creditors and lawsuits" |
| 4 | **Taxable estates** | Federal estate tax touches a tiny fraction of estates; a handful of states run their own at far lower thresholds |
| 5 | **Trustee duties** | Trustees are generally held to a prudent-investor standard; a trustee holding concentrated Bitcoin can be pressured to sell and can be personally liable; a drafted waiver can release the duty to diversify *this* asset |
| 6 | **International structures** | UK nil-rate bands and lifetime gifts · Canadian alter-ego and joint partner trusts · Australian testamentary trusts · continental foundations and usufruct |

**Questions for the estate attorney, in addition to Part 5:**

8. Are claims 1–5 accurate as general statements of US law, and where does state law materially change them?
9. Is the prudent-investor waiver characterised correctly — is it genuinely available, genuinely non-boilerplate, and does the personal-liability framing overstate the risk?
10. Is the multisig arrangement described (trustee holds one key, never the seed) sound as a way to give a trustee real participation without unilateral access?
11. Should the international paragraph be cut rather than reviewed? It is four jurisdictions in three sentences and no one attorney can sign off on all of them.

⚠ **Nothing in A8.1 is filmed or published to students until this is resolved.**
Its master, script and lesson-text layers all carry the block marker.

---

## Part 4c — The four professional reviews, and what each one gates

> ## ⚠ STATUS: REVIEW MATERIALS COMPLETE. REVIEWS OUTSTANDING.
>
> **Preparing this packet does not discharge the obligation it describes.** Not
> one of the four reviews below has happened. Everything in this part is a brief
> for a reviewer, not a finding from one, and no claim in the course has been
> professionally verified.
>
> **Each review gates a specific production wave**, and the point of gating them
> that way is to avoid discovering a factual correction after an expensive
> recording:
>
> | Review | Must complete before |
> |---|---|
> | **Bitcoin-aware CPA** | filming or publishing **Module 5**, and the affected advanced tax lessons (A5.1, A5.2, A5.3, A6.2) |
> | **Custody professional** | filming **Module 7** |
> | **Insurance professional** | filming **8.4** |
> | **Estate attorney** | publishing **A8.1**, and finalising the executor materials in **8.1 / 8.5** |
>
> Module 5 is Wave 2, so the CPA review is not urgent today — but it is the one
> most likely to produce an arithmetic correction, and arithmetic corrections are
> what force re-records.



**Added 2026-08-08.** Part 4b holds A8.1 specifically. This part is the full map:
the course can be opinionated about planning while being precise about where
professional execution begins, and that line is only defensible if the factual
claims underneath it have been checked by someone licensed to check them.

**These reviewers are not reviewing Austin's planning philosophy.** They are
reviewing factual and legal accuracy. A reviewer who wants to change *what Austin
recommends* is outside their remit — `AUSTIN-AUTHORITY.md` governs that, and it
outranks a reviewer's preference for a more conservative default.

### The four reviews

| # | Reviewer | Reviews | Blocking? |
|---|---|---|---|
| 1 | **Estate attorney** | Trust mechanics, executor and document roles, beneficiary/POD/TOD control, probate, the prudent-investor waiver | **Yes** — A8.1 is held unpublished (Part 4b) |
| 2 | **Bitcoin-aware CPA** | Cost basis and lot accounting, basis at death, Roth conversion mechanics, bracket-window logic, harvesting, RMDs, 529 and student-loan tax treatment | **Yes** for basis-at-death and Roth mechanics |
| 3 | **Custody professional** | Advanced recovery design: passphrase, multisig, collaborative custody, the wipe-and-restore standard, the institutional death-claim path | No — review before Module 7 films |
| 4 | **Insurance professional** | Coverage-gap arithmetic, product terminology, when a category is genuinely out of scope | No — review before Module 8 films |

### What to send, by priority

**1 · Estate attorney (blocking).** Full list in Part 4b. Plus:

- **Beneficiary language** — the course teaches *"for an account governed by a
  valid beneficiary, POD, or TOD designation, the provider's form generally
  controls instead of the will,"* and deliberately rejects the flat *"the form
  overrides the will."* Confirm the qualified version is right, and that the
  named exceptions (state law, community property, plan documents, spousal
  consent, validity of the designation) are the right ones to name.
- **Executor Packet** — a student hands this to a real person who then signs an
  acceptance page. Confirm the acceptance page creates no obligation the signer
  would not expect, and that the role description matches what an executor
  actually does.

**2 · Bitcoin-aware CPA (blocking on two items).**

| Claim | Where | Ask |
|---|---|---|
| **Basis at death** | A6.2 — *"under current law (verify), it passes to heirs with a step-up in basis"* | Is the step-up correctly stated, and is the "verify" caveat doing enough work given how much the worked example depends on it? |
| **Roth conversion mechanics** | 5.2, A5.1 | Conversions, the pro-rata rule, the backdoor Roth warning in 4.3, and RMD interaction |
| **Cost basis and lots** | 5.1 | Per-lot tracking, what a missing basis actually costs, reconstruction method |
| **Harvesting** | A5.2 | Loss and gain harvesting, and the wash-sale treatment the course assumes |
| **529 and student loans** | 2.4 | Qualified distributions, beneficiary changes, the student-loan allowance, the Roth rollover conditions, FAFSA reporting |
| **Bracket windows** | 5.2, A5.1 | The three-stage roadmap and the low-income-window logic |

⚠ **The two blocking items are basis at death and Roth conversion mechanics**,
because both drive arithmetic a student will act on.

**3 · Custody professional (before Module 7 films).**

- The four levels and what each one buys and costs
- The **wipe-and-restore** standard as the recovery proof for self-custody
- The **institutional path** added 2026-08-08: is *"login recovery run end to end,
  and the institution's death-claim process read and verified with the provider"*
  the right equivalent proof for a Level 1 household with no device to restore?
- Passphrase, multisig and collaborative designs in A7.1, including the
  seven-random-word passphrase standard and the multisig config-file backup
- The trustee-holds-one-key-never-the-seed arrangement in A8.1 (overlaps review 1)

**4 · Insurance professional (before Module 8 films).**

- The **coverage-gap arithmetic** in 8.4 and the Coverage Audit worksheet — this
  is the one place the course produces an insurance *number*
- Term life, disability and umbrella terminology, and the "when to stop" line
- ⚠ Confirm the course is right to *route* rather than *recommend*:
  `SOURCE-MATERIAL-POLICY.md` explicitly rejects becoming an insurance
  curriculum, so the reviewer should check the boundary is drawn safely, not
  push for more coverage teaching

### The standing rule for every reviewer

**Current-law figures stay in updateable text or the app — never in evergreen
narration.** That is already how the course is written: no bracket, limit,
exemption, RMD age, 529 figure or loan ceiling is spoken on camera. A reviewer
who supplies a current number is supplying a `lesson-text/` or app value with a
verification note, not a script line.

---

## Part 5 — Questions to put to the attorney

1. Does the course, as written and disclaimed, sit within the publisher's exclusion?
2. Does a live group-call component change that answer, and what format keeps it safe?
3. Is a separate course Terms of Service needed, or can the app Terms be extended?
4. Is the annual-subscription structure subject to auto-renewal disclosure rules in our state?
5. Is the Bitcoin-backed borrowing content adequately disclaimed, or does it need a standing warning?
6. Does Austin's professional background or any current or former licensure create additional obligations here?
7. What review, if any, does course marketing copy need before launch?
