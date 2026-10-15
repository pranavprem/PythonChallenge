"""Offline checks for the level solutions, plus the level 4 chain rules."""

import hashlib
import os

import pytest

from pythonchallenge import level0, level1, level2, level3, level4, level5, level6
from pythonchallenge.__main__ import main

HINT_TRANSLATION = (
    "i hope you didnt translate it by hand. thats what computers are for. "
    "doing it in by hand is inefficient and that's why this text is so long. "
    "using string.maketrans() is recommended. now apply on the url."
)

# Banners rendered from the checked-in puzzle files.
LEVEL5_SHA256 = "8eb7f9faa6f65dee48954e5d8cabe13aaee62762f3663589ac532fc457529371"
LEVEL6_SHA256 = "d8e3f11cd7264e7d709b65881c72a8d1d92c70c0926477f08162150aea2c53a3"


def test_level0_is_two_to_the_38():
    assert level0.solve() == str(2**38) == "274877906944"


def test_level1_shift_and_url():
    assert level1.translated_hint() == HINT_TRANSLATION
    assert level1.shift_by_hand(level1.HINT) == level1.translated_hint()
    assert level1.solve() == "ocr"


def test_level2_rare_characters_spell_equality():
    assert level2.solve() == "equality"


def test_level2_keeps_first_seen_order():
    assert level2.rare_characters("abccbaXY") == "XY"


def test_level3_bodyguards_spell_linkedlist():
    assert level3.solve() == "linkedlist"


def test_level3_ignores_the_wrong_number_of_capitals():
    text = "aBCDxFGHy AAAAbCCC aBCDDFGHi"
    assert level3.small_letters(text) == "x"


def test_level4_divides_by_two_and_ignores_decoy_numbers():
    pages = {
        "12345": "and the next nothing is 16044",
        "16044": "Yes. Divide by two and keep going.",
        "8022": (
            "There maybe misleading numbers in the text. "
            "One example is 82683. Look only for the next nothing "
            "and the next nothing is 63579"
        ),
        "63579": "peak.html",
    }
    assert level4.follow(pages.get) == "peak.html"


def test_level4_stops_on_a_loop_and_on_the_step_cap():
    looping = {"1": "nothing is 2", "2": "nothing is 1"}
    with pytest.raises(RuntimeError, match="looped"):
        level4.follow(looping.get, start="1")

    def counting(nothing: str) -> str:
        return f"nothing is {int(nothing) + 1}"

    with pytest.raises(RuntimeError, match="5 steps"):
        level4.follow(counting, start="1", limit=5)


def test_level5_banner_is_the_pickle_picture():
    banner = level5.solve()
    assert hashlib.sha256(banner.encode()).hexdigest() == LEVEL5_SHA256
    assert len(banner.splitlines()) == 23
    assert set("".join(banner.splitlines())) <= set(" #")


def test_level6_comments_keep_the_full_border():
    banner = level6.solve()
    assert hashlib.sha256(banner.encode()).hexdigest() == LEVEL6_SHA256
    border, second, _, letters = banner.splitlines()[:4]
    assert border == second == "*" * 64
    assert "YYYY" in letters and "EEEEE" in letters


def test_cli_prints_offline_answers(capsys):
    main([])
    output = capsys.readouterr().out
    assert "level 0: 274877906944" in output
    assert "level 1: ocr" in output
    assert HINT_TRANSLATION in output
    assert "level 2: equality" in output
    assert "level 3: linkedlist" in output
    assert "level 4: skipped" in output
    assert "#####" in output
    assert "YYYY" in output


def test_cli_single_level(capsys):
    main(["--level", "0"])
    assert capsys.readouterr().out.strip() == "level 0: 274877906944"


@pytest.mark.skipif(
    os.environ.get("PYTHONCHALLENGE_ONLINE") != "1",
    reason="set PYTHONCHALLENGE_ONLINE=1 to follow the live linked list",
)
def test_level4_live_chain_ends_at_peak():
    assert level4.solve() == "peak.html"
