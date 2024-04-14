"""Circular shift the digits of the integer x, shift the digits right by shift
and return the result as a string.
If shift > number of digits, return digits reversed.
>>> circular_shift(12, 1)
"21"
>>> circular_shift(12, 2)
"12"
"""

def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

def test_circular_shift(): # pragma: no cover
    global test_circular_shift, circular_shift
    assert circular_shift(12345, 1) == "51234", "Test case 1 failed"
    assert circular_shift(12345, 2) == "45123", "Test case 2 failed"
    assert circular_shift(12345, 5) == "12345", "Test case 3 failed"
    assert circular_shift(12345, 6) == "54321", "Test case 4 failed"
    assert circular_shift(12345, 10) == "54321", "Test case 5 failed"
    assert circular_shift(1, 1) == "1", "Test case 6 failed"
    
if __name__ == "__main__": # pragma: no cover
    test_circular_shift()
