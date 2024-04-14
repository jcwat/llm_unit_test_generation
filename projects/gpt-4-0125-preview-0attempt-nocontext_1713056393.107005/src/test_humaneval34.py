"""Return sorted unique elements in a list
>>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
[0, 2, 3, 5, 9, 123]
"""


def unique(l: list):
    return sorted(list(set(l)))

def test_unique(): # pragma: no cover
    global test_unique, unique
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123], "Failed to return correct sorted unique elements"
    assert unique([]) == [], "Failed with empty list"
    assert unique([1, 1, 1, 1]) == [1], "Failed with list of identical elements"
    assert unique([-3, -1, -3, -7, -8]) == [-8, -7, -3, -1], "Failed with negative numbers"

if __name__ == "__main__": # pragma: no cover
    test_unique()
