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
    # Test empty list
    assert filter_by_substring([], 'a') == [], "Test case 1 failed: filtering an empty list should return an empty list."
    # Test list with no elements containing substring
    assert filter_by_substring(['bcd', 'def', 'ghi'], 'a') == [], "Test case 2 failed: list elements do not contain the substring."
    # Test list with some elements containing substring
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array'], "Test case 3 failed: only elements containing 'a' should be returned."
    # Test list with all elements containing substring
    assert filter_by_substring(['apple', 'amazing', 'alpha', 'array'], 'a') == ['apple', 'amazing', 'alpha', 'array'], "Test case 4 failed: all elements contain 'a'."

if __name__ == "__main__": # pragma: no cover
    test_filter_by_substring()
