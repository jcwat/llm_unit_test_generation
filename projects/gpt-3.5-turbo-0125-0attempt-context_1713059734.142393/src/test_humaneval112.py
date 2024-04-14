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

    assert reverse_delete("abcde", "ae") == ('bcd', False), "Test case 1 failed"
    assert reverse_delete("abcdef", "b") == ('acdef', False), "Test case 2 failed"
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True), "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_reverse_delete()
