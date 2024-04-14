""" xs are coefficients of a polynomial.
find_zero find x such that poly(x) = 0.
find_zero returns only only zero point, even if there are many.
Moreover, find_zero only takes list xs having even number of coefficients
and largest non zero coefficient as it guarantees
a solution.
>>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
-0.5
>>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
1.0
"""
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    begin, end = -1., 1.
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin

def test_find_zero(): # pragma: no cover
    global test_find_zero, poly, math
    # Test case 1: Polynomial with one root
    assert abs(find_zero([1, 2]) + 0.5) <= 1e-5, "Test case 1 failed. Expected root close to -0.5"
    
    # Test case 2: Polynomial with multiple roots, test for one returned root
    assert abs(find_zero([-6, 11, -6, 1]) - 1.0) <= 1e-5, "Test case 2 failed. Expected root close to 1.0"
    
    # Test case 3: Test with larger coefficients and higher degree
    assert abs(find_zero([10, -45, 40, -15, 1]) - 1.0) <= 1e-5, "Test case 3 failed. Expected root close to 1.0"
    
    # Test case 4: Polynomial that approaches zero asymptotically, ensure it works in provided domain
    assert abs(find_zero([-2, 0, 1]) - math.sqrt(2)) <= 1e-5, "Test case 4 failed. Expected root close to sqrt(2)"

if __name__ == "__main__": # pragma: no cover
    test_find_zero()
