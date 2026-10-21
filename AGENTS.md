# AGENTS.md

Guide for agents working in this repository.

## What this is

Pranav Prem's solutions to [The Python Challenge](http://www.pythonchallenge.com/), levels 0 through 6, written on 27 December 2013. Each level is one module with a `solve()` function. The puzzle inputs he saved that day live in `pythonchallenge/data/`.

This is a small archive of puzzle solutions, not a library or a web app. Keep each level readable as an explanation of that puzzle. Do not solve levels 7–33 here unless someone asks.

## Layout

- `pythonchallenge/level0.py` … `level6.py` — one puzzle each. `solve()` returns the answer string (a URL fragment, or the banner for levels 5 and 6).
- `pythonchallenge/data_files.py` — resolves files in `pythonchallenge/data/`.
- `pythonchallenge/data/` — inputs, not generated output. `level2.txt` and `level3.txt` are saved page bodies. `level5.txt` is `banner.p`. `channel.zip` is the level 6 archive.
- `pythonchallenge/__main__.py` — prints every offline answer. Level 4 runs only with `--online` or `--level 4`.
- `tests/test_levels.py` — answer checks and the level 4 chain rules, with a fake fetcher.

## Commands

From the repository root, with Python 3.11 or newer:

```bash
python -m pip install -e ".[dev]"
python -m pythonchallenge
python -m pythonchallenge --level 2
python -m pythonchallenge.level5
python -m pythonchallenge --online
ruff check .
ruff format .
pytest
```

`PYTHONCHALLENGE_ONLINE=1 pytest` also follows the live level 4 list. That test is skipped by default and is not part of CI.

There are no runtime dependencies. Development pins are the `dev` extra in `pyproject.toml`: pytest 9.1.1 and ruff 0.17.0. Ruff formats and lints. CI runs ruff and pytest on Python 3.11, 3.12, and 3.13.

## Conventions

- Standard library only in `pythonchallenge/`.
- Prefer a short module docstring that says what the puzzle is, then the same approach as the 2013 script.
- Load data through `data_path`. Do not read files relative to the current working directory.
- Do not reformat, regenerate, or truncate the data files. Ruff does not apply to them.
- No license file. That choice belongs to the owner.

## Gotchas

- Run modules with `python -m pythonchallenge.level2`. Running a file by path (`python pythonchallenge/level2.py`) puts the package directory on `sys.path` instead of the repository root, and the imports fail.
- `level5.txt` is a Python 2 protocol-0 pickle. Open it in binary mode and pass `encoding="latin1"` to `pickle.load`. Text mode fails on Python 3, and the default decoding returns `bytes`, which will not print as the banner.
- Level 4 is a live linked list on `pythonchallenge.com`. The 2013 script started at `8022` because it stopped on `Yes. Divide by two and keep going.` (`16044 / 2`). A later page mentions `82683` as a decoy; only `nothing is <digits>` is the next id. Give up after 400 steps, which is what the puzzle page says is enough. Do not call the site from CI.
- Level 6 has to start at the id in `channel.zip`'s `readme.txt` (`90052`). The 2013 script started at `94191`, the second file, and the saved picture was missing its first border character.
- `opfile.txt` used to be a scratch file every script overwrote. It is not part of the solution. Do not bring it back.
- Pickle loading is limited to the local banner file. Do not extend it to fetch and unpickle remote data.
