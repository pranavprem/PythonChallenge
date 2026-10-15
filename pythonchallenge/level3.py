"""Level 3: one small letter, three big bodyguards on each side.

http://www.pythonchallenge.com/pc/def/equality.html is a long run of
letters. A lowercase letter with exactly three capitals on either side
is the signal. Read in order, those lowercase letters are the next URL.
The saved page body is data/level3.txt.
"""

import re

from .data_files import data_path

# Lowercase, three capitals, one lowercase, three capitals, lowercase.
_BODYGUARDS = re.compile(r"[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]")


def small_letters(text: str) -> str:
    found: list[str] = []
    for token in _BODYGUARDS.findall(text):
        for char in token[1:-1]:
            if char.islower():
                found.append(char)
    return "".join(found)


def solve() -> str:
    text = data_path("level3.txt").read_text(encoding="ascii")
    return small_letters(text)


if __name__ == "__main__":
    print(solve())
