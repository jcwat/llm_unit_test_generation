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

    # Test with single occurrence of each letter
    assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}, "Test case 1 failed: single occurrences should match"

    # Test with multiple occurrences, two letters tie
    assert histogram('a b b a') == {'a': 2, 'b': 2}, "Test case 2 failed: multiple occurrences with a tie should match"

    # Test with multiple occurrences, tie among all letters
    assert histogram('a b c a b') == {'a': 2, 'b': 2}, "Test case 3 failed: all letters tying should match"

    # Test with only one letter repeating
    assert histogram('b b b b a') == {'b': 4}, "Test case 4 failed: one letter dominating should match"

    # Test with empty string
    assert histogram('') == {}, "Test case 5 failed: empty string should return empty dict"

    # Test with multiple spaces and tie
    assert histogram('a   a  b') == {'a': 2}, "Test case 6 failed: handling of multiple spaces failed"

if __name__ == "__main__": # pragma: no cover
    test_histogram()
