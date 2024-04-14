"""Given a positive integer n, return the product of the odd digits.
Return 0 if all digits are even.
For example:
digits(1)  == 1
digits(4)  == 0
digits(235) == 15
"""

def digits(n):
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit%2 == 1:
            product= product*int_digit
            odd_count+=1
    if odd_count ==0:
        return 0
    else:
        return product

def test_digits(): # pragma: no cover
    global test_digits
    assert digits(1) == 1, "Test case 1 failed: single digit odd number should return itself."
    assert digits(4) == 0, "Test case 2 failed: single digit even number should return 0."
    assert digits(135) == 15, "Test case 3 failed: product of odd digits calculated incorrectly."
    assert digits(111) == 1, "Test case 4 failed: product of repeated odd digit calculated incorrectly."
    assert digits(2468) == 0, "Test case 5 failed: all even digits should return 0."
    assert abs(digits(2357) - 105) < 1e-5, "Test case 6 failed: product of multiple odd digits calculated incorrectly."
    assert digits(22222222) == 0, "Test case 7 failed: large number with all even digits should return 0."
    assert digits(123456789) == 945, "Test case 8 failed: large number with mixed digits product calculated incorrectly."

if __name__ == "__main__": # pragma: no cover
    test_digits()
