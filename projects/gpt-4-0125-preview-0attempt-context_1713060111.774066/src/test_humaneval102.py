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
    assert choose_num(12, 15) == 14, "Test case 1 failed: choose_num(12, 15) should return 14"
    assert choose_num(13, 12) == -1, "Test case 2 failed: choose_num(13, 12) should return -1"
    assert choose_num(8, 8) == -1, "Test case 3 failed: choose_num(8, 8) should return -1"
    assert choose_num(7, 7) == -1, "Test case 4 failed: choose_num(7, 7) should return -1"
    assert choose_num(10, 20) == 20, "Test case 5 failed: choose_num(10, 20) should return 20"
    assert choose_num(10, 19) == 18, "Test case 6 failed: choose_num(10, 19) should return 18"
    assert choose_num(-2, -1) == -1, "Test case 7 failed: choose_num(-2, -1) should return -1"

if __name__ == "__main__": # pragma: no cover
    test_choose_num()
