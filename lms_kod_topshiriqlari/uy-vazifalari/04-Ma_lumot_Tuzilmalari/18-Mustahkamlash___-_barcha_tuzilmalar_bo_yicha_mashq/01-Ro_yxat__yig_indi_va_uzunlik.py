nums = []
for x in input().split():
    nums.append(int(x))
total = 0
for x in nums:
    total += x
print(total, len(nums))