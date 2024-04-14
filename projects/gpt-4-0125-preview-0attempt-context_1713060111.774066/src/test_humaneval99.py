'''
Create a function that takes a value (string) representing a number
and returns the closest integer to it. If the number is equidistant
from two integers, round it away from zero.

Examples
>>> closest_integer("10")
10
>>> closest_integer("15.3")
15

Note:
Rounding away from zero means that if the given number is equidistant
from two integers, the one you should return is the one that is the
farthest from zero. For example closest_integer("14.5") should
return 15 and closest_integer("-14.5") should return -15.
'''

def closest_integer(value):
    from math import floor, ceil

    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res


def test_closest_integer(): # pragma: no cover
    global closest_integer, floor, ceil
    assert closest_integer("10") == 10, "Test with integer string failed"
    assert closest_integer("15.3") == 15, "Test rounding down failed"
    assert closest_integer("14.5") == 15, "Test rounding up (away from zero) failed"
    assert closest_integer("-14.5") == -15, "Test rounding up (away from zero for negative) failed"
    assert closest_integer("0.5") == 1, "Test rounding up from 0.5 failed"
    assert closest_integer("-2.5") == -3, "Test rounding down from -2.5 failed"
    assert closest_integer("") == 0, "Test with empty string failed"
    assert closest_integer("15.67") == 16, "Test with rounding up to next integer failed"
    assert closest_integer("-3.14") == -3, "Test with negative float rounding towards zero failed"
    assert closest_integer("0") == 0, "Test with string '0' failed"

if __name__ == "__main__": # pragma: no cover
    test_closest_integer()
