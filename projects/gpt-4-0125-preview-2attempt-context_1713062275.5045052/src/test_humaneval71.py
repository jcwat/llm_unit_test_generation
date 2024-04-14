'''
Given the lengths of the three sides of a triangle. Return the area of
the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
Otherwise return -1
Three sides make a valid triangle when the sum of any two sides is greater 
than the third side.
Example:
triangle_area(3, 4, 5) == 6.00
triangle_area(1, 2, 10) == -1
'''

def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area

def test_triangle_area(): # pragma: no cover
    global triangle_area, math
    # Case 1: Valid triangle
    assert abs(triangle_area(3, 4, 5) - 6.00) <= 1e-5, "Test case 1 failed: Valid triangle didn't return correct area."
    # Case 2: Another valid triangle
    assert abs(triangle_area(6, 8, 10) - 24.00) <= 1e-5, "Test case 2 failed: Another valid triangle didn't return correct area."
    # Case 3: Invalid triangle, return -1
    assert triangle_area(1, 2, 10) == -1, "Test case 3 failed: Invalid triangle didn't return -1."
    # Case 4: Valid triangle with floating points
    assert abs(triangle_area(3.0, 4.0, 5.0) - 6.00) <= 1e-5, "Test case 4 failed: Valid triangle with floating points didn't return correct area."
    # Case 5: Invalid triangle with one side zero
    assert triangle_area(0, 4, 5) == -1, "Test case 5 failed: Triangle with one side zero didn't return -1."

if __name__ == "__main__": # pragma: no cover
    test_triangle_area()
