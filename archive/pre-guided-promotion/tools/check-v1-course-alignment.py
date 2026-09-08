#!/usr/bin/env python3
"""Verify active course layers against the Orange Plan V1 product contract."""
from __future__ import annotations

import glob
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def active_files() -> list[Path]:
    files = [
        ROOT / "MASTER-COURSE.md",
        ROOT / "MASTER-ADVANCED.md",
        ROOT / "MODULE-CHECKPOINTS.md",
        ROOT / "SCREEN-SHOOT-LIST.md",
        ROOT / "DICTATION-ORDER.md",
        ROOT / "FILM-ORDER.md",
        ROOT / "CIRCLE-STRUCTURE.md",
        ROOT / "PRODUCTION-CHECKLIST.md",
        ROOT / "FINALIZATION-STATUS.md",
    ]
    for pattern in (
        "scripts/*.md",
        "scripts/advanced/*.md",
        "lesson-text/*.md",
        "lesson-text/advanced/*.md",
        "modules/*.md",
        "modules/advanced/*.md",
        "visuals/*.md",
    ):
        files.extend(Path(p) for p in glob.glob(str(ROOT / pattern)))
    excluded = {"README.md", "VOICE-GUIDE.md", "00-STYLE.md"}
    return sorted({p for p in files if p.exists() and p.name not in excluded})


FORBIDDEN = {
    "normal-user confidence target": re.compile(
        r"(?:choose|set|select|save|saved|saving|point out|adjust).{0,60}confidence target|"
        r"confidence target choices|target confidence",
        re.I,
    ),
    "first useful result waits until Module 9": re.compile(
        r"first (?:saved )?full.{0,60}confidence|first full 1,000-path confidence|"
        r"first full confidence run",
        re.I,
    ),
    "retired Build Your Plan name": re.compile(r"\bBuild Your Plan\b"),
    "retired Strategy route": re.compile(r"\bStrategy\s*→"),
    "retired report route": re.compile(
        r"Account menu\s*→\s*Report|Open Report|Report\s*→\s*Print|"
        r"yearly report PDF|final report assembles",
        re.I,
    ),
    "retired apply/run language": re.compile(
        r"\bApply to plan\b|\bapply to plan\b|\bRun confidence\b|\brun confidence\b"
    ),
    "retired AI framing": re.compile(r"\bPlan Guide\b|orange AI Review button", re.I),
    "percentage-first object name": re.compile(r"\bconfidence ring\b|\bconfidence number\b", re.I),
    "user example reversal": re.compile(
        r"The four paths on the screen are not recommendations", re.I
    ),
}


def section(text: str, num: str) -> str:
    match = re.search(rf"^## {re.escape(num)} .+$", text, re.M)
    if not match:
        return ""
    nxt = re.search(r"\n#{1,2} (?:A?\d+\.\d+|Unit |Advanced Module )", text[match.end():])
    end = match.end() + (nxt.start() + 1 if nxt else len(text) - match.end())
    return text[match.start():end]


def require(path: str, patterns: list[tuple[str, str]]) -> list[str]:
    text = (ROOT / path).read_text(encoding="utf-8")
    failures = []
    for label, pattern in patterns:
        if not re.search(pattern, text, re.I | re.S):
            failures.append(f"{path}: missing {label} / `{pattern}`")
    return failures


