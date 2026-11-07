a = set(input().split())
b = set(input().split())
c = set(input().split())
u = a & b & c
nums = []
for x in u:
    nums.append(int(x))
nums.sort()
res = []
for x in nums:
    res.append(str(x))
print(" ".join(res))