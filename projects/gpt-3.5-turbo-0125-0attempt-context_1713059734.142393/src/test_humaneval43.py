"""
pairs_sum_to_zero takes a list of integers as an input.
it returns True if there are two distinct elements in the list that
sum to zero, and False otherwise.
>>> pairs_sum_to_zero([1, 3, 5, 0])
False
>>> pairs_sum_to_zero([1, 3, -2, 1])
False
>>> pairs_sum_to_zero([1, 2, 3, 7])
False
>>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
True
>>> pairs_sum_to_zero([1])
False
"""


def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

def test_pairs_sum_to_zero(): # pragma: no cover
    global pairs_sum_to_zero

    assert pairs_sum_to_zero([1, 3, 5, 0]) == False, "Test case 1 failed"
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False, "Test case 2 failed"
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False, "Test case 3 failed"
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True, "Test case 4 failed"
    assert pairs_sum_to_zero([1]) == False, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_pairs_sum_to_zero()
