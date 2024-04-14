
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%2 == 0 and n >= 8

def test_is_equal_to_sum_even(): # pragma: no cover
    assert  is_equal_to_sum_even(4) == False
    assert  is_equal_to_sum_even(6) == False
    assert  is_equal_to_sum_even(8) == True
    assert  is_equal_to_sum_even(10) == True
    assert  is_equal_to_sum_even(11) == False
    assert  is_equal_to_sum_even(12) == True
    assert  is_equal_to_sum_even(13) == False
    assert  is_equal_to_sum_even(16) == True

