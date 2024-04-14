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
    global test_is_palindrome
    assert is_palindrome('') == True, "Empty string should return True"
    assert is_palindrome('aba') == True, "String 'aba' should return True"
    assert is_palindrome('aaaaa') == True, "String 'aaaaa' should return True"
    assert is_palindrome('zbcd') == False, "String 'zbcd' should return False"
    assert is_palindrome('a') == True, "Single character string should return True"
    assert is_palindrome('abba') == True, "Even length palindrome 'abba' should return True"
    assert is_palindrome('abcddcba') == True, "Even length palindrome 'abcddcba' should return True"
    assert is_palindrome('abcd') == False, "String 'abcd' should return False"

if __name__ == "__main__": # pragma: no cover
    test_is_palindrome()
