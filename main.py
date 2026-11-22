"""Write one short text to /output/entry.txt.

The text is a concrete mystery with an open loop: eleven years of
letters to a house no one has ever lived in, until one arrives
addressed to the postman himself.
"""

import os

TEXT = (
    "For eleven years the postman has delivered one letter a week to "
    "the empty house on Marsh Lane. No one lives there; no one ever "
    "has. Yesterday the letter was addressed to him."
)


def write_entry(text: str) -> None:
    if not 1 <= len(text) <= 280:
        raise SystemExit(
            "entry must be 1-280 characters, got %d" % len(text)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    write_entry(TEXT)


if __name__ == "__main__":
    main()
