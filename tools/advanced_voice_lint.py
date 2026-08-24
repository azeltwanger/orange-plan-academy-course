#!/usr/bin/env python3
"""Run the Academy voice guardrail across the current Advanced Library."""

from __future__ import annotations

import sys
from pathlib import Path

from voice_lint import audit

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts" / "advanced" / "current"
EXPECTED = 18


def main() -> int:
    paths = sorted(SCRIPTS.glob("*.md"))
    results = [audit(path, ROOT) for path in paths]
    forbidden_count = sum(len(result.forbidden) for result in results)
    warning_count = sum(len(result.warnings) for result in results)

    print("# Advanced voice and AI-slop lint\n")
    print(f"- Advanced scripts checked: **{len(results)}**")
    print(f"- Forbidden phrase findings: **{forbidden_count}**")
    print(f"- Readability warnings for Austin review: **{warning_count}**\n")
    print("| Script | Words | Avg sentence | Forbidden | Review warnings |")
    print("|---|---:|---:|---|---|")
    for result in results:
        forbidden = "; ".join(result.forbidden) if result.forbidden else "—"
        warnings = "; ".join(result.warnings) if result.warnings else "—"
        print(
            f"| `{result.path}` | {result.words:,} | {result.average_sentence_words:.1f} | "
            f"{forbidden} | {warnings} |"
        )

    print("\nWarnings are review prompts, not automatic failures. Austin's final spoken read remains the authority.")

    if len(results) != EXPECTED:
        print(f"Expected {EXPECTED} current Advanced scripts but found {len(results)}.", file=sys.stderr)
        return 1
    return 1 if forbidden_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
