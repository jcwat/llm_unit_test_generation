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
    from typing import List

    assert filter_by_prefix([], 'a') == [], "Test case 1 failed"
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array'], "Test case 2 failed"
    assert filter_by_prefix(['hello', 'world'], 'w') == ['world'], "Test case 3 failed"
    assert filter_by_prefix(['test', 'toast', 'testing', 'posted'], 'te') == ['test', 'testing'], "Test case 4 failed"
    assert filter_by_prefix(['123', '234', '345'], '1') == ['123'], "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_filter_by_prefix()
