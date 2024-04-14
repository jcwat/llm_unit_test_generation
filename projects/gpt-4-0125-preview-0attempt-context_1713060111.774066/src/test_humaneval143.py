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

    # Test case 1
    input_sentence = "This is a test"
    expected_output = "is"
    assert words_in_sentence(input_sentence) == expected_output, f"Test case 1 failed: expected '{expected_output}', got '{words_in_sentence(input_sentence)}'"

    # Test case 2
    input_sentence = "lets go for swimming"
    expected_output = "go for"
    assert words_in_sentence(input_sentence) == expected_output, f"Test case 2 failed: expected '{expected_output}', got '{words_in_sentence(input_sentence)}'"

    # Test case 3
    input_sentence = "one three five seven eleven"
    expected_output = "three five seven eleven"
    assert words_in_sentence(input_sentence) == expected_output, f"Test case 3 failed: expected '{expected_output}', got '{words_in_sentence(input_sentence)}'"

    # Test case 4: Edge case with the smallest sentence (1 word, not prime)
    input_sentence = "a"
    expected_output = ""
    assert words_in_sentence(input_sentence) == expected_output, f"Test case 4 failed: expected '{expected_output}', got '{words_in_sentence(input_sentence)}'"

    # Test case 5: Edge case with prime length word
    input_sentence = "abcd"
    expected_output = ""
    assert words_in_sentence(input_sentence) == expected_output, f"Test case 5 failed: expected '{expected_output}', got '{words_in_sentence(input_sentence)}'"

if __name__ == "__main__": # pragma: no cover
    test_words_in_sentence()
