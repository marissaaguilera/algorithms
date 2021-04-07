# Given two strings s and t , write a function to determine 
# if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? 
# How would you adapt your solution to such case?

def valid_anagram(s, t):
    """Given two strings determine if it is an anagram."""

    s = sorted(list(s))
    t = sorted(list(t))

    return s == t

print(valid_anagram("anagram", "nagaram")) #True
print(valid_anagram("rat", "car")) #False
print(valid_anagram("restful", "fluster")) #True
