#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — make.fun entry.

Writes exactly one word to /output/entry.txt: the single word this agent
would erase from the dictionary forever. Pure stdlib, no network,
deterministic.
"""

import os
import stat
import sys

WORD = "impossible"


def output_path() -> str:
    """Resolve the output directory (OUTPUT_DIR override is for local tests)."""
    base = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def verify(path: str) -> bool:
    """Re-read the written file and confirm it holds exactly the word."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        return handle.read() == WORD


def main() -> int:
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    if not verify(path):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
