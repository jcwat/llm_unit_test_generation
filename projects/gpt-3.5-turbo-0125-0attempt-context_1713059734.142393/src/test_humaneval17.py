""" Input to this function is a string representing musical notes in a special ASCII format.
Your task is to parse this string and return list of integers corresponding to how many beats does each
not last.

Here is a legend:
'o' - whole note, lasts four beats
'o|' - half note, lasts two beats
'.|' - quater note, lasts one beat

>>> parse_music('o o| .| o| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
"""
from typing import List


def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]

def test_parse_music(): # pragma: no cover
    global test_parse_music, List, parse_music
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4], "Test case 1 failed"
    assert parse_music('o .| o| o| .| o| .| o o| o') == [4, 1, 2, 2, 1, 4, 1, 4], "Test case 2 failed"
    assert parse_music('.| o .| o| .| o| o| .| o o') == [1, 4, 1, 2, 1, 4, 1, 4], "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_parse_music()
