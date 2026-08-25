#!/usr/bin/env python3
"""List every unresolved decision embedded in the canonical demo fixture."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "demo" / "demo-v1-inputs.json"


def walk(value: Any, path: str = "$"):
    if isinstance(value, dict):
        yield path, value
        for key, child in value.items():
            yield from walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


def display_value(value: Any) -> str:
    if value is None:
        return "—"
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def main() -> int:
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    decisions: list[tuple[str, dict[str, Any]]] = []

    for path, value in walk(fixture):
        status = value.get("status") if isinstance(value, dict) else None
        if isinstance(status, str) and "decision_hold" in status:
            decisions.append((path, value))

    print("# Canonical demo decisions still requiring Austin approval\n")
    print(f"- Fixture: **{fixture.get('fixtureVersion')}**")
    print(f"- Decision holds found: **{len(decisions)}**\n")

    if not decisions:
        print("No decision holds remain. The fixture is ready for the canonical app run.")
        return 0

    print("| # | Fixture path | Proposed value | Alternatives / note |")
    print("|---:|---|---|---|")
    for index, (path, value) in enumerate(decisions, start=1):
        proposed = value.get("value")
        alternatives = value.get("alternatives")
        note = value.get("note")
        context = alternatives if alternatives is not None else note
        print(
            f"| {index} | `{path}` | {display_value(proposed)} | {display_value(context)} |"
        )

    print("\nUse `AUSTIN-DEMO-DECISIONS.md` to approve or change the planning choices. After the fixture is updated, rerun this command. Austin does not need to re-dictate a lesson to resolve these fields.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
