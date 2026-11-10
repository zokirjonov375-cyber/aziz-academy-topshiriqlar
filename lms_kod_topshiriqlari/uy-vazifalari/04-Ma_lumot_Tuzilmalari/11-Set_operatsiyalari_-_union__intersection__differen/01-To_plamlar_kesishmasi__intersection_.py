a = set(input().split())
b = set(input().split())
u = a & b
nums = []
for x in u:
    nums.append(int(x))
nums.sort()
res = []
for x in nums:
    res.append(str(x))
print(" ".join(res))