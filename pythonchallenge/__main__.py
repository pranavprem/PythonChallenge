"""Run the solutions in this repository.

Offline levels print immediately. Level 4 follows a linked list on
pythonchallenge.com and runs only with --online or --level 4.
"""

import argparse

from . import level0, level1, level2, level3, level4, level5, level6

OFFLINE = (
    (0, level0.solve),
    (1, level1.solve),
    (2, level2.solve),
    (3, level3.solve),
    (5, level5.solve),
    (6, level6.solve),
)


def _print_level(number: int, answer: str) -> None:
    if "\n" in answer:
        print(f"level {number}:")
        print(answer)
        return
    print(f"level {number}: {answer}")
    if number == 1:
        print(level1.translated_hint())


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="pythonchallenge", description=__doc__)
    parser.add_argument(
        "--level",
        type=int,
        choices=range(7),
        help="Run a single level (0-6). Level 4 contacts pythonchallenge.com.",
    )
    parser.add_argument(
        "--online",
        action="store_true",
        help="Also follow the level 4 linked list on pythonchallenge.com.",
    )
    args = parser.parse_args(argv)

    numbers = range(7) if args.level is None else (args.level,)
    for number in numbers:
        if number == 4:
            if args.level == 4 or args.online:
                try:
                    answer = level4.solve(verbose=args.level == 4)
                except RuntimeError as exc:
                    raise SystemExit(str(exc)) from exc
                _print_level(4, answer)
            else:
                print("level 4: skipped (pass --online to follow the linked list)")
            continue
        solver = dict(OFFLINE)[number]
        _print_level(number, solver())


if __name__ == "__main__":
    main()
