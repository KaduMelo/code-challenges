# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.s

def prefix_common(words):

    if not words:
        return ""

    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""


    return prefix

# Test case 1
strs = ["flower","flow","flight"]
print(prefix_common(strs)) # Output: "fl"


# Test case 2
strs = ["dog","racecar","car"]
print(prefix_common(strs)) # Output: ""

