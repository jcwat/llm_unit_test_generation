"""The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
fib4(0) -> 0
fib4(1) -> 0
fib4(2) -> 2
fib4(3) -> 0
fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
>>> fib4(5)
4
>>> fib4(6)
8
>>> fib4(7)
14
"""


def fib4(n: int):
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]

def test_fib4(): # pragma: no cover
    global fib4
    assert fib4(0) == 0, "Test case fib4(0) failed"
    assert fib4(1) == 0, "Test case fib4(1) failed"
    assert fib4(2) == 2, "Test case fib4(2) failed"
    assert fib4(3) == 0, "Test case fib4(3) failed"
    assert abs(fib4(5) - 4) <= 1e-5, "Test case fib4(5) failed"
    assert abs(fib4(6) - 8) <= 1e-5, "Test case fib4(6) failed"
    assert abs(fib4(7) - 14) <= 1e-5, "Test case fib4(7) failed"

if __name__ == "__main__": # pragma: no cover
    test_fib4()
