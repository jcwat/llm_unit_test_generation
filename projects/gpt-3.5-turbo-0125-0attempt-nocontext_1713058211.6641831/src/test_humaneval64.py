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
    global test_vowels_count
    assert vowels_count("hello") == 2, "Test case 1 failed"
    assert vowels_count("HELLO") == 2, "Test case 2 failed"
    assert vowels_count("Python") == 2, "Test case 3 failed"
    assert vowels_count("why") == 1, "Test case 4 failed"
    assert vowels_count("rhythm") == 0, "Test case 5 failed"
if __name__ == "__main__": # pragma: no cover
    test_vowels_count()
