a = set(input().split())
b = set(input().split())
inter = a & b
nums = []
for x in inter:
    nums.append(int(x))
nums.sort()
res = []
for x in nums:
    res.append(str(x))
print(" ".join(res))