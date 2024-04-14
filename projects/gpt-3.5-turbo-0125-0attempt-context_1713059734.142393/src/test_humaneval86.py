"""
Write a function that takes a string and returns an ordered version of it.
Ordered version of string, is a string where all words (separated by space)
are replaced by a new word where all the characters arranged in
ascending order based on ascii value.
Note: You should keep the order of words and blank spaces in the sentence.

For example:
anti_shuffle('Hi') returns 'Hi'
anti_shuffle('hello') returns 'ehllo'
anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
"""

def anti_shuffle(s):
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])

def test_anti_shuffle(): # pragma: no cover
    global anti_shuffle

    assert anti_shuffle('Hi') == 'Hi', "Test case 1 failed"
    assert anti_shuffle('hello') == 'ehllo', "Test case 2 failed"
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor', "Test case 3 failed"
    assert anti_shuffle('abc def ghi') == 'abc def ghi', "Test case 4 failed"
    assert anti_shuffle('123 456 789') == '123 456 789', "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_anti_shuffle()
