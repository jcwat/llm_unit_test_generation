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
    assert add(2, 3) == 5, "Failed for add(2, 3)"
    assert add(5, 7) == 12, "Failed for add(5, 7)"

if __name__ == "__main__": # pragma: no cover
    test_add()
