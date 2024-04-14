"""
takes as input string encoded with encode_shift function. Returns decoded string.
"""


def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

def test_encode_decode_shift(): # pragma: no cover
    global encode_shift, decode_shift
    
    assert encode_shift("abc") == "fgh", "Test case 1 failed"
    assert encode_shift("xyz") == "cde", "Test case 2 failed"
    assert decode_shift("fgh") == "abc", "Test case 3 failed"
    assert decode_shift("cde") == "xyz", "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_encode_decode_shift()
