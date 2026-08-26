#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "AUSTIN-DICTATION-VOICE-AUDIT.md"

# The new source reinforces the existing VOICE-GUIDE: Austin explains in plain
# language, restates when it helps, marks opinions as opinions, uses concrete
# examples, and avoids compressed payoff lines. This scanner is deliberately
# over-inclusive; the report is for editorial judgment, not automatic rewriting.
PHRASES: list[tuple[str, re.Pattern[str], int]] = [
    ("clever reversal", re.compile(r"\b(?:it|this|that|the [a-z -]+) (?:isn't|is not|doesn't|does not) [^.!?]{2,80}, (?:it'?s|it is|that's|that is|they're|they are)\b", re.I), 5),
    ("importance announcement", re.compile(r"\b(?:the important part|what matters|the key thing|the whole point|the real point|the point is|the goal is|the one hard rule|the most important thing)\b", re.I), 3),
    ("compressed verdict", re.compile(r"\b(?:same [^,.]{2,35}, same [^,.]{2,35}, different|[a-z -]+ beats [a-z -]+|[a-z -]+ wins over [a-z -]+)\b", re.I), 4),
    ("essay opener", re.compile(r"^(?:Consider|Imagine|Picture|Take someone|Take a couple|For context|At its core|Fundamentally|Ultimately|In practice)\b", re.I), 3),
    ("formal transition", re.compile(r"\b(?:however|therefore|moreover|nevertheless|consequently|accordingly|in contrast|by contrast)\b", re.I), 2),
    ("abstract frame", re.compile(r"\b(?:the framework|the architecture|the mechanism|the implication|the distinction|the objective|the principle|the trade-off|the constraint|the decision surface|the planning result)\b", re.I), 2),
    ("over-compressed disclaimer", re.compile(r"\b(?:modeled, not advice|illustrative, not predictive|education, not advice|general, not personalized)\b", re.I), 2),
    ("stiff imperative", re.compile(r"^(?:Determine|Establish|Identify|Evaluate|Assess|Document|Confirm|Review)\b", re.I), 1),
    ("punchline marker", re.compile(r"\b(?:That's the job|That's the rule|That's the test|That's the win|That's the risk control|That's the whole point|That is the job|That is the rule)\b", re.I), 3),
]

SAFE_EM_DASH_CONTEXT = re.compile(r"(?:TELEPROMPTER SCRIPT|— segment|\d+–\d+|[A-Z]+—[A-Z]+)")
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'])")
CHAIN = {"so", "and", "but", "now", "then"}
ARTICLE = {"a", "an", "the", "this", "that", "these", "those"}


def spoken_body(text: str) -> str:
    return text.split("=" * 60, 1)[-1]


def script_files() -> list[Path]:
    files = sorted((ROOT / "scripts").glob("*.md")) + sorted((ROOT / "scripts" / "advanced").glob("*.md"))
    return [
        p for p in files
        if "WALKTHROUGH" not in p.name
        and "DEMO" not in p.name
        and p.name not in {"README.md", "VOICE-GUIDE.md"}
    ]


def sentences(body: str) -> list[str]:
    clean_lines = []
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith("==") or line.startswith("#") or line.startswith("-") or line.startswith("<!--"):
            continue
        clean_lines.append(line)
    return [s.strip() for s in SENTENCE_SPLIT.split(" ".join(clean_lines)) if s.strip()]


