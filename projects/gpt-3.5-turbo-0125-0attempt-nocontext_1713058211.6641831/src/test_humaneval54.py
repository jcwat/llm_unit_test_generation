"""
Check if two words have the same characters.
>>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
True
>>> same_chars('abcd', 'dddddddabc')
True
>>> same_chars('dddddddabc', 'abcd')
True
>>> same_chars('eabcd', 'dddddddabc')
False
>>> same_chars('abcd', 'dddddddabce')
False
>>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
False
"""


def same_chars(s0: str, s1: str):
    return set(s0) == set(s1)

def test_same_chars(): # pragma: no cover
    global same_chars
    assert same_chars("abc", "cba") == True, "Test case 1 failed"
    assert same_chars("hello", "world") == False, "Test case 2 failed"
    assert same_chars("", "") == True, "Test case 3 failed"
    assert same_chars("123", "321") == True, "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_same_chars()
