


# 415. Add Strings

# Given two non-negative integers num1 and num2 represented as a string, 
# return the sum of num1 and num2.

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert 
# the inputs to integer directly.

def add_strings(str1, str2):
    """Given two integers as a string return the sum of both integers."""

    s1 = list(str1)
    s2 = list(str2)
    
    s1_index = len(s1) -1
    s2_index = len(s2) -1

    result = 0
    multiple = 1
    
    
    if s1[0] == "0" or s2[0] == "0":
        return None 

    while s1_index >= 0 or s2_index >= 0:

        if s1_index >= 0 and not s1[s1_index].isdigit():
            return None

        if s2_index >= 0 and not s2[s2_index].isdigit():
            return None 


        last_s1 = int(s1[s1_index]) if s1_index >= 0 else 0
        last_s2 = int(s2[s2_index]) if s2_index >= 0 else 0

        digit = last_s1 + last_s2

        result += digit * multiple
        multiple *= 10
    
        s1_index = s1_index -1 
        s2_index = s2_index -1


    return str(result)

#convert to a string last 

print(add_strings("789", "100")) #889
print(add_strings("8", "6a9")) #None
print(add_strings("05", "12")) #None
print(add_strings("7", "3")) #10
print(add_strings("7000", "3")) #7003

