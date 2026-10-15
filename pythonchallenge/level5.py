"""Level 5: peak hell.

http://www.pythonchallenge.com/pc/def/peak.html says to pronounce it.
"Peak hell" is pickle, and the page points at banner.p. That file was
saved as data/level5.txt. It is a Python 2 pickle of rows of
``(character, count)`` pairs. Printed, the banner reads "channel".
"""

import pickle

from .data_files import data_path


def render(rows: list) -> str:
    lines: list[str] = []
    for row in rows:
        lines.append("".join(char * count for char, count in row))
    return "\n".join(lines)


def solve() -> str:
    # Protocol 0, written by Python 2. Open it as bytes and ask for str
    # characters; the default bytes result cannot be printed as a banner.
    with data_path("level5.txt").open("rb") as handle:
        rows = pickle.load(handle, encoding="latin1")
    return render(rows)


if __name__ == "__main__":
    print(solve())
