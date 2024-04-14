'''
Write a function that takes an integer a and returns True 
if this ingeger is a cube of some integer number.
Note: you may assume the input is always valid.
Examples:
iscube(1) ==> True
iscube(2) ==> False
iscube(-1) ==> True
iscube(64) ==> True
iscube(0) ==> True
iscube(180) ==> False
'''

def iscube(a):
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a

def test_iscube(): # pragma: no cover
    global test_iscube, round, abs
    assert iscube(1) == True, "Test case 1 failed"
    assert iscube(2) == False, "Test case 2 failed"
    assert iscube(-1) == True, "Test case 3 failed"
    assert iscube(64) == True, "Test case 4 failed"
    assert iscube(0) == True, "Test case 5 failed"
    assert iscube(180) == False, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_iscube()
