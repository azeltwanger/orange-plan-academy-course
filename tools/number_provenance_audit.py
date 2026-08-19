#!/usr/bin/env python3
"""Ensure key numeric lessons explain meaning, source, edit location, and impact."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LESSON_REQUIREMENTS = {
    "scripts/01-3_read-your-retirement-date-and-confidence.md": [
        "confidence",
        "earliest",
    ],
    "scripts/02-1_find-your-surplus-and-your-two-spending-.md": ["surplus"],
    "scripts/02-2_size-your-cash-reserve-in-months-of-spen.md": ["reserve target"],
    "scripts/02-3_fund-a-known-future-cost-the-six-questio.md": ["funding gap"],
    "scripts/02-4_optional-college-is-a-funding-stack.md": ["family funding gap"],
    "scripts/03-1_give-every-debt-a-job-and-set-your-ceiling.md": ["dti", "dta"],
    "scripts/04-1_set-the-bitcoin-allocation-you-can-hold.md": [
        "current allocation",
        "drawdown",
    ],
    "scripts/04-2_break-your-accounts-down-by-holding-type.md": [
        "holding mix",
        "timeframe funding",
    ],
    "scripts/04-3_order-your-contributions-which-account-g.md": [
        "available dollars",
        "saved route",
    ],
    "scripts/04-4_asset-location-which-account-each-holdin.md": ["holding mix"],
    "scripts/05-1_cost-basis-what-you-paid-and-how-to-reco.md": [
        "total basis",
        "unrealized gain",
    ],
    "scripts/05-2_taxable-tax-deferred-and-roth-bracket-wi.md": [
        "estimated tax",
        "traditional balance",
    ],
    "scripts/06-1_your-spending-income-floor-gap-and-bridg.md": [
        "retirement spending",
        "recurring income",
        "total draw",
    ],
    "scripts/06-2_set-your-withdrawal-order-and-refill-rul.md": [
        "source split",
        "bitcoin sold",
    ],
    "scripts/06-3_guardrails-how-much-you-can-spend-each-y.md": [
        "spending choice",
        "annual update",
    ],
    "scripts/08-4_insurance-term-life-disability-umbrella-.md": [
        "life gap",
        "disability gap",
    ],
    "scripts/09-2_test-a-decision-and-read-the-finished-plan.md": [
        "scenario delta"
    ],
}

FOUR_LINES = {
    "what it means": re.compile(r"what it means", re.I),
    "calculated from": re.compile(r"calculated from", re.I),
    "edit source": re.compile(r"edit source", re.I),
    "this affects": re.compile(r"this affects", re.I),
}

REGISTRY_REQUIRED_TERMS = (
    "Plan confidence result",
    "Earliest target-qualified date",
    "Reliable surplus",
    "Reserve target amount",
    "Debt-to-income (DTI)",
    "Debt-to-assets (DTA)",
    "Current Bitcoin percentage",
    "Projected tax by year",
    "Total draw",
    "Account and holding source split",
    "Bitcoin sold or retained",
    "Annual spending-policy update",
    "Scenario delta",
    "Encrypted export status",
)


def main() -> int:
    failures: list[str] = []

    for relative_path, owned_numbers in LESSON_REQUIREMENTS.items():
        path = ROOT / relative_path
        if not path.is_file():
            failures.append(f"missing lesson: {relative_path}")
            continue
        content = path.read_text(encoding="utf-8")
        lowered = content.lower()

        for label, pattern in FOUR_LINES.items():
            if not pattern.search(content):
                failures.append(f"{relative_path}: missing provenance line {label!r}")

        for number in owned_numbers:
            if number.lower() not in lowered:
                failures.append(f"{relative_path}: owned number {number!r} is not named")

    registry_path = ROOT / "NUMBER-PROVENANCE-REGISTRY.md"
    if not registry_path.is_file():
        failures.append("missing NUMBER-PROVENANCE-REGISTRY.md")
    else:
        registry = registry_path.read_text(encoding="utf-8")
        for term in REGISTRY_REQUIRED_TERMS:
            if term not in registry:
                failures.append(f"number registry is missing {term!r}")

    print("# Number provenance audit\n")
    print(f"- Numeric lesson contracts checked: **{len(LESSON_REQUIREMENTS)}**")
    print(f"- Registry anchor terms checked: **{len(REGISTRY_REQUIRED_TERMS)}**")
    print(f"- Findings: **{len(failures)}**")

    if failures:
        print("\n## Failures")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nEvery key numeric lesson contains the four provenance lines and the central registry contains the required output contracts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
