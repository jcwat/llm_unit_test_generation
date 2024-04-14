"""Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
Example
is_equal_to_sum_even(4) == False
is_equal_to_sum_even(6) == False
is_equal_to_sum_even(8) == True
"""

def is_equal_to_sum_even(n):
    return n%2 == 0 and n >= 8

def test_is_equal_to_sum_even(): # pragma: no cover
    global is_equal_to_sum_even
    assert is_equal_to_sum_even(4) == False, "Test case 1 failed"
    assert is_equal_to_sum_even(6) == False, "Test case 2 failed"
    assert is_equal_to_sum_even(8) == True, "Test case 3 failed"
    assert is_equal_to_sum_even(10) == True, "Test case 4 failed"
    assert is_equal_to_sum_even(14) == True, "Test case 5 failed"
    assert is_equal_to_sum_even(7) == False, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_is_equal_to_sum_even()
