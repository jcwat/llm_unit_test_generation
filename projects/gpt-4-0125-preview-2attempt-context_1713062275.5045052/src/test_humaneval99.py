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
    global closest_integer, math, floor, ceil
    assert closest_integer("10") == 10, "Test case 1 failed: closest_integer('10') should return 10"
    assert closest_integer("15.3") == 15, "Test case 2 failed: closest_integer('15.3') should return 15"
    assert closest_integer("14.5") == 15, "Test case 3 failed: closest_integer('14.5') should round away from zero to 15"
    assert closest_integer("-14.5") == -15, "Test case 4 failed: closest_integer('-14.5') should round away from zero to -15"
    assert closest_integer("0.0") == 0, "Test case 5 failed: closest_integer('0.0') should return 0"
    assert closest_integer("-2.999") == -3, "Test case 6 failed: closest_integer('-2.999') should be rounded to -3"
    assert closest_integer("2.999") == 3, "Test case 7 failed: closest_integer('2.999') should be rounded to 3"
    assert closest_integer("-0.1") == 0, "Test case 8 failed: closest_integer('-0.1') should be rounded to 0"
    assert closest_integer("0.1") == 0, "Test case 9 failed: closest_integer('0.1') should be rounded to 0"
    assert closest_integer("") == 0, "Test case 10 failed: closest_integer('') should handle empty string by returning 0"

if __name__ == "__main__": # pragma: no cover
    test_closest_integer()
