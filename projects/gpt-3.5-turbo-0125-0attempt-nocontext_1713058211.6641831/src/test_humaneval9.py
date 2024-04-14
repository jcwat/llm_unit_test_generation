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
    global rolling_max, List, Tuple

    # Test case 1: list with positive numbers
    numbers = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert rolling_max(numbers) == expected, "Test case 1 failed"

    # Test case 2: list with negative numbers
    numbers = [-1, -2, -3, -4, -5]
    expected = [-1, -1, -1, -1, -1]
    assert rolling_max(numbers) == expected, "Test case 2 failed"

    # Test case 3: list with mixed positive and negative numbers
    numbers = [1, -2, 3, -4, 5]
    expected = [1, 1, 3, 3, 5]
    assert rolling_max(numbers) == expected, "Test case 3 failed"

    # Test case 4: list with repeated numbers
    numbers = [2, 2, 2, 2, 2]
    expected = [2, 2, 2, 2, 2]
    assert rolling_max(numbers) == expected, "Test case 4 failed"

    # Test case 5: empty list
    numbers = []
    expected = []
    assert rolling_max(numbers) == expected, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_rolling_max()
