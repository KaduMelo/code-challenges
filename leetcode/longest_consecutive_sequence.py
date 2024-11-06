# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    num_set = set(nums)
    longest_streak = 0

    for num in nums:

        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Test case 1
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums)) # Output: 4

# Test case 2
nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums)) # Output: 9