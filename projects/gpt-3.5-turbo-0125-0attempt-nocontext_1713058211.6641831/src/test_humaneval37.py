"""This function takes a list l and returns a list l' such that
l' is identical to l in the odd indicies, while its values at the even indicies are equal
to the values of the even indicies of l, but sorted.
>>> sort_even([1, 2, 3])
[1, 2, 3]
>>> sort_even([5, 6, 3, 4])
[3, 6, 5, 4]
"""


def sort_even(l: list):
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans

def test_sort_even(): # pragma: no cover
    global sort_even
    
    # Test case 1: When input list is already sorted
    input_list = [1, 2, 3, 4, 5, 6]
    expected_output = [2, 1, 4, 3, 6, 5]
    assert sort_even(input_list) == expected_output, "Test case 1 failed"

    # Test case 2: When input list is reverse sorted
    input_list = [6, 5, 4, 3, 2, 1]
    expected_output = [2, 1, 4, 3, 6, 5]
    assert sort_even(input_list) == expected_output, "Test case 2 failed"

    # Test case 3: When input list has duplicate values
    input_list = [3, 6, 2, 5, 2, 4]
    expected_output = [2, 2, 4, 3, 6, 5]
    assert sort_even(input_list) == expected_output, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_sort_even()
