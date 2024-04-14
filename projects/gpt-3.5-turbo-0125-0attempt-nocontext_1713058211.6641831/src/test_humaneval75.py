"""Write a function that returns true if the given number is the multiplication of 3 prime numbers
and false otherwise.
Knowing that (a) is less then 100. 
Example:
is_multiply_prime(30) == True
30 = 2 * 3 * 5
"""

def is_multiply_prime(a):
    def is_prime(n):
        for j in range(2,n):
            if n%j == 0:
                return False
        return True

    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False

def test_is_multiply_prime(): # pragma: no cover
    global is_multiply_prime

    assert is_multiply_prime(6) == True, "Test case 1 failed"
    assert is_multiply_prime(8) == True, "Test case 2 failed"
    assert is_multiply_prime(9) == False, "Test case 3 failed"
    assert is_multiply_prime(49) == True, "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_is_multiply_prime()
