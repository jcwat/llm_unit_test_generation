"""Return 2^n modulo p (be aware of numerics).
>>> modp(3, 5)
3
>>> modp(1101, 101)
2
>>> modp(0, 101)
1
>>> modp(3, 11)
8
>>> modp(100, 101)
1
"""


def modp(n: int, p: int):
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret

def test_modp(): # pragma: no cover
    global test_modp
    assert modp(3, 5) == 3, "Test case 1 failed"
    assert modp(1101, 101) == 2, "Test case 2 failed"
    assert modp(0, 101) == 1, "Test case 3 failed"
    assert modp(3, 11) == 8, "Test case 4 failed"
    assert modp(100, 101) == 1, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_modp()
