#!/usr/bin/env python3
"""Resolve the final direct-voice findings surfaced by paragraph-level audit."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "scripts/03-2_give-each-dollar-a-job-before-choosing-the-investment.md": [
        (
            "I think those are useful for understanding the pattern, but they are not rigid account rules. The current app makes the retirement access question more specific: Reserve is available now, Bridge is the money needed before age fifty-nine and a half, and Legacy is the money for after that point.",
            "Those ranges help explain the pattern. The current app makes the retirement access question more specific: Reserve is available now, Bridge is the money needed before age fifty-nine and a half, and Legacy is the money for after that point.",
        )
    ],
    "scripts/06-2_choose-withdrawal-order-and-refill-rule.md": [
        (
            "It is not a complete strategy if the only answer to every cash need is a new loan. The tools can be mixed across years.",
            "A sustainable strategy can mix withdrawals, sales, and borrowing across years. Using a new loan for every cash need compounds interest, lender, and repayment risk.",
        )
    ],
    "scripts/08-1_choose-who-is-in-charge-and-put-the-legal-baseline-in-place.md": [
        (
            "That authority generally ends at death, which is why it is not a replacement for the executor or trustee role. A healthcare directive covers medical decisions and wishes.",
            "A power of attorney generally ends at death. The executor or trustee role takes over then. A healthcare directive covers medical decisions and wishes.",
        )
    ],
    "scripts/advanced/A8-1_do-you-need-a-trust.md": [
        (
            "It is not an automatic upgrade because the estate owns Bitcoin. Start with the triggers.",
            "Start with the triggers that give a trust a specific job. Bitcoin ownership by itself does not establish the need.",
        )
    ],
}


def main() -> None:
    changed = 0
    for rel, pairs in REPLACEMENTS.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        for old, new in pairs:
            if old in text:
                text = text.replace(old, new)
                changed += 1
            elif new not in text:
                raise RuntimeError(f"Cannot prove direct-voice replacement in {rel}: {old}")
        path.write_text(text, encoding="utf-8")
    print(f"resolved {changed} final direct-voice findings")


if __name__ == "__main__":
    main()
