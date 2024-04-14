"""
remove_vowels is a function that takes string and returns string without vowels.
>>> remove_vowels('')
''
>>> remove_vowels("abcdef\nghijklm")
'bcdf\nghjklm'
>>> remove_vowels('abcdef')
'bcdf'
>>> remove_vowels('aaaaa')
''
>>> remove_vowels('aaBAA')
'B'
>>> remove_vowels('zbcd')
'zbcd'
"""


def remove_vowels(text):
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])

def test_remove_vowels(): # pragma: no cover
    global remove_vowels
    assert remove_vowels('') == '', "Test case 1 failed: Should return empty string for empty input"
    assert remove_vowels('abcdef\nghijklm') == 'bcdf\nghjklm', "Test case 2 failed"
    assert remove_vowels('abcdef') == 'bcdf', "Test case 3 failed"
    assert remove_vowels('aaaaa') == '', "Test case 4 failed: Should handle all vowels"
    assert remove_vowels('aaBAA') == 'B', "Test case 5 failed: Should be case insensitive"
    assert remove_vowels('zbcd') == 'zbcd', "Test case 6 failed: Should return the same string if no vowels"
    
if __name__ == "__main__": # pragma: no cover
    test_remove_vowels()
