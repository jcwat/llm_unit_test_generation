"""Return True if all numbers in the list l are below threshold t.
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
"""


def below_threshold(l: list, t: int):
    for e in l:
        if e >= t:
            return False
    return True

def test_below_threshold(): # pragma: no cover
    global test_below_threshold
    assert below_threshold([1, 2, 4, 10], 100) == True, "Test case 1 failed"
    assert below_threshold([1, 20, 4, 10], 5) == False, "Test case 2 failed"
    assert below_threshold([], 10) == True, "Test case 3 failed"
    assert below_threshold([10, 20, 30], 31) == True, "Test case 4 failed"
    assert below_threshold([10, 20, 30], 30) == False, "Test case 5 failed"
    assert below_threshold([1, 2, 3], 3) == False, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_below_threshold()
