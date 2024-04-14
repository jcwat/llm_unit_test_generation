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
    global test_greatest_common_divisor, math
    
    assert greatest_common_divisor(3, 5) == 1, "Test case 1 failed"
    assert greatest_common_divisor(25, 15) == 5, "Test case 2 failed"
    assert greatest_common_divisor(17, 23) == 1, "Test case 3 failed"
    assert greatest_common_divisor(18, 27) == 9, "Test case 4 failed"
    
if __name__ == "__main__": # pragma: no cover
    test_greatest_common_divisor()
