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
    # Test with the provided examples
    assert sort_even([1, 2, 3]) == [1, 2, 3], "Test case 1 failed"
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4], "Test case 2 failed"

    # Test with an empty list
    assert sort_even([]) == [], "Test case 3 failed"

    # Test with a list of all even indices
    assert sort_even([4, 3, 2, 1]) == [2, 3, 4, 1], "Test case 4 failed"

    # Test with a list of all odd indices
    assert sort_even([1]) == [1], "Test case 5 failed"
    assert sort_even([3, 2, 1]) == [1, 2, 3], "Test case 6 failed"

    # Test with negative numbers
    assert sort_even([-5, -6, -3, -4]) == [-5, -6, -3, -4], "Test case 7 failed"

    # Test list with repeating elements
    assert sort_even([1, 3, 3, 2, 2, 1]) == [1, 3, 2, 2, 3, 1], "Test case 8 failed"

if __name__ == "__main__": # pragma: no cover
    test_sort_even()
