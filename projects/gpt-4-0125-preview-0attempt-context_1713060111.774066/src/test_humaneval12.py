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
    global test_longest
    assert longest([]) is None, "Test case with empty list failed"
    assert longest(['a', 'b', 'c']) == 'a', "Test case with single character strings failed"
    assert longest(['a', 'bb', 'ccc']) == 'ccc', "Test case with progressively longer strings failed"
    assert longest(['hello', 'world', 'python', 'is', 'awesome']) == 'awesome', "Test case with mixed length strings failed"
    assert longest(['equal', 'length', 'words']) == 'equal', "Test case with all strings of equal length failed"

if __name__ == "__main__": # pragma: no cover
    test_longest()
