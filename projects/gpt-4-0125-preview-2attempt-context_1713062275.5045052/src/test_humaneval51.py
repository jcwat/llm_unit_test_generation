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
    assert remove_vowels('') == '', "Test case with empty string failed"
    assert remove_vowels('abcdef\nghijklm') == 'bcdf\nghjklm', "Test case with newline character failed"
    assert remove_vowels('abcdef') == 'bcdf', "Test case with mixed vowels failed"
    assert remove_vowels('aaaaa') == '', "Test case with only vowels failed"
    assert remove_vowels('aaBAA') == 'B', "Test case with mixed case vowels failed"
    assert remove_vowels('zbcd') == 'zbcd', "Test case with no vowels failed"

if __name__ == "__main__": # pragma: no cover
    test_remove_vowels()
