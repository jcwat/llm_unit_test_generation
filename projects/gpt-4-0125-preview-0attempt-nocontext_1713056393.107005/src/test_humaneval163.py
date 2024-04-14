"""
Given two positive integers a and b, return the even digits between a
and b, in ascending order.

For example:
generate_integers(2, 8) => [2, 4, 6, 8]
generate_integers(8, 2) => [2, 4, 6, 8]
generate_integers(10, 14) => []
"""

def generate_integers(a, b):
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def test_generate_integers(): # pragma: no cover
    global generate_integers
    assert generate_integers(2, 8) == [2, 4, 6, 8], "Test case 1 failed: generate_integers(2, 8)"
    assert generate_integers(8, 2) == [2, 4, 6, 8], "Test case 2 failed: generate_integers(8, 2)"
    assert generate_integers(10, 14) == [], "Test case 3 failed: generate_integers(10, 14)"
    assert generate_integers(1, 5) == [2, 4], "Test case 4 failed: generate_integers(1, 5)"
    assert generate_integers(5, 3) == [4], "Test case 5 failed: generate_integers(5, 3)"
    assert generate_integers(0, 1) == [], "Test case 6 failed: generate_integers(0, 1)"

if __name__ == "__main__": # pragma: no cover
    test_generate_integers()
