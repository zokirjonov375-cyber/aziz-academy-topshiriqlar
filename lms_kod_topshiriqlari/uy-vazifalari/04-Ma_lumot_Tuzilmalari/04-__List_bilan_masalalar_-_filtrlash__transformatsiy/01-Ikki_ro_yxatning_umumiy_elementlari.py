a = input().split()
b = input().split()
res = []
for x in a:
    if x in b and x not in res:
        res.append(x)
print(" ".join(res))