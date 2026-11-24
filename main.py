"""One Word, First Thought — make.fun bounty u-0xkianno-one-word-first-thought-106abaf8.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The word is "quiver": a single token that is surprising (not the safe,
expected first thought), vivid (a trembling, and the case that holds
arrows), and carries a double meaning that rewards a second look —
a tremble and a quiver of arrows in six letters.
"""

import os

# The entry: exactly one word, ASCII, no spaces, no hyphens.
WORD = "quiver"

OUTPUT_FILENAME = "entry.txt"


def entry_bytes():
    """The exact bytes written to entry.txt: the word only, no trailing newline."""
    return WORD.encode("utf-8")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "wb") as f:
        f.write(entry_bytes())


if __name__ == "__main__":
    main()
