

def is_palindrome(text: str):
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
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

def test_is_palindrome(): # pragma: no cover
    assert  is_palindrome('') == True
    assert  is_palindrome('aba') == True
    assert  is_palindrome('aaaaa') == True
    assert  is_palindrome('zbcd') == False
    assert  is_palindrome('xywyx') == True
    assert  is_palindrome('xywyz') == False
    assert  is_palindrome('xywzx') == False


