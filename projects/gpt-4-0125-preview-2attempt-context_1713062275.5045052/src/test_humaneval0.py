""" Check if in given list of numbers, are any two numbers closer to each other than
given threshold.
>>> has_close_elements([1.0, 2.0, 3.0], 0.5)
False
>>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
True
"""
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False

def test_has_close_elements(): # pragma: no cover
    global test_has_close_elements, List
    # Test case with numbers far apart should return False
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False, "Test case 1 failed: Expected False as no elements are closer than 0.5"
    # Test case with numbers close enough should return True
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True, "Test case 2 failed: Expected True as there are elements closer than 0.3"
    # Test case with exactly the threshold distance should return False
    assert has_close_elements([10.0, 10.5, 11.0], 0.5) == False, "Test case 3 failed: Expected False as elements are exactly 0.5 apart, which is the threshold"
    # Test case with negative numbers and closer than threshold
    assert has_close_elements([-1.0, -1.1, 2.0], 0.15) == True, "Test case 4 failed: Expected True as there are close elements in negatives"
    # Test case with an empty list
    assert has_close_elements([], 1.0) == False, "Test case 5 failed: Expected False as there are no elements"

if __name__ == "__main__": # pragma: no cover
    test_has_close_elements()
