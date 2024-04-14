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
    # Test with correct input in direct order
    assert bf("Mercury", "Venus") == (), "Test case 1 failed"
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus"), "Test case 2 failed"
    assert bf("Earth", "Mars") == (), "Test case 3 failed"

    # Test with correct input in reverse order
    assert bf("Venus", "Mercury") == (), "Test case 4 failed"
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus"), "Test case 5 failed"
    assert bf("Mars", "Earth") == (), "Test case 6 failed"

    # Test with the full range
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"), "Test case 7 failed"

    # Test incorrect or equal planet names
    assert bf("Pluto", "Earth") == (), "Test case 8 failed, expected empty tuple for incorrect planet name"
    assert bf("Earth", "Earth") == (), "Test case 9 failed, expected empty tuple for equal planet names"
    assert bf("Mercury", "Pluto") == (), "Test case 10 failed, expected empty tuple for incorrect planet name"

if __name__ == "__main__": # pragma: no cover
    test_bf()
