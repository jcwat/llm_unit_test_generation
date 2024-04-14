"""
Given an array arr of integers and a positive integer k, return a sorted list 
of length k with the maximum k numbers in arr.

Example 1:

Input: arr = [-3, -4, 5], k = 3
Output: [-4, -3, 5]

Example 2:

Input: arr = [4, -4, 4], k = 2
Output: [4, 4]

Example 3:

Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
Output: [2]

Note:
1. The length of the array will be in the range of [1, 1000].
2. The elements in the array will be in the range of [-1000, 1000].
3. 0 <= k <= len(arr)
"""

def maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans

def test_maximum(): # pragma: no cover
    global maximum
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5], "Test case 1 failed"
    assert maximum([4, -4, 4], 2) == [4, 4], "Test case 2 failed"
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2], "Test case 3 failed"
    assert maximum([], 0) == [], "Test case 4 failed"
    assert maximum([1], 1) == [1], "Test case 5 failed"
    assert maximum([4, 1, 3, 2], 2) == [3, 4], "Test case 6 failed"
    assert maximum([-3, 2, 1, -5, -9, 22, 11], 3) == [2, 11, 22], "Test case 7 failed"

if __name__ == "__main__": # pragma: no cover
    test_maximum()
