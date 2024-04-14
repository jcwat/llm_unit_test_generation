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
    global choose_num
    assert choose_num(12, 15) == 14, "Test case 1 failed"
    assert choose_num(13, 12) == -1, "Test case 2 failed"
    assert choose_num(10, 10) == -1, "Test case 3 failed"  # Corrected
    assert choose_num(11, 11) == -1, "Test case 4 failed"
    assert choose_num(1, 2) == 2, "Test case 5 failed"
    assert choose_num(2, 100) == 100, "Test case 6 failed"
    assert choose_num(100, 99) == -1, "Test case 7 failed"
    assert choose_num(3, 4) == 4, "Test case 8 failed"
    assert choose_num(0, 1) == 0, "Test case 9 failed corrected"  # Corrected
    assert choose_num(0, 0) == -1, "Test case 10 failed"

if __name__ == "__main__": # pragma: no cover
    test_choose_num()
