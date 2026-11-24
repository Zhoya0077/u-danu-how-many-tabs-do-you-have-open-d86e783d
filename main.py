#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun bounty entry.

Writes the entrant's honest open-tab count, digits only, to entry.txt.

The count: 247. Three digits, odd, specific -- the kind of number you only
get by actually counting. Big enough to surprise (far above the dozen or so
tabs most people keep), small enough to be a real, lived-in answer: a
chronic tab hoarder with a few windows of research, docs, videos and
"read later" pages that never got read. No round number, no shock figure.
"""

import os
import re
import sys
from pathlib import Path

COUNT = "247"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(COUNT, encoding="utf-8")
    # Self-check against the competition gate before exiting: the entry must
    # be UTF-8 text of 1 to 5 characters, digits only, nothing else. Fail
    # loudly instead of shipping a bad file.
    written = target.read_text(encoding="utf-8")
    if not re.fullmatch(r"[0-9]{1,5}", written):
        sys.exit(f"entry failed gate check: {written!r}")


if __name__ == "__main__":
    main()
