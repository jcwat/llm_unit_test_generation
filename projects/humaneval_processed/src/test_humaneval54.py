

def same_chars(s0: str, s1: str):
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
    return set(s0) == set(s1)

def test_same_chars(): # pragma: no cover
    assert  same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert  same_chars('abcd', 'dddddddabc') == True
    assert  same_chars('dddddddabc', 'abcd') == True
    assert  same_chars('eabcd', 'dddddddabc') == False
    assert  same_chars('abcd', 'dddddddabcf') == False
    assert  same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    assert  same_chars('aabb', 'aaccc') == False


