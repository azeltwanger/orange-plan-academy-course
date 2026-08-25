#!/usr/bin/env python3
"""Validate canonical Orange Plan Academy demo checkpoint receipts.

The audit passes when no receipts exist yet. Once a receipt is committed, it must
identify the exact fixture/app context, contain no secret-bearing fields, and
show passing reconciliation checks.
"""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RECEIPT_ROOT = ROOT / "demo" / "receipts"
FIXTURE_VERSION = "demo-v1-inputs"
VALID_CHECKPOINTS = {
    "demo-v1-baseline",
    "demo-v1-cashflow",
    "demo-v1-debt",
    "demo-v1-allocation",
    "demo-v1-tax",
    "demo-v1-income",
    "demo-v1-protect",
    "demo-v1-final",
}
APP_COMMIT = re.compile(r"^[0-9a-f]{7,40}$")
FORBIDDEN_KEY_PARTS = {
    "seedphrase",
    "seedwords",
    "mnemonic",
    "privatekey",
    "walletbackup",
    "passphrase",
    "password",
    "pincode",
    "safecombination",
    "socialsecuritynumber",
    "fullaccountnumber",
    "authenticationcode",
}

REQUIRED_OUTPUT_KEYS = {
    "demo-v1-baseline": {
        "confidenceAtPlannedAgePercent",
        "earliestTargetQualifiedMonthOrAge",
    },
    "demo-v1-cashflow": {
        "displayedTaxAnnualUsd",
        "displayedSurplusMonthlyUsd",
        "reserveMonthsFunded",
    },
    "demo-v1-debt": {
        "displayedDtiPercent",
        "displayedDtaPercent",
        "autoPayoffDate",
    },
    "demo-v1-allocation": {
        "displayedCurrentBitcoinPercent",
        "displayedTargetBitcoinPercent",
        "displayedDrift",
    },
    "demo-v1-tax": {
        "projectedTaxByYear",
        "rothConversionComparison",
    },
    "demo-v1-income": {
        "conservativeSpendingAnnualUsd",
        "balancedSpendingAnnualUsd",
        "aggressiveSpendingAnnualUsd",
        "currentPlanSpendingConfidencePercent",
        "firstYearTotalNeedUsd",
        "firstYearRecurringIncomeUsd",
        "firstYearTotalDrawUsd",
        "accountAndHoldingSourceSplit",
        "bitcoinSoldOrRetained",
        "retirementReserveMonthsFunded",
    },
    "demo-v1-protect": {
        "protectReadiness",
        "recoveryStatus",
        "beneficiaryAndRoleStatus",
    },
    "demo-v1-final": {
        "scenarioDeltas",
        "endingAssetsUsd",
        "projectedEstateUsd",
        "nextActions",
    },
}


