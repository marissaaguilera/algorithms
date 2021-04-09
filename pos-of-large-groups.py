
# In a string s of lowercase letters, these letters form consecutive 
# groups of the same character.

# For example, a string like s = "abbxxxxzyy" has the groups 
# "a", "bb", "xxxx", "z", and "yy".

# A group is identified by an interval [start, end], where start and 
# end denote the start and end indices (inclusive) of the group. 
# In the above example, "xxxx" has the interval [3,6].

# A group is considered large if it has 3 or more characters.

# Return the intervals of every large group sorted in 
# increasing order by start index.

 


def large_groups(s):
    """Return the intervals of every large group by start index."""

    interval = []

    for i in range(len(s)):
        if s[i] == s[i+1]:
            print(i) 

    # for idx, letter in enumerate(s):
    #     if idx +1 == letter: #letters have to be consecutive 
    #     # if s.count(letter) >= 3 and idx +1 == letter: #letters have to be consecutive 
    #         print(letter)




print(large_groups("abbxxxxzzy")) #[[3,6]]
print(large_groups("abc")) #[]
print(large_groups("abcdddeeeeaabbbcd")) #[[3,5],[6,9],[12,14]]
print(large_groups("aba")) #[]