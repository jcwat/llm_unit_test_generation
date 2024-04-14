"""Write a function vowels_count which takes a string representing
a word as input and returns the number of vowels in the string.
Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
vowel, but only when it is at the end of the given word.

Example:
>>> vowels_count("abcde")
2
>>> vowels_count("ACEDY")
3
"""

FIX = """
Add more test cases.
"""

def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels

def test_vowels_count(): # pragma: no cover
    global vowels_count
    assert vowels_count("abcde") == 2, "Test case 1 failed"
    assert vowels_count("test") == 1, "Test case 2 failed"
    assert vowels_count("ACEDY") == 3, "Test case 3 failed"
    assert vowels_count("rhythm") == 1, "Test case 4 failed - rhythm should count 'y' as vowel corrected"
    assert vowels_count("SYZYGY") == 1, "Test case 5 failed"
    assert vowels_count("qwrtyp") == 0, "Test case 6 failed"
    assert vowels_count("Y") == 1, "Test case 7 failed"
    assert vowels_count("y") == 1, "Test case 8 failed"
    assert vowels_count("AeIouY") == 6, "Test case 9 failed"
    assert vowels_count("aeiou") == 5, "Additional test case 10 failed"
    assert vowels_count("AEIOU") == 5, "Additional test case 11 failed"
    assert vowels_count("bcdfg") == 0, "Additional test case 12 failed"
    assert vowels_count("py") == 1, "Additional test case 13 failed - py should count 'y' as vowel"
    assert vowels_count("") == 0, "Additional test case 14 failed - Empty string should have 0 vowels"
if __name__ == "__main__": # pragma: no cover
    test_vowels_count()
