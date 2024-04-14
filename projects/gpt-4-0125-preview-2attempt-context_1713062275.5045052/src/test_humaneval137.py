"""
Create a function that takes integers, floats, or strings representing
real numbers, and returns the larger variable in its given variable type.
Return None if the values are equal.
Note: If a real number is represented as a string, the floating point might be . or ,

compare_one(1, 2.5) ➞ 2.5
compare_one(1, "2,3") ➞ "2,3"
compare_one("5,1", "6") ➞ "6"
compare_one("1", 1) ➞ None
"""

def compare_one(a, b):
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): return None
    return a if float(temp_a) > float(temp_b) else b 

def test_compare_one(): # pragma: no cover
    global compare_one
    # Test with integers and floats
    assert compare_one(1, 2.5) == 2.5, "Test case 1 failed"
    # Test with integer and string
    assert compare_one(1, "2,3") == "2,3", "Test case 2 failed"
    # Test with strings
    assert compare_one("5,1", "6") == "6", "Test case 3 failed"
    # Test with equal values of different types
    assert compare_one("1", 1) == None, "Test case 4 failed"
    # Test with negative values
    assert compare_one("-10", -5) == -5, "Test case 5 failed"
    # Test with floating point and comma in string
    assert compare_one("3,3", 3.2) == "3,3", "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_compare_one()