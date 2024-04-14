""" Return a string containing space-delimited numbers starting from 0 upto n inclusive.
>>> string_sequence(0)
'0'
>>> string_sequence(5)
'0 1 2 3 4 5'
"""


def string_sequence(n: int) -> str:
    return ' '.join([str(x) for x in range(n + 1)])

def test_string_sequence(): # pragma: no cover
    global test_string_sequence
    assert string_sequence(0) == '0', "Test case 1 failed"
    assert string_sequence(1) == '0 1', "Test case 2 failed"
    assert string_sequence(5) == '0 1 2 3 4 5', "Test case 3 failed"
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10', "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_string_sequence()
