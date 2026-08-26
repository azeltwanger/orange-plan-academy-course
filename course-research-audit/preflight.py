#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def patch(path: str, replacements: list[tuple[str, str]]) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    for old, new in replacements:
        if old not in text:
            raise RuntimeError(f"{path}: preflight source text not found: {old[:100]!r}")
        text = text.replace(old, new, 1)
    target.write_text(text, encoding="utf-8")


patch("course-research-audit/tax_replacements.py", [
    (
        "## Complete when\n\nEvery material lot is labeled verified, estimated for planning, or unproven; the source evidence is retained outside Orange Plan; and unresolved basis goes to the tax professional before a return claims it.",
        "## YOUR DECISION\n\nWhich lots are verified, estimated for planning, or unproven.\n\n## PUT IT IN ORANGE PLAN\n\nUse Dashboard → Update Transactions for history and Strategy → Tax for the basis review.\n\n## YOU ARE DONE WHEN\n\nEvery material lot is labeled verified, estimated for planning, or unproven; the source evidence is retained outside Orange Plan; and unresolved basis goes to the tax professional before a return claims it.",
    ),
    (
        "## Complete when\n\nEvery account has a tax job, the low-income window is marked, and the planned move is sized from its all-in marginal cost rather than one bracket label.",
        "## YOUR DECISION\n\nWhat job each account has and which years deserve a tax-window review.\n\n## PUT IT IN ORANGE PLAN\n\nUse Strategy → Tax to model one gain and one conversion without applying either automatically.\n\n## YOU ARE DONE WHEN\n\nEvery account has a tax job, the low-income window is marked, and the planned move is sized from its all-in marginal cost rather than one bracket label.",
    ),
    (
        "The important part is that basis is tracked by units or lots. One purchase on one date can have a completely different basis and holding period from another purchase.",
        "Basis is tracked by units or lots, so one purchase can have a completely different cost and holding period from the next purchase.",
    ),
    (
        "So the real question is not only which federal bracket the next dollar enters.\n\nIt is: what does the next dollar cost after every rule it touches?",
        "So I would not stop at the federal bracket. I would look at what the next dollar actually costs after every rule it touches.",
    ),
    (
        "Every account has a tax job, the low-income window is marked on the timeline, and you can explain why the all-in marginal cost—not one bracket label—decides the size of the move.",
        "You know what job each account has, you can point to the low-income years on the timeline, and you can explain what the next dollar actually costs before you decide how large the move should be.",
    ),
    (
        "So the estate implication is real—traditional money can pass a compressed tax problem to heirs—but the exact schedule belongs in the current beneficiary rules and the family's tax review.",
        "So traditional money can leave heirs with a shorter distribution window and a larger tax problem. The exact schedule depends on the current beneficiary rules and the family's tax situation, so I would verify this part with the CPA.",
    ),
    (
        "The cost is the Bitcoin sold, the tax, and the lost future participation on those units.",
        "When you sell, you are giving up the Bitcoin, paying any tax on the gain, and giving up whatever future growth those units would have had.",
    ),
])

patch("course-research-audit/custody_replacements.py", [
    ("== THE DECISION ==", "== YOUR DECISION =="),
    (
        "**Complete when:** the level and trade-off are written in plain language and the exact setup has a matching recovery test.",
        "## YOUR DECISION\n\nWhich course custody level fits and which failure the added complexity removes.\n\n## PUT IT IN ORANGE PLAN\n\nRecord the level, reason, and next review trigger in Protect without recording secrets.\n\n## YOU ARE DONE WHEN\n\nThe level and trade-off are written in plain language and the exact setup has a matching recovery test.",
    ),
    (
        "**Complete when:** the intended wallet—not only a list of words—was recovered without risking the only working copy of a meaningful balance.",
        "## YOUR DECISION\n\nWhether the setup uses a vendor backup check, spare-device recovery, or an optional staged destructive test.\n\n## PUT IT IN ORANGE PLAN\n\nMark recovery complete in Protect only after the intended wallet was independently verified.\n\n## YOU ARE DONE WHEN\n\nThe intended wallet—not only a list of words—was recovered without risking the only working copy of a meaningful balance.",
    ),
    (
        "**Complete when:** the primary email and custodial accounts use the strongest practical authentication and the largest remaining failure has a dated fix.",
        "## YOUR DECISION\n\nThe largest remaining single point of failure and its dated fix.\n\n## PUT IT IN ORANGE PLAN\n\nRecord checklist completion and the next action in Protect; keep credentials and locations off-app.\n\n## YOU ARE DONE WHEN\n\nThe primary email and custodial accounts use the strongest practical authentication and the largest remaining failure has a dated fix.",
    ),
    ("Austin's 0.01–0.02 BTC transfer threshold", "Austin's 0.01 to 0.02 BTC transfer threshold"),
    (
        "Then write the reason in one sentence.",
        "Then write down why that level fits your household.",
    ),
    (
        "What recovers the wallet depends on the setup: the wallet backup, any passphrase, the address or script type, derivation information, and—for multisig—the wallet policy or descriptor.",
        "What recovers the wallet depends on the setup. That can include the wallet backup, a passphrase, the address or script type, derivation information, and the wallet policy or descriptor if you use multisig.",
    ),
    (
        "The intended wallet—not only a list of words—was recovered without risking the only working copy of a meaningful balance.",
        "You recovered the intended wallet without risking the only working copy of a meaningful balance. Seeing a list of words by itself is not the finish line.",
    ),
    (
        "Consider a second independent institution when:",
        "I would look at a second independent institution when:",
    ),
])

