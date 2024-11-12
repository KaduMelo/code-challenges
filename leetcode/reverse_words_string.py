# 151. Reverse Words in a String

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    return " ".join(reversed(s.split()))

# Test case 1
s = "the sky is blue"
print(reverseWords(s)) # Output "blue is sky the"

# Test case 2
s = "  hello world  "
print(reverseWords(s)) # Output "world hello"

# Test case 3
s = "a good   example"
print(reverseWords(s)) # Output "example good a"