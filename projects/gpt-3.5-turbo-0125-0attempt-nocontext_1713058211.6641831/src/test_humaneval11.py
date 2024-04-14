""" Input are two strings a and b consisting only of 1s and 0s.
Perform binary XOR on these inputs and return result also as a string.
>>> string_xor('010', '110')
'100'
"""
from typing import List


def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

def test_string_xor(): # pragma: no cover
    global test_string_xor, List

    assert string_xor("1100", "1010") == "0110", "Test case 1 failed"
    assert string_xor("1111", "0000") == "1111", "Test case 2 failed"
    assert string_xor("101010", "010101") == "111111", "Test case 3 failed"
    
if __name__ == "__main__": # pragma: no cover
    test_string_xor()
