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
    global filter_by_substring
    
    # Test cases
    assert filter_by_substring([], 'a') == [], "Test case 1 failed"
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array'], "Test case 2 failed"
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z') == [], "Test case 3 failed"
    assert filter_by_substring(['xyz', 'def', 'ghi', 'jkl'], 'z') == ['xyz'], "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_filter_by_substring()
