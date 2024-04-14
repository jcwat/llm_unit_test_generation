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

    assert generate_integers(2, 8) == [2, 4, 6, 8], "Test case 1 failed"
    assert generate_integers(8, 2) == [2, 4, 6, 8], "Test case 2 failed"
    assert generate_integers(10, 14) == [], "Test case 3 failed"
    assert generate_integers(5, 5) == [6], "Test case 4 failed"
    assert generate_integers(2, 11) == [2, 4, 6, 8, 10], "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_generate_integers()
