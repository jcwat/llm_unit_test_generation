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
    # Test for a product of 3 prime numbers
    assert is_multiply_prime(30) == True, "Test case 1 failed: 30 is a product of primes 2, 3, 5"
    # Test for a prime number itself
    assert is_multiply_prime(13) == False, "Test case 2 failed: 13 is a prime but not a product of 3 primes"
    # Test for a number that is not a product of any number of primes
    assert is_multiply_prime(64) == False, "Test case 3 failed: 64 is not a product of 3 primes"
    # Test for a number that is a product of 2 primes
    assert is_multiply_prime(15) == False, "Test case 4 failed: 15 is a product of 2 primes, not 3"
    # Test for 1, which is neither prime nor a product of primes
    assert is_multiply_prime(1) == False, "Test case 5 failed: 1 is not a product of 3 primes"

if __name__ == "__main__": # pragma: no cover
    test_is_multiply_prime()
