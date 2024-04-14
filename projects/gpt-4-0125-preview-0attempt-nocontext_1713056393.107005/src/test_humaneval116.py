"""
In this Kata, you have to sort an array of non-negative integers according to
number of ones in their binary representation in ascending order.
For similar number of ones, sort based on decimal value.

It must be implemented like this:
>>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
>>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
>>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
"""

def sort_array(arr):
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))

def test_sort_array(): # pragma: no cover
    global sort_array
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5], "Test case 1 failed"
    assert sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2], "Test case 2 failed incorrectly handling negative numbers"
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4], "Test case 3 failed"
    assert sort_array([3, 8, 3, 6, 5]) == [8, 3, 3, 5, 6], "Test case 4 failed"
    assert sort_array([]) == [], "Test case 5 failed with empty array"

if __name__ == "__main__": # pragma: no cover
    test_sort_array()
