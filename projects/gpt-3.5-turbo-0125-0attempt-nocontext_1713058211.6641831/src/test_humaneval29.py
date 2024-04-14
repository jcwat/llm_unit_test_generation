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
    global test_filter_by_prefix, List
    
    strings = ["apple", "banana", "cherry", "orange"]
    
    # Test case 1: prefix matches with some strings
    prefix = "a"
    expected_output_1 = ["apple"]
    assert filter_by_prefix(strings, prefix) == expected_output_1, "Test case 1 failed"
    
    # Test case 2: prefix does not match with any strings
    prefix = "d"
    expected_output_2 = []
    assert filter_by_prefix(strings, prefix) == expected_output_2, "Test case 2 failed"
    
    # Test case 3: prefix matches with all strings
    prefix = ""
    expected_output_3 = ["apple", "banana", "cherry", "orange"]
    assert filter_by_prefix(strings, prefix) == expected_output_3, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_filter_by_prefix()
