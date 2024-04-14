"""Return n-th Fibonacci number.
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
"""


def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def test_fib(): # pragma: no cover
    global test_fib
    assert fib(10) == 55, "Test case 1 failed"
    assert fib(1) == 1, "Test case 2 failed"
    assert fib(8) == 21, "Test case 3 failed"
    assert fib(0) == 0, "Test case 4 failed"
    assert abs(fib(20) - 6765) <= 1e-5, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_fib()
