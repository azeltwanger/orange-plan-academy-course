#!/usr/bin/env python3
"""Make generated pre-dictation briefs easier to speak from.

The research script can keep exact app paths. The working dictation surface gets
one natural handoff sentence and hides the path as an editor reference.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFTS = ROOT / "dictation-drafts"

CORE_HANDOFFS = {
    "1.3": "Then use the Foundation walkthrough to add your real accounts and current holdings and review the assumptions behind the estimate. We are not entering every other part of the plan or running the full confidence check yet.",
    "2.1": "For now, write down your normal spending, bare-bones spending, and true monthly surplus. In the walkthrough for this module, I'll show you exactly where to enter them and how to check them against your real transactions.",
    "2.3": "Once you have the reserve and future-cost decisions written down, the module walkthrough will show you how to enter the cash-flow numbers, reserve settings, and expected life events in Orange Plan. If the optional college lesson applies to you, take that lesson before the walkthrough.",
    "2.4": "For now, write down what you are actually committing to provide and the part you want protected from a forced Bitcoin sale. In the module walkthrough, I'll show you where the life event and protected funding amount belong.",
    "3.1": "For now, write down the job and ceiling you chose for each debt. In the walkthrough for this module, I'll show you exactly where to enter the debts and record the strategy in Orange Plan.",
    "4.1": "For now, write down the Bitcoin allocation you think you can actually hold through a full drawdown. In the module walkthrough, I'll show you where to save it and how to test it against the rest of the plan.",
    "4.2": "For now, write down which accounts belong to Reserve, Bridge, and Legacy. In the module walkthrough, I'll show you where to assign those timeframes and check whether each one is funded.",
    "4.4": "Once the allocation, timeframes, next-dollar rule, and asset-location decisions are written down, use the module walkthrough to put the full routing plan into Orange Plan.",
    "5.1": "For now, gather the records and label each material lot as verified, estimated for planning, or still unproven. In the tax walkthrough, I'll show you how to bring that history into Orange Plan and review the result.",
    "5.2": "For now, write down the job of each tax bucket and the years that may create a planning window. In the tax walkthrough, I'll show you how to model a sale and a conversion without applying either one by accident.",
    "6.1": "For now, write down your retirement spending, reliable income, annual gap, and the years your Bridge has to cover. In the module walkthrough, I'll show you where each number goes.",
    "6.2": "For now, write down the withdrawal order and refill rule you want to test. In the module walkthrough, I'll show you how to preview the strategy before you apply it to the plan.",
    "6.3": "Once the spending guardrail decision is written down, use the module walkthrough to build the full retirement paycheck and compare the preview with the current plan.",
    "7.1": "For now, write down the custody level that fits the amount, your skill, and your family. The custody demo and walkthrough will show the exact setup, recovery test, and no-secrets map.",
    "7.2": "For now, write down the recovery test your setup has to pass. The custody demo will show the exact device process; do not improvise from a generic click path in a teaching video.",
    "7.3": "Once the single points of failure are written down, use the custody demo and walkthrough to harden the accounts and complete the custody map.",
    "8.1": "For now, write down who holds each legal role and which documents are missing. In the estate walkthrough, I'll show you where Orange Plan records completion without storing the legal documents or secrets.",
    "8.2": "For now, write down whether the setup passes the dual-control and redundancy tests. In the estate walkthrough, I'll show you where to record the level and recovery status without putting secret material in the app.",
    "8.3": "For now, draft the first two lines your family needs and decide who receives the message. In the estate walkthrough, I'll show you how to build and test the heir-letter process without putting secrets in it.",
    "8.4": "Once the coverage gaps and protection decisions are written down, use the estate walkthrough to finish the Protect checklist and identify what still needs an outside professional.",
    "9.1": "For now, write down the monthly and annual review rhythm you will actually follow. In the final walkthrough, I'll show you how to run the completed plan and save the first review.",
    "9.2": "Use the final walkthrough to run the 1,000-path confidence check, set the target, test one real decision, and save the finished report.",
}


def lesson_number(text: str, path: Path) -> str:
    match = re.search(r"(?m)^# (A?\d+\.\d+)\s+·", text)
    if match:
        return match.group(1)
    raise RuntimeError(f"Could not identify lesson number in {path}")


def handoff_for(number: str) -> str | None:
    if number == "0.2":
        return None
    if number.startswith("A"):
        return "For now, write down the decision or comparison you want to carry back to the plan. Use the owning core page or a Scenario after the lesson; the exact app path stays in the reference below rather than being read twice."
    return CORE_HANDOFFS.get(
        number,
        "For now, write down the decision you just made. In the walkthrough for this module, I'll show you exactly where to enter it in Orange Plan and how the app uses it.",
    )


def refine(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    number = lesson_number(text, path)

    text = text.replace("## Suggested opening", "## Opening you can start from")
    text = text.replace("## Teach it in this order", "## Talking points in order")
    text = text.replace("## Close without manufacturing a payoff line", "## Finish the lesson")
    text = text.replace("**Decision the learner needs to make:**", "**Decision to land:**")
    text = text.replace("**What should be true before they move on:**", "**Finish line:**")

    handoff = handoff_for(number)
    marker = "**App or walkthrough handoff — do not read a click path twice:**"
    if marker in text:
        pattern = re.compile(
            rf"(?ms)^{re.escape(marker)}\n(.*?)(?=^\*\*Finish line:\*\*|^\*\*Sequence note|^## Reference only)"
        )
        match = pattern.search(text)
        if not match:
            raise RuntimeError(f"Could not isolate app handoff in {path}")
        original = match.group(1).strip()
        replacement_lines = []
        if handoff:
            replacement_lines += ["**Suggested spoken handoff:**", "", f"> {handoff}", ""]
        replacement_lines += [
            "<details>",
            "<summary>App path for the walkthrough/editor — do not read this aloud</summary>",
            "",
            original or "The exact path remains in the canonical research script.",
            "",
            "</details>",
            "",
        ]
        text = text[: match.start()] + "\n".join(replacement_lines) + text[match.end() :]
    elif handoff and number != "0.2":
        reference_marker = "## Reference only — do not dictate this section"
        if reference_marker not in text:
            raise RuntimeError(f"Reference marker missing in {path}")
        addition = f"**Suggested spoken handoff:**\n\n> {handoff}\n\n"
        text = text.replace(reference_marker, addition + reference_marker, 1)

    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    if not DRAFTS.exists():
        raise RuntimeError("dictation-drafts/ does not exist; run build-dictation-prep.py first")
    count = 0
    for path in sorted(DRAFTS.rglob("*.md")):
        refine(path)
        count += 1
    print(f"refined {count} pre-dictation drafts")


if __name__ == "__main__":
    main()
