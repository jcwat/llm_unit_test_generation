"""The Brazilian factorial is defined as:
brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
where n > 0

For example:
>>> special_factorial(4)
288

The function will receive an integer as input and should return the special
factorial of this integer.
"""

def special_factorial(n):
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

def test_special_factorial(): # pragma: no cover
    global special_factorial, math
    assert special_factorial(1) == 1, "Test case 1 failed"
    assert special_factorial(2) == 2, "Test case 2 failed"
    assert special_factorial(3) == 12, "Test case 3 failed"
    assert special_factorial(4) == 288, "Test case 4 failed"
    assert abs(special_factorial(5) - 34560) <= 1e-5, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_special_factorial()
