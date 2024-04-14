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
    global x_or_y
    # Test prime number case
    assert x_or_y(7, 34, 12) == 34, "Failed: Expected 34 for prime number 7"
    # Test non-prime number case
    assert x_or_y(15, 8, 5) == 5, "Failed: Expected 5 for non-prime number 15"
    # Test edge case 1 (the smallest prime number)
    assert x_or_y(2, 10, 3) == 10, "Failed: Expected 10 for prime number 2"
    # Test edge case with 1
    assert x_or_y(1, 15, 20) == 20, "Failed: Expected 20 for n=1"
    # Test large prime number
    assert x_or_y(13, 5, 2) == 5, "Failed: Expected 5 for prime number 13"
    # Test large non-prime number
    assert x_or_y(10, 1, 0) == 0, "Failed: Expected 0 for non-prime number 10"

if __name__ == "__main__": # pragma: no cover
    test_x_or_y()
