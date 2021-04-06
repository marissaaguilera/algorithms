

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

def two_sum(lst, target):
    """Given an array and an integer return the indices of two numbers that sum is the target."""

    indices = []

    for idx, number in enumerate(lst):
        number2 = target - number
        number1 = target - number2
        if number1 in lst and number2 in lst:
            indices.append(idx)
            # print(idx)
    return indices


print(two_sum([2,7,11,15], 9)) #[0,1]
print(two_sum([3,2,4], 6)) #[1,2]
print(two_sum([3,3], 6)) #[0,1]
print(two_sum([7,4,5,2,7], 14)) #[0,4]
print(two_sum([7,4,5,4,7], 8)) #[1,3]