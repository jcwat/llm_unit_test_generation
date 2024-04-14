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
    global test_rescale_to_unit, List
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0], "Test case 1 failed"
    assert rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0]) == [0.0, 0.25, 0.5, 0.75, 1.0], "Test case 2 failed"
    assert rescale_to_unit([100.0, 150.0]) == [0.0, 1.0], "Test case 3 failed"
    assert rescale_to_unit([-100.0, 0.0, 100.0]) == [0.0, 0.5, 1.0], "Test case 4 failed"
    # Test with numbers close to each other
    result = rescale_to_unit([1.00001, 1.00002, 1.00003])
    for i, expected in zip(result, [0.0, 0.5, 1.0]):
        assert abs(i - expected) <= 1e-5, f"Test case 5 failed at index {result.index(i)} with value {i}"

if __name__ == "__main__": # pragma: no cover
    test_rescale_to_unit()
