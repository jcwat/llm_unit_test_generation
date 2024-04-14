"""Given a list of positive integers x. return a sorted list of all 
elements that hasn't any even digit.

Note: Returned list should be sorted in increasing order.

For example:
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
"""

def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

def test_unique_digits(): # pragma: no cover
    global test_unique_digits
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33], "Test case 1 failed"
    assert unique_digits([152, 323, 1422, 10]) == [], "Test case 2 failed"
    assert unique_digits([13579, 3571, 97531]) == [13579, 3571, 97531], "Test case 3 failed"
    assert unique_digits([2468, 1234, 2222]) == [], "Test case 4 failed"
    assert unique_digits([111, 222, 333, 444]) == [111, 333], "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_unique_digits()