def normalize_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def walk(value: Any, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield path, key, child
            yield from walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


def numeric_sum(value: Any) -> float | None:
    if isinstance(value, dict):
        numbers = [item for item in value.values() if isinstance(item, (int, float)) and not isinstance(item, bool)]
        if numbers and len(numbers) == len(value):
            return float(sum(numbers))
    if isinstance(value, list):
        numbers: list[float] = []
        for item in value:
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                numbers.append(float(item))
            elif isinstance(item, dict):
                candidate = item.get("amountUsd", item.get("amount"))
                if isinstance(candidate, (int, float)) and not isinstance(candidate, bool):
                    numbers.append(float(candidate))
                else:
                    return None
            else:
                return None
        return sum(numbers) if numbers else None
    return None


def validate_receipt(path: Path) -> list[str]:
    failures: list[str] = []
    try:
        receipt = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return [f"invalid JSON: {error}"]

    if receipt.get("schemaVersion") != 1:
        failures.append("schemaVersion must be 1")
    if receipt.get("fixtureVersion") != FIXTURE_VERSION:
        failures.append(f"fixtureVersion must be {FIXTURE_VERSION}")

    checkpoint = receipt.get("checkpointId")
    if checkpoint not in VALID_CHECKPOINTS:
        failures.append(f"invalid checkpointId: {checkpoint!r}")
    commit = receipt.get("appCommit")
    if not isinstance(commit, str) or not APP_COMMIT.fullmatch(commit):
        failures.append("appCommit must be a 7–40 character lowercase hexadecimal commit")
    if receipt.get("noSecretsPresent") is not True:
        failures.append("noSecretsPresent must be true")
    if not isinstance(receipt.get("sourceInputHash"), str) or len(receipt["sourceInputHash"]) < 8:
        failures.append("sourceInputHash is missing or too short")

    storage = receipt.get("storageContext")
    if not isinstance(storage, dict):
        failures.append("storageContext must be an object")
    else:
        if storage.get("isolatedFromCustomerData") is not True:
            failures.append("storageContext must be isolated from customer data")
        if not storage.get("syntheticOwner"):
            failures.append("storageContext.syntheticOwner is required")
        if storage.get("mode") not in {"local_test", "development_cloud", "other_isolated_test"}:
            failures.append("storageContext.mode is not an allowed isolated mode")

    outputs = receipt.get("outputs")
    if not isinstance(outputs, dict) or not outputs:
        failures.append("outputs must be a non-empty object")
    elif checkpoint in REQUIRED_OUTPUT_KEYS:
        missing = sorted(REQUIRED_OUTPUT_KEYS[checkpoint] - set(outputs))
        if missing:
            failures.append(f"missing required output keys: {', '.join(missing)}")
        null_values = sorted(key for key in REQUIRED_OUTPUT_KEYS[checkpoint] if outputs.get(key) is None)
        if null_values:
            failures.append(f"canonical receipt contains null required outputs: {', '.join(null_values)}")

    reconciliations = receipt.get("reconciliations")
    if not isinstance(reconciliations, list) or not reconciliations:
        failures.append("reconciliations must be a non-empty array")
    else:
        seen_ids: set[str] = set()
        for index, item in enumerate(reconciliations):
            if not isinstance(item, dict):
                failures.append(f"reconciliations[{index}] must be an object")
                continue
            reconcile_id = item.get("id")
            if not reconcile_id:
                failures.append(f"reconciliations[{index}].id is required")
            elif reconcile_id in seen_ids:
                failures.append(f"duplicate reconciliation id: {reconcile_id}")
            else:
                seen_ids.add(str(reconcile_id))
            status = item.get("status")
            if status not in {"pass", "not_applicable"}:
                failures.append(
                    f"reconciliation {reconcile_id or index} is not canonical: status={status!r}"
                )
            if not item.get("description"):
                failures.append(f"reconciliations[{index}].description is required")

    if checkpoint == "demo-v1-income" and isinstance(outputs, dict):
        total_draw = outputs.get("firstYearTotalDrawUsd")
        split_sum = numeric_sum(outputs.get("accountAndHoldingSourceSplit"))
        if isinstance(total_draw, (int, float)) and split_sum is not None:
            if not math.isclose(float(total_draw), split_sum, rel_tol=0, abs_tol=1):
                failures.append(
                    f"Income source split ({split_sum}) does not reconcile to total draw ({total_draw})"
                )
        else:
            failures.append("Income receipt source split must contain numeric amounts that can be reconciled")

    for parent, key, _ in walk(receipt):
        normalized = normalize_key(key)
        if any(part in normalized for part in FORBIDDEN_KEY_PARTS):
            failures.append(f"secret-bearing field name detected at {parent}.{key}")

    expected_parts = [FIXTURE_VERSION, str(checkpoint), str(commit)]
    relative = str(path.relative_to(RECEIPT_ROOT)).replace("\\", "/")
    for part in expected_parts:
        if part not in relative:
            failures.append(f"receipt path does not include {part!r}: {relative}")

    return failures


def main() -> int:
    if not RECEIPT_ROOT.exists():
        print("# Checkpoint receipt audit\n")
        print("- Canonical receipts found: **0**")
        print("\nNo receipts are expected until the approved synthetic household is run in the current app.")
        return 0

    paths = sorted(RECEIPT_ROOT.rglob("*.json"))
    print("# Checkpoint receipt audit\n")
    print(f"- Canonical receipts found: **{len(paths)}**")

    all_failures: dict[str, list[str]] = {}
    for path in paths:
        failures = validate_receipt(path)
        if failures:
            all_failures[str(path.relative_to(ROOT))] = failures

    print(f"- Receipts with findings: **{len(all_failures)}**")

    if all_failures:
        print("\n## Failures")
        for path, failures in all_failures.items():
            print(f"\n### `{path}`")
            for failure in failures:
                print(f"- {failure}")
        return 1

    print("\nEvery committed receipt identifies the fixture/app context, contains passing reconciliations, and passes the no-secrets field check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
