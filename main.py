#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes one deadpan sentence — the single line that could have replaced an
entire pointless meeting — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: an email that got promoted beyond its abilities. The meeting never
needed to exist; the email already said it all, and the promotion was the joke.
"""

import os
import sys

LINE = "This meeting is just an email that got promoted beyond its abilities."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")

    # Self-check the gate before writing: 1-200 chars, not whitespace-only.
    if not 1 <= len(LINE) <= 200:
        print(f"gate failed: {len(LINE)} chars", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("gate failed: whitespace-only", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the entry is exactly the line, 69 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Verify after write: exact bytes, one line, gate holds.
    with open(path, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert text == LINE, "written text differs from line"
    assert 1 <= len(text) <= 200, "gate failed after write"
    assert text.strip(), "gate failed after write (whitespace-only)"
    assert "\n" not in text, "entry must be a single line"
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
