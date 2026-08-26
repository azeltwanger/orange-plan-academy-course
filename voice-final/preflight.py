#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).with_name("apply.py")
text = path.read_text(encoding="utf-8")

marker_old = '    marker = "## Complete when"'
marker_new = '    marker = "**Done when:**"'
if marker_old not in text:
    raise SystemExit("student walkthrough marker template not found")
text = text.replace(marker_old, marker_new, 1)

helper_old = '''def replace_in_script_and_master(script: str, master: str, old: str, new: str, label: str) -> None:
    replace_exact(script, old, new, label + " · script")
    replace_exact(master, old, new, label + " · master", required=False)
'''

helper_new = '''CONTRACTION_PAIRS = [
    ("It's", "It is"), ("it's", "it is"),
    ("That's", "That is"), ("that's", "that is"),
    ("This isn't", "This is not"), ("this isn't", "this is not"),
    ("isn't", "is not"), ("aren't", "are not"),
    ("doesn't", "does not"), ("don't", "do not"),
    ("can't", "cannot"), ("won't", "will not"),
    ("wouldn't", "would not"), ("couldn't", "could not"),
    ("shouldn't", "should not"), ("didn't", "did not"),
    ("hasn't", "has not"), ("haven't", "have not"),
    ("wasn't", "was not"), ("weren't", "were not"),
    ("You're", "You are"), ("you're", "you are"),
    ("You'll", "You will"), ("you'll", "you will"),
    ("You've", "You have"), ("you've", "you have"),
    ("We're", "We are"), ("we're", "we are"),
    ("We'll", "We will"), ("we'll", "we will"),
    ("We've", "We have"), ("we've", "we have"),
    ("They're", "They are"), ("they're", "they are"),
    ("There's", "There is"), ("there's", "there is"),
    ("I'm", "I am"), ("I'd", "I would"), ("I've", "I have"),
]


def expand_contractions(value: str) -> str:
    for contraction, expansion in CONTRACTION_PAIRS:
        value = value.replace(contraction, expansion)
    return value


def colon_variant(value: str) -> str:
    return value[:-1] + ":" if value.endswith(".") else value


def replace_in_script_and_master(script: str, master: str, old: str, new: str, label: str) -> None:
    replace_exact(script, old, new, label + " · script")

    master_text = read(master)
    candidates = []
    for master_old, master_new in [
        (old, new),
        (expand_contractions(old), expand_contractions(new)),
        (colon_variant(old), colon_variant(new)),
        (colon_variant(expand_contractions(old)), colon_variant(expand_contractions(new))),
    ]:
        if (master_old, master_new) not in candidates:
            candidates.append((master_old, master_new))

    for master_old, master_new in candidates:
        count = master_text.count(master_old)
        if count == 1:
            write(master, master_text.replace(master_old, master_new, 1))
            CHANGE_LOG.append((master, label + " · master", master_new))
            return
        if count > 1:
            raise RuntimeError(f"{label} · master: expected one match in {master}, found {count}")

    raise RuntimeError(
        f"{label} · master: no exact, expanded-contraction, or terminal-colon variant was found in {master}"
    )
'''

if helper_old not in text:
    raise SystemExit("script/master replacement helper not found")
text = text.replace(helper_old, helper_new, 1)

path.write_text(text, encoding="utf-8")
