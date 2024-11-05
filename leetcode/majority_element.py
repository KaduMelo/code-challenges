# counts = {2: 4, 1: 3, 12: 1}

# # Find the key with the maximum value in the dictionary
# major_element = max(counts, key=counts.get)

# print(major_element)  # Output: 2


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

nums = [3,2,3]
print(majorityElement(nums))