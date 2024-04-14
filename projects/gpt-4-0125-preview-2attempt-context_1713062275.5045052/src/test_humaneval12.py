""" Out of list of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in case the input list is empty.
>>> longest([])

>>> longest(['a', 'b', 'c'])
'a'
>>> longest(['a', 'bb', 'ccc'])
'ccc'
"""
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s

def test_longest(): # pragma: no cover
    global test_longest, List, Optional
    # Test with empty list
    assert longest([]) is None, "Test case with empty list failed"
    
    # Test with single character strings
    assert longest(['a', 'b', 'c']) == 'a', "Test case with single character strings failed"
    
    # Test with multiple length strings
    assert longest(['a', 'bb', 'ccc']) == 'ccc', "Test case with multiple length strings failed"
    
    # Test with equal length longest strings, should return the first one
    assert longest(['aaa', 'bbb', 'cc']) == 'aaa', "Test case with equal length longest strings failed"
    
    # Test with mixed length strings
    assert longest(['hello', 'world', '!', 'python programming']) == 'python programming', "Test case with mixed length strings failed"

if __name__ == "__main__": # pragma: no cover
    test_longest()
