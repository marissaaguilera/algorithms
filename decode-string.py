

# In this challenge, you’ll write a decoder.

# A valid code is a sequence of numbers and letters, always starting with a number 
# and ending with letter(s).

# Each number tells you how many characters to skip before finding a good letter. 
# After each good letter should come the next next number.

# For example, the string “hey” could be encoded by “0h1ae2bcy”. This means “skip 0, find the ‘h’, skip 1, find the ‘e’, skip 2, find the ‘y’”.

# A single letter should work:

# >>> decode("0h")
# 'h'

# >>> decode("2abh")
# 'h'
# Longer patterns should work:

# >>> decode("0h1ae2bcy")
# 'hey'
# We’ve provided a file, decode.py, with a stub function in it:



def decode(s):
    """Decode a string."""



    word = ""

    i = 0

    while i < len(s):

        num_to_skip = int(s[i])
        i += num_to_skip + 1

        word += s[i]

        i += 1

    return word


    # m = ""

    # for char in s:
    #     if char.isdigit():
    #         move = char
    #         print(move)
    #     else:






print(decode("0h")) #h
print(decode("2abh")) #h
print(decode("0h1ae2bcy")) #hey