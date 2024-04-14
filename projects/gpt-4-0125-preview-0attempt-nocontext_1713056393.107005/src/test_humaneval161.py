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

    # Test case when string has letters and they need to be swapped
    result = solve("#a@C")
    assert result == "#A@c", f"Expected '#A@c', got '{result}'"

    # Test case when string is all digits and needs to be reversed
    result = solve("1234")
    assert result == "4321", f"Expected '4321', got '{result}'"

    # Test case when string has both letters and they need to be swapped along with digits/special characters
    result = solve("aB12")
    assert result == "Ab12", f"Expected 'Ab12', got '{result}'"

    # Test empty string case
    result = solve("")
    assert result == "", "Expected '', got '{result}'"

    # Test case when string has no letters and it's not just digits (special symbols included)
    result = solve("!?@123")
    assert result == "321@?!", f"Expected '321@?!', got '{result}'"

if __name__ == "__main__": # pragma: no cover
    test_solve()