def candidate_lines(path: Path, text: str) -> list[tuple[int, int, str, str]]:
    results: list[tuple[int, int, str, str]] = []
    in_body = "=" * 60 not in text
    for lineno, raw in enumerate(text.splitlines(), 1):
        if raw.startswith("=" * 60):
            in_body = True
            continue
        if not in_body:
            continue
        line = raw.strip()
        if not line or line.startswith(("==", "#", "<!--", "*", ">")):
            continue
        if line.startswith("-") and not re.match(r"-?\$?\d", line):
            continue
        score = 0
        reasons: list[str] = []
        for name, rx, weight in PHRASES:
            if rx.search(line):
                score += weight
                reasons.append(name)
        if "—" in line and not SAFE_EM_DASH_CONTEXT.search(line):
            score += 1
            reasons.append("em dash")
        words = re.findall(r"\b[\w'$%.-]+\b", line)
        if 2 <= len(words) <= 6 and re.search(r"[.!?]$", line) and not re.match(r"^(One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten):", line):
            score += 2
            reasons.append("short payoff/fragment")
        if score:
            results.append((score, lineno, ", ".join(sorted(set(reasons))), line))
    return sorted(results, key=lambda x: (-x[0], x[1]))


def metrics(body: str) -> dict[str, float]:
    sents = sentences(body)
    words = re.findall(r"\b[\w'$%.-]+\b", body)
    starts = Counter()
    for sent in sents:
        first = re.findall(r"\b[A-Za-z']+\b", sent)
        if first:
            starts[first[0].lower()] += 1
    word_count = max(len(words), 1)
    return {
        "words": len(words),
        "sentences": len(sents),
        "avg": len(words) / max(len(sents), 1),
        "chain": 100 * sum(starts[w] for w in CHAIN) / max(len(sents), 1),
        "article": 100 * sum(starts[w] for w in ARTICLE) / max(len(sents), 1),
        "i_think": 1000 * len(re.findall(r"\bI (?:think|don't think|would|like|personally)\b", body, re.I)) / word_count,
        "because": 1000 * len(re.findall(r"\bbecause\b", body, re.I)) / word_count,
        "questions": 1000 * body.count("?") / word_count,
    }


def main() -> None:
    rows = []
    all_candidates: dict[Path, list[tuple[int, int, str, str]]] = {}
    for path in script_files():
        text = path.read_text(encoding="utf-8")
        body = spoken_body(text)
        cands = candidate_lines(path, text)
        all_candidates[path] = cands
        m = metrics(body)
        score = sum(item[0] for item in cands)
        rows.append((score, path, m, len(cands)))

    rows.sort(key=lambda x: (-x[0], x[1].name))
    lines = [
        "# Austin dictation voice audit",
        "",
        "**Generated:** 2026-08-26",
        "",
        "## What the new dictation adds",
        "",
        "The source is explanatory rather than polished. Austin usually names the plain-language meaning, explains why it changes the plan, walks through a concrete example, and then repeats the practical decision in slightly different words. Opinions are marked with `I think`, `I would`, or `personally`. The useful repetition stays. Transcription errors, false starts, duplicated clicks, and incorrect math do not.",
        "",
        "This audit ranks likely written-prose lines. A high score means **review**, not automatically replace. Tax rules, legal qualifications, custody warnings, and required app labels can legitimately sound more formal.",
        "",
        "## Script ranking",
        "",
        "| Score | Script | Words | Avg sentence | Chain openers | Article openers | Judgment markers / 1k | Because / 1k | Candidates |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for score, path, m, count in rows:
        rel = path.relative_to(ROOT)
        lines.append(
            f"| {score} | `{rel}` | {m['words']:.0f} | {m['avg']:.1f} | {m['chain']:.0f}% | {m['article']:.0f}% | {m['i_think']:.1f} | {m['because']:.1f} | {count} |"
        )

    lines += ["", "## Candidate lines", ""]
    for score, path, m, count in rows:
        cands = all_candidates[path]
        if not cands:
            continue
        lines += [f"### `{path.relative_to(ROOT)}` · score {score}", ""]
        for item_score, lineno, reasons, line in cands:
            lines.append(f"- **{item_score}** · L{lineno} · {reasons}: `{line}`")
        lines.append("")

    lines += [
        "## Editorial rule for the pass",
        "",
        "Do not inject `So` and `I think` mechanically. Rewrite the idea as Austin would teach it: plain meaning, cause, example, practical decision. Keep the full explanation when it earns clarity. Remove only the sentence whose job is to sound finished or quotable.",
    ]
    OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
