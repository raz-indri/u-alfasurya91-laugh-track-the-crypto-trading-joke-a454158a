#!/usr/bin/env python3
"""Write the winning crypto trading joke to /output/entry.txt.

Entry for the make.fun bounty "Laugh Track: The Crypto Trading Joke
Contest" (u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a).
One line, under 200 characters, about crypto and trading life.
Deterministic: no network, no randomness, no input.
"""

import os

JOKE = (
    "I set an alarm for 3 a.m. to catch the pump. "
    "The pump happened at 2:58, and my alarm is the only thing that went up."
)

# The gate requires 1-200 characters of UTF-8 text, not only whitespace.
assert 1 <= len(JOKE) <= 200, "joke must fit the 200-character cap"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
