def numberOfSteps(num: int) -> int:
    steps = 0
    while num > 0:
        if num & 1:
            num-=1
        else:
            num>>=1
        steps+=1
    return steps

# Test case 1
num = 14
print(numberOfSteps(num)) # Output 6

# Test case 2
num = 8
print(numberOfSteps(num)) # Output 4

# Test case 3
num = 123
print(numberOfSteps(num)) # Output 12

