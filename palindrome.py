
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

def valid_palindrome(message):
    """Determine a palindrome."""

    m = "".join(message.split()).lower() #original joined message
    rev = "".join(m[::-1]).lower() #reversed/joined message

    if rev == m: 
        return True 

    else: 
        return False 

#TODO - fix this so that the syntax ignores if there is a special character 
    # special_chars = [',', '.', '/', ':', ';', '>', '<', '[', ']']

    # for char in special_chars:
    #     if char in m and char in rev:
    #         print(char)
    #         pass 

# print(valid_palindrome("A man, a plan, a canal: Panama")) #True
print(valid_palindrome("A man a plan a canal Panama")) #True
print(valid_palindrome("race a car")) #False
