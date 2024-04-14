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
    assert count_distinct_characters('Mississippi') == 5, "Test case 3 failed"
    
if __name__ == "__main__": # pragma: no cover
    test_count_distinct_characters()
