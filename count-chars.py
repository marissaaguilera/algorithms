#Count characters in your string 

# The main idea is to count all the occurring characters in a string. 
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):
    """Count characters in a string to add to a dictionary."""

    library = {}

    for char in string: 
        count = string.count(char)
        library[char] = count
    return library
print(count('aba')) #, {'a': 2, 'b': 1})
print(count('')) #, {})
print(count('Marissa')) #, {'a': 2, 'i': 1, 'm': 1, 'r':1, 's':2})