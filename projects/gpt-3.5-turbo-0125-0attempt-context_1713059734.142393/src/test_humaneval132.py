'''
Create a function that takes a string as input which contains only square brackets.
The function should return True if and only if there is a valid subsequence of brackets 
where at least one bracket in the subsequence is nested.

is_nested('[[]]') ➞ True
is_nested('[]]]]]]][[[[[]') ➞ False
is_nested('[][]') ➞ False
is_nested('[]') ➞ False
is_nested('[[][]]') ➞ True
is_nested('[[]][[') ➞ True
'''

def is_nested(string):
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2

    

def test_is_nested(): # pragma: no cover
    global is_nested

    assert is_nested('[[]]') == True, "Test case 1 failed"
    assert is_nested('[]]]]]]][[[[[]') == False, "Test case 2 failed"
    assert is_nested('[][]') == False, "Test case 3 failed"
    assert is_nested('[]') == False, "Test case 4 failed"
    assert is_nested('[[][]]') == True, "Test case 5 failed"
    assert is_nested('[[]][[') == True, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_is_nested()
