

# Define a function max_of_three that takes in three numbers as 
# arguments and returns the largest of them.

# For example:

# >>> maxofthree(1, 5, 2)
# 5

# >>> maxofthree(10, 1, 11)
# 11
# We’ve given you a skeleton in maxofthree.py:

def max_of_three(num1, num2, num3):
    """Returns the largest of three integers"""

    numbers = []

    numbers.append(num1)
    numbers.append(num2)
    numbers.append(num3)

    return max(numbers)


print(max_of_three(1, 5, 2))
print(max_of_three(10, 1, 11))