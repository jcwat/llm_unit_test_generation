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
    global test_sort_array
    assert sort_array([]) == [], "Test case 1 failed"
    assert sort_array([5]) == [5], "Test case 2 failed"
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5], "Test case 3 failed"
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0], "Test case 4 failed"
    assert sort_array([1, 3, 5, 7]) == [1, 3, 5, 7], "Test case 5 failed"
if __name__ == "__main__": # pragma: no cover
    test_sort_array()
