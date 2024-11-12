def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    d = {}
    
    for i in range(len(nums)):
       if nums[i] in d and i - d[nums[i]] <= k:
          return True
       d[nums[i]] = i

    return False

# Test case 1
nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k)) # Output: true

# Test case 2
nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums, k)) # Output: true

# Test case 3
nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k)) # Output: false