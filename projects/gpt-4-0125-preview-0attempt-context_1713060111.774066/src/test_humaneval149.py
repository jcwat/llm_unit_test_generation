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
    assert sorted_list_sum(["banana", "apple", "pear", "fig"]) == ["fig", "pear", "banana"], "Test case 1 failed"
    assert sorted_list_sum(["dog", "wolf", "cat", "mouse", "fly"]) == ["dog", "cat", "wolf", "mouse"], "Test case 2 failed"
    assert sorted_list_sum(["one", "two", "three", "four", "five", "six"]) == ["two", "four", "six"], "Test case 3 failed"
    assert sorted_list_sum([]) == [], "Test case 4 failed"
    assert sorted_list_sum(["a", "bb", "ccc", "dddd"]) == ["bb", "dddd"], "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_sorted_list_sum()
