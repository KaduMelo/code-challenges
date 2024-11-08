# 557. Reverse Words in a String III

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    return ' '.join(word[::-1] for word in s.split())

# Test case 1
s = "Let's take LeetCode contest"
output = "s'teL ekat edoCteeL tsetnoc"

result = reverseWords(s)

print(result)
print(result == output)

# Test case 2
s = "Mr Ding"
output = "rM gniD"

result = reverseWords(s)

print(result)
print(result == output)