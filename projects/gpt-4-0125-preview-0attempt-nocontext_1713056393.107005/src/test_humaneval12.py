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
    assert longest(['a', 'bb', 'c']) == 'bb', "Test with one longest string failed"
    assert longest(['hello', 'world', 'python', 'code']) == 'python', "Test with one longest string among many failed"
    assert longest(['abc', 'def', 'ghi']) == 'abc', "Test with all same length strings failed"
    assert longest([]) is None, "Test with empty list failed"
    assert longest(['a']) == 'a', "Test with single one-character string failed"
    assert longest(['aa', 'b', 'cc']) == 'aa', "Test with multiple strings of same max length failed"

if __name__ == "__main__": # pragma: no cover
    test_longest()
