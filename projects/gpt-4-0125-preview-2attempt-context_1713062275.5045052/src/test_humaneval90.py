"""
You are given a list of integers.
Write a function next_smallest() that returns the 2nd smallest element of the list.
Return None if there is no such element.

next_smallest([1, 2, 3, 4, 5]) == 2
next_smallest([5, 1, 4, 3, 2]) == 2
next_smallest([]) == None
next_smallest([1, 1]) == None
"""

def next_smallest(lst):
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]

def test_next_smallest(): # pragma: no cover
    global next_smallest
    assert next_smallest([1, 2, 3, 4, 5]) == 2, "Test case 1 failed"
    assert next_smallest([5, 1, 4, 3, 2]) == 2, "Test case 2 failed"
    assert next_smallest([]) == None, "Test case 3 failed"
    assert next_smallest([1, 1]) == None, "Test case 4 failed"
    assert next_smallest([10, 9, 8, 7, 11]) == 8, "Test case 5 failed"
    assert next_smallest([2]) == None, "Test case 6 failed"
    assert next_smallest([3, 3, 3]) == None, "Test case 7 failed"

if __name__ == "__main__": # pragma: no cover
    test_next_smallest()
