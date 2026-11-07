nums = input().split()
s = 0
for i in range(len(nums)):
    if i % 2 == 0:
        s += int(nums[i])
print(s)
