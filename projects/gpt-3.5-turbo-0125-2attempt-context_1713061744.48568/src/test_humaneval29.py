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
    global filter_by_prefix, List
    
    # Test case 1: Empty input list
    assert filter_by_prefix([], 'a') == [], "Test case 1 failed"
    
    # Test case 2: Non-empty input list
    input_list = ['abc', 'bcd', 'cde', 'array']
    assert filter_by_prefix(input_list, 'a') == ['abc', 'array'], "Test case 2 failed"

if __name__ == "__main__": # pragma: no cover
    test_filter_by_prefix()
