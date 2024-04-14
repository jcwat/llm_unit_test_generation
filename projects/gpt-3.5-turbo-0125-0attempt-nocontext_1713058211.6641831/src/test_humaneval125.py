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
    
    # Test case 1: txt contains spaces
    assert split_words("hello world") == ['hello', 'world'], "Test case 1 failed"
    
    # Test case 2: txt contains comma
    assert split_words("apple,banana,grape") == ['apple', 'banana', 'grape'], "Test case 2 failed"
    
    # Test case 3: txt contains lowercase letters with even ascii values
    assert split_words("abcdefg") == 4, "Test case 3 failed"
    
    # Test case 4: txt contains lowercase letters with odd ascii values
    assert split_words("lmnopqrs") == 4, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_split_words()
