""" Filter given list of any python values only for integers
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
"""
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    return [x for x in values if isinstance(x, int)]

def test_filter_integers(): # pragma: no cover
    global test_filter_integers, filter_integers
    assert filter_integers(['a', 3.14, 5]) == [5], "Test case 1 failed: should filter out non-integer values"
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3], "Test case 2 failed: should return list of integers"
    assert filter_integers([]) == [], "Test case 3 failed: empty list should return empty list"
    assert filter_integers(['a', 'b', 'c']) == [], "Test case 4 failed: list with no integers should return empty list"
    assert filter_integers([True, False, 100.0, 1]) == [1], "Test case 5 failed: Booleans and float should not be considered as integers"

if __name__ == "__main__": # pragma: no cover
    test_filter_integers()
