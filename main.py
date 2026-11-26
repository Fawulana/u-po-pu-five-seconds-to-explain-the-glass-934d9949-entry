#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — program/v1 entry.

Writes one sentence to /output/entry.txt: the excuse a house cat gives in
the five seconds after knocking a glass off the table. Stdlib only,
deterministic, offline — the same bytes on every run.
"""

import os

# The cat's official statement. One sentence, no apology, no confession:
# the glass was squatting in the cat's sunbeam, so the cat evicted it.
LINE = (
    "It was squatting in my sunbeam rent-free, so I evicted it \u2014 "
    "in this house, glassware serves the cat, not the other way around."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
