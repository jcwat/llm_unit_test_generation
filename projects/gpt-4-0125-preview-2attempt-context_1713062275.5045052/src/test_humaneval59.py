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
    global test_largest_prime_factor
    assert largest_prime_factor(13195) == 29, "Test case 1 failed for input 13195"
    assert largest_prime_factor(2048) == 2, "Test case 2 failed for input 2048"
    assert largest_prime_factor(10) == 5, "Test case 3 failed for input 10"

if __name__ == "__main__": # pragma: no cover
    test_largest_prime_factor()
