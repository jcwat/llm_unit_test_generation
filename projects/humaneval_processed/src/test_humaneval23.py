

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

def test_strlen(): # pragma: no cover
    assert  strlen('') == 0
    assert  strlen('x') == 1
    assert  strlen('asdasnakj') == 9

