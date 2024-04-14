"""Return only positive numbers in the list.
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
"""


def get_positive(l: list):
    return [e for e in l if e > 0]

def test_get_positive(): # pragma: no cover
    global get_positive
    
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6], "Test case 1 failed"
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1], "Test case 2 failed"

if __name__ == "__main__": # pragma: no cover
    test_get_positive()
