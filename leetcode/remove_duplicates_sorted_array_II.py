# 80. Remove Duplicates from Sorted Array II

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums):

    max_count = 2
    hasher = {}
    new_nums = []

    for idx, num in enumerate(nums):
        if hasher.get(num) is None or hasher.get(num) < max_count:
            if num in hasher:
                hasher[num] += 1
            else:
                hasher[num] = 1
            new_nums.insert(idx, num)


    nums[:] = new_nums
    nums.sort()
    return len(nums)

# Teste case 1
nums = [1,1,2]
print(removeDuplicates(nums)) # Output: 2, nums = [1,2,_]
print(nums)

# Teste case 2
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums)) # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
print(nums)