# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

#HackerRank Problem: Swap Case 

def swap_case(string):
    """Covert lowercase letters to uppercase and vice versa."""

    new_string = ""

    for char in string: 
        if char == char.upper():
            char = char.lower()
            new_string += char
            # print(new_string)
            # print("upper to lower", char)

        elif char == char.lower():
            char = char.upper()
            new_string += char
    return new_string
         # print("lower", char)
#special characters 


print(swap_case("Www.HackerRank.com")) #wWW.hACKERrANK.COM
print(swap_case("Pythonist 2")) #pYTHONIST 2
