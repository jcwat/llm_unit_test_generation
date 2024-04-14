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
    assert add_elements([123, 45, 678, 90, 12], 3) == 168, "Test case 1 failed"
    assert add_elements([1, 2, 345, 6, 78], 4) == 16, "Test case 2 failed"
    assert add_elements([100, 200, 300, 400, 500], 5) == 1500, "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_add_elements()
