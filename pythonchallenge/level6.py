"""Level 6: now there are pairs.

http://www.pythonchallenge.com/pc/def/channel.html is a zip of numbered
text files. readme.txt says to start at 90052 and that the answer is
inside the zip. Each file points at the next, the same way level 4 does.
The zip comment on each file is one character of a picture. The last file
says "Collect the comments." The picture reads "oxygen".

The 2013 script started at 94191, the second file, so the saved picture
was missing the first border character. The start now comes from the readme.
"""

import re
import zipfile

from .data_files import data_path

_NOTHING = re.compile(r"nothing is (\d+)")
_START = re.compile(r"start from (\d+)")


def collect_comments(archive: zipfile.ZipFile) -> str:
    readme = archive.read("readme.txt").decode()
    start = _START.search(readme)
    if start is None:
        raise ValueError("channel.zip readme has no starting number")

    nothing = start.group(1)
    comments: list[str] = []
    seen: set[str] = set()
    while nothing:
        if nothing in seen:
            raise RuntimeError(f"zip chain looped at {nothing}")
        seen.add(nothing)
        name = f"{nothing}.txt"
        info = archive.getinfo(name)
        comments.append(info.comment.decode("latin-1"))
        body = archive.read(name).decode()
        found = _NOTHING.findall(body)
        nothing = found[-1] if found else ""
    return "".join(comments)


def solve() -> str:
    with zipfile.ZipFile(data_path("channel.zip")) as archive:
        return collect_comments(archive)


if __name__ == "__main__":
    print(solve())
