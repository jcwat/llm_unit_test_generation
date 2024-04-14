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

    assert even_odd_palindrome(3) == (1, 2), "Test case 1 failed"
    assert even_odd_palindrome(12) == (4, 6), "Test case 2 failed"
    assert even_odd_palindrome(1) == (0, 1), "Test case 3 failed"
    assert even_odd_palindrome(9) == (1, 4), "Test case 4 failed"
    assert even_odd_palindrome(20) == (9, 9), "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_even_odd_palindrome()
