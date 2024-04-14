""" For a given number n, find the largest number that divides n evenly, smaller than n
>>> largest_divisor(15)
5
"""


def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        if n % i == 0:
            return i

def test_largest_divisor(): # pragma: no cover
    global largest_divisor, math
    assert largest_divisor(15) == 5, "Test case 1 failed"
    assert largest_divisor(10) == 5, "Test case 2 failed"
    assert largest_divisor(7) == 1, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_largest_divisor()
