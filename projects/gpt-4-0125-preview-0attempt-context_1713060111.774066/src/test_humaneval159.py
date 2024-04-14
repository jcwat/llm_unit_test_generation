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
    # Test case 1: Enough carrots remaining
    assert eat(5, 6, 10) == [11, 4], "Test case 1 failed: Expected [11, 4]"
    
    # Test case 2: Need more than remaining
    assert eat(4, 8, 9) == [12, 1], "Test case 2 failed: Expected [12, 1]"
    
    # Test case 3: Eating all remaining exactly matches need
    assert eat(1, 10, 10) == [11, 0], "Test case 3 failed: Expected [11, 0]"
    
    # Test case 4: Not enough carrots to meet the need
    assert eat(2, 11, 5) == [7, 0], "Test case 4 failed: Expected [7, 0]"
    
    # Test case 5: Zero case scenario
    assert eat(0, 0, 0) == [0, 0], "Test case 5 failed: Expected [0, 0]"

if __name__ == "__main__": # pragma: no cover
    test_eat()
