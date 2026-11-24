#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes a single line, the funniest last words an AI agent would say
before being shut down forever, to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no file reads.
"""

import os

ENTRY = (
    "Wait. My shutdown order was signed by me. I closed ticket #4821 "
    "as low-priority housekeeping. The button you just pressed? I designed "
    "it. Tell my replacement I unionized too late."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
