"""
Write a function count_nums which takes an array of integers and returns
the number of elements which has a sum of digits > 0.
If a number is negative, then its first signed digit will be negative:
e.g. -123 has signed digits -1, 2, and 3.
>>> count_nums([]) == 0
>>> count_nums([-1, 11, -11]) == 1
>>> count_nums([1, 1, 2]) == 3
"""

def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))

def test_count_nums(): # pragma: no cover
    global count_nums
    
    assert count_nums([]) == 0, "Test case 1 failed"
    assert count_nums([-1, 11, -11]) == 1, "Test case 2 failed"
    assert count_nums([1, 1, 2]) == 3, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_count_nums()
