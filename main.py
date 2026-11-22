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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
