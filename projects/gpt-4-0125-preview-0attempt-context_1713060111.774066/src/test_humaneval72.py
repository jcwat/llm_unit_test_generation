'''
Write a function that returns True if the object q will fly, and False otherwise.
The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

Example:
will_it_fly([1, 2], 5) ➞ False 
# 1+2 is less than the maximum possible weight, but it's unbalanced.

will_it_fly([3, 2, 3], 1) ➞ False
# it's balanced, but 3+2+3 is more than the maximum possible weight.

will_it_fly([3, 2, 3], 9) ➞ True
# 3+2+3 is less than the maximum possible weight, and it's balanced.

will_it_fly([3], 5) ➞ True
# 3 is less than the maximum possible weight, and it's balanced.
'''

def will_it_fly(q,w):
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True

def test_will_it_fly(): # pragma: no cover
    global will_it_fly
    # Test cases
    assert will_it_fly([1, 2], 5) == False, "Test case 1 failed: Unbalanced list should not fly."
    assert will_it_fly([3, 2, 3], 1) == False, "Test case 2 failed: Exceeding max weight should not fly."
    assert will_it_fly([3, 2, 3], 9) == True, "Test case 3 failed: Balanced and within max weight should fly."
    assert will_it_fly([3], 5) == True, "Test case 4 failed: Single element list within max weight should fly."
    assert will_it_fly([], 2) == True, "Test case 5 failed: Empty list within max weight should fly."
    assert will_it_fly([1, 2, 3, 2, 1], 10) == True, "Test case 6 failed: Balanced and within max weight should fly."
    assert will_it_fly([1, 2, 3, 2, 1], 8) == False, "Test case 7 failed: Balanced but exceeds max weight should not fly."

if __name__ == "__main__": # pragma: no cover
    test_will_it_fly()
