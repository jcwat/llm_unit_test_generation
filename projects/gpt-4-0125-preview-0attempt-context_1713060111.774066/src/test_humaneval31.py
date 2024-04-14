"""Return true if a given number is prime, and false otherwise.
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
"""


def is_prime(n):
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True

def test_is_prime(): # pragma: no cover
    global test_is_prime, math
    assert not is_prime(6), "Test case 1 (6 is not prime) failed"
    assert is_prime(101), "Test case 2 (101 is prime) failed"
    assert is_prime(11), "Test case 3 (11 is prime) failed"
    assert is_prime(13441), "Test case 4 (13441 is prime) failed"
    assert is_prime(61), "Test case 5 (61 is prime) failed"
    assert not is_prime(4), "Test case 6 (4 is not prime) failed"
    assert not is_prime(1), "Test case 7 (1 is not considered prime) failed"

if __name__ == "__main__": # pragma: no cover
    test_is_prime()
