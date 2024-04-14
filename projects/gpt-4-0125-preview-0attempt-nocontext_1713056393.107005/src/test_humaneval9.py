""" From a given list of integers, generate a list of rolling maximum element found until given moment
in the sequence.
>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]
"""
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result

def test_rolling_max(): # pragma: no cover
    global test_rolling_max, List, Tuple
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4], "Test case 1 failed"
    assert rolling_max([5, 4, 2, 1]) == [5, 5, 5, 5], "Test case 2 failed"
    assert rolling_max([-1, -3, -2, -5]) == [-1, -1, -1, -1], "Test case 3 failed"
    assert rolling_max([]) == [], "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_rolling_max()
