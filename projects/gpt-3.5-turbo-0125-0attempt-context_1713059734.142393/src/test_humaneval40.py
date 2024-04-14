"""
triples_sum_to_zero takes a list of integers as an input.
it returns True if there are three distinct elements in the list that
sum to zero, and False otherwise.

>>> triples_sum_to_zero([1, 3, 5, 0])
False
>>> triples_sum_to_zero([1, 3, -2, 1])
True
>>> triples_sum_to_zero([1, 2, 3, 7])
False
>>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
True
>>> triples_sum_to_zero([1])
False
"""


def triples_sum_to_zero(l: list):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

def test_triples_sum_to_zero(): # pragma: no cover
    global triples_sum_to_zero

    assert triples_sum_to_zero([1, 3, 5, 0]) == False, "Test case 1 failed"
    assert triples_sum_to_zero([1, 3, -2, 1]) == True, "Test case 2 failed"
    assert triples_sum_to_zero([1, 2, 3, 7]) == False, "Test case 3 failed"
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True, "Test case 4 failed"
    assert triples_sum_to_zero([1]) == False, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_triples_sum_to_zero()
