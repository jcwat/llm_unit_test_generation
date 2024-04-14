"""Given length of a side and high return area for a triangle.
>>> triangle_area(5, 3)
7.5
"""


def triangle_area(a, h):
    return a * h / 2.0

def test_triangle_area(): # pragma: no cover
    global test_triangle_area
    assert abs(triangle_area(5, 3) - 7.5) < 1e-5, "Test case 1 failed: Incorrect area for sides 5 and 3"
    assert abs(triangle_area(10, 2) - 10.0) < 1e-5, "Test case 2 failed: Incorrect area for sides 10 and 2"
    assert abs(triangle_area(0, 100) - 0.0) < 1e-5, "Test case 3 failed: Incorrect area for side 0 and height 100"
    assert abs(triangle_area(100, 0) - 0.0) < 1e-5, "Test case 4 failed: Incorrect area for side 100 and height 0"
    assert abs(triangle_area(1.5, 2.5) - 1.875) < 1e-5, "Test case 5 failed: Incorrect area for sides 1.5 and 2.5"

if __name__ == "__main__": # pragma: no cover
    test_triangle_area()
