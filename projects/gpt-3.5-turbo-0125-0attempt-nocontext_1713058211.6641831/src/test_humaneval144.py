"""Your task is to implement a function that will simplify the expression
x * n. The function returns True if x * n evaluates to a whole number and False
otherwise. Both x and n, are string representation of a fraction, and have the following format,
<numerator>/<denominator> where both numerator and denominator are positive whole numbers.

You can assume that x, and n are valid fractions, and do not have zero as denominator.

simplify("1/5", "5/1") = True
simplify("1/6", "2/1") = False
simplify("7/10", "10/2") = False
"""

def simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False

def test_simplify(): # pragma: no cover
    global simplify

    # Test cases where x/n can be simplified
    assert simplify("2/4", "1/2") == True, "Test case 1 failed"
    assert simplify("6/9", "2/3") == True, "Test case 2 failed"

    # Test cases where x/n cannot be simplified
    assert simplify("3/5", "4/7") == False, "Test case 3 failed"
    assert simplify("8/11", "3/5") == False, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_simplify()
