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
    assert count_upper("Hello, World!") == 1, "Test case 1 failed"
    assert count_upper("Python is Fun") == 2, "Test case 2 failed"
    assert count_upper("aEiOu") == 3, "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_count_upper()
