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
    global has_close_elements, List
    
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False, "Test case 1 failed"
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True, "Test case 2 failed"
    assert has_close_elements([5.6, 7.8, 9.1, 1.2], 2.0) == False, "Test case 3 failed"
    assert has_close_elements([0.1, 0.2, 0.3, 0.4], 0.01) == False, "Test case 4 failed"
    
if __name__ == "__main__": # pragma: no cover
    test_has_close_elements()
