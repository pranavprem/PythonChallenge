"""Locations of the puzzle inputs checked in with the solutions."""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"


def data_path(name: str) -> Path:
    path = DATA_DIR / name
    if not path.is_file():
        raise FileNotFoundError(f"Missing puzzle input: {path}")
    return path
