from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]

def test_remove_duplicates(): # pragma: no cover
    assert  remove_duplicates([]) == []
    assert  remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert  remove_duplicates([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]

