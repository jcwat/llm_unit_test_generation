""" For a given list of input numbers, calculate Mean Absolute Deviation
around the mean of this dataset.
Mean Absolute Deviation is the average absolute difference between each
element and a centerpoint (mean in this case):
MAD = average | x - x_mean |
>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
"""
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

def test_mean_absolute_deviation(): # pragma: no cover
    global mean_absolute_deviation, math

    assert math.isclose(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0, rel_tol=1e-5), "Test case 1 failed"
    assert math.isclose(mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]), 0.0, rel_tol=1e-5), "Test case 2 failed"
    assert math.isclose(mean_absolute_deviation([3.0, 3.0, 3.0, 3.0]), 0.0, rel_tol=1e-5), "Test case 3 failed"
    
if __name__ == "__main__": # pragma: no cover
    test_mean_absolute_deviation()
