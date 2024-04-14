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
    global test_derivative
    # Test case 1
    result = derivative([3, 1, 2, 4, 5])
    expected = [1, 4, 12, 20]
    assert all(abs(r - e) < 1e-5 for r, e in zip(result, expected)), "Test case 1 failed"

    # Test case 2
    result = derivative([1, 2, 3])
    expected = [2, 6]
    assert all(abs(r - e) < 1e-5 for r, e in zip(result, expected)), "Test case 2 failed"

    # Test case 3
    result = derivative([0, 10, 0, 0, 5])
    expected = [10, 0, 0, 20]
    assert all(abs(r - e) < 1e-5 for r, e in zip(result, expected)), "Test case 3 failed"

    # Test case 4: Zero polynomial
    result = derivative([0])
    expected = []
    assert result == expected, "Test case 4 failed with zero polynomial"

if __name__ == "__main__": # pragma: no cover
    test_derivative()
