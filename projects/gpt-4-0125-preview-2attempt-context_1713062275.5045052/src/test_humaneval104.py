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
    global unique_digits
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33], "Test case 1 failed"
    assert unique_digits([152, 323, 1422, 10]) == [], "Test case 2 failed"
    assert unique_digits([111, 123, 321, 555]) == [111, 321, 555], "Test case 3 failed"
    assert unique_digits([]) == [], "Test case 4 failed"
    assert unique_digits([1111, 333, 7777, 999]) == [1111, 333, 7777, 999], "Test case 5 failed"
    assert unique_digits([2, 4, 6, 8, 0]) == [], "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_unique_digits()
