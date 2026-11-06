words = input().split()
res = list({len(w) for w in words})
res.sort()
print(res)