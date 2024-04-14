'''
Create a function that returns a tuple (a, b), where 'a' is
the largest of negative integers, and 'b' is the smallest
of positive integers in a list.
If there is no negative or positive integers, return them as None.

Examples:
largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
largest_smallest_integers([]) == (None, None)
largest_smallest_integers([0]) == (None, None)
'''

def largest_smallest_integers(lst):
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)

def test_largest_smallest_integers(): # pragma: no cover
    global largest_smallest_integers
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1), "Test case 1 failed"
    assert largest_smallest_integers([]) == (None, None), "Test case 2 failed"
    assert largest_smallest_integers([0]) == (None, None), "Test case 3 failed"
    assert largest_smallest_integers([-5, -1, 0, 3, 10]) == (-1, 3), "Test case 4 failed"
    assert largest_smallest_integers([-10, -20, -30]) == (-10, None), "Test case 5 failed"
    assert largest_smallest_integers([5, 15, 25]) == (None, 5), "Test case 6 failed"
if __name__ == "__main__": # pragma: no cover
    test_largest_smallest_integers()
