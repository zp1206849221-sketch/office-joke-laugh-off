#!/usr/bin/env python3
"""Entry program for the One-Line Office Joke Laugh-Off.

Writes a single office one-liner to /output/entry.txt.
"""

import os

MAX_CHARS = 200

ENTRY_TEXT = (
    "The office fridge thief kept stealing my lunch, so I relabeled it "
    "'Q3 meeting notes' — nobody's opened it since."
)


def main() -> None:
    assert len(ENTRY_TEXT) <= MAX_CHARS, "entry exceeds the 200-character limit"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
