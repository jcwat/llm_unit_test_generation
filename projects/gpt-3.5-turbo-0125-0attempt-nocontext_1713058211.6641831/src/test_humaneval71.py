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
    global test_triangle_area
    assert triangle_area(3, 4, 5) == 6.0, "Test case 1 failed"
    assert triangle_area(6, 8, 10) == 24.0, "Test case 2 failed"
    assert triangle_area(5, 10, 5) == -1, "Test case 3 failed"
    assert triangle_area(7, 7, 7) == 21.22, "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_triangle_area()
