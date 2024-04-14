"""Given a string s and a natural number n, you have been tasked to implement 
a function that returns a list of all words from string s that contain exactly 
n consonants, in order these words appear in the string s.
If the string s is empty then the function should return an empty list.
Note: you may assume the input string contains only letters and spaces.
Examples:
select_words("Mary had a little lamb", 4) ==> ["little"]
select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
select_words("simple white space", 2) ==> []
select_words("Hello world", 4) ==> ["world"]
select_words("Uncle sam", 3) ==> ["Uncle"]
"""

def select_words(s, n):
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n:
            result.append(word)
    return result


def test_select_words(): # pragma: no cover
    global select_words
    assert select_words("Mary had a little lamb", 4) == ["little"], "Test case 1 failed"
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"], "Test case 2 failed"
    assert select_words("simple white space", 2) == [], "Test case 3 failed"
    assert select_words("Hello world", 4) == ["world"], "Test case 4 failed"
    assert select_words("Uncle sam", 3) == ["Uncle"], "Test case 5 failed"
    assert select_words("", 3) == [], "Test case 6 failed for empty string"
    assert select_words("This is a test with multiple correct words", 1) == ["a"], "Test case 7 failed"
    assert select_words("A E I O U", 0) == ["A", "E", "I", "O", "U"], "Test case 8 failed with only vowels"

if __name__ == "__main__": # pragma: no cover
    test_select_words()
