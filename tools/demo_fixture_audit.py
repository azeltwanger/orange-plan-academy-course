#!/usr/bin/env python3
"""Validate the machine-readable Orange Plan Academy demo fixture."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "demo" / "demo-v1-inputs.json"

FORBIDDEN_KEY_FRAGMENTS = (
    "seedphrase",
    "seed_phrase",
    "mnemonic",
    "privatekey",
    "private_key",
    "walletbackup",
    "wallet_backup",
    "password",
    "passphrase",
    "safecombination",
    "safe_combination",
    "socialsecuritynumber",
    "social_security_number",
    "fullaccountnumber",
    "full_account_number",
)


def close(left: float, right: float, tolerance: float = 0.01) -> bool:
    return math.isclose(left, right, rel_tol=0, abs_tol=tolerance)


def walk(value: Any, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield path, key, child
            yield from walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


def numeric(value: Any, label: str, failures: list[str]) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        failures.append(f"{label} must be numeric")
        return 0.0
    return float(value)


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    if not FIXTURE_PATH.is_file():
        print(f"Missing fixture: {FIXTURE_PATH.relative_to(ROOT)}", file=sys.stderr)
        return 1

    try:
        fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print(f"Invalid JSON: {error}", file=sys.stderr)
        return 1

    if fixture.get("fixtureVersion") != "demo-v1-inputs":
        failures.append("fixtureVersion must be demo-v1-inputs")
    if fixture.get("privacy", {}).get("synthetic") is not True:
        failures.append("fixture must be marked synthetic")
    if fixture.get("privacy", {}).get("containsClientData") is not False:
        failures.append("fixture must explicitly contain no client data")
    if fixture.get("privacy", {}).get("containsSecrets") is not False:
        failures.append("fixture must explicitly contain no secrets")

    incomes = fixture.get("income", [])
    annual_income = sum(
        numeric(row.get("annualGross"), f"income[{index}].annualGross", failures)
        for index, row in enumerate(incomes)
    )
    cash_flow = fixture.get("cashFlow", {})
    if not close(
        annual_income,
        numeric(cash_flow.get("annualGrossIncome"), "cashFlow.annualGrossIncome", failures),
    ):
        failures.append("income rows do not reconcile to annualGrossIncome")

    working_tax = numeric(
        cash_flow.get("workingTeachingTaxEstimate", {}).get("annual"),
        "working tax estimate",
        failures,
    )
    living = numeric(
        cash_flow.get("normalLivingSpendingAnnual"),
        "normal living spending",
        failures,
    )
    debt_payments_annual = numeric(
        cash_flow.get("requiredDebtPaymentsAnnual"),
        "required debt payments",
        failures,
    )
    expected_route = annual_income - working_tax - living - debt_payments_annual
    if not close(
        expected_route,
        numeric(cash_flow.get("approvedRepeatableRouteAnnual"), "approved annual route", failures),
    ):
        failures.append("approved annual route does not reconcile to the teaching equation")
    if not close(
        expected_route / 12,
        numeric(cash_flow.get("approvedRepeatableRouteMonthly"), "approved monthly route", failures),
    ):
        failures.append("approved monthly route does not reconcile to the teaching equation")

    asset_totals = {
        "bitcoin_quantity": 0.0,
        "bitcoin_value": 0.0,
        "stocks": 0.0,
        "bonds": 0.0,
        "cash": 0.0,
        "real_estate": 0.0,
    }
    allocatable_portfolio = 0.0
    beneficiary_restricted_education = 0.0

    for account_index, account in enumerate(fixture.get("accounts", [])):
        scope = account.get("allocationScope")
        if scope not in {
            "included",
            "excluded_beneficiary_restricted",
            "excluded_primary_residence",
        }:
            failures.append(f"accounts[{account_index}].allocationScope is missing or invalid")
        for holding_index, holding in enumerate(account.get("holdings", [])):
            asset_class = holding.get("assetClass")
            label = f"accounts[{account_index}].holdings[{holding_index}]"
            value = 0.0
            if asset_class == "bitcoin":
                quantity = numeric(holding.get("quantity"), f"{label}.quantity", failures)
                value = numeric(
                    holding.get("referenceValueUsd"),
                    f"{label}.referenceValueUsd",
                    failures,
                )
                asset_totals["bitcoin_quantity"] += quantity
                asset_totals["bitcoin_value"] += value
            elif asset_class in {"stocks", "bonds", "cash", "real_estate"}:
                value = numeric(holding.get("valueUsd"), f"{label}.valueUsd", failures)
                asset_totals[asset_class] += value
            else:
                warnings.append(f"unrecognized asset class at {label}: {asset_class!r}")

            if scope == "included":
                allocatable_portfolio += value
            elif scope == "excluded_beneficiary_restricted":
                beneficiary_restricted_education += value

    totals = fixture.get("startingTotalsAtReferenceValuation", {})
    expected_asset_values = {
        "bitcoin_quantity": totals.get("bitcoinQuantity"),
        "bitcoin_value": totals.get("bitcoinValueUsd"),
        "stocks": totals.get("stocksValueUsd"),
        "bonds": totals.get("bondsValueUsd"),
        "cash": totals.get("cashValueUsd"),
        "real_estate": totals.get("homeValueUsd"),
    }
    for key, expected in expected_asset_values.items():
        if not close(asset_totals[key], numeric(expected, f"starting total {key}", failures)):
            failures.append(f"account holdings do not reconcile to starting total: {key}")

    financial_assets = (
        asset_totals["bitcoin_value"]
        + asset_totals["stocks"]
        + asset_totals["bonds"]
        + asset_totals["cash"]
    )
    if not close(
        financial_assets,
        numeric(totals.get("financialAssetsIncludingEducationUsd"), "financialAssetsIncludingEducationUsd", failures),
    ):
        failures.append("financial assets including education do not reconcile")
    if not close(
        financial_assets,
        numeric(totals.get("investableAssetsUsd"), "investableAssetsUsd", failures),
    ):
        failures.append("legacy investableAssetsUsd alias does not reconcile")
    if not close(
        beneficiary_restricted_education,
        numeric(totals.get("beneficiaryRestrictedEducationUsd"), "beneficiaryRestrictedEducationUsd", failures),
    ):
        failures.append("beneficiary-restricted education total does not reconcile")
    if not close(
        allocatable_portfolio,
        numeric(totals.get("allocatablePortfolioUsd"), "allocatablePortfolioUsd", failures),
    ):
        failures.append("allocatable portfolio does not reconcile")

    gross_assets = financial_assets + asset_totals["real_estate"]
    if not close(
        gross_assets,
        numeric(totals.get("grossAssetsUsd"), "grossAssetsUsd", failures),
    ):
        failures.append("gross asset total does not reconcile")

    debts = fixture.get("debts", [])
    total_debt = sum(
        numeric(row.get("balanceUsd"), f"debts[{index}].balanceUsd", failures)
        for index, row in enumerate(debts)
    )
    required_payments = sum(
        numeric(row.get("requiredPaymentMonthly"), f"debts[{index}].requiredPaymentMonthly", failures)
        for index, row in enumerate(debts)
    )
    debt_metrics = fixture.get("startingDebtMetricsAtReferenceValuation", {})
    if not close(
        total_debt,
        numeric(debt_metrics.get("totalDebtUsd"), "totalDebtUsd", failures),
    ):
        failures.append("debt balances do not reconcile")
    if not close(
        required_payments,
        numeric(debt_metrics.get("requiredPaymentsMonthly"), "requiredPaymentsMonthly", failures),
        tolerance=1,
    ):
        failures.append("required debt payments do not reconcile")

    gross_monthly_income = annual_income / 12
    calculated_dti = required_payments / gross_monthly_income * 100
    if not close(
        calculated_dti,
        numeric(debt_metrics.get("dtiPercent"), "dtiPercent", failures),
        tolerance=0.1,
    ):
        failures.append("reference DTI does not reconcile")
    calculated_dta = total_debt / gross_assets * 100
    if not close(
        calculated_dta,
        numeric(debt_metrics.get("dtaPercent"), "dtaPercent", failures),
        tolerance=0.1,
    ):
        failures.append("reference DTA does not reconcile")

    reserve = fixture.get("reserve", {})
    reserve_target = (
        numeric(reserve.get("basisMonthlyUsd"), "reserve basis", failures)
        * numeric(reserve.get("targetMonths"), "reserve months", failures)
    )
    if not close(
        reserve_target,
        numeric(reserve.get("targetUsd"), "reserve target", failures),
    ):
        failures.append("reserve target does not reconcile")

    routing = fixture.get("monthlyRouting", {})
    route_total = sum(
        numeric(row.get("amountUsd"), f"routing[{index}].amountUsd", failures)
        for index, row in enumerate(routing.get("destinations", []))
    )
    if not close(route_total, numeric(routing.get("availableUsd"), "routing available", failures)):
        failures.append("monthly routing does not reconcile to the approved amount")
    if route_total - numeric(
        cash_flow.get("approvedRepeatableRouteMonthly"),
        "approved monthly route",
        failures,
    ) > 0.01:
        failures.append("monthly routing exceeds the approved repeatable route")

    events_by_id = {event.get("id"): event for event in fixture.get("lifeEvents", [])}
    vehicle = events_by_id.get("vehicle-replacement", {})
    vehicle_gap = (
        numeric(vehicle.get("purchaseCeilingUsd"), "vehicle ceiling", failures)
        - numeric(vehicle.get("expectedProceedsUsd"), "vehicle proceeds", failures)
        - numeric(vehicle.get("expectedCashFlowInPurchaseYearUsd"), "vehicle cash flow", failures)
    )
    if not close(
        vehicle_gap,
        numeric(vehicle.get("amountToAccumulateUsd"), "vehicle amount to accumulate", failures),
    ):
        failures.append("vehicle funding gap does not reconcile")

    college = events_by_id.get("college-commitment", {})
    college_sources = (
        numeric(college.get("existing529Usd"), "college 529", failures)
        + numeric(college.get("parentCashFlowDuringCollegeUsd"), "college parent cash flow", failures)
        + numeric(college.get("studentAidWorkOrAcceptedBorrowingUsd"), "college student source", failures)
        + numeric(college.get("remainingToAccumulateOrFundUsd"), "college remaining source", failures)
    )
    if not close(
        college_sources,
        numeric(college.get("familyCommitmentUsd"), "college commitment", failures),
    ):
        failures.append("college funding stack does not reconcile")

    lots = fixture.get("bitcoinTaxLots", {})
    lot_quantity = sum(
        numeric(row.get("quantity"), f"bitcoinTaxLots.positions[{index}].quantity", failures)
        for index, row in enumerate(lots.get("positions", []))
    )
    if not close(
        lot_quantity,
        numeric(lots.get("totalQuantity"), "bitcoin tax-lot total quantity", failures),
    ):
        failures.append("Bitcoin tax-lot quantity does not reconcile")
    if not close(lot_quantity, asset_totals["bitcoin_quantity"]):
        failures.append("Bitcoin tax-lot quantity does not match holdings")

    allocation = fixture.get("allocation", {})
    current_btc_allocatable = asset_totals["bitcoin_value"] / allocatable_portfolio * 100
    if not close(
        current_btc_allocatable,
        numeric(
            allocation.get("currentBitcoinPercentOfAllocatableAtReferencePrice"),
            "current Bitcoin percent of allocatable portfolio",
            failures,
        ),
        tolerance=0.1,
    ):
        failures.append("app-scope Bitcoin allocation does not reconcile")
    current_btc_financial = asset_totals["bitcoin_value"] / financial_assets * 100
    if not close(
        current_btc_financial,
        numeric(
            allocation.get("currentBitcoinPercentOfFinancialAssetsAtReferencePrice"),
            "current Bitcoin percent of financial assets",
            failures,
        ),
        tolerance=0.1,
    ):
        failures.append("full financial-asset Bitcoin percentage does not reconcile")

    drawdown = numeric(allocation.get("drawdownTestPercent"), "drawdown percent", failures) / 100
    loss = asset_totals["bitcoin_value"] * drawdown
    if not close(
        loss,
        numeric(allocation.get("referenceBitcoinLossUsd"), "reference Bitcoin loss", failures),
    ):
        failures.append("reference Bitcoin drawdown loss does not reconcile")
    if not close(
        allocatable_portfolio - loss,
        numeric(
            allocation.get("referenceAllocatablePortfolioAfterDrawdownUsd"),
            "allocatable portfolio after drawdown",
            failures,
        ),
    ):
        failures.append("allocatable post-drawdown portfolio does not reconcile")
    if not close(
        financial_assets - loss,
        numeric(
            allocation.get("referenceFinancialAssetsAfterDrawdownUsd"),
            "financial assets after drawdown",
            failures,
        ),
    ):
        failures.append("full financial post-drawdown total does not reconcile")

    retirement = fixture.get("retirementIncome", {})
    spending_choice = retirement.get("startingSpendingChoice", {})
    if spending_choice.get("status") != "approved_from_engine_candidate_ui_verification_pending":
        failures.append("starting spending choice must record the approved engine-candidate status")
    if not close(
        numeric(spending_choice.get("valueAnnualUsd"), "starting spending choice", failures),
        numeric(retirement.get("baselineLivingSpendingAnnualTodayDollars"), "retirement baseline spending", failures),
    ):
        failures.append("starting spending choice must match the deliberate Plan amount")

    candidate = fixture.get("engineCheckpointCandidate", {})
    if candidate.get("status") != "generated_ui_verification_pending":
        failures.append("engine checkpoint candidate status is missing")
    if not isinstance(candidate.get("appCommit"), str) or len(candidate.get("appCommit", "")) < 7:
        failures.append("engine checkpoint candidate must record an app commit")

    for path, key, child in walk(fixture):
        normalized_key = key.lower().replace("-", "").replace(" ", "")
        if any(fragment.replace("_", "") in normalized_key for fragment in FORBIDDEN_KEY_FRAGMENTS):
            if key not in {"containsSecrets"}:
                failures.append(f"forbidden secret-bearing field name at {path}.{key}")
        if isinstance(child, (int, float)) and not isinstance(child, bool) and child < 0:
            if not path.startswith("$.engineCheckpointCandidate.final"):
                warnings.append(f"negative numeric value at {path}.{key}; confirm it is intentional")

    outputs = fixture.get("checkpointOutputPlaceholders", {})
    for path, key, child in walk(outputs, "$.checkpointOutputPlaceholders"):
        if key == "source":
            if child != "orange_plan_current_app":
                failures.append(f"checkpoint source must remain orange_plan_current_app at {path}.{key}")
        elif child is not None and not isinstance(child, dict):
            failures.append(f"app-owned output placeholder must remain null at {path}.{key}")

    print("# Demo fixture audit")
    print()
    print(f"- Fixture: **{fixture.get('fixtureVersion')}**")
    print(f"- Accounts: **{len(fixture.get('accounts', []))}**")
    print(f"- Debts: **{len(debts)}**")
    print(f"- Life events: **{len(fixture.get('lifeEvents', []))}**")
    print(f"- Financial assets including education: **${financial_assets:,.0f}**")
    print(f"- App allocatable portfolio: **${allocatable_portfolio:,.0f}**")
    print(f"- Reference gross assets: **${gross_assets:,.0f}**")
    print(f"- Bitcoin quantity: **{asset_totals['bitcoin_quantity']:.2f} BTC**")
    print(f"- Approved monthly route: **${route_total:,.0f}**")
    print(f"- Engine candidate commit: **{candidate.get('appCommit', 'missing')}**")
    print(f"- Critical findings: **{len(failures)}**")
    print(f"- Warnings: **{len(warnings)}**")

    if warnings:
        print("\n## Warnings")
        for warning in warnings:
            print(f"- {warning}")

    if failures:
        print("\n## Failures")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "\nAll course-owned inputs and engine-candidate controls reconcile. "
        "Final app-owned receipt fields remain null until deployed UI verification."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
