"""
takes as input string encoded with encode_cyclic function. Returns decoded string.
"""


def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    return encode_cyclic(encode_cyclic(s))

def test_decode_cyclic(): # pragma: no cover
    global decode_cyclic, encode_cyclic
    assert decode_cyclic("bcdaef") == "abcdef", "Test case 1 failed: single cycle group with no remainder"
    assert decode_cyclic("defabc") == "abcdef", "Test case 2 failed: perfect group division"
    assert decode_cyclic("defghibc") == "abcdefghi", "Test case 3 failed: multiple full groups"
    assert decode_cyclic("a") == "a", "Test case 4 failed: single character"
    assert decode_cyclic("") == "", "Test case 5 failed: empty string"

if __name__ == "__main__": # pragma: no cover
    test_decode_cyclic()
