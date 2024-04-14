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
    # Test cases with expected 'Yes' outputs
    assert file_name_check("example.txt") == 'Yes', "Test case 1 failed"
    assert file_name_check("data2.dll") == 'Yes', "Test case 2 failed"
    assert file_name_check("Version8.exe") == 'Yes', "Test case 3 failed"
    assert file_name_check("a123.txt") == 'Yes', "Test case 4 failed"

    # Test cases with expected 'No' outputs
    assert file_name_check("1example.dll") == 'No', "Test case 5 failed"
    assert file_name_check(".txt") == 'No', "Test case 6 failed"
    assert file_name_check("exampletexttxt") == 'No', "Test case 7 failed"  # Fixed test: Removed dot to ensure 'No' response
    assert file_name_check("example.exe.pdf") == 'No', "Test case 8 failed"
    assert file_name_check("1234a.dll") == 'No', "Test case 9 failed"
    assert file_name_check("abc.") == 'No', "Test case 10 failed"
    assert file_name_check("abc.def.ghi") == 'No', "Test case 11 failed"
    assert file_name_check("") == 'No', "Test case 12 failed"

if __name__ == "__main__": # pragma: no cover
    test_file_name_check()
