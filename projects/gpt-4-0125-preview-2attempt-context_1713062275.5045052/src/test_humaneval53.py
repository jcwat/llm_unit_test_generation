"""Add two numbers x and y
>>> add(2, 3)
5
>>> add(5, 7)
12
"""


def add(x: int, y: int):
    return x + y

def test_add(): # pragma: no cover
    global add
    assert add(2, 3) == 5, "Adding 2 and 3 should equal 5"
    assert add(0, 0) == 0, "Adding 0 and 0 should equal 0"
    assert add(-1, -1) == -2, "Adding -1 and -1 should equal -2"
    assert add(100, 200) == 300, "Adding 100 and 200 should equal 300"

if __name__ == "__main__": # pragma: no cover
    test_add()
