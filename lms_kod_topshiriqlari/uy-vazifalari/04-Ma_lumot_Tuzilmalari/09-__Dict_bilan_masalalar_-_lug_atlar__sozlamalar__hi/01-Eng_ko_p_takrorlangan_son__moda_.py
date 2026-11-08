nums = input().split()
freq = {}
for x in nums:
    num = int(x)
    freq[num] = freq.get(num, 0) + 1
best = None
best_count = -1
for num in sorted(freq):
    if freq[num] > best_count:
        best_count = freq[num]
        best = num
print(best)        