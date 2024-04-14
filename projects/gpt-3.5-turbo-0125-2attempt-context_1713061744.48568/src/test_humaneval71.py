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

''' # pragma: no cover
Given the lengths of the three sides of a triangle. Return the area of
the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
Otherwise return -1
Three sides make a valid triangle when the sum of any two sides is greater 
than the third side.
Example:
triangle_area(3, 4, 5) == 6.00
triangle_area(1, 2, 10) == -1
'''

def test_triangle_area():
    global triangle_area, math
    assert triangle_area(3, 4, 5) == 6.00, "Test case 1 failed"
    assert triangle_area(5, 12, 13) == 30.00, "Test case 2 failed"
    assert triangle_area(7, 24, 25) == 84.00, "Test case 3 failed"
    assert triangle_area(8, 15, 17) == 60.00, "Test case 4 failed"
    assert triangle_area(1, 2, 10) == -1, "Test case 5 failed"
    assert triangle_area(1, 1, 1) == 0.43, "Test case 6 failed"
if __name__ == "__main__": # pragma: no cover
    test_triangle_area()
