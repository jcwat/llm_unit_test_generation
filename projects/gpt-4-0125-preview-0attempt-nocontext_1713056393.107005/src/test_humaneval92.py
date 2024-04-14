'''
Create a function that takes 3 numbers.
Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
Returns false in any other cases.

Examples
any_int(5, 2, 7) ➞ True

any_int(3, 2, 2) ➞ False

any_int(3, -2, 1) ➞ True

any_int(3.6, -2.2, 2) ➞ False
  


'''

def any_int(x, y, z):
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False

def test_any_int(): # pragma: no cover
    global any_int
    assert any_int(5, 2, 7) == True, "Test case 1 failed"
    assert any_int(3, 2, 2) == False, "Test case 2 failed"
    assert any_int(3, -2, 1) == True, "Test case 3 failed"
    assert any_int(3.6, -2.2, 2) == False, "Test case 4 failed"
    assert any_int(0, 0, 0) == True, "Test case 5 failed"
    assert any_int(10, -5, -15) == True, "Test case 6 failed"
    assert any_int(3, 5, 7) == False, "Test case 7 failed"

if __name__ == "__main__": # pragma: no cover
    test_any_int()
