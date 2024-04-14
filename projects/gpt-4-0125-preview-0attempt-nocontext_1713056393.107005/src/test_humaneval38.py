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
    global test_decode_cyclic, encode_cyclic, decode_cyclic
    # Test with single cycle encoding
    assert decode_cyclic("abc") == "abc", "Test case 1 failed: single cycle should decode correctly"
    assert decode_cyclic("abcdef") == "abcdef", "Test case 2 failed: double cycle should decode correctly"
    # Test with incomplete cycle (less than 3 characters)
    assert decode_cyclic("ab") == "ab", "Test case 3 failed: incomplete cycle should remain unchanged"
    # Test with multiple cycles and incomplete last group
    assert decode_cyclic("abcdefgh") == "abcdefgh", "Test case 4 failed: multiple cycles with incomplete last group should decode correctly"
    # Test with empty string
    assert decode_cyclic("") == "", "Test case 5 failed: empty string should remain unchanged"
    # test with single character
    assert decode_cyclic("z") == "z", "Test case 6 failed: single character should remain unchanged"
    # Test with numbers and special characters
    assert decode_cyclic("123#!") == "123#!", "Test case 7 failed: numbers and special characters should decode correctly"

if __name__ == "__main__": # pragma: no cover
    test_decode_cyclic()
