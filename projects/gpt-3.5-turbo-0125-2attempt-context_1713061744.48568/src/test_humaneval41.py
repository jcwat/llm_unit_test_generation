"""
Imagine a road that's a perfectly straight infinitely long line.
n cars are driving left to right;  simultaneously, a different set of n cars
are driving right to left.   The two sets of cars start out being very far from
each other.  All cars move in the same speed.  Two cars are said to collide
when a car that's moving left to right hits a car that's moving right to left.
However, the cars are infinitely sturdy and strong; as a result, they continue moving
in their trajectory as if they did not collide.

This function outputs the number of such collisions.
"""


def car_race_collision(n: int):
    return n**2

def test_car_race_collision(): # pragma: no cover
    global test_car_race_collision
    assert car_race_collision(3) == 9, "Test case 1 failed"
    assert car_race_collision(5) == 25, "Test case 2 failed"
    assert car_race_collision(0) == 0, "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_car_race_collision()
