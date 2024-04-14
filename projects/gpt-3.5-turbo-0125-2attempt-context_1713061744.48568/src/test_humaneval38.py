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
    global math
    assert decode_cyclic("abc") == "abc", "Test case 1 failed"
    assert decode_cyclic("def") == "def", "Test case 2 failed"
    assert decode_cyclic("xyz") == "xyz", "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_decode_cyclic()
