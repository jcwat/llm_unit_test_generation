""" From a list of integers, remove all elements that occur more than once.
Keep order of elements left the same as in the input.
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
"""
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]

def test_remove_duplicates(): # pragma: no cover
    global remove_duplicates, collections
    
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4], "Test case 1 failed"
    assert remove_duplicates([1, 2, 2, 2, 3, 4, 4, 5]) == [1, 3, 5], "Test case 2 failed"
    assert remove_duplicates([1, 1, 1, 1, 1]) == [], "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_remove_duplicates()
