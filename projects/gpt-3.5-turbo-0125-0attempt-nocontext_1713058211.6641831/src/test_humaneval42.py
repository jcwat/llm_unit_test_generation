"""Return list with elements incremented by 1.
>>> incr_list([1, 2, 3])
[2, 3, 4]
>>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
"""


def incr_list(l: list):
    return [(e + 1) for e in l]

def test_incr_list(): # pragma: no cover
    global test_incr_list
    assert incr_list([1, 2, 3, 4]) == [2, 3, 4, 5], "Test case 1 failed"
    assert incr_list([-1, -2, -3, -4]) == [0, -1, -2, -3], "Test case 2 failed"
    assert incr_list([0, 0, 0, 0]) == [1, 1, 1, 1], "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_incr_list()
