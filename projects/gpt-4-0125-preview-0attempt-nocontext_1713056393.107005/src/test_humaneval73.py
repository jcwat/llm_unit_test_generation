"""
Given an array arr of integers, find the minimum number of elements that
need to be changed to make the array palindromic. A palindromic array is an array that
is read the same backwards and forwards. In one change, you can change one element to any other element.

For example:
smallest_change([1,2,3,5,4,7,9,6]) == 4
smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
smallest_change([1, 2, 3, 2, 1]) == 0
"""

def smallest_change(arr):
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans

def test_smallest_change(): # pragma: no cover
    global smallest_change
    assert smallest_change([1,2,3,5,4,7,9,6]) == 4, "Test case 1 failed"
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1, "Test case 2 failed"
    assert smallest_change([1, 2, 3, 2, 1]) == 0, "Test case 3 failed"
    assert smallest_change([1, 1, 1, 1]) == 0, "Test case 4 failed"
    assert smallest_change([5, 9, 8, 1, 8, 9, 5]) == 0, "Test case 5 failed"
    assert smallest_change([]) == 0, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_smallest_change()
