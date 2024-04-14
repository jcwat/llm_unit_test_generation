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
    global make_palindrome, is_palindrome
    
    assert make_palindrome('') == '', "Test case 1 failed: Should return an empty string for an empty input"
    assert make_palindrome('a') == 'a', "Test case 2 failed: Single character should return the same character"
    assert make_palindrome('cat') == 'catac', "Test case 3 failed: 'cat' should return 'catac'"
    assert make_palindrome('cata') == 'catac', "Test case 4 failed: 'cata' should return 'catac'"
    assert make_palindrome('race') == 'racecar', "Test case 5 failed: 'race' should return 'racecar'"
    assert make_palindrome('madam') == 'madam', "Test case 6 failed: 'madam' is already a palindrome"


if __name__ == "__main__": # pragma: no cover
    test_make_palindrome()
