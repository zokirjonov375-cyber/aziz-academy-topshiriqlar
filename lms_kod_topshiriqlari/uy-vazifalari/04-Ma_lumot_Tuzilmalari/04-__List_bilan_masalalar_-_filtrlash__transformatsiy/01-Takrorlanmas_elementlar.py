nums = input().split()
seen = []
for x in nums:
    if x not in seen:
        seen.append(x)
print(" ".join(seen))