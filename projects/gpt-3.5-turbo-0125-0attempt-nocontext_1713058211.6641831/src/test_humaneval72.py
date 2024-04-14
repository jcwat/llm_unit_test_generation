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
    
    # Test case 1: sum of q elements is less than w
    q1 = [1, 2, 3, 4, 5]
    w1 = 20
    assert will_it_fly(q1, w1) == True, "Test case 1 failed"
    
    # Test case 2: sum of q elements is greater than w
    q2 = [4, 5, 6, 7]
    w2 = 20
    assert will_it_fly(q2, w2) == False, "Test case 2 failed"
    
    # Test case 3: q elements form a palindrome
    q3 = [1, 2, 3, 2, 1]
    w3 = 10
    assert will_it_fly(q3, w3) == True, "Test case 3 failed"
    
    # Test case 4: q elements do not form a palindrome
    q4 = [1, 2, 3, 4, 5]
    w4 = 15
    assert will_it_fly(q4, w4) == False, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_will_it_fly()
