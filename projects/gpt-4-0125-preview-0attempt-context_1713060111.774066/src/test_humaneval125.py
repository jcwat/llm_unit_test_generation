'''
Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
Examples
split_words("Hello world!") ➞ ["Hello", "world!"]
split_words("Hello,world!") ➞ ["Hello", "world!"]
split_words("abcdef") == 3 
'''

def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])

def test_split_words(): # pragma: no cover
    global split_words
    assert split_words("Hello world!") == ["Hello", "world!"], "Test case 1 failed"
    assert split_words("Hello,world!") == ["Hello", "world!"], "Test case 2 failed"
    assert split_words("abcdef") == 3, "Test case 3 failed"
    assert split_words("Testing,without spaces") == ["Testing", "without", "spaces"], "Test case 4 failed"
    assert split_words("abcABC") == 2, "Test case 5 failed"
    assert split_words("") == 0, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_split_words()
