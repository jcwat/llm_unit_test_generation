""" Input is a space-delimited string of numberals from 'zero' to 'nine'.
Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
Return the string with numbers sorted from smallest to largest
>>> sort_numbers('three one five')
'one three five'
"""
from typing import List


def sort_numbers(numbers: str) -> str:
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))

def test_sort_numbers(): # pragma: no cover
    global test_sort_numbers, sorted
    assert sort_numbers('three one five') == 'one three five', "Test case 1 failed"
    assert sort_numbers('nine eight seven') == 'seven eight nine', "Test case 2 failed"
    assert sort_numbers('two four six eight') == 'two four six eight', "Test case 3 failed"
    assert sort_numbers('') == '', "Test case 4 failed"
    assert sort_numbers('zero nine five two') == 'zero two five nine', "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_sort_numbers()
