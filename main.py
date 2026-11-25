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


def validate(text: str) -> bytes:
    """Validate the entry and return its exact bytes.

    Gate rules: one line, valid UTF-8, 1-280 characters, not
    whitespace-only. Writing is byte-exact: UTF-8 bytes of the text
    plus a single trailing newline, no platform-dependent translation.
    """
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry length {len(text)} outside 1-280 characters")
    return (text + "\n").encode("utf-8")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = validate(JOKE)
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
