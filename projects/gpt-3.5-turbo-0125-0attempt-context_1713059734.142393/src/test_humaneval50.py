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
    global test_decode_shift
    assert decode_shift("afpq") == "vaky", "Test case 1 failed"
    assert decode_shift("gur dhvpx oebja sbk whzcf bire gur ynml qbt") == "the quick brown fox jumps over the lazy dog", "Test case 2 failed"
    assert decode_shift("rqhfxphq") == "mlemksml", "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_decode_shift()
