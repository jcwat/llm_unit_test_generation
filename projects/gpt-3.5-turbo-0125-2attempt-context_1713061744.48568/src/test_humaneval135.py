"""Create a function which returns the largest index of an element which
is not greater than or equal to the element immediately preceding it. If
no such element exists then return -1. The given array will not contain
duplicate values.

Examples:
can_arrange([1,2,4,3,5]) = 3
can_arrange([1,2,3]) = -1
"""

def can_arrange(arr):
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind

def test_can_arrange(): # pragma: no cover
    global test_can_arrange

    assert can_arrange([1, 2, 4, 3, 5]) == 3, "Test case 1 failed"
    assert can_arrange([1, 2, 3]) == -1, "Test case 2 failed"
    assert can_arrange([5, 4, 3, 2, 1]) == 4, "Test case 3 failed"
    assert can_arrange([1, 3, 1, 4]) == 2, "Test case 4 failed"
    assert can_arrange([5, 1, 2, 3, 4]) == 1, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_can_arrange()
