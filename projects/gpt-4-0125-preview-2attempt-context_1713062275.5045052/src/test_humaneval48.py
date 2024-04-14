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
    global test_is_palindrome, is_palindrome
    assert is_palindrome('') == True, "Test case 1 failed: empty string should be a palindrome"
    assert is_palindrome('aba') == True, "Test case 2 failed: 'aba' should be a palindrome"
    assert is_palindrome('aaaaa') == True, "Test case 3 failed: 'aaaaa' should be a palindrome"
    assert is_palindrome('zbcd') == False, "Test case 4 failed: 'zbcd' should not be a palindrome"
    assert is_palindrome('a') == True, "Test case 5 failed: single character should be considered a palindrome"
    assert is_palindrome('abba') == True, "Test case 6 failed: 'abba' should be a palindrome"
    assert is_palindrome('abcba') == True, "Test case 7 failed: 'abcba' should be a palindrome"
    assert is_palindrome('abcde') == False, "Test case 8 failed: 'abcde' should not be a palindrome"

if __name__ == "__main__": # pragma: no cover
    test_is_palindrome()
