"""
You're a hungry rabbit, and you already have eaten a certain number of carrots,
but now you need to eat more carrots to complete the day's meals.
you should return an array of [ total number of eaten carrots after your meals,
the number of carrots left after your meals ]
if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.

Example:
* eat(5, 6, 10) -> [11, 4]
* eat(4, 8, 9) -> [12, 1]
* eat(1, 10, 10) -> [11, 0]
* eat(2, 11, 5) -> [7, 0]

Variables:
@number : integer
the number of carrots that you have eaten.
@need : integer
the number of carrots that you need to eat.
@remaining : integer
the number of remaining carrots thet exist in stock

Constrain:
* 0 <= number <= 1000
* 0 <= need <= 1000
* 0 <= remaining <= 1000

Have fun :)
"""

def eat(number, need, remaining):
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]

def test_eat(): # pragma: no cover
    global eat
    # Test case when there are enough remaining carrots to satisfy the need
    assert eat(5, 6, 10) == [11, 4], "Test case 1 failed. Expected output did not match when there are more remaining carrots than needed."

    # Test case when the need is exactly equal to the remaining carrots
    assert eat(4, 8, 8) == [12, 0], "Test case 2 failed. Expected output did not match when the need equals the remaining carrots."

    # Test case when there are not enough remaining carrots to satisfy the need
    assert eat(1, 10, 5) == [6, 0], "Test case 3 failed. Expected output did not match when there are fewer remaining carrots than needed."

    # Test case when there are no remaining carrots
    assert eat(2, 5, 0) == [2, 0], "Test case 4 failed. Expected output did not match when there are no remaining carrots."

    # Test case when need is zero
    assert eat(10, 0, 5) == [10, 5], "Test case 5 failed. Expected output did not match when the need is zero."

    # Test with large numbers
    assert eat(500, 250, 750) == [750, 500], "Test case 6 failed. Expected output did not match with larger numbers."

if __name__ == "__main__": # pragma: no cover
    test_eat()
