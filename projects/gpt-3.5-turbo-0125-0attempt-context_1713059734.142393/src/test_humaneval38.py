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
    global encode_cyclic, decode_cyclic
    
    assert decode_cyclic("abc") == "abc", "Test case 1 failed"
    assert decode_cyclic("defghi") == "defghi", "Test case 2 failed"
    assert decode_cyclic("jklmnopqr") == "jklmnopqr", "Test case 3 failed"
    assert decode_cyclic("stuvwxyza") == "stuvwxyza", "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_decode_cyclic()
