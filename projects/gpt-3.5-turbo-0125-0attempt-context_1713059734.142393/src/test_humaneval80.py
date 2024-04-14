"""You are given a string s.
Your task is to check if the string is happy or not.
A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
For example:
is_happy(a) => False
is_happy(aa) => False
is_happy(abcd) => True
is_happy(aabb) => False
is_happy(adb) => True
is_happy(xyy) => False
"""

def is_happy(s):
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True

def test_is_happy(): # pragma: no cover
    global is_happy

    assert is_happy("a") == False, "Test case 1 failed"
    assert is_happy("aa") == False, "Test case 2 failed"
    assert is_happy("abcd") == True, "Test case 3 failed"
    assert is_happy("aabb") == False, "Test case 4 failed"
    assert is_happy("adb") == True, "Test case 5 failed"
    assert is_happy("xyy") == False, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_is_happy()
