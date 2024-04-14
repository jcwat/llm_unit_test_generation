"""Given length of a side and high return area for a triangle.
>>> triangle_area(5, 3)
7.5
"""


def triangle_area(a, h):
    return a * h / 2.0

def test_triangle_area(): # pragma: no cover
    global test_triangle_area
    assert triangle_area(3, 4) == 6, "Test case 1 failed"
    assert triangle_area(5, 12) == 30, "Test case 2 failed"
    assert triangle_area(8, 15) == 60, "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_triangle_area()
