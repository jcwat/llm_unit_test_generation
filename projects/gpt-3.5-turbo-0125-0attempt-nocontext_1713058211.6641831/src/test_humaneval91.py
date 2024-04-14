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
    assert is_bored("I am bored. Do you feel bored? I'm not bored!") == 2, "Test case 1 failed"
    assert is_bored("I feel excited. Are you bored? I am not bored at all.") == 1, "Test case 2 failed"
    assert is_bored("I'm bored. Are you bored too? I'm really bored!") == 3, "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_is_bored()
