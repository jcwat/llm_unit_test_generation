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
    assert fibfib(0) == 0, "fibfib(0) should return 0"
    assert fibfib(1) == 0, "fibfib(1) should return 0"
    assert fibfib(2) == 1, "fibfib(2) should return 1"
    assert fibfib(3) == 1, "fibfib(3) should return 1"
    assert fibfib(4) == 2, "fibfib(4) should return 2"
    assert fibfib(5) == 4, "fibfib(5) should return 4"
    assert fibfib(6) == 7, "fibfib(6) should return 7"
    assert fibfib(8) == 24, "fibfib(8) should return 24"
    assert abs(fibfib(10) - 81) <= 1e-5, "fibfib(10) should return 81"

if __name__ == "__main__": # pragma: no cover
    test_fibfib()
