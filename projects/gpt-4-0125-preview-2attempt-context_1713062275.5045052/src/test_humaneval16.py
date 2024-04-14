""" Given a string, find out how many distinct characters (regardless of case) does it consist of
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
"""


def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

def test_count_distinct_characters(): # pragma: no cover
    global count_distinct_characters
    assert count_distinct_characters('xyzXYZ') == 3, "Test case 1 failed"
    assert count_distinct_characters('Jerry') == 4, "Test case 2 failed"
    assert count_distinct_characters('') == 0, "Test case 3 failed"
    assert count_distinct_characters('AaAa') == 1, "Test case 4 failed"
    assert count_distinct_characters('123abcABC') == 6, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_count_distinct_characters()
