"""Return sorted unique common elements for two lists.
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]

"""


def common(l1: list, l2: list):
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))

def test_common(): # pragma: no cover
    global common

    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653], "Test case 1 failed"
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3], "Test case 2 failed"
    assert common([5, 5, 5], [5, 5, 5]) == [5], "Test case 3 failed"
    assert common([], [1, 2, 3]) == [], "Test case 4 failed"
    assert common([1, 2, 3], []) == [], "Test case 5 failed"
if __name__ == "__main__": # pragma: no cover
    test_common()
