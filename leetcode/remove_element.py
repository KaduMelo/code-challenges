# 27. Remove Element

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    k = len(nums) - nums.count(val)
    nums[:] = [num for num in nums if num != val]

    return k
    



# Test case 1
nums = [3,2,2,3]
val = 3

k = removeElement(nums, val)
print(k)  # Output should be 2
print(nums)  # Output should be [2,2]

# Test case 2
nums = [0,1,2,2,3,0,4,2]
val = 2

k = removeElement(nums, val)
print(k)  # Output should be 5
print(nums)  # Output should be [0,1,3,0,4]