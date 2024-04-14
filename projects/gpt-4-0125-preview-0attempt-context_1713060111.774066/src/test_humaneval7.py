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
    assert filter_by_substring([], 'a') == [], "Test case 1 failed: empty list should return an empty list"
    assert filter_by_substring(['abc', 'bacd', 'cde'], 'a') == ['abc', 'bacd'], "Test case 2 failed: did not filter correctly for substring 'a'"
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array'], "Test case 3 failed: did not filter correctly for substring 'a' with more items"
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z') == [], "Test case 4 failed: should return an empty list when no items contain the substring"
    assert filter_by_substring(['hello', 'world', 'this', 'is', 'python'], 'is') == ['this', 'is'], "Test case 5 failed: did not filter correctly for substring 'is'"

if __name__ == "__main__": # pragma: no cover
    test_filter_by_substring()
