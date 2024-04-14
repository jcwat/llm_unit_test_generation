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
    global car_race_collision

    # Test for n = 0
    assert car_race_collision(0) == 0, "Failed for n = 0"

    # Test for n = 1
    assert car_race_collision(1) == 1, "Failed for n = 1"

    # Test for n = 5
    assert car_race_collision(5) == 25, "Failed for n = 5"
    
    # Test for n = 10
    assert car_race_collision(10) == 100, "Failed for n = 10"

if __name__ == "__main__": # pragma: no cover
    test_car_race_collision()
