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
    assert remove_vowels('') == '', "Test case 1 failed: Handling empty string"
    assert remove_vowels('abcdef\nghijklm') == 'bcdf\nghjklm', "Test case 2 failed"
    assert remove_vowels('abcdef') == 'bcdf', "Test case 3 failed"
    assert remove_vowels('aaaaa') == '', "Test case 4 failed: All vowels"
    assert remove_vowels('aaBAA') == 'B', "Test case 5 failed: Case sensitivity"
    assert remove_vowels('zbcd') == 'zbcd', "Test case 6 failed: No vowels present"

if __name__ == "__main__": # pragma: no cover
    test_remove_vowels()
