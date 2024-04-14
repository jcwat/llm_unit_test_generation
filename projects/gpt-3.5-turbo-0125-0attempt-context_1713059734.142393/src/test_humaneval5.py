""" Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
>>> intersperse([], 4)
[]
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
"""
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result

def test_intersperse(): # pragma: no cover
    global intersperse, List
    assert intersperse([], 4) == [], "Test case 1 failed"
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3], "Test case 2 failed"
    assert intersperse([5, 8, 2, 6], 0) == [5, 0, 8, 0, 2, 0, 6], "Test case 3 failed"
    assert intersperse([9], 1) == [9], "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_intersperse()
