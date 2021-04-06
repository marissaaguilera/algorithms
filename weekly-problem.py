
#This file has the weekly wednesday HB problems

#11/18 

####################################################################

#1. Max Number 

def max_num(num_list):
    """Returns largest integer from given list"""

    return max(num_list)

print(max_num([5, 3, 6, 2, 1])) #6



#2. Count List Recursively 

def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    if lst == []:
        return 0
    
    return 1 + count_recursively(lst[1:])

print(count_recursively([])) #0
print(count_recursively([1, 2, 3])) #3



#3. Reverse Linked List 

# class Node(object):
#     """Class in a linked list."""

#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

#     def as_string(self):
#         """Represent data for this node and it's successors as a string.

#         Node(3).as_string()
#         '3'

#         Node(3, Node(2, Node(1))).as_string()
#         '321'
#         """

#         out = []
#         n = self

#         while n:
#             out.append(str(n.data))
#             n = n.next

#         return "".join(out)
    
#     def reverse_linked_list(head):
#         """Given LL head node, return head node of new, reversed linked list."""

#     # ll = Node(1, Node(2, Node(3)))
#     # reverse_linked_list(ll).as_string()
#     # '321'

#     ll = Node(1, Node(2, Node(3)))
#     new_ll = reverse_linked_list(ll)
#     new_ll.as_string() #'321'

####################################################################

#12/15 

#1. Balanced Parenthesis


# Given a string, return True or False depending on whether that string has balanced parentheses.

# For the purposes of this problem, you only need to worry about 
# parentheses (( and )), not other opening-and-closing marks, like curly brackets, 
# square brackets, or angle brackets.


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

#     result = False

#     open_count = 0
#     close_count = 0

#     for char in phrase:
#         if char == "(":
#             open_count += 1

#         if char == ")":
#             close_count += 1
    
#         if open_count < close_count:
#             return result 


#     if open_count == close_count:
#         result = True

        
# #open has to come first 
#     return result

        # pair = "()"

        # if char == "(": #no open parenthesis then false
# (  ) (

# )(
    #for every open parenthesis there has to be a closed parenthesis 


    parenthesis = []
    result = True

    for char in phrase:
        if char == "(":
            parenthesis.append(char)
        if char == ")" and len(parenthesis) < 1: #seeing a closed before an open 
            result = False
        if char == ")" and len(parenthesis) >= 1:
            parenthesis.pop()
    

    if len(parenthesis) == 0:
        return result 

    else: 
        result = False 
    return result
    
print(has_balanced_parens("()")) #True
print(has_balanced_parens("(Oh Noes!)(")) #False
print(has_balanced_parens("((There's a bonus open paren here.)")) #False
print(has_balanced_parens(")")) #False
print(has_balanced_parens("(")) #False
print(has_balanced_parens("(This has (too many closes.) ) )")) #False
print(has_balanced_parens(")(")) #False





# def spiral(matrix_size):
#     """Spiral coordinates of a matrix of `matrix_size` size."""


####################################################################


# Write a function, find_longest_word, that takes a list of words and returns the 
# length of the longest one.

# >>> find_longest_word(["hi", "hello"])
# 5

# >>> find_longest_word(["Balloonicorn", "Hackbright"])
# 12
# We’ve given you longest-word.py, which includes the stub of a find_longest_word function:

# longest-word.py
def find_longest_word(words):
    """Return longest word in list of words."""
    
    # lengths = []

    # for word in words: 
    #     l = len(word)
    #     lengths.append(l)
    #     result = max(lengths)
    # return result

    #ALT SOLUTION ONE LINE 
    return len(max(words, key=lambda words: len(words)))

print(find_longest_word(["hi", "hello"]))# 5
print(find_longest_word(["Balloonicorn", "Hackbright"])) # 12



# Count the number of items in a list, using recursion.

# For example:

# >>> count_recursively([])
# 0

# >>> count_recursively([1, 2, 3])
# 3
# We’ve written a file, countrecursively.py, with a function, count_recursively:

def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    if len(lst) == 0: 
        return 0
    else: 
        return 1 + count_recursively(lst[1:])

print(count_recursively([])) # 0
print(count_recursively([1, 2, 3])) # 3


# 01/20 weekly problems 

def primes(count):
    """Return count number of prime numbers, starting at 2."""

    prime_numbers = [2]
    next_num = 3 

    def is_prime(next_num):
        if next_num % 2 == 0:
            return False 
        
        for i in range(3, next_num, 2):
            if next_num % i == 0:
                return False 
        return True 

    while count > len(prime_numbers): 
        if is_prime(next_num): 
            prime_numbers.append(next_num)
        next_num += 1

    return prime_numbers
     

print(primes(1)) #[2]
print(primes(5))#[2, 3, 5, 7, 11]






# def can_win(n):
#     """Can this player win takeaway?"""

#     # 2, 3, 5 stones/moves from the pool 
#     moves = [2, 3, 5]
#     result = False
    
#     #cant move return false 
#     if n <2:
#         return result 

#     for move in moves: 
#         # if we win and opponent cant mat win with the move made result = True 
#         if not can_win(n-move):
#             result = True
#             return result
#     return result 
#         #else return result 

# print(can_win(1)) #False
# print(can_win(2)) #True
# print(can_win(3)) #True
# print(can_win(4)) #True
# print(can_win(5)) #True
# print(can_win(6)) #True
# print(can_win(7)) #False
# print(can_win(8)) #False
# print(can_win(9)) #True
# print(can_win(10)) #True 