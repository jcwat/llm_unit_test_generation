"""Given a string representing a space separated lowercase letters, return a dictionary
of the letter with the most repetition and containing the corresponding count.
If several letters have the same occurrence, return all of them.

Example:
histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
histogram('a b b a') == {'a': 2, 'b': 2}
histogram('a b c a b') == {'a': 2, 'b': 2}
histogram('b b b b a') == {'b': 4}
histogram('') == {}

"""

def histogram(test):
    dict1={}
    list1=test.split(" ")
    t=0

    for i in list1:
        if(list1.count(i)>t) and i!='':
            t=list1.count(i)
    if t>0:
        for i in list1:
            if(list1.count(i)==t):
                
                dict1[i]=t
    return dict1

def test_histogram(): # pragma: no cover
    global histogram
    assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}, "Test case 1 failed"
    assert histogram('a b b a') == {'a': 2, 'b': 2}, "Test case 2 failed"
    assert histogram('a b c a b') == {'a': 2, 'b': 2}, "Test case 3 failed"
    assert histogram('b b b b a') == {'b': 4}, "Test case 4 failed"
    assert histogram('') == {}, "Test case 5 failed"
    assert histogram('e e e e d d d c c b a') == {'e': 4}, "Test case 6 failed"
    assert histogram('x') == {'x': 1}, "Test case 7 failed"
    assert histogram('f f g h i j k f g h') == {'f': 3, 'g':2, 'h': 2}, "Test case 8 failed, should handle multiple instances with the same and different occurrences"

if __name__ == "__main__": # pragma: no cover
    test_histogram()
