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
    assert strlen("hello") == 5, "Test case 1 failed"
    assert strlen("") == 0, "Test case 2 failed"
    assert strlen("123456789") == 9, "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_strlen()
