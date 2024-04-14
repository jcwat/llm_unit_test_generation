

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a

def test_greatest_common_divisor(): # pragma: no cover
    assert  greatest_common_divisor(3, 7) == 1
    assert  greatest_common_divisor(10, 15) == 5
    assert  greatest_common_divisor(49, 14) == 7
    assert  greatest_common_divisor(144, 60) == 12

