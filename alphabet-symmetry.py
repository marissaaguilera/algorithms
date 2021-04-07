

# Consider the word "abode". We can see that the letter a is in position 1 and b
#  is in position 2. In the alphabet, a and b are also in positions 1 and 2. 
# Notice also that d and e in abode occupy the positions they would occupy in 
# the alphabet, which are positions 4 and 5.

# Given an array of words, return an array of the number of letters that 
# occupy their positions in the alphabet for each word. For example,

# solve(["abode","ABc","xyzD"]) = [4, 3, 1]
# See test cases for more examples.

# Input will consist of alphabet characters, both uppercase and lowercase. 
# No spaces.



def solve(arr):
    """Return an array of the number of letters that have alphabet symmetry."""

    alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 
                'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 
                'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 
                'w':23, 'x':24, 'y':25, 'z':26}

    new = []

    for string in arr:
        count = 0
        for position, letter in enumerate(string):
            letter = letter.lower()
            position = position +1

            if position == alphabet[letter]:
                count +=1
        new.append(count)
    return new


print(solve(["abode","ABc","xyzD"])) #,[4,3,1])))
print(solve(["abide","ABc","xyz"])) #,[4,3,0])))
print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"])) #,[6,5,7])))
print(solve(["encode","abc","xyzD","ABmD"])) #,[1, 3, 1, 3])))