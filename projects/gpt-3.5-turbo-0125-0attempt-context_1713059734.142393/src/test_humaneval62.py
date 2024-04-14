""" xs represent coefficients of a polynomial.
xs[0] + xs[1] * x + xs[2] * x^2 + ....
 Return derivative of this polynomial in the same form.
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
"""


def derivative(xs: list):
    return [(i * x) for i, x in enumerate(xs)][1:]

def test_derivative(): # pragma: no cover
    global derivative
    
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20], "Test case 1 failed"
    assert derivative([1, 2, 3]) == [2, 6], "Test case 2 failed"

if __name__ == "__main__": # pragma: no cover
    test_derivative()
