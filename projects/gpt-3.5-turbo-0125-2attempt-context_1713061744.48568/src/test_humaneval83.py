"""
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
"""

def starts_one_ends(n):
    if n == 1: return 1
    return 18 * (10 ** (n - 2))

def test_starts_one_ends(): # pragma: no cover
    global starts_one_ends

    assert starts_one_ends(1) == 1, "Test case failed for n=1"
    assert starts_one_ends(2) == 18, "Test case failed for n=2"
    assert starts_one_ends(3) == 180, "Test case failed for n=3"
    assert starts_one_ends(4) == 1800, "Test case failed for n=4"
    assert starts_one_ends(5) == 18000, "Test case failed for n=5"

if __name__ == "__main__": # pragma: no cover
    test_starts_one_ends()
