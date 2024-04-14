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
    # Test Case 1
    result = derivative([3, 1, 2, 4, 5])
    expected = [1, 4, 12, 20]
    assert all(abs(r - e) < 1e-5 for r, e in zip(result, expected)), f"Test case 1 failed: {result} != {expected}"
    
    # Test Case 2
    result = derivative([1, 2, 3])
    expected = [2, 6]
    assert all(abs(r - e) < 1e-5 for r, e in zip(result, expected)), f"Test case 2 failed: {result} != {expected}"
    
    # Test Case 3
    result = derivative([10])
    expected = []
    assert all(abs(r - e) < 1e-5 for r, e in zip(result, expected)), f"Test case 3 failed: {result} != {expected}"
    
    # Test Case 4
    result = derivative([5, 3])
    expected = [3]
    assert all(abs(r - e) < 1e-5 for r, e in zip(result, expected)), f"Test case 4 failed: {result} != {expected}"

    # Test Case 5
    result = derivative([])
    expected = []
    assert all(abs(r - e) < 1e-5 for r, e in zip(result, expected)), f"Test case 5 failed: {result} != {expected}"

if __name__ == "__main__": # pragma: no cover
    test_derivative()
