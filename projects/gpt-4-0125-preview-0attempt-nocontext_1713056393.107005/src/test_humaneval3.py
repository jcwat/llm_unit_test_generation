""" You're given a list of deposit and withdrawal operations on a bank account that starts with
zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
at that point function should return True. Otherwise it should return False.
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
"""
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False

def test_below_zero(): # pragma: no cover
    global test_below_zero, List
    assert below_zero([1, 2, 3]) == False, "Test case 1 failed: Positive balance should not return True"
    assert below_zero([1, 2, -4, 5]) == True, "Test case 2 failed: Negative balance at some point should return True"
    assert below_zero([-1, -2, 3, 4]) == True, "Test case 3 failed: Immediate negative balance should return True"
    assert below_zero([10, -2, -8, 1]) == False, "Test case 4 failed: Never goes negative should not return True"
    assert below_zero([]) == False, "Test case 5 failed: Empty list should not return True"

if __name__ == "__main__": # pragma: no cover
    test_below_zero()
