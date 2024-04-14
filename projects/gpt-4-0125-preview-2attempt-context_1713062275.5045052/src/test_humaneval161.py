"""You are given a string s.
if s[i] is a letter, reverse its case from lower to upper or vise versa, 
otherwise keep it as it is.
If the string contains no letters, reverse the string.
The function should return the resulted string.
Examples
solve("1234") = "4321"
solve("ab") = "AB"
solve("#a@C") = "#A@c"
"""

def solve(s):
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s

def test_solve(): # pragma: no cover
    global solve
    assert solve("1234") == "4321", "Test case 1 failed"
    assert solve("ab") == "AB", "Test case 2 failed"
    assert solve("#a@C") == "#A@c", "Test case 3 failed"
    assert solve("") == "", "Test case 4 failed"
    assert solve("ABC") == "abc", "Test case 5 failed"
    assert solve("a1B2") == "A1b2", "Test case 6 failed"
    assert solve("!!") == "!!", "Test case 7 failed"

if __name__ == "__main__": # pragma: no cover
    test_solve()
