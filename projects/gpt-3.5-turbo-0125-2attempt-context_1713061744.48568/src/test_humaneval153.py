"""You will be given the name of a class (a string) and a list of extensions.
The extensions are to be used to load additional classes to the class. The
strength of the extension is as follows: Let CAP be the number of the uppercase
letters in the extension's name, and let SM be the number of lowercase letters 
in the extension's name, the strength is given by the fraction CAP - SM. 
You should find the strongest extension and return a string in this 
format: ClassName.StrongestExtensionName.
If there are two or more extensions with the same strength, you should
choose the one that comes first in the list.
For example, if you are given "Slices" as the class and a list of the
extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
(its strength is -1).
Example:
for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
"""

def Strongest_Extension(class_name, extensions):
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans


def test_Strongest_Extension(): # pragma: no cover
    global Strongest_Extension
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA', "Test case 1 failed"
    assert Strongest_Extension('Test', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Test.SErviNGSliCes', "Test case 2 failed"
    assert Strongest_Extension('ClassName', ['ExtensION', 'ExteND', 'AbC']) == 'ClassName.AbC', "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_Strongest_Extension()
