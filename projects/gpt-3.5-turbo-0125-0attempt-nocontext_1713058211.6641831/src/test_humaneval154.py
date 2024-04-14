"""You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
cycpattern_check("abcd","abd") => False
cycpattern_check("hello","ell") => True
cycpattern_check("whassup","psus") => False
cycpattern_check("abab","baa") => True
cycpattern_check("efef","eeff") => False
cycpattern_check("himenss","simen") => True

"""

def cycpattern_check(a , b):
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False

def test_cycpattern_check(): # pragma: no cover
    global test_cycpattern_check
    
    assert cycpattern_check("hello", "lohel") == True, "Test case 1 failed"
    assert cycpattern_check("coding", "ingcod") == True, "Test case 2 failed"
    assert cycpattern_check("python", "python") == True, "Test case 3 failed"
    assert cycpattern_check("programming", "grammingpro") == False, "Test case 4 failed"
    assert cycpattern_check("abc", "def") == False, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_cycpattern_check()
