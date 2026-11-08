nums = input().split()
v= input().strip()
c = 0
for x in nums:
    if x == v:
        c += 1
print(c)