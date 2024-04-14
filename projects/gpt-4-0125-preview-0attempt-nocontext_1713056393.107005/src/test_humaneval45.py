"""Given length of a side and high return area for a triangle.
>>> triangle_area(5, 3)
7.5
"""


def triangle_area(a, h):
    return a * h / 2.0

def test_triangle_area(): # pragma: no cover
    global test_triangle_area
    assert abs(triangle_area(5, 3) - 7.5) <= 1e-5, "Test case 1 failed"
    assert abs(triangle_area(10, 2) - 10.0) <= 1e-5, "Test case 2 failed"
    assert abs(triangle_area(0, 100) - 0.0) <= 1e-5, "Test case 3 failed"
    assert abs(triangle_area(8.5, 4.2) - 17.85) <= 1e-5, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_triangle_area()
