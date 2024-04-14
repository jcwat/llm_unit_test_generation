""" Return a greatest common divisor of two integers a and b
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
"""


def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def test_greatest_common_divisor(): # pragma: no cover
    global greatest_common_divisor
    assert greatest_common_divisor(12, 8) == 4, "Test case 1 failed"
    assert greatest_common_divisor(17, 5) == 1, "Test case 2 failed"
    assert greatest_common_divisor(50, 20) == 10, "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_greatest_common_divisor()
