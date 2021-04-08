

# Modify the kebabize function so that it converts a camel 
# case string into a kebab case.

# kebabize('camelsHaveThreeHumps') // camels-have-three-humps
# kebabize('camelsHave3Humps') // camels-have-h



def kebabize(string):
    """Given a string in camel case convert it to kebab case."""

    result = ""

    for char in string: 
        if char.isupper():
            if result is not "":
                result += "-{}".format(char.lower())
            else:
                result += char.lower()
        if char.islower():
            result += char
    return result


print(kebabize('camelsHaveThreeHumps')) #camels-have-three-humps
print(kebabize('piratesOfTheCarribean')) #pirates-of-the-carribean
print(kebabize('camelsHave3Humps')) #camels-have-h