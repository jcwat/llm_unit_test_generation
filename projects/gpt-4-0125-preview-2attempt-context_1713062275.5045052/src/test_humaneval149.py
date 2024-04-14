"""Write a function that accepts a list of strings as a parameter,
deletes the strings that have odd lengths from it,
and returns the resulted list with a sorted order,
The list is always a list of strings and never an array of numbers,
and it may contain duplicates.
The order of the list should be ascending by length of each word, and you
should return the list sorted by that rule.
If two words have the same length, sort the list alphabetically.
The function should return a list of strings in sorted order.
You may assume that all words will have the same length.
For example:
assert list_sort(["aa", "a", "aaa"]) => ["aa"]
assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
"""

def sorted_list_sum(lst):
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)

def test_sorted_list_sum(): # pragma: no cover
    global sorted_list_sum
    assert sorted_list_sum(["ab", "a", "aaa", "cd", "bbaa", "dddd"]) == ["ab", "cd", "bbaa", "dddd"], "Test case 1 failed: Expected ['ab', 'cd', 'bbaa', 'dddd']"
    assert sorted_list_sum(["hello", "world", "in", "a", "frame"]) == ["in"], "Test case 2 failed: Expected ['in']"
    assert sorted_list_sum(["even", "odd", "evenly", "oddly", "neat", "clean"]) == ["clean", "even", "neat", "even"], "Test case 3 failed: Expected ['clean', 'even', 'neat', 'even']"
    assert sorted_list_sum([]) == [], "Test case 4 failed: Expected []"
    assert sorted_list_sum(["aa", "bb", "cc", "dd"]) == ["aa", "bb", "cc", "dd"], "Test case 5 failed: Expected ['aa', 'bb', 'cc', 'dd']"

if __name__ == "__main__": # pragma: no cover
    test_sorted_list_sum()
