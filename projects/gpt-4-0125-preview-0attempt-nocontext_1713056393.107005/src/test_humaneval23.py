""" Return length of given string
>>> strlen('')
0
>>> strlen('abc')
3
"""


def strlen(string: str) -> int:
    return len(string)

def test_strlen(): # pragma: no cover
    global test_strlen
    assert strlen('') == 0, "Test case 1 (empty string) failed"
    assert strlen('hello') == 5, "Test case 2 ('hello') failed"
    assert strlen('12345') == 5, "Test case 3 ('12345') failed"
    assert strlen(' ') == 1, "Test case 4 (single space) failed"
    assert strlen('hello world') == 11, "Test case 5 ('hello world') failed"

if __name__ == "__main__": # pragma: no cover
    test_strlen()
