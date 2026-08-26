#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def patch(path: str, pairs: list[tuple[str, str]]) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new)
    target.write_text(text, encoding="utf-8")


patch("MASTER-COURSE.md", [
    (
        "The useful question is not everything the AI cannot do. It is how it can help you understand and improve the financial plan you are building.",
        "I want to focus this lesson on how the AI can help you understand and improve the financial plan you are building.",
    ),
    (
        "The goal is to replace doomscrolling with one clean read that takes less than two minutes. It checks the parts of the Bitcoin market that are actually worth following:",
        "I use this so I can get one clean read of the market without checking five different places. It should take less than two minutes and cover the parts of the Bitcoin market that are actually useful for the plan:",
    ),
    (
        "The goal is not to have the AI make every decision for you. The goal is to understand what the plan is showing, what is missing, and which trade-off you are accepting before you act.",
        "I would not use the AI to make every decision for you. I would use it to understand what the plan is showing, find information that is missing, and think through the trade-off before you make the decision yourself.",
    ),
    (
        "This is why it is important to think through what you personally feel is a conservative and realistic way to model Bitcoin in the future. The goal is not to choose the model that gives you the earliest date. The goal is to choose the model you can defend.",
        "This is why I think you need to choose a conservative and realistic way to model Bitcoin in the future. I would not choose the model just because it gives you the earliest retirement date. I would choose the one you could defend if you were explaining it to a family member or a friend.",
    ),
    (
        "Not every family uses all six. **College does not have to be solved entirely with money you saved before freshman year.** A complete plan might be: the parents provide the existing 529, add a fixed amount from annual cash flow, the student applies for aid and works summers and takes a defined amount of federal loans, and Bitcoin covers part of the rest if the price and the tax situation work out.",
        "Not every family is going to use all six. A family might use the existing 529, add a fixed amount from annual cash flow, have the student apply for aid and work summers, set a limit on federal loans, and use Bitcoin for part of the remaining cost if the price and tax situation make sense. So college does not have to be solved entirely with money you saved before freshman year.",
    ),
    (
        "**The goal is not to stop buying Bitcoin for seven years because your child may go to college.**",
        "I would not automatically stop buying Bitcoin for seven years because your child may go to college.",
    ),
    (
        "The goal is that the amount you have *firmly promised* does not depend entirely on Bitcoin being at a favorable price on the exact day tuition is due.",
        "What I would do is protect the amount you have *firmly promised* so that portion does not depend entirely on Bitcoin being at a favorable price when tuition is due.",
    ),
    (
        "Same sale proceeds. Different identified units. Different gain.",
        "The sale proceeds are the same, but the gain changes because the Bitcoin came from a different lot.",
    ),
    (
        "Start with contemporaneous records.",
        "Start with the records that were created when the transactions happened.",
    ),
    (
        "The honest plan labels what is known, what is estimated, and what is still unproven.",
        "So in the plan, label what is known, what is estimated, and what is still unproven.",
    ),
    (
        "That is too simple.",
        "I think that leaves out too many of the other costs that can change at the same time.",
    ),
    (
        "The answer is not the most impressive setup. It is the one you can prove.",
        "I would choose the simplest setup you can actually prove works.",
    ),
    (
        "The response is always the same.",
        "When you get one of these messages, stop before you do anything.",
    ),
    (
        "Privacy is part of custody.",
        "Who knows the amount, location, or exact setup is also part of your custody risk.",
    ),
    (
        "Those are different failures.\n\nDual control answers the first. Redundancy answers the second.",
        "These are two different questions. Dual control tells you whether one person can spend alone. Redundancy tells you whether one loss can stop recovery.",
    ),
    (
        "Three documents, three jobs.\n\n",
        "",
    ),
    (
        "You're also not the only reader. It's the agenda for a twenty-minute sit-down with your spouse, the tax pages plus the transaction export go to your CPA, and the access and estate pages go to your attorney. What matters in all three is that you're handing a professional a document rather than asking them to log into an app, and that's what lets three different people start from the same set of facts.",
        "This report is also something you can hand to other people. Use it as the agenda for a twenty-minute conversation with your spouse. Give the tax pages and transaction export to your CPA. Give the access and estate pages to your attorney. That way all three people can start from the same facts without needing to log into your app.",
    ),
])

patch("MASTER-ADVANCED.md", [
    ("That is the whole product.", "So the basic transaction is pretty simple."),
    (
        "That is only the first pass.",
        "I think that leaves out too many of the other costs that can change with the conversion.",
    ),
    (
        "The course used to imply that the state where you live in the year of sale is the whole answer.\n\nIt is not.",
        "The course used to imply that the state where you live in the year of sale is the whole answer. That leaves out a lot of the actual residency rules.",
    ),
    ("State income tax is one line.\n\nAlso price:", "Then I would price the rest of the move too:"),
    (
        "The tax comparison therefore cannot stop at \"loan proceeds are not taxable.\"",
        "So I would not stop the tax comparison at \"loan proceeds are not taxable.\"",
    ),
    (
        "That is the wrong comparison.",
        "I think that comparison leaves out how long you carry the loan and what happens if Bitcoin falls.",
    ),
    (
        "The goal is not maximum complexity. It is removing a specific failure without creating a recovery process your family cannot operate.",
        "I would only add complexity when it removes a specific failure and your family can still operate the recovery process.",
    ),
    (
        "It cannot sign by itself.",
        "The descriptor helps reconstruct and watch the wallet, but it cannot sign a transaction by itself.",
    ),
    (
        "The goal is that any intended two-key recovery team can reconstruct the wallet without guessing derivation paths or depending on one company.",
        "You are done when any two people who are supposed to recover the wallet can do it without guessing derivation paths or depending on one company.",
    ),
    (
        "If you do take the job, being a little paranoid is appropriate. You should feel the weight. The goal is not fear. The goal is to build a process strong enough that you do not need to think about it every day.",
        "If you take the job, I think some caution is appropriate. You should feel the weight of it. Then build a process strong enough that you do not have to think about it every day.",
    ),
    (
        "The goal is not to collect devices. It is to prevent one flaw, provider, credential, household event, or process error from reaching everything.",
        "I would not add a second device or provider just to have more pieces. I would add it when one flaw, provider, credential, household event, or process error can still reach everything.",
    ),
    (
        "None of those results happens automatically.",
        "The trust only produces those results when the documents, funding, retained powers, and state law actually support them.",
    ),
])
