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
    from typing import List

    result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5, f"Expected {e}, got {r} for input [1.0, 2.0, 3.0, 4.0, 5.0]"

    result = rescale_to_unit([10, 20])
    expected = [0.0, 1.0]
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5, f"Expected {e}, got {r} for input [10, 20]"

    result = rescale_to_unit([-1, 0, 1])
    expected = [0.0, 0.5, 1.0]
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5, f"Expected {e}, got {r} for input [-1, 0, 1]"

if __name__ == "__main__": # pragma: no cover
    test_rescale_to_unit()
