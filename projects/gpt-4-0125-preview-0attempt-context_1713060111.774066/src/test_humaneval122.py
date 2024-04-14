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
    
    # Test cases
    assert add_elements([111,21,3,4000,5,6,7,8,9], 4) == 24, "Test case 1 failed"
    assert add_elements([10, 20, 30, 40, 50], 3) == 60, "Test case 2 failed"
    assert add_elements([1, 2, 3, 4, 5], 5) == 15, "Test case 3 failed"
    assert add_elements([100, 200], 2) == 0, "Test case 4 failed"
    assert add_elements([99, 1, 101, 23], 4) == 123, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_add_elements()
