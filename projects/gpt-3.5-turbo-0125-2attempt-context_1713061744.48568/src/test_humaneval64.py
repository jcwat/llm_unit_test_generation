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
    assert vowels_count("ACEDY") == 3, "Test case 2 failed"
    assert vowels_count("tESt") == 1, "Test case 3 failed"
    assert vowels_count("why") == 1, "Test case 4 failed"
    assert vowels_count("pythOn") == 2, "Test case 5 failed"
    assert vowels_count("HELLO") == 2, "Test case 6 failed"
    assert vowels_count("word") == 1, "Test case 7 failed"
    assert vowels_count("PYTHON!") == 2, "Test case 8 failed"
    assert vowels_count("Python") == 2, "Test case 9 failed"
    assert vowels_count("y") == 1, "Test case 10 failed"
    assert vowels_count("Y") == 1, "Test case 11 failed"
if __name__ == "__main__": # pragma: no cover
    test_vowels_count()
