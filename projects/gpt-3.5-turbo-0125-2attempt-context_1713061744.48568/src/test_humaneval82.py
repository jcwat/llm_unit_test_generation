"""Write a function that takes a string and returns True if the string
length is a prime number or False otherwise
Examples
prime_length('Hello') == True
prime_length('abcdcba') == True
prime_length('kittens') == True
prime_length('orange') == False
"""

def prime_length(string):
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

def test_prime_length(): # pragma: no cover
    global prime_length
    assert prime_length('Hello') == True, "Test case 1 failed"
    assert prime_length('abcdcba') == True, "Test case 2 failed"
    assert prime_length('kittens') == True, "Test case 3 failed"
    assert prime_length('orange') == False, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_prime_length()
