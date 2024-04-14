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
    global decode_shift, encode_shift
    # Test case with a single word
    original = "hello"
    encoded = encode_shift(original)
    decoded = decode_shift(encoded)
    assert original == decoded, f"Single word test failed. Expected {original}, got {decoded}."

    # Test case with empty string
    original = ""
    encoded = encode_shift(original)
    decoded = decode_shift(encoded)
    assert original == decoded, "Empty string test failed."

    # Test case with full alphabet
    original = "abcdefghijklmnopqrstuvwxyz"
    encoded = encode_shift(original)
    decoded = decode_shift(encoded)
    assert original == decoded, "Full alphabet test failed."

    # Test case with a word needing wrapping
    original = "xyz"
    encoded = encode_shift(original)
    decoded = decode_shift(encoded)
    assert original == decoded, f"Wrapping test failed. Expected {original}, got {decoded}."

if __name__ == "__main__": # pragma: no cover
    test_decode_shift()
