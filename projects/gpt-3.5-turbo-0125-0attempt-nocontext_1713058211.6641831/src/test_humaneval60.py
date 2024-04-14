"""sum_to_n is a function that sums numbers from 1 to n.
>>> sum_to_n(30)
465
>>> sum_to_n(100)
5050
>>> sum_to_n(5)
15
>>> sum_to_n(10)
55
>>> sum_to_n(1)
1
"""


def sum_to_n(n: int):
    return sum(range(n + 1))

def test_sum_to_n(): # pragma: no cover
    global sum_to_n
    assert sum_to_n(0) == 0, "Test case 1 failed"
    assert sum_to_n(1) == 1, "Test case 2 failed"
    assert sum_to_n(5) == 15, "Test case 3 failed"
    assert sum_to_n(10) == 55, "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_sum_to_n()
