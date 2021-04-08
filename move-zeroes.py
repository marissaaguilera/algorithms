
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


#Leetocde Problem: Move Zeroes 

def move_zeroes(nums):
    """Given an array of numbers move all the zeroes to the end."""

    for idx, num in enumerate(nums):
        if num == 0: 
            nums.pop(idx)
            nums.append(num)
    return nums

            # nums.insert(-1, num)
            # nums.pop(num.insert(-1, num))

print(move_zeroes([0,1,0,3,12])) #[1,3,12,0,0]
print(move_zeroes([5,4,0])) #[5,4,0]


#could use .remove as well 