""" For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
Empty sum should be equal to 0 and empty product should be equal to 1.
>>> sum_product([])
(0, 1)
>>> sum_product([1, 2, 3, 4])
(10, 24)
"""
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

def test_sum_product(): # pragma: no cover
    global sum_product, math
    assert sum_product([]) == (0, 1), "Test case 1 failed"
    assert sum_product([1, 2, 3, 4]) == (10, 24), "Test case 2 failed"
    assert sum_product([-1, 1]) == (0, -1), "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_sum_product()
