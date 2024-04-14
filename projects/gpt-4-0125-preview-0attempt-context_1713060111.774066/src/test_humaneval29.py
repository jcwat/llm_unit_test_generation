""" Filter an input list of strings only for ones that start with a given prefix.
>>> filter_by_prefix([], 'a')
[]
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
"""
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

def test_filter_by_prefix(): # pragma: no cover
    global test_filter_by_prefix
    assert filter_by_prefix([], 'a') == [], "Test case 1 with empty list failed"
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array'], "Test case 2 with 'a' prefix failed"
    assert filter_by_prefix(['banana', 'apple', 'apricot', 'cherry'], 'ap') == ['apple', 'apricot'], "Test case 3 with 'ap' prefix failed"
    assert filter_by_prefix(['banana', 'apple', 'apricot', 'cherry'], 'z') == [], "Test case 4 with 'z' (no match) prefix failed"

if __name__ == "__main__": # pragma: no cover
    test_filter_by_prefix()
