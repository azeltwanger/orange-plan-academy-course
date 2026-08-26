#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHANGED_SCRIPTS: set[str] = set()
CHANGE_LOG: list[tuple[str, str, str]] = []


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_exact(path: str, old: str, new: str, label: str, *, required: bool = True) -> bool:
    text = read(path)
    count = text.count(old)
    if count == 0:
        if required:
            raise RuntimeError(f"{label}: source text not found in {path}: {old[:140]!r}")
        return False
    if count > 1:
        raise RuntimeError(f"{label}: expected one match in {path}, found {count}")
    write(path, text.replace(old, new, 1))
    if path.startswith("scripts/") and "WALKTHROUGH" not in path and "DEMO" not in path:
        CHANGED_SCRIPTS.add(path)
    CHANGE_LOG.append((path, label, new))
    return True


def replace_in_script_and_master(script: str, master: str, old: str, new: str, label: str) -> None:
    replace_exact(script, old, new, label + " · script")
    replace_exact(master, old, new, label + " · master", required=False)


def replace_regex(path: str, pattern: str, new: str, label: str, *, flags: int = 0) -> None:
    text = read(path)
    updated, count = re.subn(pattern, new, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one regex match in {path}, found {count}")
    write(path, updated)
    CHANGE_LOG.append((path, label, new))


# ---------------------------------------------------------------------------
# Preserve the new Austin authority before editing anything downstream.
# ---------------------------------------------------------------------------

write(
    "source-material/2026-08-26-f20-and-voice-pass.md",
    """# Austin source material — five-year funding rule and voice pass

**Received:** 2026-08-26  
**Source:** Austin's direct instructions in the course-revision conversation  
**Policy:** Preserve the exact statements below. Course wording may remove transcription errors or explain the implementation, but it may not replace the planning judgment.

## Exact statements

> yes Bitcoin can remain part of funding 5 years out

> use my dictation to run thorugh a pass on the material to try to make it sound more like me..

## Narrow implementation boundary

The first statement resolves F20 this far, and no farther:

- At roughly five years out, Bitcoin may remain one source in the funding plan.
- The course does not invent a fixed Bitcoin percentage.
- The amount the household has firmly committed to and cannot afford to miss becomes less dependent on Bitcoin as the date approaches.
- The existing one-to-two-year rule remains: the committed amount needed that soon should not depend on Bitcoin cooperating.
- Bitcoin can remain in the Legacy funding source while the protected amount builds in Bridge. This ruling does not require relabeling Bitcoin itself as a Bridge asset.

The second statement authorizes a voice pass. It does not authorize changing course structure, Austin's planning positions, verified math, legal qualifications, or app mechanics.
""",
)

# ---------------------------------------------------------------------------
# Voice guide: use the new source as a calibration master, not a bag of filler.
# ---------------------------------------------------------------------------

voice_marker = "## Dictation-derived rules (diffed against the same content written by AI)\n"
voice_addition = """## Additional calibration from the 2026-08-25 dictation

Source: `source-material/2026-08-25-module-0-1-dictation.md`, reinforced by
`source-material/2026-08-26-f20-and-voice-pass.md`.

The newer dictation adds a five-part pattern that outranks polished prose:

1. **Say what the thing means in plain language.** Austin explains cost basis as
   the purchase history and price paid before using the tax term.
2. **Explain why it changes the plan.** He connects the input to taxes,
   retirement date, spending, or the decision downstream instead of announcing
   that it is important.
3. **Tell the viewer where the real information comes from.** Log in, check the
   current rate, download the CSV, pull the pay stub, or open the employer plan.
4. **Use a concrete example and then restate the decision.** Useful repetition
   stays when the second version makes the action clearer.
5. **Preserve optionality.** "If you'd rather gather it as you go, that's totally
   fine" is Austin's voice. Do not turn a preferred workflow into a universal
   command.

Do not imitate transcription errors, false starts, repeated navigation, or math
errors. The teach lesson explains the decision. The walkthrough performs the
clicks. When the source itself asks whether a click path is duplicated, remove
it from the teach lesson rather than reading the same instructions twice.

"""
voice = read("scripts/VOICE-GUIDE.md")
if voice_addition.strip() not in voice:
    if voice_marker not in voice:
        raise RuntimeError("VOICE-GUIDE insertion marker missing")
    voice = voice.replace(voice_marker, voice_addition + voice_marker, 1)
    write("scripts/VOICE-GUIDE.md", voice)

# ---------------------------------------------------------------------------
# Voice edits. These are deliberately exact and local. Real Austin dictation,
# factual qualifications, numbered teaching, and walkthrough mechanics stay.
# ---------------------------------------------------------------------------

CORE = "MASTER-COURSE.md"
ADV = "MASTER-ADVANCED.md"

replace_in_script_and_master(
    "scripts/00-2_how-the-ai-works-what-it-reads-what-it-n.md", CORE,
    "The useful question is not everything the AI cannot do. It's how it can help you understand and improve the financial plan you're building.",
    "I want to focus this lesson on how the AI can help you understand and improve the financial plan you're building.",
    "0.2 benefit-first opening",
)
replace_in_script_and_master(
    "scripts/00-2_how-the-ai-works-what-it-reads-what-it-n.md", CORE,
    "The goal is to replace doomscrolling with one clean read that takes less than two minutes. It checks the parts of the Bitcoin market that are actually worth following.",
    "I use this so I can get one clean read of the market without checking five different places. It should take less than two minutes and cover the parts of the Bitcoin market that are actually useful for the plan.",
    "0.2 daily report",
)
replace_in_script_and_master(
    "scripts/00-2_how-the-ai-works-what-it-reads-what-it-n.md", CORE,
    "The goal isn't to have the AI make every decision for you. The goal is to understand what the plan is showing, what is missing, and which trade-off you're accepting before you act.",
    "I would not use the AI to make every decision for you. I would use it to understand what the plan is showing, find information that is missing, and think through the trade-off before you make the decision yourself.",
    "0.2 decision role",
)

replace_in_script_and_master(
    "scripts/01-2_set-your-growth-and-inflation-assumption.md", CORE,
    "This is why it's important to think through what you personally feel is a conservative and realistic way to model Bitcoin in the future. The goal isn't to choose the model that gives you the earliest date. The goal is to choose the model you can defend.",
    "This is why I think you need to choose a conservative and realistic way to model Bitcoin in the future. I would not choose the model just because it gives you the earliest retirement date. I would choose the one you could defend if you were explaining it to a family member or a friend.",
    "1.2 assumption judgment",
)

replace_in_script_and_master(
    "scripts/02-4_optional-college-is-a-funding-stack.md", CORE,
    "Not every family uses all six. The point is that college does not have to be solved entirely with money you saved before freshman year. A complete plan might be: the parents provide the existing 529, add a fixed amount from annual cash flow, the student applies for aid and works summers and takes a defined amount of federal loans, and Bitcoin covers part of the rest if the price and the tax situation work out.",
    "Not every family is going to use all six. A family might use the existing 529, add a fixed amount from annual cash flow, have the student apply for aid and work summers, set a limit on federal loans, and use Bitcoin for part of the remaining cost if the price and tax situation make sense. So college does not have to be solved entirely with money you saved before freshman year.",
    "2.4 funding stack example",
)
replace_in_script_and_master(
    "scripts/02-4_optional-college-is-a-funding-stack.md", CORE,
    "The goal is not to stop buying Bitcoin for seven years because your child may go to college.",
    "I would not automatically stop buying Bitcoin for seven years because your child may go to college.",
    "2.4 accumulation judgment",
)
replace_in_script_and_master(
    "scripts/02-4_optional-college-is-a-funding-stack.md", CORE,
    "The goal is to make sure the amount you have firmly promised does not depend entirely on Bitcoin being at a favorable price on the exact day tuition is due.",
    "What I would do is protect the amount you have firmly promised so that portion does not depend entirely on Bitcoin being at a favorable price when tuition is due.",
    "2.4 protected commitment",
)

replace_in_script_and_master(
    "scripts/05-1_cost-basis-what-you-paid-and-how-to-reco.md", CORE,
    "Same sale proceeds. Different identified units. Different gain.",
    "The sale proceeds are the same, but the gain changes because the Bitcoin came from a different lot.",
    "5.1 remove payoff triad",
)
replace_in_script_and_master(
    "scripts/05-1_cost-basis-what-you-paid-and-how-to-reco.md", CORE,
    "Start with contemporaneous records.",
    "Start with the records that were created when the transactions happened.",
    "5.1 plain record language",
)
replace_in_script_and_master(
    "scripts/05-1_cost-basis-what-you-paid-and-how-to-reco.md", CORE,
    "The honest plan labels what is known, what is estimated, and what is still unproven.",
    "So in the plan, label what is known, what is estimated, and what is still unproven.",
    "5.1 direct instruction",
)

replace_in_script_and_master(
    "scripts/05-2_taxable-tax-deferred-and-roth-bracket-wi.md", CORE,
    "That is too simple.",
    "I think that leaves out too many of the other costs that can change at the same time.",
    "5.2 bracket qualification",
)

replace_in_script_and_master(
    "scripts/07-1_choose-the-custody-setup-that-matches-you.md", CORE,
    "The answer is not the most impressive setup. It is the one you can prove.",
    "I would choose the simplest setup you can actually prove works.",
    "7.1 setup choice",
)
replace_in_script_and_master(
    "scripts/07-1_choose-the-custody-setup-that-matches-you.md", CORE,
    "This is simple enough for many households to maintain well. The trade-off is concentration: one sufficient backup can authorize the wallet, and one missing required element can block recovery.",
    "I think this is simple enough for a lot of households to maintain well. The risk is that one complete backup can authorize the wallet, and one missing required piece can also block recovery.",
    "7.1 single-signature risk",
)
replace_in_script_and_master(
    "scripts/07-1_choose-the-custody-setup-that-matches-you.md", CORE,
    "The level matches today's amount and family, the trade-off is stated honestly, and the exact setup has a recovery test appropriate to it—not merely a belief that it works.",
    "The level fits the amount and your family, you can explain the risk you accepted, and you have actually tested the recovery process instead of assuming it works.",
    "7.1 completion",
)

replace_in_script_and_master(
    "scripts/07-2_set-up-a-hardware-wallet-and-test-recove.md", CORE,
    "Use this order.",
    "I would test it in this order.",
    "7.2 recovery sequence",
)
replace_in_script_and_master(
    "scripts/07-2_set-up-a-hardware-wallet-and-test-recove.md", CORE,
    "Record no secrets in the app.",
    "Do not record any seed words, passphrases, PINs, private keys, or backup contents in the app.",
    "7.2 no-secrets instruction",
)

replace_in_script_and_master(
    "scripts/07-3_single-points-of-failure-account-hardeni.md", CORE,
    "The response is always the same.",
    "When you get one of these messages, stop before you do anything.",
    "7.3 scam response",
)
replace_in_script_and_master(
    "scripts/07-3_single-points-of-failure-account-hardeni.md", CORE,
    "Privacy is part of custody.",
    "Who knows the amount, location, or exact setup is also part of your custody risk.",
    "7.3 privacy risk",
)

replace_in_script_and_master(
    "scripts/08-2_split-access-dual-control-and-redundancy.md", CORE,
    "Those are different failures.\n\nDual control answers the first. Redundancy answers the second.",
    "These are two different questions. Dual control tells you whether one person can spend alone. Redundancy tells you whether one loss can stop recovery.",
    "8.2 two tests",
)
replace_in_script_and_master(
    "scripts/08-2_split-access-dual-control-and-redundancy.md", CORE,
    "Protect records the level, recovery-test status, and process completion.\n\nThe secret distribution stays off-app.",
    "Protect records the level, recovery-test status, and process completion. Keep the seed, passphrase, key distribution, and exact storage locations out of the app.",
    "8.2 off-app details",
)

replace_in_script_and_master(
    "scripts/08-3_the-heir-letter-and-the-dead-mans-switch.md", CORE,
    "Three documents, three jobs.\n\n",
    "",
    "8.3 remove slogan",
)

replace_in_script_and_master(
    "scripts/09-2_test-a-decision-and-read-the-finished-plan.md", CORE,
    "You're also not the only reader. It's the agenda for a twenty-minute sit-down with your spouse, the tax pages plus the transaction export go to your CPA, and the access and estate pages go to your attorney. What matters in all three is that you're handing a professional a document rather than asking them to log into an app, and that's what lets three different people start from the same set of facts.",
    "This report is also something you can hand to other people. Use it as the agenda for a twenty-minute conversation with your spouse. Give the tax pages and transaction export to your CPA. Give the access and estate pages to your attorney. That way all three people can start from the same facts without needing to log into your app.",
    "9.2 report handoff",
)

replace_in_script_and_master(
    "scripts/advanced/A3-1_borrow-against-bitcoin-without-getting-l.md", ADV,
    "That's the whole product.",
    "So the basic transaction is pretty simple.",
    "A3.1 plain loan setup",
)

replace_in_script_and_master(
    "scripts/advanced/A5-1_rmd-risk-and-roth-conversions.md", ADV,
    "That is only the first pass.",
    "I think that leaves out too many of the other costs that can change with the conversion.",
    "A5.1 conversion cost",
)

replace_in_script_and_master(
    "scripts/advanced/A5-3_state-taxes-and-relocation.md", ADV,
    "The course used to imply that the state where you live in the year of sale is the whole answer.\n\nIt is not.",
    "The course used to imply that the state where you live in the year of sale is the whole answer. That leaves out a lot of the actual residency rules.",
    "A5.3 residency explanation",
)
replace_in_script_and_master(
    "scripts/advanced/A5-3_state-taxes-and-relocation.md", ADV,
    "State income tax is one line.\n\nAlso price:",
    "Then I would price the rest of the move too:",
    "A5.3 whole move",
)

replace_in_script_and_master(
    "scripts/advanced/A6-2_sell-borrow-or-hold-funding-a-year-of-sp.md", ADV,
    "The tax comparison therefore cannot stop at \"loan proceeds are not taxable.\"",
    "So I would not stop the tax comparison at \"loan proceeds are not taxable.\"",
    "A6.2 tax comparison",
)
replace_in_script_and_master(
    "scripts/advanced/A6-2_sell-borrow-or-hold-funding-a-year-of-sp.md", ADV,
    "That is the wrong comparison.",
    "I think that comparison leaves out how long you carry the loan and what happens if Bitcoin falls.",
    "A6.2 comparison context",
)

replace_in_script_and_master(
    "scripts/advanced/A7-1_advanced-custody-passphrase-multisig-collaborative.md", ADV,
    "The goal is not maximum complexity. It is removing a specific failure without creating a recovery process your family cannot operate.",
    "I would only add complexity when it removes a specific failure and your family can still operate the recovery process.",
    "A7.1 complexity judgment",
)
replace_in_script_and_master(
    "scripts/advanced/A7-1_advanced-custody-passphrase-multisig-collaborative.md", ADV,
    "It cannot sign by itself.",
    "The descriptor helps reconstruct and watch the wallet, but it cannot sign a transaction by itself.",
    "A7.1 descriptor explanation",
)
replace_in_script_and_master(
    "scripts/advanced/A7-1_advanced-custody-passphrase-multisig-collaborative.md", ADV,
    "The goal is that any intended two-key recovery team can reconstruct the wallet without guessing derivation paths or depending on one company.",
    "You are done when any two people who are supposed to recover the wallet can do it without guessing derivation paths or depending on one company.",
    "A7.1 recovery finish line",
)

replace_in_script_and_master(
    "scripts/advanced/A7-2_what-self-custody-actually-asks-of-you.md", ADV,
    "If you do take the job, being a little paranoid is appropriate. You should feel the weight. The goal is not fear. The goal is to build a process strong enough that you do not need to think about it every day.",
    "If you take the job, I think some caution is appropriate. You should feel the weight of it. Then build a process strong enough that you do not have to think about it every day.",
    "A7.2 responsibility close",
)

replace_in_script_and_master(
    "scripts/advanced/A7-3_concentration-one-institution-one-vendor.md", ADV,
    "The goal is not to collect devices. It is to prevent one flaw, provider, credential, household event, or process error from reaching everything.",
    "I would not add a second device or provider just to have more pieces. I would add it when one flaw, provider, credential, household event, or process error can still reach everything.",
    "A7.3 concentration judgment",
)
replace_in_script_and_master(
    "scripts/advanced/A7-3_concentration-one-institution-one-vendor.md", ADV,
    "Whether the current amount justifies a second institution or independent signing path—and whether the household can maintain it well.",
    "Whether the current amount justifies a second institution or independent signing path, and whether the household can maintain it well.",
    "A7.3 decision line",
)

replace_in_script_and_master(
    "scripts/advanced/A8-1_advanced-do-you-need-a-trust-and-which-o.md", ADV,
    "None of those results happens automatically.",
    "The trust only produces those results when the documents, funding, retained powers, and state law actually support them.",
    "A8.1 trust mechanics",
)

# ---------------------------------------------------------------------------
# F20: Bitcoin can remain part of a funding plan five years out.
# ---------------------------------------------------------------------------

f20_script_old = """Three to 7 years out is where you can start taking some risk. A balanced mix of stocks and bonds, or something like an I-Bond ladder. I'd still keep Bitcoin out of that lane.

And then 10 years or more is where a planned Bitcoin sell schedule can actually start to make sense. At that point, cash is the wrong answer, because the drag of holding cash that long is going to cost you more than the volatility would. If you are going to fund something out of Bitcoin, plan those sales into your low-bracket years, meaning the years when your income is small enough that the tax rate on those sales is low, and I'll cover how to find those years in the tax module."""

f20_script_new = """Three to 5 years out is where I would start separating the part you have firmly committed to from the part that is still flexible. The committed portion can start moving into a balanced mix of stocks and bonds, an I-Bond ladder, or another less volatile Bridge holding.

From 5 to 10 years out, Bitcoin can remain part of the funding plan. I would not automatically move the entire future expense into cash at year 5. The part you absolutely cannot afford to come up short on should depend less and less on Bitcoin as the date gets closer. The part that is flexible can stay exposed to Bitcoin longer.

At 10 years or more, a planned Bitcoin sell schedule can make sense for a larger part of the cost. If you are going to fund something out of Bitcoin, plan the sales into your low-bracket years, meaning the years when your income is small enough that the tax rate on those sales is low, and I'll cover how to find those years in the tax module."""

replace_exact(
    "scripts/02-3_fund-a-known-future-cost-the-six-questio.md",
    f20_script_old,
    f20_script_new,
    "F20 spoken lane",
)

# Record Austin's source in the protected script header.
replace_exact(
    "scripts/02-3_fund-a-known-future-cost-the-six-questio.md",
    "this lesson and stops.\n============================================================",
    "this lesson and stops.\nSOURCE: source-material/2026-08-26-f20-and-voice-pass.md · Austin five-year funding ruling\n============================================================",
    "F20 script source header",
)

# Master header: turn the filming block into a resolved authority note.
replace_regex(
    CORE,
    r"> 🔴 \*\*FILMING BLOCKER \(F20\).*?See `AUTHORITY-FLAGS\.md`\.\n",
    "> ✅ **F20 RESOLVED BY AUSTIN, 2026-08-26.** Bitcoin can remain part of a funding plan five years out. The protected amount becomes less dependent on Bitcoin as the date approaches; no fixed percentage was invented. Source: `source-material/2026-08-26-f20-and-voice-pass.md`.\n",
    "F20 master blocker resolution",
    flags=re.S,
)

f20_master_table_old = """| 0 to 1 year | High-yield savings, T-bills, CDs. Treat it like part of the reserve | Anything volatile |
| 1 to 3 years | Short-term Treasuries, HYSA | Stocks, Bitcoin — not enough time to recover from a bad draw right before the bill |
| 3 to 7 years | A balanced mix of stocks and bonds, or an I-Bond ladder | Bitcoin |
| 10+ years | A planned Bitcoin sell schedule can start to make sense here | Cash — the drag over that long costs more than the volatility would |

> 🔶 F20: the 7-to-10 band is not addressed in the dictation. Left as spoken.

For 10+ year costs, plan the sales into low-bracket years — the years when your income is small enough that the tax rate on those sales is low. Module 5 shows you how to find yours."""

f20_master_table_new = """| 0 to 1 year | High-yield savings, T-bills, CDs. Treat it like part of the reserve | Anything volatile |
| 1 to 3 years | Short-term Treasuries, HYSA | Stocks or Bitcoin for the committed amount |
| 3 to 5 years | Start moving the firmly committed portion into a less-volatile Bridge mix | Letting the whole commitment depend on Bitcoin |
| 5 to 10 years | Bitcoin can remain part of the funding plan while the protected portion grows in Bridge | Automatically moving the entire future expense to cash at year 5 |
| 10+ years | A planned Bitcoin sell schedule can fund a larger part of the cost | Holding the entire long-term target in cash |

Bitcoin can remain in the Legacy funding source. The amount you cannot afford to miss moves into Bridge as the date gets closer. By the time the committed money is needed in one or two years, that amount should no longer depend on Bitcoin cooperating.

For costs funded partly from Bitcoin, plan sales into low-bracket years when practical. Module 5 shows you how to find those years."""
replace_exact(CORE, f20_master_table_old, f20_master_table_new, "F20 master table")

f20_lesson_table_old = """| 0–1 year | HYSA, T-bills, CDs. Treat it like part of the reserve | Anything volatile |
| 1–3 years | Short Treasuries, HYSA | Stocks, Bitcoin — not enough time to recover from a bad draw right before the bill |
| 3–7 years | Balanced stocks/bonds, or an I-Bond ladder | Bitcoin |
| 10+ years | A planned Bitcoin sell schedule can start to make sense here | Cash — the drag over that long costs more than the volatility would |

For 10+ year costs, plan the sales into low-bracket years — the years your income is small enough that the tax rate on those sales is low. Module 5 shows you how to find yours."""

f20_lesson_table_new = """| 0–1 year | HYSA, T-bills, CDs. Treat it like part of the reserve | Anything volatile |
| 1–3 years | Short Treasuries, HYSA | Stocks or Bitcoin for the committed amount |
| 3–5 years | Start moving the firmly committed portion into a less-volatile Bridge mix | Letting the whole commitment depend on Bitcoin |
| 5–10 years | Bitcoin can remain part of the funding plan while the protected portion grows in Bridge | Automatically moving the entire future expense to cash at year 5 |
| 10+ years | A planned Bitcoin sell schedule can fund a larger part of the cost | Holding the entire long-term target in cash |

Bitcoin can remain in the Legacy funding source. The amount you cannot afford to miss moves into Bridge as the date gets closer. By the time the committed money is needed in one or two years, that amount should no longer depend on Bitcoin cooperating.

For costs funded partly from Bitcoin, plan sales into low-bracket years when practical. Module 5 shows you how to find those years."""
replace_exact(
    "lesson-text/02-3_fund-a-known-future-cost-the-six-questio.md",
    f20_lesson_table_old,
    f20_lesson_table_new,
    "F20 lesson table",
)

# Visual brief now has a complete timeline and carries the approved claim.
write(
    "visuals/2-3_cost-lanes.md",
    """# 2.3 · Every future cost has a lane

**Paste `00-STYLE.md` first, then this.**

## What it has to make obvious
That time changes how much of a committed expense can still depend on Bitcoin. Bitcoin can remain part of the funding plan five years out, while the amount the household cannot miss gradually moves into Bridge.

## The visual
Five horizontal lanes stacked by time horizon, left-aligned to a shared **today**. Each lane shows the funding sources and the amount becoming protected as the date approaches. Use a growing Bridge bar across the 5–10 and 3–5 lanes rather than presenting one abrupt all-cash cutoff.

## Labels and data

- **0–1 yr:** HYSA, T-bills, CDs. Committed amount fully protected.
- **1–3 yr:** short Treasuries, HYSA. No Bitcoin dependency for the committed amount.
- **3–5 yr:** committed portion transitions into Bridge; flexible portion can remain invested.
- **5–10 yr:** **Bitcoin can remain part of the funding plan**; the protected Bridge portion grows as the date gets closer.
- **10+ yr:** planned Bitcoin sell schedule can fund a larger part of the cost.

Do not show a fixed Bitcoin percentage. Do not relabel Bitcoin itself as a Bridge asset. Show Bitcoin in Legacy feeding planned sales while the committed amount accumulates in Bridge.

## Motion
Build the lanes from long-term to near-term. At 5–10 years, Bitcoin and Bridge appear together. As the timeline moves toward today, the Bridge portion grows and the Bitcoin-dependent portion shrinks. At 1–3 years, the committed amount is fully outside Bitcoin.
""",
)

# Walkthrough handoff: connect the life event to the committed/protected amount.
walk_path = "scripts/02-5_WALKTHROUGH_cashflow-and-reserve.md"
walk_old = """Add the dated expenses or income changes you genuinely expect. If there is nothing major coming, return to Build Your Plan and choose **Nothing major coming** rather than leaving the area ambiguous.

⚠ Life events are expected changes. Hypothetical questions stay in Scenarios."""
walk_new = """Add the dated expenses or income changes you genuinely expect. For a cost five or more years away, say which part can still depend on Bitcoin and which part you have firmly committed to protect in Bridge as the date gets closer. If there is nothing major coming, return to Build Your Plan and choose **Nothing major coming** rather than leaving the area ambiguous.

⚠ Life events are expected changes. Hypothetical questions stay in Scenarios. The life event holds the cost; Allocation holds the protected Bridge amount."""
replace_exact(walk_path, walk_old, walk_new, "F20 walkthrough handoff")

# Student walkthrough mirrors the same handoff.
student_walk = "lesson-text/02-5_walkthrough-cashflow-reserve.md"
student_text = read(student_walk)
if "Bitcoin can remain part of the funding plan" not in student_text:
    marker = "## Complete when"
    addition = """## Future-cost handoff

For a cost five or more years away, Bitcoin can remain part of the funding plan. Record the full expected cost as a life event, then identify the amount you have firmly committed to protect in Bridge as the date approaches. The life event and the funding container are two separate entries.

"""
    if marker not in student_text:
        raise RuntimeError("2.5 student handoff marker missing")
    write(student_walk, student_text.replace(marker, addition + marker, 1))

# Module checkpoint now tests the five-year ruling instead of leaving a gap.
checkpoint_old = "- [ ] Every known future cost inside ten years is entered as a **life event** (so the projection knows it is coming) and has a funding lane, or you have deliberately decided monthly cash flow absorbs it"
checkpoint_new = "- [ ] Every known future cost inside ten years is entered as a **life event** and has a funding lane, or you have deliberately decided monthly cash flow absorbs it. For a cost five or more years away, Bitcoin can remain part of the funding plan, and you have identified the committed amount that will become less Bitcoin-dependent as the date approaches"
replace_exact("MODULE-CHECKPOINTS.md", checkpoint_old, checkpoint_new, "F20 checkpoint")

# Authority flag: preserve history, state the ruling and its narrow scope.
replace_regex(
    "AUTHORITY-FLAGS.md",
    r"### F20 · The 7-to-10-year funding lane is unstated\n.*?(?=\n### F21)",
    """### F20 ✅ RESOLVED · Bitcoin can remain part of funding five years out

**Austin's ruling, 2026-08-26:** *\"yes Bitcoin can remain part of funding 5 years out.\"*

The course now treats five years as a transition rather than an automatic all-cash cutoff. Bitcoin may remain one source in the funding plan. The amount the household has firmly committed to and cannot afford to miss becomes less dependent on Bitcoin as the date approaches. By one to two years out, the committed amount should not depend on Bitcoin cooperating.

No fixed Bitcoin percentage was invented. Bitcoin can remain in Legacy while planned sales build the protected amount in Bridge. This resolves the 7-to-10-year gap without relabeling Bitcoin as a Bridge holding.

Source: `source-material/2026-08-26-f20-and-voice-pass.md`.

""",
    "F20 authority resolution",
    flags=re.S,
)

# Dictation pickup sheet now contains one true blocker.
replace_regex(
    "DICTATION-PICKUPS.md",
    r"## Blocking pickup 1 · F20 · the 7-to-10-year funding lane\n.*?\n---\n\n## Blocking pickup 2 · F22",
    """## Resolved · F20 · the 7-to-10-year funding lane

Austin ruled on 2026-08-26 that Bitcoin can remain part of the funding plan five years out. The protected commitment becomes less Bitcoin-dependent as the date approaches, with no fixed percentage invented. Implemented in 2.3, its visual, checkpoint, walkthrough handoff, and source registry.

---

## Blocking pickup · F22""",
    "F20 pickup resolution",
    flags=re.S,
)

# Final status and research receipt: F22 is now the only Austin-authorship block.
replace_exact(
    "FINALIZATION-STATUS.md",
    "- **F20:** the 7-to-10-year future-cost lane.\n- **F22:** the next-dollar default order, overrides, and deliberate-split rule.",
    "- **F22:** the next-dollar default order, overrides, and deliberate-split rule.",
    "final status blocker list",
)
replace_exact(
    "PROFESSIONAL-RESEARCH-VERIFICATION.md",
    "- F20 and F22 remain the only Austin dictation blockers.",
    "- F20 is resolved by Austin's five-year funding ruling. F22 remains the only Austin dictation blocker.",
    "research receipt blocker status",
)

# Source map records why the pass changed tone without replacing dictation.
source_map = read("DICTATION-SOURCE-MAP.md")
source_section = """## 2026-08-26 · Voice pass and five-year funding ruling

**Source:** `source-material/2026-08-26-f20-and-voice-pass.md` plus the retained 0.2 / 1.1 / 1.2 dictation.

The voice pass reviewed every core and Advanced teach script. It changed editor-shaped lines that sounded like slogans, clever reversals, compressed verdicts, or formal research prose. It did not rewrite Austin's actual dictation, walkthrough click paths, verified legal or tax qualifications, course structure, or unresolved F22 planning policy.

F20 is now resolved narrowly: Bitcoin can remain part of a funding plan five years out; the firmly committed amount becomes less dependent on Bitcoin as the date approaches; no percentage was invented.

"""
if source_section.strip() not in source_map:
    write("DICTATION-SOURCE-MAP.md", source_map.rstrip() + "\n\n" + source_section)

# Claim registry protects the new planning ruling in every live 2.3 layer.
registry = read("CLAIM-REGISTRY.md")
claim_row = "| five-year-btc-funding | 2.3 | `(?i)Bitcoin can remain part of the funding plan` | master,script,lesson-text,module,visual | Austin's 2026-08-26 ruling; no fixed percentage is implied |"
if claim_row not in registry:
    anchor = "| known-cost-rule | 2.3 | `(?i)does not automatically need to be fully funded` | master,script,lesson-text,module | A future expense needs a plan; it does not outrank Bitcoin accumulation by default. This is the AUSTIN-AUTHORITY worked example |"
    if anchor not in registry:
        raise RuntimeError("CLAIM-REGISTRY known-cost anchor missing")
    registry = registry.replace(anchor, anchor + "\n" + claim_row, 1)
    write("CLAIM-REGISTRY.md", registry)

# ---------------------------------------------------------------------------
# Voice-pass report: what was actually reviewed and what was deliberately left.
# ---------------------------------------------------------------------------

changed_list = "\n".join(f"- `{path}`" for path in sorted(CHANGED_SCRIPTS))
write(
    "AUSTIN-VOICE-PASS-REPORT.md",
    f"""# Austin dictation voice pass

**Completed:** 2026-08-26  
**Authority:** `source-material/2026-08-25-module-0-1-dictation.md` and `source-material/2026-08-26-f20-and-voice-pass.md`

## What the source says about Austin's voice

Austin explains the plain-language meaning first, tells the viewer why it affects the plan, gives a concrete example or source of truth, and then restates the practical decision. He marks judgment with phrases such as **I think**, **I would**, and **personally**. Useful repetition stays when it makes the action clearer. App clicks stay in walkthroughs.

## Scope

Every core and Advanced teach script was scanned. Actual Austin dictation, direct numbered teaching, app labels, and required factual qualifications were deliberately left alone. The pass changed the editor-shaped lines that were trying to sound finished rather than trying to explain the decision.

## Spoken scripts changed

{changed_list}

## Representative changes

- **Benefit first:** the AI lesson now opens with how the tool helps, matching Austin's direction, instead of using a clever cannot-do reversal.
- **Explain instead of sloganize:** short lines such as *\"That's the whole product\"*, *\"Three documents, three jobs\"*, and repeated *\"The goal is...\"* constructions were replaced with the actual mechanism or action.
- **Mark judgment:** college, assumptions, custody complexity, and concentration decisions now use Austin's **I think / I would** framing where the statement is a planning judgment.
- **Keep technical precision:** tax, custody, insurance, and estate qualifications from the primary-source audit remain intact, but formal transitions were rewritten into plain explanations.
- **Resolve F20:** Bitcoin can remain part of the funding plan five years out. The committed amount becomes less dependent on Bitcoin as the date approaches. No fixed percentage was added.

## Deliberately unchanged

- 0.1 and the genuine 1.1 / 1.2 dictation, except for already-documented factual or lifecycle corrections.
- Walkthrough narration, which remains a DO / SEE / warning sheet rather than a teleprompter script.
- Lesson 4.3's planning order. F22 is still Austin's decision and is the only remaining authorship blocker.
- Current-law qualifications and professional publication gates.
""",
)

# Remove the temporary scan artifacts from the finished branch.
for temp in [
    ROOT / "AUSTIN-DICTATION-VOICE-AUDIT.md",
    ROOT / "voice-final" / "RUN-SCAN",
]:
    if temp.exists():
        temp.unlink()

print(f"changed {len(CHANGED_SCRIPTS)} spoken scripts")
for path in sorted(CHANGED_SCRIPTS):
    print(f"  {path}")
