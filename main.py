#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

The program writes a single line, at most 200 characters, reviewing
the most boring everyday object: the doorstop. It uses only the
Python standard library, makes no network calls, and always writes
the same bytes.
"""

import os

LINE = (
    "The doorstop's whole career is being kicked across the floor "
    "by people who forgot it, then blamed when the door slams anyway."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
