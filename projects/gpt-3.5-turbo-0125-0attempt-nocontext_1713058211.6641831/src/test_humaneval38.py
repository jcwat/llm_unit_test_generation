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

def test_encode_cyclic(): # pragma: no cover
    global encode_cyclic
    
    assert encode_cyclic("abc") == "bca", "Test case 1 failed"
    assert encode_cyclic("hello") == "elhol", "Test case 2 failed"
    assert encode_cyclic("1234567890") == "2314567890", "Test case 3 failed"

def test_decode_cyclic():
    global decode_cyclic

    assert decode_cyclic("bca") == "abc", "Test case 1 failed"
    assert decode_cyclic("elhol") == "hello", "Test case 2 failed"
    assert decode_cyclic("2314567890") == "1234567890", "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_encode_cyclic()
    test_decode_cyclic()
