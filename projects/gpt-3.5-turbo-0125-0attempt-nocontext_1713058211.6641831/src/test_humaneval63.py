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
    global test_fibfib
    assert fibfib(0) == 0, "Test case n=0 failed"
    assert fibfib(1) == 0, "Test case n=1 failed"
    assert fibfib(2) == 1, "Test case n=2 failed"
    assert fibfib(3) == 1, "Test case n=3 failed"
    assert fibfib(4) == 2, "Test case n=4 failed"
    assert fibfib(5) == 4, "Test case n=5 failed"
    assert fibfib(6) == 7, "Test case n=6 failed"
if __name__ == "__main__": # pragma: no cover
    test_fibfib()
