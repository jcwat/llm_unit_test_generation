"""
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
"""

def starts_one_ends(n):
    if n == 1: return 1
    return 18 * (10 ** (n - 2))

def test_starts_one_ends(): # pragma: no cover
    global starts_one_ends
    assert starts_one_ends(1) == 1, "Test with n=1 failed"
    assert starts_one_ends(2) == 18, "Test with n=2 failed"
    assert starts_one_ends(3) == 180, "Test with n=3 failed"
    assert abs(starts_one_ends(4) - 1800) <= 1e-5, "Test with n=4 failed"
    assert abs(starts_one_ends(5) - 18000) <= 1e-5, "Test with n=5 failed"

if __name__ == "__main__": # pragma: no cover
    test_starts_one_ends()
