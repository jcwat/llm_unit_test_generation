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
    assert longest(["apple", "banana", "grape"]) == "banana", "Test case 1 failed"
    assert longest(["kiwi", "pear", "orange", "melon"]) == "orange", "Test case 2 failed"
    assert longest(["cat", "dog", "elephant"]) == "elephant", "Test case 3 failed"
    assert longest([]) == None, "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_longest()
