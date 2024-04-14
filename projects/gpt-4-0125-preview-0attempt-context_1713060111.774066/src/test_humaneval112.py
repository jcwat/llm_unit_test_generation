"""Task
We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
then check if the result string is palindrome.
A string is called palindrome if it reads the same backward as forward.
You should return a tuple containing the result string and True/False for the check.
Example
For s = "abcde", c = "ae", the result should be ('bcd',False)
For s = "abcdef", c = "b"  the result should be ('acdef',False)
For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
"""

def reverse_delete(s,c):
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)

def test_reverse_delete(): # pragma: no cover
    global reverse_delete
    # Test cases
    result = reverse_delete("abcde", "ae")
    assert result == ("bcd", False), f"Test case 1 failed, expected ('bcd', False) but got {result}"

    result = reverse_delete("abcdef", "b")
    assert result == ("acdef", False), f"Test case 2 failed, expected ('acdef', False) but got {result}"

    result = reverse_delete("abcdedcba", "ab")
    assert result == ("cdedc", True), f"Test case 3 failed, expected ('cdedc', True) but got {result}"

    # Check empty strings
    result = reverse_delete("", "")
    assert result == ("", True), f"Test case 4 failed, expected ('', True) but got {result}"

    # Check same strings
    result = reverse_delete("a", "a")
    assert result == ("", True), f"Test case 5 failed, expected ('', True) but got {result}"

    # All characters will be deleted
    result = reverse_delete("aaa", "a")
    assert result == ("", True), f"Test case 6 failed, expected ('', True) but got {result}"

if __name__ == "__main__": # pragma: no cover
    test_reverse_delete()
