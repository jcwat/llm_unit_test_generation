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
    global test_is_bored, is_bored
    assert is_bored("Hello world.") == 0, "Test case 1 failed"
    assert is_bored("I am feeling bored. What about you?") == 1, "Test case 2 failed"
    assert is_bored("The sky is blue. The sun is shining. I love this weather!") == 1, "Test case 3 failed"
    assert is_bored("I think I am bored. I cannot decide.") == 2, "Test case 4 failed"
    assert is_bored("") == 0, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_is_bored()
