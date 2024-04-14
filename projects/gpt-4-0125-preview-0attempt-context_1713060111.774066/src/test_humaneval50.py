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

def test_decode_shift(): # pragma: no cover
    global test_decode_shift, encode_shift, decode_shift
    assert decode_shift(encode_shift("hello")) == "hello", "Test case 1 failed: encoding and then decoding should return original"
    assert decode_shift(encode_shift("abc")) == "abc", "Test case 2 failed: encoding and then decoding should return original"
    assert decode_shift(encode_shift("xyz")) == "xyz", "Test case 3 failed: encoding and then decoding should return original"
    assert decode_shift(encode_shift("")) == "", "Test case 4 failed: encoding and then decoding should return original with empty string"
    assert decode_shift(encode_shift("sphinxofblackquartzjudge")) == "sphinxofblackquartzjudge", "Test case 5 failed: encoding and then decoding long text should return original"

if __name__ == "__main__": # pragma: no cover
    test_decode_shift()
