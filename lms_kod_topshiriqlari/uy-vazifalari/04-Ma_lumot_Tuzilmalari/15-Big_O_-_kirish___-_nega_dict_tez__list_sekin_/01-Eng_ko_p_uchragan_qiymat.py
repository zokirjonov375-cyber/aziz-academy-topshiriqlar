nums = input().split()
counts = {}
for x in nums:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1
best = None
best_c = 0
for x in counts:
    if counts[x] > best_c:
        best_c = counts[x]
        best = x
print(best)