#!/usr/bin/env python3
"""Office joke entry for make.fun.

Writes a single one-line office joke (under 200 characters) to
/output/entry.txt, the artifact the competition's judge reads.
"""

import os

JOKE = (
    "My boss says we're one big family here, so I asked HR when "
    "the family reunion starts covering my therapy bills."
)


def main() -> None:
    output_dir = "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(JOKE)
    except OSError:
        # Local runs (no sandbox /output): write next to the program.
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(JOKE)
    print(f"wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
