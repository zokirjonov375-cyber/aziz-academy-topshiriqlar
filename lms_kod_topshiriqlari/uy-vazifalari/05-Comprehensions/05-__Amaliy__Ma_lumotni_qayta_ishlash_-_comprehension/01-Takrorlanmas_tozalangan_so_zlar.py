words = input().split()
res = list({w.lower() for w in words})
res.sort()
print(res)