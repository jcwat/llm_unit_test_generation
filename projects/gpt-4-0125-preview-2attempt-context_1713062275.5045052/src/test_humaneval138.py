"""Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
Example
is_equal_to_sum_even(4) == False
is_equal_to_sum_even(6) == False
is_equal_to_sum_even(8) == True
"""

def is_equal_to_sum_even(n):
    return n%2 == 0 and n >= 8

def test_is_equal_to_sum_even(): # pragma: no cover
    global test_is_equal_to_sum_even, is_equal_to_sum_even

    assert not is_equal_to_sum_even(4), "Test case 1 failed"
    assert not is_equal_to_sum_even(6), "Test case 2 failed"
    assert is_equal_to_sum_even(8), "Test case 3 failed"
    assert is_equal_to_sum_even(12), "Test case 4 failed"
    assert not is_equal_to_sum_even(7), "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_is_equal_to_sum_even()
