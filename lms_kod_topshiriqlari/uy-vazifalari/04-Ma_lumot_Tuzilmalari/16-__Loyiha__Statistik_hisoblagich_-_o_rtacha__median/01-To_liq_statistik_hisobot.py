nums = []
for x in input().split():
    nums.append(int(x))
n = len(nums)
total = 0
for x in nums:
    total += x
mean = round(total / n, 2)
s = sorted(nums)
if n % 2 == 1:
    median = s[n // 2]
else:
    median = (s[n // 2 - 1] + s[n // 2]) // 2
counts = {}
for x in nums:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1
best = None
best_count = -1
for num in sorted(counts):
    if counts[num] > best_count:
        best_count = counts[num]
        best = num
print("O'rtacha:", mean)
print("Mediana:", median)
print("Moda:", best)
        
        
        