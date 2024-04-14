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
    global test_can_arrange, can_arrange
    # Test case where the function should find an element that is not greater than the previous one.
    assert can_arrange([1,2,4,3,5]) == 3, "Test case 1 failed: Expected index 3 but got a different index."
    # Test case where all elements are in increasing order.
    assert can_arrange([1,2,3]) == -1, "Test case 2 failed: Expected -1 for strictly increasing array."
    # Test case with negative numbers.
    assert can_arrange([-5, -3, -4]) == 2, "Test case 3 failed: Expected index 2 but got a different index."
    # Test case with duplicates, which should not occur as per the problem statement, but checking edge case handling.
    assert can_arrange([1,2,2,3]) == -1, "Test case 4 failed: Expected -1 as duplicates should not impact the logic."
    # Test case with larger numbers and a larger array to see if the logic holds.
    assert can_arrange([10, 20, 30, 40, 35, 45]) == 4, "Test case 5 failed: Expected index 4 but got a different index."

if __name__ == "__main__": # pragma: no cover
    test_can_arrange()
