"""
Given a non-empty array of integers arr and an integer k, return
the sum of the elements with at most two digits from the first k elements of arr.

Example:

Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
Output: 24 # sum of 21 + 3

Constraints:
1. 1 <= len(arr) <= 100
2. 1 <= k <= len(arr)
"""

def add_elements(arr, k):
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)

def test_add_elements(): # pragma: no cover
    global add_elements
    # Test case 1
    arr1 = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k1 = 4
    expected1 = 24
    assert add_elements(arr1, k1) == expected1, f"Test case 1 failed: expected {expected1}, got {add_elements(arr1, k1)}"

    # Test case 2
    arr2 = [10, 20, 30, 40, 50]
    k2 = 3
    expected2 = 60
    assert add_elements(arr2, k2) == expected2, f"Test case 2 failed: expected {expected2}, got {add_elements(arr2, k2)}"

    # Test case 3
    arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k3 = 10
    expected3 = 55
    assert add_elements(arr3, k3) == expected3, f"Test case 3 failed: expected {expected3}, got {add_elements(arr3, k3)}"

    # Test case 4
    arr4 = [100, 200, 300, 400, 500]
    k4 = 5
    expected4 = 0
    assert add_elements(arr4, k4) == expected4, f"Test case 4 failed: expected {expected4}, got {add_elements(arr4, k4)}"

    # Test case 5
    arr5 = [99, 11, 2, 1000]
    k5 = 4
    expected5 = 112
    assert add_elements(arr5, k5) == expected5, f"Test case 5 failed: expected {expected5}, got {add_elements(arr5, k5)}"

if __name__ == "__main__": # pragma: no cover
    test_add_elements()
