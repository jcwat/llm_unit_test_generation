""" Given list of numbers (of at least two elements), apply a linear transform to that list,
such that the smallest number will become 0 and the largest will become 1
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
"""
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]

def test_rescale_to_unit(): # pragma: no cover
    global rescale_to_unit, List
    numbers = [1, 2, 3, 4, 5]
    expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(numbers) == expected_result, "Test case 1 failed"

    numbers = [5, 4, 3, 2, 1]
    expected_result = [1.0, 0.75, 0.5, 0.25, 0.0]
    assert rescale_to_unit(numbers) == expected_result, "Test case 2 failed"

    numbers = [10, 20, 15, 25]
    expected_result = [0.0, 0.5, 0.25, 1.0]
    assert rescale_to_unit(numbers) == expected_result, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_rescale_to_unit()
