#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def patch(path: str, replacements: list[tuple[str, str]]) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    for old, new in replacements:
        if old not in text:
            raise RuntimeError(f"{path}: style source text not found: {old[:120]!r}")
        text = text.replace(old, new, 1)
    target.write_text(text, encoding="utf-8")


patch("course-research-audit/tax_replacements.py", [
    (
        "The important part is that basis is tracked by units or lots.",
        "Basis is tracked by units or lots.",
    ),
    (
        "So the real question is not only which federal bracket the next dollar enters.",
        "A federal bracket label does not answer the cost of the next dollar.",
    ),
    (
        "Every account has a tax job, the low-income window is marked on the timeline, and you can explain why the all-in marginal cost—not one bracket label—decides the size of the move.",
        "Every account has a tax job and the low-income window is marked on the timeline. You can explain why the all-in marginal cost decides the size of the move instead of one bracket label.",
    ),
    (
        "So the estate implication is real—traditional money can pass a compressed tax problem to heirs—but the exact schedule belongs in the current beneficiary rules and the family's tax review.",
        "Traditional money can pass a compressed tax problem to heirs. The exact schedule belongs in the current beneficiary rules and the family's tax review.",
    ),
    (
        "The cost is the Bitcoin sold, the tax, and the lost future participation on those units.",
        "Selling removes the identified Bitcoin units and may create tax. It also gives up their future participation.",
    ),
])

patch("course-research-audit/custody_replacements.py", [
    (
        "Then write the reason in one sentence.",
        "Write why this level fits the household.",
    ),
    (
        "What recovers the wallet depends on the setup: the wallet backup, any passphrase, the address or script type, derivation information, and—for multisig—the wallet policy or descriptor.",
        "Recovery depends on the setup. Inventory the wallet backup, any passphrase, the address or script type, derivation information, and the multisig wallet policy or descriptor.",
    ),
    (
        "The intended wallet—not only a list of words—was recovered without risking the only working copy of a meaningful balance.",
        "Recovery verified the intended wallet rather than only accepting a list of words. The test did not risk the only working copy of a meaningful balance.",
    ),
    (
        "Consider a second independent institution when:",
        "A second independent institution may be appropriate when:",
    ),
])

patch("course-research-audit/estate_insurance_replacements.py", [
    (
        "The first contact, the first prohibited action, the recipients, and the backup delivery method if automation fails.",
        "Name the first contact and the first prohibited action. Then name the recipients and the backup delivery method if automation fails.",
    ),
    (
        "The gap—not the salary—is the planning result.",
        "Compare the policy benefit with the spending floor. The remaining shortfall is the planning result.",
    ),
])
