nums = input().split()
i = 0
while i + 1 < len(nums):
    nums[ i ], nums[i + 1] = nums[i + 1],nums[i]
    i += 2
print(" ".join(nums))