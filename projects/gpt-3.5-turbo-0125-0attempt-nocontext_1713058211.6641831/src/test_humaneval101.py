"""
You will be given a string of words separated by commas or spaces. Your task is
to split the string into words and return an array of the words.

For example:
words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
"""

def words_string(s):
    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()

def test_words_string(): # pragma: no cover
    global words_string
    
    # Test with empty string
    assert words_string("") == [], "Empty string test failed"
    
    # Test with string containing only one word
    assert words_string("hello") == ["hello"], "Single word test failed"
    
    # Test with string containing multiple words separated by commas
    assert words_string("hello,world") == ["hello", "world"], "Multiple words test failed"
    
    # Test with string containing spaces
    assert words_string("hello, my,   world") == ["hello", "my", "world"], "String with spaces test failed"

if __name__ == "__main__": # pragma: no cover
    test_words_string()
