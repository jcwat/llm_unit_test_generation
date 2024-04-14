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
    # Test case 1: Simple quadratic polynomial coefficients
    polynomial1 = [1, 2, 3]
    expected1 = [2, 6]
    result1 = derivative(polynomial1)
    assert all(abs(a - b) < 1e-5 for a, b in zip(expected1, result1)), f"Test case 1 failed: {result1} != {expected1}"

    # Test case 2: Higher degree polynomial coefficients
    polynomial2 = [3, 1, 2, 4, 5]
    expected2 = [1, 4, 12, 20]
    result2 = derivative(polynomial2)
    assert all(abs(a - b) < 1e-5 for a, b in zip(expected2, result2)), f"Test case 2 failed: {result2} != {expected2}"

    # Test case 3: Linear polynomial coefficients
    polynomial3 = [5, 7]
    expected3 = [7]
    result3 = derivative(polynomial3)
    assert all(abs(a - b) < 1e-5 for a, b in zip(expected3, result3)), f"Test case 3 failed: {result3} != {expected3}"

    # Test case 4: Constant polynomial (should result in an empty list)
    polynomial4 = [42]
    expected4 = []
    result4 = derivative(polynomial4)
    assert result4 == expected4, f"Test case 4 failed: {result4} != {expected4}"

if __name__ == "__main__": # pragma: no cover
    test_derivative()
