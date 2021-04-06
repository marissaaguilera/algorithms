
# The word i18n is a common abbreviation of internationalization 
# in the developer community, used instead of typing the whole 
# word and trying to spell it correctly. Similarly, a11y is an 
# abbreviation of accessibility.

# Write a function that takes a string and turns any and all 
# "words" (see below) within that string of length 4 or greater 
# into an abbreviation, following these rules:

# A "word" is a sequence of alphabetical characters. By this
#  definition, any other character like a space or hyphen 
# (eg. "elephant-ride") will split up a series of letters into 
# two words (eg. "elephant" and "ride").
# The abbreviated version of the word should have the first 
# letter, then the number of removed characters, then the last 
# letter (eg. "elephant ride" => "e6t r2e").


def abbreviation(string):
    """Given a string return an abbreviation."""

    s = string.split(" ")

    count = 0 

    for word in s: 
        first = word[0]
        last = word[-1]
        l = len(word)

        if l >= 4:
            print(word)

        else:
            print(word)

# final = - first - last
# return final 


print(abbreviation("elephant-rides are really fun!")) # "e6t-r3s are r4y fun!"
print(abbreviation("internationalization")) # "i18n"
print(abbreviation("accessibility")) # "a11y"
print(abbreviation("elephant-ride")) # "e6t-r2e"