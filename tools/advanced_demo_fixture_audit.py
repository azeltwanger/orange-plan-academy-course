#!/usr/bin/env python3
"""Validate Orange Plan Academy Advanced synthetic examples.

The audit keeps arithmetic and example ownership stable without pretending that an
illustrative fixture is a lender agreement, tax return, insurance quote, custody
proof, or legal document.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "demo" / "advanced-demo-fixtures.json"
CONTRACT_PATH = ROOT / "curriculum" / "advanced-learner-questions.json"
EXPECTED_LESSONS = 18
TOLERANCE = 0.02

SCRIPT_ANCHORS = {
    "A1.1": ("94.6%", "91.6%"),
    "A1.2": ("FBTC", "Bitcoin assumptions"),
    "A2.1": ("$30,000", "1.50 BTC", "20%"),
    "A2.2": ("0.45 BTC", "$6,923"),
    "A2.3": ("0.30 BTC", "$20,000"),
    "A2.4": ("collateral", "exit"),
    "A3.1": ("1.25 BTC", "0.40 BTC", "0.10 BTC"),
    "A3.2": ("$40,000", "$80,000"),
    "A3.3": ("$15,000", "$20,000"),
    "A3.4": ("$20,000", "$60,000"),
    "A4.1": ("$101,948", "Bridge"),
    "A4.2": ("$12,000", "$6,000", "$18,000"),
    "A4.3": ("$100,000", "$8,000", "$13,000", "$15,000"),
    "A5.1": ("passphrase", "practice wallet"),
    "A5.2": ("2-of-3", "Jordan"),
    "A5.3": ("1.50 BTC", "small live tranche"),
    "A6.1": ("minor children", "trust"),
    "A6.2": ("1.50 BTC", "successor trustee"),
}


def close(actual: float, expected: float, tolerance: float = TOLERANCE) -> bool:
    return math.isclose(float(actual), float(expected), rel_tol=0, abs_tol=tolerance)


def main() -> int:
    failures: list[str] = []

    if not FIXTURE_PATH.is_file():
        print("Advanced fixture is missing.")
        return 1

    fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    lessons = contract.get("lessons", [])

    privacy = fixture.get("privacy", {})
    for field in (
        "containsClientData",
        "containsAustinPersonalPlan",
        "containsCredentials",
        "containsBitcoinSecrets",
    ):
        if privacy.get(field) is not False:
            failures.append(f"privacy.{field} must be false")
    if privacy.get("synthetic") is not True:
        failures.append("fixture must remain synthetic")

    if len(lessons) != EXPECTED_LESSONS:
        failures.append(f"expected {EXPECTED_LESSONS} Advanced lessons; found {len(lessons)}")

    model = fixture["modeling"]
    if not close(
        model["stressConfidencePercent"] - model["baselineConfidencePercent"],
        model["confidenceDeltaPoints"],
    ):
        failures.append("modeling confidence delta does not reconcile")

    loan = fixture["bitcoinLoan"]
    collateral_value = loan["collateralBtc"] * loan["startingBitcoinPriceUsd"]
    if not close(collateral_value, loan["startingCollateralValueUsd"]):
        failures.append("starting collateral value does not reconcile")
    starting_ltv = loan["loanBalanceUsd"] / collateral_value * 100
    if not close(starting_ltv, loan["startingLtvPercent"]):
        failures.append("starting LTV does not reconcile")

    action_price = loan["loanBalanceUsd"] / loan["collateralBtc"] / (
        loan["illustrativeActionLtvPercent"] / 100
    )
    liquidation_price = loan["loanBalanceUsd"] / loan["collateralBtc"] / (
        loan["illustrativeLiquidationLtvPercent"] / 100
    )
    if not close(action_price, loan["actionThresholdBitcoinPriceUsd"]):
        failures.append("action threshold BTC price does not reconcile")
    if not close(liquidation_price, loan["liquidationThresholdBitcoinPriceUsd"]):
        failures.append("liquidation threshold BTC price does not reconcile")

    def restore_math(price: float) -> tuple[float, float]:
        current_value = loan["collateralBtc"] * price
        target_value = loan["loanBalanceUsd"] / (loan["targetRestoreLtvPercent"] / 100)
        top_up_btc = (target_value - current_value) / price
        target_balance = current_value * (loan["targetRestoreLtvPercent"] / 100)
        cash_paydown = loan["loanBalanceUsd"] - target_balance
        return top_up_btc, cash_paydown

    action_top_up, action_paydown = restore_math(action_price)
    liquidation_top_up, liquidation_paydown = restore_math(liquidation_price)
    if not close(action_top_up, loan["topUpBtcAtActionLine"]):
        failures.append("action-line BTC top-up does not reconcile")
    if not close(action_paydown, loan["cashPaydownUsdAtActionLine"]):
        failures.append("action-line cash paydown does not reconcile")
    if not close(liquidation_top_up, loan["topUpBtcAtLiquidationLine"]):
        failures.append("liquidation-line BTC top-up does not reconcile")
    if not close(liquidation_paydown, loan["cashPaydownUsdAtLiquidationLine"]):
        failures.append("liquidation-line cash paydown does not reconcile")
    if loan["finiteTopUpReserveBtc"] >= loan["topUpBtcAtLiquidationLine"]:
        failures.append("finite top-up example no longer demonstrates resource exhaustion")

    sale = fixture["sellVersusBorrow"]
    if not close(sale["bitcoinSoldBtc"] * sale["saleBitcoinPriceUsd"], sale["saleProceedsUsd"]):
        failures.append("sale proceeds do not reconcile")
    if not close(sale["saleProceedsUsd"] - sale["basisOfUnitsSoldUsd"], sale["modeledGainUsd"]):
        failures.append("modeled sale gain does not reconcile")
    borrow_ltv = sale["borrowAmountUsd"] / (
        sale["borrowCollateralBtc"] * sale["saleBitcoinPriceUsd"]
    ) * 100
    if not close(borrow_ltv, sale["borrowStartingLtvPercent"]):
        failures.append("sell-versus-borrow starting LTV does not reconcile")

    basis = fixture["basis"]
    unresolved = basis["reconstructionPendingBtc"] + basis["missingRecordsBtc"]
    total = basis["completeQuantityBtc"] + unresolved
    if not close(unresolved, basis["unresolvedQuantityBtc"]):
        failures.append("unresolved basis quantity does not reconcile")
    if not close(total, basis["currentBitcoinBtc"]):
        failures.append("basis quantities do not reconcile to current Bitcoin")

    conversion = fixture["rothConversion"]
    if not close(
        conversion["selectedPlanningCeilingUsd"] - conversion["expectedOrdinaryIncomeUsd"],
        conversion["firstPassRoomUsd"],
    ):
        failures.append("first-pass conversion room does not reconcile")

    harvesting = fixture["harvesting"]
    for name in ("lossLot", "gainLot"):
        lot = harvesting[name]
        if not close(lot["currentValueUsd"] - lot["basisUsd"], lot["modeledGainLossUsd"]):
            failures.append(f"{name} gain/loss does not reconcile")

    relocation = fixture["relocation"]
    if not close(
        relocation["illustrativeTaxBenefitUsd"] - relocation["addedThreeYearLifeCostsUsd"],
        relocation["fullLifeNetDeltaUsd"],
    ):
        failures.append("relocation full-life delta does not reconcile")

    healthcare = fixture["healthcare"]
    if not close(
        healthcare["illustrativeNetPremiumUsd"] + healthcare["illustrativeExpectedOutOfPocketUsd"],
        healthcare["illustrativeAllInCostUsd"],
    ):
        failures.append("healthcare all-in cost does not reconcile")

    integrated = fixture["integratedFunding"]
    cash_need = integrated["spendableCashNeedUsd"]
    if not close(
        integrated["taxableFirst"]["cashUsd"] + integrated["taxableFirst"]["taxableSaleUsd"],
        cash_need,
    ):
        failures.append("taxable-first spendable cash does not reconcile")
    if not close(
        integrated["taxablePlusConversion"]["cashUsd"]
        + integrated["taxablePlusConversion"]["taxableSaleUsd"],
        cash_need,
    ):
        failures.append("conversion path spendable cash does not reconcile")
    if not close(
        integrated["employerPlanSource"]["cashUsd"]
        + integrated["employerPlanSource"]["traditionalDistributionUsd"]
        + integrated["employerPlanSource"]["taxableSaleUsd"],
        cash_need,
    ):
        failures.append("employer-plan path spendable cash does not reconcile")

    custody = fixture["custody"]
    if custody["multisigPolicy"] != "2_of_3" or custody["keyCount"] != 3 or custody["signingThreshold"] != 2:
        failures.append("multisig example must remain a correct 2-of-3")
    if len(custody["migrationStages"]) < 6:
        failures.append("custody migration sequence is incomplete")

    trust = fixture["trust"]["mismatch"]
    if not (
        trust["documentClaimsTrustOwnership"]
        and trust["walletStillIndividual"]
        and trust["successorTrusteeNamed"]
        and not trust["successorRecoveryTested"]
        and not trust["providerOrAssignmentProof"]
    ):
        failures.append("trust example no longer demonstrates the intended legal/technical mismatch")

    contract_by_id = {entry["id"]: entry for entry in lessons}
    for lesson_id, anchors in SCRIPT_ANCHORS.items():
        entry = contract_by_id.get(lesson_id)
        if entry is None:
            failures.append(f"missing contract entry for {lesson_id}")
            continue
        script_path = ROOT / entry["script"]
        if not script_path.is_file():
            failures.append(f"missing script for {lesson_id}: {entry['script']}")
            continue
        content = script_path.read_text(encoding="utf-8")
        for anchor in anchors:
            if anchor.lower() not in content.lower():
                failures.append(f"{lesson_id}: fixture anchor {anchor!r} is missing from the current script")

    print("# Advanced demo fixture audit\n")
    print(f"- Advanced lesson contracts: **{len(lessons)}**")
    print(f"- Script/example anchor groups: **{len(SCRIPT_ANCHORS)}**")
    print(f"- Findings: **{len(failures)}**")

    if failures:
        print("\n## Failures")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nThe Advanced examples reconcile, remain synthetic, and still appear in the lessons that own them. External proof gates remain outside the fixture.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
