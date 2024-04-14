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
    global test_digitSum
    assert digitSum("") == 0, "Empty string case failed"
    assert digitSum("ABC") == 198, "Uppercase letters only case failed"
    assert digitSum("abc") == 0, "Lowercase letters only case failed"
    assert digitSum("aBcDeF") == 321, "Mix of uppercase and lowercase letters case failed"
if __name__ == "__main__": # pragma: no cover
    test_digitSum()
