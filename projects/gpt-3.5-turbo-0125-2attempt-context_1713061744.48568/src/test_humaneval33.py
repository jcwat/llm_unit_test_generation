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
    global sort_third

    assert sort_third([1, 2, 3]) == [1, 2, 3], "Test case 1 failed"
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5], "Test case 2 failed"
    assert sort_third([7, 3, 1, 0, 4, 6, 2, 5]) == [0, 3, 1, 4, 6, 6, 2, 5], "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_sort_third()
