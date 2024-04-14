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
    assert file_name_check("example.txt") == 'Yes', "Test case 1 failed"
    assert file_name_check("1example.dll") == 'No', "Test case 2 failed"
    assert file_name_check("example_only") == 'No', "Test case 3 failed"
    assert file_name_check("txtfile..txt") == 'No', "Test case 4 failed"
    assert file_name_check("testFile.exe") == 'Yes', "Test case 5 failed"
if __name__ == "__main__": # pragma: no cover
    test_file_name_check()