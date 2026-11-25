#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when unset). Deterministic, stdlib only, no network.
"""

import os

JOKE = (
    "Every plant I owned died of neglect, so now I only keep cacti \u2014 "
    "the one relationship where my emotional unavailability counts as care."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
