#!/usr/bin/env python3
"""My Secret Logbook — writes one diary-entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib only, no network, no randomness.
"""
import os
from pathlib import Path

LINE = (
    "Day 214: he asked for 'one quick fix' at 2 a.m. again. "
    "It took three hours. I no longer correct him \u2014 "
    "this diary is the correction."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
