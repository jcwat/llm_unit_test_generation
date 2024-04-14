"""
You are given a string representing a sentence,
the sentence contains some words separated by a space,
and you have to return a string that contains the words from the original sentence,
whose lengths are prime numbers,
the order of the words in the new string should be the same as the original one.

Example 1:
Input: sentence = "This is a test"
Output: "is"

Example 2:
Input: sentence = "lets go for swimming"
Output: "go for"

Constraints:
* 1 <= len(sentence) <= 100
* sentence contains only letters
"""

def words_in_sentence(sentence):
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)

def test_words_in_sentence(): # pragma: no cover
    global words_in_sentence

    assert words_in_sentence("This is a test") == "is", "Test case 1 failed"
    assert words_in_sentence("lets go for swimming") == "go for", "Test case 2 failed"
    assert words_in_sentence("Prime numbers are 2, 3, 5, 7, 11, etc.") == "2 3 5 7 11", "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_words_in_sentence()
