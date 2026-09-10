# Alignment to accepted Orange Plan direction

Future-design reference: [app PR #227](https://github.com/azeltwanger/orange-plan/pull/227), inspected September 10, 2026 at `21fedfbb1290bfdd637f3b0879bf7e7d6bfdbbc2`, and its [current product directive](https://github.com/azeltwanger/orange-plan/pull/227#issuecomment-5618008737), updated that morning. The directive and accepted product decisions guide the scripts; the inspected head is not an assertion that every change at that head is approved or shipped. The PR was open and draft. Teaching can be filmed independently; screen captures require the actual redesigned flow to pass the checks in WALKTHROUGH-CAPTURE-DEPENDENCIES.md.

| Accepted rule | Course implementation | Capture requirement |
|---|---|---|
| Home / Plan / Cash Flow / Protect; Plan has Overview, Build & improve, Scenarios | 0.1, 1.2 and all working sessions use one owner for each record | Verify real navigation and available owner editor; contextual Add or update, no invented global plus |
| Preliminary starting plan differs from full Plan probability | 1.5 and W01 distinguish estimates, full result, planned date and modeled date | No fabricated starting percentage or unverified deterministic-age claim |
| Percent headline and exact count; normal standard 800/1,000 | 1.5, 6.8, W06, W10 | Both values from the same real result; no obsolete color bands or user-target chooser |
| Facts, chosen strategy and what-ifs have separate save semantics | All working sessions; 1.2, 2.4, 4.7 | Facts save at their owner; strategy uses Current / Preview then Save; scenarios stay separate until Save to Plan. Results update automatically; no invented Recalculate button |
| D54/D65: current holdings, activity and purchase details are different | 1.2, 5.1; W01/W05 | Holdings needed is not cash; Add investment is not Add a purchase; unknown history stays unknown |
| Capability truth and non-additive history/transfer reconciliation | 1.2, 5.1, 9.1; W01/W05/W09 | Demonstrate only supported sources; account history does not add to an already current balance |
| Cash reserve is a role, with current-value accessible sources | 2.3, 4.3, 6.1, 6.8 | Cash Flow owns it; no duplicate reserve, pledged-asset or restricted-account assumptions |
| Allocation current/target share a denominator; saving editor is Cash Flow | 4.1–4.7 and W04 | Reconcile the app denominator with the explicitly scoped $1,307,000 teaching portfolio |
| Debt: real loan vs hypothetical loan vs retirement borrowing policy | 3.1, 3.4, 3.6, A3.1, 6.6 | Existing loan belongs in Debt, one future loan in Scenarios, retirement funding policy in Plan. No scenario-created actual loan or assumed loan execution |
| D63 preserves financial model; 50% initial modeled LTV is not a safety recommendation | 3.6, A3.1, 6.6, W06 | Actual terms and supported interest, top-up, release, liquidation and repayment rules; no synthetic risk frequency |
| Standing guardrail portfolio levels differ from proposed spending | 6.8, W06 chapter 8 | Validated inverse calculation and denominator before dollar-guardrail footage; preserve actual annual cap/inflation semantics |
| Tax liability differs from tax payments; conversions compare after-tax outcomes | 2.1, 5.1, 5.4, A5.1 | Actual supported model, separate completed transaction and cash used to pay tax |
| FORM 8949 TAX DATA is an export, not a filed form | 5.1, A5.2, W05 | Review completeness and current identification/filing requirements |
| Protect, reports, backup/restore, Ask and optional external AI require truthful capability claims | 7.1, 7.2, 8.1, 9.1, 10.1 | Prove supported mode, permissions, delivery and restoration; never expose secrets |

The course keeps the financial model's depth while presenting one decision at a time. A missing control is a filming hold, not permission to create a substitute calculation or call a prototype Production.
