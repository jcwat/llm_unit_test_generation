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
    assert split_words("Hello world!") == ["Hello", "world!"], "Failed on input 'Hello world!'"
    assert split_words("Hello,world!") == ["Hello", "world!"], "Failed on input 'Hello,world!'"
    assert split_words("abcdef") == 3, "Failed on input 'abcdef'"
    assert split_words("ABC EFG") == ["ABC", "EFG"], "Failed on input 'ABC EFG'"
    assert split_words("NoSpacesOrCommas") == 4, "Failed on updated input 'NoSpacesOrCommas'"

if __name__ == "__main__": # pragma: no cover
    test_split_words()
