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
    global rescale_to_unit
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0], "Test case 1 failed"
    assert rescale_to_unit([10, 20, 30]) == [0.0, 0.5, 1.0], "Test case 2 failed"
    assert rescale_to_unit([-5.0, 0.0, 5.0, 10.0]) == [0.0, 0.3333333333333333, 0.6666666666666666, 1.0], "Test case 3 failed"
    assert rescale_to_unit([100, 1000]) == [0.0, 1.0], "Test case 4 failed"
    # Check for tolerance
    result = rescale_to_unit([1.00001, 2.00001, 3.00001])
    expected = [0.0, 0.5, 1.0]
    assert all(abs(a-b) < 1e-5 for a, b in zip(result, expected)), "Test case 5 failed: tolerance issue"
    
if __name__ == "__main__": # pragma: no cover
    test_rescale_to_unit()
