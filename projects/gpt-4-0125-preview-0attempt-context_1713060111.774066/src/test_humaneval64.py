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
    global test_vowels_count, vowels_count

    # Test lowercase
    assert vowels_count("abcde") == 2, "Test lowercase failed"
    assert vowels_count("rythm") == 0, "Test no vowel except y failed"
    assert vowels_count("fly") == 1, "Test y as a vowel at the end failed"
    assert vowels_count("encyclopedia") == 6, "Test multiple vowels failed"

    # Test uppercase
    assert vowels_count("ABCDE") == 2, "Test uppercase failed"
    assert vowels_count("FLY") == 1, "Test uppercase Y as vowel failed"
    assert vowels_count("RYTHM") == 0, "Test no vowel uppercase except Y failed"

    # Test mixed case and special characters
    assert vowels_count("Hello World") == 3, "Test mixed case failed"
    assert vowels_count("PythoN") == 1, "Test mixed case with Y at the end failed"

    # Test empty string
    assert vowels_count("") == 0, "Test empty string failed"

if __name__ == "__main__": # pragma: no cover
    test_vowels_count()
