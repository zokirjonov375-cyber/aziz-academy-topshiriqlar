nums = []
for x in input().split():
    nums.append(int(x))
nums.sort()
n = len(nums)
print(nums[n // 2])