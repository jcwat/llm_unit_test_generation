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
    assert filter_integers(['a', 3.14, 5]) == [5], "Test case 1 failed"
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3], "Test case 2 failed"
    assert filter_integers([0, '0', False, True, None]) == [0], "Test case 3 failed"
    assert filter_integers([]) == [], "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_filter_integers()
