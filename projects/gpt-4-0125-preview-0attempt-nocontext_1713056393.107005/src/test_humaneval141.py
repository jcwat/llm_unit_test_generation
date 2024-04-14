"""Create a function which takes a string representing a file's name, and returns
'Yes' if the the file's name is valid, and returns 'No' otherwise.
A file's name is considered to be valid if and only if all the following conditions 
are met:
- There should not be more than three digits ('0'-'9') in the file's name.
- The file's name contains exactly one dot '.'
- The substring before the dot should not be empty, and it starts with a letter from 
the latin alphapet ('a'-'z' and 'A'-'Z').
- The substring after the dot should be one of these: ['txt', 'exe', 'dll']
Examples:
file_name_check("example.txt") # => 'Yes'
file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
"""

def file_name_check(file_name):
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'

def test_file_name_check(): # pragma: no cover
    global file_name_check

    # Test for valid names
    assert file_name_check("example.txt") == 'Yes', "Test case 1 failed - should have been a valid name."
    assert file_name_check("A2B3.dll") == 'Yes', "Test case 2 failed - should have been valid with digits < 4 and valid extension."
    assert file_name_check("File123.exe") == 'Yes', "Test case 3 failed - should have been valid with exactly 3 digits."

    # Test for invalid names
    assert file_name_check("1example.dll") == 'No', "Test case 4 failed - should be invalid as it starts with a digit."
    assert file_name_check("example1234.txt") == 'No', "Test case 5 failed - should be invalid with more than 3 digits."
    assert file_name_check("noextension") == 'No', "Test case 6 failed - should be invalid without a dot."
    assert file_name_check(".dll") == 'No', "Test case 7 failed - should be invalid with empty filename before dot."
    assert file_name_check("example.doc") == 'No', "Test case 8 failed - should be invalid with wrong extension."
    assert file_name_check("example..txt") == 'No', "Test case 9 failed - should be invalid with more than one dot."

if __name__ == "__main__": # pragma: no cover
    test_file_name_check()
