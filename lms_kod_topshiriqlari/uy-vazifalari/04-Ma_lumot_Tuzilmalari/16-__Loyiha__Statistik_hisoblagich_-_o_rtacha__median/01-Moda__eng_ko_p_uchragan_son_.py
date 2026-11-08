nums = []
for x in input().split():
    nums.append(int(x))
counts = {}
for x in nums:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1
best = nums[0]
best_count = 0
for num in counts:
    if counts[num] > best_count:
        best_count = counts[num]
        best = num
print(best)