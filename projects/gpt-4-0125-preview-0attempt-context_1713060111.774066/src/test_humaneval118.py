"""You are given a word. Your task is to find the closest vowel that stands between 
two consonants from the right side of the word (case sensitive).

Vowels in the beginning and ending doesn't count. Return empty string if you didn't
find any vowel met the above condition. 

You may assume that the given string contains English letter only.

Example:
get_closest_vowel("yogurt") ==> "u"
get_closest_vowel("FULL") ==> "U"
get_closest_vowel("quick") ==> ""
get_closest_vowel("ab") ==> ""
"""

def get_closest_vowel(word):
    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return ""

def test_get_closest_vowel(): # pragma: no cover
    global get_closest_vowel
    assert get_closest_vowel("yogurt") == "u", "Test case 1 failed"
    assert get_closest_vowel("FULL") == "U", "Test case 2 failed"
    assert get_closest_vowel("quick") == "", "Test case 3 failed"
    assert get_closest_vowel("ab") == "", "Test case 4 failed"
    assert get_closest_vowel("programming") == "a", "Test case 5 failed"
    assert get_closest_vowel("AeIou") == "", "Test case 6 failed"
    assert get_closest_vowel("b") == "", "Test case 7 failed"
    assert get_closest_vowel("Bat") == "", "Test case 8 failed"

if __name__ == "__main__": # pragma: no cover
    test_get_closest_vowel()
