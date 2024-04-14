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
    assert change_base(8, 3) == '22', "Failed on input (8, 3)"
    assert change_base(8, 2) == '1000', "Failed on input (8, 2)"
    assert change_base(7, 2) == '111', "Failed on input (7, 2)"
    assert change_base(0, 2) == '', "Failed on input (0, 2), expected empty string for 0 input"
    assert change_base(15, 8) == '17', "Failed on input (15, 8)"
    assert change_base(255, 16) == 'ff', "Failed on input (255, 16), make sure to handle base larger than 10 correctly"

if __name__ == "__main__": # pragma: no cover
    test_change_base()
