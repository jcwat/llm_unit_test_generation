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
    global longest, List, Optional
    
    assert longest([]) is None, "Test case 1 failed"
    assert longest(['a', 'b', 'c']) == 'a', "Test case 2 failed"
    assert longest(['a', 'bb', 'ccc']) == 'ccc', "Test case 3 failed"
    assert longest(['aa', 'bb', 'cc']) == 'aa', "Test case 4 failed"
    assert longest(['aa', 'bb', 'ccc', 'dddd']) == 'dddd', "Test case 5 failed"
if __name__ == "__main__": # pragma: no cover
    test_longest()
