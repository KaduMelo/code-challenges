# 917. Reverse Only Letters

# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

def reverseOnlyLetters(s):
    """
    :type s: str
    :rtype: str
    """
    
    s_list = list(s)
    left, right = 0, len(s_list) - 1

    while left < right:
        if not s_list[left].isalpha():
            left += 1
        elif not s_list[right].isalpha():
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        
    return ''.join(s_list)

# Test case 1
s = "ab-cd"
print(reverseOnlyLetters(s)) # Output "dc-ba"

# Test case 2
s = "a-bC-dEf-ghIj"
print(reverseOnlyLetters(s)) # Output "j-Ih-gfE-dCba"

# Test case 3
s = "Test1ng-Leet=code-Q!"
print(reverseOnlyLetters(s)) # Output "Qedo1ct-eeLg=ntse-T!"