# September 10 manuscript finish — targeted patches

## Bounded-review follow-up

The owner supplied Claude's bounded review of PR #30: the arithmetic and seven stated attention items passed, with four wording fixes requested. This follow-up changes narration only in 03 / 1.4, 10 / 3.6 and the Bitcoin-loan lesson / A3.1. The 25 + 8 structure and all other narration, including insurance and the Reserve, remain unchanged.

- A3.1 now states at the sizing step that $50,000 assumes interest/fees are separately funded; capitalize them only after resizing principal or supporting BTC. The later example ties one year of 12% directly to the exhausted $6,000 headroom.
- A3.1 explicitly compares 50% initial posting with about 14.3% when all 3.5 BTC is posted upfront.
- 3.6 labels 25% as a mechanical comparison showing the effect of more upfront collateral, not a competing default.
- 1.4 restores "Don't choose the most optimistic return just to reach the retirement date you want" beside the existing conservative-assumption reasoning.

[First-party owner excerpts and upstream addendum](../reference/owner-decisions-20260910.md) make the insurance and reviewer authority retrievable. The previous audit's historical LTV quote remains historical. The exact external voice-and-philosophy/research/project-instruction originals were not found in accessible sources; they have **not** been marked edited. Use the supplied addendum there before treating upstream synchronization as finished. No app repository files are changed.

New regression checks cover the sizing condition at its point of use, the numerical comparison, the restored failure mode, the user-originated insurance/reviewer statements and the untouched insurance/Reserve narration. Repository tests do not constitute a fresh independent Claude review of this follow-up.

## Read the current version

[All recording scripts](../ALL-FILMING-SCRIPTS.md) · [25-video reading order](../filming/DICTATION-ORDER.md) · [Dated source checks](../reference/script-finishing-sources.md).

This updates the approved 25 main + 8 situation-specific course. It does not redesign the curriculum or add filming assignments. Record narration first; text and graphics are edited afterward. The application is the member's own Orange Plan, with app/device footage captured separately once verified.

## Changed passages

| Recording | Change |
|---|---|
| 01 / 0.1 | Shortened the table-of-contents paragraph. |
| 03 / 1.4 | Restored Austin's conservative-assumption reasoning from his supplied video, without adopting its old return rates. |
| 06 / 2.3 | Only five precisely scoped language edits: two “cannot” contractions, “actually available,” simpler comparison-month wording, and “They're.” The accepted example and liquidity judgment remain exact. |
| College / 2.5; 12 / 4.5 | $850, 70%/30%, and age 59½ formatting. |
| 10 / 3.6 | Removed percentage-tutorial wording; introduced downside-first loan sizing before the initial 50% collateral decision. |
| Bitcoin loan / A3.1 | Added the full 80%-decline reserve calculation and custody trade-off. Explicitly rejects equality with liquidation as sufficient, the extra 50% stressed target, external-wallet automatic top-up, and repeated use of the same reserve. Retains interest, repeat borrowing, estate and repayment consequences. |
| 14 / 5.1 | Missing basis remains unknown, but failure to substantiate it can lead to zero basis. Recover records before relying on the tax result. |
| 17 / 6.3; 20 / 7.1 | Removed redundant three-part signposts. |
| 18 / 6.6 | Added the conditional reason to compare borrowing and tied it to the existing downside and repayment work. No duplicate reserve walkthrough. |
| 19 / 6.8 | Retained the sequence example; added scoped research evidence and a complete 60/80/95 risk-based annual review, inflation-before-cap math, the practical budget choice and Reserve effect. Made-up solver results are labeled. |
| 21 / 7.2 | More direct recovery opening; email first; security keys/passkeys before authenticator codes, with SMS a last resort. Kept backup-access safeguards and removed the redundant hardware-key/wallet summary sentence. |
| 23 / 8.4 | Added Austin's quality-of-life self-funding test, a needs-minus-resources life example, disability capacity and liability/umbrella exposure. No universal net-worth or assumed-Bitcoin-return threshold. |

## Authority and boundaries

Austin's latest borrowing dictation is the course authority: size debt for the severe drawdown against available supporting BTC, then consider a 50% initial LTV to commit less BTC to the lender. The relevant stress constraint is below the actual liquidation threshold with chosen room, plus any earlier contractual cure or maturity requirement. The old conservative 10–20% posted-LTV line is not a competing default. Narrative phrasing is an editorial adaptation of this conversation, not a transcript of a prior video.

Austin's insurance position is to transfer losses that could materially damage the family's quality of life and consider self-funding once resources can comfortably absorb the event. Assets may replace the need to protect earnings while still needing liability protection. There is no invented personal insurance story.

Claude is the cross-checker. The audit's Alfred routing instruction is not part of Austin's workflow. AI review does not count as licensed advice. The proposed categorical will wording stays out. No unreconciled return range, debt-ratio rule, Social Security preference, multisig key distribution or 33-story quota was imported.

The Reserve was previously protected byte-for-byte. The checker now reverses only the five authorized substitutions and verifies the original hash. Every other character and all its financial reasoning remain protected. W02, D07, the fixed Reed fixture, original source material, member toolkit and capture receipts stay unchanged. Previous reviews retain their dates; this fact-check supplements only the stated topics.

## Bounded Claude cross-check

Review the changed narration and adjacent handoffs. Check whether it expresses Austin's approved reasoning, distinguishes example calculations from actual results, respects the source limitations, and lets a beginner understand the choice. Identify any repeated explanation or contradiction introduced by the patches. Do not restart the curriculum or import the audit's older financial defaults.

Pay particular attention to collateral at liquidation equality, stricter cure/maturity requirements, interest consuming the buffer, the annual cap applied after inflation, whether confidence has actually been restored, and cash counted only once. In insurance, check usable assets and continuing income against the changed household costs, rather than testing net worth alone.

## Recording status

The manuscript can receive Austin's spoken read-through. Actual recording, editing, independent Claude review of this commit and app/device capture remain separate work; none is claimed completed by repository tests. The app repo and production systems are unchanged. Read the actual verification and merge evidence in the associated pull request.
