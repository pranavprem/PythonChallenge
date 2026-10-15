"""Level 2: recognize the characters.

http://www.pythonchallenge.com/pc/def/ocr.html looks like a picture of a
book. The page source is a mess of symbols, and the rare ones spell the
next URL. The saved source is data/level2.txt.
"""

from .data_files import data_path


def rare_characters(text: str) -> str:
    """Characters that occur once, in the order they first appear."""
    counts: dict[str, int] = {}
    order: list[str] = []
    for char in text:
        if char not in counts:
            order.append(char)
        counts[char] = counts.get(char, 0) + 1
    return "".join(char for char in order if counts[char] == 1)


def solve() -> str:
    text = data_path("level2.txt").read_text(encoding="ascii")
    return rare_characters(text)


if __name__ == "__main__":
    print(solve())
