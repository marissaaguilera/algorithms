
# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.

# Follow up: If you have figured out the O(n) solution, 
# try coding another solution using the divide and conquer 
# approach, which is more subtle.



def max_subarray(nums):
    """Given an integer array nums, find the contiguous subarray ."""

    current_sum = 0
    largest_sum = 0 
    all_negatives = True 


    for num in nums:

        if num > 0: 
            all_negatives = False 

        if current_sum + num < 0:
            current_sum = 0 
        else:
            current_sum += num


        if current_sum > largest_sum:
            largest_sum = current_sum


    if all_negatives:
        largest_sum = max(nums)  
        #doing a check 
    

    return largest_sum

print(max_subarray([1])) #1
print(max_subarray([-1])) #-1
print(max_subarray([0])) #0
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) #6,  [4,-1,2,1]
print(max_subarray([8,9,-1,0])) #17


#subarray is anything from one number to the whole array 
#go from each end and check the highest sum 
# if one sum is bigger record that as the largest sum 
