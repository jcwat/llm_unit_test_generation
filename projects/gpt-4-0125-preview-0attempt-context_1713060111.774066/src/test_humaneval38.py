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
    
    # Test with a string of length exactly divisible by 3
    input_str = "abcdef"
    expected_output = "abcdef"
    assert decode_cyclic(input_str) == expected_output, f"Test case 1 failed: expected '{expected_output}', got '{decode_cyclic(input_str)}'"

    # Test with a string of length not divisible by 3
    input_str = "abcdefgh"
    expected_output = "abcdefgh"
    assert decode_cyclic(input_str) == expected_output, f"Test case 2 failed: expected '{expected_output}', got '{decode_cyclic(input_str)}'"

    # Test with a short string
    input_str = "ab"
    expected_output = "ab"
    assert decode_cyclic(input_str) == expected_output, f"Test case 3 failed: expected '{expected_output}', got '{decode_cyclic(input_str)}'"

    # Test with an empty string
    input_str = ""
    expected_output = ""
    assert decode_cyclic(input_str) == expected_output, f"Test case 4 failed: expected '{expected_output}', got '{decode_cyclic(input_str)}'"

    # Test with a string including spaces and punctuation
    input_str = "Hello, World!"
    expected_output = "Hello, World!"
    assert decode_cyclic(input_str) == expected_output, f"Test case 5 failed: expected '{expected_output}', got '{decode_cyclic(input_str)}'"
    
if __name__ == "__main__": # pragma: no cover
    test_decode_cyclic()
