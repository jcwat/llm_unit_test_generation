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
    # Test cases from the documentation
    assert not has_close_elements([1.0, 2.0, 3.0], 0.5), "Test case 1 failed"
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3), "Test case 2 failed"
    
    # Additional test cases
    assert not has_close_elements([10.0, 20.0, 30.0, 40.0], 5.0), "Test case 3 failed"
    assert has_close_elements([1.002, 1.003, 2.0, 3.0], 0.002), "Test case 4 failed"
    assert not has_close_elements([], 1.0), "Test case 5 failed"  # Test with an empty list
    assert has_close_elements([0.0, 0.00001], 0.00002), "Test case 6 failed"
    assert not has_close_elements([1.0, 2.0], 0.99999), "Test case 7 failed"

if __name__ == "__main__": # pragma: no cover
    test_has_close_elements()
