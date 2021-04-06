

# Write a function that translates english to pig latin.
# constant at the end 
# add ay at the end 
# if it already caps then it stays caps 

def pig_latin(string):
    """Given a string change the text to pig latin."""

    vowels = ['a', 'e', 'i', 'o', 'u'] # need to account for caps also 
    final  = ''
    result = ''


    for word in string.split():

        for idx, char in enumerate(word): 
            schar = ''

            
            if char.lower() in vowels: 
                # everything before that vowel is listed as a variable 
                last = word[:idx]
                first = word[idx:]
                if not word[-1].isalpha():
                    schar = word[-1]
                    # first = len(word) - word
                    first = word[idx:len(word) - 1] #length of word minus one 
                    #first = word[:-1]
                final = first + last + "ay" + schar
                # final[0] = final[0].upper()
                result += final + ' '
                break #need this break because there are multiple values, reassign final 


    return result.capitalize()


print(pig_latin("pig")) #igpay 
print(pig_latin("egg")) #eggay
print(pig_latin("Hello")) #Ellohay
print(pig_latin("Orange")) #Orangeay
print(pig_latin("Struck")) #Uckstray 
print(pig_latin("Hello world")) #Ellohay orldway - stuck here 
print(pig_latin("Hello, world.")) #Ellohay, orldway. - stuck here 


#if letter is cap then return cap else leave it lowercase 


# all constants before the first vowel get placed at the end 
# last two letters are "ay"


#pseudocode: 
# for loop through each letter 
# if statement checking if it is a constant or a vowel 

# special character 
# two words 
# caps 