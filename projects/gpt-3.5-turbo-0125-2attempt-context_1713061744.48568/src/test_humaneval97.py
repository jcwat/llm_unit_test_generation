"""Complete the function that takes two integers and returns 
the product of their unit digits.
Assume the input is always valid.
Examples:
multiply(148, 412) should return 16.
multiply(19, 28) should return 72.
multiply(2020, 1851) should return 0.
multiply(14,-15) should return 20.
"""

def multiply(a, b):
    return abs(a % 10) * abs(b % 10)

def test_multiply(): # pragma: no cover
    global test_multiply, math
    assert multiply(148, 412) == 16, "Test case 1 failed"
    assert multiply(19, 28) == 72, "Test case 2 failed"
    assert multiply(2020, 1851) == 0, "Test case 3 failed"
    assert multiply(14, -15) == 20, "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_multiply()
