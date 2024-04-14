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
    
    # Test case 1: Check for balanced and underweight
    assert will_it_fly([1, 2, 1], 5) == True, "Test case 1 failed: Balanced and under max weight."
    
    # Test case 2: Check for unbalanced
    assert will_it_fly([1, 2, 2], 5) == False, "Test case 2 failed: Unbalanced but under max weight."
    
    # Test case 3: Check for balance and overweight
    assert will_it_fly([3, 2, 3], 5) == False, "Test case 3 failed: Balanced but over max weight."
    
    # Test case 4: Check for single element
    assert will_it_fly([3], 5) == True, "Test case 4 failed: Single element which is balanced and under max weight."

    # Test case 5: Check for empty list
    assert will_it_fly([], 5) == True, "Test case 5 failed: Empty list should be considered balanced and under max weight."

if __name__ == "__main__": # pragma: no cover
    test_will_it_fly()
