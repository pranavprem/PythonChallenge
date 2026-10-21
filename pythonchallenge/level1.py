"""Level 1: everybody thinks twice before solving this.

http://www.pythonchallenge.com/pc/def/map.html hides a Caesar cipher in the
page, each letter shifted forward by two. The first attempt walked the
string by hand. The decoded hint recommends maketrans(); in Python 3 that
is str.maketrans. The same shift applied to "map" (this level's URL) is
"ocr".
"""

HINT = (
    "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr "
    "amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q "
    "ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. "
    "lmu ynnjw ml rfc spj."
)


def shift_by_hand(text: str) -> str:
    """The first attempt: add 2 to each lowercase letter, wrapping at z."""
    chars = list(text)
    for index, char in enumerate(chars):
        if char == " ":
            continue
        code = ord(char)
        if code > 96:
            code += 2
            if code > 122:
                code -= 26
            chars[index] = chr(code)
    return "".join(chars)


def shift_with_maketrans(text: str) -> str:
    """The version the hint asks for. a-z maps onto c-z, a, b."""
    source = "".join(chr(97 + i) for i in range(26))
    target = "".join(chr(99 + i) for i in range(24)) + "ab"
    return text.translate(str.maketrans(source, target))


def translated_hint() -> str:
    return shift_with_maketrans(HINT)


def solve() -> str:
    return shift_with_maketrans("map")


if __name__ == "__main__":
    print(translated_hint())
    print(solve())
