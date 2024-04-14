"""Write a function that accepts a list of strings.
The list contains different words. Return the word with maximum number
of unique characters. If multiple strings have maximum number of unique
characters, return the one which comes first in lexicographical order.

find_max(["name", "of", "string"]) == "string"
find_max(["name", "enam", "game"]) == "enam"
find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
"""

def find_max(words):
    return sorted(words, key = lambda x: (-len(set(x)), x))[0]

def test_find_max(): # pragma: no cover
    global find_max

    assert find_max(["name", "of", "string"]) == "string", "Test case 1 failed"
    assert find_max(["name", "enam", "game"]) == "enam", "Test case 2 failed"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa", "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_find_max()
