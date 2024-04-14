"""This function takes a list l and returns a list l' such that
l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
to the values of the corresponding indicies of l, but sorted.
>>> sort_third([1, 2, 3])
[1, 2, 3]
>>> sort_third([5, 6, 3, 4, 8, 9, 2])
[2, 6, 3, 4, 8, 9, 5]
"""


def sort_third(l: list):
    l = list(l)
    l[::3] = sorted(l[::3])
    return l

def test_sort_third(): # pragma: no cover
    global test_sort_third
    assert sort_third([1, 3, 2, 4, 7, 6]) == [1, 3, 2, 4, 6, 7], "Test case 1 failed"
    assert sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 1, 6, 5, 4, 7, 2, 3], "Test case 2 failed"
    assert sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9], "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_sort_third()
