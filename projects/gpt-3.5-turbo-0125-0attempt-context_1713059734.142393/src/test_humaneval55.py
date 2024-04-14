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
    assert fib(0) == 0, "Test case n=0 failed"
    assert fib(1) == 1, "Test case n=1 failed"
    assert fib(2) == 1, "Test case n=2 failed"
    assert fib(3) == 2, "Test case n=3 failed"
    assert fib(4) == 3, "Test case n=4 failed"
    assert fib(5) == 5, "Test case n=5 failed"
    assert fib(6) == 8, "Test case n=6 failed"
    assert fib(7) == 13, "Test case n=7 failed"
if __name__ == "__main__": # pragma: no cover
    test_fib()
