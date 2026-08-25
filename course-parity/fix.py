#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text.rstrip() + "\n", encoding="utf-8")


def add_beats(path: str, decision: str, action: str) -> None:
    text = read(path)
    if "## Your decision" not in text:
        marker = "## You are done when"
        if marker not in text:
            raise RuntimeError(f"Missing done-when marker in {path}")
        addition = f"## Your decision\n\n{decision}\n\n## Put it in Orange Plan\n\n{action}\n\n"
        text = text.replace(marker, addition + marker, 1)
    write(path, text)


def patch_lesson_text() -> None:
    add_beats(
        "lesson-text/01-1_what-to-gather-before-you-build-the-plan.md",
        "What you are gathering now, and what will wait for the module that owns it.",
        "Nothing yet. Use the Foundation walkthrough for personal details, accounts, and current holdings. Keep the other records in your folder until their module.",
    )
    add_beats(
        "lesson-text/01-2_set-your-growth-and-inflation-assumption.md",
        "Which growth model and inflation rate your baseline will use, and why.",
        "Hold the decision for the Foundation walkthrough. You will review the onboarding preset, inflation, life expectancy, and the other asset assumptions there.",
    )
    add_beats(
        "lesson-text/01-3_read-your-retirement-date-and-confidence.md",
        "Which rough onboarding input is most likely to change when the full plan is built.",
        "Open **Build Your Plan → Foundation**. Do not run the full confidence check yet.",
    )


def patch_master() -> None:
    path = "MASTER-COURSE.md"
    text = read(path)
    text = text.replace("*`TEACH` · 957 words · ~7 min*", "*`TEACH` · ~1,670 words · ~11 min*", 1)
    text = text.replace("*`TEACH` · ~1,250 words · ~8 min*", "*`TEACH` · ~1,070 words · ~7 min*", 1)
    text = text.replace("*`TEACH` · ~1,150 words · ~7 min*", "*`TEACH` · ~750 words · ~5 min*", 1)

    if "##### Who this course is built for" not in text:
        marker = "See you there.\n\nAustin"
        section = """##### Who this course is built for

This course is built on US rules. The Tax module uses US federal and state tax law. The Estate module uses US legal roles, documents, probate, and trust rules. Parts of Retirement Income also use US programs and account rules, including Social Security, Medicare, and the treatment of retirement accounts.

The rest of the planning framework travels: cash reserves, allocation, debt ratios, custody, retirement math, scenarios, and the review process.

Orange Plan models values in US dollars, and its tax engine is US federal plus state. If you live outside the US, you can still build the plan and use the same decision framework, but take the tax and estate sections to a qualified professional in your country to map the local rules.

"""
        if marker not in text:
            raise RuntimeError("Could not find Module 0 insertion point")
        text = text.replace(marker, section + marker, 1)
    write(path, text)


def patch_generator() -> None:
    path = "tools/build-dictation-order.py"
    text = read(path)
    old = "ai = re.search(r'^## (\\d+\\.\\d+) (How the AI works.+)$', master, re.M)"
    new = "ai = re.search(r'^## (\\d+\\.\\d+) (How (?:the AI works|to use Orange Plan AI).*)$', master, re.M)"
    if old not in text and new not in text:
        raise RuntimeError("Could not find AI lesson title parser")
    text = text.replace(old, new, 1)
    write(path, text)


def run(label: str, command: list[str], report: list[str]) -> None:
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    output = (proc.stdout + proc.stderr).strip()
    report += [f"### {'PASS' if proc.returncode == 0 else 'FAIL'} · {label}", "", "```text", output[-5000:] or "(no output)", "```", ""]
    if proc.returncode != 0:
        raise RuntimeError(f"{label} failed\n{output}")


def main() -> None:
    patch_lesson_text()
    patch_master()
    patch_generator()

    report = ["## Final parity and generator pass", ""]
    commands = [
        ("split modules", ["python3", "tools/split-modules.py"]),
        ("build dictation order", ["python3", "tools/build-dictation-order.py"]),
        ("check layer parity", ["python3", "tools/check-layer-parity.py"]),
        ("slop scan", ["python3", "tools/slop-scan.py", "--all"]),
        ("check crossrefs", ["python3", "tools/check-crossrefs.py"]),
        ("check metrics", ["python3", "tools/course-metrics.py", "--check"]),
    ]
    for label, command in commands:
        run(label, command, report)

    report_path = ROOT / "COURSE-LIFECYCLE-REVISION-REPORT.md"
    existing = report_path.read_text(encoding="utf-8").rstrip()
    report_path.write_text(existing + "\n\n" + "\n".join(report).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
