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
    assert add(3, 5) == 8, "Sum of 3 and 5 should be 8"
    assert add(-3, -5) == -8, "Sum of -3 and -5 should be -8"
    assert add(0, 0) == 0, "Sum of 0 and 0 should be 0"
if __name__ == "__main__": # pragma: no cover
    test_add()
