"""Return maximum element in the list.
>>> max_element([1, 2, 3])
3
>>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
123
"""


def max_element(l: list):
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m

def test_max_element(): # pragma: no cover
    global max_element
    assert max_element([1, 2, 3, 4, 5]) == 5, "Test case 1 failed"
    assert max_element([-1, -2, -3, -4, -5]) == -1, "Test case 2 failed"
    assert max_element([5, 4, 3, 2, 1]) == 5, "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_max_element()
