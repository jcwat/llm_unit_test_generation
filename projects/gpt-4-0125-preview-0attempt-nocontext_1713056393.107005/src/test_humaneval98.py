"""
Given a string s, count the number of uppercase vowels in even indices.

For example:
count_upper('aBCdEf') returns 1
count_upper('abcdefg') returns 0
count_upper('dBBE') returns 0
"""

def count_upper(s):
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count

def test_count_upper(): # pragma: no cover
    global count_upper
    assert count_upper("aBCdEf") == 0, "Test case 1 failed"
    assert count_upper("abcdefg") == 0, "Test case 2 failed"
    assert count_upper("dBBE") == 0, "Test case 3 failed"
    assert count_upper("ABECIDOFUG") == 4, "Test case 4 failed"
    assert count_upper("") == 0, "Test case 5 failed"
    assert count_upper("AE") == 1, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_count_upper()
