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
    global below_zero
    assert below_zero([1, 2, 3]) == False, "The balance should not go below zero."
    assert below_zero([1, 2, -4, 5]) == True, "The balance should go below zero."
    assert below_zero([-1, -2, -3]) == True, "The balance should go below zero from the start."
    assert below_zero([]) == False, "The balance should remain zero with no operations."
    assert below_zero([10, -5, -1, -4, 1]) == False, "The balance should not go below zero."
    assert below_zero([100, -150, 50]) == True, "The balance should go below zero."

if __name__ == "__main__": # pragma: no cover
    test_below_zero()
