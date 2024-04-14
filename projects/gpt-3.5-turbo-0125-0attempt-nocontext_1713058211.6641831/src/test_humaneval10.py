""" Find the shortest palindrome that begins with a supplied string.
Algorithm idea is simple:
- Find the longest postfix of supplied string that is a palindrome.
- Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
>>> make_palindrome('')
''
>>> make_palindrome('cat')
'catac'
>>> make_palindrome('cata')
'catac'
"""


def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]

def test_is_palindrome(): # pragma: no cover
    global is_palindrome
    assert is_palindrome("racecar") == True, "Test case 1 failed"
    assert is_palindrome("hello") == False, "Test case 2 failed"
    assert is_palindrome("hannah") == True, "Test case 3 failed"
    
def test_make_palindrome():
    global make_palindrome, is_palindrome
    assert make_palindrome("abc") == "abccba", "Test case 1 failed"
    assert make_palindrome("ab") == "aba", "Test case 2 failed"
    assert make_palindrome("radar") == "radar", "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_is_palindrome()
    test_make_palindrome()
