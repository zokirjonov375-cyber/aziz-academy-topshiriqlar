first = [int(x) for x in input().split()]
second = [int(x) for x in input().split()]
res = list({x for x in first if x in second})
res.sort()
print(res)