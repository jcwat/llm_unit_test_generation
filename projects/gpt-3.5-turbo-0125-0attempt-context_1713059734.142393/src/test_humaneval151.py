'''
Given a list of numbers, return the sum of squares of the numbers
in the list that are odd. Ignore numbers that are negative or not integers.

double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
double_the_difference([-1, -2, 0]) == 0
double_the_difference([9, -2]) == 81
double_the_difference([0]) == 0  
   
If the input list is empty, return 0.
'''

def double_the_difference(lst):
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])

''' # pragma: no cover
Given a list of numbers, return the sum of squares of the numbers
in the list that are odd. Ignore numbers that are negative or not integers.

double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
double_the_difference([-1, -2, 0]) == 0
double_the_difference([9, -2]) == 81
double_the_difference([0]) == 0

If the input list is empty, return 0.
'''

def test_double_the_difference():
    global double_the_difference
    assert double_the_difference([1, 3, 2, 0]) == 10, "Test case 1 failed"
    assert double_the_difference([-1, -2, 0]) == 0, "Test case 2 failed"
    assert double_the_difference([9, -2]) == 81, "Test case 3 failed"
    assert double_the_difference([0]) == 0, "Test case 4 failed"
    assert double_the_difference([2, 4, 6, 8]) == 0, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_double_the_difference()
