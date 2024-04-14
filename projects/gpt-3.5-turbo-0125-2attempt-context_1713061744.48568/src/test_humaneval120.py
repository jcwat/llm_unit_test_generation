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
    
    # Example 1
    arr1 = [-3, -4, 5]
    k1 = 3
    assert maximum(arr1, k1) == [-4, -3, 5], "Test case 1 failed"
    
    # Example 2
    arr2 = [4, -4, 4]
    k2 = 2
    assert maximum(arr2, k2) == [4, 4], "Test case 2 failed"
    
    # Example 3
    arr3 = [-3, 2, 1, 2, -1, -2, 1]
    k3 = 1
    assert maximum(arr3, k3) == [2], "Test case 3 failed"
    
    # Additional test cases
    arr4 = [4, -5, 3, 2, -1, 7]
    k4 = 4
    assert maximum(arr4, k4) == [2, 3, 4, 7], "Test case 4 failed"
    
    arr5 = [0, 0, 0, 0, 0, 0]
    k5 = 3
    assert maximum(arr5, k5) == [0, 0, 0], "Test case 5 failed"
    
if __name__ == "__main__": # pragma: no cover
    test_maximum()
