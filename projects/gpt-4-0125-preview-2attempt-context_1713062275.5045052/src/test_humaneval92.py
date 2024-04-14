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
    # Test cases
    assert any_int(5, 2, 7), "Test case 1 failed: Expected True for (5, 2, 7)"
    assert not any_int(3, 2, 2), "Test case 2 failed: Expected False for (3, 2, 2)"
    assert any_int(3, -2, 1), "Test case 3 failed: Expected True for (3, -2, 1)"
    assert not any_int(3.6, -2.2, 2), "Test case 4 failed: Expected False for (3.6, -2.2, 2) as inputs are not all integers"

    # Additional tests
    assert not any_int(0, 0, 1), "Test case 5 failed: Expected False for (0, 0, 1) as sum does not match any single number"
    assert any_int(0, 0, 0), "Test case 6 failed: Expected True for (0, 0, 0) as the sum of any two zeros is the third zero"
    assert any_int(-3, 3, 0), "Test case 7 failed: Expected True for (-3, 3, 0) as the sum does match and all values are indeed integers"

if __name__ == "__main__": # pragma: no cover
    test_any_int()
