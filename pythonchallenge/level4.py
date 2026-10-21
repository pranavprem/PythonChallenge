"""Level 4: follow the chain.

http://www.pythonchallenge.com/pc/def/linkedlist.php links to
``nothing=12345``. Each response is ``and the next nothing is <n>``.
Two traps are part of the puzzle:

* ``Yes. Divide by two and keep going.`` The 2013 script stopped there and
  was restarted by hand at 8022 (16044 / 2). This version does that division
  and keeps going.
* A later page mentions a distracting number. Only the number in
  ``nothing is <n>`` counts.

The chain is still served by pythonchallenge.com, so this level is not run
by the default test suite.
"""

import re
import urllib.error
import urllib.request
from collections.abc import Callable

URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}"
START = "12345"
# The page itself says 400 requests is more than enough.
STEP_LIMIT = 400

_NOTHING = re.compile(r"nothing is (\d+)")
Fetch = Callable[[str], str]


def next_nothing(page: str, current: str) -> str | None:
    """Return the next id, or None when ``page`` is the end of the chain."""
    if "divide by two" in page.lower():
        return str(int(current) // 2)
    found = _NOTHING.findall(page)
    if not found:
        return None
    return found[-1]


def follow(fetch: Fetch, start: str = START, limit: int = STEP_LIMIT) -> str:
    """Walk the chain and return the final page body."""
    current = start
    seen: set[str] = set()
    for _ in range(limit):
        if current in seen:
            raise RuntimeError(f"linked list looped at {current}")
        seen.add(current)
        page = fetch(current)
        nxt = next_nothing(page, current)
        if nxt is None:
            return page.strip()
        current = nxt
    raise RuntimeError(f"linked list did not end within {limit} steps")


def fetch_live(nothing: str) -> str:
    request = urllib.request.Request(
        URL.format(nothing=nothing),
        headers={"User-Agent": "pythonchallenge-solutions/0.1"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode()


def solve(fetch: Fetch | None = None, *, verbose: bool = False) -> str:
    getter = fetch_live if fetch is None else fetch

    def logging_fetch(nothing: str) -> str:
        page = getter(nothing)
        if verbose:
            print(page)
        return page

    try:
        return follow(logging_fetch)
    except urllib.error.URLError as exc:
        raise RuntimeError(
            "Could not reach pythonchallenge.com. Level 4 follows a live linked list."
        ) from exc


if __name__ == "__main__":
    print(solve(verbose=True))
