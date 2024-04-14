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
    global mean_absolute_deviation
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-5, "Test case 1 failed"
    assert abs(mean_absolute_deviation([1, 1, 1, 1]) - 0) < 1e-5, "Test case 2 failed"
    assert abs(mean_absolute_deviation([-1.5, 0.0, 1.5, 3.0]) - 1.5) < 1e-5, "Test case 3 failed"
    assert abs(mean_absolute_deviation([-2, -1, 0, 1, 2]) - 1.2) < 1e-5, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_mean_absolute_deviation()
