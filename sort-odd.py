

# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers 
# must be on their places.

# Zero isn't an odd number and you don't need to move it. 
# If you have an empty array, you need to return it.

#Codewars Problem: Sort the odd


def sort_odd(nums):
    """Given an array of numbers sort only the odd numbers."""

    o = []
    x = 0

    for num in nums: 
        if num % 2 != 0:
            o.append(num)
    o.sort()
    # print(o)

    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            nums[i] = o[x]
            x += 1
    return nums


print(sort_odd([5, 3, 2, 8, 1, 4])) #, [1, 3, 2, 8, 5, 4])
print(sort_odd([5, 3, 1, 8, 0])) #, [1, 3, 5, 8, 0])
print(sort_odd([])) #,[])
