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

    # Test case 1
    input_arr1 = [1, 5, 2, 3, 4]
    expected_output1 = [1, 2, 3, 4, 5]
    assert sort_array(input_arr1) == expected_output1, "Test case 1 failed"

    # Test case 2
    input_arr2 = [-2, -3, -4, -5, -6]
    expected_output2 = [-6, -5, -4, -3, -2]
    assert sort_array(input_arr2) == expected_output2, "Test case 2 failed"

    # Test case 3
    input_arr3 = [1, 0, 2, 3, 4]
    expected_output3 = [0, 1, 2, 3, 4]
    assert sort_array(input_arr3) == expected_output3, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_sort_array()
