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

def test_make_palindrome(): # pragma: no cover
    global test_make_palindrome, is_palindrome, make_palindrome

    assert make_palindrome('') == '', "Test case 1 failed"
    assert make_palindrome('cat') == 'catac', "Test case 2 failed"
    assert make_palindrome('cata') == 'catac', "Test case 3 failed"
    assert make_palindrome('abacdefg') == 'abacdegfdcaba', "Test case 4 failed"
    assert make_palindrome('radar') == 'radar', "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_make_palindrome()
