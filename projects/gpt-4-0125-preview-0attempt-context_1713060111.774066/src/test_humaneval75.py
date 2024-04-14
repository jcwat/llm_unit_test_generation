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
    # Test case with a known multiplication of 3 prime numbers
    assert is_multiply_prime(30) == True, "Test case 1 failed: 30 is multiple of 2, 3, and 5"
    # Test case with a prime number
    assert is_multiply_prime(7) == False, "Test case 2 failed: 7 is a prime, not a multiplication of 3 primes"
    # Test case with a multiplication of 2 primes
    assert is_multiply_prime(15) == False, "Test case 3 failed: 15 is multiple of 2 primes (3 and 5), not 3"
    # Test case with a number that is not a multiplication of primes
    assert is_multiply_prime(64) == False, "Test case 4 failed: 64 is not a multiplication of 3 distinct prime numbers"
    # Test case with a large number that is a multiplication of 3 primes
    assert is_multiply_prime(2*3*7) == True, "Test case 5 failed: 42 is multiple of 2, 3, and 7"
    # Test case with 1, should return False since 1 is not a prime number
    assert is_multiply_prime(1) == False, "Test case 6 failed: 1 is not a multiplication of 3 primes"

if __name__ == "__main__": # pragma: no cover
    test_is_multiply_prime()
