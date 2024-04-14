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
    global math
    assert fib4(0) == 0, "Test case for n=0 failed"
    assert fib4(1) == 0, "Test case for n=1 failed"
    assert fib4(2) == 2, "Test case for n=2 failed"
    assert fib4(3) == 0, "Test case for n=3 failed"
    assert fib4(4) == 2, "Test case for n=4 failed"
    assert fib4(5) == 4, "Test case for n=5 failed"
    assert fib4(6) == 8, "Test case for n=6 failed"
    assert fib4(7) == 14, "Test case for n=7 failed"
    assert fib4(8) == 26, "Test case for n=8 failed"
if __name__ == "__main__": # pragma: no cover
    test_fib4()
