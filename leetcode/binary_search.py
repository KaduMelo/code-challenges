# 704. Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    p_min = 0
    p_max = len(nums)

    while p_min < p_max:
        p_mid = int((p_max+p_min)/2)

        if nums[p_mid] == target:
            return p_mid
        elif nums[p_mid] < target:
            p_min = p_mid + 1
        else:
            p_max = p_mid
        
    return -1

# Test case 1
nums = [-1,0,3,5,9,12]
target = 9

print(search(nums, target)) # Output 4

# Test case 2
nums = [-1,0,3,5,9,12]
target = 2

print(search(nums, target)) # Output -1