"""
Write a function which sorts the given list of integers
in ascending order according to the sum of their digits.
Note: if there are several items with similar sum of their digits,
order them based on their index in original list.

For example:
>>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
>>> order_by_points([]) == []
"""

def order_by_points(nums):
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)

def test_order_by_points(): # pragma: no cover
    global order_by_points
    
    # Test on provided examples
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11], "Test case 1 failed"
    assert order_by_points([]) == [], "Test case 2 failed"
    
    # Additional test cases
    assert order_by_points([123, 321, 111, 222]) == [111, 123, 321, 222], "Additional Test case 1 failed"
    assert order_by_points([0, 9, 99, 999, 9999]) == [0, 9, 99, 999, 9999], "Additional Test case 2 failed"
    assert order_by_points([899, 991, 778, 655, 223, -89]) == [-89, 223, 899, 655, 778, 991], "Additional Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_order_by_points()
