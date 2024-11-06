def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    major_element = max(counts, key=counts.get)
    return major_element

# Test case 1
nums = [3,2,3]
print(majorityElement(nums)) # Output 3

# Test case 2
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums)) # Output 2