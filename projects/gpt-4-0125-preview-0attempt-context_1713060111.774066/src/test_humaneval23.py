""" Return length of given string
>>> strlen('')
0
>>> strlen('abc')
3
"""


def strlen(string: str) -> int:
    return len(string)

def test_strlen(): # pragma: no cover
    global test_strlen, strlen
    assert strlen('') == 0, "Test case 1 failed"
    assert strlen('abc') == 3, "Test case 2 failed"
    assert strlen('hello world') == 11, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_strlen()
