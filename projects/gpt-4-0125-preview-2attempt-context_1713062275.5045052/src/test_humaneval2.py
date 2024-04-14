""" Given a positive floating point number, it can be decomposed into
and integer part (largest integer smaller than given number) and decimals
(leftover part always smaller than 1).

Return the decimal part of the number.
>>> truncate_number(3.5)
0.5
"""


def truncate_number(number: float) -> float:
    return number % 1.0

def test_truncate_number(): # pragma: no cover
    global test_truncate_number
    assert abs(truncate_number(3.5) - 0.5) < 1e-5, "Test case 1 failed"
    assert abs(truncate_number(10.123) - 0.123) < 1e-5, "Test case 2 failed"
    assert abs(truncate_number(0.9999999) - 0.9999999) < 1e-5, "Test case 3 failed"
    assert abs(truncate_number(5.0) - 0.0) < 1e-5, "Test case 4 failed"
    assert abs(truncate_number(123456.654321) - 0.654321) < 1e-5, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_truncate_number()
