# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    dict = {}

    for idx, char in enumerate(s):
        if not dict.get(char):
            dict[char] = [idx, 1]
        else:
            dict[char][1] += 1
    
    for ch, val in dict.items():
        if val[1] == 1:
            return val[0]
    
    return -1
            


# Test case 1
s = "loveleetcode"
print(firstUniqChar(s)) # Output 2

# Test case 2
s = "aabb"
print(firstUniqChar(s)) # Output -1

# Test case 2
s = "leetcode"
print(firstUniqChar(s)) # Output 0
    