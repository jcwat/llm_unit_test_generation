""" Filter an input list of strings only for ones that contain given substring
>>> filter_by_substring([], 'a')
[]
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
"""
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

def test_filter_by_substring(): # pragma: no cover
    global test_filter_by_substring, List
    assert filter_by_substring([], 'a') == [], "Test case 1 failed: should handle empty list"
    assert filter_by_substring(['abc', 'def', 'ghi'], 'a') == ['abc'], "Test case 2 failed: single match"
    assert filter_by_substring(['abc', 'bac', 'cab'], 'a') == ['abc', 'bac', 'cab'], "Test case 3 failed: all match"
    assert filter_by_substring(['def', 'ghi', 'jkl'], 'a') == [], "Test case 4 failed: no match"
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array'], "Test case 5 failed: multiple matches"

if __name__ == "__main__": # pragma: no cover
    test_filter_by_substring()
