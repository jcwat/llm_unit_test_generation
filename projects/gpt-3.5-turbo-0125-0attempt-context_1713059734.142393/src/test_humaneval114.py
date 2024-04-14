"""
Given an array of integers nums, find the minimum sum of any non-empty sub-array
of nums.
Example
minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
minSubArraySum([-1, -2, -3]) == -6
"""

def minSubArraySum(nums):
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if (s < 0):
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = -max_sum
    return min_sum

def test_minSubArraySum(): # pragma: no cover
    global minSubArraySum

    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1, "Test case 1 failed"
    assert minSubArraySum([-1, -2, -3]) == -6, "Test case 2 failed"
    assert minSubArraySum([5, -2, 3, 10, -6]) == -5, "Test case 3 failed"
    assert minSubArraySum([1, 2, 3, 4, -10]) == -10, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_minSubArraySum()
