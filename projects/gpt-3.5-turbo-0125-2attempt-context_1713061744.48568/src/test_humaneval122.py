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

    arr1 = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k1 = 4
    assert add_elements(arr1, k1) == 24, "Test case 1 failed"
    
    arr2 = [12, 345, 67, 89, 1001]
    k2 = 3
    assert add_elements(arr2, k2) == 166, "Test case 2 failed"
    
    arr3 = [1111, 2222, 3333, 4444, 5555]
    k3 = 2
    assert add_elements(arr3, k3) == 0, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_add_elements()
