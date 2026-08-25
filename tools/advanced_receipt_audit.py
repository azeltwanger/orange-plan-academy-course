#!/usr/bin/env python3
"""Audit Advanced demonstration receipt coverage and honesty."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "demo" / "advanced-receipt-manifest.json"
RECEIPT_DIR = ROOT / "demo" / "advanced-receipts"
CONTRACT_PATH = ROOT / "curriculum" / "advanced-learner-questions.json"
EXPECTED_DEMOS = {f"AD{i}" for i in range(1, 10)}
ALLOWED_STATUS = {"hold", "candidate", "accepted", "retired"}
ALLOWED_STATE = {"saved", "preview", "scenario", "recorded_status", "external_only", "mixed"}


def validate_receipt(path: Path, expected_demo: str) -> list[str]:
    failures: list[str] = []
    try:
        receipt = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"{path.relative_to(ROOT)}: invalid JSON: {exc}"]

    required = (
        "receiptVersion",
        "demoId",
        "lessonIds",
        "status",
        "synthetic",
        "evidenceType",
        "sourceVersion",
        "capturedAt",
        "decision",
        "state",
        "inputs",
        "outputs",
        "externalProof",
        "limitations",
    )
    for key in required:
        if key not in receipt:
            failures.append(f"{path.name}: missing {key}")

    if receipt.get("receiptVersion") != 1:
        failures.append(f"{path.name}: receiptVersion must be 1")
    if receipt.get("demoId") != expected_demo:
        failures.append(f"{path.name}: demoId must be {expected_demo}")
    if receipt.get("status") not in ALLOWED_STATUS:
        failures.append(f"{path.name}: invalid status")
    if receipt.get("synthetic") is not True:
        failures.append(f"{path.name}: receipt must use synthetic/redacted evidence only")

    state = receipt.get("state", {})
    if state.get("savedPreviewScenarioOrRecorded") not in ALLOWED_STATE:
        failures.append(f"{path.name}: invalid saved/preview/Scenario state")
    for key in ("completionRule", "humanFinishLine"):
        if not str(state.get(key, "")).strip():
            failures.append(f"{path.name}: state.{key} is required")

    source = receipt.get("sourceVersion", {})
    for key in ("courseCommit", "sourceName", "sourceVersionOrDate"):
        if not str(source.get(key, "")).strip():
            failures.append(f"{path.name}: sourceVersion.{key} is required")

    proof = receipt.get("externalProof", [])
    if not isinstance(proof, list) or not proof:
        failures.append(f"{path.name}: externalProof must name the evidence boundary")

    if receipt.get("status") == "accepted":
        if receipt.get("capturedAt") is None:
            failures.append(f"{path.name}: accepted receipt needs capturedAt")
        if any(item.get("status") == "hold" for item in proof if isinstance(item, dict)):
            failures.append(f"{path.name}: accepted receipt still contains a hold")
        accepted_roles = receipt.get("acceptedBy", [])
        if not accepted_roles:
            failures.append(f"{path.name}: accepted receipt needs acceptedBy roles")
        elif any(item.get("status") == "hold" for item in accepted_roles if isinstance(item, dict)):
            failures.append(f"{path.name}: accepted receipt has an unaccepted required role")

    serialized = json.dumps(receipt).lower()
    forbidden = (
        "seed phrase",
        "private key",
        "xprv",
        "authentication code",
        "real client",
        "customer name",
    )
    for term in forbidden:
        if term in serialized and "never" not in serialized and "no " not in serialized:
            failures.append(f"{path.name}: possible prohibited sensitive content marker {term!r}")

    return failures


def main() -> int:
    failures: list[str] = []
    if not MANIFEST_PATH.is_file():
        print("Advanced receipt manifest is missing.")
        return 1

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    entries = manifest.get("receipts", [])
    demos = {entry.get("demoId") for entry in entries}

    if demos != EXPECTED_DEMOS:
        failures.append(f"manifest demo IDs are {sorted(demos)}; expected {sorted(EXPECTED_DEMOS)}")
    if len(entries) != len(EXPECTED_DEMOS):
        failures.append(f"manifest has {len(entries)} entries; expected 9")

    lesson_contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8")).get("lessons", [])
    expected_lessons = {entry["id"] for entry in lesson_contract}
    covered_lessons: list[str] = []

    for entry in entries:
        demo_id = entry.get("demoId")
        if entry.get("status") not in ALLOWED_STATUS:
            failures.append(f"{demo_id}: invalid manifest status")
        if not entry.get("required"):
            failures.append(f"{demo_id}: required evidence list is empty")
        covered_lessons.extend(entry.get("lessonIds", []))

        receipt_path = RECEIPT_DIR / f"{demo_id}.json"
        if receipt_path.exists():
            failures.extend(validate_receipt(receipt_path, demo_id))
            if entry.get("status") == "hold":
                failures.append(f"{demo_id}: receipt file exists but manifest still says hold")
        elif entry.get("status") in {"candidate", "accepted"}:
            failures.append(f"{demo_id}: manifest says {entry.get('status')} but receipt file is missing")

    if set(covered_lessons) != expected_lessons:
        missing = sorted(expected_lessons - set(covered_lessons))
        extra = sorted(set(covered_lessons) - expected_lessons)
        failures.append(f"receipt lesson coverage mismatch; missing={missing}, extra={extra}")
    if len(covered_lessons) != len(set(covered_lessons)):
        failures.append("a current Advanced lesson is assigned to more than one primary receipt group")

    all_hold = all(entry.get("status") == "hold" for entry in entries)
    expected_manifest_status = "all_receipts_hold" if all_hold else "receipts_in_progress"
    if manifest.get("status") != expected_manifest_status:
        failures.append(
            f"manifest status {manifest.get('status')!r} should be {expected_manifest_status!r}"
        )

    print("# Advanced receipt audit\n")
    print(f"- Demonstration groups: **{len(entries)}**")
    print(f"- Advanced lessons covered: **{len(set(covered_lessons))}**")
    print(f"- Receipt JSON files present: **{len(list(RECEIPT_DIR.glob('AD*.json')))}**")
    print(f"- Findings: **{len(failures)}**")

    if failures:
        print("\n## Failures")
        for failure in failures:
            print(f"- {failure}")
        return 1

    if all_hold:
        print("\nAll nine receipts are honestly held; no app, agreement, quote, device, or legal evidence is being claimed prematurely.")
    else:
        print("\nReceipt coverage and acceptance states reconcile with the manifest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
