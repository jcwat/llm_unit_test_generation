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
    global test_filter_integers, List, Any
    
    assert filter_integers([1, 'a', 2, 'b', 3]) == [1, 2, 3], "Test case 1 failed"
    assert filter_integers([4, 5, 6, 'c', 'd']) == [4, 5, 6], "Test case 2 failed"
    assert filter_integers(['e', 'f', 'g']) == [], "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_filter_integers()
