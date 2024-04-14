'''
Given the lengths of the three sides of a triangle. Return True if the three
sides form a right-angled triangle, False otherwise.
A right-angled triangle is a triangle in which one angle is right angle or 
90 degree.
Example:
right_angle_triangle(3, 4, 5) == True
right_angle_triangle(1, 2, 3) == False
'''

def right_angle_triangle(a, b, c):
    return a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b

def test_right_angle_triangle(): # pragma: no cover
    global right_angle_triangle
    assert right_angle_triangle(3, 4, 5) == True, "Test case 1 failed"
    assert right_angle_triangle(5, 12, 13) == True, "Test case 2 failed"
    assert right_angle_triangle(1, 2, 3) == False, "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_right_angle_triangle()
