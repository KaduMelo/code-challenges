# 3090. Maximum Length Substring With Two Occurrences

# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.

def maximumLengthSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    l, r = 0, 0
    _max = 1
    counter ={}

    counter[s[0]] = 1

    while r < len(s) - 1:
        r += 1
        if counter.get(s[r]):
            counter[s[r]] += 1
        else:
            counter[s[r]] = 1
        
        while counter[s[r]] == 3:
            counter[s[l]] -= 1
            l += 1

        _max = max(_max, r - l + 1)

    return _max 


# Test case 1
s = "bcbbbcba"
print(maximumLengthSubstring(s))  # Output: 4

# Test case 2
s = "aaaa"
print(maximumLengthSubstring(s))  # Output: 2