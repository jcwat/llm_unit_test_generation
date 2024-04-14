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
    # Test case 1
    result = reverse_delete("abcde", "ae")
    expected = ('bcd', False)
    assert result == expected, f"Test case 1 failed, expected {expected}, got {result}"
    # Test case 2
    result = reverse_delete("abcdef", "b")
    expected = ('acdef', False)
    assert result == expected, f"Test case 2 failed, expected {expected}, got {result}"
    # Test case 3
    result = reverse_delete("abcdedcba", "ab")
    expected = ('cdedc', True)
    assert result == expected, f"Test case 3 failed, expected {expected}, got {result}"
    # Test case 4: No deletion
    result = reverse_delete("racecar", "")
    expected = ('racecar', True)
    assert result == expected, f"Test case 4 failed, expected {expected}, got {result}"
    # Test case 5: Delete all
    result = reverse_delete("hello", "hello")
    expected = ('', True)
    assert result == expected, f"Test case 5 failed, expected {expected}, got {result}"

if __name__ == "__main__": # pragma: no cover
    test_reverse_delete()
