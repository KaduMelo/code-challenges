# 557. Reverse Words in a String III

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords(s):
    res = ''
    l, r = 0, 0

    while r < len(s):
        if s[r] != ' ':
            r += 1
        else:
            res += s[l:r+1][::-1]
            r += 1
            l = r

    res += ' '
    res += s[l:r + 2][::-1]
    return res[1:]

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