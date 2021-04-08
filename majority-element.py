# 169. Majority Element
# Easy

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

#Leetcode Problem: Majority Element 


def majority_element(nums):
    """Given an array find the majority element."""

    nums.sort()

    majority_num = nums[len(nums)//2]

    return majority_num

print(majority_element([3,2,3])) #3
print(majority_element([2,2,1,1,1,2,2])) #2


#ATTEMPTS
    # majority_num = len(nums)//2
    # print(majority_num)
    # print(max(nums))

    # for num in nums:
    #     # print(max(num))
    #     # if num.count() > 1:
    #     if num/2 :
    #         print(num)