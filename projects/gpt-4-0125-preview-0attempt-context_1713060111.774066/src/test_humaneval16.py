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
    assert count_distinct_characters('xyzXYZ') == 3, "Test case 1 failed: 'xyzXYZ' should have 3 distinct characters ignoring case"
    assert count_distinct_characters('Jerry') == 4, "Test case 2 failed: 'Jerry' should have 4 distinct characters"
    assert count_distinct_characters('') == 0, "Test case 3 failed: Empty string should have 0 distinct characters"
    assert count_distinct_characters('aaaaa') == 1, "Test case 4 failed: 'aaaaa' should have 1 distinct character"
    assert count_distinct_characters('AbCdEfGhIj') == 10, "Test case 5 failed: 'AbCdEfGhIj' should have 10 distinct characters ignoring case"

if __name__ == "__main__": # pragma: no cover
    test_count_distinct_characters()
