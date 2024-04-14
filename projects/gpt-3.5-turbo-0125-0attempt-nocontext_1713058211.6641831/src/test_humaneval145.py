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

    assert order_by_points([10, 5, -7, 2, -1]) == [-1, 2, 5, -7, 10], "Test case 1 failed"
    assert order_by_points([100, 20, -35, -12, 7]) == [7, 20, -35, -12, 100], "Test case 2 failed"
    assert order_by_points([-3, 9, -5, 13]) == [-5, 9, -3, 13], "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_order_by_points()
