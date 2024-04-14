""" From a supplied list of numbers (of length at least two) select and return two that are the closest to each
other and return them in order (smaller number, larger number).
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
(2.0, 2.2)
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
(2.0, 2.0)
"""
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair

def test_find_closest_elements(): # pragma: no cover
    global find_closest_elements, List, Tuple

    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2), "Test case 1 failed"
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0), "Test case 2 failed"
    assert find_closest_elements([10.5, 20.3, 30.1, 40.6, 50.2, 21.8]) == (20.3, 21.8), "Test case 3 failed"
    assert find_closest_elements([-5.0, 0.0, 10.0, 15.0, -3.0, 4.0]) == (-3.0, 0.0), "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_find_closest_elements()
