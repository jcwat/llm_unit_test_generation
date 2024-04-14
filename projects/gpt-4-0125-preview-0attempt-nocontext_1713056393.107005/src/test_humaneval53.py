"""Add two numbers x and y
>>> add(2, 3)
5
>>> add(5, 7)
12
"""


def add(x: int, y: int):
    return x + y

def test_add(): # pragma: no cover
    global test_add
    assert add(2, 3) == 5, "Test case 1 failed"
    assert add(5, 7) == 12, "Test case 2 failed"
    assert add(-1, 1) == 0, "Test case 3 failed"
    assert add(0, 0) == 0, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_add()
