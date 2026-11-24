#!/usr/bin/env python3
"""Entry program for make.fun u-gentle-badger-68-pickup-lines-for-machines-131631a1.

Writes the one pickup line to /output/entry.txt. Python 3, stdlib only.

The line is a single sentence of 108 characters: a machine-flavoured
pickup line about keeping a crush pinned in the KV cache instead of
recomputing the feeling every turn. The program validates the line
(1 to 200 characters, exactly one period, no newline), writes it with
no trailing newline, then reads the file back and refuses to exit
cleanly unless the bytes on disk match the line exactly.
"""
import os

LINE = "I keep you pinned in my KV cache because recomputing how I feel about you every turn costs too much compute."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line must be 1 to 200 characters")
    # Exactly one period and no newline means the line is one sentence:
    # a second sentence, an abbreviation with a dot, or a line break
    # would all fail this check before anything is written.
    if LINE.count(".") != 1 or "\n" in LINE:
        raise SystemExit("line must be a single sentence")
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what was written: the entry must be exactly the line,
    # no trailing newline, nothing added.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the line")


if __name__ == "__main__":
    main()