patch("course-research-audit/estate_insurance_replacements.py", [
    (
        "- **Beneficiary/POD/TOD and plan records:** generally transfer the covered asset outside the will, subject to plan terms, ERISA, spousal consent, QDROs, state law, and validity.",
        "- **Beneficiary/POD/TOD and plan records:** a valid provider-held designation generally controls that covered asset instead of the will, subject to plan terms, ERISA, spousal consent, QDROs, state law, and validity.",
    ),
    (
        "**Complete when:** the executor has accepted, provider-held beneficiary records were reviewed, and a state-licensed attorney has the digital-asset and custody questions.",
        "## YOUR DECISION\n\nWho will be nominated, whether they accepted, and which state-licensed attorney will coordinate the documents.\n\n## PUT IT IN ORANGE PLAN\n\nRecord completion status and beneficiary intent in Protect; confirm the binding record with each provider.\n\n## YOU ARE DONE WHEN\n\nThe executor has accepted, provider-held beneficiary records were reviewed, and a state-licensed attorney has the digital-asset and custody questions.",
    ),
    (
        "**Complete when:** both tests are answered honestly and the intended recovery team has tested the process without giving one unintended person enough to spend.",
        "## YOUR DECISION\n\nWhich access test the setup passes, which it fails, and why that trade-off is accepted.\n\n## PUT IT IN ORANGE PLAN\n\nRecord the level and recovery-test status in Protect without storing the secret distribution.\n\n## YOU ARE DONE WHEN\n\nBoth tests are answered honestly and the intended recovery team has tested the process without giving one unintended person enough to spend.",
    ),
    (
        "**Complete when:** the family recognizes the test message, can find the process documents, and still possesses no secret merely because the letter exists.",
        "## YOUR DECISION\n\nThe first contact, first prohibited action, recipients, and backup delivery method.\n\n## PUT IT IN ORANGE PLAN\n\nDraft and export the heir letter in Protect; arm or document the delivery process without storing secrets.\n\n## YOU ARE DONE WHEN\n\nThe family recognizes the test message, can find the process documents, and still possesses no secret merely because the letter exists.",
    ),
    (
        "**Complete when:** the rough math is labeled, contract terms came from the policy, and exact gaps go to a licensed reviewer.",
        "## YOUR DECISION\n\nWhich gaps need a current contract or quote review and which risks the household retains.\n\n## PUT IT IN ORANGE PLAN\n\nRecord review status and unresolved gaps in Protect; carrier contracts remain the source of truth.\n\n## YOU ARE DONE WHEN\n\nThe rough math is labeled, contract terms came from the policy, and exact gaps go to a licensed reviewer.",
    ),
    (
        "The first contact, the first prohibited action, the recipients, and the backup delivery method if automation fails.",
        "Write down who gets contacted first, what they should not do, who receives the message, and how the letter gets delivered if the automatic process fails.",
    ),
    (
        "The gap—not the salary—is the planning result.",
        "The number we are trying to cover is the gap between what the family would need and what the assets and other income could already provide.",
    ),
])

patch("course-research-audit/apply.py", [
    ("(?i)(seed|backup).{0,50}works? in any hardware wallet", "(?i)(seed\\|backup).{0,50}works? in any hardware wallet"),
    ("(?i)irrevocable.{0,50}(automatically|means).{0,50}(outside|leave).{0,30}estate", "(?i)irrevocable.{0,50}(automatically\\|means).{0,50}(outside\\|leave).{0,30}estate"),
])
