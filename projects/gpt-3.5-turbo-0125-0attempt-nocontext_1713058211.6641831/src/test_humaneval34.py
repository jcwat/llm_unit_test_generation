"""Return sorted unique elements in a list
>>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
[0, 2, 3, 5, 9, 123]
"""


def unique(l: list):
    return sorted(list(set(l)))

def test_unique(): # pragma: no cover
    global test_unique
    assert unique([1, 2, 3, 3, 4, 5, 5]) == [1, 2, 3, 4, 5], "Test case 1 failed"
    assert unique([3, 3, 3, 3, 3]) == [3], "Test case 2 failed"
    assert unique([]) == [], "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_unique()
