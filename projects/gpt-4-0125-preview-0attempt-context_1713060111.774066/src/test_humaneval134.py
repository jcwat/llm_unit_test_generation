'''
Create a function that returns True if the last character
of a given string is an alphabetical character and is not
a part of a word, and False otherwise.
Note: "word" is a group of characters separated by space.

Examples:
check_if_last_char_is_a_letter("apple pie") ➞ False
check_if_last_char_is_a_letter("apple pi e") ➞ True
check_if_last_char_is_a_letter("apple pi e ") ➞ False
check_if_last_char_is_a_letter("") ➞ False 
'''

def check_if_last_char_is_a_letter(txt):
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

def test_check_if_last_char_is_a_letter(): # pragma: no cover
    global check_if_last_char_is_a_letter
    assert check_if_last_char_is_a_letter("apple pie") is False, "Test case 1 failed: Expected False for 'apple pie'"
    assert check_if_last_char_is_a_letter("apple pi e") is True, "Test case 2 failed: Expected True for 'apple pi e'"
    assert check_if_last_char_is_a_letter("apple pi e ") is False, "Test case 3 failed: Expected False for 'apple pi e '"
    assert check_if_last_char_is_a_letter("") is False, "Test case 4 failed: Expected False for empty string"
    assert check_if_last_char_is_a_letter(" ") is False, "Test case 5 failed: Expected False for single space"
    assert check_if_last_char_is_a_letter("a") is True, "Test case 6 failed: Expected True for single letter 'a'"
    assert check_if_last_char_is_a_letter("a!") is False, "Test case 7 failed: Expected False for 'a!'"
    
if __name__ == "__main__": # pragma: no cover
    test_check_if_last_char_is_a_letter()
