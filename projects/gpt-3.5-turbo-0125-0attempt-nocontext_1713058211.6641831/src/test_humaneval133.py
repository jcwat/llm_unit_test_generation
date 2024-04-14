"""You are given a list of numbers.
You need to return the sum of squared numbers in the given list,
round each element in the list to the upper int(Ceiling) first.
Examples:
For lst = [1,2,3] the output should be 14
For lst = [1,4,9] the output should be 98
For lst = [1,3,5,7] the output should be 84
For lst = [1.4,4.2,0] the output should be 29
For lst = [-2.4,1,1] the output should be 6


"""


def sum_squares(lst):
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared

def test_sum_squares(): # pragma: no cover
    global test_sum_squares, math
    assert sum_squares([1, 2, 3, 4, 5]) == 55, "Test case 1 failed"
    assert sum_squares([0, 0, 0, 0, 0]) == 0, "Test case 2 failed"
    assert sum_squares([-1, -2, -3, -4, -5]) == 55, "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_sum_squares()
