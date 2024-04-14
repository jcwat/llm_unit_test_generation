"""
Checks if given string is a palindrome
>>> is_palindrome('')
True
>>> is_palindrome('aba')
True
>>> is_palindrome('aaaaa')
True
>>> is_palindrome('zbcd')
False
"""


def is_palindrome(text: str):
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

def test_is_palindrome(): # pragma: no cover
    global is_palindrome
    assert is_palindrome("racecar") == True, "Test case 1 failed"
    assert is_palindrome("hello") == False, "Test case 2 failed"
    assert is_palindrome("noon") == True, "Test case 3 failed"
    assert is_palindrome("12321") == True, "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_is_palindrome()
