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
    global digits
    
    assert digits(1) == 1, "Test case 1 failed"
    assert digits(4) == 0, "Test case 2 failed"
    assert digits(235) == 15, "Test case 3 failed"
    assert digits(2468) == 0, "Test case 4 failed"
    assert digits(13579) == 945, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_digits()
