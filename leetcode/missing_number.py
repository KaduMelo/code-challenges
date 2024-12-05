def missingNumber(nums):
    x = 0

    for num in nums:
        x ^= num
    for i in range(len(nums)+1):
        x ^= i

    return x

nums = [3,0,1]
print(missingNumber(nums))

nums = [0,1]
print(missingNumber(nums))

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))