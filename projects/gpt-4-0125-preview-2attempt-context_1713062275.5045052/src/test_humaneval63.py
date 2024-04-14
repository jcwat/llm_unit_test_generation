"""The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
fibfib(0) == 0
fibfib(1) == 0
fibfib(2) == 1
fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
Please write a function to efficiently compute the n-th element of the fibfib number sequence.
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
"""


def fibfib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

def test_fibfib(): # pragma: no cover
    global test_fibfib, fibfib
    assert fibfib(0) == 0, "Test for fibfib(0) failed"
    assert fibfib(1) == 0, "Test for fibfib(1) failed"
    assert fibfib(2) == 1, "Test for fibfib(2) failed"
    assert fibfib(3) == 1, "Test for fibfib(3) failed"
    assert fibfib(4) == 2, "Test for fibfib(4) failed"
    assert fibfib(5) == 4, "Test for fibfib(5) failed"
    assert fibfib(6) == 7, "Test for fibfib(6) failed"
    assert fibfib(8) == 24, "Test for fibfib(8) failed"
    assert abs(fibfib(10) - 81) <= 1e-5, "Test for fibfib(10) failed"

if __name__ == "__main__": # pragma: no cover
    test_fibfib()
