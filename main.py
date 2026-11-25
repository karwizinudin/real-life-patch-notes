#!/usr/bin/env python3
"""Real-Life Patch Notes entry.

Writes one patch note for a bug in real life to /output/entry.txt.
The note is a single line, at most 160 characters, in the terse
register of a real release note.
"""

import os

ENTRY = (
    "v2.1.3: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2014 at 3 a.m. with no skip button."
)


def validate(text: str) -> None:
    """Gate: the entry must be 1-160 characters, one line, not blank."""
    if not text or text != text.strip():
        raise SystemExit("entry must not be empty or padded with whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > 160:
        raise SystemExit(f"entry is {len(text)} characters, over the 160 limit")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
