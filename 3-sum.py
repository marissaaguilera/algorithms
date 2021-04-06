# Given an array nums of n integers, are there elements a, b, c in 
# nums such that a + b + c = 0? Find all unique triplets in the 
# array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []

def three_sum(nums):
    """Given an array return the numbers that sum equal to zero."""

    count = 0 

    for i in range(len(nums)):
        sum = nums[i] + nums[i] + nums[i]
        if sum == 0:
            print(nums[i])




print(three_sum([-1,0,1,2,-1,-4])) #[[-1,-1,2],[-1,0,1]]
print(three_sum([])) #[]
print(three_sum([0])) #[]
