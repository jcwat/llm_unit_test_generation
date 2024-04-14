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
    assert is_palindrome('') == True, "Test case for empty string failed"
    assert is_palindrome('aba') == True, "Test case for 'aba' failed"
    assert is_palindrome('aaaaa') == True, "Test case for 'aaaaa' failed"
    assert is_palindrome('zbcd') == False, "Test case for 'zbcd' failed"
    assert is_palindrome('abba') == True, "Test case for 'abba' failed"
    assert is_palindrome('Aba') == False, "Test case for case sensitive 'Aba' failed"
    assert is_palindrome('a man a plan a canal panama') == False, "Test with spaces failed"
    assert is_palindrome('12321') == True, "Test case for numeric '12321' failed"
    assert is_palindrome('12345') == False, "Test case for numeric '12345' failed"

if __name__ == "__main__": # pragma: no cover
    test_is_palindrome()
