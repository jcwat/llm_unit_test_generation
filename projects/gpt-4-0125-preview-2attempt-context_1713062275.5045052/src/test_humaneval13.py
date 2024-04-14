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
    assert greatest_common_divisor(3, 5) == 1, "Test case 1 failed: GCD of 3 and 5 expected to be 1"
    assert greatest_common_divisor(25, 15) == 5, "Test case 2 failed: GCD of 25 and 15 expected to be 5"
    assert greatest_common_divisor(100, 10) == 10, "Test case 3 failed: GCD of 100 and 10 expected to be 10"
    assert greatest_common_divisor(-25, 15) == 5, "Test case 4 failed: GCD of -25 and 15 expected to be 5"
    assert greatest_common_divisor(1, 0) == 1, "Test case 5 failed: GCD of 1 and 0 expected to be 1"
    assert greatest_common_divisor(0, 1) == 1, "Test case 6 failed: GCD of 0 and 1 expected to be 1"
    assert greatest_common_divisor(0, 0) == 0, "Test case 7 failed: GCD of 0 and 0 expected to be 0"

if __name__ == "__main__": # pragma: no cover
    test_greatest_common_divisor()
