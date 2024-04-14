"""
Given an array of non-negative integers, return a copy of the given array after sorting,
you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
or sort it in descending order if the sum( first index value, last index value) is even.

Note:
* don't change the given array.

Examples:
* sort_array([]) => []
* sort_array([5]) => [5]
* sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
* sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
"""

def sort_array(array):
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 

def test_sort_array(): # pragma: no cover
    global sort_array
    assert sort_array([]) == [], "Test case 1 failed"
    assert sort_array([5]) == [5], "Test case 2 failed"
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5], "Test case 3 failed"
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0], "Test case 4 failed"
    # Testing with an even sum for first and last element, expected descending order
    assert sort_array([10, 8, 6, 2]) == [10, 8, 6, 2], "Test case 5 failed"
    # Correcting Test case 6 based on the method description
    # This case should expect sorted in ascending order due to odd sum of first and last elements, not descending
    assert sort_array([1, 8, 6, 3]) == [1, 3, 6, 8], "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_sort_array()
