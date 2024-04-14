"""Return True is list elements are monotonically increasing or decreasing.
>>> monotonic([1, 2, 4, 20])
True
>>> monotonic([1, 20, 4, 10])
False
>>> monotonic([4, 1, 0, -10])
True
"""


def monotonic(l: list):
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False

def test_monotonic(): # pragma: no cover
    global monotonic

    assert monotonic([1, 2, 4, 20]) == True, "Test case 1 failed"
    assert monotonic([1, 20, 4, 10]) == False, "Test case 2 failed"
    assert monotonic([4, 1, 0, -10]) == True, "Test case 3 failed"
    assert monotonic([3, 3, 3, 3]) == True, "Test case 4 failed"
    assert monotonic([1, 2, 2, 3]) == True, "Test case 5 failed"
    assert monotonic([5, 4, 3, 2, 1]) == True, "Test case 6 failed"
    assert monotonic([5, 5, 5]) == True, "Test case 7 failed"

if __name__ == "__main__": # pragma: no cover
    test_monotonic()
