"""Return the largest prime factor of n. Assume n > 1 and is not a prime.
>>> largest_prime_factor(13195)
29
>>> largest_prime_factor(2048)
2
"""


def largest_prime_factor(n: int):
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest

def test_largest_prime_factor(): # pragma: no cover
    global largest_prime_factor
    assert largest_prime_factor(13195) == 29, "Test case 1 failed"
    assert largest_prime_factor(2048) == 2, "Test case 2 failed"
    assert largest_prime_factor(7) == 7, "Test case 3 failed: 7 is prime itself"
    assert largest_prime_factor(49) == 7, "Test case 4 failed"
    assert largest_prime_factor(695) == 139, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_largest_prime_factor()
