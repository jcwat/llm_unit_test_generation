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
    global test_greatest_common_divisor
    assert greatest_common_divisor(3, 5) == 1, "Test case 1 failed for input (3, 5)"
    assert greatest_common_divisor(25, 15) == 5, "Test case 2 failed for input (25, 15)"
    assert greatest_common_divisor(10, 100) == 10, "Test case 3 failed for input (10, 100)"
    assert greatest_common_divisor(17, 17) == 17, "Test case 4 failed for input (17, 17)"
    assert greatest_common_divisor(0, 5) == 5, "Test case 5 failed for input (0, 5)"
    assert greatest_common_divisor(5, 0) == 5, "Test case 6 failed for input (5, 0)"
    assert greatest_common_divisor(0, 0) == 0, "Test case 7 failed for input (0, 0)"

if __name__ == "__main__": # pragma: no cover
    test_greatest_common_divisor()
