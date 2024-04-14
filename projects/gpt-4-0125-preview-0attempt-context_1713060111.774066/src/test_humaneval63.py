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
    global fibfib
    assert fibfib(0) == 0, "Test case fibfib(0) failed"
    assert fibfib(1) == 0, "Test case fibfib(1) failed"
    assert fibfib(2) == 1, "Test case fibfib(2) failed"
    assert abs(fibfib(5) - 4) <= 1e-5, "Test case fibfib(5) failed"
    assert abs(fibfib(8) - 24) <= 1e-5, "Test case fibfib(8) failed"

if __name__ == "__main__": # pragma: no cover
    test_fibfib()
