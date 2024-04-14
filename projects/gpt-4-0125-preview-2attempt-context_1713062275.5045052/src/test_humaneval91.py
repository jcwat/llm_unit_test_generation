"""
You'll be given a string of words, and your task is to count the number
of boredoms. A boredom is a sentence that starts with the word "I".
Sentences are delimited by '.', '?' or '!'.
   
For example:
>>> is_bored("Hello world")
0
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
"""

def is_bored(S):
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)

def test_is_bored(): # pragma: no cover
    global is_bored, re
    assert is_bored("I am feeling bored. I am tired!") == 2, "Test case 1 failed"
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1, "Test case 2 failed"
    assert is_bored("Hello world") == 0, "Test case 3 failed"
    assert is_bored("I wonder. I think. I am!") == 3, "Test case 4 failed"
    assert is_bored("") == 0, "Test case 5 failed"
    assert is_bored("Is it me? Or is it you?") == 0, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_is_bored()
