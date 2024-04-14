"""A simple program which should return the value of x if n is 
a prime number and should return the value of y otherwise.

Examples:
for x_or_y(7, 34, 12) == 34
for x_or_y(15, 8, 5) == 5

"""

def x_or_y(n, x, y):
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x

def test_x_or_y(): # pragma: no cover
    global test_x_or_y
    assert x_or_y(1, 10, 20) == 20, "Test case 1 failed"
    assert x_or_y(2, 10, 20) == 10, "Test case 2 failed"
    assert x_or_y(3, 10, 20) == 10, "Test case 3 failed"
    assert x_or_y(4, 10, 20) == 20, "Test case 4 failed"
    assert x_or_y(5, 10, 20) == 10, "Test case 5 failed"
if __name__ == "__main__": # pragma: no cover
    test_x_or_y()
