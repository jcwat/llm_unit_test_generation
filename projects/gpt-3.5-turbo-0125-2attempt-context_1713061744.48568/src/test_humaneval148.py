'''
There are eight planets in our solar system: the closerst to the Sun 
is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
Uranus, Neptune.
Write a function that takes two planet names as strings planet1 and planet2. 
The function should return a tuple containing all planets whose orbits are 
located between the orbit of planet1 and the orbit of planet2, sorted by 
the proximity to the sun. 
The function should return an empty tuple if planet1 or planet2
are not correct planet names. 
Examples
bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
bf("Earth", "Mercury") ==> ("Venus")
bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
'''

def bf(planet1, planet2):
    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    if planet1_index < planet2_index:
        return (planet_names[planet1_index + 1: planet2_index])
    else:
        return (planet_names[planet2_index + 1 : planet1_index])

def test_bf(): # pragma: no cover
    global bf
    
    planets = bf("Jupiter", "Neptune")
    assert planets == ("Saturn", "Uranus"), "Test case 1 failed"
    
    planets = bf("Earth", "Mercury")
    assert planets == ("Venus",), "Test case 2 failed"
    
    planets = bf("Mercury", "Uranus")
    assert planets == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Test case 3 failed"
    
    planets = bf("Invalid", "Neptune")
    assert planets == (), "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_bf()
