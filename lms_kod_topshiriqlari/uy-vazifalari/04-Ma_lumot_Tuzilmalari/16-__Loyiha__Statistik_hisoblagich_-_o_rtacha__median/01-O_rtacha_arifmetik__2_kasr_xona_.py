nums = []
for x in input().split():
    nums.append(int(x))
total = 0
for x in nums:
    total += x
print(round(total / len(nums), 2))