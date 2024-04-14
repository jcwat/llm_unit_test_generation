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
    global test_is_prime, is_prime
    assert is_prime(6) is False, "Test case 1 failed"
    assert is_prime(101) is True, "Test case 2 failed"
    assert is_prime(11) is True, "Test case 3 failed"
    assert is_prime(13441) is True, "Test case 4 failed"
    assert is_prime(61) is True, "Test case 5 failed"
    assert is_prime(4) is False, "Test case 6 failed"
    assert is_prime(1) is False, "Test case 7 failed"

if __name__ == "__main__": # pragma: no cover
    test_is_prime()