def main() -> None:
    failures: list[str] = []
    scanned = active_files()

    for path in scanned:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        for label, rx in FORBIDDEN.items():
            for match in rx.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                snippet = re.sub(r"\s+", " ", text[match.start():match.end() + 80]).strip()
                failures.append(f"{rel}:{line}: {label}: {snippet[:180]}")

    failures += require(
        "scripts/00-2_how-to-use-orange-plan-ai.md",
        [
            ("Ask in the header", r"Ask is available from the header"),
            ("Current versus Preview", r"Current versus Preview"),
            ("Needs Attention", r"Needs Attention"),
            ("Daily Bitcoin Market Report", r"Daily Bitcoin Market Report"),
            ("outside AI export", r"AI Strategy Review Export"),
        ],
    )
    failures += require(
        "scripts/01-3_what-the-onboarding-retirement-age-actually-means.md",
        [
            ("deterministic onboarding", r"deterministic estimate"),
            ("fixed standard", r"800 of 1,000"),
            ("simulation count", r"790 of 1,000"),
            ("four freshness states", r"Preliminary.{0,300}Current.{0,300}Stale.{0,300}Unavailable"),
            ("planned date", r"planned retirement date"),
            ("earliest modeled date", r"earliest modeled retirement date"),
        ],
    )
    failures += require(
        "scripts/03-1_set-the-bitcoin-allocation-you-can-actually-hold.md",
        [("direct four-path sentence", r"The four paths describe where you are today")],
    )
    failures += require(
        "scripts/06-3_use-plan-confidence-and-guardrails-to-adjust-spending.md",
        [
            ("fixed standard", r"800 of 1,000"),
            ("lower guardrail", r"lower guardrail"),
            ("current portfolio", r"current retirement-portfolio value"),
            ("upper guardrail", r"upper guardrail"),
            ("10 percent cap", r"capped at 10%"),
        ],
    )
    failures += require(
        "scripts/09-1_keep-the-plan-current-without-rebuilding-it.md",
        [
            ("Home review", r"Home answers"),
            ("Cash Flow review", r"Cash Flow answers"),
            ("Plan review", r"Plan answers"),
            ("Protect review", r"Protect answers"),
            ("account continuity distinction", r"Balance and holdings, recorded activity, and tax details"),
        ],
    )
    failures += require(
        "scripts/09-2_test-decisions-and-read-the-finished-plan.md",
        [
            ("Current versus Preview", r"Current versus Preview"),
            ("Your Plan", r"Your Plan"),
            ("800 standard", r"800-of-1,000|800 of 1,000"),
            ("planned and earliest dates", r"planned retirement date.{0,220}earliest modeled date"),
        ],
    )
    failures += require(
        "scripts/01-4_WALKTHROUGH_foundation.md",
        [
            ("Needs Attention", r"Needs Attention"),
            ("separate continuity dimensions", r"what the account owns now.{0,220}which activity has been recorded.{0,220}tax history"),
            ("transfer preservation", r"internal transfer preserves total quantity"),
            ("fixed standard", r"800 of 1,000"),
        ],
    )
    failures += require(
        "scripts/09-3_WALKTHROUGH_finish-test-review-and-save.md",
        [
            ("normal standard boundary", r"Normal users do not choose another standard"),
            ("four destination walk", r"\*\*HOME\*\*.{0,600}\*\*CASH FLOW\*\*.{0,600}\*\*PLAN\*\*.{0,600}\*\*PROTECT\*\*"),
            ("Your Plan route", r"View full plan|Your plan"),
        ],
    )

    # Core guardrail lesson and visual must no longer surface the old probability
    # stops as the customer-facing object.
    for rel in (
        "scripts/06-3_use-plan-confidence-and-guardrails-to-adjust-spending.md",
        "lesson-text/06-3_use-plan-confidence-and-guardrails-to-adjust-spending.md",
        "visuals/6-3_guardrails.md",
    ):
        path = ROOT / rel
        if path.exists() and re.search(r"60.{0,30}80.{0,30}95", path.read_text(encoding="utf-8"), re.I | re.S):
            failures.append(f"{rel}: old 60/80/95 customer-facing guardrail sequence remains")

    if failures:
        print("V1 COURSE ALIGNMENT FAILURES")
        for failure in failures:
            print(" -", failure)
        print(f"\n{len(failures)} failures across {len(scanned)} active files")
        raise SystemExit(1)

    print(f"V1 course alignment passed across {len(scanned)} active files")


if __name__ == "__main__":
    main()
