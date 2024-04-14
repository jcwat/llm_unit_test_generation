"""This function takes two positive numbers x and y and returns the
biggest even integer number that is in the range [x, y] inclusive. If 
there's no such number, then the function should return -1.

For example:
choose_num(12, 15) = 14
choose_num(13, 12) = -1
"""

def choose_num(x, y):
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

def test_choose_num(): # pragma: no cover
    global test_choose_num
    assert choose_num(12, 15) == 14, "Test case 1 failed: should return the largest even number within the range."
    assert choose_num(13, 12) == -1, "Test case 2 failed: should return -1 when x > y."
    assert choose_num(5, 5) == -1, "Test case 3 failed: should return -1 when x == y and y is not even."
    assert choose_num(10, 10) == 10, "Test case 4 failed: should return y when y is even and x equals y."
    assert choose_num(1, 2) == 2, "Test case 5 failed: should return y when y is the only even number in the range."

if __name__ == "__main__": # pragma: no cover
    test_choose_num()
