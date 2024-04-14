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
    
    # Test case 1: Basic test case
    input_str = "hello world hello"
    expected_output = {"hello": 2, "world": 1}
    assert histogram(input_str) == expected_output, "Test case 1 failed"
    
    # Test case 2: Empty input string
    input_str = ""
    expected_output = {}
    assert histogram(input_str) == expected_output, "Test case 2 failed"
    
    # Test case 3: Input string with special characters
    input_str = "apple orange$ apple orange apple$ orange"
    expected_output = {"apple": 3, "orange$": 2}
    assert histogram(input_str) == expected_output, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_histogram()
