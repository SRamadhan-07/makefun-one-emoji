#!/usr/bin/env python3
"""One Emoji, One Smile - a make.fun entry.

The entry is a single emoji and nothing more. This program writes
that emoji to entry.txt inside the output directory. The file gets
no trailing newline and no extra decoration, so the output is
exactly one character on every single run.
"""

import os

# Rolling on the floor laughing: warmth at first glance, for anyone.
FACE = "🤣"


def output_file() -> str:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def main() -> None:
    with open(output_file(), "w", encoding="utf-8", newline="") as handle:
        handle.write(FACE)


if __name__ == "__main__":
    main()
