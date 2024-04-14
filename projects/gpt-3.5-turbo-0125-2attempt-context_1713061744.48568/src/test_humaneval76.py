"""Your task is to write a function that returns true if a number x is a simple
power of n and false in other cases.
x is a simple power of n if n**int=x
For example:
is_simple_power(1, 4) => true
is_simple_power(2, 2) => true
is_simple_power(8, 2) => true
is_simple_power(3, 2) => false
is_simple_power(3, 1) => false
is_simple_power(5, 3) => false
"""

def is_simple_power(x, n):
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 

def test_is_simple_power(): # pragma: no cover
    global test_is_simple_power, math

    assert is_simple_power(1, 4) == True, "Test case 1 failed"
    assert is_simple_power(2, 2) == True, "Test case 2 failed"
    assert is_simple_power(8, 2) == True, "Test case 3 failed"
    assert is_simple_power(3, 2) == False, "Test case 4 failed"
    assert is_simple_power(3, 1) == False, "Test case 5 failed"
    assert is_simple_power(5, 3) == False, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_is_simple_power()
