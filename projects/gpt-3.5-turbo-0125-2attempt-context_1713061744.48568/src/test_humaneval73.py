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
    
    # Test case where 4 elements need to be changed
    assert smallest_change([1,2,3,5,4,7,9,6]) == 4, "Test case 1 failed"
    
    # Test case where 1 element needs to be changed
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1, "Test case 2 failed"
    
    # Test case where no elements need to be changed
    assert smallest_change([1, 2, 3, 2, 1]) == 0, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_smallest_change()
