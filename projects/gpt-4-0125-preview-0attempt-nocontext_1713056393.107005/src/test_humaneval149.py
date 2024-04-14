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
    assert sorted_list_sum(["hello", "to", "world", "a", "bcd", "ae"]) == ["to", "ae", "bcd"], "Test case 1 failed"
    assert sorted_list_sum(["a", "ab", "abc", "abcd", "abcde", "abcdef"]) == ["ab", "abcd"], "Test case 2 failed"
    assert sorted_list_sum(["even", "odd", "evening", "morning", "day", "night", "noon"]) == ["even", "day", "night", "evening"], "Test case 3 failed"
    assert sorted_list_sum([]) == [], "Test case 4 failed"
    assert sorted_list_sum(["aa", "bbb", "cc", "dddd", "eeeee", "ffffff"]) == ["aa", "cc", "dddd", "ffffff"], "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_sorted_list_sum()
