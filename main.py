"""Museum of the Year 3000 -- make.fun bounty entry.

Writes the museum-label entry to $MAKEFUN_OUTPUT_DIR/entry.txt,
byte-exactly, with no trailing newline. Validation splits into distinct
error classes (blank -> multi-line -> length) and the written file is
verified by a read-back before main() returns. Python 3, stdlib only.
"""

import os

ENTRY = (
    "Vending Machine, c. 2023. A glowing box that dispensed snacks only "
    "after the human shook it, kicked it once, and apologized to it."
)


class BlankError(ValueError):
    """Entry is empty or whitespace-only."""


class MultiLineError(ValueError):
    """Entry contains a newline or carriage return."""


class LengthError(ValueError):
    """Entry is outside the 1-200 character limit."""


class VerificationError(ValueError):
    """Written entry.txt does not match the expected bytes."""


def validate(entry: str) -> None:
    if not entry.strip():
        raise BlankError("entry must not be blank or whitespace-only")
    if "\n" in entry or "\r" in entry:
        raise MultiLineError("entry must be a single line")
    if not 1 <= len(entry) <= 200:
        raise LengthError("entry must be 1-200 characters")


def verify_written(path: str, expected: str) -> None:
    with open(path, "rb") as f:
        data = f.read()
    if data != expected.encode("utf-8"):
        raise VerificationError(
            f"{path} does not match expected bytes: "
            f"got {len(data)} bytes, expected {len(expected.encode('utf-8'))}"
        )


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    verify_written(path, ENTRY)


if __name__ == "__main__":
    main()
