"""Return median of elements in the list l.
>>> median([3, 1, 2, 4, 5])
3
>>> median([-10, 4, 6, 1000, 10, 20])
15.0
"""


def median(l: list):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0

def test_median(): # pragma: no cover
    global test_median
    assert median([1, 2, 3, 4, 5]) == 3, "Test case 1 failed"
    assert median([1, 2, 3, 4, 5, 6]) == 3.5, "Test case 2 failed"
    assert median([6, 5, 4, 3, 2, 1]) == 3.5, "Test case 3 failed"
    assert median([1]) == 1, "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_median()
