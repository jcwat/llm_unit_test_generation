"""Task
Write a function that takes a string as input and returns the sum of the upper characters only'
ASCII codes.

Examples:
digitSum("") => 0
digitSum("abAB") => 131
digitSum("abcCd") => 67
digitSum("helloE") => 69
digitSum("woArBld") => 131
digitSum("aAaaaXa") => 153
"""

def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

def test_digitSum(): # pragma: no cover
    global test_digitSum, digitSum
    assert digitSum("") == 0, "Test case 1 failed"
    assert digitSum("abAB") == 131, "Test case 2 failed"
    assert digitSum("abcCd") == 67, "Test case 3 failed"
    assert digitSum("helloE") == 69, "Test case 4 failed"
    assert digitSum("woArBld") == 131, "Test case 5 failed"
    assert digitSum("aAaaaXa") == 153, "Test case 6 failed"
    assert abs(digitSum("Z") - 90) < 1e-5, "Test case 7 failed"

if __name__ == "__main__": # pragma: no cover
    test_digitSum()
