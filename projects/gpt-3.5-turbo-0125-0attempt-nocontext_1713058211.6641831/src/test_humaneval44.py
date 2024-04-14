"""Change numerical base of input number x to base.
return string representation after the conversion.
base numbers are less than 10.
>>> change_base(8, 3)
'22'
>>> change_base(8, 2)
'1000'
>>> change_base(7, 2)
'111'
"""


def change_base(x: int, base: int):
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret

def test_change_base(): # pragma: no cover
    global test_change_base
    assert change_base(10, 2) == "1010", "Test case 1 failed"
    assert change_base(16, 8) == "20", "Test case 2 failed"
    assert change_base(25, 16) == "19", "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_change_base()
