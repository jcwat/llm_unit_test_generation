"""
prime_fib returns n-th number that is a Fibonacci number and it's also prime.
>>> prime_fib(1)
2
>>> prime_fib(2)
3
>>> prime_fib(3)
5
>>> prime_fib(4)
13
>>> prime_fib(5)
89
"""


def prime_fib(n: int):
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]

def test_prime_fib(): # pragma: no cover
    global prime_fib, math
    assert prime_fib(1) == 2, "Test case 1 failed: prime_fib(1) should return 2"
    assert prime_fib(2) == 3, "Test case 2 failed: prime_fib(2) should return 3"
    assert prime_fib(3) == 5, "Test case 3 failed: prime_fib(3) should return 5"
    assert prime_fib(4) == 13, "Test case 4 failed: prime_fib(4) should return 13"
    assert prime_fib(5) == 89, "Test case 5 failed: prime_fib(5) should return 89"

if __name__ == "__main__": # pragma: no cover
    test_prime_fib()
