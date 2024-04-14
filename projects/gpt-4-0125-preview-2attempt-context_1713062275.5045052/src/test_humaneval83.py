"""
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
"""

def starts_one_ends(n):
    if n == 1: return 1
    return 18 * (10 ** (n - 2))

def test_starts_one_ends(): # pragma: no cover
    global starts_one_ends
    # Test cases for different values of n
    assert starts_one_ends(1) == 1, "Test case 1 failed: starts_one_ends(1) should be 1"
    assert starts_one_ends(2) == 18, "Test case 2 failed: starts_one_ends(2) should be 18"
    assert abs(starts_one_ends(3) - 180) <= 1e-5, "Test case 3 failed: starts_one_ends(3) should be approximately 180"
    assert abs(starts_one_ends(4) - 1800) <= 1e-5, "Test case 4 failed: starts_one_ends(4) should be approximately 1800"
    assert abs(starts_one_ends(5) - 18000) <= 1e-5, "Test case 5 failed: starts_one_ends(5) should be approximately 18000"

if __name__ == "__main__": # pragma: no cover
    test_starts_one_ends()
