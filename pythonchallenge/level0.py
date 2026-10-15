"""Level 0: warming up.

The page at http://www.pythonchallenge.com/pc/def/0.html shows 2**38 and
asks you to change the URL. The result is the next address.
"""


def solve() -> str:
    return str(2**38)


if __name__ == "__main__":
    print(solve())
