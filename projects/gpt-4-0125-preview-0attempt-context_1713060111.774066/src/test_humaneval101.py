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
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"], "Test case 1 failed"
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"], "Test case 2 failed"
    assert words_string("") == [], "Test case 3 failed"
    assert words_string("Hello") == ["Hello"], "Test case 4 failed"
    assert words_string("A,B,C,D") == ["A", "B", "C", "D"], "Test case 5 failed"
    assert words_string("Spaces    and,commas,   mixed") == ["Spaces", "and", "commas", "mixed"], "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_words_string()
