'''
Given a list of numbers, return whether or not they are sorted
in ascending order. If list has more than 1 duplicate of the same
number, return False. Assume no negative numbers and only integers.

Examples
is_sorted([5]) ➞ True
is_sorted([1, 2, 3, 4, 5]) ➞ True
is_sorted([1, 3, 2, 4, 5]) ➞ False
is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
'''

def is_sorted(lst):
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1 
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False
    
    

def test_is_sorted(): # pragma: no cover
    global is_sorted

    # Test cases
    assert is_sorted([5]) == True, "Test case 1 failed"
    assert is_sorted([1, 2, 3, 4, 5]) == True, "Test case 2 failed"
    assert is_sorted([1, 3, 2, 4, 5]) == False, "Test case 3 failed"
    assert is_sorted([1, 2, 3, 4, 5, 6]) == True, "Test case 4 failed"
    assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == True, "Test case 5 failed"
    assert is_sorted([1, 3, 2, 4, 5, 6, 7]) == False, "Test case 6 failed"
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True, "Test case 7 failed"
    assert is_sorted([1, 2, 2, 2, 3, 4]) == False, "Test case 8 failed"

if __name__ == "__main__": # pragma: no cover
    test_is_sorted()
