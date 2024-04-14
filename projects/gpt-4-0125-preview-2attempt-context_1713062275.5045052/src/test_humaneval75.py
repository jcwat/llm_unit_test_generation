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
    global test_is_multiply_prime, is_multiply_prime
    
    assert is_multiply_prime(30) == True, "Test case 1 failed: 30 is a product of primes 2, 3, 5"
    assert is_multiply_prime(31) == False, "Test case 2 failed: 31 is not a product of 3 primes"
    assert is_multiply_prime(2*3*7) == True, "Test case 3 failed: 2*3*7 should be true"
    assert is_multiply_prime(2*2*5) == True, "Test case 4 failed: 2*2*5 should be considered true as it's a product of 3 primes, including repeated ones"
    assert is_multiply_prime(97) == False, "Test case 5 failed: 97 is prime but not a product of 3 primes"
    assert is_multiply_prime(5*7*11) == True, "Test case 6 failed: 5*7*11 is a product of primes"

if __name__ == "__main__": # pragma: no cover
    test_is_multiply_prime()
