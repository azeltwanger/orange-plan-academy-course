#!/usr/bin/env python3
"""Update the durable unit introductions that are not generated from scripts."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "MASTER-COURSE.md"

REPLACEMENTS = {
    "*Close every Build & improve area, run the first full simulation test, test decisions separately, save the report, and establish the monthly and annual rhythm.*":
        "*Close every Build & improve area, confirm the completed current simulation result, test one decision separately, save Your Plan, and establish the monthly and annual rhythm.*",
    "**You will build:** A completed baseline, saved confidence target and retirement date, one tested scenario, yearly report, encrypted backup, and review calendar.":
        "**You will build:** A completed current baseline, understood simulation result and retirement dates, one tested scenario, yearly copy of Your Plan, encrypted backup, and review calendar.",
}


def main() -> None:
    text = MASTER.read_text(encoding="utf-8")
    missing = []
    for old, new in REPLACEMENTS.items():
        if old not in text and new not in text:
            missing.append(old)
        text = text.replace(old, new)
    if missing:
        raise RuntimeError("Missing unit-intro source text:\n- " + "\n- ".join(missing))
    MASTER.write_text(text, encoding="utf-8")
    print("updated V1 unit introductions")


if __name__ == "__main__":
    main()
