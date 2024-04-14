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
    global fib
    assert fib(10) == 55, "Test case for n=10 failed"
    assert fib(1) == 1, "Test case for n=1 failed"
    assert fib(8) == 21, "Test case for n=8 failed"
    assert fib(5) == 5, "Test case for n=5 failed"
if __name__ == "__main__": # pragma: no cover
    test_fib()
