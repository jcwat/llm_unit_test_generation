"""
Given a positive integer n, return a tuple that has the number of even and odd
integer palindromes that fall within the range(1, n), inclusive.

Example 1:

Input: 3
Output: (1, 2)
Explanation:
Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

Example 2:

Input: 12
Output: (4, 6)
Explanation:
Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

Note:
1. 1 <= n <= 10^3
2. returned tuple has the number of even and odd integer palindromes respectively.
"""

def even_odd_palindrome(n):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n+1):
        if i%2 == 1 and is_palindrome(i):
                odd_palindrome_count += 1
        elif i%2 == 0 and is_palindrome(i):
            even_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)

def test_even_odd_palindrome(): # pragma: no cover
    global even_odd_palindrome

    # Test case 1
    result = even_odd_palindrome(3)
    expected = (1, 2)
    assert result == expected, f"Test case 1 failed, expected {expected}, got {result}"

    # Test case 2
    result = even_odd_palindrome(12)
    expected = (4, 6)
    assert result == expected, f"Test case 2 failed, expected {expected}, got {result}"

    # Test case 3 (Edge case: minimum input)
    result = even_odd_palindrome(1)
    expected = (0, 1)
    assert result == expected, f"Test case 3 failed, expected {expected}, got {result}"

    # Test case 4 (Testing with a higher number)
    result = even_odd_palindrome(22)
    expected = (5, 9)  # Palindromes up to 22: 1-9, 11 (10 even (2, 4, 6, 8, 22) and 11 odd (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21))
    assert result == expected, f"Test case 4 failed, expected {expected}, got {result}"

if __name__ == "__main__": # pragma: no cover
    test_even_odd_palindrome()
